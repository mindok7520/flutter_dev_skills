"""Verify portable task packets, required inputs, and filesystem boundaries."""

from contextlib import redirect_stderr, redirect_stdout
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from scripts.install import SOURCE_ROOT, apply_plan, build_plan
from scripts.task_context import build_packet, main, project_path


class TaskContextTests(unittest.TestCase):
    def test_packet_records_requested_checks_without_claiming_execution(self):
        packet = build_packet(SOURCE_ROOT, '08', 'Fix the reported failure',
                              ['The reproduction succeeds'], ['scripts/install.py'],
                              ['python -m unittest discover -s tests'])
        self.assertIn('prompts/08-fix-bug.md', packet)
        self.assertIn('scripts/install.py', packet)
        self.assertIn('not executed results', packet)
        self.assertNotIn('import argparse', packet)
        self.assertNotIn('prompts/32-payment-integration.md', packet)

    def test_required_inputs_and_bounded_scope_are_enforced(self):
        for task, accept, files, checks in [
            ('99', ['Done'], [], ['Inspect']), ('08', [], [], ['Inspect']),
            ('08', ['Done'], [], []), ('08', ['Done'], ['AGENTS.md'] * 13, ['Inspect']),
        ]:
            with self.subTest(task=task, files=len(files)):
                with self.assertRaises(ValueError):
                    build_packet(SOURCE_ROOT, task, 'Goal', accept, files, checks)
        with self.assertRaisesRegex(ValueError, 'single lines'):
            build_packet(SOURCE_ROOT, '08', 'Goal\nInjected section', ['Done'], [], ['Inspect'])

    def test_paths_reject_escape_missing_files_and_absolute_windows_paths(self):
        for value in ['../outside', '/outside', 'C:/outside', 'C:outside', 'missing.md', 'docs/../README.md']:
            with self.subTest(path=value):
                with self.assertRaises(ValueError):
                    project_path(SOURCE_ROOT, value)

    def test_installed_generator_runs_without_material_repository_dependencies(self):
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary).resolve()
            (target / 'pubspec.yaml').write_text('name: product\n', encoding='utf-8')
            apply_plan(build_plan(SOURCE_ROOT, target), target)
            result = subprocess.run(
                [sys.executable, '-I', '.agents/task_context.py', '--task', '07', '--goal',
                 'Implement the approved feature', '--accept', 'Saved state survives restart',
                 '--file', 'PROJECT.md', '--check', 'flutter test'],
                cwd=target, capture_output=True, encoding='utf-8', timeout=15,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn('prompts/07-implement-feature.md', result.stdout)
            self.assertNotIn(str(SOURCE_ROOT), result.stdout)

    def test_output_never_overwrites_an_existing_file(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary).resolve()
            (root / 'pubspec.yaml').write_text('name: product\n', encoding='utf-8')
            apply_plan(build_plan(SOURCE_ROOT, root), root)
            output = root / 'task.md'
            output.write_text('Keep this content', encoding='utf-8')
            with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                code = main(['--root', str(root), '--task', '08', '--goal', 'Fix failure',
                             '--accept', 'Recovered', '--check', 'Manual reproduction', '--output', 'task.md'])
            self.assertEqual(code, 1)
            self.assertEqual(output.read_text(encoding='utf-8'), 'Keep this content')


if __name__ == '__main__':
    unittest.main()

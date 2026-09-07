"""Exercise collisions, idempotency, and safe installation boundaries."""

from pathlib import Path
import os
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from scripts.install import SOURCE_ROOT, apply_plan, build_plan, destination_for


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.target = Path(self.temporary.name).resolve() / 'app'
        self.target.mkdir()
        (self.target / 'pubspec.yaml').write_text('name: existing_product\n', encoding='utf-8')

    def test_preview_does_not_write_or_select_application_configuration(self):
        plan = build_plan(SOURCE_ROOT, self.target)
        destinations = {entry.destination.relative_to(self.target).as_posix() for entry in plan}
        self.assertIn('AGENTS.md', destinations)
        self.assertIn('PROJECT.md', destinations)
        self.assertIn('docs/design/DESIGN_WORKFLOW.md', destinations)
        self.assertIn('docs/performance/SHADER_GUIDE.md', destinations)
        self.assertIn('.agents/skills/ui-design/agents/openai.yaml', destinations)
        self.assertIn('.agents/skills/shaders/SKILL.md', destinations)
        self.assertIn('prompts/61-component-catalog.md', destinations)
        self.assertIn('docs/references/repositories.json', destinations)
        self.assertNotIn('pubspec.yaml', destinations)
        self.assertNotIn('LICENSE', destinations)
        self.assertNotIn('.github/workflows/ci.yml', destinations)
        self.assertEqual(list(self.target.iterdir()), [self.target / 'pubspec.yaml'])

    def test_collision_aborts_before_copying_any_file(self):
        (self.target / 'AGENTS.md').write_text('Existing project instructions', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'Existing files differ'):
            build_plan(SOURCE_ROOT, self.target)
        self.assertEqual((self.target / 'AGENTS.md').read_text(), 'Existing project instructions')
        self.assertFalse((self.target / 'docs').exists())

    def test_installation_is_idempotent_and_preserves_manifest(self):
        before = (self.target / 'pubspec.yaml').read_bytes()
        plan = build_plan(SOURCE_ROOT, self.target)
        self.assertGreater(apply_plan(plan, self.target), 100)
        repeated = build_plan(SOURCE_ROOT, self.target)
        self.assertTrue(all(entry.identical for entry in repeated))
        self.assertEqual(apply_plan(repeated, self.target), 0)
        self.assertEqual((self.target / 'pubspec.yaml').read_bytes(), before)
        self.assertFalse((self.target / 'lib').exists())

    def test_target_must_exist_and_not_overlap_the_source(self):
        with self.assertRaises(ValueError):
            build_plan(SOURCE_ROOT, SOURCE_ROOT)
        with self.assertRaises(ValueError):
            build_plan(SOURCE_ROOT, SOURCE_ROOT.parent)
        with self.assertRaises(ValueError):
            destination_for(self.target, Path('../outside.md'))

    def test_ci_requires_tooling_and_uses_application_workflows(self):
        with self.assertRaisesRegex(ValueError, 'requires --with-tooling'):
            build_plan(SOURCE_ROOT, self.target, with_ci=True)
        with self.assertRaisesRegex(ValueError, 'requires the target SDK version'):
            build_plan(SOURCE_ROOT, self.target, with_tooling=True, with_ci=True)
        (self.target / '.fvmrc').write_text('{"flutter": "3.47.2"}', encoding='utf-8')
        plan = build_plan(SOURCE_ROOT, self.target, with_tooling=True, with_ci=True)
        ci = next(entry for entry in plan if entry.destination == self.target / '.github/workflows/ci.yml')
        self.assertIn('templates/flutter', ci.source.as_posix())
        self.assertTrue(any(entry.destination.name == 'verify.dart' for entry in plan))

    def test_exclusive_creation_preserves_a_file_added_after_preflight(self):
        plan = build_plan(SOURCE_ROOT, self.target)
        first = next(entry for entry in plan if not entry.identical)
        first.destination.parent.mkdir(parents=True, exist_ok=True)
        first.destination.write_text('Concurrent change', encoding='utf-8')
        with self.assertRaises(RuntimeError):
            apply_plan(plan, self.target)
        self.assertEqual(first.destination.read_text(), 'Concurrent change')

    def test_copied_material_links_resolve_in_the_target_project(self):
        from scripts.validate import local_link_errors
        plan = build_plan(SOURCE_ROOT, self.target)
        apply_plan(plan, self.target)
        errors = []
        for path in self.target.rglob('*.md'):
            errors.extend(local_link_errors(path, self.target))
        self.assertEqual(errors, [])
        self.assertFalse((self.target / 'config/workflow_catalog.json').exists())

    def test_incomplete_source_aborts_before_copying(self):
        original = Path.is_file
        missing = SOURCE_ROOT / 'templates/project/PROJECT.md'
        with patch.object(Path, 'is_file', lambda path: False if path == missing else original(path)):
            with self.assertRaisesRegex(ValueError, 'Required source file is missing'):
                build_plan(SOURCE_ROOT, self.target)
        self.assertFalse((self.target / 'AGENTS.md').exists())

    def test_tooling_can_be_added_after_product_documents_are_customized(self):
        apply_plan(build_plan(SOURCE_ROOT, self.target), self.target)
        product = self.target / 'PROJECT.md'
        product.write_text('The real product definition', encoding='utf-8')
        plan = build_plan(SOURCE_ROOT, self.target, only_tooling=True)
        self.assertTrue(all(entry.destination.relative_to(self.target).parts[0] in ('tool', 'scripts') for entry in plan))
        self.assertGreater(apply_plan(plan, self.target), 0)
        self.assertEqual(product.read_text(encoding='utf-8'), 'The real product definition')
        self.assertEqual(apply_plan(build_plan(SOURCE_ROOT, self.target, only_tooling=True), self.target), 0)

    def test_tooling_only_still_rejects_tool_conflicts(self):
        (self.target / 'tool').mkdir()
        (self.target / 'tool/verify.dart').write_text('Existing verifier', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'Existing files differ'):
            build_plan(SOURCE_ROOT, self.target, only_tooling=True)

    def test_ci_pin_rejects_non_object_json_and_accepts_utf8_bom(self):
        pin = self.target / '.fvmrc'
        for value in ('[]', 'null', '"3.47.2"'):
            pin.write_text(value, encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'exact stable Flutter version'):
                build_plan(SOURCE_ROOT, self.target, only_tooling=True, with_ci=True)
        pin.write_text('{"flutter": "3.47.2"}', encoding='utf-8-sig')
        self.assertTrue(build_plan(SOURCE_ROOT, self.target, only_tooling=True, with_ci=True))

    def test_installed_ci_sdk_readers_accept_the_same_bom_as_the_installer(self):
        from scripts.validate import parse_yaml
        (self.target / '.fvmrc').write_text('{"flutter": "3.47.2"}', encoding='utf-8-sig')
        scripts = set()
        for path in (SOURCE_ROOT / 'templates/flutter/.github/workflows').glob('*.yml'):
            workflow = parse_yaml(path.read_text(encoding='utf-8'))
            for job in workflow['jobs'].values():
                for step in job.get('steps', []):
                    if step.get('id') == 'sdk':
                        scripts.add(step['run'])
        self.assertTrue(scripts)
        for index, script in enumerate(sorted(scripts)):
            output = self.target / f'output-{index}.txt'
            result = subprocess.run([sys.executable, '-I', '-c', script], cwd=self.target,
                                    env=dict(os.environ, GITHUB_OUTPUT=str(output)),
                                    capture_output=True, encoding='utf-8', timeout=15)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(output.read_text(encoding='utf-8'), 'version=3.47.2\n')


if __name__ == '__main__':
    unittest.main()

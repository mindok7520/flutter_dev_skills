"""Exercise the real Dart verifier with a recording Flutter stand-in, not an app build."""

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from scripts.install import SOURCE_ROOT


DART = os.environ.get('DART_EXECUTABLE')


@unittest.skipUnless(DART, 'Set DART_EXECUTABLE to run Dart tooling checks; no Flutter app is built.')
class DartToolingTests(unittest.TestCase):
    def setUp(self):
        dart_bin = Path(DART).resolve().parent
        flutter = dart_bin.parent.parent.parent / ('flutter.bat' if os.name == 'nt' else 'flutter')
        if flutter.is_file():
            self.fail('DART_EXECUTABLE must select a standalone SDK so tests cannot invoke real Flutter builds.')
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        shutil.copytree(SOURCE_ROOT / 'templates/flutter/tool', self.root / 'tool')
        (self.root / 'lib').mkdir()
        (self.root / 'test').mkdir()
        (self.root / 'lib/main.dart').write_text('void main() {}\n', encoding='utf-8')
        (self.root / 'test/example_test.dart').write_text('void main() {}\n', encoding='utf-8')
        (self.root / 'pubspec.yaml').write_text("name: tooling_fixture\nenvironment:\n  sdk: '>=3.13.0 <4.0.0'\n", encoding='utf-8')
        (self.root / '.fvmrc').write_text('{"flutter": "3.47.2"}', encoding='utf-8-sig')
        for name in ('AGENTS.md', 'PROJECT.md', 'ARCHITECTURE.md', 'pubspec.lock'):
            (self.root / name).touch()
        executable_dir = self.root / 'fake-bin'
        executable_dir.mkdir()
        fake = executable_dir / 'record.py'
        fake.write_text(
            'import json, os, pathlib, sys\n'
            'args = sys.argv[1:]\n'
            "with pathlib.Path('commands.jsonl').open('a', encoding='utf-8') as output:\n"
            "    output.write(json.dumps(args) + '\\n')\n"
            "if args == ['--version', '--machine']:\n"
            "    print(json.dumps({'frameworkVersion': '3.47.2', 'dartSdkVersion': '3.13.2'}))\n"
            "if args and args[0] == os.environ.get('FAIL_FLUTTER_COMMAND'):\n"
            '    sys.exit(7)\n', encoding='utf-8',
        )
        if os.name == 'nt':
            (executable_dir / 'flutter.bat').write_text(f'@echo off\n"{sys.executable}" "{fake}" %*\n', encoding='utf-8')
        else:
            wrapper = executable_dir / 'flutter'
            wrapper.write_text(f'#!{sys.executable}\nexec(compile(open({str(fake)!r}).read(), {str(fake)!r}, "exec"))\n', encoding='utf-8')
            wrapper.chmod(0o755)
        self.environment = dict(os.environ, PATH=str(executable_dir) + os.pathsep + os.environ.get('PATH', ''))
        # A standalone SDK must be used: a Flutter-bundled Dart intentionally resolves its own Flutter.
        self.dart = str(Path(DART).resolve())

    def verify(self, *arguments):
        return subprocess.run([self.dart, 'tool/verify.dart', *arguments], cwd=self.root,
                              env=self.environment, capture_output=True, encoding='utf-8', timeout=60)

    def commands(self):
        path = self.root / 'commands.jsonl'
        return [json.loads(line) for line in path.read_text().splitlines()] if path.exists() else []

    def test_dart_sources_analyze_without_dependencies(self):
        result = subprocess.run([self.dart, 'analyze', 'tool'], cwd=self.root,
                                capture_output=True, encoding='utf-8', timeout=60)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_default_runs_common_checks_without_building(self):
        result = self.verify()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn(['analyze', '--fatal-infos'], self.commands())
        self.assertIn(['test', '--coverage'], self.commands())
        self.assertFalse(any(command[0] == 'build' for command in self.commands()))
        self.assertIn('NOT RUN', result.stdout)

    def test_selected_platforms_build_once(self):
        (self.root / 'web').mkdir()
        (self.root / 'android').mkdir()
        result = self.verify('--platform', 'web', '--platform', 'android', '--platform', 'web')
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual([command for command in self.commands() if command[0] == 'build'],
                         [['build', 'web', '--release'], ['build', 'apk', '--release']])

    def test_invalid_platform_fails_before_running_commands(self):
        for arguments in [('--platform',), ('--unknown', 'web'), ('--platform', 'missing')]:
            with self.subTest(arguments=arguments):
                self.assertNotEqual(self.verify(*arguments).returncode, 0)
                self.assertEqual(self.commands(), [])

    def test_platform_requiring_another_host_fails_before_commands(self):
        target = 'windows' if sys.platform != 'win32' else 'ios'
        (self.root / target).mkdir()
        result = self.verify('--platform', target)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('current host cannot build', result.stderr)
        self.assertEqual(self.commands(), [])

    def test_test_failure_prevents_build_and_success_report(self):
        (self.root / 'web').mkdir()
        self.environment['FAIL_FLUTTER_COMMAND'] = 'test'
        result = self.verify('--platform', 'web')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(['test', '--coverage'], self.commands())
        self.assertFalse(any(command[0] == 'build' for command in self.commands()))
        self.assertNotIn('unit/widget tests passed', result.stdout)


if __name__ == '__main__':
    unittest.main()

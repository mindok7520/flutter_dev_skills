import 'dart:io';

import 'src/processes.dart';

Future<void> main() => guarded(() async {
  requireProject();
  await run(Platform.resolvedExecutable, ['run', 'tool/check.dart']);
  final directories = [
    'lib',
    'test',
    'integration_test',
    'tool',
  ].where((path) => Directory(path).existsSync()).toList();
  await run(Platform.resolvedExecutable, [
    'format',
    '--output=none',
    '--set-exit-if-changed',
    ...directories,
  ]);
  await run(flutterExecutable, ['analyze', '--fatal-infos']);
  final tests = Directory('test');
  if (!tests.existsSync() ||
      !tests
          .listSync(recursive: true)
          .any((file) => file.path.endsWith('_test.dart'))) {
    throw StateError(
      'Add meaningful project tests before running the quality gate.',
    );
  }
  await run(flutterExecutable, ['test', '--coverage']);
  await run(flutterExecutable, ['build', 'web', '--release']);
  stdout.writeln(
    'Format, analysis, unit/widget tests, and web build passed. Device tests remain separate.',
  );
});

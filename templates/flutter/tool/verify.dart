import 'dart:io';

import 'src/processes.dart';

Future<void> main(List<String> arguments) => guarded(() async {
  requireProject();
  final targets = <String>[];
  for (var index = 0; index < arguments.length; index += 2) {
    if (arguments[index] != '--platform' || index + 1 >= arguments.length) {
      throw const FormatException(
        'Usage: dart run tool/verify.dart [--platform web|android|ios|linux|macos|windows]',
      );
    }
    final target = arguments[index + 1];
    if (![
          'web',
          'android',
          'ios',
          'linux',
          'macos',
          'windows',
        ].contains(target) ||
        !Directory(target).existsSync()) {
      throw FormatException('Unsupported or missing project platform: $target');
    }
    if ((target == 'ios' || target == 'macos') && !Platform.isMacOS ||
        target == 'windows' && !Platform.isWindows ||
        target == 'linux' && !Platform.isLinux) {
      throw StateError(
        'The current host cannot build $target. Use a matching CI runner.',
      );
    }
    if (!targets.contains(target)) targets.add(target);
  }
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
  for (final target in targets) {
    await run(flutterExecutable, [
      'build',
      target == 'android' ? 'apk' : target,
      '--release',
      if (target == 'ios') '--no-codesign',
    ]);
  }
  stdout.writeln(
    'Format, analysis, and unit/widget tests passed. '
    'Builds: ${targets.isEmpty ? 'NOT RUN (select --platform)' : targets.join(', ')}. '
    'Device tests, signing readiness, and deployment remain separate.',
  );
});

import 'dart:io';

import 'src/processes.dart';

Future<void> main() => guarded(() async {
  requireProject();
  for (final path in [
    'AGENTS.md',
    'PROJECT.md',
    'ARCHITECTURE.md',
    'pubspec.lock',
  ]) {
    if (!File(path).existsSync()) {
      throw StateError('Required project file is missing: $path');
    }
  }
  final manifest = File('pubspec.yaml').readAsStringSync();
  if (RegExp(
    r'^dependency_overrides\s*:',
    multiLine: true,
  ).hasMatch(manifest)) {
    throw StateError(
      'Remove dependency_overrides or explicitly revise the project policy with evidence.',
    );
  }
  await checkSdk();
  stdout.writeln(
    'Project configuration check passed. This is not a security audit or device test.',
  );
});

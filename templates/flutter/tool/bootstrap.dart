import 'dart:io';

import 'src/processes.dart';

Future<void> main() => guarded(() async {
  requireProject();
  await checkSdk();
  await run(flutterExecutable, ['pub', 'get']);
  if (File('l10n.yaml').existsSync()) {
    await run(flutterExecutable, ['gen-l10n']);
  }
  stdout.writeln(
    'Dependencies prepared. Review lockfile and generated metadata changes. No app code, SDK upgrade, or Git commands were performed.',
  );
});

import 'dart:convert';
import 'dart:io';

Future<void> guarded(Future<void> Function() action) async {
  try {
    await action();
  } on Object catch (error) {
    stderr.writeln('ERROR: $error');
    exitCode = 1;
  }
}

void requireProject() {
  if (!File('pubspec.yaml').existsSync() || !Directory('lib').existsSync()) {
    throw StateError('Run this tool from an existing Flutter project root.');
  }
}

String get flutterExecutable {
  // Use the Flutter SDK containing the currently executing Dart VM when possible.
  final dartBin = File(Platform.resolvedExecutable).parent;
  final flutterBin = dartBin.parent.parent.parent;
  final candidate = File.fromUri(
    flutterBin.uri.resolve(Platform.isWindows ? 'flutter.bat' : 'flutter'),
  );
  if (candidate.existsSync()) return candidate.path;
  return Platform.isWindows ? 'flutter.bat' : 'flutter';
}

Future<ProcessResult> capture(String executable, List<String> arguments) async {
  final result = await Process.run(
    executable,
    arguments,
    runInShell: Platform.isWindows && executable.endsWith('.bat'),
  );
  if (result.exitCode != 0) {
    throw ProcessException(
      executable,
      arguments,
      result.stderr.toString(),
      result.exitCode,
    );
  }
  return result;
}

Future<void> run(String executable, List<String> arguments) async {
  stdout.writeln('> $executable ${arguments.join(' ')}');
  final process = await Process.start(
    executable,
    arguments,
    mode: ProcessStartMode.inheritStdio,
    runInShell: Platform.isWindows && executable.endsWith('.bat'),
  );
  final result = await process.exitCode;
  if (result != 0) {
    throw ProcessException(executable, arguments, 'Command failed.', result);
  }
}

Future<void> checkSdk() async {
  final result = await capture(flutterExecutable, ['--version', '--machine']);
  final version = jsonDecode(result.stdout.toString()) as Map<String, dynamic>;
  final pin = File('.fvmrc');
  if (pin.existsSync()) {
    final expected =
        (jsonDecode(pin.readAsStringSync()) as Map<String, dynamic>)['flutter'];
    if (expected != version['frameworkVersion']) {
      throw StateError(
        'Flutter ${version['frameworkVersion']} does not match .fvmrc $expected.',
      );
    }
  }
  stdout.writeln(
    'Flutter ${version['frameworkVersion']}; Dart ${version['dartSdkVersion']}.',
  );
}

Map<String, dynamic> readObject(String path) {
  final value = jsonDecode(File(path).readAsStringSync());
  if (value is! Map<String, dynamic>) {
    throw FormatException('Expected a JSON object: $path');
  }
  return value;
}

File projectFile(String path) {
  if (path.isEmpty ||
      Uri.parse(path).hasScheme ||
      path.startsWith('/') ||
      path.startsWith('\\')) {
    throw FormatException('Expected a relative project path: $path');
  }
  final root = Directory.current.resolveSymbolicLinksSync();
  final file = File(path);
  final resolved = file.resolveSymbolicLinksSync();
  if (!resolved.startsWith('$root${Platform.pathSeparator}')) {
    throw FormatException('Evidence path escaped the project: $path');
  }
  return file;
}

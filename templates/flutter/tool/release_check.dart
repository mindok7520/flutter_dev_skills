import 'dart:io';

import 'src/processes.dart';

Future<void> main(List<String> arguments) => guarded(() async {
  requireProject();
  final candidate = arguments.contains('--candidate');
  final options = arguments.where((value) => value != '--candidate').toList();
  if (options.length != 2 || options.first != '--platform') {
    throw const FormatException(
      'Usage: dart run tool/release_check.dart --platform android|ios|web [--candidate]',
    );
  }
  final platform = options[1];
  if (!['android', 'ios', 'web'].contains(platform)) {
    throw const FormatException('Unsupported release platform.');
  }
  if (!Directory(platform).existsSync()) {
    throw StateError('Generate the required platform in the target app first.');
  }
  await checkSdk();
  final version = RegExp(
    r'^version:\s*([0-9]+\.[0-9]+\.[0-9]+\+[0-9]+)\s*$',
    multiLine: true,
  ).firstMatch(File('pubspec.yaml').readAsStringSync())?.group(1);
  if (version == null) {
    throw const FormatException(
      'Set an explicit version and build number in pubspec.yaml.',
    );
  }
  String? androidBuild;
  if (platform == 'android') {
    final kotlin = File('android/app/build.gradle.kts');
    final groovy = File('android/app/build.gradle');
    androidBuild = (kotlin.existsSync() ? kotlin : groovy).readAsStringSync();
    if (RegExp(
      r'^\s*signingConfig\s*[^\r\n]*\bdebug\b',
      multiLine: true,
    ).hasMatch(androidBuild)) {
      throw StateError(
        'Review and remove explicit debug signing before creating a release candidate.',
      );
    }
  }
  if (candidate) {
    stdout.writeln(
      'Candidate $platform $version only. Signing, store approval, and deployment are not verified.',
    );
    return;
  }
  final config = readObject('tool/release_config.json');
  if (config['schemaVersion'] != 1) {
    throw const FormatException('Unsupported release configuration schema.');
  }
  if (config['productReady'] != true) {
    throw StateError('Product release readiness has not been approved.');
  }
  final identity = config['applicationId'];
  if (identity is! String ||
      identity.contains('example') ||
      !identity.contains('.')) {
    throw const FormatException('Configure the real application identity.');
  }
  if (androidBuild != null) {
    final declared = RegExp(r'''applicationId\s*(?:=\s*)?["']([^"']+)["']''')
        .firstMatch(androidBuild)
        ?.group(1);
    if (declared != identity) {
      throw StateError(
        'Android applicationId must match the release configuration. Review flavor-specific builds separately.',
      );
    }
  }
  final current = (await capture('git', [
    'rev-parse',
    'HEAD',
  ])).stdout.toString().trim();
  final evidencePaths = config['evidence'] as Map<String, dynamic>;
  for (final name in [
    'quality',
    'security',
    'privacy',
    'operations',
    platform,
  ]) {
    final path = evidencePaths[name];
    if (path is! String) {
      throw FormatException('Missing release evidence: $name');
    }
    final evidence = readObject(projectFile(path).path);
    if (evidence['commit'] != current ||
        evidence['status'] != 'passed' ||
        evidence['details'] is! String ||
        (evidence['details'] as String).trim().isEmpty) {
      throw StateError(
        'Release evidence is not passed for the current commit: $name',
      );
    }
    final recorded = DateTime.tryParse(
      evidence['recordedAt']?.toString() ?? '',
    );
    if (recorded == null || recorded.isAfter(DateTime.now().toUtc())) {
      throw FormatException('Invalid release evidence timestamp: $name');
    }
  }
  stdout.writeln(
    'Recorded readiness evidence matches $current. This tool does not sign, submit, or deploy.',
  );
});

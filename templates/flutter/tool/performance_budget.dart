import 'dart:io';

import 'src/processes.dart';

Future<void> main(List<String> arguments) => guarded(() async {
  if (arguments.length != 2 || arguments.first != '--measurements') {
    throw const FormatException(
      'Usage: dart run tool/performance_budget.dart --measurements path.json',
    );
  }
  final budget = readObject('tool/performance_budget.json');
  if (budget['schemaVersion'] != 1) {
    throw const FormatException('Unsupported performance budget schema.');
  }
  final measurement = readObject(arguments[1]);
  for (final field in [
    'platform',
    'device',
    'mode',
    'commit',
    'profile',
    'evidence',
  ]) {
    if (measurement[field] is! String ||
        (measurement[field] as String).trim().isEmpty) {
      throw FormatException('Missing measurement metadata: $field');
    }
  }
  if (!['profile', 'release'].contains(measurement['mode'])) {
    throw const FormatException(
      'Performance measurements require profile or release mode.',
    );
  }
  if (!RegExp(r'^[a-f0-9]{40}$').hasMatch(measurement['commit'] as String)) {
    throw const FormatException('Measurement commit must be a full Git SHA.');
  }
  if (measurement['sampleCount'] is! int ||
      (measurement['sampleCount'] as int) < 20) {
    throw const FormatException(
      'At least 20 samples are required by the example policy.',
    );
  }
  projectFile(measurement['evidence'] as String);
  final profiles = budget['profiles'] as Map<String, dynamic>;
  final profile = profiles[measurement['profile']];
  if (profile is! Map<String, dynamic>) {
    throw const FormatException('Unknown budget profile.');
  }
  if (profile.isEmpty) {
    throw const FormatException('A budget profile must contain metrics.');
  }
  final metrics = measurement['metrics'] as Map<String, dynamic>;
  var failures = 0;
  for (final entry in profile.entries) {
    final limit = entry.value as Map<String, dynamic>;
    final measured = metrics[entry.key];
    if (measured is! Map<String, dynamic> ||
        measured['unit'] != limit['unit']) {
      throw FormatException('Missing metric or mismatched unit: ${entry.key}');
    }
    final value = measured['value'];
    if (value is! num || !value.isFinite || value < 0) {
      throw FormatException('Invalid measurement: ${entry.key}');
    }
    final maximum = limit['max'];
    if (maximum is! num || !maximum.isFinite || maximum < 0) {
      throw FormatException('Invalid budget limit: ${entry.key}');
    }
    final passed = value <= maximum;
    if (!passed) failures++;
    stdout.writeln(
      '${entry.key}: $value ${limit['unit']}; max $maximum; ${passed ? 'PASS' : 'FAIL'}',
    );
  }
  stdout.writeln(
    'Budget status: ${budget['status']}. Example limits are not product approval.',
  );
  if (failures > 0) {
    throw StateError('$failures performance budget(s) exceeded.');
  }
});

import 'dart:convert';
import 'dart:io';

import 'src/processes.dart';

Future<void> main(List<String> arguments) => guarded(() async {
  requireProject();
  if (arguments.any((arg) => arg != '--outdated' && arg != '--security')) {
    throw const FormatException(
      'Usage: dart run tool/analyze_dependencies.dart [--outdated] [--security]',
    );
  }
  final result = await capture(flutterExecutable, ['pub', 'deps', '--json']);
  final data = jsonDecode(result.stdout.toString()) as Map<String, dynamic>;
  final packages = (data['packages'] as List<dynamic>)
      .cast<Map<String, dynamic>>();
  final hosted = <Map<String, dynamic>>[];
  for (final package in packages) {
    if (package['kind'] == 'root' || package['source'] == 'sdk') continue;
    if (package['source'] != 'hosted') {
      throw StateError(
        'Review non-hosted dependency ${package['name']} before changing the baseline policy.',
      );
    }
    hosted.add(package);
    stdout.writeln('${package['name']} ${package['version']}');
  }
  if (arguments.contains('--outdated')) {
    await run(flutterExecutable, ['pub', 'outdated']);
  }
  if (arguments.contains('--security') && hosted.isNotEmpty) {
    final client = HttpClient()
      ..connectionTimeout = const Duration(seconds: 15);
    try {
      final request = await client.postUrl(
        Uri.parse('https://api.osv.dev/v1/querybatch'),
      );
      request.headers.contentType = ContentType.json;
      request.write(
        jsonEncode({
          'queries': [
            for (final package in hosted)
              {
                'package': {'name': package['name'], 'ecosystem': 'Pub'},
                'version': package['version'],
              },
          ],
        }),
      );
      final response = await request.close().timeout(
        const Duration(seconds: 30),
      );
      if (response.statusCode != 200) {
        throw HttpException('OSV status ${response.statusCode}');
      }
      final bytes = <int>[];
      await for (final chunk in response.timeout(const Duration(seconds: 30))) {
        bytes.addAll(chunk);
        if (bytes.length > 2000000) {
          throw const FormatException('OSV response is too large.');
        }
      }
      final body = jsonDecode(utf8.decode(bytes)) as Map<String, dynamic>;
      final results = body['results'] as List<dynamic>;
      if (results.length != hosted.length) {
        throw const FormatException('Unexpected OSV result count.');
      }
      var findings = 0;
      for (var index = 0; index < results.length; index++) {
        final item = results[index] as Map<String, dynamic>;
        final vulnerabilities = item['vulns'] as List<dynamic>? ?? [];
        for (final vulnerability in vulnerabilities) {
          stdout.writeln(
            '${hosted[index]['name']}: ${(vulnerability as Map<String, dynamic>)['id']}',
          );
          findings++;
        }
      }
      if (findings > 0) {
        throw StateError(
          'OSV reported $findings known vulnerability record(s).',
        );
      }
      stdout.writeln(
        'OSV returned no known vulnerabilities for the resolved hosted Pub packages.',
      );
    } finally {
      client.close(force: true);
    }
  }
  stdout.writeln(
    'Native dependencies, licenses, maintenance status, and private registries require separate review.',
  );
});

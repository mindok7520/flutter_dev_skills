"""Check pinned validation dependencies against the public OSV database."""

import json
from pathlib import Path
import re
import sys
import urllib.error
import urllib.request


def main() -> int:
    requirements = Path(__file__).resolve().parents[1] / 'requirements-dev.txt'
    packages = []
    for line in requirements.read_text(encoding='utf-8').splitlines():
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        match = re.fullmatch(r'([A-Za-z0-9_.-]+)==([0-9][A-Za-z0-9_.+-]*)', line.strip())
        if not match:
            raise ValueError('Validation dependencies must use exact versions.')
        packages.append(match.groups())
    queries = [{'package': {'name': name, 'ecosystem': 'PyPI'}, 'version': version} for name, version in packages]
    request = urllib.request.Request(
        'https://api.osv.dev/v1/querybatch',
        data=json.dumps({'queries': queries}).encode(),
        headers={'Content-Type': 'application/json', 'User-Agent': 'flutter-ai-base-audit'},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        body = response.read(2_000_001)
    if len(body) > 2_000_000:
        raise ValueError('OSV response exceeded the size limit.')
    results = json.loads(body)['results']
    if not isinstance(results, list) or len(results) != len(packages):
        raise ValueError('OSV returned an unexpected result count.')
    failed = False
    for (name, version), result in zip(packages, results):
        vulnerabilities = result.get('vulns', [])
        if vulnerabilities:
            failed = True
            print(f'{name} {version}: ' + ', '.join(v['id'] for v in vulnerabilities))
        else:
            print(f'{name} {version}: no known vulnerabilities returned by OSV.')
    print('This check covers pinned Python validation dependencies, not product or native dependencies.')
    return int(failed)


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (OSError, ValueError, KeyError, TypeError, urllib.error.URLError) as error:
        print(f'Dependency audit failed: {error}', file=sys.stderr)
        raise SystemExit(1) from error

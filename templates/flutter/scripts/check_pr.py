"""Validate issue-linked branches and pull request destinations."""

import json
import os
from pathlib import Path
import re
import sys


def validate_pr(event: dict) -> list[str]:
    pr = event.get('pull_request')
    if not isinstance(pr, dict):
        return ['A pull_request event is required.']
    head = pr['head']['ref']
    base = pr['base']['ref']
    errors = []
    work = re.fullmatch(r'(feature|fix|refactor|docs|chore|perf|test|codex|hotfix)/(\d+)-[a-z0-9]+(?:-[a-z0-9]+)*', head)
    release = re.fullmatch(r'release/\d+\.\d+\.\d+', head)
    if base == 'master':
        if not release and not (work and work.group(1) == 'hotfix'):
            errors.append('master accepts release or hotfix branches.')
    elif base == 'develop':
        if not work and not release:
            errors.append('develop accepts issue-linked work or release synchronization branches.')
    else:
        errors.append('Pull requests must target develop or master.')
    if work and not re.search(rf'(?<!\d)#{work.group(2)}(?!\d)', pr.get('body') or ''):
        errors.append('The PR body must reference the branch issue number.')
    if not (pr.get('body') or '').strip():
        errors.append('The PR body must describe scope and verification.')
    return errors


def main() -> int:
    event_path = os.environ.get('GITHUB_EVENT_PATH')
    if not event_path:
        print('GITHUB_EVENT_PATH is required.', file=sys.stderr)
        return 1
    try:
        errors = validate_pr(json.loads(Path(event_path).read_text(encoding='utf-8')))
    except (OSError, ValueError, KeyError, TypeError) as error:
        errors = [str(error)]
    for error in errors:
        print(error, file=sys.stderr)
    if not errors:
        print('Pull request branch and issue policy passed.')
    return int(bool(errors))


if __name__ == '__main__':
    raise SystemExit(main())

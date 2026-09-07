"""Build a small, explicit task packet without executing commands or reading app code."""

from __future__ import annotations

import argparse
import json
from pathlib import Path, PureWindowsPath
import sys


def project_path(root: Path, value: str, *, must_exist: bool = True) -> Path:
    path = Path(value)
    if not value.strip() or path.is_absolute() or PureWindowsPath(value).drive or '\\' in value:
        raise ValueError(f'Use a relative project path with forward slashes: {value}')
    if '..' in path.parts or any(ord(char) < 32 for char in value):
        raise ValueError(f'Unsafe project path: {value!r}')
    destination = root / path
    if not destination.resolve().is_relative_to(root):
        raise ValueError(f'Path escaped the project: {value}')
    if must_exist and not destination.is_file():
        raise ValueError(f'Required context file is missing: {value}')
    return destination


def load_catalog(root: Path) -> dict:
    candidates = [root / 'config/workflow_catalog.json', root / '.agents/workflow_catalog.json']
    path = next((path for path in candidates if path.is_file()), None)
    if path is None:
        raise ValueError('Workflow catalog is missing. Install the development materials first.')
    data = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(data, dict) or data.get('schema_version') != 1 or not isinstance(data.get('prompts'), list):
        raise ValueError('Unsupported workflow catalog.')
    return data


def single_line(value: str) -> str:
    value = value.strip()
    if not value or len(value) > 2000 or any(ord(char) < 32 for char in value):
        raise ValueError('Task fields must be nonempty single lines of at most 2000 characters.')
    return value


def build_packet(root: Path, task: str, goal: str, acceptance: list[str], files: list[str],
                 checks: list[str], *, plan: str | None = None, constraints: list[str] = ()) -> str:
    root = root.resolve(strict=True)
    catalog = load_catalog(root)
    matches = [entry for entry in catalog['prompts'] if isinstance(entry, dict) and
               (task in (str(entry.get('id')), str(entry.get('id')).zfill(2)) or
                task == Path(entry.get('path', '')).stem)]
    if len(matches) != 1:
        raise ValueError(f'Unknown or ambiguous task: {task}. Use --list.')
    if not acceptance or not checks:
        raise ValueError('Provide at least one --accept and --check; describe manual evidence if no command applies.')
    if len(files) > 12 or len(acceptance) > 8 or len(checks) > 8:
        raise ValueError('Split this task: at most 12 files, 8 acceptance criteria, and 8 checks per packet.')
    entry = matches[0]
    required = ['AGENTS.md', 'PROJECT.md', 'ARCHITECTURE.md',
                'docs/agent/PROMPT_CONTRACT.md', entry['path']]
    if plan:
        required.append(plan)
    required.extend(files)
    required = list(dict.fromkeys(required))
    for value in required:
        project_path(root, value)
    lines = [f'# Task: {single_line(entry["title_ko"])}', '', '## Goal', '', single_line(goal), '',
             '## Acceptance criteria', '']
    lines.extend(f'- {single_line(value)}' for value in acceptance)
    lines.extend(['', '## Read first', ''])
    lines.extend(f'- `{value}`' for value in required)
    lines.extend(['', 'Read the selected prompt and its task-specific references as needed. Do not load the whole index.',
                  'Inspect the actual manifest, lockfile, SDK pin, Git changes, and relevant callers before editing.',
                  'This packet lists paths, not their contents; use a tool with repository access or provide those files.',
                  '', '## Scope and constraints', ''])
    lines.extend(f'- {single_line(value)}' for value in constraints)
    lines.extend(['- Treat listed code files as investigation starting points, not proof that the scope is complete.',
                  '- Implement one acceptance criterion at a time. Preserve existing changes and approved decisions.',
                  '- Ask only for missing decisions that block the task; continue independent authorized work.',
                  '- Report contradictory requirements or repeated failures with evidence before expanding scope.',
                  '', '## Verification to perform', ''])
    lines.extend(f'- {single_line(value)}' for value in checks)
    lines.extend(['', 'These are requested checks, not executed results. Inspect commands before running them.',
                  'Record baseline failures separately. Do not claim a check passed without current evidence.',
                  '', '## Completion', '', single_line(entry['output_ko']), '',
                  'Report in Korean: delivered behavior, changed files, commands and results, remaining risks, and next action.',
                  'Update the active plan with exact paths and evidence before handing work to another session or model.', ''])
    return '\n'.join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path.cwd())
    parser.add_argument('--list', action='store_true')
    parser.add_argument('--task')
    parser.add_argument('--goal')
    parser.add_argument('--accept', action='append', default=[])
    parser.add_argument('--file', action='append', default=[])
    parser.add_argument('--check', action='append', default=[])
    parser.add_argument('--constraint', action='append', default=[])
    parser.add_argument('--plan')
    parser.add_argument('--output', help='Create a new UTF-8 file relative to --root; never overwrite.')
    args = parser.parse_args(argv)
    try:
        root = args.root.resolve(strict=True)
        if args.list:
            for entry in load_catalog(root)['prompts']:
                print(f'{entry["id"]:02d} {entry["title_ko"]}: {entry["output_ko"]}')
            return 0
        if not args.task or not args.goal:
            raise ValueError('--task and --goal are required unless --list is used.')
        packet = build_packet(root, args.task, args.goal, args.accept, args.file, args.check,
                              plan=args.plan, constraints=args.constraint)
        if args.output:
            output = project_path(root, args.output, must_exist=False)
            # Require the caller to choose an existing directory; do not create a project tree.
            with output.open('x', encoding='utf-8', newline='\n') as stream:
                stream.write(packet)
            print(f'Created {args.output}; no checks were executed.')
        else:
            print(packet, end='')
        return 0
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f'Task context failed: {error}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    # Windows consoles and redirected files must preserve Korean input and output.
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
    raise SystemExit(main())

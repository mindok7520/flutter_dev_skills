"""Preview and copy development materials without overwriting project files."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
from pathlib import Path
import re
import shutil
import sys


SOURCE_ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class CopyEntry:
    source: Path
    destination: Path
    identical: bool


def walk_files(directory: Path):
    if not directory.is_dir() or directory.is_symlink():
        raise ValueError(f'Required source directory is missing or unsupported: {directory}')
    for path in sorted(directory.rglob('*')):
        if path.is_symlink():
            raise ValueError(f'Symbolic links are not supported: {path}')
        if path.is_file() and '__pycache__' not in path.parts:
            yield path


def destination_for(target: Path, relative: Path) -> Path:
    destination = target / relative
    current = destination
    while current != target:
        if current.is_symlink():
            raise ValueError(f'Destination contains a symbolic link: {current}')
        if current.parent == current:
            raise ValueError('Destination escaped the target directory.')
        current = current.parent
    if not destination.resolve().is_relative_to(target):
        raise ValueError('Destination escaped the target directory.')
    for parent in destination.parents:
        if parent == target:
            break
        if parent.exists() and not parent.is_dir():
            raise ValueError(f'Destination parent is not a directory: {parent}')
    return destination


def build_plan(
    source: Path,
    target: Path,
    *,
    with_tooling: bool = False,
    with_ci: bool = False,
) -> list[CopyEntry]:
    source = source.resolve()
    target = target.resolve(strict=True)
    if target == source or target.is_relative_to(source) or source.is_relative_to(target):
        raise ValueError('Source and target must be separate, non-overlapping directories.')
    if not (target / 'pubspec.yaml').is_file():
        raise ValueError('Create the target Flutter project first; pubspec.yaml is required.')
    if with_ci and not with_tooling:
        raise ValueError('--with-ci requires --with-tooling.')
    for relative in ('templates/project/PROJECT.md', 'templates/project/ARCHITECTURE.md'):
        if not (source / relative).is_file():
            raise ValueError(f'Required source file is missing: {relative}')
    if with_ci:
        pin = target / '.fvmrc'
        if not pin.is_file():
            raise ValueError('Optional CI requires the target SDK version in .fvmrc. See templates/README.md.')
        version = json.loads(pin.read_text(encoding='utf-8')).get('flutter')
        if not isinstance(version, str) or not re.fullmatch(r'\d+\.\d+\.\d+', version):
            raise ValueError('Optional CI requires an exact stable Flutter version in .fvmrc.')

    selected: dict[Path, Path] = {}
    for name in ('AGENTS.md', 'CLAUDE.md', 'GEMINI.md'):
        selected[Path(name)] = source / name
    for directory in ('docs', 'prompts', '.agents', '.cursor'):
        for path in walk_files(source / directory):
            relative = path.relative_to(source)
            if relative.as_posix() == 'docs/FILE_MAP.md':
                continue
            if relative.parts[:3] == ('docs', 'exec-plans', 'completed'):
                if path.name != '.gitkeep':
                    continue
            if relative.parts[:3] == ('docs', 'exec-plans', 'active'):
                if path.name != '.gitkeep':
                    continue
            selected[relative] = path
    for name in ('copilot-instructions.md', 'PULL_REQUEST_TEMPLATE.md'):
        selected[Path('.github') / name] = source / '.github' / name
    for directory in ('instructions', 'prompts', 'ISSUE_TEMPLATE'):
        for path in walk_files(source / '.github' / directory):
            selected[path.relative_to(source)] = path
    for path in walk_files(source / 'templates' / 'project'):
        selected[path.relative_to(source / 'templates' / 'project')] = path
    if with_tooling:
        for directory in ('tool', 'scripts'):
            for path in walk_files(source / 'templates' / 'flutter' / directory):
                selected[path.relative_to(source / 'templates' / 'flutter')] = path
    if with_ci:
        for path in walk_files(source / 'templates' / 'flutter' / '.github' / 'workflows'):
            selected[path.relative_to(source / 'templates' / 'flutter')] = path

    plan = []
    conflicts = []
    for relative, path in sorted(selected.items()):
        if not path.is_file() or path.is_symlink():
            raise ValueError(f'Source file is missing or unsupported: {path}')
        destination = destination_for(target, relative)
        exists = destination.exists()
        identical = exists and destination.is_file() and path.read_bytes() == destination.read_bytes()
        if exists and not identical:
            conflicts.append(str(relative))
        plan.append(CopyEntry(path, destination, identical))
    if conflicts:
        raise ValueError('Existing files differ; no files were copied:\n' + '\n'.join(conflicts))
    return plan


def apply_plan(plan: list[CopyEntry], target: Path) -> int:
    target = target.resolve(strict=True)
    created: list[Path] = []
    try:
        for entry in plan:
            relative = entry.destination.relative_to(target)
            destination_for(target, relative)
            if entry.identical:
                if entry.destination.read_bytes() != entry.source.read_bytes():
                    raise ValueError(f'File changed after preflight: {entry.destination}')
                continue
            entry.destination.parent.mkdir(parents=True, exist_ok=True)
            # Exclusive creation also protects against a file appearing after preflight.
            with entry.destination.open('xb') as output:
                created.append(entry.destination)
                with entry.source.open('rb') as input_file:
                    shutil.copyfileobj(input_file, output)
    except (OSError, ValueError) as error:
        # Keep copied files recoverable rather than deleting an uncertain partial result.
        raise RuntimeError(
            f'Copy stopped after creating {len(created)} files. Existing files were not overwritten. '
            f'Review the target and rerun to skip identical files. Cause: {error}'
        ) from error
    return len(created)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target', type=Path, required=True)
    parser.add_argument('--apply', action='store_true', help='Copy after all conflicts are checked.')
    parser.add_argument('--with-tooling', action='store_true')
    parser.add_argument('--with-ci', action='store_true')
    parser.add_argument('--list', action='store_true', help='List every planned destination.')
    args = parser.parse_args()
    try:
        plan = build_plan(SOURCE_ROOT, args.target, with_tooling=args.with_tooling, with_ci=args.with_ci)
        new_count = sum(not entry.identical for entry in plan)
        print(f'Preflight: {new_count} new files; {len(plan) - new_count} identical files; no conflicts.')
        if args.list:
            for entry in plan:
                print(('KEEP ' if entry.identical else 'COPY ') + str(entry.destination))
        if args.apply:
            print(f'Copied {apply_plan(plan, args.target)} files. No application code was generated.')
        else:
            print('Preview only. Add --apply to copy the reviewed plan.')
        return 0
    except (OSError, ValueError, RuntimeError) as error:
        print(str(error), file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())

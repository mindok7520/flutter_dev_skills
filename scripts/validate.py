"""Validate material coverage, local links, metadata, YAML, and workflow policies."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

from markdown_it import MarkdownIt
import yaml


ROOT = Path(__file__).resolve().parents[1]
IGNORED = {'.git', '.venv', '__pycache__', '.dart_tool', 'build', '.local', 'artifacts'}


class UniqueKeyLoader(yaml.BaseLoader):
    """Preserve YAML strings and reject duplicate mapping keys."""


def unique_mapping(loader, node):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=True)
        if key in mapping:
            raise ValueError(f'Duplicate YAML key: {key}')
        mapping[key] = loader.construct_object(value_node, deep=True)
    return mapping


UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def parse_yaml(text: str):
    return yaml.load(text, Loader=UniqueKeyLoader)


def workflow_errors(data, relative: Path) -> list[str]:
    errors = []
    if not isinstance(data, dict) or 'on' not in data or not isinstance(data.get('jobs'), dict):
        return [f'Invalid workflow structure: {relative}']
    if data.get('permissions') != {'contents': 'read'}:
        errors.append(f'Workflow must default to contents: read: {relative}')
    events = data['on']
    if not isinstance(events, (dict, list, str)):
        errors.append(f'Invalid workflow event declaration: {relative}')
    elif 'pull_request_target' in events:
        errors.append(f'Unsafe PR event in workflow: {relative}')
    pending = [data]
    visited = set()
    while pending:
        value = pending.pop()
        if isinstance(value, (dict, list)):
            if id(value) in visited:
                continue
            visited.add(id(value))
        if isinstance(value, dict):
            if 'uses' in value:
                uses = value['uses']
                if not isinstance(uses, str) or not re.fullmatch(r'[\w./-]+@[0-9a-f]{40}', uses):
                    errors.append(f'Action is not pinned to a commit: {relative}: {uses}')
            pending.extend(value.values())
        elif isinstance(value, list):
            pending.extend(value)
    for job in data['jobs'].values():
        if not isinstance(job, dict):
            errors.append(f'Invalid job: {relative}')
        elif 'runs-on' in job and 'timeout-minutes' not in job:
            errors.append(f'Job has no timeout: {relative}')
    return errors


def local_link_errors(path: Path, root: Path) -> list[str]:
    text = path.read_text(encoding='utf-8')
    errors = []
    pending = list(MarkdownIt('commonmark').parse(text))
    while pending:
        token = pending.pop()
        pending.extend(token.children or [])
        if token.type == 'link_open':
            raw = token.attrGet('href') or ''
        elif token.type == 'image':
            raw = token.attrGet('src') or ''
        else:
            continue
        parsed = urlsplit(raw)
        if parsed.scheme or not parsed.path:
            continue
        destination = (path.parent / unquote(parsed.path)).resolve()
        if not destination.is_relative_to(root) or not destination.exists():
            errors.append(f'{path.relative_to(root)}: broken local link: {raw}')
    return errors


def catalog_errors(data, root: Path) -> list[str]:
    """Check discovery entries against actual files rather than fixed counts."""
    if not isinstance(data, dict) or data.get('schema_version') != 1:
        return ['Invalid workflow catalog schema.']
    prompts, skills = data.get('prompts'), data.get('skills')
    if not isinstance(prompts, list) or not prompts or not isinstance(skills, list) or not skills:
        return ['Workflow catalog requires nonempty prompt and skill lists.']
    errors = []
    if any(not isinstance(name, str) or not re.fullmatch(r'[a-z0-9-]{1,64}', name) for name in skills):
        return ['Invalid workflow catalog skill name.']
    if len(skills) != len(set(skills)):
        errors.append('Duplicate workflow catalog skill.')
    actual_skills = {path.parent.name for path in (root / '.agents/skills').glob('*/SKILL.md')}
    if set(skills) != actual_skills:
        errors.append('Workflow catalog skills differ from actual skill files.')
    paths, ids = [], []
    for entry in prompts:
        if not isinstance(entry, dict):
            errors.append('Invalid workflow catalog prompt entry.')
            continue
        identifier, path = entry.get('id'), entry.get('path')
        if type(identifier) is not int or not 0 <= identifier <= 99:
            errors.append('Invalid workflow catalog prompt id.')
            continue
        ids.append(identifier)
        if not isinstance(path, str) or not re.fullmatch(r'prompts/[0-9]{2}-[a-z0-9-]+\.md', path):
            errors.append(f'Invalid workflow catalog prompt path: {path}')
            continue
        paths.append(path)
        if not Path(path).name.startswith(f'{identifier:02d}-'):
            errors.append(f'Workflow catalog id and filename differ: {path}')
        if entry.get('language') not in ('en', 'ko'):
            errors.append(f'Invalid workflow catalog language: {path}')
        for key in ('title_ko', 'output_ko', 'category'):
            if not isinstance(entry.get(key), str) or not entry[key].strip():
                errors.append(f'Missing workflow catalog {key}: {path}')
        mapped = entry.get('skills')
        if not isinstance(mapped, list) or any(not isinstance(name, str) or name not in skills for name in mapped):
            errors.append(f'Unknown workflow catalog skill reference: {path}')
    if len(paths) != len(set(paths)) or len(ids) != len(set(ids)):
        errors.append('Duplicate workflow catalog prompt path or id.')
    if sorted(ids) != list(range(len(prompts))):
        errors.append('Workflow catalog prompt ids are not contiguous.')
    actual_prompts = {path.relative_to(root).as_posix() for path in (root / 'prompts').glob('[0-9][0-9]-*.md')}
    if set(paths) != actual_prompts:
        errors.append('Workflow catalog prompts differ from actual prompt files.')
    actual_adapters = {path.name for path in (root / '.github/prompts').glob('*.prompt.md')}
    expected_adapters = {Path(path).stem + '.prompt.md' for path in actual_prompts}
    if actual_adapters != expected_adapters:
        errors.append('Workflow prompt adapters differ from actual prompt files.')
    return errors


def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors = []
    manifest_path = root / 'config' / 'required_files.json'
    try:
        manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        for entry in manifest['files'] + manifest.get('extensions', []):
            path = (root / entry['path']).resolve()
            if not path.is_relative_to(root) or not path.is_file():
                errors.append(f'Missing required file: {entry["path"]}')
    except (OSError, ValueError, KeyError, TypeError) as error:
        errors.append(f'Cannot load required file manifest: {error}')

    try:
        catalog = json.loads((root / 'config/workflow_catalog.json').read_text(encoding='utf-8'))
        errors.extend(catalog_errors(catalog, root))
    except (OSError, ValueError, TypeError) as error:
        errors.append(f'Cannot load workflow catalog: {error}')

    for name in ('pubspec.yaml', 'lib', 'android', 'ios', 'web', 'macos', 'windows', 'linux'):
        if (root / name).exists():
            errors.append(f'Application content must not live in the material repository root: {name}')
    for name in ('질문.txt', '답변.txt'):
        if (root / name).exists():
            errors.append(f'Original request file must be removed before completion: {name}')

    for path in sorted(root.rglob('*')):
        relative = path.relative_to(root)
        if any(part in IGNORED for part in relative.parts) or not path.is_file():
            continue
        try:
            if path.suffix in ('.md', '.mdc'):
                errors.extend(local_link_errors(path, root))
                text = path.read_text(encoding='utf-8')
                if '\ufffd' in text or re.search(r'\?{2,}', text):
                    errors.append(f'Unicode replacement character: {relative}')
                if re.search(r'\b(?:TODO|TBD|FIXME|NotImplementedError)\b', text):
                    errors.append(f'Unfinished content marker: {relative}')
                if text.startswith('---\n'):
                    parse_yaml(text.split('---\n', 2)[1])
            if path.suffix in ('.yml', '.yaml'):
                yaml_text = path.read_text(encoding='utf-8')
                if '\ufffd' in yaml_text or re.search(r'\?{2,}', yaml_text):
                    errors.append(f'Unicode replacement character: {relative}')
                data = parse_yaml(yaml_text)
                if 'workflows' in relative.parts:
                    errors.extend(workflow_errors(data, relative))
            if path.suffix == '.json':
                json.loads(path.read_text(encoding='utf-8'))
        except (OSError, ValueError, yaml.YAMLError, IndexError, TypeError) as error:
            errors.append(f'{relative}: {error}')

    skills = sorted((root / '.agents' / 'skills').glob('*/SKILL.md'))
    for path in skills:
        try:
            text = path.read_text(encoding='utf-8')
            metadata = parse_yaml(text.split('---\n', 2)[1])
            if set(metadata) != {'name', 'description'}:
                errors.append(f'Skill metadata fields are invalid: {path.parent.name}')
            if metadata['name'] != path.parent.name or not re.fullmatch(r'[a-z0-9-]{1,64}', metadata['name']):
                errors.append(f'Skill name is invalid: {path.parent.name}')
            if len(text) < 1200 or len(text.splitlines()) > 500:
                errors.append(f'Skill detail or size is invalid: {path.parent.name}')
            interface = parse_yaml((path.parent / 'agents' / 'openai.yaml').read_text(encoding='utf-8'))['interface']
            if '$' + path.parent.name not in interface['default_prompt']:
                errors.append(f'Skill invocation missing from default prompt: {path.parent.name}')
            if not 25 <= len(interface['short_description']) <= 64:
                errors.append(f'Skill short description length is invalid: {path.parent.name}')
        except (OSError, ValueError, KeyError, IndexError, TypeError) as error:
            errors.append(f'Invalid skill {path.parent.name}: {error}')

    prompts = sorted((root / 'prompts').glob('[0-9][0-9]-*.md'))
    for index, path in enumerate(prompts):
        if not path.name.startswith(f'{index:02d}-'):
            errors.append(f'Prompt numbering is not contiguous: {path.name}')
        if len(path.read_text(encoding='utf-8')) < 1500:
            errors.append(f'Prompt lacks required detail: {path.name}')
        adapter = root / '.github' / 'prompts' / (path.stem + '.prompt.md')
        if not adapter.is_file() or path.name not in adapter.read_text(encoding='utf-8'):
            errors.append(f'Prompt adapter missing or stale: {path.name}')
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    errors = validate(args.root)
    if errors:
        for error in errors:
            print('ERROR: ' + error, file=sys.stderr)
        print(f'Validation failed: {len(errors)} problem(s).', file=sys.stderr)
        return 1
    print('Validated required files, links, prompt/skill catalog, YAML, JSON, and workflow policies.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

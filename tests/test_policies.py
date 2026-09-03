"""Test externally supplied PR metadata and document parser boundaries."""

from pathlib import Path
import tempfile
import unittest

from scripts.check_pr import validate_pr
from scripts.validate import local_link_errors, parse_yaml, workflow_errors


class PolicyTests(unittest.TestCase):
    def test_yaml_on_key_is_preserved_and_duplicate_keys_fail(self):
        self.assertIn('on', parse_yaml('on: [push]\n'))
        with self.assertRaises(ValueError):
            parse_yaml('name: first\nname: second\n')

    def test_work_branch_requires_matching_issue_and_destination(self):
        event = {'pull_request': {'head': {'ref': 'codex/42-add-guidance'}, 'base': {'ref': 'develop'}, 'body': 'Refs #42. Verified.'}}
        self.assertEqual(validate_pr(event), [])
        event['pull_request']['body'] = 'Refs #420.'
        self.assertTrue(validate_pr(event))
        event['pull_request']['body'] = 'Refs #42.'
        event['pull_request']['base']['ref'] = 'master'
        self.assertTrue(validate_pr(event))

    def test_missing_and_escaping_local_links_are_reported(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary).resolve()
            document = root / 'guide.md'
            document.write_text('[missing](missing.md)\n[escape](../outside.md)\n[official](https://docs.flutter.dev/)\n', encoding='utf-8')
            self.assertEqual(len(local_link_errors(document, root)), 2)

    def test_action_pins_are_checked_independently_of_yaml_formatting(self):
        for step in [
            '- uses: actions/checkout@main',
            "- 'uses': actions/checkout@main",
            '- {uses: actions/checkout@main}',
        ]:
            workflow = parse_yaml(
                'on: [push]\npermissions: {contents: read}\njobs:\n'
                '  quality:\n    runs-on: ubuntu-24.04\n    timeout-minutes: 5\n'
                f'    steps:\n      {step}\n'
            )
            errors = workflow_errors(workflow, Path('ci.yml'))
            self.assertTrue(any('not pinned' in error for error in errors), step)

    def test_markdown_titles_and_reference_links_follow_commonmark(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary).resolve()
            (root / 'README.md').write_text('# Existing\n', encoding='utf-8')
            document = root / 'guide.md'
            document.write_text(
                '[existing](README.md "Read me")\n'
                '[missing-guide][guide]\n\n[guide]: missing-guide.md\n',
                encoding='utf-8',
            )
            errors = local_link_errors(document, root)
            self.assertEqual(len(errors), 1)
            self.assertIn('missing-guide.md', errors[0])

    def test_non_mapping_workflows_report_errors_without_crashing(self):
        self.assertTrue(workflow_errors(parse_yaml('- invalid\n'), Path('ci.yml')))


if __name__ == '__main__':
    unittest.main()

"""Exercise catalog drift and malformed discovery metadata."""

import copy
import json
import unittest

from scripts.validate import ROOT, catalog_errors


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.catalog = json.loads((ROOT / 'config/workflow_catalog.json').read_text(encoding='utf-8'))

    def test_catalog_matches_repository_files_and_adapters(self):
        self.assertEqual(catalog_errors(self.catalog, ROOT), [])

    def test_missing_entry_and_duplicate_entry_are_rejected(self):
        self.catalog['prompts'].pop()
        errors = catalog_errors(self.catalog, ROOT)
        self.assertTrue(any('differ from actual prompt files' in error for error in errors))
        self.catalog['prompts'].append(copy.deepcopy(self.catalog['prompts'][0]))
        self.assertTrue(any('Duplicate' in error for error in catalog_errors(self.catalog, ROOT)))

    def test_missing_skill_and_unknown_skill_reference_are_rejected(self):
        self.catalog['skills'].remove('ui-design')
        errors = catalog_errors(self.catalog, ROOT)
        self.assertTrue(any('skills differ' in error for error in errors))
        self.assertTrue(any('Unknown' in error for error in errors))

    def test_escaping_paths_and_invalid_entries_report_errors(self):
        for value in ('../outside.md', '/outside.md', 'prompts/../outside.md', None):
            with self.subTest(path=value):
                data = copy.deepcopy(self.catalog)
                data['prompts'][0]['path'] = value
                self.assertTrue(any('Invalid workflow catalog prompt path' in error for error in catalog_errors(data, ROOT)))
        for data in (None, {}, {'schema_version': 1, 'prompts': {}, 'skills': []}):
            self.assertTrue(catalog_errors(data, ROOT))

    def test_invalid_language_id_and_discovery_text_are_rejected(self):
        for field, value in (('language', 'unknown'), ('id', True), ('title_ko', ''), ('skills', ['missing'])):
            with self.subTest(field=field):
                data = copy.deepcopy(self.catalog)
                data['prompts'][0][field] = value
                self.assertTrue(catalog_errors(data, ROOT))


if __name__ == '__main__':
    unittest.main()

import csv
import json
from pathlib import Path
import unittest


RECORDS = Path(__file__).resolve().parents[1] / 'records'
SCHEMAS = {'frames.json': 'dict', 'draws.json': 'dict', 'reviews.json': 'dict',
           'publication_ledger.json': 'dict'}


class PartnerSourceTests(unittest.TestCase):
    def test_format(self):
        self.assertEqual({path.name for path in RECORDS.iterdir()}, set(SCHEMAS))
        for name, shape in SCHEMAS.items():
            with self.subTest(name=name), (RECORDS / name).open(encoding='utf-8', newline='') as source:
                if isinstance(shape, list):
                    rows = csv.DictReader(source)
                    self.assertEqual(rows.fieldnames, shape)
                    records = list(rows)
                    self.assertTrue(records)
                    self.assertTrue(all(None not in row and None not in row.values() for row in records))
                else:
                    records = json.load(source)
                    self.assertIsInstance(records, list if shape == 'list' else dict)
                    self.assertTrue(records)

    def test_publication_references(self):
        def read(name):
            return json.loads((RECORDS / name).read_text(encoding='utf-8'))

        frames = read('frames.json')
        available = read('reviews.json')
        journal = read('publication_ledger.json')
        universes = {item['id']: item['season'] for item in journal['universes']}
        schools = {work['school'] for work in frames['works']}
        for row in journal['already_issued'] + journal['requests']:
            self.assertIn(row['theme'], frames['themes'][row['theme_version']])
            self.assertEqual(row['season'], universes[row['universe']])
            self.assertLessEqual(set(row['schools']), schools)
        for slot in journal['review_slots']:
            reviewer = available['alias'].get(slot['reviewer'], slot['reviewer'])
            self.assertIn(slot['language'], available['qualifications'][reviewer])

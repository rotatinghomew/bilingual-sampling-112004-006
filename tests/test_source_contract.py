import csv
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1] / "records"


class SourceContract(unittest.TestCase):
    def test_export_shape(self):
        self.assertEqual({path.name for path in ROOT.iterdir()}, set(EXPECTED))
        for name, contract in EXPECTED.items():
            with self.subTest(source=name):
                path = ROOT / name
                if path.suffix == ".csv":
                    with path.open(encoding="utf-8", newline="") as source:
                        reader = csv.DictReader(source)
                        self.assertEqual(reader.fieldnames, contract)
                        rows = list(reader)
                    self.assertTrue(rows)
                    self.assertTrue(all(None not in row and None not in row.values() for row in rows))
                else:
                    body = json.loads(path.read_text(encoding="utf-8"))
                    self.assertIsInstance(body, list if contract == "list" else dict)
                    self.assertTrue(body)

    def test_related_export_records(self):
        for name, value in SEQUENCE.items():
            with self.subTest(source=name):
                path = ROOT / name
                if path.suffix == ".csv":
                    with path.open(encoding="utf-8", newline="") as source:
                        cells = {cell for row in csv.reader(source) for cell in row}
                else:
                    rows = json.loads(path.read_text(encoding="utf-8"))
                    cells = {item for row in rows for item in row.values() if isinstance(item, str)}
                self.assertIn(value, cells)


EXPECTED = {'program.json': 'dict', 'attendance.csv': ['seat', 'activity', 'person', 'checked', 'checkin', 'alias_of'], 'evidence.csv': ['id', 'seat', 'partner', 'at', 'type', 'code', 'use', 'pair', 'share'], 'claims.csv': ['seq', 'claim', 'activity', 'partner', 'kind', 'min', 'amount'], 'adjudication.csv': ['seq', 'id', 'kind', 'evidence', 'related']}
SEQUENCE = {'evidence.csv': 'single', 'claims.csv': 'accepted', 'adjudication.csv': 'e6'}

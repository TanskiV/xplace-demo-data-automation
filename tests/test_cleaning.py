import unittest

from data_automation.cleaning import clean_rows


class CleaningTests(unittest.TestCase):
    def test_normalizes_deduplicates_and_reports_invalid_rows(self):
        rows, report = clean_rows(
            [
                {" ID ": "1", "Email": " alice@example.test ", "Name": " Alice "},
                {"ID": "1", "Email": "alice@example.test", "Name": "Alice"},
                {"ID": "2", "Email": "", "Name": "Missing"},
            ]
        )
        self.assertEqual(rows, [{"id": "1", "email": "alice@example.test", "name": "Alice"}])
        self.assertEqual(report["duplicate_rows_removed"], 1)
        self.assertEqual(report["missing_required_rows"], 1)
        self.assertEqual(report["output_rows"], 1)


if __name__ == "__main__":
    unittest.main()

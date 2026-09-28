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

    def test_empty_input_is_deterministic(self):
        first = clean_rows([])
        second = clean_rows([])
        self.assertEqual(first, second)
        self.assertEqual(first[0], [])

    def test_utf8_and_quoted_values_are_preserved(self):
        rows, report = clean_rows(
            [{"ID": "7", "Email": "dana@example.test", "Name": 'Dana, "D" — שלום'}]
        )
        self.assertEqual(rows[0]["name"], 'Dana, "D" — שלום')
        self.assertEqual(report["output_rows"], 1)


if __name__ == "__main__":
    unittest.main()

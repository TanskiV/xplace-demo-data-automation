# Data Automation Demo

Demonstration/reference project; not client work. It uses synthetic sample data
and requires no credentials.

Small reference project showing a repeatable CSV/Excel data-cleaning workflow.
It loads tabular records, normalizes headers and values, validates required
fields, removes exact duplicates, and exports clean CSV plus a validation
report.

This is a demonstration/reference project with synthetic data. It is not a
client project and contains no private data.

## Run

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -e '.[excel,test]'
python -m data_automation.cli examples/input.csv --output-dir build
```

For `.xlsx` input, the optional `excel` extra installs `openpyxl`.

## Example output

The command writes `build/cleaned.csv` and `build/validation.json`.

## Test

```bash
python -m unittest discover -s tests -v
```

The test suite is network-independent and writes no files outside its temporary
test workspace.

## Business problem

Operational spreadsheets often contain inconsistent headers, whitespace,
duplicate rows and missing required values. This utility makes those changes
explicit, reproducible and reviewable before the cleaned file is used downstream.

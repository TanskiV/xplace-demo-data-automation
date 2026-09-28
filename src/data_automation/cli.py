from __future__ import annotations

import argparse
from pathlib import Path

from .cleaning import clean_rows
from .io import read_rows, write_outputs


def main() -> None:
    parser = argparse.ArgumentParser(description="Clean and validate CSV/XLSX records")
    parser.add_argument("input", type=Path)
    parser.add_argument("--output-dir", type=Path, default=Path("build"))
    args = parser.parse_args()
    rows, report = clean_rows(read_rows(args.input))
    write_outputs(rows, report, args.output_dir)
    print(f"Wrote {report['output_rows']} cleaned rows to {args.output_dir}")


if __name__ == "__main__":
    main()

from __future__ import annotations

import re
from collections.abc import Iterable, Mapping


def normalize_header(value: object) -> str:
    text = str(value or "").strip().lower()
    return re.sub(r"[^a-z0-9]+", "_", text).strip("_")


def clean_rows(
    rows: Iterable[Mapping[object, object]],
    *,
    required: tuple[str, ...] = ("id", "email"),
) -> tuple[list[dict[str, str]], dict[str, object]]:
    """Normalize, validate and deduplicate rows without mutating input."""
    cleaned: list[dict[str, str]] = []
    seen: set[tuple[tuple[str, str], ...]] = set()
    missing_required = 0
    duplicate_rows = 0

    for source in rows:
        normalized = {
            normalize_header(key): str(value or "").strip()
            for key, value in source.items()
        }
        if any(not normalized.get(field) for field in required):
            missing_required += 1
            continue
        fingerprint = tuple(sorted(normalized.items()))
        if fingerprint in seen:
            duplicate_rows += 1
            continue
        seen.add(fingerprint)
        cleaned.append(normalized)

    report = {
        "input_rows": len(cleaned) + missing_required + duplicate_rows,
        "output_rows": len(cleaned),
        "missing_required_rows": missing_required,
        "duplicate_rows_removed": duplicate_rows,
    }
    return cleaned, report

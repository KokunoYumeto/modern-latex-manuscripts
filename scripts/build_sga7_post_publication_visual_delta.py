#!/usr/bin/env python3
"""Build a rights-blocked metadata delta against the public SGA7 image index."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path


PRIVATE_MARKERS = (
    "c:\\users\\",
    "c:/users/",
    "appdata",
    "papors",
    "chatnotes",
    ".claude",
    ".codex",
)
EXPECTED_PARENT_SHA256 = (
    "9CD40FF06EB1E488AF385A56899D4F492492A06A1E2E3C0ED6876B82E3E3603F"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline-index", type=Path, required=True)
    parser.add_argument("--candidate-index", type=Path, required=True)
    parser.add_argument("--candidate-validation", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--cutoff-local", required=True)
    parser.add_argument("--checked-at", required=True)
    parser.add_argument("--sga-record", type=int, required=True)
    return parser.parse_args()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError(f"Missing CSV header: {path}")
        rows = list(reader)
    return list(reader.fieldnames), rows


def write_csv(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def csv_errors(path: Path) -> list[str]:
    fields, rows = read_csv(path)
    errors: list[str] = []
    for row_number, row in enumerate(rows, start=2):
        if set(row) != set(fields):
            errors.append(f"nonrectangular:{path.name}:{row_number}")
        for field, value in row.items():
            if value and re.match(r"^[=+\-@]", value):
                errors.append(
                    f"formula_unsafe:{path.name}:{row_number}:{field}"
                )
    return errors


def json_write(path: Path, value: object) -> None:
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    args = parse_args()
    baseline_path = args.baseline_index.resolve()
    candidate_path = args.candidate_index.resolve()
    candidate_validation_path = args.candidate_validation.resolve()
    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)

    baseline_fields, baseline = read_csv(baseline_path)
    candidate_fields, candidate = read_csv(candidate_path)
    if candidate_fields != baseline_fields:
        raise ValueError("Candidate and baseline index schemas differ")

    with candidate_validation_path.open("r", encoding="utf-8") as handle:
        candidate_validation = json.load(handle)
    if candidate_validation.get("status") != "PASS_METADATA_CUSTODY_READY":
        raise ValueError("Candidate inventory did not pass its custody gate")
    parent = candidate_validation.get("parent_pdf", {})
    if parent.get("sha256") != EXPECTED_PARENT_SHA256:
        raise ValueError("Unexpected parent scan identity")

    baseline_by_hash: dict[str, dict[str, str]] = {}
    for row in baseline:
        digest = row["sha256"].upper()
        if digest in baseline_by_hash:
            raise ValueError(f"Duplicate baseline hash: {digest}")
        baseline_by_hash[digest] = row

    new_rows: list[dict[str, object]] = []
    overlap_rows: list[dict[str, object]] = []
    for row in candidate:
        digest = row["sha256"].upper()
        baseline_row = baseline_by_hash.get(digest)
        if baseline_row:
            overlap_rows.append(
                {
                    "candidate_root_id": row["root_id"],
                    "candidate_relative_path": row["relative_path"],
                    "bytes": row["bytes"],
                    "sha256": digest,
                    "baseline_visual_id": baseline_row["visual_id"],
                    "baseline_root_id": baseline_row["root_id"],
                    "baseline_relative_path": baseline_row["relative_path"],
                    "disposition": "already_represented_by_hash",
                }
            )
            continue
        new_rows.append(dict(row))

    new_rows.sort(
        key=lambda row: (
            str(row["sha256"]).upper(),
            str(row["root_id"]),
            str(row["relative_path"]).casefold(),
        )
    )
    for number, row in enumerate(new_rows, start=1):
        row["visual_id"] = f"SGA7I-POSTCUT-VIS-{number:05d}"
    overlap_rows.sort(key=lambda row: str(row["sha256"]))

    delta_path = output / "SGA7I_POST_PUBLICATION_VISUAL_EVIDENCE_DELTA.csv"
    overlap_path = output / "SGA7I_POST_PUBLICATION_BASELINE_OVERLAPS.csv"
    readme_path = output / "README.md"
    validation_path = output / "VALIDATION.json"
    checksums_path = output / "SHA256SUMS.csv"

    write_csv(delta_path, candidate_fields, new_rows)
    overlap_fields = [
        "candidate_root_id",
        "candidate_relative_path",
        "bytes",
        "sha256",
        "baseline_visual_id",
        "baseline_root_id",
        "baseline_relative_path",
        "disposition",
    ]
    write_csv(overlap_path, overlap_fields, overlap_rows)

    new_bytes = sum(int(row["bytes"]) for row in new_rows)
    overlap_bytes = sum(int(row["bytes"]) for row in overlap_rows)
    evidence_classes = Counter(str(row["evidence_class"]) for row in new_rows)
    page_resolved = sum(bool(row["parent_pdf_index_0based"]) for row in new_rows)
    generator_resolved = sum(bool(row["generator_script_sha256"]) for row in new_rows)
    readme = f"""# SGA 7 I post-publication visual-evidence delta

This metadata-only checkpoint records high-detail source-audit images created
after the public SGA 7 I visual-evidence inventory cutoff at
`{args.cutoff_local}`. It contains no image pixels and no private absolute
paths.

- candidate scratch instances replayed: {len(candidate)} / {sum(int(row['bytes']) for row in candidate):,} bytes;
- hashes not represented in the public baseline: {len(new_rows)} / {new_bytes:,} bytes;
- hashes already represented in the public baseline: {len(overlap_rows)} / {overlap_bytes:,} bytes;
- parent scan SHA-256: `{EXPECTED_PARENT_SHA256}`;
- existing SGA record at classification time: `{args.sga_record}`.

Every new row is `rights_blocked_not_public`. The CSV records hashes,
dimensions, provisional page/folio mappings, linked TeX identities, recovered
generator identities, and QA disposition. Page and bounding-box fields remain
blank where they were not recoverable from filenames or generator code.

The images are source-derived audit witnesses, not a translation release,
complete visual audit, source-fidelity certification, critical edition, or
rights clearance. Expose IX remains incomplete and contains explicit
non-transcription placeholders; this delta does not change the current public
reader or authorize a Zenodo successor.
"""
    readme_path.write_text(readme, encoding="utf-8")

    errors = [
        *csv_errors(delta_path),
        *csv_errors(overlap_path),
    ]
    if len(candidate) != len(new_rows) + len(overlap_rows):
        errors.append("candidate_partition_mismatch")
    if len({str(row["sha256"]) for row in new_rows}) != len(new_rows):
        errors.append("duplicate_new_hash")
    if any(
        row["publication_disposition"] != "rights_blocked_not_public"
        for row in new_rows
    ):
        errors.append("unexpected_publication_disposition")
    output_text = "\n".join(
        path.read_text(encoding="utf-8", errors="replace").lower()
        for path in (delta_path, overlap_path, readme_path)
    )
    errors.extend(
        f"privacy_marker:{marker}"
        for marker in PRIVATE_MARKERS
        if marker in output_text
    )

    validation = {
        "status": "PASS_GITHUB_METADATA_CUSTODY_READY" if not errors else "FAIL",
        "errors": errors,
        "checked_at": args.checked_at,
        "cutoff_local": args.cutoff_local,
        "existing_sga_record": args.sga_record,
        "parent_pdf": {
            "bytes": parent.get("bytes"),
            "sha256": parent.get("sha256"),
            "pages": parent.get("pages"),
            "included": False,
        },
        "baseline": {
            "rows": len(baseline),
            "index_bytes": baseline_path.stat().st_size,
            "index_sha256": sha256(baseline_path),
        },
        "candidate_inventory": {
            "instances": len(candidate),
            "bytes": sum(int(row["bytes"]) for row in candidate),
            "index_sha256": sha256(candidate_path),
            "validation_sha256": sha256(candidate_validation_path),
        },
        "new_unique_images": len(new_rows),
        "new_unique_image_bytes": new_bytes,
        "baseline_overlaps": len(overlap_rows),
        "baseline_overlap_bytes": overlap_bytes,
        "page_resolved": page_resolved,
        "generator_resolved": generator_resolved,
        "evidence_classes": dict(sorted(evidence_classes.items())),
        "publication_dispositions": {"rights_blocked_not_public": len(new_rows)},
        "image_pixels_included": 0,
        "metadata_files": {
            delta_path.name: {
                "bytes": delta_path.stat().st_size,
                "sha256": sha256(delta_path),
                "rows": len(new_rows),
            },
            overlap_path.name: {
                "bytes": overlap_path.stat().st_size,
                "sha256": sha256(overlap_path),
                "rows": len(overlap_rows),
            },
            readme_path.name: {
                "bytes": readme_path.stat().st_size,
                "sha256": sha256(readme_path),
            },
        },
    }
    json_write(validation_path, validation)

    checksum_rows = []
    for path in sorted(
        (delta_path, overlap_path, readme_path, validation_path),
        key=lambda item: item.name.casefold(),
    ):
        checksum_rows.append(
            {"path": path.name, "bytes": path.stat().st_size, "sha256": sha256(path)}
        )
    write_csv(checksums_path, ["path", "bytes", "sha256"], checksum_rows)

    if errors:
        raise RuntimeError(errors)
    print(json.dumps(validation, indent=2, ensure_ascii=True))
    print(
        json.dumps(
            {
                "SHA256SUMS.csv": {
                    "bytes": checksums_path.stat().st_size,
                    "sha256": sha256(checksums_path),
                    "rows": len(checksum_rows),
                }
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()

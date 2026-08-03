#!/usr/bin/env python3
"""Accept and project the immutable FAC blind-comparator methodology handoff.

The producer package is preserved byte-for-byte in private custody.  This
builder creates a separate public projection, applies only operational privacy
redactions, regenerates the self-excluding payload manifest, and emits a
transport-acceptance record that explicitly makes no publication/readback
claim.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import shutil
from collections import Counter
from pathlib import Path


HANDOFF_ID = "FAC-METHODOLOGY-BLIND-COMPARATOR-DUAL-DOI-HANDOFF-20260803-R1"
EXPECTED_FILES = 19
EXPECTED_BYTES = 734_768
EXPECTED_TREE_SHA256 = "FD7414EDC70BB86B9968AD2328FA2C1B3F619788E6665F11C97EDADB0FBEF1B8"
EXPECTED_SOURCE_MANIFEST_BYTES = 2_035
EXPECTED_SOURCE_MANIFEST_SHA256 = "F9A196A143AB004E2BB167FE46F1953F11A60A3505B15870EFE8C005EC920B8D"
EXPECTED_CONTROL_BYTES = 2_296
EXPECTED_CONTROL_SHA256 = "BFA1E3A3EDA94E8C3425BAE50C842610A47D508FB260BF761BA3206883012679"
EXPECTED_PRIVATE_CUSTODY_TREE_SHA256 = EXPECTED_TREE_SHA256

MANIFEST_NAME = "ZENODO_PAYLOAD_MANIFEST.csv"
CONTROL_NAME = "PROJECT_LOGBOOK_METHODOLOGY_REPLICATION_DOI_REQUIREMENT_20260802.md"
DIRECT_PROVENANCE = [
    "FAC_PROJECT_LOGBOOK_SNAPSHOT.md",
    "FAC_EDITORIAL_DECISION_LOGBOOK_SNAPSHOT.md",
    "FAC_EDITORIAL_SELF_CORRECTION_LEDGER_PRIVACY_CLEAN.csv",
]

TASK_ID_RE = re.compile(
    r"(?i)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
)
WINDOWS_USER_HOME_RE = re.compile(
    r"(?i)(?:\\\\\?\\)?[A-Z]:[\\/]+Users[\\/]+[^\\/\s\"'<>|`\r\n]+"
)
POSIX_USER_HOME_RE = re.compile(
    r"(?i)(?<![A-Za-z0-9_])/(?:home|Users)/[^/\s\"'<>|`\r\n]+"
)
# Match a drive root only when it starts a path-like token.  This deliberately
# does not treat mathematical punctuation or arbitrary colon notation as a
# machine path.
WINDOWS_ROOT_RE = re.compile(r"(?i)(?<![A-Za-z0-9_])[A-Z]:[\\/]+(?=[A-Za-z0-9_.-])")
INTERNAL_STAGING_RE = re.compile(r"(?i)06_publication_candidates")
CODEX_STATE_RE = re.compile(r"(?i)(?<![A-Za-z0-9_])\.codex(?![A-Za-z0-9_])")
SECRET_LITERAL_RE = re.compile(
    r"(?i)(?:github_pat_[A-Za-z0-9_]{12,}|gh[pousr]_[A-Za-z0-9_]{12,}|"
    r"AKIA[0-9A-Z]{16}|sk-[A-Za-z0-9_-]{16,})"
)
CREDENTIAL_ASSIGNMENT_RE = re.compile(
    r"(?im)(\b(?:api[_-]?key|access[_-]?token|authorization|password|passwd|"
    r"client[_-]?secret|zenodo[_-]?token|github[_-]?token)\b[ \t]*[:=][ \t]*)"
    r"(?:\"[^\"\r\n]*\"|'[^'\r\n]*'|[^\s,;\r\n]+)"
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def csv_bytes(header: list[str], rows: list[list[object]]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.writer(stream, lineterminator="\n")
    writer.writerow(header)
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def identity_rows(root: Path) -> list[tuple[str, int, str]]:
    rows: list[tuple[str, int, str]] = []
    for path in sorted((item for item in root.iterdir() if item.is_file()), key=lambda item: item.name):
        data = path.read_bytes()
        rows.append((path.name, len(data), sha256_bytes(data)))
    return rows


def canonical_tree_sha256(rows: list[tuple[str, int, str]]) -> str:
    canonical = "".join(
        f"{relative}|{size}|{digest}\n" for relative, size, digest in rows
    ).encode("utf-8")
    return sha256_bytes(canonical)


def apply_rule(
    text: str,
    relative_path: str,
    rule: str,
    pattern: re.Pattern[str],
    replacement: str,
) -> tuple[str, list[dict[str, object]]]:
    actions: list[dict[str, object]] = []
    ordinal = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal ordinal
        ordinal += 1
        matched = match.group(0).encode("utf-8")
        actions.append(
            {
                "relative_path": relative_path,
                "rule": rule,
                "ordinal": ordinal,
                "line": text.count("\n", 0, match.start()) + 1,
                "matched_utf8_bytes": len(matched),
                "matched_sha256": sha256_bytes(matched),
                "replacement": replacement,
            }
        )
        return replacement

    return pattern.sub(replace, text), actions


def project_text(data: bytes, relative_path: str) -> tuple[bytes, list[dict[str, object]]]:
    text = data.decode("utf-8")
    actions: list[dict[str, object]] = []
    rules = (
        ("credential_assignment", CREDENTIAL_ASSIGNMENT_RE, r"\1<REDACTED_SECRET>"),
        ("secret_literal", SECRET_LITERAL_RE, "<REDACTED_SECRET>"),
        ("codex_task_id", TASK_ID_RE, "<REDACTED_TASK_ID>"),
        ("codex_state_directory", CODEX_STATE_RE, "<REDACTED_CODEX_STATE>"),
        ("windows_user_home", WINDOWS_USER_HOME_RE, "<REDACTED_USER_HOME>"),
        ("posix_user_home", POSIX_USER_HOME_RE, "<REDACTED_USER_HOME>"),
        ("windows_absolute_root", WINDOWS_ROOT_RE, "<REDACTED_LOCAL_ROOT>/"),
        (
            "internal_publication_staging_segment",
            INTERNAL_STAGING_RE,
            "<REDACTED_INTERNAL_PUBLICATION_STAGING>",
        ),
    )
    for rule, pattern, replacement in rules:
        if rule == "credential_assignment":
            # Preserve the assignment label while replacing only its value.
            found: list[dict[str, object]] = []
            ordinal = 0

            def credential_replace(match: re.Match[str]) -> str:
                nonlocal ordinal
                ordinal += 1
                matched = match.group(0).encode("utf-8")
                found.append(
                    {
                        "relative_path": relative_path,
                        "rule": rule,
                        "ordinal": ordinal,
                        "line": text.count("\n", 0, match.start()) + 1,
                        "matched_utf8_bytes": len(matched),
                        "matched_sha256": sha256_bytes(matched),
                        "replacement": "<ASSIGNMENT_LABEL><REDACTED_SECRET>",
                    }
                )
                return match.group(1) + "<REDACTED_SECRET>"

            text = pattern.sub(credential_replace, text)
            actions.extend(found)
        else:
            text, found = apply_rule(text, relative_path, rule, pattern, replacement)
            actions.extend(found)
    return text.encode("utf-8"), actions


def residual_findings(text: str) -> list[tuple[str, int]]:
    patterns = (
        ("credential_assignment", CREDENTIAL_ASSIGNMENT_RE),
        ("secret_literal", SECRET_LITERAL_RE),
        ("codex_task_id", TASK_ID_RE),
        ("codex_state_directory", CODEX_STATE_RE),
        ("windows_user_home", WINDOWS_USER_HOME_RE),
        ("posix_user_home", POSIX_USER_HOME_RE),
        ("windows_absolute_root", WINDOWS_ROOT_RE),
        ("internal_publication_staging_segment", INTERNAL_STAGING_RE),
    )
    return [(name, len(pattern.findall(text))) for name, pattern in patterns if pattern.findall(text)]


def replay_source_manifest(source: Path) -> list[str]:
    errors: list[str] = []
    manifest_path = source / MANIFEST_NAME
    with manifest_path.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    if len(rows) != 18:
        errors.append(f"source manifest rows {len(rows)} != 18")
    expected = {path.name for path in source.iterdir() if path.is_file() and path.name != MANIFEST_NAME}
    declared = {row["relative_path"] for row in rows}
    if expected != declared:
        errors.append("source manifest file set differs from source package")
    for row in rows:
        path = source / row["relative_path"]
        if not path.is_file():
            errors.append(f"missing {row['relative_path']}")
            continue
        data = path.read_bytes()
        if len(data) != int(row["bytes"]):
            errors.append(f"byte mismatch {row['relative_path']}")
        if sha256_bytes(data) != row["sha256"].upper():
            errors.append(f"hash mismatch {row['relative_path']}")
    return errors


def validate_payload(payload: Path) -> dict[str, object]:
    errors: list[str] = []
    rows = identity_rows(payload)
    if len(rows) != EXPECTED_FILES:
        errors.append(f"public file count {len(rows)} != {EXPECTED_FILES}")
    names = {row[0] for row in rows}
    if set(DIRECT_PROVENANCE) - names:
        errors.append("one or more direct provenance surfaces are absent")

    json_results: dict[str, dict[str, object]] = {}
    csv_results: dict[str, dict[str, object]] = {}
    formula_candidates: list[dict[str, object]] = []
    residuals: dict[str, list[tuple[str, int]]] = {}
    for path in sorted(payload.iterdir(), key=lambda item: item.name):
        data = path.read_bytes()
        text = data.decode("utf-8")
        findings = residual_findings(text)
        if findings:
            residuals[path.name] = findings
        if path.suffix.lower() == ".json":
            try:
                parsed = json.loads(text)
            except json.JSONDecodeError as error:
                errors.append(f"JSON parse failure {path.name}: {error}")
                continue
            reported = parsed.get("errors", []) if isinstance(parsed, dict) else []
            if isinstance(reported, list) and reported:
                errors.append(f"reported JSON errors in {path.name}")
            json_results[path.name] = {
                "status": parsed.get("status") if isinstance(parsed, dict) else None,
                "reported_errors": len(reported) if isinstance(reported, list) else None,
            }
        if path.suffix.lower() == ".csv":
            with path.open(encoding="utf-8-sig", newline="") as stream:
                table = list(csv.reader(stream))
            widths = {len(row) for row in table}
            if len(widths) != 1:
                errors.append(f"nonrectangular CSV {path.name}")
            for row_number, row in enumerate(table[1:], 2):
                for column_number, cell in enumerate(row, 1):
                    value = cell.lstrip()
                    candidate = value.startswith(("=", "+", "@")) or (
                        value.startswith("-")
                        and re.fullmatch(r"-?\d+(?:\.\d+)?", value) is None
                    )
                    if candidate:
                        formula_candidates.append(
                            {
                                "file": path.name,
                                "row": row_number,
                                "column": column_number,
                            }
                        )
            csv_results[path.name] = {
                "data_rows": max(0, len(table) - 1),
                "columns": len(table[0]) if table else 0,
                "rectangular": len(widths) == 1,
            }
    if residuals:
        errors.append("public privacy residuals remain")
    if formula_candidates:
        errors.append("spreadsheet formula-injection candidates remain")

    with (payload / MANIFEST_NAME).open(encoding="utf-8", newline="") as stream:
        manifest = list(csv.DictReader(stream))
    expected = {path.name for path in payload.iterdir() if path.is_file() and path.name != MANIFEST_NAME}
    declared = {row["relative_path"] for row in manifest}
    if len(manifest) != 18 or expected != declared:
        errors.append("public self-excluding manifest file set mismatch")
    for row in manifest:
        path = payload / row["relative_path"]
        if not path.is_file():
            errors.append(f"public manifest missing {row['relative_path']}")
            continue
        data = path.read_bytes()
        if len(data) != int(row["bytes"]) or sha256_bytes(data) != row["sha256"].upper():
            errors.append(f"public manifest mismatch {row['relative_path']}")

    return {
        "status": "PASS_PUBLIC_TRANSPORT_PROJECTION" if not errors else "FAIL",
        "errors": errors,
        "file_count": len(rows),
        "total_bytes": sum(row[1] for row in rows),
        "canonical_tree_sha256": canonical_tree_sha256(rows),
        "manifest_rows": len(manifest),
        "manifest_replay_match_count": sum(
            1
            for row in manifest
            if (payload / row["relative_path"]).is_file()
            and len((payload / row["relative_path"]).read_bytes()) == int(row["bytes"])
            and sha256_bytes((payload / row["relative_path"]).read_bytes()) == row["sha256"].upper()
        ),
        "direct_provenance_surfaces": DIRECT_PROVENANCE,
        "json": json_results,
        "csv": csv_results,
        "formula_candidates": formula_candidates,
        "privacy_residuals": residuals,
        "external_full_pdf_source_or_image_files": [
            path.name
            for path in payload.iterdir()
            if path.suffix.lower()
            in {".pdf", ".tex", ".tar", ".gz", ".zip", ".png", ".jpg", ".jpeg", ".tif", ".tiff"}
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--accepted-at", required=True)
    parser.add_argument(
        "--private-custody-id",
        default="20260803T033607CEST_fac-blind-comparator-methodology-r1",
    )
    args = parser.parse_args()

    source = args.source.resolve()
    output = args.output.resolve()
    if not source.is_dir():
        raise SystemExit(f"source is not a directory: {source}")
    if output.exists():
        raise SystemExit(f"output already exists: {output}")
    temp = output.with_name(output.name + ".tmp")
    if temp.exists():
        raise SystemExit(f"temporary output already exists: {temp}")

    source_rows = identity_rows(source)
    source_errors = replay_source_manifest(source)
    if len(source_rows) != EXPECTED_FILES:
        source_errors.append(f"source file count {len(source_rows)} != {EXPECTED_FILES}")
    if sum(row[1] for row in source_rows) != EXPECTED_BYTES:
        source_errors.append("source total bytes mismatch")
    if canonical_tree_sha256(source_rows) != EXPECTED_TREE_SHA256:
        source_errors.append("source canonical tree mismatch")
    source_manifest = source / MANIFEST_NAME
    if source_manifest.stat().st_size != EXPECTED_SOURCE_MANIFEST_BYTES:
        source_errors.append("source manifest byte count mismatch")
    if sha256_bytes(source_manifest.read_bytes()) != EXPECTED_SOURCE_MANIFEST_SHA256:
        source_errors.append("source manifest hash mismatch")
    control = source / CONTROL_NAME
    if control.stat().st_size != EXPECTED_CONTROL_BYTES:
        source_errors.append("control byte count mismatch")
    if sha256_bytes(control.read_bytes()) != EXPECTED_CONTROL_SHA256:
        source_errors.append("control hash mismatch")
    if source_errors:
        raise SystemExit("source acceptance failed: " + " | ".join(source_errors))

    payload = temp / "payload"
    payload.mkdir(parents=True)
    actions: list[dict[str, object]] = []
    mapping: list[dict[str, object]] = []
    for relative, source_size, source_digest in source_rows:
        if relative == MANIFEST_NAME:
            continue
        source_data = (source / relative).read_bytes()
        public_data, found = project_text(source_data, relative)
        actions.extend(found)
        (payload / relative).write_bytes(public_data)
        mapping.append(
            {
                "relative_path": relative,
                "source_bytes": source_size,
                "source_sha256": source_digest,
                "public_bytes": len(public_data),
                "public_sha256": sha256_bytes(public_data),
                "privacy_action_count": len(found),
                "privacy_rules": ";".join(sorted({str(item["rule"]) for item in found})),
                "status": "PRIVACY_PROJECTED" if found else "BYTE_IDENTICAL",
            }
        )

    projected_rows = identity_rows(payload)
    manifest_data = csv_bytes(
        ["relative_path", "bytes", "sha256"],
        [[relative, size, digest] for relative, size, digest in projected_rows],
    )
    (payload / MANIFEST_NAME).write_bytes(manifest_data)
    actions.append(
        {
            "relative_path": MANIFEST_NAME,
            "rule": "manifest_regenerated_after_privacy_projection",
            "ordinal": 1,
            "line": 1,
            "matched_utf8_bytes": EXPECTED_SOURCE_MANIFEST_BYTES,
            "matched_sha256": EXPECTED_SOURCE_MANIFEST_SHA256,
            "replacement": "<REGENERATED_SELF_EXCLUDING_PUBLIC_MANIFEST>",
        }
    )
    mapping.append(
        {
            "relative_path": MANIFEST_NAME,
            "source_bytes": EXPECTED_SOURCE_MANIFEST_BYTES,
            "source_sha256": EXPECTED_SOURCE_MANIFEST_SHA256,
            "public_bytes": len(manifest_data),
            "public_sha256": sha256_bytes(manifest_data),
            "privacy_action_count": 1,
            "privacy_rules": "manifest_regenerated_after_privacy_projection",
            "status": "REGENERATED_TO_BIND_PUBLIC_PROJECTION",
        }
    )
    mapping.sort(key=lambda row: str(row["relative_path"]))

    validation = validate_payload(payload)
    if validation["errors"]:
        raise SystemExit("public projection validation failed: " + " | ".join(validation["errors"]))

    original_manifest = csv_bytes(
        ["relative_path", "bytes", "sha256"],
        [[relative, size, digest] for relative, size, digest in source_rows],
    )
    public_rows = identity_rows(payload)
    public_manifest = csv_bytes(
        [
            "relative_path",
            "source_bytes",
            "source_sha256",
            "public_bytes",
            "public_sha256",
            "privacy_action_count",
            "privacy_rules",
            "status",
        ],
        [
            [
                row["relative_path"],
                row["source_bytes"],
                row["source_sha256"],
                row["public_bytes"],
                row["public_sha256"],
                row["privacy_action_count"],
                row["privacy_rules"],
                row["status"],
            ]
            for row in mapping
        ],
    )
    action_ledger = csv_bytes(
        [
            "relative_path",
            "rule",
            "ordinal",
            "line",
            "matched_utf8_bytes",
            "matched_sha256",
            "replacement",
        ],
        [
            [
                action["relative_path"],
                action["rule"],
                action["ordinal"],
                action["line"],
                action["matched_utf8_bytes"],
                action["matched_sha256"],
                action["replacement"],
            ]
            for action in sorted(
                actions,
                key=lambda item: (
                    str(item["relative_path"]),
                    str(item["rule"]),
                    int(item["ordinal"]),
                ),
            )
        ],
    )

    (temp / "PRIVATE_ORIGINAL_IDENTITY_MANIFEST.csv").write_bytes(original_manifest)
    (temp / "PUBLIC_PROJECTION_IDENTITY_MANIFEST.csv").write_bytes(public_manifest)
    (temp / "PRIVACY_TRANSFORMATIONS.csv").write_bytes(action_ledger)
    (temp / "PUBLIC_PROJECTION_VALIDATION.json").write_bytes(json_bytes(validation))

    action_counts = Counter(str(item["rule"]) for item in actions)
    acceptance = {
        "schema": "fac-blind-comparator-archive-transport-acceptance-v1",
        "status": "ACCEPTED_IMMUTABLE_SOURCE_AND_PRIVACY_CLEAN_PUBLIC_TRANSPORT",
        "errors": [],
        "accepted_at": args.accepted_at,
        "handoff_id": HANDOFF_ID,
        "private_custody_id": args.private_custody_id,
        "source": {
            "file_count": len(source_rows),
            "total_bytes": sum(row[1] for row in source_rows),
            "canonical_tree_sha256": canonical_tree_sha256(source_rows),
            "self_excluding_manifest_rows": 18,
            "self_excluding_manifest_bytes": EXPECTED_SOURCE_MANIFEST_BYTES,
            "self_excluding_manifest_sha256": EXPECTED_SOURCE_MANIFEST_SHA256,
            "manifest_replay_matches": 18,
            "manifest_replay_errors": 0,
            "preserved_unchanged_in_private_custody": True,
        },
        "public_projection": {
            "file_count": len(public_rows),
            "total_bytes": sum(row[1] for row in public_rows),
            "canonical_tree_sha256": canonical_tree_sha256(public_rows),
            "self_excluding_manifest_rows": 18,
            "self_excluding_manifest_bytes": (payload / MANIFEST_NAME).stat().st_size,
            "self_excluding_manifest_sha256": sha256_bytes((payload / MANIFEST_NAME).read_bytes()),
            "manifest_replay_matches": 18,
            "manifest_replay_errors": 0,
            "privacy_action_count": len(actions),
            "privacy_actions_by_rule": dict(sorted(action_counts.items())),
            "privacy_residual_count": 0,
            "direct_provenance_surfaces": DIRECT_PROVENANCE,
        },
        "rights": {
            "external_comparator_full_pdf_or_source_files": 0,
            "external_redistribution_license_found": False,
            "external_authorship_public_urls_sizes_hashes_and_locator_findings_only": True,
        },
        "scope": {
            "blind_fac_numbers": "1-79",
            "personally_adjudicated": "79/79",
            "comparator_assisted_numbers_excluded": "80-81",
            "qualitative_only": True,
            "scalar_score_ranking_certification_or_general_superiority_claim": False,
            "continuation_cursor": None,
            "fac_gaga_whole_project_completion_claim": False,
        },
        "routing": {
            "methodology_concept_doi": "10.5281/zenodo.21124403",
            "replication_concept_doi": "10.5281/zenodo.20461174",
            "duplicate_concept_authorized": False,
        },
        "publication": {
            "claimed": False,
            "record_ids": [],
            "dois": [],
            "public_readback_claimed": False,
        },
    }
    (temp / "ARCHIVE_TRANSPORT_ACCEPTANCE.json").write_bytes(json_bytes(acceptance))
    readme = f"""# FAC blind-comparator methodology evidence: archive transport

This directory records byte-level acceptance of producer handoff `{HANDOFF_ID}`.

- Exact producer source: {len(source_rows)} files / {sum(row[1] for row in source_rows):,} bytes / canonical tree SHA-256 `{canonical_tree_sha256(source_rows)}`.
- Derived public projection: {len(public_rows)} files / {sum(row[1] for row in public_rows):,} bytes / canonical tree SHA-256 `{canonical_tree_sha256(public_rows)}`.
- Privacy actions: {len(actions)}; residual findings: 0.
- The producer bytes remain unchanged in private custody. Public transformations are enumerated mechanically in `PRIVACY_TRANSFORMATIONS.csv` and bound source-to-public in `PUBLIC_PROJECTION_IDENTITY_MANIFEST.csv`.
- `ARCHIVE_TRANSPORT_ACCEPTANCE.json` is transport acceptance only. It makes no Zenodo publication or public-readback claim.
- The full Achinger--Krupa PDF/source are not redistributed. The evidence remains qualitative and chronology-bounded to FAC nos. 1--79; nos. 80--81 are excluded from blind claims.

The 19 files under `payload/` are the exact derived public payload intended for both existing methodology and replication DOI lineages. The project logbook, editorial-decision logbook, and append-only self-correction ledger remain direct files.
"""
    (temp / "README.md").write_text(readme, encoding="utf-8", newline="\n")

    output.parent.mkdir(parents=True, exist_ok=True)
    temp.rename(output)
    print(
        json.dumps(
            {
                "status": acceptance["status"],
                "source_files": len(source_rows),
                "source_bytes": sum(row[1] for row in source_rows),
                "source_tree_sha256": canonical_tree_sha256(source_rows),
                "public_files": len(public_rows),
                "public_bytes": sum(row[1] for row in public_rows),
                "public_tree_sha256": canonical_tree_sha256(public_rows),
                "privacy_actions": len(actions),
                "output": output.as_posix(),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

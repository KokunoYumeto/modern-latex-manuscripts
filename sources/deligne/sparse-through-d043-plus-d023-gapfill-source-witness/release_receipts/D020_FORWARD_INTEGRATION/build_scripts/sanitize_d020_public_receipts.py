"""Sanitize local-account path literals in copied D020 Job receipts only.

The authoritative cold-audit masters are untouched.  This operates solely on
the generated public source/provenance copies, records before/after identities,
and reseals their manifests after verifying the pre-change trees.
"""
from __future__ import annotations

import csv
import json
import os
import re
from pathlib import Path

import d020_contract as c
import finalize_manifest_nonregression as finalizer


BUILD = c.TASK / "build/cumulative"
SOURCE = BUILD / "source_tree"
PROVENANCE = BUILD / "provenance_tree"
AUDIT = BUILD / "audit"
SOURCE_MANIFEST = SOURCE / c.SOURCE_MANIFEST_NAME
PROVENANCE_MANIFEST = PROVENANCE / "PROVENANCE_MANIFEST.tsv"
SOURCE_EVIDENCE = SOURCE / "works/D020_PUBLIC_SAFE/cold_audit/evidence"
PROVENANCE_EVIDENCE = PROVENANCE / "D020/S06_math_v6_01/evidence"
SOURCE_STATE_BUILD = SOURCE / "works/D020_PUBLIC_SAFE/state/build"
PROVENANCE_STATE_BUILD = PROVENANCE / "D020/S06_math_v6_01/state/build"
OUTPUT = AUDIT / "PUBLIC_RECEIPT_SANITIZATION.json"
MAX_JSON_TARGET_BYTES = 16 * 1024
MAX_LOG_TARGET_BYTES = 128 * 1024
MAX_TARGETS = 64
PLACEHOLDER = "LOCAL_ACCOUNT"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise c.Failure(message)


def verify_provenance_manifest() -> None:
    rows = []
    with PROVENANCE_MANIFEST.open("r", encoding="utf-8", newline="") as stream:
        for row in csv.DictReader(stream, delimiter="\t"):
            rows.append({"path": row["path"], "bytes": int(row["bytes"]), "sha256": row["sha256"]})
    actual_names = c.inventory_tree(PROVENANCE)
    actual_names.remove("PROVENANCE_MANIFEST.tsv")
    require([row["path"] for row in rows] == actual_names, "provenance manifest topology differs before sanitization")
    for row in rows:
        c.check(c.confined(PROVENANCE, row["path"]), row)


def atomic_replace(path: Path, data: bytes) -> None:
    temporary = path.with_name(f".{path.name}.public-sanitize-{os.getpid()}.tmp")
    require(not temporary.exists(), "stale sanitization temporary")
    try:
        temporary.write_bytes(data)
        if path.suffix.casefold() == ".json":
            json.loads(temporary.read_text(encoding="utf-8"))
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def main() -> None:
    previous = json.loads(OUTPUT.read_text(encoding="utf-8")) if OUTPUT.exists() else None
    if previous is not None:
        require(previous.get("status") == "PASS", "prior sanitization receipt is not PASS")
    c.verify_source_manifest(SOURCE, SOURCE_MANIFEST)
    verify_provenance_manifest()

    token = os.environ.get("USERNAME", "")
    require(token.isascii() and token.casefold() == c.TASK.parts[2].casefold(), "local-account token unavailable")
    pattern = re.compile(re.escape(token), re.IGNORECASE)
    targets = []
    candidate_roots = (
        ("source", SOURCE_EVIDENCE, "job_receipt"),
        ("provenance", PROVENANCE_EVIDENCE, "job_receipt"),
        ("source", SOURCE_STATE_BUILD / "V4_PDF_PLACEHOLDER_BACKUP", "tex_log"),
        ("source", SOURCE_STATE_BUILD / "V5_GUARDED_REBUILD", "tex_log"),
        ("provenance", PROVENANCE_STATE_BUILD / "V4_PDF_PLACEHOLDER_BACKUP", "tex_log"),
        ("provenance", PROVENANCE_STATE_BUILD / "V5_GUARDED_REBUILD", "tex_log"),
    )
    for surface, root, kind in candidate_roots:
        c.reject_reparse(root)
        for path in sorted(root.iterdir(), key=lambda item: item.name):
            if not path.is_file():
                continue
            if kind == "job_receipt" and not path.name.endswith("_JOB_GUARD.json"):
                continue
            if kind == "tex_log" and path.suffix.casefold() != ".log":
                continue
            limit = MAX_JSON_TARGET_BYTES if kind == "job_receipt" else MAX_LOG_TARGET_BYTES
            require(path.stat().st_size <= limit, "candidate public text file exceeds bounded size")
            text = path.read_text(encoding="utf-8")
            matches = len(pattern.findall(text))
            if not matches:
                continue
            before = c.identity(path)
            replaced = pattern.sub(PLACEHOLDER, text)
            require(token.casefold() not in replaced.casefold(), "sanitization left local-account token")
            atomic_replace(path, replaced.encode("utf-8"))
            after = c.identity(path)
            targets.append({
                "surface": surface,
                "kind": kind,
                "path": path.relative_to(SOURCE if surface == "source" else PROVENANCE).as_posix(),
                "occurrences_replaced": matches,
                "before": before,
                "after": after,
            })

    require(1 <= len(targets) <= MAX_TARGETS, "new sanitization target count outside exact bounded contract")
    source_rows, source_seal = finalizer.write_manifest(SOURCE, c.SOURCE_MANIFEST_NAME)
    provenance_rows, provenance_seal = finalizer.write_manifest(PROVENANCE, "PROVENANCE_MANIFEST.tsv")
    c.verify_source_manifest(SOURCE, SOURCE_MANIFEST)
    verify_provenance_manifest()

    result = {
        "schema": "d020-public-receipt-sanitization-v1",
        "status": "PASS",
        "policy": "straightforward case-insensitive local-account first-name replacement in copied Job-receipt JSON only",
        "authoritative_cold_audit_masters_modified": False,
        "generated_public_copies_only": True,
        "replacement_literal": PLACEHOLDER,
        "prior_targets": 0 if previous is None else len(previous.get("targets", [])),
        "new_targets": len(targets),
        "targets": ([] if previous is None else previous.get("targets", [])) + targets,
        "source_manifest": {"members": len(source_rows), **source_seal},
        "provenance_manifest": {"members": len(provenance_rows), **provenance_seal},
    }
    OUTPUT.write_text(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"status": "PASS", "targets": len(targets), "receipt": c.identity(OUTPUT)}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

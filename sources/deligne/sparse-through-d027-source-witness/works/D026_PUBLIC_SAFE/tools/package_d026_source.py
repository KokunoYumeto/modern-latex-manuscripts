#!/usr/bin/env python3
"""Create the deterministic, provenance-bearing D026 editable-source ZIP."""

from __future__ import annotations

import argparse
import hashlib
import json
import zipfile
from pathlib import Path


FIXED_ZIP_TIME = (1980, 1, 1, 0, 0, 0)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def add_spec(specs: list[tuple[str, str, str]], role: str, source: str, archive_path: str) -> None:
    specs.append((role, source, archive_path))


def zip_info(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, date_time=FIXED_ZIP_TIME)
    info.create_system = 3
    info.external_attr = (0o100644 & 0xFFFF) << 16
    info.compress_type = zipfile.ZIP_DEFLATED
    info.flag_bits |= 0x800
    return info


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    base = args.base.resolve()

    specs: list[tuple[str, str, str]] = []
    add_spec(specs, "PACKAGE_README", "source/README.md", "README.md")
    add_spec(specs, "CANONICAL_EDITABLE_SOURCE", "source/Deligne_D026_FR.tex", "editions/Deligne_D026_FR.tex")
    add_spec(specs, "CANONICAL_EDITABLE_SOURCE", "source/Deligne_D026_EN.tex", "editions/Deligne_D026_EN.tex")
    add_spec(specs, "RESTRAINED_APPARATUS_SOURCE", "source/Deligne_D026_APPARATUS.tex", "editions/Deligne_D026_APPARATUS.tex")
    add_spec(specs, "ASSET_LEDGER_EMPTY_SEMANTIC_REPLAY", "source/ASSET_LEDGER.tsv", "assets/ASSET_LEDGER.tsv")
    add_spec(specs, "CANONICAL_BUILT_READER", "output/pdf/Deligne_D026_FR.pdf", "built/Deligne_D026_FR.pdf")
    add_spec(specs, "CANONICAL_BUILT_READER", "output/pdf/Deligne_D026_EN.pdf", "built/Deligne_D026_EN.pdf")

    add_spec(specs, "CONTROLLING_AUTHORITY", "input/expanded_state/source/20_AUTHORITY_DELIGNE_D026_LOCAL_CONSTANTS_ARTIN_ORTHOGONAL_18PP_IAS_300DPI.pdf", "witnesses/authority/20_AUTHORITY_DELIGNE_D026_LOCAL_CONSTANTS_ARTIN_ORTHOGONAL_18PP_IAS_300DPI.pdf")
    add_spec(specs, "LOWER_AUTHORITY_COMPARATOR", "input/expanded_state/source/21_COMPARATOR_DELIGNE_D026_LOCAL_CONSTANTS_ARTIN_ORTHOGONAL_18PP_COLLECTED_SPLIT.pdf", "witnesses/comparator/21_COMPARATOR_DELIGNE_D026_LOCAL_CONSTANTS_ARTIN_ORTHOGONAL_18PP_COLLECTED_SPLIT.pdf")
    for name in ("source_language.ndjson", "english_standalone.ndjson", "apparatus.ndjson", "salvage_comparison.tsv", "asset_ledger.tsv"):
        add_spec(specs, "RETURNED_MACHINE_RECORD", f"input/expanded_state/edition/{name}", f"records/{name}")
    for name in ("PAGE_MAP.tsv", "CRITICAL_PIXEL_FACTS.tsv", "SESSION_PLAN.tsv"):
        add_spec(specs, "RETURNED_CONTROL_RECORD", f"input/expanded_state/control/{name}", f"control/{name}")
    add_spec(specs, "RETURNED_COVERAGE_RECORD", "input/expanded_state/coverage/coverage.tsv", "control/coverage.tsv")
    for name in ("S02_CANON_AUDIT.tsv", "S03_CANON_AUDIT.tsv", "S03_COLD_AUDIT.tsv", "SESSION_LOG.tsv"):
        add_spec(specs, "RETURNED_AUDIT_WITNESS", f"input/expanded_state/audit/{name}", f"returned_audit/{name}")

    add_spec(specs, "MAINTENANCE_INTAKE_RECEIPT", "evidence/INTAKE_AND_AUTHORITY_RECEIPT.json", "maintenance_evidence/INTAKE_AND_AUTHORITY_RECEIPT.json")
    add_spec(specs, "SANITIZED_ZERO_ACCEPTED_LEDGER", "evidence/SANITIZED_ZERO_ACCEPTED_PRIOR_WORK_LEDGER.tsv", "maintenance_evidence/SANITIZED_ZERO_ACCEPTED_PRIOR_WORK_LEDGER.tsv")
    add_spec(specs, "ZERO_ACCEPTED_PRESERVATION_RECEIPT", "evidence/ZERO_ACCEPTED_PRESERVATION_RECEIPT.json", "maintenance_evidence/ZERO_ACCEPTED_PRESERVATION_RECEIPT.json")
    add_spec(specs, "MAINTENANCE_COLD_AUDIT", "qa/cold_audit/COLD_AUDIT_REPORT.json", "maintenance_evidence/COLD_AUDIT_REPORT.json")
    add_spec(specs, "MAINTENANCE_FRESH_REPLAY", "qa/cold_audit/FRESH_NONPATCHING_REPLAY_REPORT.json", "maintenance_evidence/FRESH_NONPATCHING_REPLAY_REPORT.json")
    add_spec(specs, "MAINTENANCE_NONPATCHING_RECEIPT", "qa/cold_audit/NONPATCHING_REPLAY_RECEIPT.json", "maintenance_evidence/NONPATCHING_REPLAY_RECEIPT.json")
    add_spec(specs, "MAINTENANCE_VISUAL_AUDIT", "qa/cold_audit/MANUAL_VISUAL_COLD_AUDIT.tsv", "maintenance_evidence/MANUAL_VISUAL_COLD_AUDIT.tsv")
    add_spec(specs, "APPARATUS_BUILD_CHECK", "qa/cold_audit/APPARATUS_BUILD_CHECK.json", "maintenance_evidence/APPARATUS_BUILD_CHECK.json")
    add_spec(specs, "PUBLIC_PAYLOAD_SECURITY_SCAN", "qa/cold_audit/PUBLIC_PAYLOAD_COMPONENT_SECURITY_SCAN.json", "maintenance_evidence/PUBLIC_PAYLOAD_COMPONENT_SECURITY_SCAN.json")

    for name in ("build_d026_editions.py", "cold_audit_d026.py", "nonpatching_replay_d026.py", "package_d026_source.py", "sanitize_prior_ledger.py"):
        add_spec(specs, "MAINTENANCE_TOOL", f"tools/{name}", f"tools/{name}")

    payloads: list[tuple[str, str, bytes]] = []
    for role, source_rel, archive_path in specs:
        source = base / source_rel
        if not source.is_file():
            raise FileNotFoundError(source)
        payloads.append((role, archive_path, source.read_bytes()))

    manifest_lines = ["role\tpath\tbytes\tsha256"]
    for role, archive_path, data in sorted(payloads, key=lambda row: row[1]):
        manifest_lines.append(f"{role}\t{archive_path}\t{len(data)}\t{sha256_bytes(data)}")
    manifest = ("\n".join(manifest_lines) + "\n").encode("utf-8")
    payloads.append(("PACKAGE_MANIFEST", "PACKAGE_MANIFEST.tsv", manifest))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(args.output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9, strict_timestamps=True) as archive:
        for _role, archive_path, data in sorted(payloads, key=lambda row: row[1]):
            archive.writestr(zip_info(archive_path), data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)

    with zipfile.ZipFile(args.output) as archive:
        if archive.testzip() is not None:
            raise RuntimeError("deterministic ZIP failed CRC replay")
        members = len(archive.infolist())
    output_bytes = args.output.read_bytes()
    print(json.dumps({
        "result": "PASS",
        "filename": args.output.name,
        "bytes": len(output_bytes),
        "sha256": sha256_bytes(output_bytes),
        "members": members,
        "fixed_member_timestamp": "1980-01-01T00:00:00",
    }, sort_keys=True))


if __name__ == "__main__":
    main()

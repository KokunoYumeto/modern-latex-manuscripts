#!/usr/bin/env python3
"""Build the FAC/Korean/Spanish-SGA provenance successor for both broad DOIs."""

from __future__ import annotations

import csv
import hashlib
import io
import json
import os
import re
import zipfile
from pathlib import Path

import build_korean_noether_unchecked_public_snapshots_20260804 as archive
import build_korean_noether_p04_complete_privacy_corrected_snapshot_20260804 as p04complete
import publish_current_reader_bundles_zenodo_20260730 as base
import publish_sga5_spanish_complete_zenodo_20260804 as spanish


REPO_ROOT = Path(__file__).resolve().parents[1]
INTERLANGUAGE_ROOT = Path(
    os.environ.get(
        "INTERLANGUAGE_ROOT",
        str(Path.home() / "Documents" / "interlanguage"),
    )
)
OUTPUT = (
    REPO_ROOT
    / "sources"
    / "provenance"
    / "fac-korean-sga5-dual-doi-provenance-20260804-r4"
)
FAC_ROOT = (
    INTERLANGUAGE_ROOT
    / "03_projects"
    / "language_management"
    / "english_germanic"
    / "06_publication_candidates"
    / "FAC_single_concept_complete_reader_blind_comparison_reference_v2_20260804_r4"
)
P03_ROOT = REPO_ROOT / "sources" / "noether" / "korean-unchecked-paper-03-20260804"
P04_ROOT = REPO_ROOT / "sources" / "noether" / "korean-unchecked-paper-04-t04-t06-20260804"
P04_T07_ROOT = REPO_ROOT / "sources" / "noether" / "korean-unchecked-paper-04-t07-20260804"
P04_COMPLETE_ROOT = (
    REPO_ROOT
    / "sources"
    / "noether"
    / "korean-unchecked-paper-04-complete-producer-draft-20260804"
)
NESTED_CORRECTION_ROOT = (
    REPO_ROOT
    / "sources"
    / "noether"
    / "korean-nested-zip-privacy-correction-20260804-r2"
)
KOREAN_INITIAL_ROOT = (
    REPO_ROOT / "sources" / "noether" / "korean-unchecked-papers-01-05-07-41-42-20260804"
)
METHODOLOGY_RECORD = 21783420
METHODOLOGY_CONCEPT_DOI = "10.5281/zenodo.21124403"
REPLICATION_RECORD = 21783421
REPLICATION_CONCEPT_DOI = "10.5281/zenodo.20461174"

CARRYFORWARD = [
    "01_ENGLISH_GERMANIC_DECISION_LOG_PRIVACY_TRANSFORMATIONS_v3.csv",
    "03_ENGLISH_GERMANIC_DECISION_LOG_PRIVACY_README_v3.md",
    "07z_Retained_Machine_Companion_Metadata_20260804.zip",
    "08_EGA_P138__08a_EGA1_CHAPTER1_P138_VALIDATION_R61.json",
    "08_EGA_P138__08b_EGA_ENGLISH_SOURCE_DIFF_VALIDATION_R82.json",
    "08_EGA_P138__09a_FRENCH_DIPLOMATIC_TRANSCRIPTION_APPEND_P138_20260804.jsonl",
    "08_EGA_P138__09b_ENGLISH_CORRECTION_RECHECK_APPEND_P138_20260804.jsonl",
    "08_EGA_P138__09c_WORKFLOW_ERROR_APPEND_P138_20260804.jsonl",
    "08_EGA_P138__11_PRIVACY_TRANSFORMATIONS.csv",
    "08_EGA_P138__12_PRIVACY_VALIDATION.json",
    "08_EGA_P138__13_PACKAGE_PAYLOAD_MANIFEST.csv",
    "08_EGA_P138__15_PACKAGE_VALIDATION.json",
]

DIRECT_SOURCES = {
    "09_FAC_R4__01_PROJECT_LOGBOOK.md": FAC_ROOT / "15_FAC_Project_Logbook.md",
    "09_FAC_R4__02_EDITORIAL_DECISION_LOGBOOK.md": FAC_ROOT / "13_FAC_Editorial_Decision_Logbook.md",
    "09_FAC_R4__03_SELF_CORRECTION_LEDGER.csv": FAC_ROOT / "14_FAC_Self_Correction_Ledger.csv",
    "09_KO__01_CJK_DECISION_LOGBOOK_PRIVACY_CLEAN.md": P04_COMPLETE_ROOT / "70_KO_CJK_DECISION_LOGBOOK_PRIVACY_CLEAN_20260804.md",
    "09_KO__02_CJK_PRODUCTION_METHODOLOGY_PRIVACY_CLEAN.md": P04_COMPLETE_ROOT / "06_CJK_PRODUCTION_METHODOLOGY_PRIVACY_CLEAN.md",
}

FAC_BUNDLE_FILES = [
    "05_READ_ME_FIRST.md",
    "12_FAC_Model_and_Process_Provenance.md",
    "13_FAC_Editorial_Decision_Logbook.md",
    "14_FAC_Self_Correction_Ledger.csv",
    "15_FAC_Project_Logbook.md",
    "16_RIGHTS_AND_LIMITS.md",
    "18_FAC_Blind_Comparator_Validation.json",
    "23_FAC_Publication_Lineage_Reversal_Logbook.md",
    "30_FAC_REFERENCE_V2_VALIDATION.json",
    "34_FAC_REFERENCE_V2_LOGBOOK.md",
    "35_FAC_REFERENCE_V2_STATUS.md",
    "FAC__COMPLETE_PROVENANCE.zip",
    "FAC__COMPLETE_PROVENANCE_MANIFEST.csv",
    "PACKAGE_VALIDATION.json",
    "ZENODO_PAYLOAD_MANIFEST.csv",
]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256_file(path: Path) -> str:
    return archive.sha256_file(path)


def csv_bytes(fields: list[str], rows: list[dict]) -> bytes:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


def public_entries(record: dict) -> dict[str, dict]:
    entries = record.get("files", {}).get("entries", [])
    if isinstance(entries, dict):
        return entries
    return {row["key"]: row for row in entries}


def fetch_carryforward() -> tuple[dict[str, bytes], list[dict]]:
    session = base.make_session()
    record = base.check(
        session.get(
            f"{base.API}/records/{METHODOLOGY_RECORD}/versions/latest",
            headers={"Accept": "application/vnd.inveniordm.v1+json"},
            timeout=(30, 300),
        ),
        {200},
    ).json()
    entries = public_entries(record)
    if (
        int(record["id"]) != METHODOLOGY_RECORD
        or record["parent"]["pids"]["doi"]["identifier"] != METHODOLOGY_CONCEPT_DOI
        or len(entries) != 100
    ):
        raise RuntimeError("Methodology carry-forward source boundary changed")
    data = {}
    rows = []
    for name in CARRYFORWARD:
        row = entries[name]
        response = base.check(session.get(row["links"]["content"], timeout=(30, 600)), {200})
        value = response.content
        if len(value) != int(row["size"]):
            raise RuntimeError(f"Carry-forward download size changed: {name}")
        data[name] = value
        rows.append(
            {
                "filename": name,
                "bytes": len(value),
                "sha256": sha256_bytes(value),
                "source_record": METHODOLOGY_RECORD,
                "source_url": row["links"]["content"],
            }
        )
    return data, rows


def add_path(entries: dict[str, bytes], archive_path: str, path: Path) -> None:
    if archive_path in entries:
        raise RuntimeError(f"Duplicate provenance archive path: {archive_path}")
    entries[archive_path] = path.read_bytes()


def add_tree(
    entries: dict[str, bytes],
    archive_root: str,
    source_root: Path,
    privacy_rows: list[dict],
) -> list[dict]:
    rows = []
    for path in sorted(
        (item for item in source_root.rglob("*") if item.is_file()),
        key=lambda item: item.relative_to(source_root).as_posix().casefold(),
    ):
        relative = path.relative_to(source_root).as_posix()
        source = path.read_bytes()
        if path.suffix.lower() == ".zip":
            public, applied = sanitize_zip(path, f"{archive_root}/{relative}")
        else:
            public, applied = p04complete.transform_public(
                source, f"{archive_root}/{relative}"
            )
        archive_path = f"{archive_root}/{relative}"
        if archive_path in entries:
            raise RuntimeError(f"Duplicate provenance archive path: {archive_path}")
        entries[archive_path] = public
        for applied_row in applied:
            if len(applied_row) == 2:
                rule, count = applied_row
                transformed_label = archive_path
                source_member_bytes = len(source)
                source_member_sha = sha256_bytes(source)
                public_member_bytes = len(public)
                public_member_sha = sha256_bytes(public)
            else:
                (
                    rule,
                    count,
                    member_path,
                    source_member_bytes,
                    source_member_sha,
                    public_member_bytes,
                    public_member_sha,
                ) = applied_row
                transformed_label = f"{archive_path}!/{member_path}"
            privacy_rows.append(
                {
                    "relative_path": transformed_label,
                    "rule_id": rule,
                    "occurrences": count,
                    "source_bytes": source_member_bytes,
                    "source_sha256": source_member_sha,
                    "public_bytes": public_member_bytes,
                    "public_sha256": public_member_sha,
                    "effect": "minimal private-path/operator-token replacement; substantive provenance retained",
                }
            )
        rows.append(
            {
                "relative_path": relative,
                "bytes": len(public),
                "sha256": sha256_bytes(public),
            }
        )
    return rows


def sanitize_zip(path: Path, label: str) -> tuple[bytes, list[tuple]]:
    transformed_members = []
    applied_rows = []
    with zipfile.ZipFile(path) as package:
        infos = [row for row in package.infolist() if not row.is_dir()]
        if package.testzip() is not None:
            raise RuntimeError(f"Nested ZIP CRC changed: {label}")
        for info in infos:
            source = package.read(info)
            public, applied = p04complete.transform_public(
                source, f"{label}!/{info.filename}"
            )
            transformed_members.append((info.filename, public))
            for rule, count in applied:
                applied_rows.append(
                    (
                        rule,
                        count,
                        info.filename,
                        len(source),
                        sha256_bytes(source),
                        len(public),
                        sha256_bytes(public),
                    )
                )
    output = io.BytesIO()
    with zipfile.ZipFile(
        output,
        mode="w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
        allowZip64=True,
    ) as package:
        for member_name, data in sorted(transformed_members, key=lambda row: row[0]):
            info = zipfile.ZipInfo(member_name, date_time=archive.ZIP_DATE)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 0
            info.external_attr = 0
            package.writestr(
                info,
                data,
                compress_type=zipfile.ZIP_DEFLATED,
                compresslevel=9,
            )
    public_zip = output.getvalue()
    with zipfile.ZipFile(io.BytesIO(public_zip)) as package:
        replay = [row for row in package.infolist() if not row.is_dir()]
        if len(replay) != len(transformed_members) or package.testzip() is not None:
            raise RuntimeError(f"Sanitized nested ZIP replay changed: {label}")
        for info in replay:
            p04complete.transform_public(
                package.read(info), f"sanitized:{label}!/{info.filename}"
            )
    return public_zip, applied_rows


def validate_bundle_privacy(entries: dict[str, bytes]) -> dict:
    patterns = {
        "windows_user_path": re.compile(rb"(?i)[A-Z]:\\Users\\"),
        "escaped_windows_user_path": re.compile(rb"(?i)[A-Z]:\\\\Users\\\\"),
        "posix_user_path": re.compile(rb"(?i)(?:/home/|/Users/)[^/\r\n]+"),
    }
    hits = []
    scanned_members = 0
    nested_zips = 0
    nested_members = 0

    def scan_value(label: str, data: bytes, depth: int = 0) -> None:
        nonlocal nested_zips, nested_members
        observed = {
            name: len(pattern.findall(data)) for name, pattern in patterns.items()
        }
        observed = {name: count for name, count in observed.items() if count}
        if observed:
            hits.append({"relative_path": label, "hits": observed})
        if depth >= 4 or not label.lower().endswith(".zip"):
            return
        try:
            with zipfile.ZipFile(io.BytesIO(data)) as package:
                infos = [row for row in package.infolist() if not row.is_dir()]
                if package.testzip() is not None:
                    raise RuntimeError(f"Nested ZIP CRC failure in bundle privacy scan: {label}")
                nested_zips += 1
                nested_members += len(infos)
                for info in infos:
                    scan_value(f"{label}!/{info.filename}", package.read(info), depth + 1)
        except zipfile.BadZipFile as exc:
            raise RuntimeError(f"Invalid ZIP in bundle privacy scan: {label}") from exc

    for name, data in entries.items():
        scanned_members += 1
        scan_value(name, data)
    if hits:
        raise RuntimeError(f"Bundle private-path privacy scan failed: {hits[:10]}")
    return {
        "schema": "cross_corpus_bundle_recursive_privacy_validation_v1",
        "status": "PASS",
        "errors": [],
        "outer_members_scanned": scanned_members,
        "nested_zips_scanned": nested_zips,
        "nested_members_scanned": nested_members,
        "private_path_hits": 0,
        "proper_name_policy": "public attribution/provenance names are retained; private local user-root paths are prohibited",
    }


def main() -> int:
    if OUTPUT.exists():
        raise RuntimeError("Dual-DOI provenance output already exists; never overwrite")
    if len([path for path in FAC_ROOT.iterdir() if path.is_file()]) != 50:
        raise RuntimeError("FAC R4 root file count changed")
    if sum(path.stat().st_size for path in FAC_ROOT.iterdir() if path.is_file()) != 14_827_551:
        raise RuntimeError("FAC R4 root byte count changed")
    if (FAC_ROOT / "PACKAGE_VALIDATION.json").stat().st_size != 1_199 or sha256_file(FAC_ROOT / "PACKAGE_VALIDATION.json") != "F9E7C37FD34365AAE4ADC4891C681B9163901B922D5DD2BB2BF9DE6726634CB7":
        raise RuntimeError("FAC R4 validation identity changed")
    initial_validation = json.loads(
        (KOREAN_INITIAL_ROOT / "SNAPSHOT_VALIDATION.json").read_text(encoding="utf-8")
    )
    p03_validation = json.loads((P03_ROOT / "SNAPSHOT_VALIDATION.json").read_text(encoding="utf-8"))
    p04_validation = json.loads((P04_ROOT / "SNAPSHOT_VALIDATION.json").read_text(encoding="utf-8"))
    p04_t07_validation = json.loads(
        (P04_T07_ROOT / "SNAPSHOT_VALIDATION.json").read_text(encoding="utf-8")
    )
    p04_complete_validation = json.loads(
        (P04_COMPLETE_ROOT / "SNAPSHOT_VALIDATION.json").read_text(encoding="utf-8")
    )
    nested_correction_validation = json.loads(
        (NESTED_CORRECTION_ROOT / "VALIDATION.json").read_text(encoding="utf-8")
    )
    if initial_validation.get("status") != "PASS_READY_FOR_SAME_CONCEPT_PUBLICATION" or initial_validation.get("errors") != []:
        raise RuntimeError("Initial Korean provenance source is not PASS")
    if p03_validation.get("status") != "PASS_READY_FOR_SAME_CONCEPT_PUBLICATION" or p03_validation.get("errors") != []:
        raise RuntimeError("P03 provenance source is not PASS")
    if p04_validation.get("status") != "PASS_READY_FOR_SAME_CONCEPT_PUBLICATION" or p04_validation.get("errors") != []:
        raise RuntimeError("P04 provenance source is not PASS")
    if p04_t07_validation.get("status") != "PASS_READY_FOR_SAME_CONCEPT_PUBLICATION" or p04_t07_validation.get("errors") != []:
        raise RuntimeError("P04 T07 provenance source is not PASS")
    if p04_complete_validation.get("status") != "PASS_READY_FOR_PRIVACY_CORRECTIVE_SAME_CONCEPT_PUBLICATION" or p04_complete_validation.get("errors") != []:
        raise RuntimeError("P04 complete provenance source is not PASS")
    if nested_correction_validation.get("status") != "PASS_READY_FOR_SAME_CONCEPT_PRIVACY_CORRECTION" or nested_correction_validation.get("errors") != []:
        raise RuntimeError("Nested-ZIP correction provenance source is not PASS")

    spanish_surface, spanish_zip_replay = spanish.local_new_surface()
    if spanish_zip_replay.get("status") != "PASS" or spanish_zip_replay.get("members") != 408:
        raise RuntimeError("Spanish SGA 5 public surface replay changed")
    spanish_direct = {
        "09_SGA5_ES__01_PUBLIC_RELEASE_AUTHORIZATION_AND_HOLD_SUPERSESSION.md": spanish_surface["SGA5_ES_PUBLIC_RELEASE_AUTHORIZATION_AND_HOLD_SUPERSESSION.md"]["path"],
        "09_SGA5_ES__02_PUBLIC_SOURCE_AND_RIGHTS.md": spanish_surface["SGA5_ES_PUBLIC_SOURCE_AND_RIGHTS.md"]["path"],
        "09_SGA5_ES__03_CONTINUATION_CURSOR.md": spanish_surface["SGA5_ES_CONTINUATION_CURSOR.md"]["path"],
        "09_SGA5_ES__04_SUPERSESSION.md": spanish_surface["SGA5_ES_SUPERSESSION.md"]["path"],
    }
    direct_sources = {**DIRECT_SOURCES, **{name: Path(path) for name, path in spanish_direct.items()}}
    if len(direct_sources) != 9:
        raise RuntimeError("Dual-DOI direct human surface count changed")

    carry_data, carry_rows = fetch_carryforward()
    bundle: dict[str, bytes] = {}
    bundle_privacy_rows: list[dict] = []
    for name in FAC_BUNDLE_FILES:
        add_path(bundle, f"FAC_R4/{name}", FAC_ROOT / name)
    for name, path in direct_sources.items():
        add_path(bundle, f"DIRECT_HUMAN_SURFACES/{name}", path)

    korean_roots = {
        "KOREAN_NOETHER_P01_P05_P07_P41_P42": KOREAN_INITIAL_ROOT,
        "KOREAN_NOETHER_P03": P03_ROOT,
        "KOREAN_NOETHER_P04_T04_T06": P04_ROOT,
        "KOREAN_NOETHER_P04_T07": P04_T07_ROOT,
        "KOREAN_NOETHER_P04_COMPLETE": P04_COMPLETE_ROOT,
        "KOREAN_NOETHER_NESTED_ZIP_PRIVACY_CORRECTION": NESTED_CORRECTION_ROOT,
    }
    korean_root_rows = {
        name: add_tree(bundle, name, root, bundle_privacy_rows)
        for name, root in korean_roots.items()
    }

    skip_spanish = {"SGA5_ES.pdf", "sga5_es.tex", spanish.COMPLETE_ZIP_NAME}
    for name, row in spanish_surface.items():
        if name in skip_spanish:
            continue
        add_path(bundle, f"SGA5_SPANISH/{name}", Path(row["path"]))
    for name, value in carry_data.items():
        if f"METHODOLOGY_CARRYFORWARD/{name}" in bundle:
            raise RuntimeError("Duplicate carry-forward path")
        bundle[f"METHODOLOGY_CARRYFORWARD/{name}"] = value

    privacy_csv = csv_bytes(
        [
            "relative_path",
            "rule_id",
            "occurrences",
            "source_bytes",
            "source_sha256",
            "public_bytes",
            "public_sha256",
            "effect",
        ],
        bundle_privacy_rows,
    )
    bundle["BUNDLE_PRIVACY_TRANSFORMATIONS.csv"] = privacy_csv
    bundle_privacy_validation = validate_bundle_privacy(bundle)
    bundle_privacy_validation_bytes = (
        json.dumps(bundle_privacy_validation, ensure_ascii=True, indent=2) + "\n"
    ).encode("utf-8")
    bundle["BUNDLE_PRIVACY_VALIDATION.json"] = bundle_privacy_validation_bytes

    manifest_rows = [
        {
            "relative_path": name,
            "bytes": len(value),
            "sha256": sha256_bytes(value),
            "role": (
                "methodology_file_ceiling_carryforward"
                if name.startswith("METHODOLOGY_CARRYFORWARD/")
                else "current_public_provenance"
            ),
        }
        for name, value in sorted(bundle.items())
    ]
    bundle_manifest = csv_bytes(
        ["relative_path", "bytes", "sha256", "role"], manifest_rows
    )
    bundle["BUNDLE_CONTENT_MANIFEST.csv"] = bundle_manifest

    OUTPUT.mkdir(parents=True)
    bundle_path = OUTPUT / "09_ARCHIVE_PROVENANCE__00_FAC_KOREAN_SGA5_COMPLETE_20260804.zip"
    archive.deterministic_zip(bundle_path, sorted(bundle.items()))
    for name, path in direct_sources.items():
        (OUTPUT / name).write_bytes(path.read_bytes())

    direct_rows = [
        {
            "filename": path.name,
            "bytes": path.stat().st_size,
            "sha256": sha256_file(path),
            "role": "complete_current_provenance_bundle" if path == bundle_path else "direct_human_provenance",
        }
        for path in sorted((item for item in OUTPUT.iterdir() if item.is_file()), key=lambda item: item.name.casefold())
    ]
    direct_manifest_path = OUTPUT / "09_ARCHIVE_PROVENANCE__98_DIRECT_SURFACE_MANIFEST.csv"
    archive.write_csv(
        direct_manifest_path,
        ["filename", "bytes", "sha256", "role"],
        direct_rows,
    )
    validation = {
        "schema": "cross_corpus_dual_doi_provenance_package_v5",
        "status": "PASS_READY_FOR_DUAL_DOI_PUBLICATION",
        "errors": [],
        "target_concepts": [METHODOLOGY_CONCEPT_DOI, REPLICATION_CONCEPT_DOI],
        "bundle": {
            "filename": bundle_path.name,
            "bytes": bundle_path.stat().st_size,
            "sha256": sha256_file(bundle_path),
            "members": len(bundle),
            "represented_content_rows": len(manifest_rows),
        },
        "direct_human_files": len(direct_sources),
        "direct_surface_files_excluding_this_validation": len(direct_rows) + 1,
        "methodology_carryforward_files": len(carry_rows),
        "methodology_carryforward": carry_rows,
        "fac_required_direct": 3,
        "korean_required_direct": 2,
        "korean_complete_public_projection_roots": {
            name: {
                "files": len(rows),
                "bytes": sum(int(row["bytes"]) for row in rows),
                "tree_sha256": archive.tree_sha(rows),
            }
            for name, rows in korean_root_rows.items()
        },
        "bundle_privacy_transformations": {
            "rows": len(bundle_privacy_rows),
            "occurrences": sum(int(row["occurrences"]) for row in bundle_privacy_rows),
            "bytes": len(privacy_csv),
            "sha256": sha256_bytes(privacy_csv),
        },
        "bundle_recursive_privacy_validation": {
            **bundle_privacy_validation,
            "bytes": len(bundle_privacy_validation_bytes),
            "sha256": sha256_bytes(bundle_privacy_validation_bytes),
        },
        "spanish_sga5_required_direct": 4,
        "privacy_sources": "all inputs are previously validated public projections or immutable published public bytes",
        "fac_record": "10.5281/zenodo.21783868",
        "noether_record": "10.5281/zenodo.21785492",
        "sga_record": "10.5281/zenodo.21783548",
    }
    validation_path = OUTPUT / "09_ARCHIVE_PROVENANCE__99_PACKAGE_VALIDATION.json"
    archive.write_json(validation_path, validation)
    final = archive.inventory(OUTPUT)
    if len(final) != 12:
        raise RuntimeError(f"Dual-DOI direct surface count changed: {len(final)}")
    result = {
        **validation,
        "public_root": str(OUTPUT),
        "public_root_files": len(final),
        "public_root_bytes": sum(int(row["bytes"]) for row in final),
        "public_root_tree_sha256": archive.tree_sha(final),
        "direct_surface_manifest": {
            "bytes": direct_manifest_path.stat().st_size,
            "sha256": sha256_file(direct_manifest_path),
        },
        "package_validation": {
            "bytes": validation_path.stat().st_size,
            "sha256": sha256_file(validation_path),
        },
    }
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

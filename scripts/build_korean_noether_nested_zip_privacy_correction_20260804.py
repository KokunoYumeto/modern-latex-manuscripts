#!/usr/bin/env python3
"""Rebuild six Korean Noether public ZIPs with nested path privacy correction."""

from __future__ import annotations

import json
import re
import zipfile
from pathlib import Path

import build_korean_noether_unchecked_public_snapshots_20260804 as archive
import build_korean_noether_p04_complete_privacy_corrected_snapshot_20260804 as privacy


REPO_ROOT = Path(__file__).resolve().parents[1]
PUBLIC_ROOT = REPO_ROOT / "sources/noether/korean-nested-zip-privacy-correction-20260804-r2"
PRIVATE_ROOT = (
    archive.CJK_CONTROL.parent
    / "90_logs/private_archive_custody/KOREAN_NOETHER_NESTED_ZIP_PRIVACY_CORRECTION_20260804_r2"
)
INITIAL = REPO_ROOT / "sources/noether/korean-unchecked-papers-01-05-07-41-42-20260804"
P03 = REPO_ROOT / "sources/noether/korean-unchecked-paper-03-20260804"

SOURCES = {
    "70a_KO_P01__00_COMPLETE_UNCHECKED_PUBLIC_SNAPSHOT_20260804.zip": (
        INITIAL / "P01_Korean_UNCHECKED_Public_Snapshot_20260804.zip",
        81_864,
        "83E6A988F1E1F7B7A4EB239C96AAC8FDEE2043D9CB59E5E50EF47158EBCD2311",
        35,
        94,
    ),
    "70b_KO_P05__00_COMPLETE_UNCHECKED_PUBLIC_SNAPSHOT_20260804.zip": (
        INITIAL / "P05_Korean_UNCHECKED_Public_Snapshot_20260804.zip",
        73_186,
        "0CD26F1BB25C745520B73A002E2003F515E6E73F5E3FE71C90BA3D12452AF687",
        29,
        158,
    ),
    "70c_KO_P07__00_COMPLETE_UNCHECKED_PUBLIC_SNAPSHOT_20260804.zip": (
        INITIAL / "P07_Korean_UNCHECKED_Public_Snapshot_20260804.zip",
        95_089,
        "10D5070AF8EEF4B2E9CE88DD591367839C174FFFB2F37AAB533BDEE70D9FE5A9",
        45,
        139,
    ),
    "70d_KO_P41__00_COMPLETE_UNCHECKED_PUBLIC_SNAPSHOT_20260804.zip": (
        INITIAL / "P41_Korean_UNCHECKED_Public_Snapshot_20260804.zip",
        180_083,
        "0DB7DA9E85C8EE416CD10F21CB6BBBA7B299C6659A02A96CF9F1030B3F14EF87",
        47,
        413,
    ),
    "70e_KO_P42__00_COMPLETE_UNCHECKED_PUBLIC_SNAPSHOT_20260804.zip": (
        INITIAL / "P42_Korean_UNCHECKED_Public_Snapshot_20260804.zip",
        82_940,
        "73F83B2D28BB8D68B7E62DF9E08A879DCD030559E1F84C5003CBB6995ABE6772",
        36,
        197,
    ),
    "70f_KO_P03__00_COMPLETE_UNCHECKED_PUBLIC_SNAPSHOT_20260804.zip": (
        P03 / "P03_Korean_UNCHECKED_Public_Snapshot_20260804.zip",
        128_450,
        "AEB6810B64E5222ABBC57BE28C997FEC335D2E330C01D1321B920FCFEFB6FBD8",
        37,
        460,
    ),
}

PRIVATE_PATTERNS = {
    "windows_user_path": re.compile(rb"(?i)[A-Z]:\\Users\\"),
    "escaped_windows_user_path": re.compile(rb"(?i)[A-Z]:\\\\Users\\\\"),
    "posix_user_path": re.compile(rb"(?i)(?:/home/|/Users/)[^/\r\n]+"),
    "operator_name": re.compile(
        rb"\b" + re.escape(archive.USER_PROFILE_ROOT.name.encode("utf-8")) + rb"\b",
        re.IGNORECASE,
    ),
}


def privacy_hits(data: bytes) -> dict[str, int]:
    return {
        label: count
        for label, pattern in PRIVATE_PATTERNS.items()
        if (count := len(pattern.findall(data)))
    }


def main() -> int:
    if PUBLIC_ROOT.exists() or PRIVATE_ROOT.exists():
        raise RuntimeError("Nested-ZIP correction output exists; never overwrite")
    PUBLIC_ROOT.mkdir(parents=True)
    PRIVATE_ROOT.mkdir(parents=True)
    archive.deterministic_zip(
        PRIVATE_ROOT / "SIX_AFFECTED_PUBLIC_ZIPS_EXACT_ADVERSE_SNAPSHOT_20260804.zip",
        [(name, source.read_bytes()) for name, (source, *_rest) in SOURCES.items()],
    )

    zip_rows = []
    member_rows = []
    transformation_rows = []
    total_occurrences = 0
    for remote_name, (source, expected_bytes, expected_sha, expected_members, expected_occurrences) in SOURCES.items():
        raw = source.read_bytes()
        if (len(raw), archive.sha256_bytes(raw)) != (expected_bytes, expected_sha):
            raise RuntimeError(f"Adverse ZIP source identity changed: {remote_name}")
        members = []
        occurrences = 0
        with zipfile.ZipFile(source) as package:
            infos = [row for row in package.infolist() if not row.is_dir()]
            if len(infos) != expected_members or package.testzip() is not None:
                raise RuntimeError(f"Adverse ZIP member boundary changed: {remote_name}")
            for info in infos:
                original = package.read(info)
                before_hits = privacy_hits(original)
                occurrences += sum(before_hits.values())
                public, applied = privacy.transform_public(
                    original, f"{remote_name}!/{info.filename}"
                )
                if privacy_hits(public):
                    raise RuntimeError(f"Nested privacy hit remains: {remote_name}!/{info.filename}")
                members.append((info.filename, public))
                member_rows.append(
                    {
                        "zip_filename": remote_name,
                        "member_path": info.filename,
                        "source_bytes": len(original),
                        "source_sha256": archive.sha256_bytes(original),
                        "public_bytes": len(public),
                        "public_sha256": archive.sha256_bytes(public),
                        "privacy_occurrences": sum(count for _, count in applied),
                    }
                )
                for rule, count in applied:
                    transformation_rows.append(
                        {
                            "zip_filename": remote_name,
                            "member_path": info.filename,
                            "rule_id": rule,
                            "occurrences": count,
                            "effect": "nested serialized local-path/operator token replaced; substantive evidence retained",
                        }
                    )
        if occurrences != expected_occurrences:
            raise RuntimeError(
                f"Adverse nested privacy occurrence count changed for {remote_name}: {occurrences}"
            )
        destination = PUBLIC_ROOT / remote_name
        archive.deterministic_zip(destination, members)
        with zipfile.ZipFile(destination) as corrected:
            infos = [row for row in corrected.infolist() if not row.is_dir()]
            if len(infos) != expected_members or corrected.testzip() is not None:
                raise RuntimeError(f"Corrected ZIP replay changed: {remote_name}")
            for info in infos:
                if privacy_hits(corrected.read(info)):
                    raise RuntimeError(f"Corrected ZIP still leaks: {remote_name}!/{info.filename}")
        total_occurrences += occurrences
        zip_rows.append(
            {
                "remote_filename": remote_name,
                "predecessor_record": 21785396,
                "source_bytes": len(raw),
                "source_sha256": archive.sha256_bytes(raw),
                "source_members": expected_members,
                "private_path_occurrences": occurrences,
                "successor_bytes": destination.stat().st_size,
                "successor_sha256": archive.sha256_file(destination),
                "successor_members": expected_members,
                "supersession": "replace_live_same_filename; immutable predecessors retain adverse container",
            }
        )
    if total_occurrences != 1_461:
        raise RuntimeError("Nested privacy correction occurrence total changed")

    readme = """# Korean Noether nested-ZIP privacy correction

Anonymous and local member-level inspection found serialized Windows user-root paths inside six earlier Korean snapshot ZIPs. This is an archive packaging defect, not a mathematical or translation defect. The same six live filenames are replaced by deterministic ZIPs whose 229 members preserve the substantive bytes while minimally replacing path/operator tokens.

The exact adverse container identities, corrected identities, member hashes, and 1,461 transformations are bound here. Immutable predecessor records remain adverse-history witnesses. State labels remain UNCHECKED, uncompiled, unrendered, unassembled, unreviewed, and uncertified; publication is not approval and there is no release hold.
"""
    archive.write_text(PUBLIC_ROOT / "README.md", readme)
    archive.write_csv(
        PUBLIC_ROOT / "NESTED_ZIP_PRIVACY_CORRECTION_MANIFEST.csv",
        [
            "remote_filename",
            "predecessor_record",
            "source_bytes",
            "source_sha256",
            "source_members",
            "private_path_occurrences",
            "successor_bytes",
            "successor_sha256",
            "successor_members",
            "supersession",
        ],
        zip_rows,
    )
    archive.write_csv(
        PUBLIC_ROOT / "NESTED_ZIP_MEMBER_TRANSFORMATIONS.csv",
        ["zip_filename", "member_path", "rule_id", "occurrences", "effect"],
        transformation_rows,
    )
    archive.write_csv(
        PUBLIC_ROOT / "NESTED_ZIP_MEMBER_MANIFEST.csv",
        [
            "zip_filename",
            "member_path",
            "source_bytes",
            "source_sha256",
            "public_bytes",
            "public_sha256",
            "privacy_occurrences",
        ],
        member_rows,
    )
    before_validation = archive.inventory(PUBLIC_ROOT)
    validation = {
        "schema": "korean_noether_nested_zip_privacy_correction_v1",
        "status": "PASS_READY_FOR_SAME_CONCEPT_PRIVACY_CORRECTION",
        "errors": [],
        "affected_zip_files": 6,
        "affected_members": 17,
        "total_members": 229,
        "private_path_occurrences": total_occurrences,
        "corrected_zip_member_mismatches": 0,
        "source_and_successor_zips": zip_rows,
        "state_labels_unchanged": [
            "UNCHECKED",
            "uncompiled",
            "unrendered",
            "unassembled",
            "unreviewed",
            "uncertified",
        ],
        "publication_is_approval": False,
        "release_hold": False,
        "public_files_excluding_this_validation": len(before_validation),
        "public_bytes_excluding_this_validation": sum(int(row["bytes"]) for row in before_validation),
        "public_tree_sha256_excluding_this_validation": archive.tree_sha(before_validation),
    }
    validation_path = PUBLIC_ROOT / "VALIDATION.json"
    archive.write_json(validation_path, validation)
    final = archive.inventory(PUBLIC_ROOT)
    result = {
        **validation,
        "public_root": str(PUBLIC_ROOT),
        "public_root_files": len(final),
        "public_root_bytes": sum(int(row["bytes"]) for row in final),
        "public_root_tree_sha256": archive.tree_sha(final),
        "validation_bytes": validation_path.stat().st_size,
        "validation_sha256": archive.sha256_file(validation_path),
        "private_adverse_container_zip_bytes": (PRIVATE_ROOT / "SIX_AFFECTED_PUBLIC_ZIPS_EXACT_ADVERSE_SNAPSHOT_20260804.zip").stat().st_size,
        "private_adverse_container_zip_sha256": archive.sha256_file(PRIVATE_ROOT / "SIX_AFFECTED_PUBLIC_ZIPS_EXACT_ADVERSE_SNAPSHOT_20260804.zip"),
    }
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

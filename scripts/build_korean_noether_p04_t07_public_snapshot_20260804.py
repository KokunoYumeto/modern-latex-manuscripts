#!/usr/bin/env python3
"""Freeze P04 privately and public-project exactly the authorized T07 tranche."""

from __future__ import annotations

import json
from pathlib import Path

import build_korean_noether_unchecked_public_snapshots_20260804 as archive


REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = archive.SOURCE_BASE / "noether_paper04_ko_translation_001_20260804"
PRIVATE_ROOT = (
    archive.CJK_CONTROL.parent
    / "90_logs"
    / "private_archive_custody"
    / "KOREAN_NOETHER_P04_T07_SNAPSHOT_20260804_r1"
)
PUBLIC_ROOT = REPO_ROOT / "sources" / "noether" / "korean-unchecked-paper-04-t07-20260804"
PUBLIC_TRANCHE = PUBLIC_ROOT / "P04_T07"
POINTER_V004 = archive.POINTER_SOURCE.parent / "NOETH_DE_AUTHORITY_POINTER_v004_20260804.json"
HANDOFF_LOG_BYTES = 637_188
HANDOFF_LOG_SHA256 = "D636440BA189927F29758E5F0BE46BDAF943E57BDD3A4E55FF64BE629C0BE44E"

SELECTED = {
    "targets/Noether_P04_Korean_T07_U33_UNCHECKED.tex": (3_295, "A4FE355CA44A9EC87E1F86287D3CE18834FF8ADD7966DA00A45C59FFA5BEC8D5"),
    "targets/Noether_P04_Korean_T07_U34_UNCHECKED.tex": (2_496, "29B5581122A9C993878976CEFEBEFC068DA729F56946FD63C3DB6B66B3784DE0"),
    "targets/Noether_P04_Korean_T07_U35_UNCHECKED.tex": (2_695, "2A5295BCFFD02A0F4874257C79FC289B37030989D839EFAF942CE6CDA3FABE1F"),
    "targets/Noether_P04_Korean_T07_U36_UNCHECKED.tex": (3_054, "1E7EEDA0FF9B95F51C6DDE6E22A5E37257EC4A175DA6EB081973D263BE035020"),
    "targets/Noether_P04_Korean_T07_U37_UNCHECKED.tex": (2_724, "8F2DC0D514194A08AA3E0999B0C08ECBD115A3FB8259558BB65045AEF186C527"),
    "targets/Noether_P04_Korean_T07_U38_UNCHECKED.tex": (1_336, "DDF04812D84E68452CBBCB0163A4C501E64091FEAB369C2FD9B7D21510B80B94"),
    "SOURCE_CUSTODY_T07.md": (2_262, "FE8714C1A87286112D5C01F933A27130DCE4020547A805F52F380B9E2A545175"),
    "STATUS_T07.md": (1_099, "063B522F63325EFF0A301B010C6F50958265E9E44B58A4D955C6C197D3429E09"),
    "CHECKER_HANDOFF_T07_U33_U38.md": (1_861, "C5808DFE103F054C3A2A9EBCE06E30A7B930E4708F7F5D83B87B5C0706AC5FC1"),
    "TRANSLATION_CHOICES_T07.md": (2_654, "7BD8691D0CA60EAC7755020243848C7A6505D09311E898CAEB84BF0854B524D2"),
}


def transform(data: bytes, relative: str) -> tuple[bytes, list[tuple[str, int]]]:
    public, applied = archive.transform_text(data)
    archive.assert_privacy_clean(relative, public)
    return public, applied


def main() -> int:
    if PRIVATE_ROOT.exists() or PUBLIC_ROOT.exists():
        raise RuntimeError("P04 T07 output exists; frozen revisions are never overwritten")
    before = archive.inventory(SOURCE_ROOT)
    source_map = {row["relative_path"]: row for row in before}
    full_files = len(before)
    full_bytes = sum(int(row["bytes"]) for row in before)
    if len(SELECTED) != 10 or sum(value[0] for value in SELECTED.values()) != 23_476:
        raise RuntimeError("P04 T07 declaration changed")
    for relative, expected in SELECTED.items():
        row = source_map.get(relative)
        if row is None or (int(row["bytes"]), row["sha256"]) != expected:
            raise RuntimeError(f"P04 T07 exact selected identity changed: {relative}")
    if (POINTER_V004.stat().st_size, archive.sha256_file(POINTER_V004)) != (
        16_536,
        "A1C62FDACAA34DFC1B806DC18258F2E732539F7AE9D85AA4BD9E1067B8749D9F",
    ):
        raise RuntimeError("Noether pointer v004 changed")
    current_log = (archive.CJK_CONTROL / "CJK_DECISION_LOGBOOK_20260718.md").read_bytes()
    handoff_log = current_log[:HANDOFF_LOG_BYTES]
    if len(handoff_log) != HANDOFF_LOG_BYTES or archive.sha256_bytes(handoff_log) != HANDOFF_LOG_SHA256:
        raise RuntimeError("P04 T07 exact append-only log generation is not recoverable")

    PRIVATE_ROOT.mkdir(parents=True)
    PUBLIC_TRANCHE.mkdir(parents=True)
    full_zip = PRIVATE_ROOT / "P04_FULL_PRODUCER_ROOT_EXACT_PRIVATE_SNAPSHOT_AT_T07_20260804.zip"
    selected_zip = PRIVATE_ROOT / "P04_T07_10_FILE_EXACT_PRIVATE_TRANCHE_20260804.zip"
    archive.deterministic_zip(
        full_zip,
        [(row["relative_path"], Path(row["path"]).read_bytes()) for row in before],
    )
    archive.deterministic_zip(
        selected_zip,
        [(relative, (SOURCE_ROOT / relative).read_bytes()) for relative in sorted(SELECTED)],
    )
    archive.write_csv(
        PRIVATE_ROOT / "P04_FULL_ROOT_AT_T07_EXACT_MANIFEST.csv",
        ["relative_path", "bytes", "sha256", "tranche_disposition"],
        [
            {
                "relative_path": row["relative_path"],
                "bytes": row["bytes"],
                "sha256": row["sha256"],
                "tranche_disposition": "PUBLIC_T07_INCLUDE" if row["relative_path"] in SELECTED else "OUTSIDE_T07_TRANCHE_PRIVATE_CUSTODY_ONLY",
            }
            for row in before
        ],
    )

    projection = []
    privacy = []
    for row in before:
        relative = row["relative_path"]
        if relative not in SELECTED:
            projection.append(
                {
                    "relative_path": relative,
                    "source_bytes": row["bytes"],
                    "source_sha256": row["sha256"],
                    "public_bytes": "",
                    "public_sha256": "",
                    "privacy_transformations": 0,
                    "disposition": "OUTSIDE_BOUNDED_T07_TRANCHE",
                    "rationale": "exact byte preserved in private full-root snapshot; not selected by this handoff",
                }
            )
            continue
        data, applied = transform((SOURCE_ROOT / relative).read_bytes(), relative)
        destination = PUBLIC_TRANCHE / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(data)
        projection.append(
            {
                "relative_path": relative,
                "source_bytes": row["bytes"],
                "source_sha256": row["sha256"],
                "public_bytes": len(data),
                "public_sha256": archive.sha256_bytes(data),
                "privacy_transformations": sum(count for _, count in applied),
                "disposition": "PUBLIC_T07_INCLUDE",
                "rationale": "minimal private path/operator substitution" if applied else "byte-identical source projection",
            }
        )
        for rule, count in applied:
            privacy.append(
                {
                    "relative_path": relative,
                    "rule_id": rule,
                    "occurrences": count,
                    "source_sha256": row["sha256"],
                    "public_sha256": archive.sha256_bytes(data),
                    "semantic_scope": "private path/operator token only; mathematical text unchanged",
                }
            )
    archive.write_csv(
        PUBLIC_TRANCHE / "ARCHIVE_PUBLIC_PROJECTION_MANIFEST.csv",
        ["relative_path", "source_bytes", "source_sha256", "public_bytes", "public_sha256", "privacy_transformations", "disposition", "rationale"],
        projection,
    )
    archive.write_csv(
        PUBLIC_TRANCHE / "ARCHIVE_PRIVACY_TRANSFORMATIONS.csv",
        ["relative_path", "rule_id", "occurrences", "source_sha256", "public_sha256", "semantic_scope"],
        privacy,
    )
    archive.write_text(
        PUBLIC_TRANCHE / "ARCHIVE_PUBLICATION_README.md",
        f"""# Korean Noether Paper 4 — T07 bounded tranche

This public snapshot contains exactly ten authorized files: six editable Korean TeX units U33–U38 plus source-custody, status, checker-handoff, and translation-choice documents. It covers source lines 4162–4303; blank line 4304 is excluded; the next exact cursor is line 4305. It does not claim Paper 4 completion.

State: **UNCHECKED, incomplete, uncompiled, unrendered, unassembled, and unreviewed**. These are scope labels, not release holds or approval. Archive maintenance performed no source correction, checking, compilation, rendering, assembly, or certification.

The contemporaneous {full_files}-file producer root is frozen privately; all {full_files - len(SELECTED)} nonselected identities are ledgered. No visual/image/right-sensitive file belongs to this tranche.
""",
    )
    represented = archive.inventory(PUBLIC_TRANCHE)
    tranche_validation = {
        "schema": "korean_noether_p04_t07_public_snapshot_validation_v1",
        "status": "PASS_PUBLIC_UNCHECKED_INCOMPLETE_TRANCHE",
        "errors": [],
        "selected_source_files": 10,
        "selected_source_bytes": 23_476,
        "target_units": 6,
        "authority_lines": "4162-4303",
        "excluded_blank_line": 4304,
        "next_line": 4305,
        "full_producer_root_files": full_files,
        "full_producer_root_bytes": full_bytes,
        "full_producer_root_tree_sha256": archive.tree_sha(before),
        "out_of_tranche_files": full_files - len(SELECTED),
        "public_files_excluding_this_validation": len(represented),
        "public_bytes_excluding_this_validation": sum(int(row["bytes"]) for row in represented),
        "public_tree_sha256_excluding_this_validation": archive.tree_sha(represented),
        "privacy_transformation_occurrences": sum(int(row["occurrences"]) for row in privacy),
        "state_labels": ["UNCHECKED", "incomplete", "uncompiled", "unrendered", "unassembled", "unreviewed"],
        "release_hold": False,
    }
    archive.write_json(PUBLIC_TRANCHE / "ARCHIVE_SNAPSHOT_VALIDATION.json", tranche_validation)
    public_members = [
        (path.relative_to(PUBLIC_TRANCHE).as_posix(), path.read_bytes())
        for path in sorted((x for x in PUBLIC_TRANCHE.rglob("*") if x.is_file()), key=lambda x: x.relative_to(PUBLIC_TRANCHE).as_posix())
    ]
    public_zip = PUBLIC_ROOT / "P04_T07_Korean_UNCHECKED_Public_Snapshot_20260804.zip"
    archive.deterministic_zip(public_zip, public_members)

    common_raw = [
        ("70_KO_CJK_DECISION_LOGBOOK_HANDOFF_EXACT_20260804.md", handoff_log),
        ("70_KO_NOETH_DE_AUTHORITY_POINTER_v004_20260804.json", POINTER_V004.read_bytes()),
    ]
    common_private_zip = PRIVATE_ROOT / "P04_T07_COMMON_CONTROLS_EXACT_PRIVATE_SNAPSHOT_20260804.zip"
    archive.deterministic_zip(common_private_zip, common_raw)
    common = []
    for name, data in common_raw:
        public_name = name.replace("_HANDOFF_EXACT", "_PRIVACY_CLEAN")
        value, applied = transform(data, public_name)
        destination = PUBLIC_ROOT / public_name
        destination.write_bytes(value)
        common.append({"filename": public_name, "source_bytes": len(data), "source_sha256": archive.sha256_bytes(data), "public_bytes": len(value), "public_sha256": archive.sha256_bytes(value), "privacy_occurrences": sum(count for _, count in applied)})

    index_path = PUBLIC_ROOT / "70h_KO_P04_T07_SNAPSHOT_INDEX_20260804.csv"
    archive.write_csv(
        index_path,
        ["scope", "selected_files", "selected_bytes", "targets", "authority_lines", "excluded_blank", "next_line", "full_root_files", "full_root_bytes", "out_of_tranche_files", "public_zip", "public_zip_bytes", "public_zip_sha256", "public_zip_members", "state"],
        [{"scope": "P04_T07_U33_U38", "selected_files": 10, "selected_bytes": 23_476, "targets": 6, "authority_lines": "4162-4303", "excluded_blank": 4304, "next_line": 4305, "full_root_files": full_files, "full_root_bytes": full_bytes, "out_of_tranche_files": full_files - len(SELECTED), "public_zip": public_zip.name, "public_zip_bytes": public_zip.stat().st_size, "public_zip_sha256": archive.sha256_file(public_zip), "public_zip_members": len(public_members), "state": "UNCHECKED;incomplete;uncompiled;unrendered;unassembled;unreviewed"}],
    )
    readme_path = PUBLIC_ROOT / "README.md"
    archive.write_text(
        readme_path,
        f"""# Korean Noether Paper 4 — T07 archive snapshot

The complete ZIP is the exact privacy-clean ten-file tranche. Direct source-custody, status, checker, and translation-choice surfaces expose its incomplete and UNCHECKED state. All {full_files - len(SELECTED)} contemporaneous out-of-tranche identities are public-ledgered and their bytes remain in the exact private full-root snapshot.
""",
    )
    before_root_validation = archive.inventory(PUBLIC_ROOT)
    root_validation = {
        "schema": "korean_noether_p04_t07_public_closeout_v1",
        "status": "PASS_READY_FOR_SAME_CONCEPT_PUBLICATION",
        "errors": [],
        "tranche_validation": tranche_validation,
        "public_zip": {"filename": public_zip.name, "bytes": public_zip.stat().st_size, "sha256": archive.sha256_file(public_zip), "members": len(public_members)},
        "common_controls": common,
        "private_custody": {"root": str(PRIVATE_ROOT), "full_root_zip_bytes": full_zip.stat().st_size, "full_root_zip_sha256": archive.sha256_file(full_zip), "selected_tranche_zip_bytes": selected_zip.stat().st_size, "selected_tranche_zip_sha256": archive.sha256_file(selected_zip), "common_controls_zip_bytes": common_private_zip.stat().st_size, "common_controls_zip_sha256": archive.sha256_file(common_private_zip)},
        "public_root_files_excluding_this_validation": len(before_root_validation),
        "public_root_bytes_excluding_this_validation": sum(int(row["bytes"]) for row in before_root_validation),
        "public_root_tree_sha256_excluding_this_validation": archive.tree_sha(before_root_validation),
        "explicit_public_exclusions": full_files - len(SELECTED),
        "excluded_bytes_preserved_private": True,
        "release_hold": False,
    }
    validation_path = PUBLIC_ROOT / "SNAPSHOT_VALIDATION.json"
    archive.write_json(validation_path, root_validation)
    after = archive.inventory(SOURCE_ROOT)
    if [(r["relative_path"], r["bytes"], r["sha256"]) for r in after] != [(r["relative_path"], r["bytes"], r["sha256"]) for r in before]:
        raise RuntimeError("P04 root changed during T07 bounded snapshot")
    final = archive.inventory(PUBLIC_ROOT)
    result = {
        **root_validation,
        "public_root_files": len(final),
        "public_root_bytes": sum(int(row["bytes"]) for row in final),
        "public_root_tree_sha256": archive.tree_sha(final),
        "validation_path": str(validation_path),
        "validation_bytes": validation_path.stat().st_size,
        "validation_sha256": archive.sha256_file(validation_path),
        "index_bytes": index_path.stat().st_size,
        "index_sha256": archive.sha256_file(index_path),
        "readme_bytes": readme_path.stat().st_size,
        "readme_sha256": archive.sha256_file(readme_path),
    }
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

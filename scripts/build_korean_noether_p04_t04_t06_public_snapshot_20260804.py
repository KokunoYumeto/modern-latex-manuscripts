#!/usr/bin/env python3
"""Freeze P04 privately and publish-project exactly the authorized T04-T06 tranche."""

from __future__ import annotations

import json
from pathlib import Path

import build_korean_noether_unchecked_public_snapshots_20260804 as engine


REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = engine.SOURCE_BASE / "noether_paper04_ko_translation_001_20260804"
PRIVATE_ROOT = (
    engine.CJK_CONTROL.parent
    / "90_logs"
    / "private_archive_custody"
    / "KOREAN_NOETHER_P04_T04_T06_SNAPSHOT_20260804_r1"
)
PUBLIC_ROOT = (
    REPO_ROOT / "sources" / "noether" / "korean-unchecked-paper-04-t04-t06-20260804"
)
PUBLIC_TRANCHE = PUBLIC_ROOT / "P04_T04_T06"
POINTER_V004 = (
    engine.POINTER_SOURCE.parent / "NOETH_DE_AUTHORITY_POINTER_v004_20260804.json"
)
HANDOFF_LOG_BYTES = 621_629
HANDOFF_LOG_SHA256 = "4A6395938E782DDC561429436D1EF7209A409E9D2A1AD0B420688E960F7D2489"

SELECTED = {
    "targets/Noether_P04_Korean_T04_U17_UNCHECKED.tex": (1_984, "48C5D717BF3DBDE03828A3CEF518B9984D1BC43BABA9BC6645940B09E1EDCB1D"),
    "targets/Noether_P04_Korean_T04_U18_UNCHECKED.tex": (1_546, "7A5EECB9CE6AF71B372A293ED23113913CFCB8CB99454B16EFD1B181E4B1B425"),
    "targets/Noether_P04_Korean_T04_U19_UNCHECKED.tex": (2_643, "69DBA358AC9882ED3CD7935A793986281858E6F8E614733E70B8D2D689FB7E1B"),
    "targets/Noether_P04_Korean_T04_U20_UNCHECKED.tex": (2_013, "12292B0A0178D9DBA60498C8A84143624B6E8716F18FD79E5B9557D3B78B316B"),
    "targets/Noether_P04_Korean_T04_U21_UNCHECKED.tex": (2_151, "FE69137C3446CCD17F66D9FC33ECA71E3809BEDD9BFE6359407682ABD8B348C9"),
    "targets/Noether_P04_Korean_T05_U22_UNCHECKED.tex": (1_408, "372CAE0ACCFF3DC0AA4EC8313A6F09D67C8911F634D7A27287BCC1690F5F2146"),
    "targets/Noether_P04_Korean_T05_U23_UNCHECKED.tex": (3_367, "7F4659F3777765F55BBA59AC1C4F04B4EA229E0A9E394512510E227BB4296C3B"),
    "targets/Noether_P04_Korean_T05_U24_UNCHECKED.tex": (2_436, "E1D6918969032A8D6C586409B474AE99F6B76D89E9E7C576B106CA1FA3AD1AF5"),
    "targets/Noether_P04_Korean_T05_U25_UNCHECKED.tex": (1_815, "432EB596F5FA17A35B64916810C3A26A55499EF0DBD3EB84A6559FC0778A8A88"),
    "targets/Noether_P04_Korean_T05_U26_UNCHECKED.tex": (1_828, "3EF6BAEF876C909D76FF83A1324BCE3640F2DBA410A42DA4908FB61CEE8B1E6F"),
    "targets/Noether_P04_Korean_T06_U27_UNCHECKED.tex": (3_928, "5ACE78C48EEC3E2D77141EA8177F2737D9D1ED3392E465DDB080EDC0CF654760"),
    "targets/Noether_P04_Korean_T06_U28_UNCHECKED.tex": (2_056, "5AF078024CBEC085E7C7AF45B655741157C8814EFC660B1594D69844E37FF79C"),
    "targets/Noether_P04_Korean_T06_U29_UNCHECKED.tex": (2_459, "51D5EF319190C3D155F1049CDBE7958142436585EB7ACA0C0EC89CB5F978763A"),
    "targets/Noether_P04_Korean_T06_U30_UNCHECKED.tex": (1_241, "5052FF31E086BA06D5ECFE4D039A171E3F55E2055607462356B3F471181DE513"),
    "targets/Noether_P04_Korean_T06_U31_UNCHECKED.tex": (2_183, "74141212EE4CFAE1B645DB35E79A730DAE7CF2BAEF0782C46604F2D863C5A185"),
    "targets/Noether_P04_Korean_T06_U32_UNCHECKED.tex": (1_102, "01165205A8F187C8538321CBA50EFED54C41211F051F39E7A274660D4321128B"),
    "SOURCE_CUSTODY_T04_T06.md": (4_552, "0828771775F0153D1AF5B2A748266358CC28123AF160960018C2D75996EB6A1A"),
    "STATUS_T04_T06.md": (1_263, "55C88E2B8B4688C6C8C2F6437E9B0304FAE506738E036697E649AD2CDF57E70C"),
    "CHECKER_HANDOFF_T04_T06_U17_U32.md": (2_014, "AEF341B441F00E559A81BCF7124221E73AC8656B96149FA4914198C47653BB47"),
    "TRANSLATION_CHOICES_T04_T06.md": (3_891, "B06A600CF8B2E1AD72123FDBC6F8DEC77CC7199461B78579E6005512144F600B"),
}


def project(data: bytes, relative: str) -> tuple[bytes, list[tuple[str, int]]]:
    transformed, applied = engine.transform_text(data)
    engine.assert_privacy_clean(relative, transformed)
    return transformed, applied


def main() -> int:
    if PRIVATE_ROOT.exists() or PUBLIC_ROOT.exists():
        raise RuntimeError("P04 T04-T06 snapshot output exists; never overwrite a frozen revision")
    before = engine.inventory(SOURCE_ROOT)
    source_map = {row["relative_path"]: row for row in before}
    full_root_files = len(before)
    full_root_bytes = sum(int(row["bytes"]) for row in before)
    if full_root_files < len(SELECTED):
        raise RuntimeError("P04 producer root cannot contain the authorized tranche")
    if not set(SELECTED).issubset(source_map):
        raise RuntimeError("P04 authorized tranche path is missing")
    if len(SELECTED) != 20 or sum(value[0] for value in SELECTED.values()) != 45_880:
        raise RuntimeError("P04 authorized tranche declaration changed")
    for relative, expected in SELECTED.items():
        row = source_map[relative]
        if (int(row["bytes"]), row["sha256"]) != expected:
            raise RuntimeError(f"P04 selected identity changed: {relative}")
    if (POINTER_V004.stat().st_size, engine.sha256_file(POINTER_V004)) != (
        16_536,
        "A1C62FDACAA34DFC1B806DC18258F2E732539F7AE9D85AA4BD9E1067B8749D9F",
    ):
        raise RuntimeError("Noether authority pointer v004 identity changed")
    current_log = (
        engine.CJK_CONTROL / "CJK_DECISION_LOGBOOK_20260718.md"
    ).read_bytes()
    handoff_log = current_log[:HANDOFF_LOG_BYTES]
    if len(handoff_log) != HANDOFF_LOG_BYTES or engine.sha256_bytes(handoff_log) != HANDOFF_LOG_SHA256:
        raise RuntimeError("P04 append-only handoff log generation is not recoverable")

    PRIVATE_ROOT.mkdir(parents=True)
    PUBLIC_TRANCHE.mkdir(parents=True)
    raw_full = [(row["relative_path"], Path(row["path"]).read_bytes()) for row in before]
    raw_selected = [(relative, (SOURCE_ROOT / relative).read_bytes()) for relative in sorted(SELECTED)]
    full_zip = PRIVATE_ROOT / "P04_FULL_PRODUCER_ROOT_EXACT_PRIVATE_SNAPSHOT_20260804.zip"
    tranche_zip = PRIVATE_ROOT / "P04_T04_T06_20_FILE_EXACT_PRIVATE_TRANCHE_20260804.zip"
    engine.deterministic_zip(full_zip, raw_full)
    engine.deterministic_zip(tranche_zip, raw_selected)
    engine.write_csv(
        PRIVATE_ROOT / "P04_FULL_PRODUCER_ROOT_EXACT_MANIFEST.csv",
        ["relative_path", "bytes", "sha256", "tranche_disposition"],
        [
            {
                "relative_path": row["relative_path"],
                "bytes": row["bytes"],
                "sha256": row["sha256"],
                "tranche_disposition": "PUBLIC_TRANCHE_INCLUDE" if row["relative_path"] in SELECTED else "OUTSIDE_BOUNDED_T04_T06_TRANCHE_PRIVATE_CUSTODY_ONLY",
            }
            for row in before
        ],
    )

    projection_rows = []
    privacy_rows = []
    for row in before:
        relative = row["relative_path"]
        if relative not in SELECTED:
            projection_rows.append(
                {
                    "relative_path": relative,
                    "source_bytes": row["bytes"],
                    "source_sha256": row["sha256"],
                    "public_bytes": "",
                    "public_sha256": "",
                    "privacy_transformations": 0,
                    "disposition": "OUTSIDE_BOUNDED_T04_T06_TRANCHE",
                    "rationale": "preserved in exact private full-root snapshot; not authorized in this 20-file tranche",
                }
            )
            continue
        data, applied = project((SOURCE_ROOT / relative).read_bytes(), relative)
        destination = PUBLIC_TRANCHE / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(data)
        projection_rows.append(
            {
                "relative_path": relative,
                "source_bytes": row["bytes"],
                "source_sha256": row["sha256"],
                "public_bytes": len(data),
                "public_sha256": engine.sha256_bytes(data),
                "privacy_transformations": sum(count for _, count in applied),
                "disposition": "PUBLIC_TRANCHE_INCLUDE",
                "rationale": "minimal private path/operator substitution" if applied else "byte-identical source projection",
            }
        )
        for rule, count in applied:
            privacy_rows.append(
                {
                    "relative_path": relative,
                    "rule_id": rule,
                    "occurrences": count,
                    "source_sha256": row["sha256"],
                    "public_sha256": engine.sha256_bytes(data),
                    "semantic_scope": "private path/operator token only; mathematical text unchanged",
                }
            )
    engine.write_csv(
        PUBLIC_TRANCHE / "ARCHIVE_PUBLIC_PROJECTION_MANIFEST.csv",
        ["relative_path", "source_bytes", "source_sha256", "public_bytes", "public_sha256", "privacy_transformations", "disposition", "rationale"],
        projection_rows,
    )
    engine.write_csv(
        PUBLIC_TRANCHE / "ARCHIVE_PRIVACY_TRANSFORMATIONS.csv",
        ["relative_path", "rule_id", "occurrences", "source_sha256", "public_sha256", "semantic_scope"],
        privacy_rows,
    )
    engine.write_text(
        PUBLIC_TRANCHE / "ARCHIVE_PUBLICATION_README.md",
        f"""# Korean Noether Paper 4 — T04–T06 bounded tranche

This coherent public snapshot contains exactly the 20-file T04–T06 handoff: 16 editable Korean TeX units (U17–U32) plus source-custody, status, checker-handoff, and translation-choice documents. It covers authority lines 3889–4161 and continues at line 4162. It does not claim Paper 4 completion.

State: **UNCHECKED, incomplete, uncompiled, unrendered, unassembled, and unreviewed**. These labels are not release holds. Structural/difficulty extensions are pending as later evidence successors. Archive maintenance performed no source correction, checking, compilation, rendering, assembly, certification, or approval.

The full {full_root_files}-file producer root observed at this archive cursor is separately frozen in private custody. The public selection manifest records every selected and out-of-tranche identity. No visual/image file belongs to this tranche, and no special-rights item is asserted.
""",
    )
    represented = engine.inventory(PUBLIC_TRANCHE)
    validation = {
        "schema": "korean_noether_p04_t04_t06_public_snapshot_validation_v1",
        "status": "PASS_PUBLIC_UNCHECKED_INCOMPLETE_TRANCHE",
        "errors": [],
        "selected_source_files": 20,
        "selected_source_bytes": 45_880,
        "target_units": 16,
        "authority_lines": "3889-4161",
        "next_line": 4162,
        "full_producer_root_files": full_root_files,
        "full_producer_root_bytes": full_root_bytes,
        "full_producer_root_tree_sha256": engine.tree_sha(before),
        "out_of_tranche_files": full_root_files - len(SELECTED),
        "public_files_excluding_this_validation": len(represented),
        "public_bytes_excluding_this_validation": sum(int(row["bytes"]) for row in represented),
        "public_tree_sha256_excluding_this_validation": engine.tree_sha(represented),
        "privacy_transformation_occurrences": sum(int(row["occurrences"]) for row in privacy_rows),
        "state_labels": ["UNCHECKED", "incomplete", "uncompiled", "unrendered", "unassembled", "unreviewed"],
        "compile_performed": False,
        "render_performed": False,
        "review_performed": False,
        "release_hold": False,
    }
    engine.write_json(PUBLIC_TRANCHE / "ARCHIVE_SNAPSHOT_VALIDATION.json", validation)
    public_members = [
        (path.relative_to(PUBLIC_TRANCHE).as_posix(), path.read_bytes())
        for path in sorted((x for x in PUBLIC_TRANCHE.rglob("*") if x.is_file()), key=lambda x: x.relative_to(PUBLIC_TRANCHE).as_posix())
    ]
    public_zip = PUBLIC_ROOT / "P04_T04_T06_Korean_UNCHECKED_Public_Snapshot_20260804.zip"
    engine.deterministic_zip(public_zip, public_members)

    common_raw = [
        ("70_KO_CJK_DECISION_LOGBOOK_HANDOFF_EXACT_20260804.md", handoff_log),
        ("70_KO_NOETH_DE_AUTHORITY_POINTER_v004_20260804.json", POINTER_V004.read_bytes()),
    ]
    common_private_zip = PRIVATE_ROOT / "P04_COMMON_CONTROLS_EXACT_PRIVATE_SNAPSHOT_20260804.zip"
    engine.deterministic_zip(common_private_zip, common_raw)
    common_results = []
    for name, data in common_raw:
        public_name = name.replace("_HANDOFF_EXACT", "_PRIVACY_CLEAN")
        transformed, applied = project(data, public_name)
        destination = PUBLIC_ROOT / public_name
        destination.write_bytes(transformed)
        common_results.append({
            "filename": public_name,
            "source_bytes": len(data),
            "source_sha256": engine.sha256_bytes(data),
            "public_bytes": len(transformed),
            "public_sha256": engine.sha256_bytes(transformed),
            "privacy_occurrences": sum(count for _, count in applied),
        })

    index_path = PUBLIC_ROOT / "70g_KO_P04_T04_T06_SNAPSHOT_INDEX_20260804.csv"
    engine.write_csv(
        index_path,
        ["scope", "selected_files", "selected_bytes", "targets", "authority_lines", "next_line", "full_root_files", "full_root_bytes", "out_of_tranche_files", "public_zip", "public_zip_bytes", "public_zip_sha256", "public_zip_members", "state"],
        [{
            "scope": "P04_T04_T06_U17_U32",
            "selected_files": 20,
            "selected_bytes": 45_880,
            "targets": 16,
            "authority_lines": "3889-4161",
            "next_line": 4162,
            "full_root_files": full_root_files,
            "full_root_bytes": full_root_bytes,
            "out_of_tranche_files": full_root_files - len(SELECTED),
            "public_zip": public_zip.name,
            "public_zip_bytes": public_zip.stat().st_size,
            "public_zip_sha256": engine.sha256_file(public_zip),
            "public_zip_members": len(public_members),
            "state": "UNCHECKED;incomplete;uncompiled;unrendered;unassembled;unreviewed",
        }],
    )
    readme_path = PUBLIC_ROOT / "README.md"
    engine.write_text(
        readme_path,
        f"""# Korean Noether Paper 4 — T04–T06 archive snapshot

The complete ZIP is the exact privacy-clean 20-file mathematical tranche. Direct status, checker, and translation-choice surfaces identify its incomplete and UNCHECKED state. The {full_root_files - len(SELECTED)} files outside this bounded tranche are not discarded: every identity is in the public selection manifest and every byte is frozen in the exact private full-root snapshot.
""",
    )
    before_root_validation = engine.inventory(PUBLIC_ROOT)
    root_validation = {
        "schema": "korean_noether_p04_t04_t06_public_closeout_v1",
        "status": "PASS_READY_FOR_SAME_CONCEPT_PUBLICATION",
        "errors": [],
        "tranche_validation": validation,
        "public_zip": {
            "filename": public_zip.name,
            "bytes": public_zip.stat().st_size,
            "sha256": engine.sha256_file(public_zip),
            "members": len(public_members),
        },
        "common_controls": common_results,
        "private_custody": {
            "root": str(PRIVATE_ROOT),
            "full_root_zip_bytes": full_zip.stat().st_size,
            "full_root_zip_sha256": engine.sha256_file(full_zip),
            "selected_tranche_zip_bytes": tranche_zip.stat().st_size,
            "selected_tranche_zip_sha256": engine.sha256_file(tranche_zip),
            "common_controls_zip_bytes": common_private_zip.stat().st_size,
            "common_controls_zip_sha256": engine.sha256_file(common_private_zip),
        },
        "public_root_files_excluding_this_validation": len(before_root_validation),
        "public_root_bytes_excluding_this_validation": sum(int(row["bytes"]) for row in before_root_validation),
        "public_root_tree_sha256_excluding_this_validation": engine.tree_sha(before_root_validation),
        "explicit_public_exclusions": full_root_files - len(SELECTED),
        "excluded_bytes_preserved_private": True,
        "release_hold": False,
    }
    root_validation_path = PUBLIC_ROOT / "SNAPSHOT_VALIDATION.json"
    engine.write_json(root_validation_path, root_validation)
    after = engine.inventory(SOURCE_ROOT)
    if [(r["relative_path"], r["bytes"], r["sha256"]) for r in after] != [(r["relative_path"], r["bytes"], r["sha256"]) for r in before]:
        raise RuntimeError("P04 producer root changed during bounded snapshot")
    final = engine.inventory(PUBLIC_ROOT)
    result = {
        **root_validation,
        "public_root_files": len(final),
        "public_root_bytes": sum(int(row["bytes"]) for row in final),
        "public_root_tree_sha256": engine.tree_sha(final),
        "validation_path": str(root_validation_path),
        "validation_bytes": root_validation_path.stat().st_size,
        "validation_sha256": engine.sha256_file(root_validation_path),
        "index_bytes": index_path.stat().st_size,
        "index_sha256": engine.sha256_file(index_path),
        "readme_bytes": readme_path.stat().st_size,
        "readme_sha256": engine.sha256_file(readme_path),
    }
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

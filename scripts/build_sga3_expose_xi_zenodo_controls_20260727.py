#!/usr/bin/env python3
"""Build compact same-concept Zenodo controls for SGA3 Expose XI."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import zipfile
from pathlib import Path, PurePosixPath


CONCEPT_DOI = "10.5281/zenodo.20410947"
PREDECESSOR_RECORD = 21630394
PREDECESSOR_DOI = "10.5281/zenodo.21630394"
SUCCESSOR_RECORD = 21630748
SUCCESSOR_DOI = "10.5281/zenodo.21630748"
GITHUB_COMMIT = "82ebc03147b141c9db2d32906173b418238d7e3f"
GITHUB_PACKAGE = (
    "sources/sga/"
    "sga3-english-expose-xi-loop2-reference-v2-r2-20260727"
)
DEFAULT_PREVIEW = (
    "00a_SGA1_English_CompleteVolume_Working_"
    "NoExhaustiveCertification_20260722.pdf"
)

PACKAGE_FILES = {
    "SGA3_English_Expose_XI_Loop2_ReferenceV2_R2_20260727.pdf":
        "00c7_SGA3_English_Expose_XI_Loop2_ReferenceV2_R2_20260727.pdf",
    "SGA3_English_Expose_XI_Loop2_ReferenceV2_R2_Master_20260727.tex":
        "02c7_SGA3_English_Expose_XI_Loop2_ReferenceV2_R2_Master_20260727.tex",
    "SGA3_English_Expose_XI_Loop2_ReferenceV2_R2_Source_QA_20260727.zip":
        "10c7_SGA3_English_Expose_XI_Loop2_ReferenceV2_R2_Source_QA_20260727.zip",
}
PACKAGE_EXPECTED = {
    "SGA3_English_Expose_XI_Loop2_ReferenceV2_R2_20260727.pdf": (
        268_282,
        "E849010ADA0D36B3A06CA6DC5D082888E64A918C53A721526CFA2A52411FF553",
    ),
    "SGA3_English_Expose_XI_Loop2_ReferenceV2_R2_Master_20260727.tex": (
        1_731,
        "DBFA66FC0782430159DC01FF6849E58796B425DBC236E8BD7512490F699A1DCE",
    ),
    "SGA3_English_Expose_XI_Loop2_ReferenceV2_R2_Source_QA_20260727.zip": (
        15_559_954,
        "7D19A638EDF341D5E098D7041F980491E1FB528C5D4330C9479A026E9BE23CF4",
    ),
}
CONTROL_NAMES = {
    "09_README_CURRENT_RELEASE.md",
    "09a_RELEASE_FILE_MANIFEST.csv",
    "09b_RELEASE_VALIDATION.json",
}

EXPECTED_PREDECESSOR_FILES = 71
EXPECTED_PREDECESSOR_MANIFEST_ROWS = 69
EXPECTED_RETAINED_FILES = 68
EXPECTED_CONTENT_ROWS = 72
EXPECTED_FINAL_FILES = 74
EXPECTED_ZIP_ARCHIVES = 44
EXPECTED_ZIP_FILE_MEMBERS = 3_835
EXPECTED_ZIP_DIRECTORY_ENTRIES = 7
EXPECTED_ZIP_ALL_ENTRIES = 3_842
EXPECTED_ZIP_UNCOMPRESSED_BYTES = 403_339_159
RELEASE_CONTROL_COMPATIBILITY_COUNTER = 3_841


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def identity(path: Path) -> dict[str, int | str]:
    data = path.read_bytes()
    return {"bytes": len(data), "sha256": sha256_bytes(data)}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    fields = ["filename", "bytes", "sha256", "role", "provenance", "status"]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def formula_safe(rows: list[dict[str, object]]) -> bool:
    return all(
        not str(value).startswith(("=", "+", "-", "@"))
        for row in rows
        for value in row.values()
    )


def safe_member_name(name: str) -> bool:
    path = PurePosixPath(name)
    return (
        bool(name)
        and not name.startswith(("/", "\\"))
        and not (len(name) >= 2 and name[1] == ":")
        and ".." not in path.parts
        and "\\" not in name
    )


def build_readme() -> str:
    return f"""# Current compact SGA release

This same-concept successor preserves the reader-first SGA surface from
version {PREDECESSOR_DOI}. Sixty-eight predecessor files outside the three
release controls remain byte-identical. The controls are refreshed and the
independently audited complete bounded SGA3 Expose XI checkpoint is added as
one direct reader, one direct editable master TeX, and one grouped source/QA
archive.

## Reader-first order

1. English SGA1 complete-volume working reader. Its clickable-reference
   infrastructure is substantial but not exhaustively convention-v2
   certified.
2. English SGA2 complete archive-curated reference-linked R8 reader.
3. English SGA3 cumulative working reader through complete Expose IV,
   followed by standalone native-diagram/reference-linked readers for
   complete Exposes V, VI, VIII, IX, and XI. Expose VII, Expose X, and
   Exposes XII-XXVI are absent from the current public reader surface.
4. English SGA4 proper certified reference-v2 r7 reader, covering Exposes
   I-XIX including V bis and excluding SGA4half.
5. English SGA5 reference-linked R9 reader.
6. English SGA6 complete layered terminal reference-linked reader.

Available French workpasses and primary editable TeX follow the English
readers. Recursive sources, machine-readable ledgers, QA, bounded
checkpoints, predecessor material, and high-detail visual evidence remain
grouped into coherent ZIP archives. SGA1 remains the initial preview.

## SGA3 Expose XI

The new 38-page A4 reader covers authority-local pages 1-34 /
combined-reader pages 723-756 and stops before combined page 757 / Expose
XII. It has eight native diagrams, 297 named destinations, 328 valid internal
GoTo actions, 32 embedded non-Type3 fonts, and no raster XObjects.

The grouped ZIP contains 124 exact non-directory members totaling 18,356,104
uncompressed bytes: 13 editable TeX files, the reader, all 38 reviewed page
renders, target-only 300/600/1200 dpi cold-reverify evidence, reference-v2
graph data, source/translation QA, audit receipts, provenance and rights
notices, and recursive checksums. The graph records 214 targets and 728
candidates partitioned into 283 applied edges and 445 positive residuals,
with zero pending actions.

Fresh extracted-package replay passed with SHA-256
`178639736D32B1F66C3848FCDFD512A0360D96908A73C7A1E7770858FD872960`.
The package-bound independent prepackage audit has SHA-256
`3AC91C2D254B0DFE0669274C17ED440A1DFD385110F0AF92A5E920DF0389DDFE`,
and the Claude-style high-zoom cold-reverify receipt has SHA-256
`D852EECC167479848EA85831389A54CC1607B937EBCB3CF9130AE43EF8964F22`.
Archive-maintenance custody replay found zero manifest differences, zero
private-path hits, and zero pixel differences on independently rendered pages
1, 19, and 38.

This is complete Expose XI, not complete SGA3. Expose VII and Expose X remain
absent; Expose XII onward is outside this release. The checkpoint is a bounded
source-audited working translation and reference-linked reader, not a
critical edition, mathematical certification, independent human peer review,
rights determination, or tagged/accessibility-remediated PDF.

## Authority, attribution, and rights

The Polo-Gille Expose XI PDF `Expo11.pdf`, 34 pages / 431,100 bytes, SHA-256
`CDB58EA5518C29E998E12AEA8D958E488C466C3B12FE2ED178A009758A553EAD`,
is the controlling prose, formula, page, and diagram witness. It is not
redistributed and is not recovered editor TeX. OCR is locator/drafting
material only.

Jacob C. Reinhold's Expose XI Markdown from `jcreinhold/sga` commit
`e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e` is credited comparison
material, not authority or independent corroboration. Its declared CC BY 4.0
terms apply only to that contribution and grant no broader rights.

No blanket license or rights clearance is asserted. Rights in the underlying
French work, Polo-Gille re-edition, English reconstruction, and editorial
additions remain with their respective holders. Machine-assisted
contributors include OpenAI Codex / ChatGPT and Anthropic Claude under human
direction.

The current SGA6 visual-evidence surface is otherwise unchanged: 2,183
selected images are public, and 3,253 routine page derivatives remain
represented by rights-blocked metadata. Live SGA6 work beginning at idx618
remains excluded.

Existing concept DOI: {CONCEPT_DOI}.
Predecessor version preserved: {PREDECESSOR_DOI}.
GitHub package commit: {GITHUB_COMMIT}.
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--predecessor-readback", type=Path, required=True)
    parser.add_argument("--predecessor-manifest", type=Path, required=True)
    parser.add_argument("--predecessor-validation", type=Path, required=True)
    parser.add_argument("--package-root", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    args = parser.parse_args()

    errors: list[str] = []
    receipt = json.loads(
        args.predecessor_readback.read_text(encoding="utf-8-sig")
    )
    predecessor_validation = json.loads(
        args.predecessor_validation.read_text(encoding="utf-8-sig")
    )
    package_validation = json.loads(
        (args.package_root / "PACKAGE_VALIDATION.json").read_text(
            encoding="utf-8-sig"
        )
    )
    package_rows = read_csv(args.package_root / "SHA256SUMS.csv")
    predecessor_rows = read_csv(args.predecessor_manifest)

    if receipt.get("status") != "PASS":
        errors.append("predecessor_readback_status")
    if int(receipt.get("record", {}).get("id", -1)) != PREDECESSOR_RECORD:
        errors.append("predecessor_record")
    outer_rows = receipt.get("outer_files", [])
    if len(outer_rows) != EXPECTED_PREDECESSOR_FILES:
        errors.append(f"predecessor_files:{len(outer_rows)}")
    if predecessor_validation.get("status") != "PASS":
        errors.append("predecessor_validation_status")
    if len(predecessor_rows) != EXPECTED_PREDECESSOR_MANIFEST_ROWS:
        errors.append(f"predecessor_manifest_rows:{len(predecessor_rows)}")
    if package_validation.get("status") != "PASS":
        errors.append("package_validation_status")

    readback_by_name = {row["filename"]: row for row in outer_rows}
    if len(readback_by_name) != len(outer_rows):
        errors.append("predecessor_duplicate_filenames")
    for row in predecessor_rows:
        remote = readback_by_name.get(row["filename"])
        if remote is None:
            errors.append(f"predecessor_manifest_missing:{row['filename']}")
            continue
        if (
            int(row["bytes"]) != int(remote["bytes"])
            or row["sha256"].upper() != remote["sha256"].upper()
        ):
            errors.append(f"predecessor_manifest_identity:{row['filename']}")

    package_by_name = {row["filename"]: row for row in package_rows}
    for source_name, expected in PACKAGE_EXPECTED.items():
        source = args.package_root / source_name
        if not source.is_file():
            errors.append(f"package_missing:{source_name}")
            continue
        current = identity(source)
        if (current["bytes"], current["sha256"]) != expected:
            errors.append(f"package_identity:{source_name}")
        row = package_by_name.get(source_name)
        if row is None:
            errors.append(f"package_manifest_missing:{source_name}")
        elif (
            int(row["bytes"]) != current["bytes"]
            or row["sha256"].upper() != current["sha256"]
        ):
            errors.append(f"package_manifest_identity:{source_name}")

    zip_source = (
        args.package_root
        / "SGA3_English_Expose_XI_Loop2_ReferenceV2_R2_Source_QA_20260727.zip"
    )
    with zipfile.ZipFile(zip_source) as archive:
        infos = [item for item in archive.infolist() if not item.is_dir()]
        unsafe = [
            item.filename
            for item in infos
            if not safe_member_name(item.filename)
        ]
        if archive.testzip() is not None:
            errors.append("package_zip_crc")
        if len(infos) != 124:
            errors.append(f"package_zip_members:{len(infos)}")
        if sum(item.file_size for item in infos) != 18_356_104:
            errors.append("package_zip_uncompressed_bytes")
        if unsafe:
            errors.extend(f"unsafe_zip_member:{name}" for name in unsafe)

    output = args.output_root.resolve()
    if output.exists() and any(output.iterdir()):
        raise SystemExit(f"Output root must be absent or empty: {output}")
    if errors:
        raise SystemExit(json.dumps({"status": "FAIL", "errors": errors}, indent=2))
    output.mkdir(parents=True, exist_ok=True)

    for source_name, release_name in PACKAGE_FILES.items():
        shutil.copyfile(args.package_root / source_name, output / release_name)

    readme_path = output / "09_README_CURRENT_RELEASE.md"
    readme_path.write_text(build_readme(), encoding="utf-8", newline="\n")

    retained_rows = [
        dict(row)
        for row in predecessor_rows
        if row["filename"] != "09_README_CURRENT_RELEASE.md"
    ]
    if len(retained_rows) != EXPECTED_RETAINED_FILES:
        raise SystemExit(
            f"Expected {EXPECTED_RETAINED_FILES} retained rows, "
            f"found {len(retained_rows)}"
        )

    def new_row(
        filename: str, role: str, provenance: str, status: str
    ) -> dict[str, object]:
        current = identity(output / filename)
        return {
            "filename": filename,
            "bytes": current["bytes"],
            "sha256": current["sha256"],
            "role": role,
            "provenance": provenance,
            "status": status,
        }

    new_rows = [
        new_row(
            "00c7_SGA3_English_Expose_XI_Loop2_ReferenceV2_R2_20260727.pdf",
            "english_reader",
            (
                "complete bounded SGA3 Expose XI source-audited "
                f"Loop2/reference-v2 reader; GitHub commit {GITHUB_COMMIT}"
            ),
            "bounded_working_reader_sga3_incomplete_expose_xi_complete",
        ),
        new_row(
            "02c7_SGA3_English_Expose_XI_Loop2_ReferenceV2_R2_Master_20260727.tex",
            "editable_source",
            (
                "direct editable Expose XI master; eleven components and macros "
                "are preserved in the grouped source archive"
            ),
            "bounded_editable_master_sga3_incomplete_expose_xi_complete",
        ),
        new_row(
            "09_README_CURRENT_RELEASE.md",
            "manifest_status",
            "current compact release note adding bounded complete Expose XI",
            "current_release_control",
        ),
        new_row(
            "10c7_SGA3_English_Expose_XI_Loop2_ReferenceV2_R2_Source_QA_20260727.zip",
            "grouped_source_and_evidence",
            (
                "124-member privacy-clean editable source, reference graph, "
                "all-page render QA, audit, rights, and identity archive"
            ),
            "bounded_working_package_sga3_incomplete_expose_xi_complete",
        ),
    ]
    final_rows = sorted(
        retained_rows + new_rows, key=lambda row: row["filename"].casefold()
    )
    if len(final_rows) != EXPECTED_CONTENT_ROWS:
        raise SystemExit(
            f"Expected {EXPECTED_CONTENT_ROWS} content rows, "
            f"found {len(final_rows)}"
        )
    if not formula_safe(final_rows):
        raise SystemExit("Formula-unsafe release manifest value")

    manifest_path = output / "09a_RELEASE_FILE_MANIFEST.csv"
    write_csv(manifest_path, final_rows)
    manifest_id = identity(manifest_path)

    final_file_bytes = sum(int(row["bytes"]) for row in final_rows)
    predecessor_zip_count = int(
        receipt.get("zip_archive_count", EXPECTED_ZIP_ARCHIVES - 1)
    )
    predecessor_zip_members = int(
        receipt.get("zip_file_member_count", EXPECTED_ZIP_FILE_MEMBERS - 124)
    )
    predecessor_zip_dirs = int(
        receipt.get(
            "zip_directory_entry_count",
            EXPECTED_ZIP_DIRECTORY_ENTRIES,
        )
    )
    predecessor_zip_uncompressed = int(
        receipt.get(
            "zip_uncompressed_bytes",
            EXPECTED_ZIP_UNCOMPRESSED_BYTES - 18_356_104,
        )
    )

    validation = {
        "status": "PASS",
        "errors": [],
        "concept_doi": CONCEPT_DOI,
        "predecessor_record": PREDECESSOR_RECORD,
        "predecessor_doi": PREDECESSOR_DOI,
        "reserved_successor_record": SUCCESSOR_RECORD,
        "reserved_successor_doi": SUCCESSOR_DOI,
        "same_concept_only": True,
        "duplicate_concept_authorized": False,
        "retained_predecessor_files": EXPECTED_RETAINED_FILES,
        "replaced_files": sorted(CONTROL_NAMES),
        "new_sga3_expose_xi_files": sorted(PACKAGE_FILES.values()),
        "content_manifest_rows": len(final_rows),
        "release_manifest_file": manifest_path.name,
        "release_manifest_bytes": manifest_id["bytes"],
        "release_manifest_sha256": manifest_id["sha256"],
        "final_upload_file_count": EXPECTED_FINAL_FILES,
        "final_content_bytes_before_validation": final_file_bytes,
        "default_preview": DEFAULT_PREVIEW,
        "github": {
            "commit": GITHUB_COMMIT,
            "package": GITHUB_PACKAGE,
            "outer_files": 7,
            "readback_files": 8,
            "readback_errors": [],
        },
        "sga3_expose_xi": {
            "scope": "complete bounded SGA3 Expose XI",
            "combined_pages": "723-756",
            "hard_stop": "before combined page 757 / Expose XII",
            "sga3_complete": False,
            "excluded_scope": "Expose VII, Expose X, and Exposes XII-XXVI",
            "reader_pages": 38,
            "reader_sha256": PACKAGE_EXPECTED[
                "SGA3_English_Expose_XI_Loop2_ReferenceV2_R2_20260727.pdf"
            ][1],
            "editable_tex_files": 13,
            "native_diagrams": 8,
            "active_raster_image_inclusions": 0,
            "reference_targets": 214,
            "reference_edges": 283,
            "reference_candidates": 728,
            "positive_residuals": 445,
            "pdf_named_destinations": 297,
            "pdf_goto_actions": 328,
            "visual_qa_pages": 38,
            "source_archive_members": 124,
            "source_archive_uncompressed_bytes": 18_356_104,
            "member_manifest_rows": 123,
            "member_manifest_sha256":
                "D1C019910959F7E1426088E2634F36A18CCE96F9C86DC403AB302B2388D9EEB3",
            "independent_validation_sha256":
                "178639736D32B1F66C3848FCDFD512A0360D96908A73C7A1E7770858FD872960",
            "independent_prepackage_audit_sha256":
                "3AC91C2D254B0DFE0669274C17ED440A1DFD385110F0AF92A5E920DF0389DDFE",
            "diagram_cold_reverify_receipt_sha256":
                "D852EECC167479848EA85831389A54CC1607B937EBCB3CF9130AE43EF8964F22",
        },
        "sga3_expose_ix": predecessor_validation.get(
            "sga3_expose_ix", {}
        ),
        "sga3_expose_viii": predecessor_validation.get(
            "sga3_expose_viii", {}
        ),
        "sga6_source_audit_crops": predecessor_validation.get(
            "sga6_source_audit_crops", {}
        ),
        "sga3_diagram_cold_reverify": {
            "control_sha256":
                "8682D7E64EADF2E92F8015EF79BA337D3ADB062B232F296DEB6C4009360D10CB",
            "published_history_immutable": True,
            "expose_vii":
                "held_machine_evidence_failure_and_no_compliant_final_receipt",
            "expose_xi":
                "published_target_only_high_zoom_cold_reverify_compliant",
        },
        "zip_archive_count": predecessor_zip_count + 1,
        "zip_file_member_count": predecessor_zip_members + 124,
        "zip_directory_entry_count": predecessor_zip_dirs,
        "zip_all_entry_count": (
            predecessor_zip_members + 124 + predecessor_zip_dirs
        ),
        "release_control_compatibility_counter":
            RELEASE_CONTROL_COMPATIBILITY_COUNTER,
        "zip_uncompressed_bytes":
            predecessor_zip_uncompressed + 18_356_104,
        "rights": {
            "new_license_grant": False,
            "rights_clearance_claimed": False,
            "underlying_french_rights_retained": True,
            "authority_pdf_redistributed": False,
            "comparison_body_redistributed": False,
            "critical_edition_claimed": False,
            "whole_sga3_claimed": False,
        },
        "contributors": [
            "OpenAI Codex / ChatGPT",
            "Anthropic Claude",
        ],
        "privacy_hits": [],
    }
    if (
        validation["zip_archive_count"] != EXPECTED_ZIP_ARCHIVES
        or validation["zip_file_member_count"] != EXPECTED_ZIP_FILE_MEMBERS
        or validation["zip_directory_entry_count"]
        != EXPECTED_ZIP_DIRECTORY_ENTRIES
        or validation["zip_all_entry_count"] != EXPECTED_ZIP_ALL_ENTRIES
        or validation["zip_uncompressed_bytes"]
        != EXPECTED_ZIP_UNCOMPRESSED_BYTES
    ):
        raise SystemExit("Cumulative ZIP boundary mismatch")

    validation_path = output / "09b_RELEASE_VALIDATION.json"
    validation_path.write_text(
        json.dumps(validation, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    final_total_bytes = (
        final_file_bytes
        + manifest_path.stat().st_size
        + validation_path.stat().st_size
    )
    validation["final_upload_bytes"] = final_total_bytes
    validation_path.write_text(
        json.dumps(validation, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )

    final_total_bytes = (
        final_file_bytes
        + manifest_path.stat().st_size
        + validation_path.stat().st_size
    )
    if validation["final_upload_bytes"] != final_total_bytes:
        validation["final_upload_bytes"] = final_total_bytes
        validation_path.write_text(
            json.dumps(validation, indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        final_total_bytes = (
            final_file_bytes
            + manifest_path.stat().st_size
            + validation_path.stat().st_size
        )
    if validation["final_upload_bytes"] != final_total_bytes:
        raise SystemExit("Validation byte count did not stabilize")

    all_output = [path for path in output.iterdir() if path.is_file()]
    if len(all_output) != 6:
        raise SystemExit(f"Expected 6 staged files, found {len(all_output)}")
    print(
        json.dumps(
            {
                "status": "PASS",
                "errors": [],
                "output": str(output),
                "local_files": {
                    path.name: identity(path)
                    for path in sorted(all_output, key=lambda item: item.name)
                },
                "content_manifest_rows": len(final_rows),
                "final_upload_files": EXPECTED_FINAL_FILES,
                "final_upload_bytes": final_total_bytes,
                "zip_archive_count": EXPECTED_ZIP_ARCHIVES,
                "zip_file_members": EXPECTED_ZIP_FILE_MEMBERS,
                "zip_directory_entries": EXPECTED_ZIP_DIRECTORY_ENTRIES,
                "zip_uncompressed_bytes": EXPECTED_ZIP_UNCOMPRESSED_BYTES,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()

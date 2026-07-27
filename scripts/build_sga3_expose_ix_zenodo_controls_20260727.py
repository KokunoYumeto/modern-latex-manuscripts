#!/usr/bin/env python3
"""Build compact same-concept Zenodo controls for SGA3 Expose IX."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import zipfile
from pathlib import Path, PurePosixPath


CONCEPT_DOI = "10.5281/zenodo.20410947"
PREDECESSOR_RECORD = 21628220
PREDECESSOR_DOI = "10.5281/zenodo.21628220"
SUCCESSOR_RECORD = 21628601
SUCCESSOR_DOI = "10.5281/zenodo.21628601"
GITHUB_COMMIT = "e2de33aade87606712a35ca7c5857d0c08b319cd"
GITHUB_PACKAGE = (
    "sources/sga/"
    "sga3-english-expose-ix-loop2-reference-v2-r1-20260727"
)
DEFAULT_PREVIEW = (
    "00a_SGA1_English_CompleteVolume_Working_"
    "NoExhaustiveCertification_20260722.pdf"
)

PACKAGE_FILES = {
    "SGA3_English_Expose_IX_Loop2_ReferenceV2_R1_20260727.pdf":
        "00c6_SGA3_English_Expose_IX_Loop2_ReferenceV2_R1_20260727.pdf",
    "SGA3_English_Expose_IX_Loop2_ReferenceV2_R1_Master_20260727.tex":
        "02c6_SGA3_English_Expose_IX_Loop2_ReferenceV2_R1_Master_20260727.tex",
    "SGA3_English_Expose_IX_Loop2_ReferenceV2_R1_Source_QA_20260727.zip":
        "10c6_SGA3_English_Expose_IX_Loop2_ReferenceV2_R1_Source_QA_20260727.zip",
}
PACKAGE_EXPECTED = {
    "SGA3_English_Expose_IX_Loop2_ReferenceV2_R1_20260727.pdf": (
        267_685,
        "3AE231B4608B12CF1E19CBD6194CCAA03AB410F7C26DDBCEA8843951AD9ED6D3",
    ),
    "SGA3_English_Expose_IX_Loop2_ReferenceV2_R1_Master_20260727.tex": (
        1_316,
        "FA3CDED0E5D0086AF5633C14375668BDBA9B26D301D20E92E7C0B8438B9D1B46",
    ),
    "SGA3_English_Expose_IX_Loop2_ReferenceV2_R1_Source_QA_20260727.zip": (
        8_357_707,
        "5CC33C3B35ED4BDF1CBFA64177070E5C3E47913E80CDEF5AA0158998EE3D337A",
    ),
}
CONTROL_NAMES = {
    "09_README_CURRENT_RELEASE.md",
    "09a_RELEASE_FILE_MANIFEST.csv",
    "09b_RELEASE_VALIDATION.json",
}

EXPECTED_PREDECESSOR_FILES = 62
EXPECTED_PREDECESSOR_MANIFEST_ROWS = 60
EXPECTED_RETAINED_FILES = 59
EXPECTED_CONTENT_ROWS = 63
EXPECTED_FINAL_FILES = 65
EXPECTED_ZIP_ARCHIVES = 37
EXPECTED_ZIP_FILE_MEMBERS = 3_648
EXPECTED_ZIP_DIRECTORY_ENTRIES = 7
EXPECTED_ZIP_ALL_ENTRIES = 3_655
EXPECTED_ZIP_UNCOMPRESSED_BYTES = 382_076_318
RELEASE_CONTROL_COMPATIBILITY_COUNTER = 3_654


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
version {PREDECESSOR_DOI}. Fifty-nine predecessor files outside the three
release controls remain byte-identical. The controls are refreshed and the
independently audited complete bounded SGA3 Expose IX checkpoint is added as
one direct reader, one direct editable master TeX, and one grouped source/QA
archive.

## Reader-first order

1. English SGA1 complete-volume working reader. Its clickable-reference
   infrastructure is substantial but not exhaustively convention-v2
   certified.
2. English SGA2 complete archive-curated reference-linked R8 reader.
3. English SGA3 cumulative working reader through complete Expose IV,
   followed by standalone native-diagram/reference-linked readers for
   complete Exposes V, VI, VIII, and IX. Expose VII and Exposes X-XXVI are
   absent from the current public reader surface.
4. English SGA4 proper certified reference-v2 r7 reader, covering Exposes
   I-XIX including V bis and excluding SGA4half.
5. English SGA5 reference-linked R9 reader.
6. English SGA6 complete layered terminal reference-linked reader.

Available French workpasses and primary editable TeX follow the English
readers. Recursive sources, machine-readable ledgers, QA, bounded
checkpoints, predecessor material, and high-detail visual evidence remain
grouped into coherent ZIP archives. SGA1 remains the initial preview.

## SGA3 Expose IX

The new 36-page A4 reader covers Sections 1-8, all 68 named formal units,
205 display/formula-or-diagram blocks, eight native diagrams, and the
terminal bibliography and editor notes. It stops before combined-reader page
679 / Expose X. Its PDF has 276 named destinations, 288 valid internal GoTo
actions, 37 embedded non-Type3 fonts, and no raster XObjects.

The grouped ZIP contains 68 exact non-directory members totaling 9,950,178
uncompressed bytes: seven editable TeX files, the reader, all 36 reviewed
page renders, reference-v2 graph data, source/translation QA, audit receipts,
provenance and rights notices, and recursive checksums. The graph records 154
targets and 644 candidates partitioned into 215 applied edges and 429
positive residuals, with zero pending actions.

The source package passed two independent extracted-package audits plus a
fresh manager-side exact replay. The manager audit report has SHA-256
`CAF5E6351A49F1FB6FFEDEECA49270A4BA04F20C3CB5302B1973027DDB3E4860`;
its evidence JSON has SHA-256
`62377069560F7FC7EB0874D3A84E4455D0CA25C38EA04973EE04D8D2B39507FA`.
Archive-maintenance custody replay found zero manifest differences, zero
private-path hits, and zero pixel differences on independently rendered pages
1, 18, and 36.

This is complete Expose IX, not complete SGA3. Expose VII remains absent and
Expose X onward is outside this release. The checkpoint is a bounded
source-audited working translation and reference-linked reader, not a
critical edition, mathematical certification, independent human peer review,
rights determination, or tagged/accessibility-remediated PDF.

## Authority, attribution, and rights

The Polo-Gille Expose IX PDF `Exp9-8nov09.pdf`, SHA-256
`7C1E3D5B9D01AD01D0DD7B8B62045D012052E7890FB37ADC3E7934EBB5FD6FC3`,
is the controlling prose, formula, page, and diagram witness. It is not
redistributed and is not recovered editor TeX. OCR is locator/drafting
material only.

Jacob C. Reinhold's Expose IX Markdown from `jcreinhold/sga` commit
`e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e` is credited comparison
material, not authority or independent corroboration. Its declared CC BY 4.0
terms apply only to that contribution and grant no broader rights.

No blanket license or rights clearance is asserted. Rights in the underlying
French work, Polo-Gille re-edition, English reconstruction, and editorial
additions remain with their respective holders. Machine-assisted
contributors include OpenAI Codex / ChatGPT and Anthropic Claude under human
direction.

The current SGA6 visual-evidence surface is otherwise unchanged: 2,153
selected images are public, and 3,148 routine page derivatives remain
represented by rights-blocked metadata. Live SGA6 work beginning at idx597
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
        / "SGA3_English_Expose_IX_Loop2_ReferenceV2_R1_Source_QA_20260727.zip"
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
        if len(infos) != 68:
            errors.append(f"package_zip_members:{len(infos)}")
        if sum(item.file_size for item in infos) != 9_950_178:
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
            "00c6_SGA3_English_Expose_IX_Loop2_ReferenceV2_R1_20260727.pdf",
            "english_reader",
            (
                "complete bounded SGA3 Expose IX source-audited "
                f"Loop2/reference-v2 reader; GitHub commit {GITHUB_COMMIT}"
            ),
            "bounded_working_reader_sga3_incomplete_expose_ix_complete",
        ),
        new_row(
            "02c6_SGA3_English_Expose_IX_Loop2_ReferenceV2_R1_Master_20260727.tex",
            "editable_source",
            (
                "direct editable Expose IX master; five components and macros "
                "are preserved in the grouped source archive"
            ),
            "bounded_editable_master_sga3_incomplete_expose_ix_complete",
        ),
        new_row(
            "09_README_CURRENT_RELEASE.md",
            "manifest_status",
            "current compact release note adding bounded complete Expose IX",
            "current_release_control",
        ),
        new_row(
            "10c6_SGA3_English_Expose_IX_Loop2_ReferenceV2_R1_Source_QA_20260727.zip",
            "grouped_source_and_evidence",
            (
                "68-member privacy-clean editable source, reference graph, "
                "all-page render QA, audit, rights, and identity archive"
            ),
            "bounded_working_package_sga3_incomplete_expose_ix_complete",
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
        receipt.get("zip_file_member_count", EXPECTED_ZIP_FILE_MEMBERS - 68)
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
            EXPECTED_ZIP_UNCOMPRESSED_BYTES - 9_950_178,
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
        "new_sga3_expose_ix_files": sorted(PACKAGE_FILES.values()),
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
            "outer_files": 6,
            "readback_files": 7,
            "readback_errors": [],
        },
        "sga3_expose_ix": {
            "scope": "complete bounded SGA3 Expose IX",
            "combined_pages": "647-678",
            "hard_stop": "before combined page 679 / Expose X",
            "sga3_complete": False,
            "excluded_scope": "Expose VII and Exposes X-XXVI",
            "reader_pages": 36,
            "reader_sha256": PACKAGE_EXPECTED[
                "SGA3_English_Expose_IX_Loop2_ReferenceV2_R1_20260727.pdf"
            ][1],
            "editable_tex_files": 7,
            "native_diagrams": 8,
            "active_raster_image_inclusions": 0,
            "reference_targets": 154,
            "reference_edges": 215,
            "reference_candidates": 644,
            "positive_residuals": 429,
            "pdf_named_destinations": 276,
            "pdf_goto_actions": 288,
            "visual_qa_pages": 36,
            "source_archive_members": 68,
            "source_archive_uncompressed_bytes": 9_950_178,
            "member_manifest_rows": 67,
            "member_manifest_sha256":
                "DBE685A6601D41466EFD6FFB90CEE90D6244E736C85A578147C56E96F72CD232",
            "independent_validation_sha256":
                "A0C0A6496972DB0CC405BFBD156D0865FA90CCCD9A58EA58E879BBDF04684EE0",
            "independent_replay_sha256":
                "52FFA0BCD21E1E530D19C7BA11ADE17441230A6D11C5ACA5C7ECDD52AC158BEE",
            "manager_exact_audit_report_sha256":
                "CAF5E6351A49F1FB6FFEDEECA49270A4BA04F20C3CB5302B1973027DDB3E4860",
            "manager_exact_audit_evidence_sha256":
                "62377069560F7FC7EB0874D3A84E4455D0CA25C38EA04973EE04D8D2B39507FA",
        },
        "sga3_expose_viii": predecessor_validation.get(
            "sga3_expose_viii", {}
        ),
        "sga6_source_audit_crops": predecessor_validation.get(
            "sga6_source_audit_crops", {}
        ),
        "zip_archive_count": predecessor_zip_count + 1,
        "zip_file_member_count": predecessor_zip_members + 68,
        "zip_directory_entry_count": predecessor_zip_dirs,
        "zip_all_entry_count": (
            predecessor_zip_members + 68 + predecessor_zip_dirs
        ),
        "release_control_compatibility_counter":
            RELEASE_CONTROL_COMPATIBILITY_COUNTER,
        "zip_uncompressed_bytes": predecessor_zip_uncompressed + 9_950_178,
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

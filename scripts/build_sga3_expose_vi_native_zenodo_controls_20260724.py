#!/usr/bin/env python3
"""Build same-concept Zenodo controls for SGA3 Expose VI freeze4."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import zipfile
from pathlib import Path


CONCEPT_DOI = "10.5281/zenodo.20410947"
PREDECESSOR_RECORD = 21522077
PREDECESSOR_DOI = "10.5281/zenodo.21522077"
GITHUB_COMMIT = "c7b3ff769f23ad1e342c769c92493d7788d43c72"
GITHUB_PACKAGE = (
    "sources/sga/"
    "sga3-english-expose-vi-native-reference-v2-r4-freeze4-20260724"
)

OLD_SGA3_VI_FILES = {
    "00c4_SGA3_English_Expose_VIA_Loop1_Working_20260723.pdf",
    "02c4_SGA3_English_Expose_VIA_Loop1_Working_Master_20260723.tex",
    "10c4_SGA3_English_Expose_VIA_Loop1_Working_Source_Evidence_20260723.zip",
}

SOURCE_TO_RELEASE = {
    "SGA3_English_Expose_VI_Native_ReferenceV2_R4_20260724.pdf":
        "00c4_SGA3_English_Expose_VI_Native_ReferenceV2_R4_20260724.pdf",
    "SGA3_English_Expose_VI_Native_ReferenceV2_R4_Master_20260724.tex":
        "02c4_SGA3_English_Expose_VI_Native_ReferenceV2_R4_Master_20260724.tex",
    "SGA3_English_Expose_VI_Native_ReferenceV2_R4_Source_Evidence_20260724.zip":
        "10c4_SGA3_English_Expose_VI_Native_ReferenceV2_R4_Source_Evidence_20260724.zip",
}

CONTROL_NAMES = {
    "09_README_CURRENT_RELEASE.md",
    "09a_RELEASE_FILE_MANIFEST.csv",
    "09b_RELEASE_VALIDATION.json",
}

DEFAULT_PREVIEW = (
    "00a_SGA1_English_CompleteVolume_Working_"
    "NoExhaustiveCertification_20260722.pdf"
)


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


def build_readme() -> str:
    return f"""# Current SGA compact release

This same-concept successor replaces the bounded SGA 3 Expose VI-A Loop-1
objects with the independently audited complete Expose VI A+B native-diagram
and reference-v2 freeze4 reader, editable master, and grouped source/evidence
archive. It preserves 48 unrelated predecessor files byte-identically and
preserves every predecessor version immutably.

## Reader-first order

1. English SGA 1 complete-volume working reader. Its clickable-reference
   infrastructure is substantial but not exhaustively convention-v2
   certified.
2. English SGA 2 complete archive-curated reference-linked R8 reader.
3. English SGA 3 cumulative working reader through complete Expose IV,
   followed by complete standalone native-diagram readers for Exposes V and
   VI.
4. English SGA 4 proper certified reference-v2 r7 reader, covering Exposes
   I-XIX including V bis and excluding SGA 4half.
5. English SGA 5 reference-linked R9 reader.
6. English SGA 6 complete layered terminal reference-linked reader.

Available French workpasses and primary editable TeX follow the English
readers. Recursive source, machine-readable ledgers, QA, bounded checkpoints,
predecessor material, and high-detail visual evidence remain grouped into
coherent ZIP archives.

## SGA 3 Expose VI

The new 185-page standalone reader covers all of Expose VI-A and VI-B. Its
editable source consists of one master and 90 component TeX files. All 58
diagrams are native; the built reader has zero active raster-image inclusions.
Reference-v2 evidence records 987 targets, 672 linked edges, 7,629 candidates,
6,957 positive residuals, 1,224 named destinations, and 948 valid internal
GoTo actions. All 185 pages passed direct render review.

The grouped ZIP contains 133 exact members totaling 25,834,446 uncompressed
bytes. It contains the privacy-clean public projection, native diagram source,
reference data, build and review evidence, provenance and rights notices, and
recursive identity controls. GitHub and Zenodo publish identical outer PDF,
TeX, and ZIP bytes.

This is complete Expose VI, not complete SGA 3. Exposes VII-XXVI remain
untranslated and excluded. This is a bounded working translation and
reference-linked reader, not a critical edition, mathematical certification,
independent human peer review, or tagged/accessibility-remediated PDF.

## Authority, attribution, and rights

The Polo-Gille Expose VI-A and VI-B PDFs are controlling prose, formula, page,
and diagram witnesses. They are identity controls only and are not
redistributed. OCR is locator and drafting material only. Jacob C. Reinhold's
`jcreinhold/sga` snapshot
`e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e` is credited comparison and
drafting lineage, not authority. Reinhold states that his translation
contribution is CC BY 4.0; that statement does not license the underlying
French work or unrelated contributions.

No new blanket license or rights clearance is asserted. Rights in the
underlying French work and Polo-Gille re-edition remain with their holders.
Machine-assisted contributors include OpenAI Codex / ChatGPT and Anthropic
Claude under human direction.

The SGA 1 working reader remains the initial preview.

Existing concept DOI: {CONCEPT_DOI}.
Predecessor version preserved: {PREDECESSOR_DOI}.
GitHub package commit: {GITHUB_COMMIT}.
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--predecessor-manifest", type=Path, required=True)
    parser.add_argument("--predecessor-validation", type=Path, required=True)
    parser.add_argument("--predecessor-readback", type=Path, required=True)
    parser.add_argument("--package-root", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--successor-record", type=int, required=True)
    args = parser.parse_args()

    predecessor_rows = read_csv(args.predecessor_manifest)
    predecessor_validation = json.loads(
        args.predecessor_validation.read_text(encoding="utf-8-sig")
    )
    predecessor_readback = json.loads(
        args.predecessor_readback.read_text(encoding="utf-8-sig")
    )
    package_validation = json.loads(
        (args.package_root / "PACKAGE_VALIDATION.json").read_text(
            encoding="utf-8-sig"
        )
    )
    package_rows = read_csv(args.package_root / "SHA256SUMS.csv")

    errors: list[str] = []
    if len(predecessor_rows) != 52:
        errors.append(f"predecessor_manifest_rows:{len(predecessor_rows)}")
    if predecessor_validation.get("status") != "PASS":
        errors.append("predecessor_validation_not_pass")
    if predecessor_readback.get("status") != "PASS":
        errors.append("predecessor_readback_not_pass")
    if predecessor_readback.get("record", {}).get("id") != PREDECESSOR_RECORD:
        errors.append("predecessor_readback_record")
    if len(predecessor_readback.get("files", [])) != 54:
        errors.append("predecessor_readback_files")
    if package_validation.get("status") != "PASS":
        errors.append("package_validation_not_pass")
    if len(package_rows) != 5:
        errors.append(f"package_manifest_rows:{len(package_rows)}")

    readback_by_name = {
        row["name"]: row for row in predecessor_readback.get("files", [])
    }
    for row in predecessor_rows:
        remote = readback_by_name.get(row["filename"])
        if remote is None:
            errors.append(f"predecessor_readback_missing:{row['filename']}")
            continue
        if (
            int(row["bytes"]) != int(remote["bytes"])
            or row["sha256"] != remote["sha256"]
        ):
            errors.append(f"predecessor_identity:{row['filename']}")

    package_by_name = {row["relative_path"]: row for row in package_rows}
    for source_name in SOURCE_TO_RELEASE:
        source = args.package_root / source_name
        row = package_by_name.get(source_name)
        if row is None:
            errors.append(f"package_manifest_missing:{source_name}")
            continue
        actual = identity(source)
        if int(row["bytes"]) != actual["bytes"] or row["sha256"] != actual["sha256"]:
            errors.append(f"package_identity:{source_name}")

    if errors:
        raise SystemExit(json.dumps({"status": "FAIL", "errors": errors}, indent=2))

    args.output_root.mkdir(parents=True, exist_ok=True)
    for child in args.output_root.iterdir():
        if child.is_file():
            child.unlink()
        elif child.is_dir():
            shutil.rmtree(child)

    for source_name, release_name in SOURCE_TO_RELEASE.items():
        shutil.copyfile(args.package_root / source_name, args.output_root / release_name)

    readme_path = args.output_root / "09_README_CURRENT_RELEASE.md"
    readme_path.write_text(build_readme(), encoding="utf-8", newline="\n")

    excluded_predecessor_rows = OLD_SGA3_VI_FILES | {"09_README_CURRENT_RELEASE.md"}
    retained = [
        row for row in predecessor_rows
        if row["filename"] not in excluded_predecessor_rows
    ]
    if len(retained) != 48:
        raise SystemExit(f"Expected 48 retained rows, found {len(retained)}")

    def new_row(filename: str, role: str, provenance: str, status: str) -> dict[str, object]:
        current = identity(args.output_root / filename)
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
            "00c4_SGA3_English_Expose_VI_Native_ReferenceV2_R4_20260724.pdf",
            "english_reader",
            (
                "complete SGA3 Expose VI A+B native-diagram/reference-v2 "
                f"working reader; exact GitHub package commit {GITHUB_COMMIT}"
            ),
            "bounded_working_reader_sga3_incomplete_native_diagrams_complete",
        ),
        new_row(
            "02c4_SGA3_English_Expose_VI_Native_ReferenceV2_R4_Master_20260724.tex",
            "english_master_tex",
            "primary editable master for complete SGA3 Expose VI A+B",
            "bounded_working_source_sga3_incomplete_native_diagrams_complete",
        ),
        new_row(
            "09_README_CURRENT_RELEASE.md",
            "manifest_status",
            (
                "current compact same-concept release note replacing bounded "
                "VI-A Loop-1 with complete Expose VI native freeze4"
            ),
            "current_release_control",
        ),
        new_row(
            "10c4_SGA3_English_Expose_VI_Native_ReferenceV2_R4_Source_Evidence_20260724.zip",
            "grouped_source_and_evidence",
            (
                "133-member privacy-clean source, native-diagram, reference, "
                "build, review, provenance, rights, and identity archive"
            ),
            "bounded_working_package_sga3_incomplete_native_diagrams_complete",
        ),
    ]
    final_rows = sorted(retained + new_rows, key=lambda row: row["filename"])
    if len(final_rows) != 52:
        raise SystemExit(f"Expected 52 content rows, found {len(final_rows)}")
    if not formula_safe(final_rows):
        raise SystemExit("Formula-unsafe manifest value")

    manifest_path = args.output_root / "09a_RELEASE_FILE_MANIFEST.csv"
    write_csv(manifest_path, final_rows)
    manifest_id = identity(manifest_path)

    zip_name = (
        "10c4_SGA3_English_Expose_VI_Native_ReferenceV2_R4_"
        "Source_Evidence_20260724.zip"
    )
    zip_path = args.output_root / zip_name
    member_rows: list[tuple[str, int, str]] = []
    with zipfile.ZipFile(zip_path) as archive:
        infos = [info for info in archive.infolist() if not info.is_dir()]
        unsafe = [
            info.filename for info in infos
            if info.filename.startswith(("/", "\\"))
            or (len(info.filename) >= 2 and info.filename[1] == ":")
            or ".." in Path(info.filename.replace("\\", "/")).parts
        ]
        for info in sorted(infos, key=lambda item: item.filename):
            member_rows.append(
                (
                    info.filename,
                    info.file_size,
                    sha256_bytes(archive.read(info)),
                )
            )
    zip_uncompressed = sum(row[1] for row in member_rows)
    zip_aggregate = sha256_bytes(
        "".join(
            f"{name}\t{size}\t{digest}\n"
            for name, size, digest in member_rows
        ).encode("utf-8")
    )
    if (
        len(member_rows) != 133
        or zip_uncompressed != 25_834_446
        or zip_aggregate != "024E8E5FC5BF8681CCE73028582C9043A2956391669B0267DA3A05A5A12C49D2"
        or unsafe
    ):
        raise SystemExit(
            json.dumps(
                {
                    "zip_members": len(member_rows),
                    "zip_uncompressed_bytes": zip_uncompressed,
                    "zip_aggregate": zip_aggregate,
                    "unsafe_entries": unsafe,
                },
                indent=2,
            )
        )

    validation = {
        "status": "PASS",
        "errors": [],
        "concept_doi": CONCEPT_DOI,
        "predecessor_record": PREDECESSOR_RECORD,
        "predecessor_doi": PREDECESSOR_DOI,
        "reserved_successor_record": args.successor_record,
        "same_concept_only": True,
        "duplicate_concept_authorized": False,
        "retained_predecessor_files": 48,
        "replaced_files": sorted(OLD_SGA3_VI_FILES | CONTROL_NAMES),
        "new_sga3_expose_vi_files": sorted(SOURCE_TO_RELEASE.values()),
        "content_manifest_rows": 52,
        "release_manifest_file": manifest_path.name,
        "release_manifest_bytes": manifest_id["bytes"],
        "release_manifest_sha256": manifest_id["sha256"],
        "final_upload_file_count": 54,
        "final_upload_bytes": 0,
        "default_preview": DEFAULT_PREVIEW,
        "github": {
            "commit": GITHUB_COMMIT,
            "package": GITHUB_PACKAGE,
            "outer_files": 6,
            "zip_members": 133,
            "readback_files": 6,
            "readback_zip_members": 133,
            "readback_errors": [],
        },
        "sga3_expose_vi": {
            "scope": "complete SGA3 Expose VI-A and VI-B",
            "sga3_complete": False,
            "excluded_scope": "Exposes VII-XXVI",
            "reader_pages": 185,
            "reader_sha256": (
                "4891908E423F933B36E61295BDC0CC77948B60B64B727F6B3592AB73332CC5CF"
            ),
            "editable_tex_files": 91,
            "native_diagrams": 58,
            "active_raster_image_inclusions": 0,
            "reference_targets": 987,
            "reference_edges": 672,
            "reference_candidates": 7629,
            "positive_residuals": 6957,
            "pdf_named_destinations": 1224,
            "pdf_goto_actions": 948,
            "visual_qa_pages": 185,
            "source_archive_members": 133,
            "source_archive_uncompressed_bytes": zip_uncompressed,
            "source_archive_member_aggregate": zip_aggregate,
        },
        "zip_archive_count": 29,
        "zip_member_count": 3304,
        "zip_uncompressed_bytes": 346_614_809,
        "rights": {
            "new_license_grant": False,
            "rights_clearance_claimed": False,
            "authority_pdfs_redistributed": False,
            "ocr_redistributed": False,
            "underlying_french_rights_retained": True,
            "polo_gille_rights_retained": True,
            "reinhold_comparison_lineage_attributed": True,
        },
        "contributors": [
            "OpenAI Codex / ChatGPT",
            "Anthropic Claude",
        ],
        "privacy_hits": [],
    }

    validation_path = args.output_root / "09b_RELEASE_VALIDATION.json"
    content_bytes = sum(int(row["bytes"]) for row in final_rows) + int(
        manifest_id["bytes"]
    )
    encoded = b""
    for _ in range(10):
        encoded = (json.dumps(validation, indent=2) + "\n").encode("utf-8")
        total = content_bytes + len(encoded)
        if validation["final_upload_bytes"] == total:
            break
        validation["final_upload_bytes"] = total
    validation_path.write_bytes(encoded)

    staged = sorted(path for path in args.output_root.iterdir() if path.is_file())
    if len(staged) != 6:
        raise SystemExit(f"Expected 6 staging files, found {len(staged)}")
    final_bytes = content_bytes + validation_path.stat().st_size
    if final_bytes != validation["final_upload_bytes"]:
        raise SystemExit("Final upload byte count mismatch")

    print(
        json.dumps(
            {
                "status": "PASS",
                "staging_files": len(staged),
                "staging_bytes": sum(path.stat().st_size for path in staged),
                "retained_files": len(retained),
                "final_zenodo_files": 54,
                "final_zenodo_bytes": final_bytes,
                "manifest_rows": len(final_rows),
                "manifest_sha256": identity(manifest_path)["sha256"],
                "validation_sha256": identity(validation_path)["sha256"],
                "zip_members": len(member_rows),
                "zip_uncompressed_bytes": zip_uncompressed,
                "zip_member_aggregate": zip_aggregate,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()

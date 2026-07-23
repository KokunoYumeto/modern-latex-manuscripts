#!/usr/bin/env python3
"""Build same-concept Zenodo controls for the bounded SGA3 Expose VI-A release."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import zipfile
from pathlib import Path


CONCEPT_DOI = "10.5281/zenodo.20410947"
PREDECESSOR_RECORD = 21512567
PREDECESSOR_DOI = "10.5281/zenodo.21512567"
GITHUB_COMMIT = "85288dbe082dbd6938bb16ffb2930b5a29c50e21"
GITHUB_PACKAGE = "sources/sga/sga3-english-expose-via-loop1-working-20260723"

SOURCE_TO_RELEASE = {
    "SGA3_English_Expose_VIA_Loop1_Working_20260723.pdf":
        "00c4_SGA3_English_Expose_VIA_Loop1_Working_20260723.pdf",
    "SGA3_English_Expose_VIA_Loop1_Working_20260723.tex":
        "02c4_SGA3_English_Expose_VIA_Loop1_Working_Master_20260723.tex",
    "SGA3_English_Expose_VIA_Loop1_Working_Source_Evidence_20260723.zip":
        "10c4_SGA3_English_Expose_VIA_Loop1_Working_Source_Evidence_20260723.zip",
}

CONTROL_NAMES = {
    "09_README_CURRENT_RELEASE.md",
    "09a_RELEASE_FILE_MANIFEST.csv",
    "09b_RELEASE_VALIDATION.json",
}


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
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\r\n")
        writer.writeheader()
        writer.writerows(rows)


def formula_safe(rows: list[dict[str, object]]) -> bool:
    return all(
        not str(value).startswith(("=", "+", "-", "@"))
        for row in rows
        for value in row.values()
    )


def build_readme() -> str:
    return """# Current SGA compact release

This same-concept successor adds the bounded SGA 3 Expose VI-A English
Loop-1 working reader, editable master, and grouped source/evidence archive.
It preserves every predecessor version and every unrelated file immutably.

## Reader-first order

1. English SGA 1 complete-volume working reader. Its clickable-reference
   infrastructure is substantial but not exhaustively convention-v2
   certified.
2. English SGA 2 complete archive-curated reference-linked R8 reader.
3. English SGA 3 cumulative working reader through complete Expose IV,
   followed by the complete standalone Expose V Loop-2 reader and the
   bounded Expose VI-A Loop-1 reader added here.
4. English SGA 4 proper certified reference-v2 r7 reader, covering Exposes
   I-XIX including V bis and excluding SGA 4half.
5. English SGA 5 reference-linked R9 reader.
6. English SGA 6 complete layered terminal reference-linked reader.

Available French workpasses and primary editable TeX follow the English
readers. Recursive source, machine-readable ledgers, QA, bounded checkpoints,
and predecessor material remain grouped into coherent ZIP archives.

## SGA 3 Expose VI-A

The new 45-page reader covers all of Expose VI-A through its bibliography.
Its editable body is pinned to 26 component TeX files and uses 23
source-derived Loop-1 diagram assets. The PDF has 248 named destinations,
112 valid internal GoTo actions, 23 image objects, and 16 embedded, subset,
Unicode-mapped font resources. Two isolated three-pass XeLaTeX builds were
byte-identical, and all 45 rendered pages passed direct visual review.

The grouped ZIP contains 60 exact members: the pinned component sources,
required diagram assets, sanitized build and source-review evidence,
provenance and rights notices, font evidence, and recursive SHA-256 controls.
GitHub and Zenodo publish the same outer PDF, TeX, and ZIP bytes.

This is bounded progress, not complete SGA 3. Expose VI-B and Exposes
VII-XXVI are excluded. Native-diagram Loop-2 work and exhaustive
convention-v2 reference certification remain open for VI-A.

## Authority, attribution, and rights

The current Polo-Gille Expose VI-A PDF is the controlling prose, formula,
page, and diagram witness. OCR is locator and drafting material only.
Jacob C. Reinhold's `jcreinhold/sga` snapshot
`e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e` is credited comparison and
drafting lineage, not authority. Reinhold states that his translation
contribution is CC BY 4.0; that statement does not license the underlying
French work, source-derived diagram pixels, or unrelated contributions.

No new blanket license or rights clearance is asserted. Rights in the
underlying French work, Polo-Gille re-edition, and diagram pixels remain with
their holders. Machine-assisted contributors include OpenAI Codex / ChatGPT
and Anthropic Claude under human direction.

These are modern working editions and translations, not critical editions,
mathematical certifications, independent human peer review, blanket rights
determinations, or accessibility certifications.

The SGA 1 working reader remains the initial preview.

Existing concept DOI: 10.5281/zenodo.20410947.
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--predecessor-manifest", type=Path, required=True)
    parser.add_argument("--predecessor-validation", type=Path, required=True)
    parser.add_argument("--package-root", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--successor-record", type=int)
    args = parser.parse_args()

    predecessor_rows = read_csv(args.predecessor_manifest)
    predecessor_validation = json.loads(
        args.predecessor_validation.read_text(encoding="utf-8-sig")
    )
    package_rows = read_csv(args.package_root / "SHA256SUMS.csv")

    errors: list[str] = []
    if len(predecessor_rows) != 34:
        errors.append(f"predecessor_manifest_rows:{len(predecessor_rows)}")
    if predecessor_validation.get("status") != "PASS":
        errors.append("predecessor_validation_not_pass")
    if len(package_rows) != 5:
        errors.append(f"package_manifest_rows:{len(package_rows)}")

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

    retained = [
        row for row in predecessor_rows
        if row["filename"] not in CONTROL_NAMES
    ]
    if len(retained) != 33:
        raise SystemExit(f"Expected 33 retained content rows, found {len(retained)}")

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
            "00c4_SGA3_English_Expose_VIA_Loop1_Working_20260723.pdf",
            "english_reader",
            (
                "bounded SGA3 Expose VI-A English Loop-1 working reader; "
                f"exact GitHub package commit {GITHUB_COMMIT}"
            ),
            "bounded_working_reader_sga3_incomplete_expose_via",
        ),
        new_row(
            "02c4_SGA3_English_Expose_VIA_Loop1_Working_Master_20260723.tex",
            "english_master_tex",
            "publication-facing editable master for bounded SGA3 Expose VI-A",
            "bounded_working_source_sga3_incomplete_expose_via",
        ),
        new_row(
            "09_README_CURRENT_RELEASE.md",
            "release_control",
            "current compact same-concept release note adding bounded SGA3 Expose VI-A",
            "current_release_control",
        ),
        new_row(
            "10c4_SGA3_English_Expose_VIA_Loop1_Working_Source_Evidence_20260723.zip",
            "grouped_source_and_evidence",
            (
                "60-member exact source/evidence archive with 26 pinned components, "
                "23 required Loop-1 diagram assets, sanitized evidence, rights notice, "
                "and recursive SHA-256 controls"
            ),
            "bounded_working_package_sga3_incomplete_expose_via",
        ),
    ]
    final_rows = sorted(retained + new_rows, key=lambda row: row["filename"])
    if len(final_rows) != 37:
        raise SystemExit(f"Expected 37 content rows, found {len(final_rows)}")
    if not formula_safe(final_rows):
        raise SystemExit("Formula-unsafe manifest value")

    manifest_path = args.output_root / "09a_RELEASE_FILE_MANIFEST.csv"
    write_csv(manifest_path, final_rows)
    manifest_id = identity(manifest_path)

    zip_name = "10c4_SGA3_English_Expose_VIA_Loop1_Working_Source_Evidence_20260723.zip"
    zip_path = args.output_root / zip_name
    with zipfile.ZipFile(zip_path) as archive:
        names = [info.filename for info in archive.infolist() if not info.is_dir()]
        unsafe = [
            name for name in names
            if name.startswith(("/", "\\"))
            or (len(name) >= 2 and name[1] == ":")
            or ".." in Path(name.replace("\\", "/")).parts
        ]
        zip_uncompressed = sum(
            info.file_size for info in archive.infolist() if not info.is_dir()
        )
    if len(names) != 60 or unsafe:
        raise SystemExit(
            json.dumps(
                {"zip_members": len(names), "unsafe_entries": unsafe},
                indent=2,
            )
        )

    zip_archives = dict(predecessor_validation["zip_archives"])
    zip_archives[zip_name] = {
        "file_members": 60,
        "all_entries": 60,
        "uncompressed_bytes": zip_uncompressed,
    }

    validation = {
        "status": "PASS",
        "errors": [],
        "concept_doi": CONCEPT_DOI,
        "predecessor_record": PREDECESSOR_RECORD,
        "predecessor_doi": PREDECESSOR_DOI,
        "reserved_successor_record": args.successor_record,
        "same_concept_only": True,
        "duplicate_concept_authorized": False,
        "retained_predecessor_files": 33,
        "replaced_files": sorted(CONTROL_NAMES),
        "new_sga3_via_files": sorted(SOURCE_TO_RELEASE.values()),
        "content_manifest_rows": 37,
        "release_manifest_file": manifest_path.name,
        "release_manifest_bytes": manifest_id["bytes"],
        "release_manifest_sha256": manifest_id["sha256"],
        "final_upload_file_count": 39,
        "final_upload_bytes": 0,
        "default_preview": (
            "00a_SGA1_English_CompleteVolume_Working_"
            "NoExhaustiveCertification_20260722.pdf"
        ),
        "github": {
            "commit": GITHUB_COMMIT,
            "package": GITHUB_PACKAGE,
            "outer_files": 6,
            "zip_members": 60,
            "readback_errors": [],
        },
        "sga3_expose_via": {
            "scope": "complete SGA3 Expose VI-A through bibliography",
            "sga3_complete": False,
            "excluded_scope": "Expose VI-B and Exposes VII-XXVI",
            "reader_pages": 45,
            "reader_sha256": (
                "2AF40B568061CA07489B592B0783D6332FFC885ED7128B115F3B1D0EA9A46C8C"
            ),
            "component_tex_files": 26,
            "loop1_diagram_assets": 23,
            "pdf_image_objects": 23,
            "pdf_named_destinations": 248,
            "pdf_goto_actions": 112,
            "fonts_embedded_subset_unicode": 16,
            "isolated_build_byte_identical": True,
            "visual_qa_pages": 45,
            "native_diagram_loop2_complete": False,
            "exhaustive_reference_certified": False,
        },
        "rights": {
            "new_license_grant": False,
            "rights_clearance_claimed": False,
            "underlying_french_rights_retained": True,
            "polo_gille_rights_retained": True,
            "diagram_pixel_rights_retained": True,
            "reinhold_comparison_lineage_attributed": True,
        },
        "zip_archives": zip_archives,
        "zip_archive_count": len(zip_archives),
        "zip_member_count": int(predecessor_validation["zip_member_count"]) + 60,
        "zip_uncompressed_bytes": (
            int(predecessor_validation["zip_uncompressed_bytes"]) + zip_uncompressed
        ),
        "contributors": [
            "OpenAI Codex / ChatGPT",
            "Anthropic Claude",
        ],
        "privacy_hits": [],
    }

    validation_path = args.output_root / "09b_RELEASE_VALIDATION.json"
    content_bytes = sum(int(row["bytes"]) for row in final_rows) + int(manifest_id["bytes"])
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
                "final_zenodo_files": 39,
                "final_zenodo_bytes": final_bytes,
                "manifest_rows": len(final_rows),
                "manifest_sha256": identity(manifest_path)["sha256"],
                "validation_sha256": identity(validation_path)["sha256"],
                "zip_members": len(names),
                "zip_uncompressed_bytes": zip_uncompressed,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()

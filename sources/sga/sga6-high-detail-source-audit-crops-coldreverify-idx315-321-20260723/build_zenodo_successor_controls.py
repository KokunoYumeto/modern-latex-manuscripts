#!/usr/bin/env python3
"""Build exact same-concept Zenodo controls for the idx315-321 crop increment."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import urllib.request
from pathlib import Path


CONCEPT_DOI = "10.5281/zenodo.20410947"
CONTROL_NAMES = {
    "09_README_CURRENT_RELEASE.md",
    "09a_RELEASE_FILE_MANIFEST.csv",
    "09b_RELEASE_VALIDATION.json",
}
PARENT_SHA256 = (
    "73FBBAD41340C12ECCDCFCF6C3A1656953FE3D712AA8E391678458CCD17B4BAA"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--predecessor-record", type=int, required=True)
    parser.add_argument("--successor-record", type=int, required=True)
    parser.add_argument("--predecessor-readback", type=Path, required=True)
    parser.add_argument("--crop-upload-manifest", type=Path, required=True)
    parser.add_argument("--crop-validation", type=Path, required=True)
    parser.add_argument("--zip-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--github-commit", required=True)
    return parser.parse_args()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def write_text(path: Path, text: str) -> None:
    path.write_bytes(text.encode("utf-8"))


def main() -> int:
    args = parse_args()
    output_dir = args.output_dir.resolve()
    zip_dir = args.zip_dir.resolve()
    if len(args.github_commit) != 40 or any(
        character not in "0123456789abcdef" for character in args.github_commit
    ):
        raise RuntimeError("GitHub commit must be a 40-character lowercase SHA-1")
    if args.predecessor_record == args.successor_record:
        raise RuntimeError("successor must differ from predecessor")
    output_dir.mkdir(parents=True, exist_ok=True)

    predecessor = json.loads(args.predecessor_readback.read_text(encoding="utf-8"))
    if predecessor["record"] != args.predecessor_record:
        raise RuntimeError("unexpected predecessor record")
    if predecessor["conceptdoi"] != CONCEPT_DOI:
        raise RuntimeError("unexpected predecessor concept")
    predecessor_files = predecessor["files"]

    manifest_url = (
        f"https://zenodo.org/api/records/{args.predecessor_record}/files/"
        "09a_RELEASE_FILE_MANIFEST.csv/content"
    )
    with urllib.request.urlopen(manifest_url, timeout=60) as response:
        prior_manifest_bytes = response.read()
    prior_rows = list(
        csv.DictReader(io.StringIO(prior_manifest_bytes.decode("utf-8-sig")))
    )
    retained_rows = [
        row for row in prior_rows if row["filename"] not in CONTROL_NAMES
    ]
    expected_retained = set(predecessor_files) - CONTROL_NAMES
    retained_names = {row["filename"] for row in retained_rows}
    if retained_names != expected_retained:
        raise RuntimeError(
            "predecessor retained-set mismatch: "
            f"missing={sorted(expected_retained - retained_names)} "
            f"extra={sorted(retained_names - expected_retained)}"
        )
    for row in retained_rows:
        identity = predecessor_files[row["filename"]]
        if (int(row["bytes"]), row["sha256"]) != (
            int(identity["bytes"]),
            identity["sha256"],
        ):
            raise RuntimeError(f"predecessor identity mismatch: {row['filename']}")

    crop_rows = list(
        csv.DictReader(
            args.crop_upload_manifest.open("r", encoding="utf-8", newline="")
        )
    )
    if len(crop_rows) != 2:
        raise RuntimeError("expected exactly two compact crop archives")
    crop_validation = json.loads(args.crop_validation.read_text(encoding="utf-8"))
    if crop_validation["status"] != "PASS" or crop_validation["errors"] != []:
        raise RuntimeError("crop validation is not a clean PASS")
    for row in crop_rows:
        path = zip_dir / row["filename"]
        if not path.is_file():
            raise RuntimeError(f"missing crop archive: {path}")
        if (path.stat().st_size, sha256(path)) != (
            int(row["bytes"]),
            row["sha256"],
        ):
            raise RuntimeError(f"crop archive identity mismatch: {path.name}")

    readme = f"""# Current compact SGA release

This same-concept successor preserves the existing reader-first SGA surface and
adds the next compact SGA6 source-audit crop increment. All 39 non-control files
from predecessor record {args.predecessor_record} remain byte-identical.

## Reader-first order

1. English SGA1 complete-volume working reader. Its clickable-reference
   infrastructure is substantial but not exhaustively convention-v2 certified.
2. English SGA2 complete archive-curated reference-linked R8 reader.
3. English SGA3 cumulative working reader through complete Expose IV, followed
   by standalone native-diagram Expose V and bounded Loop-1 Expose VI-A.
4. English SGA4 proper certified reference-v2 r7 reader, covering Exposes I-XIX
   including V bis and excluding SGA4half.
5. English SGA5 reference-linked R9 reader.
6. English SGA6 complete layered terminal reference-linked reader.

French workpasses and primary editable TeX follow the English readers.
Recursive sources, machine-readable ledgers, QA, bounded checkpoints,
predecessors, and visual evidence remain grouped into coherent ZIP archives.
SGA1 remains the default preview.

## SGA6 high-detail source-audit visual evidence

Three image archives now preserve 1,934 targeted formula, glyph, punctuation,
diagram, and prose-detail crops actually used during the active SGA6 source
audit. Two metadata archives preserve parent identity, page/crop provenance,
exact manifests, and 1,733 routine whole-page or page-band derivatives as
`rights_blocked_not_public`; those routine pixels are not redistributed.

This incremental release adds four explicit symbol-level crops from parent PDF
indices 317 and 321 and provenance for all associated audit images from indices
315 through 321. The temporal snapshot closes after cold reverification reached
index 321 and before index 322 began. Earlier targeted archives also contain
crops from prior same-parent audit phases, so no continuous index-coverage claim
is made.

The parent is the 720-page reader *Theorie des intersections et theoreme de
Riemann-Roch*, 26,833,956 bytes, SHA-256 `{PARENT_SHA256}`; the parent PDF is
not duplicated in these archives.

## Claims and rights

The crops are visual and provenance evidence, not certification of the French
transcription, English translation, mathematics, completeness, or
critical-edition status. Rights in the underlying French work and scan remain
with their holders. No blanket license or rights transfer is asserted.

The SGA readers remain modern working editions and translations, not uniform
whole-series source certification, critical editions, mathematical
certification, independent human peer review, blanket rights determinations,
or accessibility certification. SGA3 remains incomplete after Expose VI-A.

Existing concept DOI: {CONCEPT_DOI}.
"""
    readme_path = output_dir / "09_README_CURRENT_RELEASE.md"
    write_text(readme_path, readme)

    final_rows = retained_rows[:]
    final_rows.append(
        {
            "filename": readme_path.name,
            "bytes": str(readme_path.stat().st_size),
            "sha256": sha256(readme_path),
            "role": "manifest_status",
            "provenance": (
                "current compact same-concept release note; incremental SGA6 "
                f"crop package GitHub commit {args.github_commit}"
            ),
            "status": "current_release_control",
        }
    )
    for row in crop_rows:
        is_metadata = "RightsBlocked_Metadata" in row["filename"]
        final_rows.append(
            {
                "filename": row["filename"],
                "bytes": row["bytes"],
                "sha256": row["sha256"],
                "role": "source_audit_visual_evidence_archive",
                "provenance": (
                    "SGA6 incremental high-detail source-audit crop release; "
                    f"GitHub commit {args.github_commit}; parent scan SHA-256 "
                    f"{PARENT_SHA256}"
                ),
                "status": (
                    "provenance_and_rights_blocked_metadata"
                    if is_metadata
                    else "targeted_visual_evidence_no_license_grant"
                ),
            }
        )
    final_rows.sort(key=lambda row: row["filename"].lower())

    manifest_path = output_dir / "09a_RELEASE_FILE_MANIFEST.csv"
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "filename",
                "bytes",
                "sha256",
                "role",
                "provenance",
                "status",
            ],
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(final_rows)

    new_zip_results = crop_validation["zip_validation"]
    new_zip_members = sum(int(item["members"]) for item in new_zip_results.values())
    new_zip_uncompressed = sum(
        int(item["uncompressed_bytes"]) for item in new_zip_results.values()
    )
    validation_path = output_dir / "09b_RELEASE_VALIDATION.json"
    validation = {
        "status": "PASS",
        "errors": [],
        "concept_doi": CONCEPT_DOI,
        "predecessor_record": args.predecessor_record,
        "predecessor_doi": f"10.5281/zenodo.{args.predecessor_record}",
        "reserved_successor_record": args.successor_record,
        "same_concept_only": True,
        "duplicate_concept_authorized": False,
        "retained_predecessor_files": len(retained_rows),
        "replaced_files": sorted(CONTROL_NAMES),
        "new_sga6_crop_archives": [row["filename"] for row in crop_rows],
        "content_manifest_rows": len(final_rows),
        "release_manifest_file": manifest_path.name,
        "release_manifest_bytes": manifest_path.stat().st_size,
        "release_manifest_sha256": sha256(manifest_path),
        "final_upload_file_count": len(final_rows) + 2,
        "final_upload_bytes": 0,
        "default_preview": (
            "00a_SGA1_English_CompleteVolume_Working_"
            "NoExhaustiveCertification_20260722.pdf"
        ),
        "github": {
            "commit": args.github_commit,
            "package": (
                "sources/sga/sga6-high-detail-source-audit-crops-"
                "coldreverify-idx315-321-20260723"
            ),
            "metadata_files": 13,
            "readback_files": 13,
            "readback_errors": [],
        },
        "sga6_source_audit_crops": {
            "image_snapshot_start_after_utc": crop_validation[
                "image_snapshot_start_after_utc"
            ],
            "image_snapshot_cutoff_utc": crop_validation[
                "image_snapshot_cutoff_utc"
            ],
            "selected_images": crop_validation["source_selection"][
                "associated_parent_images"
            ],
            "explicit_targeted_images": crop_validation["source_selection"][
                "explicit_targeted"
            ]["files"],
            "recovered_named_targeted_images": crop_validation["source_selection"][
                "recovered_named_targeted"
            ]["files"],
            "rights_blocked_routine_page_derivatives": crop_validation[
                "source_selection"
            ]["routine_page_derivatives_rights_blocked"]["files"],
            "cumulative_targeted_images": 1934,
            "cumulative_rights_blocked_routine_page_derivatives": 1733,
            "new_zip_count": len(new_zip_results),
            "new_zip_members": new_zip_members,
            "new_zip_uncompressed_bytes": new_zip_uncompressed,
            "producer_validation_sha256": sha256(args.crop_validation),
            "freeze_race_errors": crop_validation["freeze_race_recheck"]["errors"],
        },
        "zip_archive_count": 19,
        "zip_member_count": 3127 + new_zip_members,
        "zip_uncompressed_bytes": 314233919 + new_zip_uncompressed,
        "rights": {
            "new_license_grant": False,
            "rights_clearance_claimed": False,
            "underlying_french_rights_retained": True,
            "parent_scan_rights_retained": True,
            "routine_page_pixels_withheld": True,
            "targeted_crop_claim_is_visual_provenance_only": True,
        },
        "contributors": ["OpenAI Codex / ChatGPT", "Anthropic Claude"],
        "privacy_hits": [],
    }

    for _ in range(10):
        write_text(
            validation_path,
            json.dumps(validation, indent=2, ensure_ascii=True) + "\n",
        )
        final_bytes = (
            sum(int(row["bytes"]) for row in final_rows)
            + manifest_path.stat().st_size
            + validation_path.stat().st_size
        )
        if validation["final_upload_bytes"] == final_bytes:
            break
        validation["final_upload_bytes"] = final_bytes
    else:
        raise RuntimeError("validation byte count did not converge")

    errors: list[str] = []
    for path in (readme_path, manifest_path, validation_path):
        text = path.read_text(encoding="utf-8").lower()
        for marker in (
            "c:\\users\\",
            "floris",
            "chatnotes",
            "source_thread_id",
            "thread_id",
            "@gmail.",
            "@outlook.",
        ):
            if marker in text:
                errors.append(f"privacy marker {marker!r} in {path.name}")
    with manifest_path.open("r", encoding="utf-8", newline="") as handle:
        for row_number, row in enumerate(csv.reader(handle), 1):
            for column_number, value in enumerate(row, 1):
                if row_number > 1 and value.startswith(("=", "+", "-", "@")):
                    errors.append(
                        f"formula trigger {manifest_path.name}:"
                        f"{row_number}:{column_number}"
                    )
    if errors:
        raise RuntimeError("; ".join(errors))

    print(
        json.dumps(
            {
                "status": "PASS",
                "files": {
                    path.name: {
                        "bytes": path.stat().st_size,
                        "sha256": sha256(path),
                    }
                    for path in (readme_path, manifest_path, validation_path)
                },
                "retained_predecessor_files": len(retained_rows),
                "new_crop_archives": len(crop_rows),
                "final_upload_file_count": validation["final_upload_file_count"],
                "new_zip_members": new_zip_members,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

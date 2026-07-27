#!/usr/bin/env python3
"""Build exact same-concept Zenodo controls for the SGA6 idx618-626 crop release."""

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
PACKAGE_PATH = (
    "sources/sga/"
    "sga6-ultradetail-source-audit-crops-coldreverify-idx618-626-20260727"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--predecessor-record", type=int, required=True)
    parser.add_argument("--prior-crop-record", type=int, required=True)
    parser.add_argument("--successor-record", type=int, required=True)
    parser.add_argument("--crop-upload-manifest", type=Path, required=True)
    parser.add_argument("--crop-validation", type=Path, required=True)
    parser.add_argument("--zip-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--github-commit", required=True)
    parser.add_argument("--github-metadata-files", type=int, required=True)
    return parser.parse_args()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def fetch_json(url: str) -> dict[str, object]:
    with urllib.request.urlopen(url, timeout=60) as response:
        return json.loads(response.read().decode("utf-8"))


def fetch_bytes(url: str) -> bytes:
    with urllib.request.urlopen(url, timeout=60) as response:
        return response.read()


def write_text(path: Path, text: str) -> None:
    path.write_bytes(text.encode("utf-8"))


def load_crop_bundle(
    manifest_path: Path,
    validation_path: Path,
    zip_dir: Path,
) -> tuple[list[dict[str, str]], dict[str, object]]:
    with manifest_path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 2:
        raise RuntimeError(f"expected two crop archives in {manifest_path}")

    validation = json.loads(validation_path.read_text(encoding="utf-8"))
    if validation["status"] != "PASS" or validation["errors"] != []:
        raise RuntimeError(f"crop validation is not a clean PASS: {validation_path}")

    for row in rows:
        path = zip_dir / row["filename"]
        expected = (int(row["bytes"]), row["sha256"])
        observed = (path.stat().st_size, sha256(path)) if path.is_file() else None
        if observed != expected:
            raise RuntimeError(
                f"crop archive identity mismatch: {path.name}: "
                f"expected={expected!r} observed={observed!r}"
            )
    return rows, validation


def fetch_release_validation(record: int) -> dict[str, object]:
    url = (
        f"https://zenodo.org/api/records/{record}/files/"
        "09b_RELEASE_VALIDATION.json/content"
    )
    validation = json.loads(fetch_bytes(url).decode("utf-8"))
    if validation["status"] != "PASS" or validation["errors"] != []:
        raise RuntimeError(f"record {record} validation is not a clean PASS")
    return validation


def main() -> int:
    args = parse_args()
    output_dir = args.output_dir.resolve()
    zip_dir = args.zip_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    if len(args.github_commit) != 40 or any(
        character not in "0123456789abcdef" for character in args.github_commit
    ):
        raise RuntimeError("GitHub commit must be a 40-character lowercase SHA-1")
    if args.predecessor_record == args.successor_record:
        raise RuntimeError("successor must differ from predecessor")
    if args.github_metadata_files < 1:
        raise RuntimeError("GitHub metadata file count must be positive")

    predecessor = fetch_json(
        f"https://zenodo.org/api/records/{args.predecessor_record}"
    )
    if int(predecessor["id"]) != args.predecessor_record:
        raise RuntimeError("unexpected predecessor record")
    if predecessor["conceptdoi"] != CONCEPT_DOI:
        raise RuntimeError("unexpected predecessor concept")
    if predecessor["status"] != "published":
        raise RuntimeError("predecessor is not published")

    predecessor_files = {
        item["key"]: {
            "bytes": int(item["size"]),
            "md5": str(item["checksum"]).removeprefix("md5:"),
        }
        for item in predecessor["files"]
    }
    if len(predecessor_files) < 1:
        raise RuntimeError("predecessor has no files")
    if not CONTROL_NAMES <= set(predecessor_files):
        raise RuntimeError("predecessor release controls are incomplete")

    manifest_url = (
        f"https://zenodo.org/api/records/{args.predecessor_record}/files/"
        "09a_RELEASE_FILE_MANIFEST.csv/content"
    )
    prior_rows = list(
        csv.DictReader(
            io.StringIO(fetch_bytes(manifest_url).decode("utf-8-sig"))
        )
    )
    prior_validation = fetch_release_validation(args.predecessor_record)
    prior_crop_validation = fetch_release_validation(args.prior_crop_record)

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
    if len(retained_rows) != len(predecessor_files) - len(CONTROL_NAMES):
        raise RuntimeError(
            "unexpected retained row count: "
            f"expected={len(predecessor_files) - len(CONTROL_NAMES)} "
            f"observed={len(retained_rows)}"
        )
    for row in retained_rows:
        identity = predecessor_files[row["filename"]]
        if int(row["bytes"]) != identity["bytes"]:
            raise RuntimeError(f"predecessor byte mismatch: {row['filename']}")

    crop_rows, crop_validation = load_crop_bundle(
        args.crop_upload_manifest,
        args.crop_validation,
        zip_dir,
    )
    if {row["filename"] for row in crop_rows} & set(predecessor_files):
        raise RuntimeError("new crop archive collides with predecessor filename")

    targeted_images = int(
        crop_validation["selection"][
            "targeted_public_images_opened_during_audit"
        ]
    )
    generated_unread = int(
        crop_validation["selection"][
            "generated_unread_tight_crops_metadata_only"
        ]
    )
    blocked_bands = int(crop_validation["selection"]["rights_blocked_page_bands"])
    prior_crop_summary = prior_crop_validation["sga6_source_audit_crops"]
    cumulative_targeted = (
        int(prior_crop_summary["cumulative_targeted_images"]) + targeted_images
    )
    cumulative_blocked = (
        int(prior_crop_summary["cumulative_rights_blocked_routine_page_derivatives"])
        + blocked_bands
    )

    readme = f"""# Current compact SGA release

This same-concept successor preserves the existing reader-first SGA surface and
adds one bounded SGA6 source-audit visual-evidence tranche. All
{len(retained_rows)} files outside the three release controls from predecessor
record {args.predecessor_record} remain byte-identical.

## Reader-first order

1. English SGA1 complete-volume working reader. Its clickable-reference
   infrastructure is substantial but not exhaustively convention-v2 certified.
2. English SGA2 complete archive-curated reference-linked R8 reader.
3. English SGA3 cumulative working reader through complete Expose IV, followed
   by standalone native-diagram Exposes V and VI and bounded complete Expose
   VIII, IX, and XI checkpoints. Expose VII, Expose X, and Exposes XII-XXVI
   remain absent.
4. English SGA4 proper certified reference-v2 r7 reader, covering Exposes I-XIX
   including V bis and excluding SGA4half.
5. English SGA5 reference-linked R9 reader.
6. English SGA6 complete layered terminal reference-linked reader.

French workpasses and primary editable TeX follow the English readers.
Recursive sources, machine-readable ledgers, QA, bounded checkpoints,
predecessors, and visual evidence remain grouped into coherent ZIP archives.
SGA1 remains the default preview.

## SGA6 ultra-detail source-audit visual evidence

This release adds {targeted_images} tight formula-, glyph-, prose-, locator-,
and diagram-junction crops actually opened during the current SGA6 cold source
re-verification. They come from parent indices 618-626 and map to the stable
9-entry audit boundary #1370-#1378. The tranche spans Expose XII Proposition
3.1 through Lemma 4.4 and the opening of its proof at idx626. Each public crop records
parent identity, source page, pixel bounding box, dimensions, scaling,
generator identity, linked audit entry, target context, and QA disposition.

The paired metadata archive records {blocked_bands} routine full-width page
bands from the same audit span as `rights_blocked_not_public`. Their hashes,
coordinates, dimensions, DPI, generator identities, and target links are
public, but their pixels are withheld. This avoids duplicating ordinary page
renders while preserving the provenance needed to locate and reproduce them.
It also records {generated_unread} tight alternatives that were generated but
never opened during the audit; those pixels are withheld rather than
misrepresented as reviewed evidence.

Across the current same-concept crop series, the release controls account for
{cumulative_targeted:,} targeted public images and {cumulative_blocked:,}
rights-blocked routine page derivatives. The present two archives contain
{sum(int(item['members']) for item in crop_validation['zip_validation'].values())}
exact members. All {targeted_images} selected target images replay
pixel-for-pixel and PNG-byte-for-PNG-byte and correlate to the viewer
attachments returned during the recorded source-audit `Read` events. Their
source-image hashes are disjoint from prior public crop hashes. The
{blocked_bands} routine bands retain exact source identities and PNG dimensions
without redundant public pixels.

The parent is the 720-page reader *Theorie des intersections et theoreme de
Riemann-Roch*, 26,833,956 bytes, SHA-256 `{PARENT_SHA256}`. The parent PDF,
{blocked_bands} routine page-band pixels, and {generated_unread}
generated-but-unread alternatives are not redistributed.

## SGA3 diagram release gate

Pending unpublished diagram-bearing SGA3 payloads remain subject to the
Claude-style high-zoom nonauthor cold-reverify control recorded on GitHub.
Expose VII remains held for 32 native-diagram repairs, 37 semantic target-kind
regressions, and six coordinate literals falsely detected as section
references. Expose XI passed the high-zoom diagram gate and is already public
as a sealed bounded checkpoint. Already published bounded SGA3 checkpoints
remain immutable working history and are improved only by additive successors.

## Claims and rights

These crops are visual and provenance evidence, not certification of the
French transcription, English translation, mathematics, completeness, or
critical-edition status. Rights in the underlying French work and scan remain
with their holders. No blanket license or rights transfer is asserted.

The SGA readers remain modern working editions and translations, not uniform
whole-series source certification, critical editions, mathematical
certification, independent human peer review, blanket rights determinations,
or accessibility certification.

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
                "current compact same-concept release note; SGA6 idx618-626 "
                f"ultra-detail crop GitHub commit {args.github_commit}"
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
                    "SGA6 idx618-626 ultra-detail source-audit crop tranche; "
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

    zip_results = crop_validation["zip_validation"]
    new_zip_members = sum(int(item["members"]) for item in zip_results.values())
    new_zip_uncompressed = sum(
        int(item["member_bytes"]) for item in zip_results.values()
    )
    prior_zip_file_members = int(
        prior_validation.get(
            "zip_file_member_count",
            prior_validation.get("zip_member_count", 0),
        )
    )
    prior_zip_directory_entries = int(
        prior_validation.get("zip_directory_entry_count", 0)
    )
    prior_zip_all_entries = int(
        prior_validation.get(
            "zip_all_entry_count",
            prior_zip_file_members + prior_zip_directory_entries,
        )
    )
    prior_compatibility_counter = int(
        prior_validation.get(
            "release_control_compatibility_counter",
            prior_zip_all_entries,
        )
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
            "package": PACKAGE_PATH,
            "metadata_files": args.github_metadata_files,
            "readback_files": args.github_metadata_files,
            "readback_errors": [],
        },
        "sga3_expose_ix": prior_validation.get("sga3_expose_ix"),
        "sga3_expose_viii": prior_validation.get("sga3_expose_viii"),
        "sga3_expose_xi": prior_validation.get("sga3_expose_xi"),
        "sga6_source_audit_crops": {
            "scope": "parent indices 618-626; audit entries 1370-1378",
            "expose_boundary": (
                "Expose XII Proposition 3.1 through Lemma 4.4 and opening "
                "of its proof at idx626; idx627 excluded"
            ),
            "targeted_public_images": targeted_images,
            "generated_unread_tight_crops_metadata_only": generated_unread,
            "rights_blocked_page_bands": blocked_bands,
            "cumulative_targeted_images": cumulative_targeted,
            "cumulative_rights_blocked_routine_page_derivatives": (
                cumulative_blocked
            ),
            "new_zip_count": len(zip_results),
            "new_zip_members": new_zip_members,
            "new_zip_uncompressed_bytes": new_zip_uncompressed,
            "producer_validation_sha256": sha256(args.crop_validation),
            "source_freeze_errors": crop_validation["source_freeze"]["race_errors"],
            "prior_target_hash_intersection": crop_validation[
                "prior_public_hash_check"
            ]["target_hash_intersection"],
            "source_replay_files": crop_validation["target_replay"]["files"],
            "source_replay_dimensions_exact": crop_validation["target_replay"][
                "dimensions_exact"
            ],
            "source_replay_pixel_exact": crop_validation["target_replay"][
                "pixel_exact"
            ],
            "source_replay_png_byte_exact": crop_validation["target_replay"][
                "png_byte_exact"
            ],
            "viewer_attachment_events": crop_validation[
                "viewer_attachment_validation"
            ]["attachment_events"],
            "viewer_attachment_correlations_pass": crop_validation[
                "viewer_attachment_validation"
            ]["attachment_correlations_pass"],
            "routine_source_identity_exact": crop_validation[
                "routine_band_validation"
            ]["source_identity_exact"],
            "routine_png_decode_and_dimensions_exact": crop_validation[
                "routine_band_validation"
            ]["png_decode_and_dimensions_exact"],
            "selected_audit_heading_aggregate_sha256": crop_validation[
                "authority"
            ]["selected_audit_heading_aggregate_sha256"],
        },
        "sga3_diagram_cold_reverify": {
            "control_sha256": (
                "8682D7E64EADF2E92F8015EF79BA337D3ADB062B232F296DEB6C4009360D10CB"
            ),
            "expose_vii_repair_hold_sha256": (
                "AA121D61219000E22A3AB46113F180A8A001FAE5B65FEE6566AC352725C5A7F6"
            ),
            "expose_vii_detector_hold_sha256": (
                "D984FEF9257BBC978DBB55127E1379A8F69328A50AF43CA9ABBF2A4BDBAB7705"
            ),
            "published_history_immutable": True,
            "expose_vii": (
                "held_for_32_diagram_repairs_37_target_kind_regressions_and_"
                "six_false_coordinate_literal_links"
            ),
            "expose_xi": (
                "high_zoom_gate_and_exact_package_audit_passed_published_in_"
                f"predecessor_record_{args.predecessor_record}"
            ),
        },
        "zip_archive_count": (
            int(prior_validation["zip_archive_count"]) + len(zip_results)
        ),
        "zip_member_count": prior_zip_file_members + new_zip_members,
        "zip_file_member_count": prior_zip_file_members + new_zip_members,
        "zip_directory_entry_count": prior_zip_directory_entries,
        "zip_all_entry_count": prior_zip_all_entries + new_zip_members,
        "release_control_compatibility_counter": (
            prior_compatibility_counter + new_zip_members
        ),
        "zip_uncompressed_bytes": (
            int(prior_validation["zip_uncompressed_bytes"])
            + new_zip_uncompressed
        ),
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
                "zip_archive_count": validation["zip_archive_count"],
                "zip_member_count": validation["zip_member_count"],
                "zip_uncompressed_bytes": validation["zip_uncompressed_bytes"],
                "cumulative_targeted_images": cumulative_targeted,
                "cumulative_rights_blocked_page_bands": cumulative_blocked,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Validate the reader-clean SGA 1, 2, 4, 5, and 6 successor."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from pathlib import Path

from pypdf import PdfReader


REPO_ROOT = Path(__file__).resolve().parent.parent
PACKAGE_ROOT = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga1-6-reader-clean-presentation-successor-20260728"
)
MANIFEST_NAME = "SHA256SUMS.csv"
VALIDATION_NAME = "PACKAGE_VALIDATION.json"

PDF_NAMES = {
    "SGA1": (
        "00a_SGA1_English_CompleteVolume_Working_"
        "NoExhaustiveCertification_20260722.pdf"
    ),
    "SGA2": "00b_SGA2_English_Complete_ReferenceLinked_R8_20260723.pdf",
    "SGA4": (
        "00d_SGA4_English_Proper_Exposes_I_XIX_including_Vbis_"
        "ReferenceV2_R7_20260723.pdf"
    ),
    "SGA5": "00e_SGA5_English_ReferenceLinked_R9_20260723.pdf",
    "SGA6": "00f_SGA6_English_Complete_ReferenceLinked_20260723.pdf",
}
TEX_NAMES = {
    "SGA1": "02a_SGA1_English_CompleteVolume_Working_Master_20260722.tex",
    "SGA2": (
        "02b_SGA2_English_Complete_ReferenceLinked_R8_Master_20260723.tex"
    ),
    "SGA4": (
        "02d_SGA4_English_Proper_Master_ReferenceV2_R7_20260723.tex"
    ),
    "SGA5": "02e_SGA5_English_ReferenceLinked_R9_Master_20260723.tex",
    "SGA6": (
        "02f_SGA6_English_Complete_ReferenceLinked_Master_20260723.tex"
    ),
}
PREDECESSOR_SHA256 = {
    "SGA1": "A83DFFB4D560EF8E0EB5B831F6363222A74C4B704ADB636D1D56FAC1435ACA2B",
    "SGA2": "8CC6403208C83FBA679E6A3E1D9D5DBD2A28DE9FF93A240697A8524230D1C2B2",
    "SGA4": "A4057C39E5BF54AD12E7B2E5DBBACA884B9738F376B3418E8D97EDAB4E3A88B2",
    "SGA5": "EF93294085E06FFCF1F95DD8D2DEBB14DAD22FED44D967E09D3BAB24F5C78F6E",
    "SGA6": "3CEE0FD4D50EB1D9B062637A05214B300F1F73EA7FA801CA92FE1B2E728C35D3",
}
EXPECTED_PAGES = {
    "SGA1": 261,
    "SGA2": 184,
    "SGA4": 864,
    "SGA5": 309,
    "SGA6": 377,
}
EXPECTED_PAGE_SIZE = {
    "SGA1": ("A4", 595.276, 841.890),
    "SGA2": ("A4", 595.276, 841.890),
    "SGA4": ("A4", 595.276, 841.890),
    "SGA5": ("US Letter", 612.0, 792.0),
    "SGA6": ("A4", 595.276, 841.890),
}
EXPECTED_COMPARISON = {
    "SGA1": {
        "old_pages": 262,
        "delta": 1,
        "matches": 256,
        "old_unmatched": [1, 2, 3, 4, 5, 212],
        "new_unmatched": [1, 2, 3, 4, 211],
    },
    "SGA2": {
        "old_pages": 184,
        "delta": 0,
        "matches": 183,
        "old_unmatched": [3],
        "new_unmatched": [3],
    },
    "SGA4": {
        "old_pages": 864,
        "delta": 0,
        "matches": 862,
        "old_unmatched": [1, 2],
        "new_unmatched": [1, 2],
    },
    "SGA5": {
        "old_pages": 309,
        "delta": 0,
        "matches": 309,
        "old_unmatched": [],
        "new_unmatched": [],
    },
    "SGA6": {
        "old_pages": 378,
        "delta": 1,
        "matches": 376,
        "old_unmatched": [1, 373],
        "new_unmatched": [372],
    },
}
DISALLOWED_PATTERNS = {
    "agent_name": re.compile(r"\b(?:Claude|Codex|ChatGPT|LLM)\b", re.I),
    "machine_assistance": re.compile(r"machine[- ]assisted", re.I),
    "source_status_note": re.compile(r"source and status note", re.I),
    "english_reader_note": re.compile(r"english-reader note", re.I),
    "source_rights_notice": re.compile(r"source and rights notice", re.I),
    "editorial_status": re.compile(r"editorial status", re.I),
    "working_state": re.compile(r"working[- ]state", re.I),
    "production_boundary": re.compile(r"production boundary", re.I),
    "source_notes_appendix": re.compile(r"source notes\.", re.I),
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def normalized_text(page) -> str:
    return re.sub(r"\s+", " ", page.extract_text() or "").strip()


def scan_text(text: str) -> list[str]:
    return [
        name for name, pattern in DISALLOWED_PATTERNS.items()
        if pattern.search(text)
    ]


def link_metrics(reader: PdfReader) -> dict[str, int]:
    goto = 0
    uri = 0
    invalid = 0
    for page in reader.pages:
        for annotation_ref in page.get("/Annots") or []:
            try:
                annotation = annotation_ref.get_object()
                if annotation.get("/Subtype") != "/Link":
                    continue
                action = annotation.get("/A")
                if action is not None:
                    action = action.get_object()
                    if (
                        action.get("/S") == "/GoTo"
                        and action.get("/D") is not None
                    ):
                        goto += 1
                    elif action.get("/S") == "/URI":
                        uri += 1
                    else:
                        invalid += 1
                elif annotation.get("/Dest") is not None:
                    goto += 1
                else:
                    invalid += 1
            except Exception:
                invalid += 1
    return {
        "internal_goto_actions": goto,
        "uri_actions": uri,
        "invalid_actions": invalid,
    }


def page_size_metrics(reader: PdfReader, volume: str) -> dict[str, object]:
    format_name, expected_width, expected_height = EXPECTED_PAGE_SIZE[volume]
    unexpected = []
    for page_number, page in enumerate(reader.pages, start=1):
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        if not (
            abs(width - expected_width) <= 1.0
            and abs(height - expected_height) <= 1.0
        ):
            unexpected.append(
                {
                    "page": page_number,
                    "width_points": width,
                    "height_points": height,
                }
            )
    return {
        "expected_page_format": format_name,
        "pages_with_expected_size": len(reader.pages) - len(unexpected),
        "unexpected_page_sizes": unexpected,
    }


def compare_pages(old: PdfReader, new: PdfReader) -> dict[str, object]:
    old_text = [normalized_text(page) for page in old.pages]
    new_text = [normalized_text(page) for page in new.pages]
    old_hashes = [
        hashlib.sha256(text.encode("utf-8")).hexdigest()
        for text in old_text
    ]
    new_hashes = [
        hashlib.sha256(text.encode("utf-8")).hexdigest()
        for text in new_text
    ]
    candidates = []
    for delta in range(-5, 6):
        matches = [
            (old_index, new_index)
            for new_index, digest in enumerate(new_hashes)
            for old_index in [new_index + delta]
            if 0 <= old_index < len(old_hashes)
            and digest == old_hashes[old_index]
        ]
        candidates.append((len(matches), delta, matches))
    match_count, delta, matches = max(candidates, key=lambda item: item[0])
    old_matched = {old_index for old_index, _ in matches}
    new_matched = {new_index for _, new_index in matches}
    return {
        "old_pages": len(old.pages),
        "new_pages": len(new.pages),
        "old_index_minus_new_index": delta,
        "exact_normalized_page_text_matches": match_count,
        "old_unmatched_pages": [
            index + 1
            for index in range(len(old.pages))
            if index not in old_matched
        ],
        "new_unmatched_pages": [
            index + 1
            for index in range(len(new.pages))
            if index not in new_matched
        ],
    }


def write_manifest() -> tuple[int, str]:
    paths = sorted(
        (
            path for path in PACKAGE_ROOT.iterdir()
            if path.is_file()
            and path.name not in {MANIFEST_NAME, VALIDATION_NAME}
        ),
        key=lambda path: path.name.casefold(),
    )
    manifest_path = PACKAGE_ROOT / MANIFEST_NAME
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=("filename", "bytes", "sha256", "role"),
            lineterminator="\n",
        )
        writer.writeheader()
        for path in paths:
            writer.writerow(
                {
                    "filename": path.name,
                    "bytes": path.stat().st_size,
                    "sha256": sha256_file(path),
                    "role": (
                        "reader_pdf"
                        if path.suffix.lower() == ".pdf"
                        else "direct_master_tex"
                        if path.suffix.lower() == ".tex"
                        else "release_note"
                    ),
                }
            )
    return len(paths), sha256_file(manifest_path)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--predecessor-dir",
        type=Path,
        required=True,
        help="Directory containing the five public record-21650398 PDFs",
    )
    parser.add_argument(
        "--visual-pass",
        action="store_true",
        help="Record that representative rendered pages were inspected",
    )
    args = parser.parse_args()

    errors: list[str] = []
    readers: dict[str, dict[str, object]] = {}
    comparisons: dict[str, dict[str, object]] = {}
    privacy_hits: list[dict[str, str]] = []

    for volume in PDF_NAMES:
        new_path = PACKAGE_ROOT / PDF_NAMES[volume]
        old_path = args.predecessor_dir / PDF_NAMES[volume]
        tex_path = PACKAGE_ROOT / TEX_NAMES[volume]
        if not new_path.is_file() or not old_path.is_file():
            errors.append(f"{volume}: missing reader or predecessor")
            continue
        if not tex_path.is_file():
            errors.append(f"{volume}: missing direct master TeX")
            continue
        old_sha = sha256_file(old_path)
        if old_sha != PREDECESSOR_SHA256[volume]:
            errors.append(f"{volume}: predecessor SHA-256 mismatch")

        new_reader = PdfReader(new_path)
        old_reader = PdfReader(old_path)
        text = "\n".join(normalized_text(page) for page in new_reader.pages)
        metadata = {
            str(key): str(value)
            for key, value in (new_reader.metadata or {}).items()
        }
        text_hits = scan_text(text)
        metadata_hits = scan_text("\n".join(metadata.values()))
        tex_hits = scan_text(tex_path.read_text(encoding="utf-8"))
        for surface, hits in (
            ("pdf_text", text_hits),
            ("pdf_metadata", metadata_hits),
            ("direct_master_tex", tex_hits),
        ):
            for hit in hits:
                privacy_hits.append(
                    {"volume": volume, "surface": surface, "pattern": hit}
                )

        metrics = {
            "filename": new_path.name,
            "bytes": new_path.stat().st_size,
            "sha256": sha256_file(new_path),
            "pages": len(new_reader.pages),
            "named_destinations": len(new_reader.named_destinations),
            **link_metrics(new_reader),
            **page_size_metrics(new_reader, volume),
            "metadata": metadata,
            "disallowed_pdf_text_hits": text_hits,
            "disallowed_pdf_metadata_hits": metadata_hits,
            "direct_master_tex": {
                "filename": tex_path.name,
                "bytes": tex_path.stat().st_size,
                "sha256": sha256_file(tex_path),
                "disallowed_hits": tex_hits,
            },
        }
        readers[volume] = metrics
        if metrics["pages"] != EXPECTED_PAGES[volume]:
            errors.append(f"{volume}: unexpected page count")
        if metrics["unexpected_page_sizes"]:
            errors.append(f"{volume}: unexpected page sizes")
        if metrics["invalid_actions"]:
            errors.append(f"{volume}: invalid PDF link actions")

        comparison = compare_pages(old_reader, new_reader)
        comparisons[volume] = comparison
        expected = EXPECTED_COMPARISON[volume]
        observed = {
            "old_pages": comparison["old_pages"],
            "delta": comparison["old_index_minus_new_index"],
            "matches": comparison["exact_normalized_page_text_matches"],
            "old_unmatched": comparison["old_unmatched_pages"],
            "new_unmatched": comparison["new_unmatched_pages"],
        }
        if observed != expected:
            errors.append(f"{volume}: predecessor text comparison mismatch")

    if privacy_hits:
        errors.append("reader-facing process/status phrase scan is nonzero")
    if not args.visual_pass:
        errors.append("representative rendered-page inspection not recorded")

    manifest_rows, manifest_sha = write_manifest()
    validation = {
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "purpose": (
            "reader-facing AI/process/status cleanup with mathematical "
            "body and link preservation"
        ),
        "concept_doi": "10.5281/zenodo.20410947",
        "predecessor_record": 21650398,
        "replacement_policy": (
            "replace five existing PDF names and five existing direct "
            "master-TeX names in one same-concept successor"
        ),
        "readers": readers,
        "predecessor_text_comparisons": comparisons,
        "reader_facing_process_or_status_hits": privacy_hits,
        "representative_render_inspection": {
            "status": "PASS" if args.visual_pass else "NOT_RECORDED",
            "pages": "first three and final page of each cleaned reader",
        },
        "manifest": {
            "filename": MANIFEST_NAME,
            "rows": manifest_rows,
            "sha256": manifest_sha,
            "self_excluded": True,
            "validation_excluded": True,
        },
        "critical_edition_claimed": False,
        "new_license_grant": False,
    }
    validation_path = PACKAGE_ROOT / VALIDATION_NAME
    validation_path.write_text(
        json.dumps(validation, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(validation, ensure_ascii=True, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

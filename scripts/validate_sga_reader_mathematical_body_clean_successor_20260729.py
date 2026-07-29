#!/usr/bin/env python3
"""Validate the reader-only SGA PDF replacements and public package."""

from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

from pypdf import PdfReader


REPO_ROOT = Path(__file__).resolve().parents[1]
PACKAGE_ROOT = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga1-6-reader-mathematical-body-clean-successor-20260729"
)
PREDECESSOR_ROOT = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga1-6-reader-clean-presentation-successor-20260728"
)
SGA3_PREDECESSOR_ROOT = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga3-english-complete-working-reader-clean-r18-native-expose-i-20260729"
)

PDFS = {
    "SGA1": (
        "00a_SGA1_English_CompleteVolume_Working_NoExhaustiveCertification_20260722.pdf",
        PREDECESSOR_ROOT,
    ),
    "SGA2": (
        "00b_SGA2_English_Complete_ReferenceLinked_R8_20260723.pdf",
        PREDECESSOR_ROOT,
    ),
    "SGA3": (
        "00c00_SGA3_English_Complete_Reader_Native_Update_R18_20260729.pdf",
        SGA3_PREDECESSOR_ROOT,
    ),
    "SGA5": (
        "00e_SGA5_English_ReferenceLinked_R9_20260723.pdf",
        PREDECESSOR_ROOT,
    ),
}

PRIVATE_OR_PROCESS_PATTERNS = (
    re.compile(rb"C:[\\/]+Users[\\/]+Floris", re.IGNORECASE),
    re.compile(rb"C:[\\/]+w[\\/]+s613", re.IGNORECASE),
    re.compile(rb"\.codex", re.IGNORECASE),
    re.compile(rb"\bChatGPT\b", re.IGNORECASE),
    re.compile(rb"\bOpenAI\b", re.IGNORECASE),
    re.compile(rb"\bClaude\b", re.IGNORECASE),
    re.compile(rb"\bCodex\b", re.IGNORECASE),
    re.compile(rb"\bAI[- ](?:generated|assisted)\b", re.IGNORECASE),
    re.compile(rb"\bLLM[- ]generated\b", re.IGNORECASE),
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def inspect_pdf(path: Path) -> dict[str, object]:
    reader = PdfReader(str(path), strict=False)
    destinations = reader.named_destinations
    invalid_named_destinations: list[str] = []
    for name, destination in destinations.items():
        try:
            page_number = reader.get_destination_page_number(destination)
        except Exception:
            page_number = -1
        if page_number < 0 or page_number >= len(reader.pages):
            invalid_named_destinations.append(name)

    link_actions: Counter[str] = Counter()
    invalid_goto_destinations: list[str] = []
    page_sizes: Counter[str] = Counter()
    for page_number, page in enumerate(reader.pages, start=1):
        width = round(float(page.mediabox.width), 2)
        height = round(float(page.mediabox.height), 2)
        page_sizes[f"{width}x{height}"] += 1
        for annotation_ref in page.get("/Annots") or []:
            annotation = annotation_ref.get_object()
            if annotation.get("/Subtype") != "/Link":
                continue
            action = annotation.get("/A")
            destination = annotation.get("/Dest")
            if action is not None:
                action = action.get_object()
                action_type = str(action.get("/S") or "action_without_type")
                link_actions[action_type] += 1
                if action_type == "/GoTo":
                    destination = action.get("/D")
            elif destination is not None:
                link_actions["/Dest"] += 1
            else:
                link_actions["link_without_action"] += 1
            if destination is not None and isinstance(destination, str):
                if destination not in destinations:
                    invalid_goto_destinations.append(destination)

    metadata = {
        str(key): str(value)
        for key, value in (reader.metadata or {}).items()
    }
    metadata_text = "\n".join(metadata.values())
    metadata_blocked_hits = [
        token
        for token in (
            "ChatGPT",
            "OpenAI",
            "Claude",
            "Codex",
            "AI-generated",
            "AI-assisted",
            "LLM-generated",
        )
        if token.casefold() in metadata_text.casefold()
    ]
    return {
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
        "pages": len(reader.pages),
        "named_destinations": len(destinations),
        "invalid_named_destinations": invalid_named_destinations,
        "link_actions": dict(sorted(link_actions.items())),
        "invalid_goto_destinations": sorted(set(invalid_goto_destinations)),
        "page_sizes": dict(sorted(page_sizes.items())),
        "metadata": metadata,
        "metadata_blocked_hits": metadata_blocked_hits,
    }


def write_manifest() -> None:
    files = sorted(
        (
            path
            for path in PACKAGE_ROOT.iterdir()
            if path.is_file() and path.name != "SHA256SUMS.csv"
        ),
        key=lambda path: path.name.casefold(),
    )
    with (PACKAGE_ROOT / "SHA256SUMS.csv").open(
        "w", encoding="utf-8", newline=""
    ) as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(["filename", "bytes", "sha256"])
        for path in files:
            writer.writerow([path.name, path.stat().st_size, sha256(path)])


def main() -> int:
    errors: list[str] = []
    comparisons: dict[str, object] = {}
    for volume, (filename, predecessor_root) in PDFS.items():
        current = inspect_pdf(PACKAGE_ROOT / filename)
        predecessor = inspect_pdf(predecessor_root / filename)
        if current["invalid_named_destinations"]:
            errors.append(f"{volume}: invalid named destinations")
        if current["invalid_goto_destinations"]:
            errors.append(f"{volume}: invalid GoTo destinations")
        if current["metadata_blocked_hits"]:
            errors.append(f"{volume}: process/model metadata")
        comparisons[volume] = {
            "predecessor": predecessor,
            "reader_only_successor": current,
            "page_delta": current["pages"] - predecessor["pages"],
            "named_destination_delta": (
                current["named_destinations"]
                - predecessor["named_destinations"]
            ),
            "goto_delta": (
                current["link_actions"].get("/GoTo", 0)
                - predecessor["link_actions"].get("/GoTo", 0)
            ),
        }

    file_scan: dict[str, list[str]] = {}
    for path in sorted(PACKAGE_ROOT.iterdir()):
        if not path.is_file() or path.name == "SHA256SUMS.csv":
            continue
        data = path.read_bytes()
        hits = [
            pattern.pattern.decode("ascii", errors="replace")
            for pattern in PRIVATE_OR_PROCESS_PATTERNS
            if pattern.search(data)
        ]
        if hits:
            file_scan[path.name] = hits
    if file_scan:
        errors.append("public package privacy/process-name scan failed")

    payload = {
        "status": "PASS" if not errors else "FAIL",
        "purpose": (
            "Reader-only successor PDF structure, internal-link, metadata, "
            "and package privacy/process-name validation."
        ),
        "comparisons": comparisons,
        "package_scan_hits": file_scan,
        "errors": errors,
    }
    output = PACKAGE_ROOT / "PDF_STRUCTURE_VALIDATION.json"
    output.write_text(
        json.dumps(payload, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    write_manifest()
    print(json.dumps(payload, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())

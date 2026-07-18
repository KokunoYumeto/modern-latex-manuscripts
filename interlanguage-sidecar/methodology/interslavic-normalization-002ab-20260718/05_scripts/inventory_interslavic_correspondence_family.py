#!/usr/bin/env python3
"""Inventory correspondence-family surfaces in canonical Interslavic prose.

The scan is TeX-aware and streaming: one canonical Latin source is held at a
time, comments/math/protected arguments are excluded, and no text is edited.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

from apply_fable_tranche001 import read_text, transform_tex


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CORPUS = (
    ROOT
    / "03_projects"
    / "noether"
    / "02_slavic_working_corpus"
    / "translations"
)
DEFAULT_OUTPUT = (
    ROOT
    / "03_projects"
    / "language_management"
    / "slavic_interslavic"
    / "normalization_20260718"
    / "evidence"
    / "CORRESPONDENCE_FAMILY_SURFACE_INVENTORY.json"
)
ROOTS = ("sootvět", "sootvet", "sootvęt")
MARKERS = tuple(f"QZXCORRESPONDROOT{index}QZX" for index in range(len(ROOTS)))


def canonical_latin_files(corpus: Path) -> list[Path]:
    return sorted(
        path
        for path in corpus.rglob("*.tex")
        if "interslavic" in path.parts
        and "v001" in path.parts
        and "interslavic-cyrillic" not in path.parts
        and "working" not in path.parts
    )


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--examples-per-surface", type=int, default=3)
    args = parser.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    corpus = args.corpus.resolve()
    files = canonical_latin_files(corpus)
    if not files:
        raise SystemExit(f"No canonical Interslavic Latin TeX under {corpus}")

    mappings = tuple(zip(ROOTS, MARKERS))
    marker_patterns = {
        root: re.compile(re.escape(marker) + r"([^\W\d_]*)", re.UNICODE)
        for root, marker in mappings
    }
    surface_counts: Counter[str] = Counter()
    root_counts: Counter[str] = Counter()
    surface_files: dict[str, set[str]] = defaultdict(set)
    surface_examples: dict[str, list[dict[str, object]]] = defaultdict(list)
    affected_files: set[str] = set()
    aggregate = hashlib.sha256()

    for path in files:
        raw = path.read_bytes()
        relative = path.relative_to(corpus).as_posix()
        aggregate.update(relative.encode("utf-8"))
        aggregate.update(b"\0")
        aggregate.update(bytes.fromhex(sha256_bytes(raw)))
        original, _ = read_text(path)
        transform_counts: dict[tuple[str, str], int] = {}
        transformed = transform_tex(original, mappings, transform_counts)
        original_lines = original.splitlines()
        transformed_lines = transformed.splitlines()
        if len(original_lines) != len(transformed_lines):
            raise RuntimeError(f"Line preservation failed for {relative}")

        file_hits = 0
        for line_number, (before, after) in enumerate(
            zip(original_lines, transformed_lines), start=1
        ):
            for root, marker in mappings:
                for match in marker_patterns[root].finditer(after):
                    suffix = match.group(1)
                    surface = (root + suffix).lower()
                    surface_counts[surface] += 1
                    root_counts[root] += 1
                    surface_files[surface].add(relative)
                    file_hits += 1
                    examples = surface_examples[surface]
                    if len(examples) < args.examples_per_surface:
                        examples.append(
                            {
                                "path": relative,
                                "line": line_number,
                                "context": before.strip()[:700],
                            }
                        )
        parser_hits = sum(transform_counts.values())
        if file_hits != parser_hits:
            raise RuntimeError(
                f"Surface extraction mismatch for {relative}: "
                f"parser={parser_hits}, extracted={file_hits}"
            )
        if file_hits:
            affected_files.add(relative)

    surfaces = [
        {
            "surface": surface,
            "occurrences": count,
            "affected_files": len(surface_files[surface]),
            "examples": surface_examples[surface],
        }
        for surface, count in sorted(
            surface_counts.items(), key=lambda item: (-item[1], item[0])
        )
    ]
    report = {
        "schema": "interslavic-correspondence-family-surface-inventory-v1",
        "generated_at": datetime.now().astimezone().isoformat(),
        "scope": {
            "corpus": str(corpus),
            "selection": "canonical Latin **/interslavic/v001/*.tex; working/cumulative drafts excluded",
            "files_scanned": len(files),
            "affected_files": len(affected_files),
            "aggregate_path_and_filehash_sha256": aggregate.hexdigest().upper(),
        },
        "memory_policy": {
            "file_bodies_loaded_concurrently": 1,
            "parallel_scans": False,
            "whole_corpus_body_materialized": False,
        },
        "family_roots": list(ROOTS),
        "root_occurrences": dict(root_counts),
        "total_occurrences": sum(surface_counts.values()),
        "unique_surfaces": len(surface_counts),
        "surfaces": surfaces,
        "decision_boundary": {
            "accepted_direction": "re-head sootvětstvovati-family toward odpovědati-family",
            "execution_status": "not applied",
            "reason": "surface inventory contains verbs, adjectives, adverbs, nouns, spelling variants, and likely malformed derivatives; each needs a reviewed sense-and-inflection mapping before paired Latin/Cyrillic edits",
            "automatic_substring_replacement_authorized": False,
        },
        "interpretation_limits": [
            "Surface forms are lower-cased for grouping; original contexts preserve casing.",
            "This is a routing/paradigm inventory, not a proposed replacement table.",
            "No scalar branch score or dictionary lemma alone chooses a contextual target.",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"wrote {args.output}")
    print(
        f"files={len(files)} affected={len(affected_files)} "
        f"occurrences={report['total_occurrences']} surfaces={len(surfaces)}"
    )
    for row in surfaces[:20]:
        print(
            f"{row['occurrences']:>4}  files={row['affected_files']:>3}  "
            f"{row['surface']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

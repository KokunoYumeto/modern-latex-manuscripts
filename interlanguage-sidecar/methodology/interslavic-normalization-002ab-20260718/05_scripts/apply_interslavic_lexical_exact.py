#!/usr/bin/env python3
"""Apply only the explicitly accepted exact lexical switches of Tranche 002B.

This tranche intentionally excludes the sanctioned dictionary headword
``jednovrěmenno``, the unreviewed nearby time adverbs, the correspondence
family (which still needs an inflection table), and every held row.
"""

from __future__ import annotations

import argparse
import csv
import difflib
import hashlib
import json
import shutil
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from apply_fable_tranche001 import read_text, transform_tex, write_text


ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "03_projects" / "noether" / "02_slavic_working_corpus" / "translations"
WORKSPACE = (
    ROOT
    / "03_projects"
    / "language_management"
    / "slavic_interslavic"
    / "normalization_20260718"
    / "tranche_002b_lexical_exact"
)
EVIDENCE = WORKSPACE / "evidence"
PREIMAGE = WORKSPACE / "preimage"

LATIN_MAPPINGS = (
    ("odnovrěmenno", "jednočasno"),
    ("odnovremenno", "jednočasno"),
    ("odnovočasno", "jednočasno"),
    ("istočasno", "jednočasno"),
    ("korak", "krok"),
)

CYRILLIC_MAPPINGS = (
    ("одновременно", "једночасно"),
    ("одновочасно", "једночасно"),
    ("источасно", "једночасно"),
    ("корак", "крок"),
)

LATIN_HELD_PROBES = (
    "jednovrěmenno",  # dictionary-sanctioned headword; includes two adjectival inflections
    "Jednovremenno",
    "istovrěmenno",
    "samočasno",
)


@dataclass(frozen=True)
class PlannedFile:
    path: Path
    script: str
    before_sha256: str
    projected_after_sha256: str
    counts: dict[str, int]
    has_bom: bool


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def encoded(text: str, has_bom: bool) -> bytes:
    return text.encode("utf-8-sig" if has_bom else "utf-8")


def canonical_latin_files() -> list[Path]:
    return sorted(
        path
        for path in CORPUS.rglob("*.tex")
        if "interslavic" in path.parts
        and "v001" in path.parts
        and "interslavic-cyrillic" not in path.parts
        and "working" not in path.parts
    )


def cyrillic_sibling(latin: Path) -> Path:
    relative = latin.relative_to(CORPUS)
    parts = list(relative.parts)
    index = parts.index("interslavic")
    parts[index] = "interslavic-cyrillic"
    parts[-1] = parts[-1].replace(
        "_Interslavic_v001.tex", "_Interslavic_Cyrillic_v001.tex"
    )
    return CORPUS.joinpath(*parts)


def scan_file(path: Path, script: str, mappings: tuple[tuple[str, str], ...]) -> PlannedFile | None:
    original, has_bom = read_text(path)
    raw_counts: dict[tuple[str, str], int] = {}
    transformed = transform_tex(original, mappings, raw_counts)
    second_counts: dict[tuple[str, str], int] = {}
    second = transform_tex(transformed, mappings, second_counts)
    if transformed != second or any(second_counts.values()):
        raise RuntimeError(f"Non-idempotent transform projected for {path}")
    if transformed == original:
        return None
    counts = {
        f"{source}->{target}": raw_counts.get((source, target), 0)
        for source, target in mappings
        if raw_counts.get((source, target), 0)
    }
    return PlannedFile(
        path=path,
        script=script,
        before_sha256=sha256_bytes(path.read_bytes()),
        projected_after_sha256=sha256_bytes(encoded(transformed, has_bom)),
        counts=counts,
        has_bom=has_bom,
    )


def held_probe_counts(files: list[Path]) -> dict[str, int]:
    totals = {probe: 0 for probe in LATIN_HELD_PROBES}
    for path in files:
        original, _ = read_text(path)
        for index, probe in enumerate(LATIN_HELD_PROBES):
            marker = f"NORMHELDPROBE{index}"
            counts: dict[tuple[str, str], int] = {}
            transform_tex(original, ((probe, marker),), counts)
            totals[probe] += counts.get((probe, marker), 0)
    return totals


def preflight() -> tuple[list[PlannedFile], dict[str, object]]:
    latin_files = canonical_latin_files()
    if len(latin_files) != 221:
        raise RuntimeError(f"Expected 221 canonical Latin files, found {len(latin_files)}")
    cyrillic_files = [cyrillic_sibling(path) for path in latin_files]
    missing = [str(path) for path in cyrillic_files if not path.is_file()]
    if missing:
        raise RuntimeError("Missing Cyrillic siblings: " + ", ".join(missing))

    plan: list[PlannedFile] = []
    for script, files, mappings in (
        ("Latin", latin_files, LATIN_MAPPINGS),
        ("Cyrillic", cyrillic_files, CYRILLIC_MAPPINGS),
    ):
        for path in files:
            projected = scan_file(path, script, mappings)
            if projected:
                plan.append(projected)

    replacement_totals: dict[str, int] = {}
    for item in plan:
        for mapping, count in item.counts.items():
            key = f"{item.script}:{mapping}"
            replacement_totals[key] = replacement_totals.get(key, 0) + count

    return plan, {
        "schema": "interslavic-lexical-exact-preflight-v1",
        "generated_at": datetime.now().astimezone().isoformat(),
        "scope": "221 paired canonical Noether Interslavic Latin/Cyrillic v001 TeX units; working drafts excluded",
        "authority": "FABLE_TRANCHE_001_EXECUTABLE_SPEC Tranche 002 preview plus explicit user activation 2026-07-18",
        "memory_policy": {
            "file_bodies_loaded_concurrently": 1,
            "parallel_scans": False,
            "transformed_corpus_retained_in_memory": False,
        },
        "planned_changed_files": len(plan),
        "planned_latin_files": sum(item.script == "Latin" for item in plan),
        "planned_cyrillic_files": sum(item.script == "Cyrillic" for item in plan),
        "replacement_totals": replacement_totals,
        "sanctioned_or_unreviewed_time_forms_held": held_probe_counts(latin_files),
        "correspondence_family_touched": False,
        "held_rows_touched": False,
        "planned_files": [
            {
                "path": item.path.relative_to(CORPUS).as_posix(),
                "script": item.script,
                "before_sha256": item.before_sha256,
                "projected_after_sha256": item.projected_after_sha256,
                "counts": item.counts,
            }
            for item in plan
        ],
    }


def apply_plan(plan: list[PlannedFile], preflight: dict[str, object]) -> dict[str, object]:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    PREIMAGE.mkdir(parents=True, exist_ok=True)
    diff_path = EVIDENCE / "TRANCHE002B_LEXICAL_EXACT.diff"
    ledger_path = EVIDENCE / "CHANGE_LEDGER.csv"
    with diff_path.open("w", encoding="utf-8", newline="") as diff_handle, ledger_path.open(
        "w", encoding="utf-8", newline=""
    ) as ledger_handle:
        writer = csv.writer(ledger_handle)
        writer.writerow(["path", "script", "source", "target", "count", "before_sha256", "after_sha256"])
        for item in plan:
            if sha256_bytes(item.path.read_bytes()) != item.before_sha256:
                raise RuntimeError(f"Input changed after preflight: {item.path}")
            original, has_bom = read_text(item.path)
            mappings = LATIN_MAPPINGS if item.script == "Latin" else CYRILLIC_MAPPINGS
            counts: dict[tuple[str, str], int] = {}
            transformed = transform_tex(original, mappings, counts)
            relative = item.path.relative_to(CORPUS)
            backup = PREIMAGE / relative
            backup.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item.path, backup)
            write_text(item.path, transformed, has_bom)
            after_hash = sha256_bytes(item.path.read_bytes())
            if after_hash != item.projected_after_sha256:
                raise RuntimeError(f"Written hash mismatch: {item.path}")
            diff_handle.writelines(
                difflib.unified_diff(
                    original.splitlines(keepends=True), transformed.splitlines(keepends=True),
                    fromfile=f"a/{relative.as_posix()}", tofile=f"b/{relative.as_posix()}", n=3,
                )
            )
            for source, target in mappings:
                count = counts.get((source, target), 0)
                if count:
                    writer.writerow([relative.as_posix(), item.script, source, target, count, item.before_sha256, after_hash])

    residuals: list[dict[str, object]] = []
    for item in plan:
        mappings = LATIN_MAPPINGS if item.script == "Latin" else CYRILLIC_MAPPINGS
        text, _ = read_text(item.path)
        counts: dict[tuple[str, str], int] = {}
        second = transform_tex(text, mappings, counts)
        if second != text or any(counts.values()):
            residuals.append({"path": item.path.relative_to(CORPUS).as_posix(), "counts": {f"{a}->{b}": n for (a, b), n in counts.items() if n}})
    return {
        "schema": "interslavic-lexical-exact-rollout-v1",
        "generated_at": datetime.now().astimezone().isoformat(),
        "scope": preflight["scope"],
        "authority": preflight["authority"],
        "memory_policy": preflight["memory_policy"],
        "changed_file_count": len(plan),
        "changed_latin_files": sum(item.script == "Latin" for item in plan),
        "changed_cyrillic_files": sum(item.script == "Cyrillic" for item in plan),
        "replacement_totals": preflight["replacement_totals"],
        "sanctioned_or_unreviewed_time_forms_held": preflight["sanctioned_or_unreviewed_time_forms_held"],
        "idempotence_residuals": residuals,
        "idempotence_pass": not residuals,
        "correspondence_family_touched": False,
        "held_rows_touched": False,
        "preimage_root": str(PREIMAGE),
        "change_ledger": str(ledger_path),
        "diff": str(diff_path),
        "status_limit": "Exact accepted lexical switches only; not full simultaneity-family or correspondence-family normalization.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    plan, report = preflight()
    latin_simultaneous = sum(
        count for key, count in report["replacement_totals"].items()
        if key.startswith("Latin:") and "korak" not in key.lower()
    )
    latin_step = sum(
        count for key, count in report["replacement_totals"].items()
        if key.startswith("Latin:") and "korak" in key.lower()
    )
    if (latin_simultaneous, latin_step) != (80, 32):
        raise RuntimeError(
            f"Expected Latin lexical counts (80, 32), found ({latin_simultaneous}, {latin_step})"
        )
    preflight_path = EVIDENCE / "LEXICAL_EXACT_PREFLIGHT.json"
    preflight_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: report[key] for key in (
        "planned_changed_files", "planned_latin_files", "planned_cyrillic_files",
        "replacement_totals", "sanctioned_or_unreviewed_time_forms_held",
    )}, ensure_ascii=False, indent=2))
    print(f"wrote {preflight_path}")
    if not args.apply:
        print("dry-run only; pass --apply to write the exact lexical tranche")
        return 0
    applied = apply_plan(plan, report)
    output = EVIDENCE / "LEXICAL_EXACT_REPORT.json"
    output.write_text(json.dumps(applied, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {output}")
    print(f"changed_files={applied['changed_file_count']} idempotence_pass={applied['idempotence_pass']}")
    return 0 if applied["idempotence_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

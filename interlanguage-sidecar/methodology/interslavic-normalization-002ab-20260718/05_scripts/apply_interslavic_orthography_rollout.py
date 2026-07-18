#!/usr/bin/env python3
"""Apply the reviewed Fable orthography mappings corpus-wide, safely.

Scope: canonical Noether ``interslavic/v001`` and paired
``interslavic-cyrillic/v001`` TeX only.  The script performs a streaming
preflight, requires the known Latin residue count, keeps preimages for every
changed file, writes one file at a time, and proves a second pass is empty.
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
CORPUS = (
    ROOT
    / "03_projects"
    / "noether"
    / "02_slavic_working_corpus"
    / "translations"
)
WORKSPACE = (
    ROOT
    / "03_projects"
    / "language_management"
    / "slavic_interslavic"
    / "normalization_20260718"
    / "tranche_002a_orthography"
)
EVIDENCE = WORKSPACE / "evidence"
PREIMAGE = WORKSPACE / "preimage"

LATIN_MAPPINGS = (
    ("voobče", "obće"),
    ("vobče", "obće"),
    ("dlugost", "dolgost"),
    ("obšč", "obć"),
    ("vzet", "vzęt"),
)

CYRILLIC_MAPPINGS = (
    ("вообче", "обче"),
    ("вобче", "обче"),
    ("длугост", "долгост"),
    ("обшч", "обч"),
    ("взет", "взят"),
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

    report = {
        "schema": "interslavic-orthography-rollout-preflight-v1",
        "generated_at": datetime.now().astimezone().isoformat(),
        "scope": "221 paired canonical Noether Interslavic Latin/Cyrillic v001 TeX units; working drafts excluded",
        "memory_policy": {
            "file_bodies_loaded_concurrently": 1,
            "parallel_scans": False,
            "transformed_corpus_retained_in_memory": False,
        },
        "planned_changed_files": len(plan),
        "planned_latin_files": sum(item.script == "Latin" for item in plan),
        "planned_cyrillic_files": sum(item.script == "Cyrillic" for item in plan),
        "replacement_totals": replacement_totals,
        "paper06_changes": [
            item.path.relative_to(CORPUS).as_posix()
            for item in plan
            if "paper06" in item.path.parts
        ],
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
    return plan, report


def apply_plan(plan: list[PlannedFile], preflight_report: dict[str, object]) -> dict[str, object]:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    PREIMAGE.mkdir(parents=True, exist_ok=True)
    diff_path = EVIDENCE / "TRANCHE002A_ORTHOGRAPHY.diff"
    ledger_path = EVIDENCE / "CHANGE_LEDGER.csv"

    with diff_path.open("w", encoding="utf-8", newline="") as diff_handle, ledger_path.open(
        "w", encoding="utf-8", newline=""
    ) as ledger_handle:
        writer = csv.writer(ledger_handle)
        writer.writerow(
            [
                "path",
                "script",
                "source",
                "target",
                "count",
                "before_sha256",
                "after_sha256",
            ]
        )
        for item in plan:
            current_raw = item.path.read_bytes()
            if sha256_bytes(current_raw) != item.before_sha256:
                raise RuntimeError(f"Input changed after preflight: {item.path}")
            original, has_bom = read_text(item.path)
            mappings = LATIN_MAPPINGS if item.script == "Latin" else CYRILLIC_MAPPINGS
            raw_counts: dict[tuple[str, str], int] = {}
            transformed = transform_tex(original, mappings, raw_counts)
            if sha256_bytes(encoded(transformed, has_bom)) != item.projected_after_sha256:
                raise RuntimeError(f"Projected output drifted after preflight: {item.path}")

            relative = item.path.relative_to(CORPUS)
            backup = PREIMAGE / relative
            backup.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item.path, backup)
            write_text(item.path, transformed, has_bom)
            after_sha = sha256_bytes(item.path.read_bytes())
            if after_sha != item.projected_after_sha256:
                raise RuntimeError(f"Written hash mismatch: {item.path}")

            diff_handle.writelines(
                difflib.unified_diff(
                    original.splitlines(keepends=True),
                    transformed.splitlines(keepends=True),
                    fromfile=f"a/{relative.as_posix()}",
                    tofile=f"b/{relative.as_posix()}",
                    n=3,
                )
            )
            for source, target in mappings:
                count = raw_counts.get((source, target), 0)
                if count:
                    writer.writerow(
                        [
                            relative.as_posix(),
                            item.script,
                            source,
                            target,
                            count,
                            item.before_sha256,
                            after_sha,
                        ]
                    )

    residuals: list[dict[str, object]] = []
    for item in plan:
        mappings = LATIN_MAPPINGS if item.script == "Latin" else CYRILLIC_MAPPINGS
        text, _ = read_text(item.path)
        counts: dict[tuple[str, str], int] = {}
        second = transform_tex(text, mappings, counts)
        if second != text or any(counts.values()):
            residuals.append(
                {
                    "path": item.path.relative_to(CORPUS).as_posix(),
                    "counts": {f"{a}->{b}": n for (a, b), n in counts.items() if n},
                }
            )

    report = {
        "schema": "interslavic-orthography-rollout-v1",
        "generated_at": datetime.now().astimezone().isoformat(),
        "authority": "00_governance/FABLE_TRANCHE_001_EXECUTABLE_SPEC_20260710.md plus explicit user activation 2026-07-18",
        "scope": preflight_report["scope"],
        "memory_policy": preflight_report["memory_policy"],
        "changed_file_count": len(plan),
        "changed_latin_files": sum(item.script == "Latin" for item in plan),
        "changed_cyrillic_files": sum(item.script == "Cyrillic" for item in plan),
        "replacement_totals": preflight_report["replacement_totals"],
        "paper06_unchanged_after_prior_pilot": not preflight_report["paper06_changes"],
        "idempotence_residuals": residuals,
        "idempotence_pass": not residuals,
        "lexeme_switches_applied": False,
        "held_rows_touched": False,
        "preimage_root": str(PREIMAGE),
        "change_ledger": str(ledger_path),
        "diff": str(diff_path),
        "status_limit": "Internal reviewed orthography rollout; not lexical normalization completion or community certification.",
    }
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--expected-latin-replacements", type=int, default=162)
    args = parser.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    EVIDENCE.mkdir(parents=True, exist_ok=True)
    plan, report = preflight()
    latin_replacements = sum(
        count
        for key, count in report["replacement_totals"].items()
        if key.startswith("Latin:")
    )
    if latin_replacements != args.expected_latin_replacements:
        raise RuntimeError(
            f"Expected {args.expected_latin_replacements} Latin replacements, found {latin_replacements}"
        )
    if report["paper06_changes"]:
        raise RuntimeError(
            "Paper 06 unexpectedly contains residual Tranche 001 forms: "
            + ", ".join(report["paper06_changes"])
        )

    preflight_path = EVIDENCE / "ORTHOGRAPHY_ROLLOUT_PREFLIGHT.json"
    preflight_path.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"wrote {preflight_path}")
    print(json.dumps({k: report[k] for k in (
        "planned_changed_files",
        "planned_latin_files",
        "planned_cyrillic_files",
        "replacement_totals",
        "paper06_changes",
    )}, ensure_ascii=False, indent=2))

    if not args.apply:
        print("dry-run only; pass --apply to write the reviewed orthography rollout")
        return 0

    applied = apply_plan(plan, report)
    output = EVIDENCE / "ORTHOGRAPHY_ROLLOUT_REPORT.json"
    output.write_text(json.dumps(applied, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {output}")
    print(f"changed_files={applied['changed_file_count']} idempotence_pass={applied['idempotence_pass']}")
    return 0 if applied["idempotence_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

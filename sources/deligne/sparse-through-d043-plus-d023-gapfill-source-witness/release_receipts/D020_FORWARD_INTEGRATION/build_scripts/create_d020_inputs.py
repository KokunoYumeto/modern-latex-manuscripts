"""Create the sealed, exact-path D020 integration input manifest.

This performs bounded read-only identity checks on the published D033 build and
the fresh D020 V6 cold-audit subject.  Its only write is the new task-local
NEXT_INTEGRATION_INPUTS.json, which must not already exist.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import shutil
import sys
from pathlib import Path


TASK = Path(__file__).resolve().parents[1]
OUTPUT = TASK / "NEXT_INTEGRATION_INPUTS.json"
STAGING = TASK.parent.parent
BASE = TASK.parent / "successor_D033_gapfill_from_D019/build/cumulative"
D020_WORK = STAGING / "Noether_Multilingual_Reconciliation/corpus_gate/D020/work/S06_math_v6"
D020_COLD = STAGING / "Noether_Multilingual_Reconciliation/corpus_gate/D020/audit_cold/S06_math_v6_01"


def identity(path: Path) -> dict[str, object]:
    digest = hashlib.sha256()
    size = 0
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            size += len(block)
            digest.update(block)
    return {"path": path.as_posix(), "bytes": size, "sha256": digest.hexdigest().upper()}


def read_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    if OUTPUT.exists():
        raise RuntimeError("sealed input manifest already exists")
    receipt_path = BASE / "BUILD_RELEASE_RECEIPT.json"
    receipt = read_json(receipt_path)
    if not isinstance(receipt, dict) or receipt.get("status") != "PASS":
        raise RuntimeError("D033 predecessor build receipt is not PASS")
    source_manifest = BASE / "source_tree/PUBLIC_SOURCE_MANIFEST.tsv"
    source_rows = sum(1 for _ in source_manifest.open("r", encoding="utf-8")) - 1
    if source_rows != 2925:
        raise RuntimeError("unexpected D033 source-manifest row count")
    qa = read_json(BASE / "audit/CUMULATIVE_PAGE_QA.json")
    if qa["status"] != "PASS":
        raise RuntimeError("D033 predecessor QA is not PASS")

    subject_manifest_path = D020_COLD / "SUBJECT_MANIFEST.json"
    subject_manifest = read_json(subject_manifest_path)
    subject_files = subject_manifest.get("files", [])
    if subject_manifest.get("schema") != "d020-immutable-cold-subject-v4" or len(subject_files) != 328:
        raise RuntimeError("D020 frozen subject manifest differs")
    if sum(int(row["bytes"]) for row in subject_files) != 106_554_318:
        raise RuntimeError("D020 frozen subject byte total differs")
    final_audit_path = D020_COLD / "evidence/V6_FULL_PAPER_COLD_AUDIT.json"
    final_audit = read_json(final_audit_path)
    if not (
        final_audit.get("terminal_status") == "PASS_PAPER_COMPLETE"
        and final_audit.get("paper_complete_established") is True
        and final_audit.get("publication_ready") is True
        and final_audit.get("candidate_public_surface_status") == "PASS"
    ):
        raise RuntimeError("D020 final cold audit is not publication-ready PASS")

    release_files = []
    for row in receipt["files"]:
        path = BASE / str(row["staged_path"])
        actual = identity(path)
        if actual["bytes"] != int(row["bytes"]) or actual["sha256"].casefold() != row["sha256"].casefold():
            raise RuntimeError("D033 release identity mismatch")
        release_files.append(actual)

    selected_audit_names = (
        "SUBJECT_MANIFEST.json",
        "evidence/V6_FULL_PAPER_COLD_AUDIT.json",
        "evidence/V6_FULL_PAPER_COLD_AUDIT.md",
        "evidence/V6_COLD_AUDIT_REPORT_HASHES.json",
        "evidence/SUBJECT_INTEGRITY_END.json",
        "evidence/VISUAL_CONTACT_INVENTORY.json",
        "evidence/V6_FINALIZER_JOB_GUARD.json",
    )
    selected_audit = [identity(D020_COLD / name) | {"relative": name} for name in selected_audit_names]

    result = {
        "schema": "d020-next-integration-inputs-v1",
        "status": "SEALED_LOCAL_INPUTS",
        "prepared_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "work_id": "D020",
        "write_boundary": TASK.as_posix(),
        "publication_context": {
            "repository": "KokunoYumeto/modern-latex-manuscripts",
            "branch": "codex/github-maint-20260804",
            "concept_doi": "10.5281/zenodo.20410853",
            "figshare": "EXCLUDED",
        },
        "predecessor": {
            "work": "D033_RELEASE_BASELINE",
            "root": BASE.as_posix(),
            "receipt": identity(receipt_path),
            "source_manifest": identity(source_manifest),
            "source_manifest_members": source_rows,
            "source_readme": identity(BASE / "source_tree/README.md"),
            "release_files": release_files,
            "pages": {lang: int(qa["languages"][lang]["pages"]) for lang in ("EN", "FR")},
            "frontmatter_pages": {lang: int(qa["languages"][lang]["frontmatter_pages"]) for lang in ("EN", "FR")},
        },
        "d020": {
            "source_language": "French",
            "translation_language": "English",
            "work_root": D020_WORK.as_posix(),
            "cold_audit_root": D020_COLD.as_posix(),
            "subject_manifest": identity(subject_manifest_path),
            "subject_members": 328,
            "subject_member_bytes": 106_554_318,
            "final_audit": identity(final_audit_path),
            "selected_audit": selected_audit,
            "canonical_readers": {
                "FR": identity(D020_WORK / "readers/pdf/source_language.pdf"),
                "EN": identity(D020_WORK / "readers/pdf/english_standalone.pdf"),
                "APPARATUS": identity(D020_WORK / "readers/pdf/apparatus.pdf"),
            },
            "canonical_tex": {
                "FR": identity(D020_WORK / "tex/source_language.tex"),
                "EN": identity(D020_WORK / "tex/english_standalone.tex"),
                "APPARATUS": identity(D020_WORK / "tex/apparatus.tex"),
            },
            "authority": identity(D020_WORK / "source/20_AUTHORITY_DELIGNE_D020_WEIL_I_NUMDAM_36PP.pdf"),
        },
        "insertion": {
            "after": "D019",
            "before": "D021",
            "body_page_increments": {"EN": 35, "FR": 35},
            "source_reader_mapping": {
                "EN": "works/D020_PUBLIC_SAFE/state/readers/pdf/english_standalone.pdf",
                "FR": "works/D020_PUBLIC_SAFE/state/readers/pdf/source_language.pdf",
            },
            "master_insertions": {
                "EN": "\\includepdf[pages=-,pagecommand={},addtotoc={1,section,1,{D020 - The Weil Conjecture. I},d020}]{works/D020_PUBLIC_SAFE/state/readers/pdf/english_standalone.pdf}",
                "FR": "\\includepdf[pages=-,pagecommand={},addtotoc={1,section,1,{D020 - La conjecture de Weil. I},d020}]{works/D020_PUBLIC_SAFE/state/readers/pdf/source_language.pdf}",
            },
            "coverage_replacements": {
                "EN": [
                    ["Included in numerical order: D001--D019; D021; D022; D023;", "Included in numerical order: D001--D023;"],
                    ["Gaps: D020; D024;", "Gaps: D024;"],
                ],
                "FR": [
                    ["Inclus dans l'ordre numérique: D001--D019; D021; D022; D023;", "Inclus dans l'ordre numérique: D001--D023;"],
                    ["Lacunes: D020; D024;", "Lacunes: D024;"],
                ],
            },
            "expected_if_frontmatter_unchanged": {
                "EN": {"total_pages": 1135, "D020": [643, 677], "D021_first": 678},
                "FR": {"total_pages": 1148, "D020": [656, 690], "D021_first": 691},
            },
            "coverage_after": "D001-D023; D025-D031; D033-D036; D038-D040; D043",
            "explicit_gaps_after": "D024; D032; D037; D041-D042",
        },
        "runtime": {
            "python": Path(sys.executable).as_posix(),
            "engine": str(Path(shutil.which("xelatex") or "xelatex").as_posix()),
            "environment": {"SOURCE_DATE_EPOCH": "946684800", "FORCE_SOURCE_DATE": "1", "TZ": "UTC"},
        },
        "next_action": "Prepare a hardlink-efficient D033 clone, copy D020 bytes, patch masters, then run serial memory-capped build and QA.",
    }
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"status": "PASS", "output": OUTPUT.as_posix(), **identity(OUTPUT)}, indent=2))


if __name__ == "__main__":
    main()

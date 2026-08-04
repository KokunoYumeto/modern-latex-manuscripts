from __future__ import annotations

import hashlib
import json
from pathlib import Path


SCRIPT = Path(__file__).resolve()
RECHECK = SCRIPT.parents[1]
PAPER35 = SCRIPT.parents[2]
CHECKER_ROOT = SCRIPT.parents[3]
WORKSPACE = SCRIPT.parents[8]
RETURN = RECHECK / "return"
SNAPSHOT = RETURN / "sealed_member_snapshots" / "ZHCHK-NOETHER-P35-V002-RETURN-001"
FROZEN = RECHECK / "intake" / "frozen_producer_package_v002"
PRODUCER = (
    WORKSPACE
    / "03_projects/language_management/cjk/03_working_translations"
    / "noether_paper35_zh_translation_002_20260804"
)
RECORDED_AT = "2026-08-04T07:37:32.5890949+02:00"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def fact(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    return {"path": str(path), "bytes": len(data), "sha256": digest(data)}


def write_utf8(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def write_json(path: Path, value: object) -> None:
    write_utf8(path, json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def copy_exact(source: Path, target: Path) -> None:
    data = source.read_bytes()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
    assert target.read_bytes() == data


def parse_manifest(path: Path) -> list[tuple[str, int, str]]:
    rows: list[tuple[str, int, str]] = []
    for raw in path.read_text(encoding="utf-8-sig").splitlines():
        if not raw or raw.startswith("#"):
            continue
        sha, size, rel = raw.split("  ", 2)
        rows.append((sha.upper(), int(size), rel))
    return rows


def replay_manifest(root: Path, manifest: Path) -> dict[str, object]:
    rows = parse_manifest(manifest)
    paths = [row[2] for row in rows]
    failures: list[dict[str, object]] = []
    for expected_sha, expected_bytes, rel in rows:
        target = root / Path(rel)
        if not target.is_file():
            failures.append({"path": rel, "failure": "missing"})
            continue
        actual = fact(target)
        if actual["bytes"] != expected_bytes or actual["sha256"] != expected_sha:
            failures.append(
                {
                    "path": rel,
                    "failure": "identity",
                    "expected_bytes": expected_bytes,
                    "actual_bytes": actual["bytes"],
                    "expected_sha256": expected_sha,
                    "actual_sha256": actual["sha256"],
                }
            )
    actual_members = {
        p.relative_to(root).as_posix()
        for p in root.rglob("*")
        if p.is_file() and p.resolve() != manifest.resolve()
    }
    declared = {Path(p).as_posix() for p in paths}
    result = {
        "manifest": fact(manifest),
        "declared_entries": len(rows),
        "unique_entries": len(set(paths)),
        "duplicate_entries": len(rows) - len(set(paths)),
        "missing_or_identity_failures": failures,
        "extra_files": sorted(actual_members - declared),
        "all_pass": not failures and not (actual_members - declared) and len(rows) == len(set(paths)),
    }
    return result


def main() -> int:
    RETURN.mkdir(parents=True, exist_ok=True)
    assert PRODUCER.is_dir()
    assert FROZEN.is_dir()
    assert (PRODUCER / "SHA256SUMS.txt").read_bytes() == (FROZEN / "SHA256SUMS.txt").read_bytes()

    external_replay = replay_manifest(PRODUCER, PRODUCER / "SHA256SUMS.txt")
    snapshot_replay = replay_manifest(FROZEN, FROZEN / "SHA256SUMS.txt")
    assert external_replay["all_pass"] and snapshot_replay["all_pass"]
    assert external_replay["declared_entries"] == snapshot_replay["declared_entries"] == 130

    copy_exact(PAPER35 / "findings/P35_FINDING_LEDGER.jsonl", SNAPSHOT / "P35_FINDING_LEDGER.jsonl")
    copy_exact(
        PAPER35 / "findings/P35_DIFFICULTY_FAILURE_LEDGER.jsonl",
        SNAPSHOT / "P35_DIFFICULTY_FAILURE_LEDGER.jsonl",
    )
    copy_exact(CHECKER_ROOT / "CHECKER_DECISION_LOG.md", SNAPSHOT / "CHECKER_DECISION_LOG.md")

    hans_tex = FROZEN / "build/zh-Hans-CN-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v002.tex"
    hans_pdf = FROZEN / "build/zh-Hans-CN-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v002.pdf"
    hant_tex = FROZEN / "build/zh-Hant-controlled-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_v002.tex"
    hant_pdf = FROZEN / "build/zh-Hant-controlled-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_v002.pdf"
    candidate_tex = RECHECK / "candidate/zh-Hant-controlled/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_checker_candidate_v003.tex"
    candidate_pdf = RECHECK / "build/hant_candidate_v003/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_checker_candidate_v003.pdf"
    correction_diff = RECHECK / "findings/P35_HANT_F015_CORRECTION_DIFF.patch"
    substantive = json.loads((RECHECK / "evidence/P35_V002_SUBSTANTIVE_RECHECK_RECORD.json").read_text(encoding="utf-8"))

    expected = {
        hans_tex: (31328, "DDF7E898E706552028C2BCEAC4BBDE3D45487C6A339F7FA0A43968FF7E1F465C"),
        hans_pdf: (274158, "F6626C3DC6FFB82E3CFD5C21FA3F74B99459D477E39093715802C49E91E2A18C"),
        hant_tex: (31515, "FD16882FAC33B7FD7D0FFB882345168E40FA7F1F22FDEE83AFA2420627D1C054"),
        hant_pdf: (306051, "8E77A4C511462C8ECF5876CE7EED0E3A9C4CAD8820A492BD8E665FB47FA50CF1"),
        candidate_tex: (31515, "54DE9B43850376FD19306A11FC682166D8F34A4CA6D73E0940695357CE74A005"),
        candidate_pdf: (284856, "5595AEBC8A59247D0E87BC94D9D350B031BCEF6C071BC34642EA9F6C0E695A15"),
        correction_diff: (7840, "A87F91E27B5BA0CD25BB3983A55140F4C0C7F1AE32CE6A6FE7AFF0EAB96DD8D4"),
    }
    for path, (expected_bytes, expected_sha) in expected.items():
        actual = fact(path)
        assert actual["bytes"] == expected_bytes and actual["sha256"] == expected_sha
    assert substantive["all_assertions_pass"] is True

    summary_path = RETURN / "P35_V002_CHECKER_RETURN_SUMMARY.md"
    receipt_path = RETURN / "P35_V002_CHECKER_RETURN_RECEIPT.json"
    manifest_path = RETURN / "SHA256SUMS.txt"

    summary = rf"""# Paper 35 Chinese independent-checker return — v002

Return ID: `ZHCHK-NOETHER-P35-V002-RETURN-001`

## Disposition

- **Overall frozen dual-target package: REJECTED.** A Hant-only producer correction, serial rebuild, new freeze, and new exact re-handoff are required.
- **PRC-oriented zh-Hans-CN v002: ACCEPTED.** Findings F001–F011 are resolved and the exact 29,808-byte body (`54061274DFDE806F491EE424277886ED4C4CEEF3F7E0315DFD1039AACF69F18A`) passed the independent semantic, terminology, formula, TeX, build, PDF-text, render, and six-page visual replay.
- **Frozen controlled-generic Hant v002: REJECTED for `ZHCHK-P35-F015`.** The exact F012 and F014 loci are corrected, but page 5 contains a large mixed-script block.
- **Checker controlled-generic Hant candidate v003: VALIDATED correction candidate.** This is generic script transport only—not Taiwan, Hong Kong, or Macao localization.

## F015 exact coordinates and cause

Target: `build/zh-Hant-controlled-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_v002.tex`.

The producer regex treats the second backslash in line 244 `\\[0.6em]` as a `\[` display opener and protects through line 272. Visible unconverted Simplified prose is concentrated on lines 245–269. The corresponding 28 complete Hans/Hant lines are byte-identical: 3,901 bytes, SHA-256 `FB5301141DA8681A6551AC92E85BA8C1B96279781D4005C42FD9ED79D02C1098`; the false protected span is 2,075 characters.

## Exact correction and validation

- Candidate TeX: 31,515 bytes, SHA-256 `54DE9B43850376FD19306A11FC682166D8F34A4CA6D73E0940695357CE74A005`.
- Candidate PDF: 284,856 bytes, SHA-256 `5595AEBC8A59247D0E87BC94D9D350B031BCEF6C071BC34642EA9F6C0E695A15`.
- Exact correction diff: 7,840 bytes, SHA-256 `A87F91E27B5BA0CD25BB3983A55140F4C0C7F1AE32CE6A6FE7AFF0EAB96DD8D4`.
- Escaped-delimiter replay: all 487 math spans and all 790 TeX controls preserved; zero legacy false display spans.
- Formula/structure: 478 source formulas; zero missing symbolic source formulas; nine expected explicit target repeats; environment and structural signatures equal.
- Builds: Hans, frozen Hant, and candidate Hant each completed two serial XeLaTeX passes and produced six pages; no overfull boxes or missing characters.
- Visual QA: all pages were inspected directly or by exact raster identity. Hans passes; frozen Hant page 5 confirms F015; corrected Hant page 5 passes.

## Producer action

Integrate only the Hant F015 scanner/correction, regenerate from the accepted Hans body, reapply the already controlled generic normalizations, compile serially, freeze a new manifest/handoff, and return it here. The accepted Hans target need not change.

## Scope

F013 remains unresolved/no action. No German-source defect was confirmed, no German packet was created or sent, German was not mutated, and SGA was not touched.
"""
    write_utf8(summary_path, summary)

    selected = [
        "intake/P35_V002_CHECKER_INTAKE_RECEIPT.json",
        "intake/NOETHER_P35_ZH_V002_PRODUCER_FREEZE_VERIFICATION_20260804.json",
        "intake/frozen_producer_package_v002/SHA256SUMS.txt",
        "intake/frozen_producer_package_v002/CHINESE_PRODUCER_CORRECTED_RETURN_AND_CHECKER_REHANDOFF.md",
        "intake/frozen_producer_package_v002/source/current/CHINESE_P35_BINDER_20260804.json",
        "intake/frozen_producer_package_v002/source/current/Noether_P35_Zenodo21699405_source_native_CRLF.tex",
        "intake/frozen_producer_package_v002/source/current/Noether_P35_crosshead_LF.tex",
        "intake/frozen_producer_package_v002/build/zh-Hans-CN-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v002.tex",
        "intake/frozen_producer_package_v002/build/zh-Hans-CN-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v002.pdf",
        "intake/frozen_producer_package_v002/build/zh-Hant-controlled-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_v002.tex",
        "intake/frozen_producer_package_v002/build/zh-Hant-controlled-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_v002.pdf",
        "evidence/P35_V002_SUBSTANTIVE_RECHECK_RECORD.json",
        "evidence/P35_HANT_INDEPENDENT_AUDIT_v002.json",
        "evidence/P35_HANT_CHECKER_CANDIDATE_BUILD_RECORD_v003.json",
        "findings/P35_V002_FINDING_DISPOSITION.jsonl",
        "findings/P35_HANT_F015_CORRECTION_DIFF.patch",
        "structural/P35_TEX_AUDIT_SUMMARY.json",
        "structural/hant_candidate_v003/P35_TEX_AUDIT_SUMMARY.json",
        "build/P35_V002_CHECKER_BUILD_RECORD.json",
        "build/P35_V002_PDF_TEXT_METADATA_VERIFICATION.json",
        "build/hans_exact/Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v002.pdf",
        "build/hant_frozen_exact/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_v002.pdf",
        "candidate/zh-Hant-controlled/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_checker_candidate_v003.tex",
        "build/hant_candidate_v003/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_checker_candidate_v003.pdf",
        "render/P35_V002_RENDER_RECORD.json",
        "render/P35_V002_VISUAL_QA_LEDGER.jsonl",
        "return/sealed_member_snapshots/ZHCHK-NOETHER-P35-V002-RETURN-001/P35_FINDING_LEDGER.jsonl",
        "return/sealed_member_snapshots/ZHCHK-NOETHER-P35-V002-RETURN-001/P35_DIFFICULTY_FAILURE_LEDGER.jsonl",
        "return/sealed_member_snapshots/ZHCHK-NOETHER-P35-V002-RETURN-001/CHECKER_DECISION_LOG.md",
        "records/audit_p35_hant_v002.py",
        "records/audit_p35_tex_v002.py",
        "records/build_hant_checker_candidate_v003.py",
        "records/finalize_p35_v002_build_render_records.py",
        "records/finalize_p35_v002_substantive_recheck.py",
        "records/verify_p35_v002_pdfs.py",
        "records/seal_p35_v002_return.py",
        "records/verify_p35_v002_return.py",
        "return/P35_V002_CHECKER_RETURN_SUMMARY.md",
        "return/P35_V002_CHECKER_RETURN_RECEIPT.json",
    ]

    receipt = {
        "schema_version": "1.0.0",
        "receipt_id": "ZHCHK-NOETHER-P35-V002-RETURN-001",
        "record_type": "independent_checker_hash_pinned_return_receipt",
        "recorded_at": RECORDED_AT,
        "paper_id": "NOETHER-P35",
        "state": "REJECTED_HANT_ONLY_REBUILD_AND_NEW_FROZEN_REHANDOFF_REQUIRED",
        "custody": {
            "producer_root": str(PRODUCER),
            "handoff": fact(FROZEN / "CHINESE_PRODUCER_CORRECTED_RETURN_AND_CHECKER_REHANDOFF.md"),
            "manifest": fact(FROZEN / "SHA256SUMS.txt"),
            "freeze_verification": fact(RECHECK / "intake/NOETHER_P35_ZH_V002_PRODUCER_FREEZE_VERIFICATION_20260804.json"),
            "external_manifest_replay": external_replay,
            "checker_snapshot_manifest_replay": snapshot_replay,
            "producer_files_mutated_by_checker": False,
        },
        "authority": {
            "binder_id": "NOETH-DE-BINDER-P35-20260804-001",
            "source_native_sha256": "2E205B2C51B9093FC61C77A9A1DF1C3399FCF098706CEC69134400F1ECC8E491",
            "source_lf_sha256": "DAED6EF21C297425F018C0AE6B23BC5BDD05C0B86984B3FC25FB5937DCBEBD6A",
            "pointer_v004_route_metadata_sha256": "A1C62FDACAA34DFC1B806DC18258F2E732539F7AE9D85AA4BD9E1067B8749D9F",
        },
        "disposition": {
            "package": "rejected_target_only_Hant_rebuild_and_new_frozen_rehandoff_required",
            "zh_Hans_CN_v002": "accepted",
            "frozen_controlled_generic_Hant_v002": "rejected_ZHCHK-P35-F015",
            "checker_controlled_generic_Hant_candidate_v003": "validated_correction_candidate_nonregional",
            "producer_next_action": "integrate F015 Hant-only scanner/correction; serial rebuild; new immutable manifest and re-handoff; leave accepted Hans unchanged",
        },
        "finding_disposition": {
            "F001_F011": "resolved_and_accepted_in_exact_Hans_v002",
            "F012": "exact_loci_resolved_but_Hant_rejected_under_distinct_F015",
            "F013": "unresolved_no_action_no_German_packet",
            "F014": "exact_loci_resolved_but_Hant_rejected_under_distinct_F015",
            "F015": "confirmed_major_tooling_defect_producer_Hant_rejected",
        },
        "F015": {
            "target": fact(hant_tex),
            "target_lines": {"false_opener_line": 244, "false_span_end_line": 272, "visible_simplified_lines": [245, 269]},
            "cause": "second backslash in \\\\[0.6em] was misread as a \\[ opener and protected through the genuine closer",
            "false_protected_span_characters": 2075,
            "unchanged_complete_lines": {"count": 28, "bytes": 3901, "sha256": "FB5301141DA8681A6551AC92E85BA8C1B96279781D4005C42FD9ED79D02C1098"},
            "correction_diff": fact(correction_diff),
            "checker_candidate_tex": fact(candidate_tex),
            "checker_candidate_pdf": fact(candidate_pdf),
        },
        "accepted_hans": {"tex": fact(hans_tex), "pdf": fact(hans_pdf), "body_bytes": 29808, "body_sha256": "54061274DFDE806F491EE424277886ED4C4CEEF3F7E0315DFD1039AACF69F18A"},
        "rejected_hant": {"tex": fact(hant_tex), "pdf": fact(hant_pdf)},
        "validation": {
            "substantive_record": fact(RECHECK / "evidence/P35_V002_SUBSTANTIVE_RECHECK_RECORD.json"),
            "finding_dispositions": fact(RECHECK / "findings/P35_V002_FINDING_DISPOSITION.jsonl"),
            "hant_audit": fact(RECHECK / "evidence/P35_HANT_INDEPENDENT_AUDIT_v002.json"),
            "candidate_build_record": fact(RECHECK / "evidence/P35_HANT_CHECKER_CANDIDATE_BUILD_RECORD_v003.json"),
            "structural_hans": fact(RECHECK / "structural/P35_TEX_AUDIT_SUMMARY.json"),
            "structural_candidate_hant": fact(RECHECK / "structural/hant_candidate_v003/P35_TEX_AUDIT_SUMMARY.json"),
            "serial_build_record": fact(RECHECK / "build/P35_V002_CHECKER_BUILD_RECORD.json"),
            "pdf_text_metadata_verification": fact(RECHECK / "build/P35_V002_PDF_TEXT_METADATA_VERIFICATION.json"),
            "render_record": fact(RECHECK / "render/P35_V002_RENDER_RECORD.json"),
            "visual_qa_ledger": fact(RECHECK / "render/P35_V002_VISUAL_QA_LEDGER.jsonl"),
            "all_assertions_pass": True,
        },
        "append_only_snapshots": {
            "finding_ledger": fact(SNAPSHOT / "P35_FINDING_LEDGER.jsonl"),
            "difficulty_ledger": fact(SNAPSHOT / "P35_DIFFICULTY_FAILURE_LEDGER.jsonl"),
            "decision_log": fact(SNAPSHOT / "CHECKER_DECISION_LOG.md"),
        },
        "summary": fact(summary_path),
        "manifest_policy": {
            "path": str(manifest_path),
            "selected_member_count": len(selected),
            "self_excluded": True,
            "verifier_and_final_seal_excluded_to_avoid_circularity": True,
            "no_whole_checker_tree_extra_file_claim": True,
        },
        "scope_guards": {
            "new_corpus_translation": False,
            "German_finding_packet": None,
            "German_mutated": False,
            "SGA_touched": False,
            "Hant_claim": "controlled generic Traditional script only; not TW/HK/MO localization",
        },
    }
    write_json(receipt_path, receipt)

    assert len(selected) == len(set(selected))
    lines = [
        "# Noether Paper 35 Chinese independent-checker v002 selected return manifest",
        "# SHA256  BYTES  RELATIVE_PATH",
        "# SHA256SUMS.txt, P35_V002_RETURN_VERIFICATION.json, and P35_V002_RETURN_SEAL.json are excluded to avoid circularity.",
    ]
    for rel in sorted(selected):
        member = RECHECK / Path(rel)
        member_fact = fact(member)
        lines.append(f"{member_fact['sha256']}  {member_fact['bytes']}  {Path(rel).as_posix()}")
    write_utf8(manifest_path, "\n".join(lines) + "\n")

    print(
        json.dumps(
            {
                "receipt": fact(receipt_path),
                "summary": fact(summary_path),
                "manifest": fact(manifest_path),
                "manifest_entries": len(selected),
                "custody_all_pass": True,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

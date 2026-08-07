from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path


HERE = Path(__file__).resolve().parent
CHECK_ROOT = HERE.parent
P44 = CHECK_ROOT / "paper44" / "rb1"


def identity(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    return {
        "path": str(path),
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest().upper(),
    }


def require_identity(path: Path, size: int, digest: str) -> None:
    actual = identity(path)
    if actual["bytes"] != size or actual["sha256"] != digest:
        raise RuntimeError(f"identity mismatch: {actual}")


def write_once(path: Path, payload: dict[str, object]) -> None:
    if path.exists():
        raise RuntimeError(f"refusing to overwrite {path.name}")
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def main() -> None:
    checked_at = datetime.now(timezone.utc).isoformat()

    require_identity(
        HERE / "reader.tex",
        1_871_385,
        "910399C8CB6A8A3CC0BE40638C23AFD496C642ACC63127E3AE812CACEF599E33",
    )
    require_identity(
        HERE / "reader.pdf",
        2_547_819,
        "87FE104B4AAF83CA2A5F6D41154D2596A2E3187752F84025F8E2EF976F89C7CE",
    )
    require_identity(
        HERE / "reader.txt",
        1_881_280,
        "EEB76FE0B0B317DEF209F853B8A8FF7C7720F8ED10F6A30703350DCA99237DD2",
    )
    require_identity(
        P44 / "p44.tex",
        156_522,
        "8B94ED0C54A9C7DA1C6A8E8E02F33F4FBA3ECAB4E783CDFF289F3172AE75A76F",
    )

    diff = json.loads((HERE / "diff.json").read_text(encoding="utf-8"))
    visual_mechanical = json.loads((HERE / "vis.json").read_text(encoding="utf-8"))
    comparison = json.loads((HERE / "cmp2.json").read_text(encoding="utf-8"))
    post44_qa = json.loads((P44 / "qa.json").read_text(encoding="utf-8"))
    if diff["output"]["sha256"] != identity(HERE / "reader.tex")["sha256"]:
        raise RuntimeError("diff record does not pin final reader.tex")
    if not visual_mechanical["mechanical_screen"]["all_pass"]:
        raise RuntimeError("mechanical visual screen did not pass")
    if not comparison["all_pass"] or comparison["render"]["changed_pages"] != [380, 383]:
        raise RuntimeError("source-repair render comparison did not pass")
    if not post44_qa["all_pass"]:
        raise RuntimeError("Post44 formula/structure QA did not pass")

    bad_log_pattern = re.compile(
        r"Undefined control sequence|LaTeX Warning|Package .* Warning|"
        r"Overfull|Underfull|Missing character|Emergency stop|Fatal error"
    )
    pass2_text = (HERE / "pass2.txt").read_text(encoding="utf-8", errors="replace")
    log_text = (HERE / "reader.log").read_text(encoding="utf-8", errors="replace")
    if bad_log_pattern.search(pass2_text) or bad_log_pattern.search(log_text):
        raise RuntimeError("final pass-2 diagnostic screen found a prohibited hit")

    page_files = sorted((HERE / "img").glob("p-*.png"))
    sheet_files = sorted((HERE / "sheet").glob("s*.jpg"))
    if len(page_files) != 424 or len(sheet_files) != 27:
        raise RuntimeError("render/contact-sheet count mismatch")

    build = {
        "record_id": "ZHCHK-NOETHER-CUM-R4-BUILD-001",
        "checked_at": checked_at,
        "engine": "XeLaTeX via MiKTeX",
        "mode": "serial",
        "passes": [
            {
                "pass": 1,
                "exit_code": 0,
                "command": "xelatex -interaction=nonstopmode -halt-on-error -file-line-error -recorder reader.tex",
                "log": identity(HERE / "pass1.txt"),
            },
            {
                "pass": 2,
                "exit_code": 0,
                "command": "xelatex -interaction=nonstopmode -halt-on-error -file-line-error -recorder reader.tex",
                "log": identity(HERE / "pass2.txt"),
            },
        ],
        "page_count": 424,
        "artifacts": {
            "tex": identity(HERE / "reader.tex"),
            "pdf": identity(HERE / "reader.pdf"),
            "text": identity(HERE / "reader.txt"),
            "pdfinfo": identity(HERE / "pdfinfo.txt"),
            "latex_log": identity(HERE / "reader.log"),
        },
        "pass2_diagnostic_screen": {
            "patterns": bad_log_pattern.pattern,
            "hits": 0,
            "pass": True,
        },
        "failed_builds_preserved": ["f1/", "f2/", "f3/"],
        "all_pass": True,
    }
    write_once(HERE / "build.json", build)

    visual = {
        "record_id": "ZHCHK-NOETHER-CUM-R4-VISUAL-001",
        "checked_at": checked_at,
        "pdf_skill_workflow": {
            "fresh_render_engine": "Poppler pdftoppm",
            "dpi": 110,
            "rendered_pages": 424,
            "contact_sheets": 27,
            "mechanical_record": identity(HERE / "vis.json"),
            "mechanical_result": "PASS: zero blank, edge, or unexpected-dimension suspects; pages 41-42 are the two allowed landscape tables",
        },
        "independent_page_audits": [
            {
                "checker": "root/r4_vis_a",
                "pages": "1-141",
                "result": "PASS every page; no blank, crop, overlap, tofu, formula, header/footer, or folio defect",
                "special": "pages 41-42 landscape tables complete; sparse pages 63, 103, 113 intentional",
            },
            {
                "checker": "root/r4_vis_b",
                "pages": "142-282",
                "result": "PASS every page; no actionable visual defect",
                "special": "sparse article endings independently distinguished from blank pages",
            },
            {
                "checker": "root/r4_vis_c",
                "pages": "283-424",
                "result": "PASS every page; P38, complete Post44, Post45 boundary, and terminal material all clean",
                "special": "Post44 pages 372-414 complete; P45 begins page 415 without omission, duplication, or intervening blank page",
            },
            {
                "checker": "root/main",
                "pages": "1-424",
                "result": "PASS from all 27 contact sheets plus full-resolution review of unusual and changed pages",
                "special": "final source-repair pages 380 and 383 reopened at full resolution and passed",
            },
        ],
        "source_repair_comparison": identity(HERE / "cmp2.json"),
        "source_repair_result": "422 page rasters byte-identical to the already inspected predecessor; only pages 380 and 383 changed, exactly at the three repaired loci, and both pass full-resolution reinspection",
        "all_pages_visually_inspected": True,
        "all_pass": True,
    }
    write_once(HERE / "visual.json", visual)

    result = {
        "return_id": "ZHCHK-NOETHER-CUM-R4-RETURN-001",
        "checked_at": checked_at,
        "disposition": "ACCEPTED_CURRENT_DAY_SUCCESSOR",
        "release_state": "not final until two later distinct-calendar-day checks pass",
        "scope": "PRC-oriented Simplified Chinese cumulative reader; P01-P43, complete Post44, Post45, and post-bibliographic matter",
        "predecessor": {
            "tex_bytes": 1_811_029,
            "tex_sha256": "50B212EA04061921607E13CB7B367DEBF4AAF2449CF5614F931E74AA1B5A5338",
            "pdf_bytes": 2_489_062,
            "pdf_sha256": "86031C4790433915D3882A9DEFFFD481F2743F897E0FFE49B5AAD300D27F9B62",
            "pages": 413,
        },
        "authority": {
            "pointer_id": "NOETH-DE-AUTH-v043-20260806",
            "pointer_bytes": 70_478,
            "pointer_sha256": "D625C79008B87863D452E35FE4A4DD36D1F961967D12A37560C77897DCD94FF1",
            "edition": "ED0007",
            "edition_bytes": 2_153_563,
            "edition_sha256": "746FA01AC33CBC0BCCBF1E740413E5DC3E74CE30295B7A4794943F5198F73355",
            "post44_lf_lines": "21003-23741 inclusive",
            "post44_lf_bytes": 172_342,
            "post44_lf_sha256": "7F2AE56326328DA8DD12453C889D767683AC96EB4677CBBEF00C8FEAAB4FE3F7",
            "post44_ed0006_ed0007_relation": "byte-identical after LF normalization",
        },
        "accepted_changes": [
            {
                "unit": "P10",
                "result": "10 algebraische Basis senses corrected to 超越基 and 6 Basiszahl basis-element senses corrected to 基元素",
                "candidate_lf_sha256": "4C90B30A4FD3913700B2F181FED52427E501C3EFC1F274989A9A2CA26DEC9DCE",
            },
            {
                "unit": "P38",
                "result": "single terminology defect 主理想基数 corrected to 主理想生成元",
            },
            {
                "unit": "Post44",
                "result": "obsolete incomplete 1,951-line block replaced by the complete checked 2,730-line translation",
                "target_body": identity(P44 / "p44.tex"),
                "formula_structure_qa": identity(P44 / "qa.json"),
            },
            {
                "unit": "Post44 source-backed target repairs",
                "result": "ZHCHK-DE-P44-001, -002, and -003 realized at b.tex lines 79, 108, and 293-294 from primary-page evidence; German itself remains untouched",
                "packets": [
                    identity(CHECK_ROOT / "paper44" / "de" / "f1.json"),
                    identity(CHECK_ROOT / "paper44" / "de" / "f2.json"),
                    identity(CHECK_ROOT / "paper44" / "de" / "f3.json"),
                ],
            },
            {
                "unit": "PDF metadata",
                "result": "inherited rebase r1 label corrected to rebase r4; a prior 424-raster replay proved the metadata-only rebuild changed no rendered content",
            },
        ],
        "outputs": {
            "tex": identity(HERE / "reader.tex"),
            "pdf": identity(HERE / "reader.pdf"),
            "text": identity(HERE / "reader.txt"),
            "pages": 424,
        },
        "validation": {
            "integration_diff": identity(HERE / "diff.json"),
            "build": identity(HERE / "build.json"),
            "visual": identity(HERE / "visual.json"),
            "mechanical_visual": identity(HERE / "vis.json"),
            "source_repair_render_compare": identity(HERE / "cmp2.json"),
            "failed_probe_ledger": identity(HERE / "fail.jsonl"),
        },
        "recovery_methodology": identity(CHECK_ROOT / "METHOD_REUSE.md"),
        "localization_limits": {
            "zh_Hans_CN": "present; PRC-oriented",
            "zh_Hans_SG": "absent",
            "generic_Hant_cumulative": "not claimed by this return",
            "TW_HK_MO": "not claimed",
        },
        "german_mutated": False,
        "german_packet_transport": "three schema-valid durable packets written; cross-task transport call did not return before bounded termination, so delivery readback remains pending",
        "sga": "held and untouched",
        "later_day_checks_remaining": 2,
        "accepted": True,
    }
    write_once(HERE / "return.json", result)

    print(
        json.dumps(
            {
                "build": identity(HERE / "build.json"),
                "visual": identity(HERE / "visual.json"),
                "return": identity(HERE / "return.json"),
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()

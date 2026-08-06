#!/usr/bin/env python3
"""Run source, structure, build, page, text, and visual gates for v038."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parents[3]
LIVE_POINTER = (
    WORKSPACE
    / "03_projects"
    / "noether"
    / "07_german_canon_control"
    / "CURRENT_GERMAN_AUTHORITY_POINTER.json"
)
EVIDENCE = ROOT / "evidence"
RELEASE_EVIDENCE = ROOT / "release" / "evidence"
SOURCE = ROOT / "release" / "source"
PDF = ROOT / "release" / "pdf"
TARGETS = ("ru", "uk", "isv", "isv-cy")
EXPECTED_POINTER_ID = "NOETH-DE-AUTH-v038-20260805"
EXPECTED_POINTER_SHA256 = "666FCB863C8599778BB1B48DCD0D4E444D6486133B7FE703E6CDE073F15FFBAE"
EXPECTED_AUTHORITY_ID = "NOETH-DE-ED-0005"
EXPECTED_AUTHORITY_SHA256 = "1A44F967B29972E8F99E5C323A479162AD82A23FC457395915A4BB9DDF51AD41"
OLD_P06_FORMULA = r"\Psi(z,u)=x_1^2z^2-x_1^2u_1^2-2x_1^2x_2u_1u_2-x_1^2x_2^2u_2^2."
NEW_P06_FORMULA = r"\Psi(z,u)=x_1^2z^2-x_1^4u_1^2-2x_1^3x_2u_1u_2-x_1^2x_2^2u_2^2."

CRITICAL = {
    "BOOK_S01": [r"\nrightarrow"],
    # Six explicit three-column ellipsis rows are the fragile S12 matrix
    # witness; the authority uses \cdots rows, not \vdots.
    "BOOK_S12": [r"\cdots & \cdots & \cdots"],
    "BOOK_S13": [r"\mathfrak K_i"],
    "BOOK_S14": [r"\equiv"],
    "BOOK_S15": [r"\equiv"],
    "BOOK_S24": [r"\mathfrak K_{r\Gamma}"],
    "BOOK_S31": [r"\cong"],
}
FATAL_LOG_PATTERNS = (
    "! LaTeX Error",
    "Undefined control sequence",
    "Emergency stop",
    "Fatal error",
    "TeX capacity exceeded",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def file_record(path: Path) -> dict:
    return {"path": path.resolve().as_posix(), "bytes": path.stat().st_size, "sha256": sha256(path)}


def book_units(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8-sig")
    result = {}
    for unit in CRITICAL:
        match = re.search(
            rf"(?ms)^% BEGIN {re.escape(unit)}\s*$\n(.*?)^% END {re.escape(unit)}\s*$",
            text,
        )
        if not match:
            raise RuntimeError(f"missing {unit} markers in {path}")
        result[unit] = match.group(1)
    return result


def extract_pdf_text(pdf: Path, output: Path) -> tuple[str, dict]:
    output.parent.mkdir(parents=True, exist_ok=True)
    completed = subprocess.run(
        ["pdftotext", "-layout", str(pdf.resolve()), str(output.resolve())],
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if completed.returncode:
        raise RuntimeError(f"pdftotext failed for {pdf}: {completed.stderr}")
    text = output.read_text(encoding="utf-8", errors="replace")
    return text, {
        **file_record(output),
        "characters": len(text),
        "non_whitespace_characters": len(re.sub(r"\s+", "", text)),
        "replacement_characters": text.count("\ufffd"),
        "form_feed_pages": text.count("\f"),
    }


def extract_page_text(pdf: Path, page: int) -> str:
    completed = subprocess.run(
        ["pdftotext", "-f", str(page), "-l", str(page), "-layout", str(pdf.resolve()), "-"],
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if completed.returncode:
        raise RuntimeError(f"pdftotext page failed for {pdf} page {page}: {completed.stderr}")
    return completed.stdout


def check(condition: bool, code: str, detail: object, errors: list[dict], checks: list[dict]) -> None:
    record = {"code": code, "pass": bool(condition), "detail": detail}
    checks.append(record)
    if not condition:
        errors.append(record)


def main() -> int:
    checks: list[dict] = []
    errors: list[dict] = []
    human = json.loads((EVIDENCE / "human_unit_validation.json").read_text(encoding="utf-8"))
    assembly = json.loads((RELEASE_EVIDENCE / "source_assembly.json").read_text(encoding="utf-8"))
    build = json.loads((RELEASE_EVIDENCE / "build_manifest.json").read_text(encoding="utf-8"))
    structural = json.loads((RELEASE_EVIDENCE / "structural_index_validation.json").read_text(encoding="utf-8"))
    visual = json.loads((RELEASE_EVIDENCE / "visual_evidence_validation.json").read_text(encoding="utf-8"))
    inherited = json.loads(
        (RELEASE_EVIDENCE / "inherited_continuation_audit.json").read_text(encoding="utf-8")
    )
    reconciliation = json.loads((EVIDENCE / "authority_reconciliation_v038.json").read_text(encoding="utf-8"))
    live_pointer = json.loads(LIVE_POINTER.read_text(encoding="utf-8-sig"))

    check(
        live_pointer["pointer_id"] == EXPECTED_POINTER_ID and sha256(LIVE_POINTER) == EXPECTED_POINTER_SHA256,
        "live-pointer-still-v038",
        {"pointer_id": live_pointer["pointer_id"], **file_record(LIVE_POINTER)},
        errors,
        checks,
    )
    check(
        reconciliation["status"] == "PASS_BOUNDED_AUTHORITY_AND_BASE_RECONCILIATION",
        "authority-reconciliation-v038",
        reconciliation["status"],
        errors,
        checks,
    )
    check(
        inherited["pass"],
        "inherited-title-post45-postbib-reconciliation",
        {
            "pass": inherited["pass"],
            "errors": inherited["errors"],
            "source_backed_german_authority_discrepancy": inherited[
                "source_backed_german_authority_discrepancy"
            ],
        },
        errors,
        checks,
    )

    for target in ("ru", "uk", "isv"):
        summary = human["summary"][target]
        check(
            summary["units"] == 31 and summary["pass"] == 31 and summary["error_count"] == 0,
            f"human-unit-structure-{target}",
            summary,
            errors,
            checks,
        )
    check(
        assembly["cyrillic_projection_validation"]["pass"],
        "cyrillic-projection",
        assembly["cyrillic_projection_validation"],
        errors,
        checks,
    )
    check(
        len(assembly["cyrillic_static_projection_validation"]) == 2
        and all(item["pass"] for item in assembly["cyrillic_static_projection_validation"]),
        "cyrillic-static-projections",
        assembly["cyrillic_static_projection_validation"],
        errors,
        checks,
    )

    base_formula_results = []
    for target in TARGETS:
        base = SOURCE / f"base-papers1-43-{target}.tex"
        text = base.read_text(encoding="utf-8-sig")
        item = {
            "target": target,
            "source": file_record(base),
            "accepted_formula_count": text.count(NEW_P06_FORMULA),
            "superseded_formula_count": text.count(OLD_P06_FORMULA),
            "accepted_H_star_nonzero_count": text.count(r"H^*(\xi)\ne0"),
            "bare_H_nonzero_count": text.count(r"H(\xi)\ne0"),
        }
        base_formula_results.append(item)
        check(
            item["accepted_formula_count"] == 1
            and item["superseded_formula_count"] == 0
            and item["accepted_H_star_nonzero_count"] >= 2
            and item["bare_H_nonzero_count"] == 0,
            f"p06-ed0005-base-{target}",
            item,
            errors,
            checks,
        )
    check(structural["pass"], "structural-index", structural, errors, checks)
    check(
        visual["pass"] and visual["record_count"] == visual["reviewed_pass_count"],
        "visual-evidence-index-and-review",
        {"pass": visual["pass"], "records": visual["record_count"], "reviewed_pass": visual["reviewed_pass_count"]},
        errors,
        checks,
    )

    # Explicit current-authority critical loci on every final editable/reader source.
    authority_units = {
        unit: (ROOT / "authority_units" / f"{unit}.texfrag").read_text(encoding="utf-8-sig")
        for unit in CRITICAL
    }
    critical_results = []
    for target in TARGETS:
        units = book_units(SOURCE / f"44-book-{target}.tex")
        for unit, tokens in CRITICAL.items():
            for token in tokens:
                expected = authority_units[unit].count(token)
                observed = units[unit].count(token)
                item = {"target": target, "unit": unit, "token": token, "expected": expected, "observed": observed}
                critical_results.append(item)
                check(expected > 0 and observed == expected, f"critical-{target}-{unit}-{token}", item, errors, checks)

    title_results = []
    for target in TARGETS:
        text = (SOURCE / f"44-book-{target}.tex").read_text(encoding="utf-8-sig")
        title_line = next(line for line in text.splitlines() if line.startswith(r"\tocsec{25}"))
        item = {
            "target": target,
            "line": title_line,
            "contains_current_K_r": r"\mathfrak K_r" in title_line,
            "contains_old_R_r": r"\mathfrak R_r" in title_line,
        }
        title_results.append(item)
        check(item["contains_current_K_r"] and not item["contains_old_R_r"], f"title-toc25-{target}", item, errors, checks)

    log_results = []
    for path in sorted((ROOT / "release" / "build").rglob("*.log")):
        text = path.read_text(encoding="utf-8", errors="replace")
        hits = [pattern for pattern in FATAL_LOG_PATTERNS if pattern.casefold() in text.casefold()]
        item = {**file_record(path), "fatal_patterns": hits}
        log_results.append(item)
        check(not hits, f"build-log-{path.relative_to(ROOT).as_posix()}", item, errors, checks)

    build_results = []
    text_results = []
    for record in build["cumulative_records"]:
        target = record["target"]
        page_sum_ok = record["input_page_sum"] == record["pdf"]["pages"]
        check(page_sum_ok, f"page-sum-{target}", record, errors, checks)
        pdf = Path(record["pdf"]["path"])
        extracted_path = RELEASE_EVIDENCE / "text" / f"noether-{target}-v038.txt"
        text, extraction = extract_pdf_text(pdf, extracted_path)
        text_results.append({"target": target, "pdf": record["pdf"], "extraction": extraction})
        check(
            extraction["non_whitespace_characters"] > 10000 and extraction["replacement_characters"] == 0,
            f"text-extraction-{target}",
            extraction,
            errors,
            checks,
        )
        boundaries = []
        running = 0
        for input_record in record["inputs"]:
            running += input_record["pages"]
            sample = extract_page_text(pdf, running)
            boundaries.append({"page": running, "non_whitespace_characters": len(re.sub(r"\s+", "", sample))})
        check(
            all(item["non_whitespace_characters"] > 20 for item in boundaries),
            f"component-boundary-text-{target}",
            boundaries,
            errors,
            checks,
        )
        build_results.append({"target": target, "page_sum_ok": page_sum_ok, "boundaries": boundaries})

    report = {
        "schema": "noether-slavic-v038-release-qa/1.0",
        "generated_at": datetime.now().astimezone().isoformat(),
        "pass": not errors,
        "authority": {
            "pointer_id": EXPECTED_POINTER_ID,
            "pointer_sha256": EXPECTED_POINTER_SHA256,
            "authority_id": EXPECTED_AUTHORITY_ID,
            "authority_sha256": EXPECTED_AUTHORITY_SHA256,
        },
        "scope": "four cumulative v038 Slavic readers, rebuilt numbered-paper bases, and exact post-P43 editable source components",
        "checks": checks,
        "errors": errors,
        "critical_loci": critical_results,
        "numbered_paper_p06_loci": base_formula_results,
        "title_toc25": title_results,
        "build_results": build_results,
        "build_log_results": log_results,
        "text_results": text_results,
        "review_caveat": "Model-authored RU/UK/ISV translations; no native-speaker review or original-print reaudit claimed. Cyrillic ISV is a deterministic reader projection.",
    }
    output = RELEASE_EVIDENCE / "qa_report.json"
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"pass": report["pass"], "checks": len(checks), "errors": len(errors), "output": {**file_record(output)}}))
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

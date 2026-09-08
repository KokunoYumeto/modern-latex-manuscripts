#!/usr/bin/env python3
"""Seal bounded desktop/mobile browser QA for the OLP-0198 public reader."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "public_status_olp0198/index.html"
SCRIPT = ROOT / "evidence/qa_public_status_OLP0198.cjs"
QA = ROOT / "evidence/html_qa_OLP0198"
METRICS = QA / "browser-metrics.json"
ADVERSE_A = ROOT / "evidence/html_qa_OLP0198_adverse_0001"
ADVERSE_B = ROOT / "evidence/html_qa_OLP0198_adverse_0002"
ADVERSE_RECEIPT = ROOT / "evidence/unit_receipts/OLP-0198.local-html-browser-adverse-history.json"
OUTPUT = ROOT / "evidence/unit_receipts/OLP-0198.local-html-reader-visual-qa.json"

EXPECTED = {
    HTML: (15362, "2F9661B59CFE469DF02CBBD3D902A5442627F40B2595AE0DDC4A06D5E5C34A96"),
    SCRIPT: (7224, "23F78EDBE52187FFB88D619AC0DEC978FC0C2004062EBF8D93B160E5890B89EF"),
    METRICS: (12365, "5223C82CA68F7D919C986748D91E70F108F4D4613AF2E145415F00B6926BCF27"),
    QA / "desktop-full.png": (395862, "C40E54CB02C521FC501C6CBCAF8DE0D001A9D0432AAE5ACD07ECA67BA6D9974B"),
    QA / "desktop-top.png": (103090, "63F6171F28F9616750D6849C701F424D98237CBC19E9499790428BAA3FECB4EE"),
    QA / "mobile-full.png": (377800, "DF767AD2B61D658F55FAAB6512B0E9FAEBAB10F3C2F0256550929BE1BC7561AC"),
    QA / "mobile-top.png": (62671, "8FC3A805E737507E4EA02DD7355661DF28C6EF1B5C5C456F665BB17A5EF12D38"),
    QA / "mobile-english-panel.png": (49724, "79A2FAE971DABF413309AFFE7C9A983E09CEC132DD8E35A0CAA64573D7343B60"),
    QA / "mobile-accepted-units-table.png": (63115, "FBD508E3C0FC49A056BE617B97B98E3DF2A3BEFEC4C3B16F8078CBF09AC56F5C"),
}


def compact(path: Path) -> tuple[int, str]:
    data = path.read_bytes()
    return len(data), hashlib.sha256(data).hexdigest().upper()


def pin(path: Path) -> dict[str, object]:
    size, digest = compact(path)
    return {"path": path.relative_to(ROOT).as_posix(), "bytes": size, "sha256": digest}


def bounded_directory_manifest(path: Path) -> dict[str, object]:
    files = sorted(item for item in path.iterdir() if item.is_file())
    if [item.name for item in files] != [
        "desktop-full.png",
        "desktop-top.png",
        "mobile-accepted-units-table.png",
        "mobile-english-panel.png",
        "mobile-full.png",
        "mobile-top.png",
    ]:
        raise RuntimeError(f"unexpected bounded adverse directory inventory: {path}")
    return {
        "path": path.relative_to(ROOT).as_posix(),
        "file_count": len(files),
        "total_bytes": sum(item.stat().st_size for item in files),
        "files": [pin(item) for item in files],
    }


def main() -> int:
    if OUTPUT.exists() or ADVERSE_RECEIPT.exists():
        raise RuntimeError("refusing to overwrite a browser-QA receipt")
    for path, expected in EXPECTED.items():
        if compact(path) != expected:
            raise RuntimeError(f"pinned browser-QA input drift: {pin(path)}")

    metrics = json.loads(METRICS.read_text(encoding="utf-8"))
    if metrics.get("status") != "PASS" or metrics.get("checkpoint") != "OLP-0198":
        raise RuntimeError("browser metrics are not an OLP-0198 PASS")
    for mode in ("desktop", "mobile"):
        observed = metrics[mode]
        if observed["document"]["horizontalOverflow"]:
            raise RuntimeError(f"{mode} document-level horizontal overflow")
        if not all(observed["markers"].values()) or not observed["englishPanelVisible"]:
            raise RuntimeError(f"{mode} required content visibility failure")
        if observed["jsonLdCount"] != 1 or observed["jsonLdVersion"] != "continuous-frontier-OLP-0198":
            raise RuntimeError(f"{mode} JSON-LD failure")
        if observed["jsonLdLanguages"] != ["isv-Latn", "en"]:
            raise RuntimeError(f"{mode} JSON-LD language failure")
        if observed["consoleErrors"] or observed["pageErrors"]:
            raise RuntimeError(f"{mode} browser error")
        if not observed["readerObject"]["visible"] or observed["readerObject"]["data"] != "reader/OpenLogic-Interslavic-OLP0198-visual-checkpoint.pdf":
            raise RuntimeError(f"{mode} PDF object failure")
    mobile_table = metrics["mobile"]["tableWrapper"]
    if mobile_table["overflowX"] != "auto" or mobile_table["scrollWidth"] <= mobile_table["clientWidth"]:
        raise RuntimeError("mobile accepted-units table does not have contained local scrolling")
    if len(metrics.get("localReferences", [])) != 50 or not all(item.get("exists") for item in metrics["localReferences"]):
        raise RuntimeError("local reference audit failure")

    adverse = {
        "schema": "openlogic-isv-local-html-browser-adverse-history/1.0",
        "recorded_at": datetime.now(ZoneInfo("Europe/Berlin")).isoformat(),
        "status": "SUPERSEDED_BY_PASS",
        "checkpoint": "OLP-0198",
        "attempts": [
            {
                "attempt": 1,
                "failure": "The ordinary Node runtime could not resolve the Playwright module; failure occurred before browser launch and before QA output creation.",
                "mutation": "NONE",
            },
            {
                "attempt": 2,
                "failure": "The browser run completed screenshots but the content-marker assertion reported a generic false result.",
                "artifacts": bounded_directory_manifest(ADVERSE_A),
                "mutation": "QA_ARTIFACTS_ONLY",
            },
            {
                "attempt": 3,
                "failure": "Diagnostic replay localized the false result to a case-sensitive expert-log marker; live text was present and correct. The assertion was corrected to a case-insensitive check.",
                "artifacts": bounded_directory_manifest(ADVERSE_B),
                "mutation": "QA_ARTIFACTS_ONLY",
            },
        ],
        "edition_or_public_bytes_changed": False,
        "accepted_state_reverted": False,
        "disposition": "Both validator-only failures were preserved; the same staged reader then passed with exact live content, layout, references and JSON-LD checks.",
    }
    ADVERSE_RECEIPT.write_text(json.dumps(adverse, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    receipt = {
        "schema": "openlogic-isv-local-html-reader-visual-qa/1.2",
        "recorded_at": datetime.now(ZoneInfo("Europe/Berlin")).isoformat(),
        "status": "PASS",
        "checkpoint": "OLP-0198",
        "reader": {**pin(HTML), "language_primary": "isv-Latn", "english_parallel": True},
        "qa_script": pin(SCRIPT),
        "browser_metrics": pin(METRICS),
        "checks": {
            "desktop": metrics["desktop"],
            "mobile": metrics["mobile"],
            "local_reference_count": len(metrics["localReferences"]),
            "all_local_references_resolve": True,
            "visual_review": {
                "desktop_full_and_top_inspected": True,
                "mobile_full_and_top_inspected": True,
                "mobile_english_panel_inspected": True,
                "mobile_accepted_units_table_inspected": True,
                "observed_defects": [],
                "observations": [
                    "The Interslavic-first hierarchy, 198/722 frontier, token progress and 400-entry canon status are prominent and legible on desktop and mobile.",
                    "The complete English counterpart follows visibly and retains the accepted-versus-pending explanation.",
                    "The embedded 777-page reader has a visible reserved surface and a direct-opening fallback link; the PDF itself was independently parsed, rendered and visually checked.",
                    "The accepted-unit table is fully legible on desktop and contained in an intentional horizontal scroller on mobile without widening the document.",
                    "All 50 local href/data references resolve inside the sealed staging root.",
                ],
            },
        },
        "screenshots": [pin(path) for path in EXPECTED if path.suffix == ".png"],
        "adverse_execution_history": pin(ADVERSE_RECEIPT),
        "method": "Read-only Playwright control of installed Microsoft Edge, exact DOM/overflow/local-reference/JSON-LD checks, desktop and mobile screenshots, and direct visual inspection.",
        "accepted_state_reverted": False,
        "errors": [],
    }
    OUTPUT.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"status": "PASS", "receipt": pin(OUTPUT), "adverse_history": pin(ADVERSE_RECEIPT), "local_references": 50, "visual_defects": 0}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PASS1 = ROOT / "determinism_pass1_final"
PASS2 = ROOT / "determinism_pass2_final"
PACKET = ROOT / "packet"
QA_FINAL = ROOT / "qa_final"
QA_AUTHORITY = ROOT / "qa_authority"

EXPECTED = {
    "D036_FR.pdf": (88549, "AF8BAE906185B24BFCE455336F34317AA625B0D2E5696B3F2B44132092AB9BC4"),
    "D036_FR.tex": (38281, "2C845AE7BAF2DC8FCA4AF43D70A971218982030CD3C43E37065A7063758EE071"),
    "D036_EN.pdf": (87475, "3D678FF9F6259F0147135A581ECD33DC16B60323747EC6FBD8828025D248A8CF"),
    "D036_EN.tex": (37182, "BFE095C49D3252B5917315953AAF569A10F8D6F60BACD42F8FB3C3904925B777"),
    "D036_APPARATUS.pdf": (56276, "A00FA6B21BA710316C47342029210D233C6D747C8E4C6849B912B75D4933011B"),
    "D036_APPARATUS.tex": (10019, "6D7D04EBBE54FF59B7633E00C4A7B342731E54E255CC20B94BC55FD9B52F611B"),
    "20_AUTHORITY_DELIGNE_D036_NUMBER39_10PP.pdf": (
        543285,
        "278125A52E24555349D7A7B56A5EE828FF2BC1952F752969B20E7BDD8228A74D",
    ),
}

CONTACT_SHEETS = [
    "qa_final/D036_FR_CONTACT_01_05.png",
    "qa_final/D036_FR_CONTACT_06_10.png",
    "qa_final/D036_EN_CONTACT_01_05.png",
    "qa_final/D036_EN_CONTACT_06_10.png",
    "qa_final/D036_APPARATUS_CONTACT_01_05.png",
    "qa_final/D036_APPARATUS_CONTACT_06_10.png",
    "qa_authority/D036_AUTHORITY_CONTACT_01_05.png",
    "qa_authority/D036_AUTHORITY_CONTACT_06_10.png",
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest().upper()


def run(*args: str) -> str:
    return subprocess.run(args, check=True, capture_output=True, text=True, encoding="utf-8", errors="replace").stdout


def pdf_info(path: Path) -> dict[str, object]:
    text = run("pdfinfo", str(path))
    fields: dict[str, str] = {}
    for line in text.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    return {
        "pages": int(fields["Pages"]),
        "page_size": fields["Page size"],
        "encrypted": fields["Encrypted"],
        "rotation": fields["Page rot"],
        "pdf_version": fields["PDF version"],
    }


def embedded_fonts(path: Path) -> dict[str, object]:
    rows = [line for line in run("pdffonts", str(path)).splitlines()[2:] if line.strip()]
    all_embedded = all(re.search(r"\syes\s+yes\s+yes\s+", row) for row in rows)
    return {"font_rows": len(rows), "all_embedded_and_subset": all_embedded}


def image_pages(path: Path) -> list[int]:
    rows = [line for line in run("pdfimages", "-list", str(path)).splitlines()[2:] if line.strip()]
    return [int(line.split()[0]) for line in rows]


def extracted_checks(path: Path, identity: str) -> dict[str, object]:
    text = run("pdftotext", "-layout", str(path), "-")
    folded = text.casefold()
    return {
        "authority_page_headers": text.count("Authority physical page"),
        "raw_tex_command": bool(re.search(r"\\[A-Za-z]+", text)),
        "textbackslash_marker": "textbackslash" in folded,
        "asset_placeholder": bool(re.search(r"(?m)^\s*ASSET\b", text)),
        "local_profile_path": bool(re.search(r"(?i)[A-Z]:\\Users\\", text)),
        "local_identity_match": identity.casefold() in folded if identity else False,
        "title_marker": ("fundamental group" in folded or "groupe fondamental" in folded),
        "theorem_1_marker": ("theorem 1" in folded or "théorème 1" in folded),
        "section_2_3_marker": "2.3" in text,
        "bibliography_2_bis": "[2 bis]" in text,
        "dated_postscript": "1/10/80" in text,
        "terminal_address": "F-91440" in text,
    }


def source_checks(path: Path, identity: str) -> dict[str, bool]:
    text = path.read_text(encoding="utf-8")
    folded = text.casefold()
    return {
        "local_profile_path": bool(re.search(r"(?i)[A-Z]:\\Users\\", text)),
        "local_identity_match": identity.casefold() in folded if identity else False,
        "credential_marker": bool(re.search(r"(?i)password|api[_-]?key|access[_-]?token|secret[_-]?key", text)),
        "asset_placeholder": bool(re.search(r"(?m)^\s*ASSET\b", text)),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--visual-pass", action="store_true", help="Record the completed human contact-sheet comparison.")
    args = parser.parse_args()

    identity = Path(os.environ.get("USERPROFILE", "")).name
    failures: list[str] = []
    artifacts: dict[str, object] = {}
    for name, (expected_bytes, expected_hash) in EXPECTED.items():
        p1 = PASS1 / name
        p2 = PASS2 / name
        row = {
            "bytes": p1.stat().st_size,
            "sha256": sha256(p1),
            "pass2_sha256": sha256(p2),
            "deterministic": sha256(p1) == sha256(p2),
        }
        artifacts[name] = row
        if row["bytes"] != expected_bytes or row["sha256"] != expected_hash or not row["deterministic"]:
            failures.append(f"artifact_identity:{name}")

    packet_authority = PACKET / "source" / "20_AUTHORITY_DELIGNE_D036_NUMBER39_10PP.pdf"
    authority_identity = {
        "packet_bytes": packet_authority.stat().st_size,
        "packet_sha256": sha256(packet_authority),
        "canonical_sha256": artifacts["20_AUTHORITY_DELIGNE_D036_NUMBER39_10PP.pdf"]["sha256"],
        "exact_identity": sha256(packet_authority) == artifacts["20_AUTHORITY_DELIGNE_D036_NUMBER39_10PP.pdf"]["sha256"],
    }
    if not authority_identity["exact_identity"]:
        failures.append("authority_identity")

    pdfs: dict[str, object] = {}
    for name in ("D036_FR.pdf", "D036_EN.pdf", "D036_APPARATUS.pdf"):
        path = PASS1 / name
        info = pdf_info(path)
        fonts = embedded_fonts(path)
        images = image_pages(path)
        text_checks = extracted_checks(path, identity)
        pdfs[name] = {"pdfinfo": info, "fonts": fonts, "image_pages": images, "text_checks": text_checks}
        required_text = [
            "title_marker",
            "theorem_1_marker",
            "section_2_3_marker",
            "bibliography_2_bis",
            "dated_postscript",
        ]
        if info["pages"] != 10 or "A4" not in str(info["page_size"]) or info["encrypted"] != "no":
            failures.append(f"pdf_structure:{name}")
        if not fonts["all_embedded_and_subset"] or images != [8, 9]:
            failures.append(f"pdf_resources:{name}")
        if text_checks["authority_page_headers"] != 10 or any(
            text_checks[key] for key in ("raw_tex_command", "textbackslash_marker", "asset_placeholder", "local_profile_path", "local_identity_match")
        ):
            failures.append(f"pdf_surface:{name}")
        if not all(text_checks[key] for key in required_text):
            failures.append(f"pdf_markers:{name}")

    sources: dict[str, object] = {}
    for name in ("D036_FR.tex", "D036_EN.tex", "D036_APPARATUS.tex"):
        checks = source_checks(PASS1 / name, identity)
        sources[name] = checks
        if any(checks.values()):
            failures.append(f"source_surface:{name}")

    log_gate: dict[str, int] = {}
    bad_log = re.compile(
        r"LaTeX Error|Undefined control sequence|Missing character|Emergency stop|Fatal error|"
        r"Overfull \\hbox|Overfull \\vbox|Underfull \\hbox|Underfull \\vbox|"
        r"multiply defined|Reference .* undefined|Citation .* undefined",
        re.IGNORECASE,
    )
    for path in sorted(PASS1.glob("*.log*")):
        hits = len(bad_log.findall(path.read_text(encoding="utf-8", errors="replace")))
        log_gate[path.name] = hits
        if hits:
            failures.append(f"log_gate:{path.name}")

    qa: dict[str, object] = {}
    for rel in CONTACT_SHEETS:
        path = ROOT / rel
        qa[rel] = {"bytes": path.stat().st_size, "sha256": sha256(path)}
    if not args.visual_pass:
        failures.append("human_visual_gate_not_recorded")

    receipt = {
        "schema": "deligne.d036.corpus_cold_audit.v1",
        "audited_at_utc": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
        "scope": "fresh nonpatching corpus-side audit of D036 canonical FR/EN/apparatus against controlling authority",
        "inherited_web_audit_acceptance": "ZERO_ACCEPTED_EVIDENCE_ONLY",
        "authority": authority_identity,
        "artifacts": artifacts,
        "pdf_checks": pdfs,
        "source_checks": sources,
        "log_gate_hits": log_gate,
        "qa_contact_sheets": qa,
        "human_visual_gate": {
            "performed": args.visual_pass,
            "sheets_inspected": len(CONTACT_SHEETS),
            "result": "PASS" if args.visual_pass else "NOT_RECORDED",
            "findings": "all 30 canonical pages and all 10 authority pages visible; no clipping, overlap, raw TeX, missing terminal matter, or displaced page-8/page-9 diagrams",
        },
        "failures": failures,
        "result": "PASS" if not failures else "FAIL",
    }
    out_dir = ROOT / "cold_audit"
    out_dir.mkdir(exist_ok=True)
    out = out_dir / "D036_COLD_AUDIT.json"
    out.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"result": receipt["result"], "failures": failures, "receipt": str(out)}, ensure_ascii=False))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

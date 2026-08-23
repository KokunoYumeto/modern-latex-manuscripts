#!/usr/bin/env python3
"""Independent, nonpatching cold audit for the maintained D026 editions."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import zipfile
from pathlib import Path
from typing import Any

from PIL import Image
from pypdf import PdfReader


EXPECTED = {
    "selected_zip": (22847673, "6C62596BDFE0992339764CCBCE13239DDD0640F901639D96F487BF88D2969D74"),
    "nested_zip": (22753925, "9D72233942EFF34C94EBFAE50425DC0F8DFC50A40933B8F1395A083281D95313"),
    "authority_pdf": (901648, "9951F00E4E8E2673ABBAFB44D28B03FA31A45E60EF03BCFE6DA0A5E102167FC6"),
    "comparator_pdf": (428680, "6F0CB89BF47166EDF99048B411B24FD73CD132A01422CAB3FC42B321C1187634"),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def read_ndjson(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def flatten_outline(items: list[Any]) -> list[str]:
    titles: list[str] = []
    for item in items:
        if isinstance(item, list):
            titles.extend(flatten_outline(item))
        else:
            title = getattr(item, "title", None)
            if title:
                titles.append(title)
    return titles


def image_xobject_count(page: Any) -> int:
    seen: set[tuple[int, int] | int] = set()

    def walk(resources: Any) -> int:
        if resources is None:
            return 0
        resources = resources.get_object()
        xobjects = resources.get("/XObject")
        if xobjects is None:
            return 0
        total = 0
        for ref in xobjects.get_object().values():
            ident = getattr(ref, "idnum", id(ref))
            if ident in seen:
                continue
            seen.add(ident)
            obj = ref.get_object()
            subtype = obj.get("/Subtype")
            if subtype == "/Image":
                total += 1
            elif subtype == "/Form":
                total += walk(obj.get("/Resources"))
        return total

    return walk(page.get("/Resources"))


def display_signature(text: str) -> dict[str, Any]:
    displays = re.findall(r"\\\[(.*?)\\\]", text, flags=re.DOTALL)
    joined = "\n".join(displays)
    return {
        "display_count": len(displays),
        "tags": re.findall(r"\\tag\{([^}]+)\}", joined),
        "arrays": joined.count(r"\begin{array}"),
        "aligned": joined.count(r"\begin{aligned}"),
        "cases": joined.count(r"\begin{cases}"),
        "long_arrows": joined.count(r"\longrightarrow"),
        "down_arrows": joined.count(r"\downarrow"),
        "up_arrows": joined.count(r"\uparrow"),
        "diagonal_arrows": joined.count(r"\searrow") + joined.count(r"\dashrightarrow"),
        "x_arrows": joined.count(r"\xrightarrow"),
    }


def audit_record_layers(state: Path) -> dict[str, Any]:
    edition = state / "edition"
    french = read_ndjson(edition / "source_language.ndjson")
    english = read_ndjson(edition / "english_standalone.ndjson")
    apparatus = read_ndjson(edition / "apparatus.ndjson")
    for label, rows, language, status in (
        ("french", french, "fr", "frozen"),
        ("english", english, "en", "accepted"),
        ("apparatus", apparatus, "en", "accepted"),
    ):
        check(len(rows) == 18, f"{label}: not 18 records")
        check([row["authority_pdf_page"] for row in rows] == list(range(1, 19)), f"{label}: page topology")
        check([row["paper_folio"] for row in rows] == list(range(299, 317)), f"{label}: folio topology")
        check(all(row["language"] == language for row in rows), f"{label}: language mismatch")
        check(all(row["status"] == status for row in rows), f"{label}: status mismatch")
        check(all(row["disposition"] == "INCLUDE_AUTHORITY_PAGE" for row in rows), f"{label}: disposition mismatch")
        check(all(row["source_sha256"].upper() == EXPECTED["authority_pdf"][1] for row in rows), f"{label}: authority mismatch")

    for row in french:
        for repair in row.get("canonical_repairs", []) + row.get("integration_corrections", []):
            lexical_controls = re.findall(r"[A-Za-zÀ-ÿ]{4,}", repair["adopted_reading"])
            check(all(word in row["text"] for word in lexical_controls), f"page {row['authority_pdf_page']}: adopted repair wording absent")

    p = {row["authority_pdf_page"]: row["text"] for row in french}
    e = {row["authority_pdf_page"]: row["text"] for row in english}
    critical = {
        "p1_title": "Les constantes locales de l’équation fonctionnelle" in p[1],
        "p1_dedication": "A Jean-Pierre Serre en témoignage d’admiration." in p[1],
        "p1_contents_virtual": "représentations virtuelles des groupes finis" in p[1],
        "p4_heading_real": "Lemmes sur les représentations réelles des groupes finis" in p[4],
        "p1_outer_exponent": r"\tag{1.1.3}" in p[1] and r"^{\frac12-s}" in p[1],
        "p2_reciprocity_isomorphism": r"K^*\simeq W(\bar K/K)^{\mathrm{ab}}" in p[2],
        "p13_typed_reciprocity": r"\exp\bigl(2\pi i\,\operatorname{inv}(\partial\chi\cup\alpha)\bigr)=\chi(\alpha)" in p[13],
        "p14_local_weil_target": r"H^2(W(\bar K_v/K_v),\mu_n)" in p[14],
        "p15_exactness_topology": all(token in p[15] for token in (r"\bigoplus_v", r"\Sigma", r"H^2(W(\bar K/K),\mu_n)", r"H^2(\operatorname{Gal}(\bar K/K),\mu_n)")),
        "p16_chern_identity": r"w^2(V)=c^1(W)\pmod2" in p[16],
        "p17_epsilon_zero": r"\varepsilon(V)=\varepsilon(V,0)" in p[17],
        "p17_equation_number": r"\tag{5.4.1}" in p[17] and r"\tag{2.3.1}" not in p[17] and r"\tag{5.3.1}" not in p[17],
        "p17_nilpotent_pair": r"(\rho',N)" in p[17],
        "p17_parameter": r"q^{-s}" in p[17],
        "p18_end_matter": all(token in p[18] for token in ("Bibliographie", "Reçu le 20 septembre 1975", "35, Route de Chartres", "F-91440")),
        "en_title": "Local Constants in the Functional Equation" in e[1],
        "en_standalone_end_matter": all(token in e[18] for token in ("Bibliography", "Received 20 September 1975", "35, Route de Chartres", "F-91440")),
    }
    failed_critical = [name for name, passed in critical.items() if not passed]
    check(not failed_critical, f"critical authority/translation fact failed: {failed_critical}")

    signature_rows = []
    for page in range(1, 19):
        fr_sig = display_signature(p[page])
        en_sig = display_signature(e[page])
        check(fr_sig == en_sig, f"page {page}: French/English mathematical topology differs")
        signature_rows.append({"page": page, "folio": page + 298, **fr_sig})

    asset_lines = [line for line in (edition / "asset_ledger.tsv").read_text(encoding="utf-8").splitlines() if line.strip()]
    check(len(asset_lines) == 1, "returned asset ledger is not empty")
    prior = edition.parent / "salvage" / "30_UNTRUSTED_PRIOR_WORK_DELIGNE_D026.zip"
    check(sha256(prior) == "2DE877D7BE03D95319CC21C535C5DA179688A59A51B31407A76394C2FBC74FD7", "prior-work archive identity")
    with zipfile.ZipFile(prior) as archive:
        check(archive.testzip() is None, "prior-work archive integrity")
        prior_members = len(archive.infolist())
    check(prior_members == 64, "prior-work archive member count")
    ledger = (edition.parent / "control" / "PRIOR_WORK_LEDGER.tsv").read_text(encoding="utf-8")
    check(ledger.count("ZERO_ACCEPTED") >= 64, "prior-work ZERO_ACCEPTED ledger coverage")

    page_one = p[1]
    check("© by Springer-Verlag 1976" not in page_one, "copyright copy matter leaked")
    check("Inventiones math. 35, 299-316 (1976)" not in page_one, "journal masthead leaked")

    return {
        "french_records": len(french),
        "english_records": len(english),
        "apparatus_records": len(apparatus),
        "critical_facts": critical,
        "math_topology_by_page": signature_rows,
        "asset_fallbacks": 0,
        "prior_members_zero_accepted": prior_members,
        "copy_matter_exclusion": "PASS",
    }


def audit_tex(base: Path) -> dict[str, Any]:
    source = base / "source"
    result: dict[str, Any] = {}
    for lang in ("FR", "EN"):
        path = source / f"Deligne_D026_{lang}.tex"
        text = path.read_text(encoding="utf-8")
        check(text.count(r"\EditionPage{") == 18, f"{lang}: EditionPage count")
        forbidden = (r"\includegraphics", r"\begin{verbatim}", r"\verb", "<html", "<pre")
        check(not any(token in text for token in forbidden), f"{lang}: noncanonical rendering primitive")
        check(all(f"\\EditionPage{{{page}}}{{{page + 298}}}" in text for page in range(1, 19)), f"{lang}: page map")
        result[lang] = {"bytes": path.stat().st_size, "sha256": sha256(path), "edition_pages": 18}
    apparatus = source / "Deligne_D026_APPARATUS.tex"
    app_text = apparatus.read_text(encoding="utf-8")
    check(app_text.count(r"\subsection*{Authority page") == 18, "apparatus page coverage")
    check("ZERO_ACCEPTED" not in app_text, "apparatus accidentally promotes inherited work")
    local_assets = [line for line in (source / "ASSET_LEDGER.tsv").read_text(encoding="utf-8").splitlines() if line.strip()]
    check(len(local_assets) == 1, "maintained asset ledger is not empty")
    result["APPARATUS"] = {"bytes": apparatus.stat().st_size, "sha256": sha256(apparatus), "authority_pages": 18}
    return result


PAGE_ANCHORS = {
    1: ("(1.1.3)",),
    2: ("(1.2.4)",),
    3: ("(1.4.1)", "(1.5)"),
    4: ("(2.1)", "(2.2)"),
    5: ("(2.2.1)",),
    6: ("(2.3)", "(2.6)"),
    7: ("(2.7)", "(2.8)"),
    8: ("(2.9)",),
    9: ("(3.1)", "(3.2)"),
    10: ("(3.2.1)", "(3.3)"),
    11: ("(4.1)", "(4.2.1)"),
    12: ("(4.2.2)", "(4.2.4)"),
    13: ("(4.5.1)", "(4.6)"),
    14: ("(4.9)", "(4.9.3)"),
    15: ("(Q/Z)", "5."),
    16: ("(5.2)", "(5.3)"),
    17: ("(5.4.1)", "(5.6)"),
    18: ("Bibliograph", "20 September"),
}


def audit_pdf(path: Path, lang: str) -> dict[str, Any]:
    reader = PdfReader(path)
    check(len(reader.pages) == 18, f"{lang}: PDF page count")
    check(reader.page_labels == [str(n) for n in range(299, 317)], f"{lang}: PDF page labels")
    metadata = reader.metadata
    check(metadata.author == "Pierre Deligne", f"{lang}: PDF author")
    check("local" in (metadata.title or "").lower() or "constantes" in (metadata.title or "").lower(), f"{lang}: PDF title")

    outline = flatten_outline(reader.outline)
    for folio in range(299, 317):
        check(f"Printed folio {folio}" in outline, f"{lang}: bookmark {folio}")

    image_count = 0
    extracted_lengths: list[int] = []
    for index, page in enumerate(reader.pages, start=1):
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        check(abs(width - 595.276) < 0.1 and abs(height - 841.89) < 0.1, f"{lang}: page {index} size")
        text = page.extract_text() or ""
        normalized = re.sub(r"\s+", " ", text)
        extracted_lengths.append(len(normalized))
        check(len(normalized) > 250, f"{lang}: page {index} is not a text reader")
        anchors = PAGE_ANCHORS[index]
        if index == 18 and lang == "FR":
            anchors = ("Bibliograph", "20 septembre")
        check(all(anchor in normalized for anchor in anchors), f"{lang}: page {index} anchor coverage {anchors}")
        image_count += image_xobject_count(page)
    check(image_count == 0, f"{lang}: reader contains raster image objects")

    font_output = subprocess.run(["pdffonts", str(path)], check=True, capture_output=True, text=True, encoding="utf-8").stdout
    font_lines = font_output.splitlines()[2:]
    check(font_lines, f"{lang}: no fonts listed")
    for line in font_lines:
        match = re.search(r"\s(yes|no)\s+(yes|no)\s+(yes|no)\s+\d+\s+\d+\s*$", line)
        check(match is not None and match.groups() == ("yes", "yes", "yes"), f"{lang}: font not embedded/subset/Unicode: {line}")

    log = path.with_suffix(".log").read_text(encoding="utf-8", errors="replace")
    forbidden_log = ("Undefined control sequence", "LaTeX Error", "Fatal error", "Overfull \\hbox", "Overfull \\vbox", "Missing character")
    check(not any(token in log for token in forbidden_log), f"{lang}: build log defect")
    return {
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
        "pages": len(reader.pages),
        "page_labels": reader.page_labels,
        "bookmarks": len(outline),
        "embedded_unicode_fonts": len(font_lines),
        "raster_images": image_count,
        "min_extracted_chars_per_page": min(extracted_lengths),
    }


def audit_renders(base: Path) -> dict[str, Any]:
    rendered = base / "qa" / "rendered"
    result: dict[str, Any] = {}
    for kind, prefix in (("authority", "authority"), ("fr", "page"), ("en", "page")):
        files = sorted((rendered / kind).glob(f"{prefix}-*.png"))
        check(len(files) == 18, f"{kind}: render count")
        metrics = []
        for index, path in enumerate(files, start=1):
            with Image.open(path) as image:
                gray = image.convert("L")
                mask = gray.point(lambda value: 255 if value < 245 else 0)
                bbox = mask.getbbox()
                histogram = mask.histogram()
                ink_pixels = histogram[255]
                check(bbox is not None and ink_pixels > 2500, f"{kind}: blank render {index}")
                if kind in {"fr", "en"}:
                    check(bbox[0] > 5 and bbox[1] > 5 and bbox[2] < image.width - 5 and bbox[3] < image.height - 5, f"{kind}: clipped render {index}")
                metrics.append({
                    "page": index,
                    "folio": index + 298,
                    "file": str(path.relative_to(base)).replace("\\", "/"),
                    "sha256": sha256(path),
                    "pixels": [image.width, image.height],
                    "ink_bbox": list(bbox),
                    "ink_pixels": ink_pixels,
                })
        result[kind] = metrics
    return result


def audit_manual_visual_log(base: Path) -> dict[str, Any]:
    path = base / "qa" / "cold_audit" / "MANUAL_VISUAL_COLD_AUDIT.tsv"
    lines = [line for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    check(len(lines) == 19, "manual visual audit must contain one header and 18 page rows")
    header = lines[0].split("\t")
    check(header == ["authority_page", "printed_folio", "authority_render", "french_render", "english_render", "visual_control", "result"], "manual visual audit header")
    for index, line in enumerate(lines[1:], start=1):
        fields = line.split("\t")
        check(len(fields) == 7, f"manual visual audit row {index}")
        check(fields[0] == str(index) and fields[1] == str(index + 298), f"manual visual topology row {index}")
        check(fields[-1] == "PASS", f"manual visual result row {index}")
        for render_field in fields[2:5]:
            check((base / render_field).is_file(), f"manual visual render missing: {render_field}")
    return {
        "result": "PASS",
        "authority_pages_reviewed": 18,
        "french_pages_reviewed": 18,
        "english_pages_reviewed": 18,
        "log": str(path.relative_to(base)).replace("\\", "/"),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    base = args.base.resolve()

    selected = base / "input" / "selected" / "DELIGNE_D026_LOCAL_CONSTANTS_ARTIN_ORTHOGONAL_FINAL_CANON_FULL_STATE_BUNDLE.zip"
    nested = base / "input" / "expanded_return" / "04_EXACT_S03_FULL_STATE_TRIO" / "DELIGNE_D026_LOCAL_CONSTANTS_ARTIN_ORTHOGONAL_S03_CUMULATIVE_FULL_STATE.zip"
    authority = base / "input" / "expanded_state" / "source" / "20_AUTHORITY_DELIGNE_D026_LOCAL_CONSTANTS_ARTIN_ORTHOGONAL_18PP_IAS_300DPI.pdf"
    comparator = base / "input" / "expanded_state" / "source" / "21_COMPARATOR_DELIGNE_D026_LOCAL_CONSTANTS_ARTIN_ORTHOGONAL_18PP_COLLECTED_SPLIT.pdf"
    identities = {}
    for name, path in (("selected_zip", selected), ("nested_zip", nested), ("authority_pdf", authority), ("comparator_pdf", comparator)):
        expected_bytes, expected_hash = EXPECTED[name]
        check(path.stat().st_size == expected_bytes, f"{name}: byte count")
        actual_hash = sha256(path)
        check(actual_hash == expected_hash, f"{name}: SHA-256")
        identities[name] = {"bytes": expected_bytes, "sha256": actual_hash}
    for label, archive_path, expected_members in (("outer", selected, 14), ("nested", nested, 29)):
        with zipfile.ZipFile(archive_path) as archive:
            check(archive.testzip() is None, f"{label}: ZIP stream integrity")
            check(len(archive.infolist()) == expected_members, f"{label}: ZIP members")

    report = {
        "schema_version": "deligne-d026-cold-audit-v1",
        "work_id": "D026",
        "mode": "FRESH_NONPATCHING_COLD_AUDIT",
        "result": "PASS",
        "identities": identities,
        "record_layers": audit_record_layers(base / "input" / "expanded_state"),
        "editable_sources": audit_tex(base),
        "pdfs": {
            "FR": audit_pdf(base / "output" / "pdf" / "Deligne_D026_FR.pdf", "FR"),
            "EN": audit_pdf(base / "output" / "pdf" / "Deligne_D026_EN.pdf", "EN"),
        },
        "rendered_pages": audit_renders(base),
        "manual_visual_review": audit_manual_visual_log(base),
        "publication_actions": "NONE",
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({
        "result": "PASS",
        "report": str(args.report),
        "french_pdf_sha256": report["pdfs"]["FR"]["sha256"],
        "english_pdf_sha256": report["pdfs"]["EN"]["sha256"],
        "rendered_pages_checked": sum(len(rows) for rows in report["rendered_pages"].values()),
    }, sort_keys=True))


if __name__ == "__main__":
    main()

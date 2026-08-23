#!/usr/bin/env python3
"""Build genuine LaTeX reader sources from the frozen D021 page records.

The returned NDJSON records are immutable inputs.  This builder performs only
presentation conversion: prose is escaped for TeX, the already verified math
payload is passed to real math mode, and each included IAS article scan maps to
exactly one reader page.  It never consults the comparator or salvage archive.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
from typing import Iterable


AUTHORITY_SHA256 = "2ACE335E3C8CC08BB8B60D756886284C4E7AECF093081DDA0DE46650800E6986"
COMPARATOR_SHA256 = "3E2D6E05377BA1017EAAB113BC7523B45B56FB0C4CC108493F79EBAD39033AE8"
SALVAGE_SHA256 = "D55B831C10A0CC48C4177BFFE93FFCB1C16CA4E9276BED63948C917DC651FC68"
FIXED_PDF_DATE = "D:19740809000000Z"

LAYERS = {
    "FR": {
        "records": "source_language.ndjson",
        "title": "Formes modulaires de poids 1",
        "subtitle": "Édition française de lecture",
        "lang": "french",
        "pages": range(2, 26),
        "outfile": "D021_Formes_modulaires_de_poids_1_FR.tex",
    },
    "EN": {
        "records": "english_standalone.ndjson",
        "title": "Modular Forms of Weight 1",
        "subtitle": "Standalone English edition",
        "lang": "english",
        "pages": range(2, 26),
        "outfile": "D021_Modular_Forms_of_Weight_1_EN.tex",
    },
    "APPARATUS": {
        "records": "apparatus.ndjson",
        "title": "Formes modulaires de poids 1",
        "subtitle": "Source and translation apparatus",
        "lang": "english",
        "pages": range(1, 26),
        "outfile": "D021_Formes_modulaires_de_poids_1_APPARATUS.tex",
    },
}


def sha256(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def load_records(path: pathlib.Path) -> dict[int, dict]:
    records: dict[int, dict] = {}
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        record = json.loads(line)
        page = int(record["physical_page"])
        if page in records:
            raise ValueError(f"duplicate physical page {page} in {path}:{line_number}")
        records[page] = record
    if sorted(records) != list(range(1, 26)):
        raise ValueError(f"{path} does not contain physical pages 1-25 exactly once")
    return records


def validate_state(state: pathlib.Path) -> None:
    authority = state / "source" / "20_AUTHORITY_DELIGNE_D021_WEIGHT_ONE_IAS_NUMBER24_25PP.pdf"
    comparator = state / "comparison" / "21_COMPARATOR_DELIGNE_D021_WEIGHT_ONE_COLLECTED_SPLIT_24PP.pdf"
    salvage = state / "salvage" / "30_ZERO_ACCEPTED_PRIOR_WORK_DELIGNE_D021.zip"
    expected = {
        authority: AUTHORITY_SHA256,
        comparator: COMPARATOR_SHA256,
        salvage: SALVAGE_SHA256,
    }
    for path, digest in expected.items():
        if not path.is_file():
            raise FileNotFoundError(path)
        actual = sha256(path)
        if actual != digest:
            raise ValueError(f"hash mismatch for {path}: {actual} != {digest}")
    for spec in LAYERS.values():
        records = load_records(state / "edition" / spec["records"])
        for page, record in records.items():
            if record.get("status") != "COMPLETE":
                raise ValueError(f"incomplete record: {spec['records']} physical page {page}")
            if record.get("source_pdf_sha256") != AUTHORITY_SHA256:
                raise ValueError(f"authority mismatch: {spec['records']} physical page {page}")
            expected_disposition = (
                "EXCLUDE_COPY_MATTER_RETAIN_PROVENANCE" if page == 1 else "INCLUDE_WORK"
            )
            if record.get("disposition") != expected_disposition:
                raise ValueError(f"disposition mismatch: {spec['records']} physical page {page}")
        if spec["records"] != "apparatus.ndjson" and records[1].get("text") != "":
            raise ValueError(f"copy-matter body is not empty in {spec['records']}")


TEXT_ESCAPES = {
    "\\": r"\textbackslash{}",
    "{": r"\{",
    "}": r"\}",
    "&": r"\&",
    "%": r"\%",
    "#": r"\#",
    "_": r"\_",
    "^": r"\textasciicircum{}",
    "~": r"\textasciitilde{}",
}


def escape_text(value: str) -> str:
    return "".join(TEXT_ESCAPES.get(char, char) for char in value)


MATH_TOKEN = re.compile(r"(\$\$.*?\$\$|\$(?:\\.|[^$])*?\$)", re.DOTALL)
FOOTNOTE_SENTINELS = {
    1: "@@D021FOOTNOTE1@@",
    2: "@@D021FOOTNOTE2@@",
}


def inline_tex(value: str) -> str:
    """Escape prose while retaining verified inline math as live TeX math."""
    out: list[str] = []
    cursor = 0
    for match in MATH_TOKEN.finditer(value):
        out.append(escape_text(value[cursor : match.start()]))
        token = match.group(0)
        if token.startswith("$$"):
            raise ValueError("display math encountered inside a prose paragraph")
        out.append(r"\(" + token[1:-1].strip() + r"\)")
        cursor = match.end()
    out.append(escape_text(value[cursor:]))
    result = "".join(out)
    if "$" in result:
        raise ValueError(f"unparsed math delimiter in paragraph: {value[:120]!r}")
    for number, sentinel in FOOTNOTE_SENTINELS.items():
        result = result.replace(sentinel, rf"\footnotemark[{number}]")
    return result


def display_tex(value: str) -> str:
    body = value.strip()
    if not (body.startswith("$$") and body.endswith("$$")):
        raise ValueError("display paragraph is not bounded by $$")
    body = body[2:-2].strip()
    return "\\begin{equation*}\n" + body + "\n\\end{equation*}"


LABEL_PREFIX = re.compile(
    r"^(THÉORÈME|THEOREM|PROPOSITION|COROLLAIRE|COROLLARY|LEMME|LEMMA|"
    r"REMARQUE(?:S)?|REMARK(?:S)?|Démonstration|Proof|EXEMPLES|EXAMPLES|Variante)"
    r"([^—]*?)(?:\s+—\s+|\s+---\s+)(.*)$",
    re.DOTALL,
)
SECTION_PREFIX = re.compile(r"^§\s*(\d+)\.\s*(.*)$", re.DOTALL)


def paragraph_tex(paragraph: str, layer: str, page: int, bookmark_counts: dict[str, int]) -> str:
    paragraph = paragraph.strip()
    if not paragraph:
        return ""
    if paragraph.startswith("$$"):
        return display_tex(paragraph)

    footnote_number = {8: 1, 16: 2}.get(page) if layer in {"FR", "EN"} else None
    if footnote_number is not None:
        lead = f"({footnote_number}) "
        if paragraph.startswith(lead):
            note = inline_tex(paragraph[len(lead) :])
            return rf"\footnotetext[{footnote_number}]{{{note}}}"
        marker = f"({footnote_number})"
        if marker in paragraph:
            paragraph = paragraph.replace(marker, FOOTNOTE_SENTINELS[footnote_number], 1)

    if layer == "FR" and page == 2:
        if paragraph == "FORMES MODULAIRES DE POIDS 1":
            return r"\DTitle{FORMES MODULAIRES DE POIDS 1}"
        if paragraph == "PAR PIERRE DELIGNE ET JEAN-PIERRE SERRE":
            return r"\DByline{PAR PIERRE DELIGNE ET JEAN-PIERRE SERRE}"
        if paragraph.startswith("A Henri Cartan,"):
            lines = [inline_tex(line) for line in paragraph.splitlines()]
            if lines[-1] == "70e anniversaire":
                lines[-1] = r"70\textsuperscript{e} anniversaire"
            return "\\DDedication{" + r"\\".join(lines) + "}"
    if layer == "EN" and page == 2:
        if paragraph == "MODULAR FORMS OF WEIGHT 1":
            return r"\DTitle{MODULAR FORMS OF WEIGHT 1}"
        if paragraph == "BY PIERRE DELIGNE AND JEAN-PIERRE SERRE":
            return r"\DByline{BY PIERRE DELIGNE AND JEAN-PIERRE SERRE}"
        if paragraph.startswith("To Henri Cartan,"):
            lines = [inline_tex(line) for line in paragraph.splitlines()]
            return "\\DDedication{" + r"\\".join(lines) + "}"

    if paragraph in {"Introduction", "BIBLIOGRAPHIE", "BIBLIOGRAPHY"}:
        title = inline_tex(paragraph)
        key = "introduction" if paragraph == "Introduction" else "bibliography"
        bookmark_counts[key] = bookmark_counts.get(key, 0) + 1
        anchor = f"{key}-{bookmark_counts[key]}"
        return f"\\DSection{{{title}}}{{{anchor}}}"

    section = SECTION_PREFIX.match(paragraph)
    if section:
        number, title = section.groups()
        visible = inline_tex(f"§ {number}. {title}")
        bookmark = escape_text(f"Section {number}: {re.sub(MATH_TOKEN, '', title)}")
        return f"\\DSectionNamed{{{visible}}}{{{bookmark}}}{{section-{number}}}"

    label = LABEL_PREFIX.match(paragraph)
    if label:
        name, suffix, remainder = label.groups()
        return (
            "\\noindent\\textsc{" + inline_tex(name + suffix).strip() + "}"
            + r" \textemdash\ "
            + inline_tex(remainder)
            + "\\par"
        )

    # Preserve deliberate line grouping in addresses and short front-matter blocks.
    if "\n" in paragraph:
        lines = [inline_tex(line) for line in paragraph.splitlines()]
        return "\\begin{DLineBlock}\n" + " \\\\\n".join(lines) + "\n\\end{DLineBlock}"
    return inline_tex(paragraph) + "\\par"


def apply_presentation_repairs(text: str, layer: str, page: int) -> str:
    """Apply narrow presentation repairs without changing the frozen records."""
    if layer == "APPARATUS" and page == 9:
        inherited = r"\\frob_p notation"
        replacement = r"$\operatorname{Frob}_p$ notation"
        if text.count(inherited) != 1:
            raise ValueError("expected apparatus physical-9 Frobenius token not found exactly once")
        text = text.replace(inherited, replacement)
    if layer == "FR" and page == 12:
        suffix = r"$\rho$ cor-"
        if not text.endswith(suffix):
            raise ValueError("expected French physical-12 split-word suffix not found")
        return text[: -len("cor-")].rstrip()
    if layer == "FR" and page == 13:
        prefix = "respond bien"
        if not text.startswith(prefix):
            raise ValueError("expected French physical-13 split-word prefix not found")
        return "correspond bien" + text[len(prefix) :]
    if layer == "EN" and page == 12:
        suffix = r"$\rho$ indeed cor-"
        if not text.endswith(suffix):
            raise ValueError("expected English physical-12 split-word suffix not found")
        return text[: -len("indeed cor-")].rstrip()
    if layer == "EN" and page == 13:
        prefix = "responds indeed"
        if not text.startswith(prefix):
            raise ValueError("expected English physical-13 split-word prefix not found")
        return "corresponds indeed" + text[len(prefix) :]
    return text


def render_body(records: dict[int, dict], layer: str, pages: Iterable[int]) -> str:
    output: list[str] = []
    bookmark_counts: dict[str, int] = {}
    page_list = list(pages)
    for index, physical_page in enumerate(page_list):
        record = records[physical_page]
        printed = record.get("printed_page")
        article = record.get("article_page")
        output.append(
            f"% AUTHORITY_UNIT physical={physical_page} article={article or '-'} printed={printed or '-'}"
        )
        output.append(
            f"\\DPageUnit{{{physical_page}}}{{{printed or 'cover'}}}{{{article or 'cover'}}}"
        )
        text = apply_presentation_repairs(str(record.get("text", "")), layer, physical_page)
        if not text and layer != "APPARATUS":
            raise ValueError(f"empty included body record in {layer} physical page {physical_page}")
        paragraphs = re.split(r"\n\s*\n", text.strip()) if text.strip() else []
        for paragraph in paragraphs:
            converted = paragraph_tex(paragraph, layer, physical_page, bookmark_counts)
            if converted:
                output.append(converted)
        if index != len(page_list) - 1:
            output.append(r"\newpage")
    return "\n\n".join(output)


def preamble(layer: str, spec: dict, records_hash: str) -> str:
    lang = spec["lang"]
    title = spec["title"]
    subtitle = spec["subtitle"]
    is_apparatus = layer == "APPARATUS"
    base_size = "9.2pt" if is_apparatus else "8.65pt"
    leading = "11.3pt" if is_apparatus else "10.25pt"
    return rf"""% Generated deterministically from frozen D021 NDJSON records.
% Authority SHA-256: {AUTHORITY_SHA256}
% Records SHA-256: {records_hash}
\documentclass[10pt,oneside]{{article}}
\usepackage[paperwidth=615.118bp,paperheight=765.354bp,left=31mm,right=31mm,top=23mm,bottom=24mm,headheight=11pt,headsep=6mm,footskip=10mm]{{geometry}}
\usepackage{{amsmath}}
\usepackage{{fontspec}}
\usepackage{{unicode-math}}
\defaultfontfeatures{{Ligatures=TeX}}
\setmainfont{{TeX Gyre Pagella}}
\setsansfont{{TeX Gyre Heros}}
\setmathfont{{TeX Gyre Pagella Math}}
\usepackage[{lang}]{{babel}}
\usepackage{{microtype}}
\usepackage{{fancyhdr}}
\usepackage{{hyperref}}
\usepackage{{bookmark}}
\usepackage{{ragged2e}}
\usepackage{{enumitem}}
\hypersetup{{unicode=true,pdfencoding=auto,pdftitle={{{escape_text(title)}}},pdfauthor={{Pierre Deligne; Jean-Pierre Serre}},pdfsubject={{{escape_text(subtitle)}}},pdfkeywords={{D021; modular forms; weight one; bilingual edition}},pdfcreator={{Deterministic LuaLaTeX reconstruction}},pdfproducer={{LuaTeX}},pdfcreationdate={{{FIXED_PDF_DATE}}},pdfmoddate={{{FIXED_PDF_DATE}}},colorlinks=false,hidelinks}}
\pdfvariable suppressoptionalinfo 767
\setlength{{\parindent}}{{1.15em}}
\setlength{{\parskip}}{{0pt}}
\setlength{{\abovedisplayskip}}{{4.2pt plus 1.5pt minus 1.5pt}}
\setlength{{\belowdisplayskip}}{{4.2pt plus 1.5pt minus 1.5pt}}
\setlength{{\abovedisplayshortskip}}{{2.5pt plus 1pt}}
\setlength{{\belowdisplayshortskip}}{{3pt plus 1pt}}
\setlength{{\jot}}{{1.5pt}}
\setlist{{nosep,leftmargin=2em}}
\emergencystretch=1.5em
\clubpenalty=10000
\widowpenalty=10000
\displaywidowpenalty=10000
\raggedbottom
\newcommand{{\EditionShort}}{{{escape_text(subtitle)}}}
\newcommand{{\PhysicalPage}}{{}}
\newcommand{{\PrintedPage}}{{}}
\newcommand{{\ArticlePage}}{{}}
\newcommand{{\DPageUnit}}[3]{{%
  \renewcommand{{\PhysicalPage}}{{#1}}%
  \renewcommand{{\PrintedPage}}{{#2}}%
  \renewcommand{{\ArticlePage}}{{#3}}%
  \phantomsection\pdfbookmark[2]{{Authority physical #1 / printed #2}}{{physical-#1}}%
}}
\newcommand{{\DTitle}}[1]{{\begin{{center}}\vspace*{{2mm}}{{\fontsize{{15}}{{18}}\selectfont\bfseries #1\par}}\vspace{{4mm}}\end{{center}}}}
\newcommand{{\DByline}}[1]{{\begin{{center}}{{\small\scshape #1\par}}\vspace{{5mm}}\end{{center}}}}
\newcommand{{\DDedication}}[1]{{\begin{{flushright}}\itshape #1\end{{flushright}}\vspace{{2mm}}}}
\newcommand{{\DSection}}[2]{{\phantomsection\pdfbookmark[1]{{#1}}{{#2}}\begin{{center}}\vspace{{2.5pt}}{{\bfseries #1}}\end{{center}}\vspace{{1pt}}}}
\newcommand{{\DSectionNamed}}[3]{{\phantomsection\pdfbookmark[1]{{#2}}{{#3}}\begin{{center}}\vspace{{2.5pt}}{{\bfseries #1}}\end{{center}}\vspace{{1pt}}}}
\newenvironment{{DLineBlock}}{{\par\smallskip\begin{{center}}\begin{{minipage}}{{0.76\textwidth}}\raggedright}}{{\end{{minipage}}\end{{center}}\smallskip}}
\pagestyle{{fancy}}
\fancyhf{{}}
\fancyhead[L]{{\scriptsize\textsc{{Deligne--Serre · D021}}}}
\fancyhead[R]{{\scriptsize\EditionShort}}
\fancyfoot[C]{{\scriptsize Authority physical \PhysicalPage\ · printed \PrintedPage}}
\renewcommand{{\headrulewidth}}{{0.25pt}}
\renewcommand{{\footrulewidth}}{{0pt}}
\AtBeginDocument{{\fontsize{{{base_size}}}{{{leading}}}\selectfont}}
\begin{{document}}
\justifying
"""


def postamble() -> str:
    return "\\end{document}\n"


def write_manifest(state: pathlib.Path, out_root: pathlib.Path, generated: list[pathlib.Path]) -> None:
    manifest = out_root / "manifests" / "D021_BUILD_INPUTS.tsv"
    rows = ["role\trelative_path\tbytes\tsha256"]
    input_paths = [
        state / "source" / "20_AUTHORITY_DELIGNE_D021_WEIGHT_ONE_IAS_NUMBER24_25PP.pdf",
        state / "comparison" / "21_COMPARATOR_DELIGNE_D021_WEIGHT_ONE_COLLECTED_SPLIT_24PP.pdf",
        state / "salvage" / "30_ZERO_ACCEPTED_PRIOR_WORK_DELIGNE_D021.zip",
        state / "edition" / "source_language.ndjson",
        state / "edition" / "english_standalone.ndjson",
        state / "edition" / "apparatus.ndjson",
        state / "edition" / "asset_ledger.tsv",
        state / "control" / "PAGE_MAP.tsv",
    ]
    for path in input_paths:
        role = "authority" if path.name.startswith("20_AUTHORITY") else "frozen_input"
        if path.name.startswith("21_COMPARATOR"):
            role = "comparison_only"
        elif path.name.startswith("30_ZERO_ACCEPTED"):
            role = "zero_accepted_evidence"
        rows.append(f"{role}\t{path.relative_to(state).as_posix()}\t{path.stat().st_size}\t{sha256(path)}")
    for path in generated:
        rows.append(f"generated_latex\t{path.relative_to(out_root).as_posix()}\t{path.stat().st_size}\t{sha256(path)}")
    manifest.parent.mkdir(parents=True, exist_ok=True)
    manifest.write_text("\n".join(rows) + "\n", encoding="utf-8", newline="\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", required=True, type=pathlib.Path)
    parser.add_argument("--out-root", required=True, type=pathlib.Path)
    args = parser.parse_args()
    state = args.state.resolve()
    out_root = args.out_root.resolve()
    source_dir = out_root / "source"
    source_dir.mkdir(parents=True, exist_ok=True)
    (out_root / "manifests").mkdir(parents=True, exist_ok=True)

    validate_state(state)
    generated: list[pathlib.Path] = []
    report: dict[str, object] = {
        "authority_sha256": AUTHORITY_SHA256,
        "copy_matter_physical_page_1": "EXCLUDED_FROM_FR_EN_RETAINED_IN_APPARATUS",
        "fallback_assets": 0,
        "presentation_repairs": [
            "APPARATUS physical 9: inherited raw Frobenius token typeset as operatorname Frob subscript p",
            "FR physical 12-13: scan-line cor-/respond resolved as correspond",
            "EN physical 12-13: scan-line cor-/responds resolved as corresponds",
            "FR and EN physical 8 and 16: article notes (1) and (2) typeset as footnotes",
            "FR physical 2: authority ordinal 70e typeset with superscript e",
        ],
        "salvage_accepted_members": 0,
        "layers": {},
    }
    for layer, spec in LAYERS.items():
        records_path = state / "edition" / spec["records"]
        records = load_records(records_path)
        body = render_body(records, layer, spec["pages"])
        content = preamble(layer, spec, sha256(records_path)) + body + "\n" + postamble()
        output = source_dir / spec["outfile"]
        output.write_text(content, encoding="utf-8", newline="\n")
        generated.append(output)
        report["layers"][layer] = {
            "physical_pages": list(spec["pages"]),
            "page_units": len(list(spec["pages"])),
            "records_sha256": sha256(records_path),
            "tex_sha256": sha256(output),
            "tex_bytes": output.stat().st_size,
        }
    write_manifest(state, out_root, generated)
    report_path = out_root / "manifests" / "D021_LATEX_GENERATION_REPORT.json"
    report_path.write_text(
        json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps(report, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()

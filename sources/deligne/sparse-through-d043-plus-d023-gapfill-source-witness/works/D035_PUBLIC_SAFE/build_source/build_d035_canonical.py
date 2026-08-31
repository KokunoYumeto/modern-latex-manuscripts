#!/usr/bin/env python3
"""Build normalized, page-addressed D035 TeX sources from the returned NDJSON.

The returned HTML readers are inherited evidence only.  This builder reads the
frozen page records, removes running scan identifiers and printed folios from
reader prose, restores paragraphs, marks mathematical tokens for TeX, and keeps
one canonical reader page for each of the 34 authority pages.
"""

from __future__ import annotations

import hashlib
import json
import pathlib
import re
import shutil
import zipfile


HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[2]
STATE = ROOT / "state"
CANONICAL = ROOT / "canonical"

AUTH_SHA = "B65B39804DA147575D15CEFD37A681D586F500BEF3421CB27928D4F1550B2C0F"
COMP_SHA = "58BBD3292082B126F8C96BD74B3F1455360831F389D1C150E534FFCDE9170D9A"
ZERO_SHA = "31F2DF8D8CFB851A81CA9479404FB6BBC38A131B65914B56B5270DA508E3A13A"
WITNESS_SHA = "542174B82F6944E63A57A4D43F2CFCF771F95C82B9D239F576D20E0B9D50021F"


def sha256(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def records(layer: str) -> list[dict]:
    path = STATE / "edition" / f"{layer}.ndjson"
    out = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    assert len(out) == 34
    assert [int(item["physical_page"]) for item in out] == list(range(1, 35))
    assert all(item["status"] == "COMPLETE" for item in out)
    return out


MATH_MAP = {
    "§": r"\S{}",
    "±": r"\pm",
    "∓": r"\mp",
    "·": r"\cdot",
    "×": r"\times",
    "Γ": r"\Gamma",
    "Σ": r"\sum",
    "Φ": r"\Phi",
    "α": r"\alpha",
    "β": r"\beta",
    "γ": r"\gamma",
    "δ": r"\delta",
    "ε": r"\varepsilon",
    "ζ": r"\zeta",
    "θ": r"\theta",
    "λ": r"\lambda",
    "μ": r"\mu",
    "ν": r"\nu",
    "π": r"\pi",
    "ρ": r"\rho",
    "σ": r"\sigma",
    "τ": r"\tau",
    "φ": r"\varphi",
    "χ": r"\chi",
    "ψ": r"\psi",
    "ω": r"\omega",
    "ℓ": r"\ell",
    "↑": r"\uparrow",
    "↓": r"\downarrow",
    "↖": r"\nwarrow",
    "→": r"\to",
    "↦": r"\mapsto",
    "↪": r"\hookrightarrow",
    "∈": r"\in",
    "∏": r"\prod",
    "∑": r"\sum",
    "∧": r"\wedge",
    "∨": r"\vee",
    "∩": r"\cap",
    "∪": r"\cup",
    "∫": r"\int",
    "∬": r"\iint",
    "≃": r"\simeq",
    "≠": r"\ne",
    "≡": r"\equiv",
    "≤": r"\le",
    "≥": r"\ge",
    "⊂": r"\subset",
    "⊕": r"\oplus",
    "⊗": r"\otimes",
    "∞": r"\infty",
    "∤": r"\nmid",
    "√": r"\sqrt{}",
    "∛": r"\sqrt[3]{}",
    "²": r"^{2}",
    "ⁿ": r"^{n}",
    "𝒟": r"\mathcal{D}",
    "𝒵": r"\mathcal{Z}",
    "𝓔": r"\mathcal{E}",
    "𝓕": r"\mathcal{F}",
    "𝔞": r"\mathfrak{a}",
    "𝔭": r"\mathfrak{p}",
}

MATH_TRIGGER = set(MATH_MAP) | set("_^=<>|/∼")
SEMANTIC_HYPHEN_PREFIXES = {
    "anti", "co", "non", "quasi", "semi", "sous", "pseudo", "pre", "post",
    "p", "q", "n", "well", "square", "finite", "locally", "right", "left",
}


def tex_text(text: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
        "—": "---",
        "“": "``",
        "”": "''",
        "║": "||",
    }
    return "".join(replacements.get(ch, ch) for ch in text)


def math_tex(token: str) -> str:
    # The frozen page records use a literal reverse solidus for set quotients
    # (for example [T(F)]\T(A)^~), alongside two intentional TeX accents.
    # Normalize the four observed quotient forms before TeX sees them as
    # undefined control sequences.
    token = re.sub(r"\\(T|G|GL|U)(?![A-Za-z])", r"\\backslash \1", token)
    token = re.sub(r"([^\W\d_])\u0304", r"\\overline{\1}", token)
    token = re.sub(r"([^\W\d_])\u0303", r"\\widetilde{\1}", token)
    token = re.sub(r"([^\W\d_])\u0332", r"\\underline{\1}", token)
    token = token.replace("ā", r"\overline{a}").replace("ẽ", r"\widetilde{e}").replace("ũ", r"\widetilde{u}")
    token = token.replace("ã", r"\widetilde{a}")
    out: list[str] = []
    for ch in token:
        if ch in MATH_MAP:
            mapped = MATH_MAP[ch]
            if re.fullmatch(r"\\[A-Za-z]+", mapped):
                mapped += "{}"
            out.append(mapped)
        elif ch == "#":
            out.append(r"\#")
        elif ch == "&":
            out.append(r"\&")
        elif ch == "%":
            out.append(r"\%")
        elif ch == "~":
            out.append(r"\sim")
        elif ch in "“”":
            out.append("''")
        elif ch == "—":
            out.append("-")
        else:
            out.append(ch)
    value = "".join(out)
    if value.count("{") != value.count("}"):
        value = value.replace("{", r"\{").replace("}", r"\}")
    value = re.sub(
        r"([_^])(\\(?:overline|widetilde|underline)\{[^{}]+\})",
        r"\1{\2}",
        value,
    )
    for name in ("Tr", "Ker", "End", "Hom", "Gal", "Br", "Spec", "Res", "diag", "GL", "SL", "PGL", "PSL"):
        value = re.sub(rf"(?<![A-Za-z\\]){name}(?=\s*\()", rf"\\operatorname{{{name}}}", value)
    value = re.sub(r"(?<![A-Za-z\\])exp(?=\s*\()", r"\\exp", value)
    return value


def is_math_token(token: str) -> bool:
    if any(ch in MATH_TRIGGER for ch in token):
        return True
    if "\\widetilde" in token or "\\overline" in token:
        return True
    if re.search(r"(?:SL|GL|PGL|PSL|Br|Gal|Ker|Hom|End|Spec|Tr|diag)\s*\(", token):
        return True
    if re.search(r"[A-Za-z0-9]+/[A-Za-z0-9]", token):
        return True
    if re.fullmatch(r"\(?\d+(?:\.\d+){1,3}\)?[.,;:]?", token):
        return True
    return False


def inline_tex(text: str) -> str:
    text = text.replace("§", "section ")
    parts = re.split(r"(\s+)", text)
    rendered: list[str] = []
    for part in parts:
        if not part or part.isspace():
            rendered.append(" " if part else "")
            continue
        lead = ""
        tail = ""
        while part and part[0] in "“\"":
            lead += part[0]
            part = part[1:]
        while part and part[-1] in ",.;:!?\"”":
            tail = part[-1] + tail
            part = part[:-1]
        mixed = re.fullmatch(r"(.+?)-([A-Za-zÀ-ÿ]+-?)", part)
        if mixed and is_math_token(mixed.group(1)):
            rendered.append(
                tex_text(lead) + "$" + math_tex(mixed.group(1)) + "$-"
                + tex_text(mixed.group(2) + tail)
            )
        elif part and is_math_token(part):
            rendered.append(tex_text(lead) + "$" + math_tex(part) + "$" + tex_text(tail))
        else:
            rendered.append(tex_text(lead + part + tail))
    return "".join(rendered).strip()


def join_source_lines(lines: list[str]) -> str:
    if not lines:
        return ""
    result = lines[0].strip()
    for raw in lines[1:]:
        nxt = raw.strip()
        if result.endswith("-") and nxt and nxt[0].islower():
            match = re.search(r"([A-Za-zÀ-ÿ]+)-$", result)
            prefix = match.group(1).lower() if match else ""
            if prefix in SEMANTIC_HYPHEN_PREFIXES:
                result += nxt
            else:
                result = result[:-1] + nxt
        else:
            result += " " + nxt
    return re.sub(r"\s+", " ", result).strip()


def is_scan_identifier(block: str, printed: int) -> bool:
    value = block.strip()
    return bool(
        re.fullmatch(r"(?:[35]39)-\d{2}", value)
        or value == str(printed)
        or value == "[PHYSICAL EOF]"
    )


def is_heading(block: str) -> bool:
    value = " ".join(block.split())
    if len(value) > 100:
        return False
    if re.fullmatch(r"(?i)bibliograph(?:ie|y)\.?", value):
        return True
    return bool(re.match(r"^(?:[0O](?:\.[0O])?|[1-7](?:\.\d+)*)\.?\s+[A-ZÀ-Þ]", value))


def formula_like(block: str) -> bool:
    lines = [line for line in block.splitlines() if line.strip()]
    if not lines:
        return False
    average_indent = sum(len(line) - len(line.lstrip()) for line in lines) / len(lines)
    symbol_count = sum(ch in MATH_TRIGGER for ch in block)
    return average_indent >= 7 and symbol_count > 0


def title_block(language: str) -> str:
    if language == "fr":
        return r"""
\begin{center}
{\small S\'eminaire Bourbaki, 31e ann\'ee, 1978/79, no 539 --- juin 1979}\par
\vspace{0.55em}
{\Large\bfseries SOMMES DE GAUSS CUBIQUES ET REV\^ETEMENTS DE $\operatorname{SL}(2)$,\par
D'APR\`ES S. J. PATTERSON}\par
\vspace{0.45em}{\normalsize par P. \textsc{Deligne}}\par
\end{center}
"""
    return r"""
\begin{center}
{\small Bourbaki Seminar, 31st year, 1978/79, no. 539 --- June 1979}\par
\vspace{0.55em}
{\Large\bfseries CUBIC GAUSS SUMS AND COVERS OF $\operatorname{SL}(2)$,\par
FOLLOWING S. J. PATTERSON}\par
\vspace{0.45em}{\normalsize by P. \textsc{Deligne}}\par
\end{center}
"""


def block_tex(block: str) -> str:
    if set(block.strip()) <= {"─", "-", " ", "\n"} and len(block.strip()) > 5:
        return "\\par\\medskip\\hrule\\medskip\n"
    if is_heading(block):
        heading = inline_tex(" ".join(block.split()))
        return f"\\par\\medskip\\noindent{{\\large\\bfseries {heading}}}\\par\\smallskip\n"
    lines = [line.rstrip() for line in block.splitlines() if line.strip()]
    if formula_like(block):
        body = r" \\ ".join(inline_tex(line.strip()) for line in lines)
        return "\\par\\smallskip\\begin{center}\\begin{minipage}{0.96\\textwidth}\\centering\n" + body + "\n\\end{minipage}\\end{center}\\smallskip\n"
    paragraph = join_source_lines(lines)
    match = re.match(r"^(\(?(?:\d+(?:\.\d+){1,3})\)?)(\s+)(.*)$", paragraph)
    if match:
        return f"\\par\\noindent\\textbf{{{tex_text(match.group(1))}}}\\quad {inline_tex(match.group(3))}\\par\n"
    return "\\par " + inline_tex(paragraph) + "\\par\n"


def page_body(record: dict, language: str) -> str:
    page = int(record["physical_page"])
    printed = int(record["printed_page"])
    text = str(record["text"])
    if language == "en" and page == 14:
        before = "identified with μ\nby 0.0.2."
        after = "identified with μ\nby (0.0.2)."
        assert text.count(before) == 1
        text = text.replace(before, after)
    blocks = [block for block in re.split(r"\n\s*\n", text) if block.strip()]
    blocks = [block for block in blocks if not is_scan_identifier(block, printed)]
    if page == 1:
        blocks = blocks[2:]
        prefix = title_block(language)
    else:
        prefix = ""
    rendered = prefix + "".join(block_tex(block) for block in blocks)
    return rendered


def preamble(title: str, subject: str, language: str, font_size: str) -> str:
    babel = "french,english" if language == "fr" else "english,french"
    return rf"""\documentclass[10pt,a4paper]{{article}}
\usepackage[margin=10mm,headheight=14pt,headsep=3mm,footskip=6mm]{{geometry}}
\usepackage{{fontspec}}
\setmainfont{{TeX Gyre Termes}}
\setsansfont{{TeX Gyre Heros}}
\usepackage{{mathtools}}
\usepackage{{unicode-math}}
\setmathfont{{TeX Gyre Termes Math}}
\usepackage[{babel}]{{babel}}
\usepackage{{microtype}}
\usepackage{{fancyhdr}}
\usepackage[hidelinks]{{hyperref}}
\hypersetup{{pdftitle={{{title}}},pdfauthor={{Pierre Deligne}},pdfsubject={{{subject}}}}}
\pagestyle{{fancy}}
\fancyhf{{}}
\renewcommand{{\headrulewidth}}{{0.2pt}}
\renewcommand{{\footrulewidth}}{{0pt}}
\setlength{{\parindent}}{{1em}}
\setlength{{\parskip}}{{0.08em}}
\emergencystretch=2em
\sloppy
\begin{{document}}
\fontsize{{{font_size}}}{{8.45pt}}\selectfont
"""


def page_header(page: int, printed: int, layer: str) -> str:
    label = {"fr": r"\'Edition fran\c{c}aise diplomatique", "en": "Standalone English translation", "app": "Restrained apparatus"}[layer]
    return rf"""
{'' if page == 1 else '\\clearpage'}
\fancyhead[L]{{\scriptsize D035 --- {label}}}
\fancyhead[R]{{\scriptsize authority physical {page} / printed {printed}}}
\fancyfoot[C]{{\scriptsize {printed}}}
\phantomsection\label{{d035-physical-{page:03d}}}
"""


def build_reader(layer: str, language: str, filename: str) -> None:
    recs = records(layer)
    if language == "fr":
        title = "Sommes de Gauss cubiques et revetements de SL(2), d'apres S. J. Patterson"
        subject = "D035 diplomatic French edition normalized from the frozen authority replay"
    else:
        title = "Cubic Gauss Sums and Covers of SL(2), following S. J. Patterson"
        subject = "D035 standalone English translation of the frozen diplomatic French"
    chunks = [preamble(title, subject, language, "7.35pt")]
    for rec in recs:
        page = int(rec["physical_page"])
        printed = int(rec["printed_page"])
        chunks.append(page_header(page, printed, language))
        chunks.append(page_body(rec, language))
    chunks.append("\\end{document}\n")
    (CANONICAL / filename).write_text("".join(chunks), encoding="utf-8", newline="\n")


def build_apparatus() -> None:
    recs = records("apparatus")
    title = "D035 restrained apparatus"
    chunks = [preamble(title, "Page-addressed authority, topology, attribution, variants, and fallback evidence", "en", "9.15pt")]
    for rec in recs:
        page = int(rec["physical_page"])
        printed = int(rec["printed_page"])
        chunks.append(page_header(page, printed, "app"))
        if page == 1:
            chunks.append(r"\begin{center}{\Large\bfseries D035 RESTRAINED APPARATUS}\par\smallskip{\normalsize Sommes de Gauss cubiques et rev\^etements de $\operatorname{SL}(2)$, d'apr\`es S. J. Patterson}\end{center}\medskip" + "\n")
            chunks.append(r"\noindent\textbf{Authority.} The 34-page Bourbaki no. 539 scan (SHA-256 \texttt{B65B3980...C0F}) controls. All physical pages are article pages and map one-to-one to printed 244--277. P. Deligne is the sole printed author; Patterson is subject attribution. The comparator and every inherited branch remain comparison-only or ZERO\_ACCEPTED." + "\n")
        chunks.append(block_tex(str(rec["text"])))
        if page == 34:
            chunks.append(r"\vfill\hrule\smallskip\noindent{\scriptsize The authority ends with bibliography entries [13]--[24], a horizontal rule, printed folio 277, blank remainder, and physical EOF.}" + "\n")
    chunks.append("\\end{document}\n")
    (CANONICAL / "D035_APPARATUS.tex").write_text("".join(chunks), encoding="utf-8", newline="\n")


def deterministic_zip(path: pathlib.Path, members: list[tuple[str, bytes]]) -> None:
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, data in sorted(members):
            info = zipfile.ZipInfo(name, (1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)


def preserve_witnesses() -> None:
    witness = CANONICAL / "witness"
    witness.mkdir(parents=True, exist_ok=True)
    mapping = {
        STATE / "source" / "20_AUTHORITY_DELIGNE_D035_BOURBAKI_539_34PP.pdf": (witness / "D035_AUTHORITY_34PP.pdf", AUTH_SHA),
        STATE / "comparison" / "21_COMPARATOR_DELIGNE_D035_COLLECTED_34PP.pdf": (witness / "D035_COMPARATOR_ONLY_34PP.pdf", COMP_SHA),
        STATE / "salvage" / "30_ZERO_ACCEPTED_DEDUP_PRIOR_WORK_DELIGNE_D035.zip": (witness / "D035_ZERO_ACCEPTED_PRIOR_WORK.zip", ZERO_SHA),
        STATE / "witnesses" / "31_ZERO_ACCEPTED_D035_ONLY_DIAGRAM_WITNESSES.zip": (witness / "D035_ZERO_ACCEPTED_DIAGRAM_WITNESSES.zip", WITNESS_SHA),
    }
    for source, (target, expected) in mapping.items():
        assert sha256(source) == expected
        shutil.copyfile(source, target)
        assert sha256(target) == expected

    members: list[tuple[str, bytes]] = []
    for prefix in ("raw_crops", "presentation_derivatives"):
        for source in sorted((STATE / "assets" / prefix).glob("*")):
            if source.is_file():
                members.append((f"{prefix}/{source.name}", source.read_bytes()))
    for rel in ("edition/asset_ledger.tsv", "control/PAGE_MAP.tsv", "control/D035_DIAGRAM_WITNESS_INVENTORY.tsv"):
        members.append((rel, (STATE / rel).read_bytes()))
    manifest_rows = ["path\tbytes\tsha256"]
    manifest_rows.extend(f"{name}\t{len(data)}\t{hashlib.sha256(data).hexdigest().upper()}" for name, data in sorted(members))
    members.append(("MANIFEST.tsv", ("\n".join(manifest_rows) + "\n").encode("utf-8")))
    deterministic_zip(witness / "D035_IMAGE_FALLBACKS.zip", members)


def main() -> None:
    assert sha256(STATE / "source" / "20_AUTHORITY_DELIGNE_D035_BOURBAKI_539_34PP.pdf") == AUTH_SHA
    build_reader("source_language", "fr", "D035_FR.tex")
    build_reader("english_standalone", "en", "D035_EN.tex")
    build_apparatus()
    preserve_witnesses()
    summary = {
        "authority_sha256": AUTH_SHA,
        "canonical_tex": {
            name: {"bytes": (CANONICAL / name).stat().st_size, "sha256": sha256(CANONICAL / name)}
            for name in ("D035_FR.tex", "D035_EN.tex", "D035_APPARATUS.tex")
        },
        "image_fallback_zip": {
            "bytes": (CANONICAL / "witness" / "D035_IMAGE_FALLBACKS.zip").stat().st_size,
            "sha256": sha256(CANONICAL / "witness" / "D035_IMAGE_FALLBACKS.zip"),
        },
        "schema": "d035-canonical-source-generation-v1",
        "source_pages": 34,
        "canonical_repairs": [
            {
                "edition": "english",
                "physical_page": 14,
                "repair": "restored parentheses around authority cross-reference (0.0.2)",
            }
        ],
        "status": "PASS",
    }
    (ROOT / "audit" / "SOURCE_GENERATION_RECEIPT.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()

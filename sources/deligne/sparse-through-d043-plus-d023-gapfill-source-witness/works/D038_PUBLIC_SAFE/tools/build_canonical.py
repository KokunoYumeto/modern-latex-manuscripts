#!/usr/bin/env python3
"""Build the D038 canonical TeX sources from the exact returned packet.

The input packet is immutable.  This generator validates every record and
authority-page derivative before it writes the candidate surface.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import pathlib
import re
import shutil
import zipfile
from collections import Counter

from PIL import Image, ImageChops


PACKET_NAME = "DELIGNE_D038_CRISTAUX_CANONIQUES_S10_CUMULATIVE_FULL_STATE.zip"
PACKET_BYTES = 105_436_323
PACKET_SHA256 = "E4AD47A2F0A0BB17B1613167BB45F99819B8A0FD63845B3A58C7A7A05E6E7696"
PACKET_MEMBERS = 741
AUTHORITY_SHA256 = "07B0FEA2D9A674C6DD4894E1A97A617C5DDBB6BDC2CB190DDBBC8F7A77856FD0"
COMPARATOR_SHA256 = "23CC548768092A07BCC0EAAB1B876856FA52559D91A5F3FC2844A7C84F9C4502"
EXPECTED_PAGES = 58

LAYERS = (
    (
        "source",
        "edition/source_language.ndjson",
        "D038_SOURCE_LANGUAGE_CANONICAL.tex",
        "Canonical source-language edition",
    ),
    (
        "english",
        "edition/english_standalone.ndjson",
        "D038_ENGLISH_CANONICAL.tex",
        "Canonical English edition",
    ),
    (
        "apparatus",
        "edition/apparatus.ndjson",
        "D038_RESTRAINED_APPARATUS.tex",
        "Restrained page-local apparatus",
    ),
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256_file(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def canonical_record_hash(record: dict) -> str:
    payload = dict(record)
    payload.pop("record_sha256", None)
    encoded = json.dumps(
        payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return sha256_bytes(encoded)


def load_ndjson(path: pathlib.Path) -> dict[int, dict]:
    records: dict[int, dict] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        record = json.loads(raw)
        page = int(record["physical_page"])
        if page in records:
            raise ValueError(f"duplicate physical page {page} in {path}")
        records[page] = record
    if sorted(records) != list(range(1, EXPECTED_PAGES + 1)):
        raise ValueError(f"incomplete page topology in {path}")
    return records


def load_tsv(path: pathlib.Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


LATEX_ESCAPES = {
    "\\": r"\textbackslash{}",
    "{": r"\{",
    "}": r"\}",
    "#": r"\#",
    "$": r"\$",
    "%": r"\%",
    "&": r"\&",
    "_": r"\_",
    "^": r"\textasciicircum{}",
    "~": r"\textasciitilde{}",
}


def tex_escape(text: str) -> str:
    return "".join(LATEX_ESCAPES.get(ch, ch) for ch in text)


MATH_MARKERS = set("=→←↦↪↘↙↔⇒⇔⇉≅≃≝≡∼⊂⊃⊆⊇∈∉∪∩⊗⊕∏∑∫∂√≤≥≠∞∇ΦφσΣΩωητμγδ∧∨∥∘∀⎧⎨⎩⎪│─↓↑⊥∤⟨⟩")
DIAGRAM_MARKERS = set("─│║↓↑↗↘↙")
COMBINING_MATH_MARKERS = {"\u0302", "\u0304", "\u0332"}
SUPERSCRIPTS = str.maketrans(
    {
        "⁰": "0",
        "¹": "1",
        "²": "2",
        "³": "3",
        "⁴": "4",
        "⁵": "5",
        "⁶": "6",
        "⁷": "7",
        "⁸": "8",
        "⁹": "9",
        "⁺": "+",
        "⁻": "-",
        "ⁿ": "n",
        "ⁱ": "i",
        "ʲ": "j",
        "ᵏ": "k",
        "ˡ": "l",
        "ᵐ": "m",
        "ᵍ": "g",
        "ᵒ": "o",
        "ᵖ": "p",
        "ᶠ": "f",
        "ʳ": "r",
        "ˢ": "s",
        "ʰ": "h",
        "ᵗ": "t",
        "ᵘ": "u",
        "ᵛ": "v",
        "ʷ": "w",
        "ˣ": "x",
        "ʸ": "y",
        "ᶻ": "z",
    }
)
SUBSCRIPTS = str.maketrans(
    {
        "₀": "0",
        "₁": "1",
        "₂": "2",
        "₃": "3",
        "₄": "4",
        "₅": "5",
        "₆": "6",
        "₇": "7",
        "₈": "8",
        "₉": "9",
        "₊": "+",
        "₋": "-",
        "₌": "=",
        "₍": "(",
        "₎": ")",
        "ₐ": "a",
        "ₑ": "e",
        "ₕ": "h",
        "ᵢ": "i",
        "ⱼ": "j",
        "ₖ": "k",
        "ₗ": "l",
        "ₘ": "m",
        "ₙ": "n",
        "ₒ": "o",
        "ₚ": "p",
        "ᵣ": "r",
        "ₛ": "s",
        "ₜ": "t",
        "ᵤ": "u",
        "ᵥ": "v",
        "ₓ": "x",
    }
)
UNICODE_MATH = {
    "→": r"\to",
    "←": r"\leftarrow",
    "↦": r"\mapsto",
    "↪": r"\hookrightarrow",
    "↔": r"\leftrightarrow",
    "⇒": r"\Rightarrow",
    "⇔": r"\Leftrightarrow",
    "⇉": r"\rightrightarrows",
    "↗": r"\nearrow",
    "↘": r"\searrow",
    "↙": r"\swarrow",
    "↓": r"\downarrow",
    "↑": r"\uparrow",
    "≅": r"\cong",
    "≃": r"\simeq",
    "≝": r"\coloneqq",
    "≡": r"\equiv",
    "∼": r"\sim",
    "⊂": r"\subset",
    "⊃": r"\supset",
    "⊆": r"\subseteq",
    "⊇": r"\supseteq",
    "∈": r"\in",
    "∉": r"\notin",
    "∪": r"\cup",
    "∩": r"\cap",
    "⊗": r"\otimes",
    "⊕": r"\oplus",
    "∏": r"\prod",
    "∑": r"\sum",
    "∫": r"\int",
    "∂": r"\partial",
    "≤": r"\leq",
    "≥": r"\geq",
    "≠": r"\neq",
    "∞": r"\infty",
    "∇": r"\nabla",
    "Φ": r"\Phi",
    "φ": r"\varphi",
    "σ": r"\sigma",
    "Σ": r"\Sigma",
    "Ω": r"\Omega",
    "ω": r"\omega",
    "η": r"\eta",
    "τ": r"\tau",
    "μ": r"\mu",
    "γ": r"\gamma",
    "δ": r"\delta",
    "α": r"\alpha",
    "β": r"\beta",
    "χ": r"\chi",
    "ε": r"\varepsilon",
    "θ": r"\theta",
    "ξ": r"\xi",
    "ψ": r"\psi",
    "λ": r"\lambda",
    "∧": r"\wedge",
    "∨": r"\vee",
    "⊥": r"\perp",
    "∥": r"\parallel",
    "∘": r"\circ",
    "∀": r"\forall",
    "∤": r"\nmid",
    "⟨": r"\langle",
    "⟩": r"\rangle",
    "ℚ": r"\mathbb{Q}",
    "ℤ": r"\mathbb{Z}",
    "ℕ": r"\mathbb{N}",
    "𝒪": r"\mathcal{O}",
    "Ĝ": r"\widehat{G}",
    "ℓ": r"\ell",
    "×": r"\times",
    "⋂": r"\bigcap",
    "⋃": r"\bigcup",
    "⋯": r"\cdots",
    "…": r"\ldots",
    "−": "-",
    "•": r"\bullet",
    "′": r"^{\prime}",
}
UNICODE_MATH = {
    char: (command + "{}" if re.fullmatch(r"\\[A-Za-z]+", command) else command)
    for char, command in UNICODE_MATH.items()
}
ROMAN_OPERATORS = {
    "Spf",
    "Spec",
    "Ker",
    "Im",
    "Hom",
    "Ext",
    "End",
    "Frob",
    "Fil",
    "Gr",
    "Pic",
    "Gal",
    "rank",
    "dim",
    "log",
    "exp",
    "lim",
    "mod",
    "rg",
    "id",
}
INLINE_VARIABLES = set("BCDEFGHKLMNOPQRSTUVWXYZbdefghijklmnpqrstuvwxyz")
SCRIPT_SUPER_CHARS = {chr(codepoint) for codepoint in SUPERSCRIPTS}
SCRIPT_SUB_CHARS = {chr(codepoint) for codepoint in SUBSCRIPTS}


def _placeholder(commands: list[str], command: str) -> str:
    if re.fullmatch(r"\\[A-Za-z]+", command):
        command += "{}"
    commands.append(command)
    return f"\ue000{len(commands) - 1}\ue001"


def _normalize_unicode_scripts(text: str) -> str:
    result: list[str] = []
    index = 0
    while index < len(text):
        char = text[index]
        if char in SCRIPT_SUPER_CHARS:
            end = index
            while end < len(text) and text[end] in SCRIPT_SUPER_CHARS:
                end += 1
            result.append("^{" + text[index:end].translate(SUPERSCRIPTS) + "}")
            index = end
        elif char in SCRIPT_SUB_CHARS:
            end = index
            while end < len(text) and text[end] in SCRIPT_SUB_CHARS:
                end += 1
            result.append("_{" + text[index:end].translate(SUBSCRIPTS) + "}")
            index = end
        else:
            result.append(char)
            index += 1
    return "".join(result)


def _normalize_ascii_scripts(text: str) -> str:
    text = re.sub(r"_\(([^()]*)\)", r"_{(\1)}", text)
    text = re.sub(r"\^\(([^()]*)\)", r"^{(\1)}", text)
    text = re.sub(r"_\[([^\[\]]*)\]", r"_{[\1]}", text)
    text = re.sub(r"\^\[([^\[\]]*)\]", r"^{[\1]}", text)
    text = re.sub(r"_([A-Za-z]+)", r"_{\1}", text)
    text = re.sub(r"\^\*", r"^{*}", text)
    text = re.sub(r"\^(contin|conn|et|can|dfn)", r"^{\1}", text)
    text = re.sub(r"\^([A-Za-z0-9+\-])", r"^{\1}", text)
    return text


def math_tex(text: str) -> str:
    """Convert an authority transcription formula line to real LaTeX math."""
    if re.fullmatch(r"[A-Z]+(?:_[A-Z]+){2,}", text.strip()):
        return r"\text{" + tex_escape(text.strip()) + "}"
    commands: list[str] = []
    text = text.strip()
    # A Unicode numeric subscript followed by a bare star denotes direct
    # image (for example f₀*); other bare postfix stars denote pullback.
    # Preserve the direct-image subscript before generic script conversion.
    subscript_class = re.escape("".join(sorted(SCRIPT_SUB_CHARS)))
    text = re.sub(
        rf"([A-Za-z])([{subscript_class}]+)\*",
        lambda match: _placeholder(
            commands,
            f"{match.group(1)}_{{{match.group(2).translate(SUBSCRIPTS)}*}}",
        ),
        text,
    )
    # Compact authority-transcription sequences confirmed on physical
    # pages 4, 5, 50, and 51: these are indexed exponents, not products.
    for encoded, latex in {
        "ᵐ¹": r"^{m_{1}}",
        "ᵐⁿ": r"^{m_{n}}",
        "ⁿ¹": r"^{n_{1}}",
        "ⁿ²": r"^{n_{2}}",
    }.items():
        text = text.replace(encoded, _placeholder(commands, latex))
    text = re.sub(
        r"([A-Za-z])'\^",
        lambda match: _placeholder(commands, rf"\widehat{{{match.group(1)}^{{\prime}}}}"),
        text,
    )
    text = re.sub(
        r"(?<=[A-Za-zΑ-ω])'(?=(?:[₀-₉ₐ-ₜᵢⱼᵣₓ⁰-⁹ᵃ-ᶻ_^(*),=\s]|$))",
        "′",
        text,
    )
    text = text.replace("⊗̂", _placeholder(commands, r"\widehat{\otimes}"))
    text = re.sub(r"([A-Za-z])\u0302", lambda match: _placeholder(commands, rf"\widehat{{{match.group(1)}}}"), text)
    text = re.sub(r"([A-Za-z])\u0304", lambda match: _placeholder(commands, rf"\overline{{{match.group(1)}}}"), text)
    text = re.sub(r"([A-Za-z])\u0332", lambda match: _placeholder(commands, rf"\underline{{{match.group(1)}}}"), text)
    text = re.sub(r"─+→", lambda _: _placeholder(commands, r"\longrightarrow"), text)
    text = re.sub(r"←─+", lambda _: _placeholder(commands, r"\longleftarrow"), text)
    text = re.sub(r"─+", lambda _: _placeholder(commands, r"\text{---}"), text)
    text = text.replace(r"\overset{dfn}{=}", _placeholder(commands, r"\overset{\mathrm{dfn}}{=}"))
    braced: list[str] = []
    brace_stack: list[bool] = []
    for index, char in enumerate(text):
        if char == "{":
            structural = index > 0 and text[index - 1] in "_^"
            brace_stack.append(structural)
            braced.append(char if structural else _placeholder(commands, r"\lbrace"))
        elif char == "}":
            structural = brace_stack.pop() if brace_stack else False
            braced.append(char if structural else _placeholder(commands, r"\rbrace"))
        else:
            braced.append(char)
    text = "".join(braced)
    text = _normalize_unicode_scripts(text)
    text = _normalize_ascii_scripts(text)
    text = re.sub(r"(?<=[A-Za-z0-9À-ÖØ-öø-ÿΑ-ω})])\*", r"^{*}", text)
    for char, command in UNICODE_MATH.items():
        text = text.replace(char, _placeholder(commands, command))
    text = text.replace("│", _placeholder(commands, r"\downarrow"))
    text = text.replace("║", _placeholder(commands, r"\Vert"))
    text = text.replace("⎧", "").replace("⎨", "").replace("⎩", "").replace("⎪", "")
    text = text.replace("&", _placeholder(commands, r"\&"))
    text = text.replace("%", _placeholder(commands, r"\%"))
    text = text.replace("#", _placeholder(commands, r"\#"))
    text = text.replace("$", _placeholder(commands, r"\$"))

    def word_replace(match: re.Match[str]) -> str:
        word = match.group(0)
        before = text[: match.start()]
        in_script = before.endswith("_{") or before.endswith("^{")
        if word in ROMAN_OPERATORS:
            return _placeholder(commands, rf"\operatorname{{{word}}}")
        if word in {"Fa", "Fb", "Ff", "pb", "sd", "ba", "dx", "rq", "id"}:
            return r"\,".join(word)
        if (in_script and len(word) > 1) or (len(word) > 1 and word.isupper()) or word in {"can", "conn", "contin", "et", "DR", "PD", "NS", "dfn", "gp"}:
            return _placeholder(commands, rf"\mathrm{{{word}}}")
        if len(word) == 1 and word.isascii():
            return word
        return _placeholder(commands, rf"\text{{{tex_escape(word)}}}")

    text = re.sub(r"[A-Za-zÀ-ÖØ-öø-ÿ]+", word_replace, text)
    text = re.sub(r" {8,}", r"\\qquad\\qquad ", text)
    text = re.sub(r" {4,7}", r"\\qquad ", text)
    text = re.sub(r" {2,3}", r"\\quad ", text)
    text = text.replace(" ", r"\,")
    for index, command in enumerate(commands):
        text = text.replace(f"\ue000{index}\ue001", command)
    text = re.sub(
        r"\^\{\\prime\}_\{([^{}]*)\}\^\{([^{}]*)\}",
        lambda match: "_{" + match.group(1) + "}^{\\prime\\," + match.group(2) + "}",
        text,
    )
    text = re.sub(
        r"\^\{\\prime\}\^\{([^{}]*)\}",
        lambda match: "^{\\prime\\," + match.group(1) + "}",
        text,
    )
    text = text.replace(r"^{\prime}^{*}", r"^{\prime *}")
    text = text.replace(r"\Sigma{}_{", r"\sum_{")
    return text


def is_math_token(token: str) -> bool:
    core = token.strip(".,;:!?()[]‘’“”\"'")
    if not core:
        return False
    if any(char in MATH_MARKERS or char in UNICODE_MATH or char in SCRIPT_SUPER_CHARS or char in SCRIPT_SUB_CHARS or char in COMBINING_MATH_MARKERS for char in core):
        return True
    if any(char in core for char in "_^"):
        return True
    if "\\" in core:
        return True
    if core in INLINE_VARIABLES or core in ROMAN_OPERATORS:
        return True
    if re.match(r"^(?:Spf|Spec|Ker|Im|Hom|Ext|End|Frob|Fil|Gr|Pic|Gal|H|X|Y|Z|A|M|W|F|L|U|P|T|D|E|G|R|S)[(_{]", core):
        return True
    if re.match(r"^[A-Za-zΑ-ω]+\([^)]*\)$", core) and any(ch.isupper() for ch in core[:2]):
        return True
    if re.match(r"^[A-Za-zΑ-ω](?:,[A-Za-zΑ-ω])+$", core):
        return True
    if re.match(r"^[A-Za-zΑ-ω]{1,3}/[A-Za-zΑ-ω]{1,3}$", core):
        return True
    return False


def render_inline_text(text: str) -> str:
    pieces = re.split(r"(\s+)", text)
    rendered: list[str] = []
    for piece_index, piece in enumerate(pieces):
        if not piece:
            continue
        if piece.isspace():
            rendered.append(" ")
            continue
        leading_match = re.match(r"^[‘“\"]*", piece)
        trailing_match = re.search(r"[.,;:!?\u2019”\"]*$", piece)
        leading = leading_match.group(0) if leading_match else ""
        trailing = trailing_match.group(0) if trailing_match else ""
        core_end = len(piece) - len(trailing) if trailing else len(piece)
        core = piece[len(leading) : core_end]
        if core.startswith("'") and core.endswith("'") and is_math_token(core[1:-1]):
            core = core[1:-1]
            leading += "'"
            trailing = "'" + trailing
        if core.endswith("'s") and is_math_token(core[:-2]):
            core = core[:-2]
            trailing = "'s" + trailing
        contextual_variable = False
        if core in {"A", "I", "J", "Q"}:
            neighbors: list[str] = []
            for direction in (-1, 1):
                neighbor_index = piece_index + direction
                while 0 <= neighbor_index < len(pieces) and pieces[neighbor_index].isspace():
                    neighbor_index += direction
                if 0 <= neighbor_index < len(pieces):
                    neighbors.append(pieces[neighbor_index].strip(".,;:!?()[]‘’“”\"'"))
            contextual_variable = any(
                any(char in MATH_MARKERS or char in UNICODE_MATH for char in neighbor)
                or any(char in neighbor for char in "=_^/")
                for neighbor in neighbors
            )
        if core and (is_math_token(core) or contextual_variable):
            rendered.append(tex_escape(leading) + r"\(" + math_tex(core) + r"\)" + tex_escape(trailing))
        else:
            rendered.append(tex_escape(piece))
    return "".join(rendered)


def is_heading(block: str) -> bool:
    compact = " ".join(line.strip() for line in block.splitlines())
    if not compact or len(compact) > 125:
        return False
    if any(ch in MATH_MARKERS for ch in compact) or any(token in compact for token in ("=", "→", "⊂", "∈")):
        return False
    letters = [ch for ch in compact if ch.isalpha()]
    uppercase = bool(letters) and sum(ch.isupper() for ch in letters) / len(letters) > 0.78
    enumerated = bool(re.match(r"^\d+(?:\.\d+)*\.?\s+[A-Za-zÀ-ÿ]", compact)) and len(compact.split()) <= 14
    return uppercase or enumerated


def is_result_prose(block: str) -> bool:
    compact = " ".join(line.strip() for line in block.splitlines())
    return bool(
        re.match(
            r"^(?:THÉORÈME|THEOREM|PROPOSITION|COROLLAIRE|COROLLARY|LEMME|LEMMA|REMARQUE|REMARK|DÉFINITION|DEFINITION|PROOF|DÉMONSTRATION|UNIQUENESS LEMMA|FURTHER COROLLARY)\b",
            compact,
            flags=re.IGNORECASE,
        )
    )


def is_display_math(block: str) -> bool:
    lines = block.splitlines()
    longest = max((len(line) for line in lines), default=0)
    if any(char in block for char in DIAGRAM_MARKERS):
        return True
    math_count = sum(
        ch in MATH_MARKERS or ch in UNICODE_MATH or ch in SCRIPT_SUPER_CHARS or ch in SCRIPT_SUB_CHARS or ch in COMBINING_MATH_MARKERS or ch in "_^"
        for ch in block
    )
    if len(lines) == 1:
        words = len(block.split())
        numbered_formula = bool(
            re.match(r"^\s*(?:\([0-9.*]+\)|[0-9]+(?:\.[0-9]+){1,4})\s{2,}", block)
        )
        relational_formula = any(char in block for char in "=→←↔≅≃≝≡⊂⊃⊆⊇∈∉≤≥≠")
        leading_word = re.match(r"^\s*[\(\[\"']*([A-Za-zÀ-ÖØ-öø-ÿ]+)", block)
        starts_mathish = not leading_word or len(leading_word.group(1)) == 1 or leading_word.group(1) in ROMAN_OPERATORS or leading_word.group(1).isupper()
        if numbered_formula or (relational_formula and starts_mathish and words <= 24 and len(block) <= 260):
            return True
    if any(line.startswith(("    ", "\t")) for line in lines) and math_count and longest <= 125:
        return True
    return False


def render_math_block(block: str) -> str:
    raw_lines = [line.rstrip() for line in block.splitlines() if line.strip()]
    has_brace = any(line.lstrip().startswith(("⎧", "⎨", "⎩", "⎪")) for line in raw_lines)
    is_diagram = any(char in block for char in DIAGRAM_MARKERS)
    if has_brace:
        lines = [converted for line in raw_lines if (converted := math_tex(line))]
        body = r"\\".join(r"& " + line for line in lines)
        return "\\begin{CanonMathBlock}\n\\left\\{\\begin{aligned}\n" + body + "\n\\end{aligned}\\right.\n\\end{CanonMathBlock}"
    if is_diagram:
        split_lines = [re.split(r"\s{2,}", line.strip()) for line in raw_lines]
        columns = max(len(cells) for cells in split_lines)
        rows = []
        for cells in split_lines:
            cells = cells + [""] * (columns - len(cells))
            rows.append(" & ".join(math_tex(cell) if cell else "{}" for cell in cells))
        spec = "c" * columns
        return "\\begin{CanonMathBlock}\n\\begin{array}{" + spec + "}\n" + "\\\\\n".join(rows) + "\n\\end{array}\n\\end{CanonMathBlock}"
    lines = [math_tex(line) for line in raw_lines]
    if len(lines) == 1:
        return r"\CanonDisplay{" + lines[0] + "}"
    return "\\begin{CanonMathBlock}\n\\begin{aligned}\n" + "\\\\\n".join("& " + line for line in lines) + "\n\\end{aligned}\n\\end{CanonMathBlock}"


def render_text(text: str, source_replay: bool, apparatus: bool) -> str:
    blocks = text.replace("\r\n", "\n").replace("\r", "\n").split("\n\n")
    rendered: list[str] = []
    for raw_block in blocks:
        block = raw_block.strip("\n")
        if not block:
            continue
        if is_heading(block) and not apparatus:
            joined = " ".join(line.strip() for line in block.splitlines())
            rendered.append(r"\CanonHeading{" + render_inline_text(joined) + "}")
        elif is_result_prose(block) and not apparatus:
            inline_lines = [render_inline_text(line.strip()) for line in block.splitlines()]
            rendered.append(r"\CanonText{" + r"\\".join(inline_lines) + "}")
        elif is_display_math(block) and not apparatus:
            rendered.append(render_math_block(block))
        else:
            inline_lines = [render_inline_text(line.strip()) for line in block.splitlines()]
            rendered.append(r"\CanonText{" + r"\\".join(inline_lines) + "}")
    return "\n".join(rendered)


def tex_preamble(title: str, layer: str) -> str:
    accent = {"source": "1E4D5B", "english": "244A73", "apparatus": "5B4636"}[layer]
    trailer_id = hashlib.sha256(f"D038-canonical-{layer}-v2".encode("ascii")).hexdigest().upper()[:32]
    return rf"""% D038 canonical TeX source; generated deterministically from the returned packet.
% No inherited audit or comparator byte is accepted as editorial content.
\documentclass[9pt]{{article}}
\pdfvariable trailerid {{[<{trailer_id}><{trailer_id}>]}}
\usepackage[paperwidth=461bp,paperheight=684bp,top=22pt,bottom=22pt,left=28pt,right=28pt]{{geometry}}
\usepackage{{fontspec}}
\usepackage{{amsmath}}
\usepackage{{amssymb}}
\usepackage{{mathtools}}
\usepackage{{unicode-math}}
\usepackage{{graphicx}}
\usepackage{{xcolor}}
\usepackage{{ragged2e}}
\usepackage{{microtype}}
\setmainfont{{DejaVu Serif}}
\setsansfont{{DejaVu Sans}}
\setmathfont{{DejaVu Math TeX Gyre}}
\definecolor{{Accent}}{{HTML}}{{{accent}}}
\definecolor{{Quiet}}{{HTML}}{{5F6870}}
\pagestyle{{empty}}
\setlength{{\parindent}}{{0pt}}
\setlength{{\parskip}}{{0pt}}
\emergencystretch=2em
\hfuzz=1.5pt
\vfuzz=1.5pt
\hbadness=10000
\vbadness=10000
\newcommand{{\CanonHeading}}[1]{{\par\vspace{{1.5pt}}{{\fontsize{{8.6}}{{10.0}}\selectfont\sffamily\bfseries\color{{Accent}} #1\par}}\vspace{{1.5pt}}}}
\newcommand{{\CanonText}}[1]{{\par{{\fontsize{{8.0}}{{9.35}}\selectfont\RaggedRight #1\par}}\vspace{{2.2pt}}}}
\newcommand{{\CanonDisplay}}[1]{{\par\vspace{{1.2pt}}\begin{{center}}{{\fontsize{{7.2}}{{8.4}}\selectfont\(\displaystyle #1\)}}\end{{center}}\vspace{{1.2pt}}}}
\newenvironment{{CanonMathBlock}}{{\par\vspace{{1.2pt}}\begin{{center}}\fontsize{{6.8}}{{8.0}}\selectfont\(\displaystyle}}{{\)\end{{center}}\vspace{{1.2pt}}}}
\newcommand{{\LayerTitle}}{{{tex_escape(title)}}}
\begin{{document}}
"""


def tex_page(layer: str, record: dict, page_map: dict[str, str], last: bool) -> str:
    page = int(record["physical_page"])
    printed = int(record["printed_page"])
    if page <= 48:
        zone = "French main exposition"
        operation = "diplomatic source" if layer == "source" else "translation from frozen French"
    else:
        zone = "Katz appendix - English source"
        operation = "source replay (not translation)"
    if layer == "apparatus":
        operation = "page-local note"
    source_replay = page >= 49 and layer in ("source", "english")
    body = render_text(record["text"], source_replay=source_replay, apparatus=(layer == "apparatus"))
    fallback = f"assets/authority_pages/p{page:03d}.png"
    source_record = record.get("source_record_sha256", record.get("record_sha256", ""))
    record_hash = record["record_sha256"]
    next_page = "\n\\newpage\n" if not last else "\n"
    return rf"""% CANONICAL_PAGE physical={page:03d} printed={printed} layer={layer}
% RECORD_SHA256 {record_hash}
% SOURCE_RECORD_SHA256 {source_record}
\noindent\begin{{minipage}}[t][\dimexpr\textheight-5pt\relax][t]{{\textwidth}}
{{\sffamily\fontsize{{7.3}}{{8.2}}\selectfont\color{{Quiet}} D038 / physical {page:02d} / authority printed {printed}\hfill {tex_escape(zone)}}}
\par\vspace{{2.2pt}}{{\color{{Accent}}\hrule height 0.55pt}}\vspace{{4.5pt}}
{{\sffamily\fontsize{{10.4}}{{11.6}}\selectfont\bfseries\color{{Accent}} \LayerTitle}}
\par{{\sffamily\fontsize{{6.7}}{{7.7}}\selectfont\color{{Quiet}} {tex_escape(operation)}; exact one-page correspondence to authority physical {page}}}
\vspace{{5pt}}
{body}
\vfill
{{\color{{Accent}}\hrule height 0.35pt}}\vspace{{3pt}}
\noindent{{\sffamily\fontsize{{6.0}}{{7.0}}\selectfont\color{{Quiet}}
Layout/math fallback asset (evidence only; not reader prose): \texttt{{{tex_escape(fallback)}}}. Full-resolution image retained beside this TeX source; running headers, printed folios, and scanner/library copy matter are excluded from canonical prose.\\
Record: \texttt{{{record_hash[:16]}}}\ldots\quad Authority evidence: \texttt{{{record.get('authority_evidence_sha256', page_map.get('authority_evidence_sha256', ''))[:16]}}}\ldots}}
\end{{minipage}}{next_page}"""


def validate_packet(packet_zip: pathlib.Path, packet_root: pathlib.Path) -> dict:
    if packet_zip.stat().st_size != PACKET_BYTES:
        raise ValueError("packet byte count mismatch")
    if sha256_file(packet_zip) != PACKET_SHA256:
        raise ValueError("packet SHA-256 mismatch")
    with zipfile.ZipFile(packet_zip) as archive:
        infos = archive.infolist()
        if len(infos) != PACKET_MEMBERS:
            raise ValueError("packet member count mismatch")
        if archive.testzip() is not None:
            raise ValueError("packet CRC failure")
        names = [entry.filename for entry in infos]
        if len(names) != len(set(names)):
            raise ValueError("duplicate ZIP member names")
        for name in names:
            normalized = pathlib.PurePosixPath(name)
            if normalized.is_absolute() or ".." in normalized.parts or "\\" in name:
                raise ValueError(f"unsafe ZIP member path: {name!r}")
    control = json.loads((packet_root / "controls/authority_contract.json").read_text(encoding="utf-8"))
    if control["authority_sha256"] != AUTHORITY_SHA256 or control["authority_pages"] != EXPECTED_PAGES:
        raise ValueError("authority contract mismatch")
    if control["comparator_sha256"] != COMPARATOR_SHA256 or control["comparator_role"] != "COMPARISON_ONLY":
        raise ValueError("comparator boundary mismatch")
    if control["prior_acceptance"] != "ZERO_ACCEPTED":
        raise ValueError("inherited acceptance boundary mismatch")
    return control


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=pathlib.Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    packet_root = root / "input/packet"
    packet_zip = root / "input" / PACKET_NAME
    candidate = root / "candidate"
    assets = candidate / "assets/authority_pages"
    manifests = root / "manifests"
    candidate.mkdir(parents=True, exist_ok=True)
    assets.mkdir(parents=True, exist_ok=True)
    manifests.mkdir(parents=True, exist_ok=True)

    control = validate_packet(packet_zip, packet_root)
    page_map_rows = load_tsv(packet_root / "controls/page_map.tsv")
    coverage_rows = load_tsv(packet_root / "state/coverage.tsv")
    if len(page_map_rows) != EXPECTED_PAGES or len(coverage_rows) != EXPECTED_PAGES:
        raise ValueError("control table page count mismatch")

    records_by_layer: dict[str, dict[int, dict]] = {}
    for layer, rel, _, _ in LAYERS:
        records_by_layer[layer] = load_ndjson(packet_root / rel)

    content_rows: list[dict[str, object]] = []
    fallback_rows: list[dict[str, object]] = []
    pixel_modes = Counter()
    for page in range(1, EXPECTED_PAGES + 1):
        row = page_map_rows[page - 1]
        coverage = coverage_rows[page - 1]
        if int(row["physical_page"]) != page or int(row["printed_page"]) != page + 79:
            raise ValueError(f"page-map topology mismatch at {page}")
        if int(coverage["physical_page"]) != page or int(coverage["printed_page"]) != page + 79:
            raise ValueError(f"coverage topology mismatch at {page}")
        expected_lang = "FRENCH" if page <= 48 else "ENGLISH"
        if row["source_language_zone"].split("_")[0] != expected_lang:
            raise ValueError(f"language boundary mismatch at {page}")

        source_record = records_by_layer["source"][page]
        english_record = records_by_layer["english"][page]
        apparatus_record = records_by_layer["apparatus"][page]
        for layer, record, coverage_key in (
            ("source", source_record, "source_sha256"),
            ("english", english_record, "english_sha256"),
            ("apparatus", apparatus_record, "apparatus_sha256"),
        ):
            if record["status"] != "COMPLETE" or int(record["printed_page"]) != page + 79:
                raise ValueError(f"incomplete {layer} record at {page}")
            computed = canonical_record_hash(record)
            if computed != record["record_sha256"] or computed != coverage[coverage_key]:
                raise ValueError(f"record hash mismatch: {layer} page {page}")
            content_rows.append(
                {
                    "layer": layer,
                    "physical_page": page,
                    "printed_page": page + 79,
                    "text_sha256": sha256_bytes(record["text"].encode("utf-8")),
                    "record_sha256": record["record_sha256"],
                    "source_record_sha256": record.get("source_record_sha256", record["record_sha256"]),
                    "status": "VERIFIED_FROM_PACKET",
                }
            )

        if source_record["source_language"] != expected_lang:
            raise ValueError(f"source language mismatch at {page}")
        expected_operation = "TRANSLATION_FROM_FRENCH" if page <= 48 else "SOURCE_ALREADY_ENGLISH_REPLAY"
        if english_record["english_operation"] != expected_operation:
            raise ValueError(f"English operation mismatch at {page}")
        if page >= 49 and source_record["text"] != english_record["text"]:
            raise ValueError(f"already-English replay changed at {page}")
        if english_record["source_record_sha256"] != source_record["record_sha256"]:
            raise ValueError(f"source/English linkage mismatch at {page}")
        if apparatus_record["source_record_sha256"] != source_record["record_sha256"]:
            raise ValueError(f"source/apparatus linkage mismatch at {page}")
        if apparatus_record["english_record_sha256"] != english_record["record_sha256"]:
            raise ValueError(f"English/apparatus linkage mismatch at {page}")

        evidence = packet_root / source_record["authority_evidence_path"]
        if sha256_file(evidence) != source_record["authority_evidence_sha256"]:
            raise ValueError(f"authority evidence hash mismatch at {page}")
        png = packet_root / source_record["facsimile_path"]
        tif = packet_root / f"evidence/authority_pages/decoded_tiff/p{page:03d}.tif"
        if sha256_file(png) != source_record["facsimile_sha256"]:
            raise ValueError(f"presentation image hash mismatch at {page}")
        with Image.open(png) as png_image, Image.open(tif) as tif_image:
            png_image.load()
            tif_image.load()
            if png_image.size != (1920, 2850) or tif_image.size != (1920, 2850):
                raise ValueError(f"authority image dimensions mismatch at {page}")
            a = png_image.convert("1")
            b = tif_image.convert("1")
            if ImageChops.difference(a, b).getbbox() is not None:
                raise ValueError(f"authority PNG/TIFF pixel mismatch at {page}")
            pixel_modes[png_image.mode] += 1
        dest = assets / f"p{page:03d}.png"
        shutil.copyfile(png, dest)
        if sha256_file(dest) != sha256_file(png):
            raise ValueError(f"fallback copy mismatch at {page}")
        fallback_rows.append(
            {
                "physical_page": page,
                "printed_page": page + 79,
                "relative_path": dest.relative_to(candidate).as_posix(),
                "bytes": dest.stat().st_size,
                "sha256": sha256_file(dest),
                "pixel_dimensions": "1920x2850",
                "role": "AUTHORITY_LAYOUT_MATH_IMAGE_FALLBACK",
                "accepted_editorial_bytes": 0,
            }
        )

    # Literal high-risk invariants are checked directly from packet text.
    src = records_by_layer["source"]
    eng = records_by_layer["english"]
    literals = {
        "source_001_title": (src[1]["text"], "CRISTAUX ORDINAIRES ET COORDONNÉES CANONIQUES"),
        "source_001_credit": (src[1]["text"], "avec la collaboration de L. ILLUSIE (*)"),
        "english_001_title": (eng[1]["text"], "ORDINARY CRYSTALS AND CANONICAL COORDINATES"),
        "boundary_049_author": (src[49]["text"], "Nicholas M. Katz"),
        "p055_authority_missing_star": (src[55]["text"], "Φ_can(q_{ij}^(σ)) = (q_{ij})ᵖ"),
        "p057_repeated_left_operand": (src[57]["text"], "F(Φ_can)Φ_can*((Fil²)^(σ)) ⊂ Fil¹"),
        "p058_terminal_star": (src[58]["text"], "Φ_can*(q_i^(σ)) = (q_i)ᵖ"),
        "p058_terminal_qed": (src[58]["text"], "Q.E.D."),
    }
    for label, (haystack, needle) in literals.items():
        if needle not in haystack:
            raise ValueError(f"missing high-risk literal invariant: {label}")

    for layer, _, tex_name, title in LAYERS:
        records = records_by_layer[layer]
        parts = [tex_preamble(title, layer)]
        for page in range(1, EXPECTED_PAGES + 1):
            parts.append(tex_page(layer, records[page], page_map_rows[page - 1], page == EXPECTED_PAGES))
        parts.append("\\end{document}\n")
        tex_path = candidate / tex_name
        tex_path.write_text("".join(parts), encoding="utf-8", newline="\n")

    def write_tsv(path: pathlib.Path, rows: list[dict[str, object]]) -> None:
        fields = list(rows[0])
        with path.open("w", encoding="utf-8", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)

    write_tsv(candidate / "CONTENT_MAP.tsv", content_rows)
    write_tsv(candidate / "IMAGE_FALLBACK_MANIFEST.tsv", fallback_rows)

    generation_files = [candidate / item[2] for item in LAYERS] + [
        candidate / "CONTENT_MAP.tsv",
        candidate / "IMAGE_FALLBACK_MANIFEST.tsv",
    ]
    receipt = {
        "schema": "d038-canonical-generation-v1",
        "status": "PASS",
        "packet": {
            "file": PACKET_NAME,
            "bytes": PACKET_BYTES,
            "sha256": PACKET_SHA256,
            "members": PACKET_MEMBERS,
        },
        "authority": {
            "sha256": control["authority_sha256"],
            "pages": control["authority_pages"],
            "role": "CONTROLLING_AUTHORITY",
        },
        "comparator": {
            "sha256": control["comparator_sha256"],
            "pages": control["comparator_pages"],
            "role": "COMPARISON_ONLY",
            "accepted_bytes": 0,
        },
        "inherited_exact_work": "ZERO_ACCEPTED",
        "page_topology": {"physical": [1, 58], "printed": [80, 137], "count": 58},
        "source_language_boundary": {"French": [1, 48], "English_Katz_appendix": [49, 58]},
        "copy_matter_policy": "EXCLUDED_FROM_READER_PROSE; AUTHORITY_IMAGE_FALLBACK_IDENTIFIED_AS_EVIDENCE",
        "fallbacks": {"count": len(fallback_rows), "dimensions": "1920x2850", "pixel_modes": dict(pixel_modes)},
        "generated_files": [
            {
                "path": path.relative_to(root).as_posix(),
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            }
            for path in generation_files
        ],
    }
    receipt_path = manifests / "GENERATION_RECEIPT.json"
    receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print("PASS_GENERATION")


if __name__ == "__main__":
    main()

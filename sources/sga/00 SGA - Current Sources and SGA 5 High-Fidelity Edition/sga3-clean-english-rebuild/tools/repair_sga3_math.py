#!/usr/bin/env python3
r"""Repair SGA3 mathfixed TeX: convert Shaded/code blocks to proper LaTeX math
and fix \texttt{} math patterns.

The source was produced by pandoc from Markdown. Display-level math ended up
in \begin{Shaded}\begin{Highlighting}[]\NormalTok{...} blocks (code/verbatim),
rendering as literal text in the PDF instead of typeset math. This script:
  1. Converts single-line Shaded blocks to \[ display math \]
  2. Converts multi-line Shaded blocks (diagrams, equation arrays) to
     centered math arrays
  3. Fixes \texttt{math-content} to $math-content$ inline
  4. Cleans up text-mode escapes (\_  \{  \}) inside math contexts
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

UNICODE_TO_LATEX = {
    "⟶": r"\longrightarrow",
    "⟹": r"\Longrightarrow",
    "⟺": r"\Longleftrightarrow",
    "⟼": r"\longmapsto",
    "→": r"\to",
    "←": r"\leftarrow",
    "↑": r"\uparrow",
    "↓": r"\downarrow",
    "↕": r"\updownarrow",
    "↦": r"\mapsto",
    "↪": r"\hookrightarrow",
    "↠": r"\twoheadrightarrow",
    "↤": r"\mapsfrom",
    "⇒": r"\Rightarrow",
    "⇐": r"\Leftarrow",
    "⇔": r"\Leftrightarrow",
    "⇑": r"\Uparrow",
    "⇓": r"\Downarrow",
    "⇉": r"\rightrightarrows",
    "⇇": r"\leftleftarrows",
    "⇄": r"\rightleftarrows",
    "⇛": r"\Rrightarrow",
    "⇢": r"\dashrightarrow",
    "⇶": r"\rightthreearrows",
    "⤍": r"\rightdasharrow",
    "⤡": r"\nearrow",
    "⤴": r"\curvearrowright",
    "⤵": r"\curvearrowleft",
    "⥲": r"\twoheadrightarrowtail",
    "×": r"\times",
    "⊗": r"\otimes",
    "⊕": r"\oplus",
    "⨁": r"\bigoplus",
    "⨂": r"\bigotimes",
    "⨆": r"\bigsqcup",
    "⊠": r"\boxtimes",
    "⊔": r"\sqcup",
    "≃": r"\simeq",
    "≅": r"\cong",
    "≠": r"\neq",
    "≡": r"\equiv",
    "≥": r"\geq",
    "⩽": r"\leqslant",
    "⩾": r"\geqslant",
    "∈": r"\in",
    "∉": r"\notin",
    "∋": r"\ni",
    "⊂": r"\subset",
    "⊃": r"\supset",
    "⊆": r"\subseteq",
    "⊇": r"\supseteq",
    "∩": r"\cap",
    "∪": r"\cup",
    "⋂": r"\bigcap",
    "⋃": r"\bigcup",
    "∧": r"\wedge",
    "∨": r"\vee",
    "⋀": r"\bigwedge",
    "∀": r"\forall",
    "∃": r"\exists",
    "∂": r"\partial",
    "∅": r"\varnothing",
    "∆": r"\Delta",
    "∏": r"\prod",
    "∐": r"\coprod",
    "∑": r"\sum",
    "∗": r"*",
    "∘": r"\circ",
    "√": r"\sqrt",
    "∞": r"\infty",
    "∼": r"\sim",
    "≀": r"\wr",
    "·": r"\cdot",
    "⋅": r"\cdot",
    "⋆": r"\star",
    "⋮": r"\vdots",
    "⋯": r"\cdots",
    "…": r"\ldots",
    "⊥": r"\perp",
    "±": r"\pm",
    "−": r"-",
    "′": "'",
    "″": "''",
    "‴": "'''",
    "†": r"\dagger",
    "‡": r"\ddagger",
    "♭": r"\flat",
    "♮": r"\natural",
    "♯": r"\sharp",
    "✱": r"*",
    "⨿": r"\amalg",
    "⨶": r"\otimeshat",
    "ℂ": r"\mathbb{C}",
    "ℕ": r"\mathbb{N}",
    "ℚ": r"\mathbb{Q}",
    "ℝ": r"\mathbb{R}",
    "ℤ": r"\mathbb{Z}",
    "ℋ": r"\mathcal{H}",
    "ℐ": r"\mathcal{I}",
    "ℒ": r"\mathcal{L}",
    "ℓ": r"\ell",
    "ℛ": r"\mathcal{R}",
    "ℬ": r"\mathcal{B}",
    "ℰ": r"\mathcal{E}",
    "ℱ": r"\mathcal{F}",
    "⟨": r"\langle",
    "⟩": r"\rangle",
    "⟦": r"\llbracket",
    "⟧": r"\rrbracket",
    "°": r"^{\circ}",
    "▲": r"\blacktriangle",
    "△": r"\triangle",
    "▶": r"\blacktriangleright",
    "►": r"\blacktriangleright",
    "▼": r"\blacktriangledown",
    "◄": r"\blacktriangleleft",
    "♦": r"\diamondsuit",
    "•": r"\bullet",
}

UNICODE_SUPERSCRIPTS = {
    "⁰": "0", "¹": "1", "²": "2", "³": "3",
    "⁵": "5", "⁷": "7",
    "⁺": "+", "⁻": "-",
    "⁽": "(", "⁾": ")",
    "ⁱ": "i", "ⁿ": "n",
    "ᵈ": "d", "ᵐ": "m", "ᵖ": "p", "ᵗ": "t",
    "ʲ": "j", "ʳ": "r",
    "ⱽ": "V",
}

UNICODE_SUBSCRIPTS = {
    "₀": "0", "₁": "1", "₂": "2", "₃": "3",
    "₄": "4", "₆": "6", "₇": "7", "₈": "8",
    "₊": "+", "₋": "-", "₌": "=",
    "ₓ": "x", "ₘ": "m", "ₙ": "n", "ₛ": "s",
    "ᵢ": "i", "ᵣ": "r",
    "ⱼ": "j",
}

GREEK_MAP = {
    "Γ": r"\Gamma", "Δ": r"\Delta", "Θ": r"\Theta",
    "Λ": r"\Lambda", "Π": r"\Pi", "Σ": r"\Sigma",
    "Υ": r"\Upsilon", "Φ": r"\Phi", "Ψ": r"\Psi", "Ω": r"\Omega",
    "α": r"\alpha", "β": r"\beta", "γ": r"\gamma", "δ": r"\delta",
    "ε": r"\varepsilon", "η": r"\eta", "θ": r"\theta",
    "κ": r"\kappa", "λ": r"\lambda", "μ": r"\mu", "ν": r"\nu",
    "ξ": r"\xi", "π": r"\pi", "ρ": r"\rho", "σ": r"\sigma",
    "τ": r"\tau", "φ": r"\varphi", "χ": r"\chi", "ψ": r"\psi",
    "ω": r"\omega", "ϕ": r"\phi",
}

BOX_DRAWING = set("─│┄┌┐└┘║╱╲")
DIAGRAM_ARROWS = set("↑↓↕↖↗↘↙")
BRACKET_PARTS = set("⎛⎜⎝⎞⎟⎠⎡⎣⎤⎦⎧⎨⎩⎰⎱")


def unescape_tex(s: str) -> str:
    r"""Convert text-mode escapes to math-mode equivalents.

    \_\{...\} → _{...}  (subscript grouping)
    \^\{...\} → ^{...}  (superscript grouping)
    \_X       → _X      (single-char subscript)
    standalone \{ \} → \{ \}  (set notation, kept for math mode)
    """
    result = []
    i = 0
    # Track: when we open a _{ or ^{ group, we need to match its \} to }
    group_depth = 0  # depth of _{ / ^{ groups
    set_depth = 0    # depth of standalone \{ groups (set notation)

    while i < len(s):
        # Check for \_\{ (subscript with group)
        if s[i:i+4] == r"\_\{":
            result.append("_{")
            group_depth += 1
            i += 4
            continue
        # Check for \^\{ (superscript with group)
        if s[i:i+4] == r"\^\{":
            result.append("^{")
            group_depth += 1
            i += 4
            continue
        # Check for \_X (single-char subscript)
        if s[i:i+2] == r"\_" and i + 2 < len(s) and s[i+2] not in r"\{":
            result.append("_")
            i += 2
            continue
        # Check for \} - could close a group or a set
        if s[i:i+2] == r"\}":
            if group_depth > 0:
                result.append("}")
                group_depth -= 1
            else:
                result.append(r"\}")
            i += 2
            continue
        # Check for \{ - standalone set-notation brace
        if s[i:i+2] == r"\{":
            result.append(r"\{")
            set_depth += 1
            i += 2
            continue
        # Regular character
        result.append(s[i])
        i += 1

    return "".join(result)


def convert_superscripts(s: str) -> str:
    """Convert runs of Unicode superscript characters to ^{...}."""
    result = []
    i = 0
    while i < len(s):
        if s[i] in UNICODE_SUPERSCRIPTS:
            sup_chars = []
            while i < len(s) and s[i] in UNICODE_SUPERSCRIPTS:
                sup_chars.append(UNICODE_SUPERSCRIPTS[s[i]])
                i += 1
            body = "".join(sup_chars)
            if len(body) == 1:
                result.append(f"^{body}")
            else:
                result.append(f"^{{{body}}}")
        else:
            result.append(s[i])
            i += 1
    return "".join(result)


def convert_subscripts(s: str) -> str:
    """Convert runs of Unicode subscript characters to _{...}."""
    result = []
    i = 0
    while i < len(s):
        if s[i] in UNICODE_SUBSCRIPTS:
            sub_chars = []
            while i < len(s) and s[i] in UNICODE_SUBSCRIPTS:
                sub_chars.append(UNICODE_SUBSCRIPTS[s[i]])
                i += 1
            body = "".join(sub_chars)
            if len(body) == 1:
                result.append(f"_{body}")
            else:
                result.append(f"_{{{body}}}")
        else:
            result.append(s[i])
            i += 1
    return "".join(result)


def convert_combining_marks(s: str) -> str:
    """Convert combining diacritical marks to LaTeX hat/tilde/bar."""
    s = re.sub(r'(.)̂', r'\\hat{\1}', s)      # combining circumflex
    s = re.sub(r'(.)̃', r'\\tilde{\1}', s)     # combining tilde
    s = re.sub(r'(.)̄', r'\\bar{\1}', s)       # combining macron
    s = re.sub(r'(.)̅', r'\\overline{\1}', s)   # combining overline
    s = re.sub(r'(.)⃗', r'\\vec{\1}', s)        # combining right arrow
    return s


def unicode_to_math(s: str) -> str:
    """Convert Unicode math symbols to LaTeX commands."""
    for uc, latex in UNICODE_TO_LATEX.items():
        s = s.replace(uc, f" {latex} ")
    for uc, latex in GREEK_MAP.items():
        s = s.replace(uc, f" {latex} ")
    s = convert_superscripts(s)
    s = convert_subscripts(s)
    s = convert_combining_marks(s)
    # Handle accented Latin that are used as math (Ȟ for H-check, etc.)
    s = s.replace("Ȟ", r"\check{H}")
    s = s.replace("ḡ", r"\bar{g}")
    s = s.replace("Ḡ", r"\bar{G}")
    s = s.replace("Ỹ", r"\tilde{Y}")
    # Clean up multiple spaces
    s = re.sub(r"  +", " ", s)
    return s


def is_diagram_block(lines: list[str]) -> bool:
    """Heuristic: does this block contain box-drawing / spatial layout?"""
    if len(lines) <= 1:
        return False
    box_count = 0
    for line in lines:
        for ch in line:
            if ch in BOX_DRAWING or ch in DIAGRAM_ARROWS or ch in BRACKET_PARTS:
                box_count += 1
    return box_count >= 2


def strip_all_tok_wrappers(text: str) -> str:
    """Strip all *Tok{...} wrappers using brace counting (escaped-brace-aware)."""
    tok_re = re.compile(
        r"\\(?:Normal|Keyword|Comment|String|BuiltIn|Other|Operator|"
        r"Function|ControlFlow|DataType|Alert|Error|Extension|"
        r"Attribute|BaseN|Char|CommentVar|Constant|DecVal|"
        r"Documentation|Float|Import|Information|Preprocessor|"
        r"RegionMarker|SpecialChar|SpecialString|Variable|"
        r"VerbatimString|Warning|Annotation)Tok\{"
    )
    result = []
    i = 0
    while i < len(text):
        m = tok_re.search(text, i)
        if m is None:
            result.append(text[i:])
            break
        result.append(text[i:m.start()])
        depth = 1
        j = m.end()
        while j < len(text) and depth > 0:
            if text[j] == "\\" and j + 1 < len(text) and text[j + 1] in "{}":
                j += 2
                continue
            if text[j] == "{":
                depth += 1
            elif text[j] == "}":
                depth -= 1
            j += 1
        content = text[m.end():j - 1]
        result.append(content)
        i = j
    return "".join(result)


def extract_shaded_content(block: str) -> list[str]:
    """Extract text lines from a Shaded/Highlighting block."""
    lines = block.split("\n")
    content_lines = []
    for line in lines:
        stripped = strip_all_tok_wrappers(line)
        if re.match(r"\\begin\{(Shaded|Highlighting)", stripped):
            continue
        if re.match(r"\\end\{(Shaded|Highlighting)", stripped):
            continue
        if stripped.strip() == "":
            continue
        content_lines.append(stripped)
    return content_lines


def convert_line_to_math(line: str) -> str:
    """Convert a single content line to LaTeX math."""
    line = unescape_tex(line)
    line = unicode_to_math(line)
    # Remove excessive leading/trailing whitespace but keep internal
    line = line.strip()
    return line


def format_single_line_math(line: str) -> str:
    """Wrap a single-line formula as display math."""
    converted = convert_line_to_math(line)
    return f"\\[\n{converted}\n\\]"


def format_as_display_text(lines: list[str]) -> str:
    """Format content as centered plain text (lightweight, safe for compilation)."""
    converted = []
    for line in lines:
        cl = unescape_tex(line)
        cl = cl.strip()
        cl = cl.replace("&", r"\&")
        cl = cl.replace("#", r"\#")
        cl = cl.replace("%", r"\%")
        if cl:
            converted.append(cl)
    inner = r" \\" + "\n".join(converted)
    return (
        "\\begin{center}\n"
        + "\n".join(f"{line}" for line in converted)
        + "\n\\end{center}"
    )


def format_multiline_equations(lines: list[str]) -> str:
    """Convert multiple equation lines to centered display text."""
    return format_as_display_text(lines)


def convert_shaded_block(block: str) -> str:
    """Convert a full Shaded block to proper LaTeX math."""
    lines = extract_shaded_content(block)
    if not lines:
        return ""
    if len(lines) == 1:
        return format_single_line_math(lines[0])
    if is_diagram_block("\n".join(lines)):
        return format_as_display_text(lines)
    return format_multiline_equations(lines)


TEXTTT_MATH_RE = re.compile(
    r"\\texttt\{((?:[^{}]|\{[^{}]*\})*)\}"
)


def is_math_texttt(content: str) -> bool:
    """Heuristic: does this \\texttt{} contain math-like content?"""
    # Skip if it's clearly prose or a filename
    if content.startswith("/") or content.startswith("http"):
        return False
    if ".tex" in content or ".pdf" in content or ".md" in content:
        return False
    math_indicators = [
        r"\_", r"\{", r"\}", "→", "←", "⊗", "⊕", "×",
        "Hom", "Ker", "Im ", "Spec", "Aut", "End", "Ext",
        "Tor", "Lie", "GL", "SL", "PGL", "Mod", "Comod",
        "Fib", "Pic", "Isom",
    ]
    for indicator in math_indicators:
        if indicator in content:
            return True
    # Has subscript-like patterns
    if re.search(r"[A-Z]_", content):
        return True
    if re.search(r"[A-Z]\{", content):
        return True
    return False


def convert_texttt_to_math(match: re.Match) -> str:
    """Convert a \\texttt{...} match to $...$ if it looks like math."""
    full = match.group(0)
    content = match.group(1)
    if not is_math_texttt(content):
        return full
    # Convert to math
    math_content = unescape_tex(content)
    math_content = unicode_to_math(math_content)
    # Fix common operator names
    math_content = re.sub(r"\b(Hom|Ker|Im|Spec|Aut|End|Ext|Tor|Lie|GL|SL|PGL|"
                          r"Mod|Comod|Fib|Pic|Isom|Norm|Cent|Int|Ad|Ob|Mor|"
                          r"pr|id|tr|rk|char|deg|dim|coker|colim|lim|det|disc|"
                          r"diag|Res|Ind|Inf|Sym)\b",
                          r"\\operatorname{\1}", math_content)
    math_content = math_content.replace(r"\ ", r"\,")
    return f"${math_content}$"


SHADED_BLOCK_RE = re.compile(
    r"\\begin\{Shaded\}\s*\n"
    r"\\begin\{Highlighting\}\[\]\s*\n"
    r"(.*?)"
    r"\\end\{Highlighting\}\s*\n"
    r"\\end\{Shaded\}",
    re.DOTALL,
)


BARE_NORMALTOK_RE = re.compile(
    r"\\NormalTok\{((?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*)\}"
)

TEXTTT_OS_RE = re.compile(r"\\texttt\{OS\}")


def strip_all_normaltok(text: str) -> str:
    """Brace-counting removal of all \\NormalTok{...} wrappers.

    Skips escaped braces (\\{ and \\}) when counting depth, since pandoc
    escapes all content braces inside NormalTok arguments.
    """
    tag = r"\NormalTok{"
    result = []
    i = 0
    while i < len(text):
        pos = text.find(tag, i)
        if pos == -1:
            result.append(text[i:])
            break
        result.append(text[i:pos])
        depth = 1
        j = pos + len(tag)
        while j < len(text) and depth > 0:
            if text[j] == "\\" and j + 1 < len(text) and text[j + 1] in "{}":
                j += 2  # skip escaped brace
                continue
            if text[j] == "{":
                depth += 1
            elif text[j] == "}":
                depth -= 1
            j += 1
        content = text[pos + len(tag):j - 1]
        result.append(content)
        i = j
    return "".join(result)
TEXTTT_SIMPLE_MATH_RE = re.compile(
    r"\\texttt\{([A-Za-z]+(?:\\?\s+[A-Za-z]+)*)\}"
)

SIMPLE_MATH_NAMES = {
    "OS", "iS", "iT", "pS", "FS", "GS", "HS", "ES",
    "AS", "BS", "CS", "DS", "MS", "NS", "PS", "RS",
    "XS", "YS", "ZS", "FT", "GT", "HT",
}

CARET_BRACE_RE = re.compile(r"\\?\^{}\{([^{}]*)\}")
CARET_EMPTY_RE = re.compile(r"\\?\^{}")


def fix_caret_patterns(text: str) -> str:
    """Fix \\^{}{content} and \\^{} patterns from pandoc text-mode carets."""
    text = CARET_BRACE_RE.sub(r"^{\1}", text)
    text = CARET_EMPTY_RE.sub("^", text)
    return text


def convert_bare_normaltok(match: re.Match) -> str:
    """Convert bare \\NormalTok{...} outside Shaded blocks to math."""
    content = match.group(1)
    converted = unescape_tex(content)
    converted = unicode_to_math(converted)
    converted = converted.strip()
    return converted


def repair_tex(text: str) -> str:
    """Minimal-invasive repair: keep Shaded blocks as text but clean up rendering."""

    # Phase 1: Font substitutions
    text = text.replace(
        r"\setmainfont{FreeSerif}[Scale=MatchLowercase]",
        r"\setmainfont{DejaVu Serif}[Scale=MatchLowercase]",
    )
    text = text.replace(
        r"\setsansfont{Noto Sans}[Scale=MatchLowercase]",
        r"\setsansfont{DejaVu Sans}[Scale=MatchLowercase]",
    )
    text = text.replace(
        r"\setmonofont{FreeSerif}[Scale=MatchLowercase]",
        r"\setmonofont{DejaVu Sans Mono}[Scale=MatchLowercase]",
    )
    text = text.replace(
        r"\setmathfont{STIX Math}",
        r"\setmathfont{Cambria Math}",
    )

    # Phase 2: Redefine Highlighting to use normal font with preserved line breaks
    # instead of Verbatim monospace. This is the key visual fix.
    text = re.sub(
        r"\\DefineVerbatimEnvironment\{Highlighting\}\{Verbatim\}\{commandchars=\\\\\\\\\\\\\{\\\\\\}\}",
        r"",
        text,
    )
    # Simpler: just replace the exact definition line
    text = text.replace(
        r"\DefineVerbatimEnvironment{Highlighting}{Verbatim}{commandchars=\\\{\}}",
        r"\newenvironment{Highlighting}[1][]{\begin{trivlist}\item\relax\obeylines}{\end{trivlist}}",
    )

    # Phase 3: Neutralize syntax-highlighting color commands → just pass content through
    # Use brace-counting to handle nested definitions like {\textcolor{...}{\textbf{#1}}}
    for tok in ["Keyword", "Comment", "String", "BuiltIn", "Other", "Operator",
                "Function", "ControlFlow", "DataType", "Alert", "Error",
                "Extension", "Attribute", "BaseN", "Char", "CommentVar",
                "Constant", "DecVal", "Documentation", "Float", "Import",
                "Information", "Preprocessor", "RegionMarker", "SpecialChar",
                "SpecialString", "Variable", "VerbatimString", "Warning",
                "Annotation"]:
        tag = rf"\newcommand{{\{tok}Tok}}[1]"
        pos = text.find(tag)
        if pos == -1:
            continue
        # Find the opening brace of the body
        body_start = pos + len(tag)
        if body_start < len(text) and text[body_start] == "{":
            depth = 1
            j = body_start + 1
            while j < len(text) and depth > 0:
                if text[j] == "{":
                    depth += 1
                elif text[j] == "}":
                    depth -= 1
                j += 1
            # Replace the entire definition with pass-through
            replacement = rf"\newcommand{{\{tok}Tok}}[1]{{#1}}"
            text = text[:pos] + replacement + text[j:]

    # Phase 4: Fix double-escaped operatorname
    text = text.replace(r"\\operatorname", r"\operatorname")

    return text


def main() -> int:
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent / "SGA3_existing_english_from_jcreinhold_mathfixed.tex"
    dest = Path(sys.argv[2]) if len(sys.argv) > 2 else src.with_name("SGA3_existing_english_clean_rebuild.tex")

    if not src.exists():
        print(f"ERROR: Source not found: {src}", file=sys.stderr)
        return 1

    print(f"Reading {src} ({src.stat().st_size:,} bytes)...")
    text = src.read_text(encoding="utf-8")

    # Count before
    shaded_count = len(SHADED_BLOCK_RE.findall(text))
    texttt_count = len(TEXTTT_MATH_RE.findall(text))
    print(f"Found {shaded_count} Shaded blocks, {texttt_count} \\texttt{{}} instances")

    text = repair_tex(text)

    # Count remaining
    remaining_shaded = len(SHADED_BLOCK_RE.findall(text))
    remaining_normaltok = text.count(r"\NormalTok{")
    remaining_texttt_os = len(TEXTTT_OS_RE.findall(text))
    print(f"Remaining: {remaining_shaded} Shaded, {remaining_normaltok} NormalTok, {remaining_texttt_os} texttt{{OS}}")

    dest.write_text(text, encoding="utf-8")
    print(f"Written {dest} ({dest.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

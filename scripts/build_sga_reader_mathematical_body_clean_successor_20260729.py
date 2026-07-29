#!/usr/bin/env python3
"""Build the second reader-only SGA cleanup successor."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
TEMP_ROOT = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga_reader_mathematical_body_clean_build_v2_20260729"
)
PACKAGE_ROOT = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga1-6-reader-mathematical-body-clean-successor-v2-20260729"
)

PRESENTATION_ROOT = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga1-6-reader-clean-presentation-successor-20260728"
)
SGA3_PRESENTATION_ROOT = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga3-english-complete-working-reader-clean-r18-native-expose-i-20260729"
)

SGA2_SOURCE = (
    REPO_ROOT / "sources" / "sga" / "sga2-english-reference-linked-r8-20260723"
)
SGA3_ARCHIVE = (
    SGA3_PRESENTATION_ROOT
    / "10c9_SGA3_English_Complete_Reader_Source_and_History_R18_20260729.zip"
)
SGA6_SOURCE = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga6-english-cumulative-through-idx702-reference-linked-20260723"
    / "working"
)

PDF_OUTPUTS = {
    "sga2": "00b_SGA2_English_Complete_ReferenceLinked_R8_20260723.pdf",
    "sga3": "00c00_SGA3_English_Complete_Reader_Native_Update_R18_20260729.pdf",
    "sga6": "00f_SGA6_English_Complete_ReferenceLinked_20260723.pdf",
}
TEX_OUTPUTS = {
    "sga2": "02b_SGA2_English_Complete_ReferenceLinked_R8_Master_20260723.tex",
    "sga3": "02c00_SGA3_English_Complete_Reader_Native_Update_R18_20260729.tex",
    "sga6": "02f_SGA6_English_Complete_ReferenceLinked_Master_20260723.tex",
}
MASTER_NAMES = {
    "sga2": "SGA2_English_Full_Reader.tex",
    "sga3": "SGA3_English_Complete_Reader_Native_Update_R18_20260729.tex",
    "sga6": "SGA6_English_Complete_ReferenceLinked_Master_20260723.tex",
}
MASTER_OVERLAYS = {
    "sga2": PRESENTATION_ROOT / TEX_OUTPUTS["sga2"],
    "sga3": SGA3_PRESENTATION_ROOT / TEX_OUTPUTS["sga3"],
    "sga6": PRESENTATION_ROOT / TEX_OUTPUTS["sga6"],
}

APPARATUS_LEDGER = "READER_APPARATUS_REMOVAL_LEDGER.csv"
BUILD_SUMMARY = "BUILD_AND_TEXT_VALIDATION.json"
README_NAME = "README.md"
SHA_MANIFEST = "SHA256SUMS.csv"


@dataclass
class Removal:
    volume: str
    relative_path: str
    kind: str
    start_line: int
    bytes_removed: int
    sha256: str
    preview: str


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def normalize_preview(text: str, limit: int = 180) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return text[:limit].rstrip()


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def find_balanced(
    text: str, start: int, opening: str = "{", closing: str = "}"
) -> int:
    if start >= len(text) or text[start] != opening:
        raise ValueError(f"Expected {opening!r} at offset {start}")
    depth = 0
    escaped = False
    for index in range(start, len(text)):
        char = text[index]
        if escaped:
            escaped = False
            continue
        if char == "\\":
            escaped = True
            continue
        if char == opening:
            depth += 1
        elif char == closing:
            depth -= 1
            if depth == 0:
                return index + 1
    raise ValueError(f"Unclosed {opening!r} group at offset {start}")


def skip_space(text: str, index: int) -> int:
    while index < len(text) and text[index].isspace():
        index += 1
    return index


def parse_command_arguments(
    text: str, command_end: int, argument_count: int
) -> tuple[int, list[str]]:
    index = skip_space(text, command_end)
    if index < len(text) and text[index] == "[":
        index = find_balanced(text, index, "[", "]")
        index = skip_space(text, index)
    args: list[str] = []
    for _ in range(argument_count):
        if index >= len(text) or text[index] != "{":
            raise ValueError(f"Missing command argument at offset {index}")
        end = find_balanced(text, index)
        args.append(text[index + 1 : end - 1])
        index = skip_space(text, end)
    return index, args


def is_project_note(volume: str, body: str) -> bool:
    plain = re.sub(r"\\[A-Za-z@]+\*?", " ", body)
    plain = re.sub(r"[{}~]", " ", plain)
    plain = re.sub(r"\s+", " ", plain).strip().lower()
    if volume == "sga1":
        phrases = (
            "editorial note",
            "source note",
            "source correction",
            "source defect",
            "source oddity",
            "the original printing",
            "original printing has",
            "original printing give",
            "original printing omit",
            "french tex and the original",
            "french source prints",
            "french source has",
            "corrected french",
            "french authority",
            "attested reading",
        )
        return any(phrase in plain for phrase in phrases)
    if volume == "sga2":
        phrases = (
            "source note",
            "source correction",
            "source-normalization note",
            "source-numbering",
            "source-structure note",
            "source defect",
            "source-defect",
            "source oddity",
            "manager decision",
            "manager's final adjudication",
            "manager s final adjudication",
            "french authority is left unchanged",
            "french authority remains unchanged",
            "corrected french tex and same-edition",
            "french printed and tex sources",
            "printed french and the corrected tex",
            "french tex and printed",
            "corrected french source adds",
            "sga2-x-l",
            "sga2-ix-l",
            "sga2-xi-l",
            "tranche comparison ledger",
        )
        return any(phrase in plain for phrase in phrases)
    if volume == "sga3":
        explicitly_editor_authored = any(
            marker in plain[:160]
            for marker in (
                "editor's note",
                "editors' note",
                "editor’s note",
                "editors’ note",
            )
        )
        project_editor_exceptions = any(
            marker in plain
            for marker in (
                "english editor's note",
                "english editor’s note",
                "source pdf prints",
                "source marks this final reference",
                "french edition prints",
                "polo--gille re-edition prints",
                "polo–gille re-edition prints",
                "type-correct reading",
            )
        )
        if explicitly_editor_authored and not project_editor_exceptions:
            return False
        phrases = (
            "translator's note",
            "translator s note",
            "source note:",
            "source note.",
            "source notation note",
            "source-reading note",
            "source correction",
            "source defect",
            "source oddity",
            "source pdf",
            "source appends",
            "source display prints",
            "source marks this final reference",
            "source reverses this composition",
            "source cites the final assertion",
            "source also prints",
            "printed source",
            "printed diagram directs",
            "printed french text has",
            "printed formula writes",
            "final sentence of the printed french",
            "source prints",
            "source reads",
            "source says",
            "source notes",
            "source omits",
            "source has",
            "french source refers",
            "french source introduces",
            "french authority prints",
            "french edition prints",
            "french re-edition prints",
            "french re-edition says",
            "french re-edition labels",
            "the re-edition replaces",
            "french pdf prints",
            "french pdf labels",
            "polo--gille pdf prints",
            "polo–gille pdf prints",
            "polo--gille re-edition prints",
            "polo–gille re-edition prints",
            "there is no item numbered",
        )
        if any(phrase in plain for phrase in phrases):
            return True
        starts = (
            "the french source prints",
            "the french source reads",
            "the french source says",
            "the french source omits",
            "the french source has",
            "at this point both the french",
        )
        return plain.startswith(starts)
    if volume == "sga6":
        phrases = (
            "source note",
            "source correction",
            "source defect",
            "source-defect",
            "source oddity",
            "sga6-xiv-idx702-xref96-vs-xref46-srcdef-001",
        )
        return any(phrase in plain for phrase in phrases)
    return False


def record_removal(
    removals: list[Removal],
    volume: str,
    relative_path: str,
    kind: str,
    source_text: str,
    start: int,
    end: int,
) -> None:
    removed = source_text[start:end]
    removals.append(
        Removal(
            volume=volume,
            relative_path=relative_path,
            kind=kind,
            start_line=line_number(source_text, start),
            bytes_removed=len(removed.encode("utf-8")),
            sha256=sha256_bytes(removed.encode("utf-8")),
            preview=normalize_preview(removed),
        )
    )


def remove_begingroup_note_blocks(
    text: str,
    volume: str,
    relative_path: str,
    removals: list[Removal],
) -> str:
    cursor = 0
    pieces: list[str] = []
    pattern = re.compile(r"\\begingroup\b")
    while True:
        match = pattern.search(text, cursor)
        if match is None:
            pieces.append(text[cursor:])
            break
        group_token = re.compile(r"\\(?:begingroup|endgroup)\b")
        depth = 1
        end = -1
        for token in group_token.finditer(text, match.end()):
            if token.group(0) == r"\begingroup":
                depth += 1
            else:
                depth -= 1
                if depth == 0:
                    end = token.end()
                    break
        if end < 0:
            pieces.append(text[cursor:])
            break
        block = text[match.start() : end]
        if r"\footnote" in block and is_project_note(volume, block):
            pieces.append(text[cursor : match.start()])
            record_removal(
                removals,
                volume,
                relative_path,
                "project_note_group",
                text,
                match.start(),
                end,
            )
            cursor = end
        else:
            pieces.append(text[cursor:end])
            cursor = end
    return "".join(pieces)


def remove_commands(
    text: str,
    volume: str,
    relative_path: str,
    removals: list[Removal],
) -> str:
    commands = {
        "footnote": (1, 0, "project_footnote"),
        "footnotetext": (1, 0, "project_footnotetext"),
        "markedfootnote": (2, 1, "project_marked_footnote"),
        "sourceoddity": (2, 1, "source_oddity_box"),
    }
    command_re = re.compile(
        r"\\(?P<name>footnote|footnotetext|markedfootnote|sourceoddity)\b"
    )
    candidates: list[tuple[int, int, str]] = []
    for match in command_re.finditer(text):
        name = match.group("name")
        arg_count, body_index, kind = commands[name]
        try:
            end, args = parse_command_arguments(text, match.end(), arg_count)
        except ValueError:
            continue
        remove = name == "sourceoddity" or is_project_note(
            volume, args[body_index]
        )
        if remove:
            candidates.append((match.start(), end, kind))

    # Regex iteration sees nested footnotes independently. Keep the outermost
    # removal when both levels are project apparatus, but retain a nested
    # project note when its enclosing historical editor note is preserved.
    spans: list[tuple[int, int, str]] = []
    for start, end, kind in sorted(
        candidates, key=lambda row: (row[0], -row[1])
    ):
        if any(start >= kept_start and end <= kept_end for kept_start, kept_end, _ in spans):
            continue
        spans.append((start, end, kind))

    for start, end, kind in spans:
        record_removal(
            removals,
            volume,
            relative_path,
            kind,
            text,
            start,
            end,
        )
    for start, end, _ in sorted(spans, reverse=True):
        text = text[:start] + text[end:]
    return text


def remove_setup_commands(body: str) -> str:
    command_re = re.compile(
        r"\\(?P<name>renewcommand|addtocounter|setcounter)\b"
    )
    cursor = 0
    pieces: list[str] = []
    while True:
        match = command_re.search(body, cursor)
        if match is None:
            pieces.append(body[cursor:])
            break
        pieces.append(body[cursor : match.start()])
        try:
            end, _ = parse_command_arguments(body, match.end(), 2)
        except ValueError:
            pieces.append(body[match.start() : match.end()])
            cursor = match.end()
            continue
        cursor = end
    result = "".join(pieces)
    result = re.sub(r"(?m)%.*$", "", result)
    result = re.sub(r"\\par\b", "", result)
    return result


def remove_empty_footnote_groups(
    text: str,
    volume: str,
    relative_path: str,
    removals: list[Removal],
) -> str:
    pattern = re.compile(
        r"\\begingroup"
        r"(?:(?!\\begingroup\b|\\endgroup\b)[\s\S])*?"
        r"\\endgroup"
    )
    while True:
        matches = list(pattern.finditer(text))
        eligible = []
        for match in matches:
            body = match.group(0)[len(r"\begingroup") : -len(r"\endgroup")]
            if not remove_setup_commands(body).strip():
                eligible.append(match)
        if not eligible:
            return text
        for match in reversed(eligible):
            record_removal(
                removals,
                volume,
                relative_path,
                "empty_project_note_wrapper",
                text,
                match.start(),
                match.end(),
            )
            text = text[: match.start()] + text[match.end() :]


def remove_source_margins(
    text: str,
    volume: str,
    relative_path: str,
    removals: list[Removal],
) -> str:
    cursor = 0
    pieces: list[str] = []
    pattern = re.compile(r"\\marginpar\b")
    while True:
        match = pattern.search(text, cursor)
        if match is None:
            pieces.append(text[cursor:])
            break
        pieces.append(text[cursor : match.start()])
        try:
            end, args = parse_command_arguments(text, match.end(), 1)
        except ValueError:
            pieces.append(text[match.start() : match.end()])
            cursor = match.end()
            continue
        plain = args[0].lower()
        if (
            "french source" in plain
            or "source-pdf" in plain
            or "source pdf" in plain
        ):
            record_removal(
                removals,
                volume,
                relative_path,
                "source_page_margin",
                text,
                match.start(),
                end,
            )
        else:
            pieces.append(text[match.start() : end])
        cursor = end
    return "".join(pieces)


def remove_standalone_project_paragraphs(
    text: str,
    volume: str,
    relative_path: str,
    removals: list[Removal],
) -> str:
    starts = {
        "sga1": re.compile(
            r"(?m)^[ \t]*\\paragraph\{Editorial note(?: on the proof)?\.\}"
        ),
        "sga2": re.compile(
            r"(?m)^[ \t]*(?:"
            r"\\noindent\\textit\{(?:Editorial note|Source note|Source correction)\.\}"
            r"|\\noindent\\emph\{(?:Editorial note|Source note|Source correction)\.\}"
            r"|\\paragraph\{(?:Editorial note|Source note|Source correction)\.\}"
            r")"
        ),
        "sga3": re.compile(
            r"(?m)^[ \t]*(?:\\noindent\s*)?"
            r"(?:\{\\footnotesize\s*)?"
            r"(?:\\emph|\\textit)\{Source (?:notation )?note\.\}"
            r"(?:\\enspace)?"
        ),
    }
    pattern = starts.get(volume)
    if pattern is None:
        return text
    cursor = 0
    pieces: list[str] = []
    while True:
        match = pattern.search(text, cursor)
        if match is None:
            pieces.append(text[cursor:])
            break
        paragraph_end = re.search(r"\n[ \t]*\n", text[match.end() :])
        if paragraph_end is None:
            end = len(text)
        else:
            end = match.end() + paragraph_end.end()
        structural_close = re.search(
            r"(?m)^[ \t]*\\end\{[^}\n]+\}",
            text[match.end() : end],
        )
        if structural_close is not None:
            end = match.end() + structural_close.start()
        substantive_transition = re.search(
            r"(?m)^[ \t]*Thus there is a nonsplit exact sequence\b",
            text[match.end() : end],
        )
        if substantive_transition is not None:
            end = min(
                end,
                match.end() + substantive_transition.start(),
            )
        block = text[match.start() : end]
        if is_project_note(volume, block):
            pieces.append(text[cursor : match.start()])
            record_removal(
                removals,
                volume,
                relative_path,
                "standalone_project_note",
                text,
                match.start(),
                end,
            )
        else:
            pieces.append(text[cursor:end])
        cursor = end
    return "".join(pieces)


def remove_project_note_environments(
    text: str,
    volume: str,
    relative_path: str,
    removals: list[Removal],
) -> str:
    if volume != "sga3":
        return text
    pattern = re.compile(
        r"\\begin\{(?P<name>quote|quotation)\}"
        r"(?P<body>[\s\S]*?)"
        r"\\end\{(?P=name)\}"
    )
    cursor = 0
    pieces: list[str] = []
    for match in pattern.finditer(text):
        block = match.group(0)
        body = match.group("body")
        if "source note" not in body.lower() or not is_project_note(
            volume, body
        ):
            continue
        pieces.append(text[cursor : match.start()])
        record_removal(
            removals,
            volume,
            relative_path,
            "project_source_note_environment",
            text,
            match.start(),
            match.end(),
        )
        cursor = match.end()
    if cursor == 0:
        return text
    pieces.append(text[cursor:])
    return "".join(pieces)


def remove_inline_project_asides(
    text: str,
    volume: str,
    relative_path: str,
    removals: list[Removal],
) -> str:
    if volume != "sga3":
        return text
    command_re = re.compile(r"\\(?P<name>emph|textit)\b")
    cursor = 0
    pieces: list[str] = []
    while True:
        match = command_re.search(text, cursor)
        if match is None:
            pieces.append(text[cursor:])
            break
        pieces.append(text[cursor : match.start()])
        try:
            end, args = parse_command_arguments(text, match.end(), 1)
        except ValueError:
            pieces.append(text[match.start() : match.end()])
            cursor = match.end()
            continue
        body = args[0].strip()
        remove = (
            body.startswith("[")
            and body.endswith("]")
            and is_project_note(volume, body)
        )
        if remove:
            record_removal(
                removals,
                volume,
                relative_path,
                "inline_project_source_aside",
                text,
                match.start(),
                end,
            )
        else:
            pieces.append(text[match.start() : end])
        cursor = end
    return "".join(pieces)


def remove_project_source_note_anchors(text: str) -> str:
    text = re.sub(
        r"(?m)^[ \t]*\\phantomsection\s*\n"
        r"[ \t]*\\label\{[^}\n]*(?:source[-:]?note|source-reading)[^}\n]*\}"
        r"[ \t]*\n?",
        "",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r"(?m)^[ \t]*\\phantomsection\\label"
        r"\{[^}\n]*(?:source[-:]?note|source-reading)[^}\n]*\}"
        r"[ \t]*%?[ \t]*\n?",
        "",
        text,
        flags=re.IGNORECASE,
    )
    return text


def remove_sga2_project_boxes(
    text: str, relative_path: str, removals: list[Removal]
) -> str:
    cursor = 0
    pieces: list[str] = []
    pattern = re.compile(r"\\noindent(?:\s*\{|\s*\\colorbox\b)")
    while True:
        match = pattern.search(text, cursor)
        if match is None:
            pieces.append(text[cursor:])
            break
        command = text[match.start() : match.end()]
        if r"\colorbox" in command:
            colorbox = text.find(r"\colorbox", match.start(), match.end())
            try:
                end, _ = parse_command_arguments(
                    text, colorbox + len(r"\colorbox"), 2
                )
            except ValueError:
                pieces.append(text[cursor : match.end()])
                cursor = match.end()
                continue
        else:
            brace = text.find("{", match.start(), match.end())
            try:
                end = find_balanced(text, brace)
            except ValueError:
                pieces.append(text[cursor:])
                break
        block = text[match.start() : end]
        if is_project_note("sga2", block):
            pieces.append(text[cursor : match.start()])
            record_removal(
                removals,
                "sga2",
                relative_path,
                "project_source_box",
                text,
                match.start(),
                end,
            )
            cursor = end
        else:
            pieces.append(text[cursor:end])
            cursor = end
    return "".join(pieces)


def clean_tex(
    path: Path,
    root: Path,
    volume: str,
    removals: list[Removal],
) -> None:
    raw = path.read_text(encoding="utf-8-sig")
    relative_path = path.relative_to(root).as_posix()
    if (
        volume == "sga6"
        and relative_path.casefold()
        == (
            "fragments/"
            "sga6_xiv_idx685_702_editorial_source_notes.tex"
        ).casefold()
    ):
        record_removal(
            removals,
            volume,
            relative_path,
            "project_source_notes_file",
            raw,
            0,
            len(raw),
        )
        path.write_text(
            "% Project source notes omitted from the reader-facing build.\n",
            encoding="utf-8",
            newline="\n",
        )
        return
    text = raw
    text = remove_commands(text, volume, relative_path, removals)
    text = remove_empty_footnote_groups(
        text, volume, relative_path, removals
    )
    if volume in {"sga1", "sga2"}:
        text = remove_source_margins(
            text, volume, relative_path, removals
        )
    text = remove_project_note_environments(
        text, volume, relative_path, removals
    )
    text = remove_inline_project_asides(
        text, volume, relative_path, removals
    )
    text = remove_standalone_project_paragraphs(
        text, volume, relative_path, removals
    )
    if volume == "sga3":
        text = remove_project_source_note_anchors(text)
    if volume == "sga2":
        text = remove_sga2_project_boxes(
            text, relative_path, removals
        )
    if text != raw:
        path.write_text(text, encoding="utf-8", newline="\n")


def prepare_sources() -> dict[str, Path]:
    if TEMP_ROOT.exists():
        resolved = TEMP_ROOT.resolve()
        temp_parent = (
            Path(os.environ["LOCALAPPDATA"]) / "Temp"
        ).resolve()
        if temp_parent not in resolved.parents:
            raise RuntimeError(f"Refusing to remove non-temp path: {resolved}")
        shutil.rmtree(TEMP_ROOT)
    TEMP_ROOT.mkdir(parents=True)

    roots = {key: TEMP_ROOT / key for key in ("sga2", "sga3", "sga6")}
    shutil.copytree(SGA2_SOURCE, roots["sga2"])
    with zipfile.ZipFile(SGA3_ARCHIVE) as archive:
        archive.extractall(roots["sga3"])
    shutil.copytree(SGA6_SOURCE, roots["sga6"])

    for volume, overlay in MASTER_OVERLAYS.items():
        if not overlay.is_file():
            raise FileNotFoundError(overlay)
        shutil.copy2(overlay, roots[volume] / MASTER_NAMES[volume])
    return roots


def run_build(volume: str, root: Path, master: Path) -> dict[str, object]:
    engine_flag = "-xelatex" if volume == "sga3" else "-pdf"
    command = [
        "latexmk",
        engine_flag,
        "-interaction=nonstopmode",
        "-halt-on-error",
        "-file-line-error",
        master.name,
    ]
    result = subprocess.run(
        command,
        cwd=root,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    build_log = PACKAGE_ROOT / f"{volume.upper()}_BUILD_PUBLIC.log"
    public_log = result.stdout
    replacements = {
        str(Path.home()): "<LOCAL_HOME>",
        str(Path.home()).replace("\\", "/"): "<LOCAL_HOME>",
        str(REPO_ROOT): "<WORKTREE>",
        str(REPO_ROOT).replace("\\", "/"): "<WORKTREE>",
        str(TEMP_ROOT): "<TEMP_BUILD_ROOT>",
        str(TEMP_ROOT).replace("\\", "/"): "<TEMP_BUILD_ROOT>",
    }
    for private_path, replacement in sorted(
        replacements.items(), key=lambda item: len(item[0]), reverse=True
    ):
        public_log = public_log.replace(private_path, replacement)
    build_log.write_text(public_log, encoding="utf-8", newline="\n")
    if result.returncode:
        raise RuntimeError(
            f"{volume} build failed with exit {result.returncode}; "
            f"see {build_log}"
        )
    pdf = root / f"{master.stem}.pdf"
    if not pdf.is_file():
        raise FileNotFoundError(pdf)
    log_text = (root / f"{master.stem}.log").read_text(
        encoding="utf-8", errors="replace"
    )
    hard_patterns = {
        "undefined_references": r"LaTeX Warning: Reference .* undefined",
        "undefined_citations": r"LaTeX Warning: Citation .* undefined",
        "missing_file": r"LaTeX Error: File .* not found",
        "fatal_error": r"Fatal error occurred",
    }
    hard_counts = {
        name: len(re.findall(pattern, log_text))
        for name, pattern in hard_patterns.items()
    }
    if any(hard_counts.values()):
        raise RuntimeError(f"{volume} build log has hard errors: {hard_counts}")
    return {
        "command": command,
        "returncode": result.returncode,
        "pdf": pdf,
        "pages": pdf_page_count(pdf),
        "bytes": pdf.stat().st_size,
        "sha256": sha256_file(pdf),
        "hard_diagnostic_counts": hard_counts,
    }


def pdf_page_count(path: Path) -> int:
    result = subprocess.run(
        ["pdfinfo", str(path)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=True,
    )
    match = re.search(r"^Pages:\s+(\d+)\s*$", result.stdout, re.MULTILINE)
    if match is None:
        raise RuntimeError(f"Unable to read PDF page count: {path}")
    return int(match.group(1))


TEXT_BLOCKLIST = {
    "sga2": (
        "Source note.",
        "Source correction.",
        "Source-structure note",
        "source-normalization note",
        "The corrected French source adds",
        "The corrected French TeX and same-edition PDF",
        "French printed and TeX sources",
        "The printed French and the corrected TeX",
        "The French TeX and printed",
        "French source PDF p.",
        "manager decision",
        "manager's final adjudication",
        "French authority is left unchanged",
        "SGA2-X-L",
        "SGA2-IX-L",
        "SGA2-XI-L",
        "tranche comparison ledger",
    ),
    "sga3": (
        "Translator's note",
        "Translator’s note",
        "Source note:",
        "Source note.",
        "Source notation note.",
        "Source-reading note",
        "The source appends",
        "The source display prints",
        "the source marks this final reference",
        "The printed diagram directs",
        "The source reverses this composition",
        "The source cites the final assertion",
        "The French authority prints",
        "The printed French text has",
        "The printed formula writes",
        "The French edition prints",
        "The final sentence of the printed French",
        "The re-edition replaces",
        "There is no item numbered 4.7",
        "The source PDF",
        "The source prints",
        "The source reads",
        "The source says",
        "The source notes",
        "The source omits",
        "The source has",
        "The French source refers",
        "The French source introduces",
        "The printed source",
        "The French re-edition prints",
        "The French re-edition says",
        "The French re-edition labels",
        "The French PDF prints",
        "The French PDF labels",
        "The Polo–Gille PDF prints",
        "source defect disclosed",
        "source-status",
    ),
    "sga6": (
        "Source note",
        "SGA6-XIV-IDX702-XREF96-VS-XREF46-SRCDEF-001",
        "The printed French note reads",
    ),
}
GLOBAL_BLOCKLIST = (
    "ChatGPT",
    "OpenAI",
    "Claude",
    "Codex",
    "large language model",
    "LLM-generated",
    "AI-generated",
    "AI-assisted",
)


def extract_pdf_text(path: Path) -> str:
    result = subprocess.run(
        ["pdftotext", "-layout", str(path), "-"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    return result.stdout.decode("utf-8", errors="replace")


def write_removal_ledger(removals: list[Removal]) -> None:
    path = PACKAGE_ROOT / APPARATUS_LEDGER
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(
            stream,
            fieldnames=[
                "volume",
                "relative_path",
                "kind",
                "start_line",
                "bytes_removed",
                "sha256",
                "preview",
            ],
            lineterminator="\n",
        )
        writer.writeheader()
        for removal in removals:
            writer.writerow(removal.__dict__)


def write_readme(results: dict[str, dict[str, object]]) -> None:
    lines = [
        "# SGA reader mathematical-body presentation successor",
        "",
        "These direct English readers remove project-facing translation,",
        "source-adjudication, workflow, and machine-production apparatus from",
        "the reading surface. The mathematical body, historical source-edition",
        "prefaces and editor notes, internal links, and source ordering remain.",
        "",
        "The full annotated source and evidence archives remain preserved in",
        "the same Zenodo concept and its immutable predecessor versions. This",
        "reader-only successor does not erase or rewrite that evidence.",
        "",
        "Affected direct readers:",
    ]
    for volume in ("sga2", "sga3", "sga6"):
        result = results[volume]
        lines.append(
            f"- {volume.upper()}: {result['pages']} pages, "
            f"SHA-256 `{result['sha256']}`."
        )
    lines.extend(
        [
            "",
            "SGA 1, SGA 4, and SGA 5 required no second-pass replacement and",
            "remain byte-identical on the successor Zenodo surface.",
            "",
            "These remain scholarly working translations, not critical editions,",
            "rights clearances, peer review, mathematical certification, final",
            "diagram-fidelity certification, or tagged-PDF accessibility work.",
            "",
        ]
    )
    (PACKAGE_ROOT / README_NAME).write_text(
        "\n".join(lines), encoding="utf-8", newline="\n"
    )


def write_manifest() -> None:
    files = sorted(
        (
            path
            for path in PACKAGE_ROOT.iterdir()
            if path.is_file() and path.name != SHA_MANIFEST
        ),
        key=lambda path: path.name.casefold(),
    )
    with (PACKAGE_ROOT / SHA_MANIFEST).open(
        "w", encoding="utf-8", newline=""
    ) as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(["filename", "bytes", "sha256"])
        for path in files:
            writer.writerow(
                [path.name, path.stat().st_size, sha256_file(path)]
            )


def reused_result(volume: str) -> dict[str, object]:
    output_pdf = PACKAGE_ROOT / PDF_OUTPUTS[volume]
    build_log = PACKAGE_ROOT / f"{volume.upper()}_BUILD_PUBLIC.log"
    if not output_pdf.is_file() or not build_log.is_file():
        raise FileNotFoundError(
            f"Cannot reuse incomplete {volume} package output"
        )
    return {
        "command": ["reused_previous_clean_build"],
        "returncode": 0,
        "pdf": output_pdf,
        "pages": pdf_page_count(output_pdf),
        "bytes": output_pdf.stat().st_size,
        "sha256": sha256_file(output_pdf),
        "hard_diagnostic_counts": {
            "undefined_references": 0,
            "undefined_citations": 0,
            "missing_file": 0,
            "fatal_error": 0,
        },
    }


def build(rebuild_volumes: set[str] | None = None) -> None:
    volumes = ("sga2", "sga3", "sga6")
    selected = set(volumes) if rebuild_volumes is None else rebuild_volumes
    if not selected or not selected.issubset(volumes):
        raise ValueError(f"Invalid rebuild volume set: {sorted(selected)}")
    if rebuild_volumes is None and PACKAGE_ROOT.exists():
        resolved = PACKAGE_ROOT.resolve()
        package_parent = PACKAGE_ROOT.parent.resolve()
        if resolved.parent != package_parent:
            raise RuntimeError(
                f"Refusing to clear unexpected package path: {resolved}"
            )
        shutil.rmtree(PACKAGE_ROOT)
    PACKAGE_ROOT.mkdir(parents=True, exist_ok=True)
    roots = prepare_sources()
    removals: list[Removal] = []
    for volume, root in roots.items():
        extensions = {".tex", ".texfrag"}
        for path in sorted(root.rglob("*")):
            if path.is_file() and path.suffix.lower() in extensions:
                clean_tex(path, root, volume, removals)

    results: dict[str, dict[str, object]] = {}
    for volume in volumes:
        root = roots[volume]
        master = root / MASTER_NAMES[volume]
        output_pdf = PACKAGE_ROOT / PDF_OUTPUTS[volume]
        output_tex = PACKAGE_ROOT / TEX_OUTPUTS[volume]
        if volume in selected:
            result = run_build(volume, root, master)
            shutil.copy2(result["pdf"], output_pdf)
        else:
            result = reused_result(volume)
        shutil.copy2(master, output_tex)
        result["output_pdf"] = output_pdf.name
        result["output_tex"] = output_tex.name
        results[volume] = result

    text_validation: dict[str, object] = {}
    for volume, result in results.items():
        output_pdf = PACKAGE_ROOT / str(result["output_pdf"])
        text = extract_pdf_text(output_pdf)
        hits = [
            token
            for token in (*GLOBAL_BLOCKLIST, *TEXT_BLOCKLIST[volume])
            if token.casefold() in text.casefold()
        ]
        text_validation[volume] = {
            "characters": len(text),
            "blocked_hits": hits,
        }
        if hits:
            raise RuntimeError(
                f"{volume} reader-visible apparatus remained: {hits}"
            )

    write_removal_ledger(removals)
    write_readme(results)
    summary = {
        "status": "PASS_READER_MATHEMATICAL_BODY_CLEAN_V2",
        "volumes_rebuilt_this_run": [
            volume.upper() for volume in volumes if volume in selected
        ],
        "volumes_reused_this_run": [
            volume.upper() for volume in volumes if volume not in selected
        ],
        "affected_volumes": ["SGA2", "SGA3", "SGA6"],
        "volumes_retained": ["SGA1", "SGA4", "SGA5"],
        "removals": len(removals),
        "removals_by_volume": {
            volume: sum(1 for row in removals if row.volume == volume)
            for volume in ("sga2", "sga3", "sga6")
        },
        "results": {
            volume: {
                key: value
                for key, value in result.items()
                if key not in {"pdf"}
            }
            for volume, result in results.items()
        },
        "text_validation": text_validation,
        "errors": [],
    }
    (PACKAGE_ROOT / BUILD_SUMMARY).write_text(
        json.dumps(summary, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    write_manifest()
    print(json.dumps(summary, indent=2))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--keep-temp",
        action="store_true",
        help="Keep temporary build sources after a successful build.",
    )
    parser.add_argument(
        "--only",
        action="append",
        choices=("sga2", "sga3", "sga6"),
        help=(
            "Rebuild only the named volume and reuse the other already "
            "passing package outputs. May be repeated."
        ),
    )
    args = parser.parse_args()
    try:
        build(set(args.only) if args.only else None)
    except Exception as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    if not args.keep_temp:
        shutil.rmtree(TEMP_ROOT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

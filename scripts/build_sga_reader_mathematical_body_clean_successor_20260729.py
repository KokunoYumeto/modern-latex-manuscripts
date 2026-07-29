#!/usr/bin/env python3
"""Build reader-only SGA successors without project-facing apparatus."""

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
    / "sga_reader_mathematical_body_clean_build_20260729"
)
PACKAGE_ROOT = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga1-6-reader-mathematical-body-clean-successor-20260729"
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

SGA1_ARCHIVE = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga1-english-complete-volume-working-20260722"
    / "SGA1_English_CompleteVolume_Working_Source_20260722.zip"
)
SGA2_SOURCE = (
    REPO_ROOT / "sources" / "sga" / "sga2-english-reference-linked-r8-20260723"
)
SGA3_ARCHIVE = (
    SGA3_PRESENTATION_ROOT
    / "10c9_SGA3_English_Complete_Reader_Source_and_History_R18_20260729.zip"
)
SGA5_SOURCE = (
    REPO_ROOT / "sources" / "sga" / "sga5-english-reference-linked-r9-20260723"
)

PDF_OUTPUTS = {
    "sga1": "00a_SGA1_English_CompleteVolume_Working_NoExhaustiveCertification_20260722.pdf",
    "sga2": "00b_SGA2_English_Complete_ReferenceLinked_R8_20260723.pdf",
    "sga3": "00c00_SGA3_English_Complete_Reader_Native_Update_R18_20260729.pdf",
    "sga5": "00e_SGA5_English_ReferenceLinked_R9_20260723.pdf",
}
TEX_OUTPUTS = {
    "sga1": "02a_SGA1_English_CompleteVolume_Working_Master_20260722.tex",
    "sga2": "02b_SGA2_English_Complete_ReferenceLinked_R8_Master_20260723.tex",
    "sga3": "02c00_SGA3_English_Complete_Reader_Native_Update_R18_20260729.tex",
    "sga5": "02e_SGA5_English_ReferenceLinked_R9_Master_20260723.tex",
}
MASTER_NAMES = {
    "sga1": "SGA1_English_source_sync_workpass.tex",
    "sga2": "SGA2_English_Full_Reader.tex",
    "sga3": "SGA3_English_Complete_Reader_Native_Update_R18_20260729.tex",
    "sga5": "SGA5_English_sync_workpass.tex",
}
MASTER_OVERLAYS = {
    "sga1": PRESENTATION_ROOT / TEX_OUTPUTS["sga1"],
    "sga2": PRESENTATION_ROOT / TEX_OUTPUTS["sga2"],
    "sga3": SGA3_PRESENTATION_ROOT / TEX_OUTPUTS["sga3"],
    "sga5": PRESENTATION_ROOT / TEX_OUTPUTS["sga5"],
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
    return text[:limit]


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
            "source defect",
            "source-defect",
            "source oddity",
            "manager decision",
            "french authority remains unchanged",
            "corrected french source adds",
            "sga2-x-l",
            "sga2-xi-l",
        )
        return any(phrase in plain for phrase in phrases)
    if volume == "sga3":
        if "editor's note in the french source" in plain:
            return False
        if "editors' note in the french source" in plain:
            return False
        phrases = (
            "translator's note",
            "translator s note",
            "source note:",
            "source note.",
            "source-reading note",
            "source correction",
            "source defect",
            "source oddity",
            "source pdf",
            "printed source",
            "source prints",
            "source reads",
            "source says",
            "source notes",
            "source omits",
            "source has",
            "french source refers",
            "french source introduces",
            "french re-edition prints",
            "french re-edition says",
            "french re-edition labels",
            "french pdf prints",
            "french pdf labels",
            "polo--gille pdf prints",
            "polo–gille pdf prints",
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
    if volume == "sga5":
        return "editorial note" in plain or "source note" in plain
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
    cursor = 0
    pieces: list[str] = []
    command_re = re.compile(
        r"\\(?P<name>footnote|footnotetext|markedfootnote|sourceoddity)\b"
    )
    while True:
        match = command_re.search(text, cursor)
        if match is None:
            pieces.append(text[cursor:])
            break
        pieces.append(text[cursor : match.start()])
        name = match.group("name")
        arg_count, body_index, kind = commands[name]
        try:
            end, args = parse_command_arguments(text, match.end(), arg_count)
        except ValueError:
            pieces.append(text[match.start() : match.end()])
            cursor = match.end()
            continue
        remove = name == "sourceoddity" or is_project_note(
            volume, args[body_index]
        )
        if remove:
            record_removal(
                removals,
                volume,
                relative_path,
                kind,
                text,
                match.start(),
                end,
            )
        else:
            pieces.append(text[match.start() : end])
        cursor = end
    return "".join(pieces)


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
            r"(?:\\emph|\\textit)\{Source note\.\}"
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

    roots = {key: TEMP_ROOT / key for key in ("sga1", "sga2", "sga3", "sga5")}
    with zipfile.ZipFile(SGA1_ARCHIVE) as archive:
        archive.extractall(roots["sga1"])
    shutil.copytree(SGA2_SOURCE, roots["sga2"])
    with zipfile.ZipFile(SGA3_ARCHIVE) as archive:
        archive.extractall(roots["sga3"])
    shutil.copytree(SGA5_SOURCE, roots["sga5"])

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
    "sga1": (
        "French source p.",
        "Editorial note.",
        "Source and status note",
        "source defect disclosed",
        "attested readings",
    ),
    "sga2": (
        "Source note.",
        "Source correction.",
        "source-normalization note",
        "The corrected French source adds",
        "French source PDF p.",
        "manager decision",
        "SGA2-X-L",
        "SGA2-XI-L",
    ),
    "sga3": (
        "Translator's note",
        "Translator’s note",
        "Source note:",
        "Source note.",
        "Source-reading note",
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
    "sga5": (
        "Editorial note.",
        "machine-assisted",
        "source-status",
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
    for volume in ("sga1", "sga2", "sga3", "sga5"):
        result = results[volume]
        lines.append(
            f"- {volume.upper()}: {result['pages']} pages, "
            f"SHA-256 `{result['sha256']}`."
        )
    lines.extend(
        [
            "",
            "SGA 4 and SGA 6 required no mathematical-body replacement and are",
            "retained byte-identically from the predecessor Zenodo version.",
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


def build() -> None:
    PACKAGE_ROOT.mkdir(parents=True, exist_ok=True)
    roots = prepare_sources()
    removals: list[Removal] = []
    for volume, root in roots.items():
        extensions = {".tex", ".texfrag"}
        for path in sorted(root.rglob("*")):
            if path.is_file() and path.suffix.lower() in extensions:
                clean_tex(path, root, volume, removals)

    results: dict[str, dict[str, object]] = {}
    for volume in ("sga1", "sga2", "sga3", "sga5"):
        root = roots[volume]
        master = root / MASTER_NAMES[volume]
        result = run_build(volume, root, master)
        output_pdf = PACKAGE_ROOT / PDF_OUTPUTS[volume]
        output_tex = PACKAGE_ROOT / TEX_OUTPUTS[volume]
        shutil.copy2(result["pdf"], output_pdf)
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
        "status": "PASS_READER_MATHEMATICAL_BODY_CLEAN",
        "volumes_rebuilt": ["SGA1", "SGA2", "SGA3", "SGA5"],
        "volumes_retained": ["SGA4", "SGA6"],
        "removals": len(removals),
        "removals_by_volume": {
            volume: sum(1 for row in removals if row.volume == volume)
            for volume in ("sga1", "sga2", "sga3", "sga5")
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
    args = parser.parse_args()
    try:
        build()
    except Exception as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    if not args.keep_temp:
        shutil.rmtree(TEMP_ROOT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

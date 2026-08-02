#!/usr/bin/env python3
"""Build exact private custody and derived public FAC/EGA live snapshots.

The source roots are read-only inputs.  The builder performs a byte-stability
replay, writes exact private ZIP custody outside the repository, and produces
privacy-clean, rights-aware public ZIP parts in the repository.  It preserves
generation disagreements as evidence and never promotes them to completion or
production-validation claims.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import shutil
import subprocess
import tempfile
import zipfile
from collections import Counter
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Callable, Iterable


REPO_ROOT = Path(__file__).resolve().parent.parent
FIXED_ZIP_TIME = (2026, 8, 2, 0, 0, 0)
GITHUB_FILE_LIMIT = 100 * 1024 * 1024
PUBLIC_PART_BUDGET = 88 * 1024 * 1024
CAPTURE_START = "2026-08-02T15:16:57+02:00"
CAPTURE_END = "2026-08-02T15:22:29+02:00"
CAPTURE_MODE = "sequential_copy_composite_byte_snapshot"
CAPTURE_COMPONENTS = {
    "fac_original": {
        "captured_through": "2026-08-02T15:17:09+02:00",
        "files": 851,
        "bytes": 356_931_436,
    },
    "ega_successor_original": {
        "captured_through": "2026-08-02T15:17:09+02:00",
        "files": 154,
        "bytes": 7_565_951,
    },
    "ega_french_canon_original": {
        "captured_through": "2026-08-02T15:22:29+02:00",
        "files": 1318,
        "bytes": 1_887_431_437,
    },
}

METHODOLOGY_DOI = "10.5281/zenodo.21124403"
REPLICATION_DOI = "10.5281/zenodo.20461174"

CONTROL_SPECS = (
    (
        "PROJECT_LOGBOOK_METHODOLOGY_REPLICATION_DOI_REQUIREMENT_20260802.md",
        2296,
        "BFA1E3A3EDA94E8C3425BAE50C842610A47D508FB260BF761BA3206883012679",
    ),
    (
        "ARCHIVE_PROACTIVE_PRIVACY_AND_SUBSTANTIVE_UPDATE_REQUIREMENT_20260802.md",
        3818,
        "098B41A98D9BE38E67316F5F34E4E2FE8F72613231268FC66C07801809C8613E",
    ),
)

EGA_R2_R9_STRICT_PROVENANCE = (
    "EGA1_PRINTED69_SECTION742_745_DIRECT_AUTHORITY_IMAGES.json",
    "EGA1_PRINTED69_70_SECTION751_753_DIRECT_AUTHORITY_IMAGES.json",
    "EGA1_PRINTED70_71_PROP754_DIRECT_AUTHORITY_IMAGES.json",
    "EGA1_PRINTED71_72_PROP755_763_DIRECT_AUTHORITY_IMAGES.json",
    "EGA1_PRINTED73_PROP764_7610_DIRECT_AUTHORITY_IMAGES.json",
    "EGA1_PRINTED74_PROP7611_7614_DIRECT_AUTHORITY_IMAGES.json",
    "EGA1_PRINTED74_75_SECTION7615_7618_DIRECT_AUTHORITY_IMAGES.json",
    "ENGLISH_CORRECTION_RECHECK_APPEND_20260802.jsonl",
    "ENGLISH_CORRECTION_RECHECK_APPEND_P70_20260802.jsonl",
    "ENGLISH_CORRECTION_RECHECK_APPEND_P71_20260802.jsonl",
    "ENGLISH_CORRECTION_RECHECK_APPEND_P71_P72_20260802.jsonl",
    "ENGLISH_CORRECTION_RECHECK_APPEND_P73_20260802.jsonl",
    "ENGLISH_CORRECTION_RECHECK_APPEND_P74_20260802.jsonl",
    "ENGLISH_CORRECTION_RECHECK_APPEND_P75_20260802.jsonl",
    "ENGLISH_CORRECTION_REPAIR_APPLICATION_20260802.jsonl",
    "ENGLISH_CORRECTION_REPAIR_APPLICATION_P70_20260802.jsonl",
    "ENGLISH_CORRECTION_REPAIR_APPLICATION_P71_20260802.jsonl",
    "ENGLISH_CORRECTION_REPAIR_APPLICATION_P71_P72_20260802.jsonl",
    "ENGLISH_CORRECTION_REPAIR_APPLICATION_P73_20260802.jsonl",
    "ENGLISH_CORRECTION_REPAIR_APPLICATION_P74_20260802.jsonl",
    "ENGLISH_CORRECTION_REPAIR_APPLICATION_P75_20260802.jsonl",
    "ENGLISH_REPAIR_VALIDATION_SUPERSESSION_P70_20260802.jsonl",
    "ENGLISH_REPAIR_VALIDATION_SUPERSESSION_P71_20260802.jsonl",
)

TEXT_EXTENSIONS = {
    ".aux",
    ".bat",
    ".bib",
    ".cfg",
    ".cls",
    ".cmd",
    ".csv",
    ".fls",
    ".ini",
    ".json",
    ".jsonl",
    ".log",
    ".md",
    ".out",
    ".ps1",
    ".py",
    ".sh",
    ".sty",
    ".tex",
    ".toml",
    ".tsv",
    ".txt",
    ".xml",
    ".yaml",
    ".yml",
}

WINDOWS_USER_HOME_RE = re.compile(
    r"(?i)(?:\\\\\?\\)?[A-Z]:[\\/]+Users[\\/]+[^\\/\s\"'<>|`\r\n]+"
)
POSIX_USER_HOME_RE = re.compile(
    r"(?i)(?<![A-Za-z0-9_])/(?:home|Users)/[^/\s\"'<>|`\r\n]+"
)
WINDOWS_ROOT_RE = re.compile(r"(?i)(?<![A-Za-z0-9_])[A-Z]:[\\/]+")
SECRET_LITERAL_RE = re.compile(
    r"(?i)(?:github_pat_[A-Za-z0-9_]{12,}|gh[pousr]_[A-Za-z0-9_]{12,}|"
    r"AKIA[0-9A-Z]{16}|sk-[A-Za-z0-9_-]{16,})"
)
CREDENTIAL_ASSIGNMENT_RE = re.compile(
    r"(?im)(\b(?:api[_-]?key|access[_-]?token|authorization|password|passwd|"
    r"client[_-]?secret|zenodo[_-]?token|github[_-]?token)\b[ \t]*[:=][ \t]*)"
    r"(?:\"[^\"\r\n]*\"|'[^'\r\n]*'|[^\s,;\r\n]+)"
)
AUTHORITY_PDF_FIELD_RE = re.compile(
    r'(?i)("authority_pdf"[ \t]*:[ \t]*")[^"\r\n]*[\\/]([^\\/"\r\n]+)(")'
)
SOURCE_SUCCESSOR_ROOT_FIELD_RE = re.compile(
    r'(?i)("source_successor_root"[ \t]*:[ \t]*")[^"]*(")'
)
ENGLISH_SOURCE_FILE_FIELD_RE = re.compile(
    r'(?i)("english_source_file"[ \t]*:[ \t]*")[^"]*[\\/]source[\\/]([^"\r\n]+)(")'
)
TASK_ID_RE = re.compile(
    r"(?i)\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b"
)
CODEX_STATE_RE = re.compile(r"(?i)(?<![A-Za-z0-9_])\.codex(?![A-Za-z0-9_])")
SOURCE_THREAD_FIELD_RE = re.compile(r"(?i)source_thread_id")
CODEX_DELEGATION_RE = re.compile(r"(?i)codex_delegation")
CLAUDE_AID_RE = re.compile(r"(?i)_claude_aid")
WORKING_TRANSLATIONS_RE = re.compile(r"(?i)03_working_translations")
PUBLICATION_CANDIDATES_RE = re.compile(r"(?i)06_publication_candidates")
ARCHIVE_TASK_MARKER_RE = re.compile(r"(?i)archive-maintenance task")

BINARY_ASCII_PATTERNS = (
    ("windows_user_home_ascii", re.compile(br"(?i)[A-Z]:[\\/]+Users[\\/]+")),
    ("posix_user_home_ascii", re.compile(br"(?i)/(?:home|Users)/[^/\x00\s]+")),
    (
        "secret_literal_ascii",
        re.compile(
            br"(?i)(?:github_pat_[A-Za-z0-9_]{12,}|gh[pousr]_[A-Za-z0-9_]{12,}|"
            br"AKIA[0-9A-Z]{16}|sk-[A-Za-z0-9_-]{16,})"
        ),
    ),
    ("windows_root_utf16le", re.compile(br"(?i)[A-Z]\x00:\x00[\\/]\x00")),
)


@dataclass(frozen=True)
class TreeEntry:
    relative_path: str
    bytes: int
    sha256: str


@dataclass(frozen=True)
class CorpusConfig:
    key: str
    title: str
    slug: str
    expected_files: int
    expected_bytes: int
    output_root: Path
    provenance_paths: tuple[str, ...]
    withheld: Callable[[str], bool]


@dataclass
class ProjectedEntry:
    original: TreeEntry
    kind: str
    encoding: str
    disposition: str
    public_bytes: int | None
    public_sha256: str | None
    action_count: int
    rules: tuple[str, ...]
    zip_part: str = ""


FAC_CONFIG = CorpusConfig(
    key="fac",
    title="Serre FAC live production custody snapshot",
    slug="serre-fac-live-custody-20260802",
    expected_files=851,
    expected_bytes=356_931_436,
    output_root=REPO_ROOT / "sources/serre/serre-fac-live-custody-20260802",
    provenance_paths=(
        "STATUS.md",
        "LOGBOOK.md",
        "EDITORIAL_DECISION_LOGBOOK.md",
        "controls/CHECKPOINT_IDENTITIES.csv",
        "controls/CHECKPOINT_VALIDATION.json",
        "controls/EDITORIAL_SELF_CORRECTION_LEDGER.csv",
        "controls/ENGLISH_NORMALIZATION_OCCURRENCES.csv",
        "controls/FRENCH_CORRECTIONS.csv",
        "controls/FRENCH_TRANSCRIPTION_REPAIRS.csv",
        "controls/TRANSLATION_LINEAGES.csv",
        "controls/TRANSLATION_PROGRESS.csv",
    ),
    withheld=lambda relative: relative.casefold().startswith("qa/authority/"),
)

EGA_CONFIG = CorpusConfig(
    key="ega",
    title="EGA global French-recheck live production custody snapshot",
    slug="ega-global-french-recheck-live-custody-20260802",
    expected_files=1472,
    expected_bytes=1_894_997_388,
    output_root=REPO_ROOT / "sources/ega/ega-global-french-recheck-live-custody-20260802",
    provenance_paths=(
        "successor/STATUS.md",
        "successor/LOGBOOK.md",
        "french_canon/STATUS.md",
        "french_canon/LOGBOOK.md",
        "french_canon/CONTINUATION_HANDOFF.md",
        "french_canon/README.md",
    ),
    withheld=lambda relative: relative.casefold().startswith("french_canon/qa/"),
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def csv_bytes(header: Iterable[str], rows: Iterable[Iterable[object]]) -> bytes:
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(header)
    writer.writerows(rows)
    return output.getvalue().encode("utf-8")


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, indent=2, ensure_ascii=True, sort_keys=True) + "\n").encode(
        "utf-8"
    )


def write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def validate_member_name(name: str) -> None:
    pure = PurePosixPath(name)
    if (
        not name
        or name.startswith(("/", "\\"))
        or "\\" in name
        or pure.is_absolute()
        or ".." in pure.parts
        or (pure.parts and ":" in pure.parts[0])
    ):
        raise RuntimeError(f"unsafe ZIP member path: {name!r}")


def zip_info(name: str, compression: int) -> zipfile.ZipInfo:
    validate_member_name(name)
    info = zipfile.ZipInfo(name, date_time=FIXED_ZIP_TIME)
    info.compress_type = compression
    info.create_system = 3
    info.external_attr = 0o100644 << 16
    return info


def is_within(path: Path, parent: Path) -> bool:
    try:
        path.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def prepare_output(path: Path, boundary: Path, replace: bool) -> None:
    path = path.resolve()
    boundary = boundary.resolve()
    if path == boundary or not is_within(path, boundary):
        raise RuntimeError(f"refusing unsafe output path: {path}")
    if path.exists():
        if not replace:
            raise RuntimeError(f"output exists; rerun with --replace-output: {path}")
        shutil.rmtree(path)
    path.mkdir(parents=True)


def iter_source_files(root: Path) -> list[Path]:
    if not root.is_dir():
        raise RuntimeError(f"source root is not a directory: {root}")
    symlinks = [path for path in root.rglob("*") if path.is_symlink()]
    if symlinks:
        raise RuntimeError(f"source tree contains symlinks: {symlinks[:3]}")
    files = [path for path in root.rglob("*") if path.is_file()]
    return sorted(files, key=lambda path: path.relative_to(root).as_posix())


def scan_tree(root: Path) -> list[TreeEntry]:
    return [
        TreeEntry(
            relative_path=path.relative_to(root).as_posix(),
            bytes=path.stat().st_size,
            sha256=sha256_path(path),
        )
        for path in iter_source_files(root)
    ]


def tree_manifest(entries: list[TreeEntry]) -> bytes:
    return csv_bytes(
        ("relative_path", "bytes", "sha256"),
        ((entry.relative_path, entry.bytes, entry.sha256) for entry in entries),
    )


def tree_identity(entries: list[TreeEntry]) -> str:
    return sha256_bytes(tree_manifest(entries))


def stable_copy(source: Path, target: Path) -> list[TreeEntry]:
    before = scan_tree(source)
    target.mkdir(parents=True)
    for entry in before:
        source_path = source / PurePosixPath(entry.relative_path)
        target_path = target / PurePosixPath(entry.relative_path)
        target_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source_path, target_path)
    copied = scan_tree(target)
    after = scan_tree(source)
    if before != copied or copied != after:
        raise RuntimeError("source bytes changed during stable capture replay")
    return copied


def decode_text(data: bytes, relative_path: str) -> tuple[str, str] | None:
    extension = PurePosixPath(relative_path).suffix.casefold()
    declared_text = extension in TEXT_EXTENSIONS
    if not declared_text and b"\x00" in data[:8192]:
        return None
    candidates: list[tuple[str, str]] = []
    if data.startswith(b"\xef\xbb\xbf"):
        candidates.append(("utf-8-sig", "utf-8-sig"))
    elif data.startswith(b"\xff\xfe"):
        candidates.append(("utf-16", "utf-16le-bom"))
    elif data.startswith(b"\xfe\xff"):
        candidates.append(("utf-16", "utf-16be-bom"))
    candidates.extend((("utf-8", "utf-8"), ("cp1252", "cp1252")))
    for codec, label in candidates:
        try:
            text = data.decode(codec)
        except UnicodeDecodeError:
            continue
        if declared_text:
            return text, label
        sample = text[:8192]
        if sample and sum(character.isprintable() or character in "\r\n\t" for character in sample) / len(sample) >= 0.95:
            return text, label
    if declared_text:
        raise RuntimeError(f"declared text file could not be decoded: {relative_path}")
    return None


def encode_text(text: str, encoding: str) -> bytes:
    codecs = {
        "utf-8-sig": "utf-8-sig",
        "utf-16le-bom": "utf-16",
        "utf-16be-bom": "utf-16",
        "utf-8": "utf-8",
        "cp1252": "cp1252",
    }
    return text.encode(codecs[encoding])


def apply_rule(
    text: str,
    relative_path: str,
    rule_name: str,
    pattern: re.Pattern[str],
    replacement: str | Callable[[re.Match[str]], str],
) -> tuple[str, list[tuple[str, str, int, int]]]:
    actions: list[tuple[str, str, int, int]] = []
    ordinal = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal ordinal
        ordinal += 1
        line = text.count("\n", 0, match.start()) + 1
        actions.append((relative_path, rule_name, ordinal, line))
        return replacement(match) if callable(replacement) else replacement

    return pattern.sub(replace, text), actions


def redact_text(
    text: str, relative_path: str
) -> tuple[str, list[tuple[str, str, int, int]]]:
    actions: list[tuple[str, str, int, int]] = []
    rules: tuple[
        tuple[str, re.Pattern[str], str | Callable[[re.Match[str]], str]], ...
    ] = (
        (
            "authority_pdf_to_filename_hash_locator",
            AUTHORITY_PDF_FIELD_RE,
            lambda match: (
                match.group(1)
                + match.group(2)
                + " (exact authority SHA-256 in sibling field)"
                + match.group(3)
            ),
        ),
        (
            "english_source_file_to_stable_relative_path",
            ENGLISH_SOURCE_FILE_FIELD_RE,
            lambda match: match.group(1)
            + "source/"
            + match.group(2).replace("\\", "/")
            + match.group(3),
        ),
        (
            "source_successor_root_to_stable_root_id",
            SOURCE_SUCCESSOR_ROOT_FIELD_RE,
            lambda match: match.group(1)
            + "EGA_FRENCH_RECHECK_SOURCE_SUCCESSOR_20260802/."
            + match.group(2),
        ),
        ("secret_literal", SECRET_LITERAL_RE, "<REDACTED_SECRET>"),
        (
            "credential_assignment",
            CREDENTIAL_ASSIGNMENT_RE,
            lambda match: match.group(1) + "<REDACTED_SECRET>",
        ),
        ("codex_task_id", TASK_ID_RE, "<REDACTED_TASK_ID>"),
        ("codex_state_directory", CODEX_STATE_RE, "<REDACTED_CODEX_STATE>"),
        (
            "source_thread_field",
            SOURCE_THREAD_FIELD_RE,
            "redacted_thread_field",
        ),
        (
            "codex_delegation_marker",
            CODEX_DELEGATION_RE,
            "redacted_delegation_marker",
        ),
        ("external_agent_id", CLAUDE_AID_RE, "_redacted_external_agent_id"),
        (
            "internal_working_tree_segment",
            WORKING_TRANSLATIONS_RE,
            "<REDACTED_INTERNAL_WORKSPACE>",
        ),
        (
            "internal_publication_staging_segment",
            PUBLICATION_CANDIDATES_RE,
            "<REDACTED_INTERNAL_PUBLICATION_STAGING>",
        ),
        (
            "archive_workflow_marker",
            ARCHIVE_TASK_MARKER_RE,
            "archive workflow",
        ),
        ("windows_user_home", WINDOWS_USER_HOME_RE, "<REDACTED_USER_HOME>"),
        ("posix_user_home", POSIX_USER_HOME_RE, "<REDACTED_USER_HOME>"),
        ("windows_absolute_root", WINDOWS_ROOT_RE, "<REDACTED_LOCAL_ROOT>/"),
    )
    for name, pattern, replacement in rules:
        text, found = apply_rule(text, relative_path, name, pattern, replacement)
        actions.extend(found)
    return text, actions


def residual_text_findings(text: str) -> list[tuple[str, int]]:
    findings: list[tuple[str, int]] = []
    for name, pattern in (
        ("windows_user_home", WINDOWS_USER_HOME_RE),
        ("posix_user_home", POSIX_USER_HOME_RE),
        ("windows_absolute_root", WINDOWS_ROOT_RE),
        ("secret_literal", SECRET_LITERAL_RE),
        ("codex_task_id", TASK_ID_RE),
        ("codex_state_directory", CODEX_STATE_RE),
        ("source_thread_field", SOURCE_THREAD_FIELD_RE),
        ("codex_delegation_marker", CODEX_DELEGATION_RE),
        ("external_agent_id", CLAUDE_AID_RE),
        ("internal_working_tree_segment", WORKING_TRANSLATIONS_RE),
        ("internal_publication_staging_segment", PUBLICATION_CANDIDATES_RE),
        ("archive_workflow_marker", ARCHIVE_TASK_MARKER_RE),
    ):
        count = len(pattern.findall(text))
        if count:
            findings.append((name, count))
    for match in CREDENTIAL_ASSIGNMENT_RE.finditer(text):
        if "<REDACTED_SECRET>" not in match.group(0):
            findings.append(("credential_assignment", 1))
    return findings


def binary_findings(data: bytes) -> list[tuple[str, int]]:
    findings: list[tuple[str, int]] = []
    for name, pattern in BINARY_ASCII_PATTERNS:
        count = len(pattern.findall(data))
        if count:
            findings.append((name, count))
    return findings


def extract_pdf_text(pdftotext: Path, path: Path) -> bytes:
    def run(input_path: Path) -> subprocess.CompletedProcess[bytes]:
        return subprocess.run(
            [str(pdftotext), "-enc", "UTF-8", "-nopgbrk", str(input_path), "-"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )

    # MiKTeX's Windows pdftotext cannot open otherwise valid paths near the
    # legacy MAX_PATH boundary.  Python can read those paths, so stage only
    # long inputs under a short temporary name before extracted-text scanning.
    if len(str(path)) >= 220:
        with tempfile.TemporaryDirectory(prefix="fac-ega-pdfscan-") as temporary:
            staged = Path(temporary) / "input.pdf"
            shutil.copyfile(path, staged)
            result = run(staged)
    else:
        result = run(path)
    if result.returncode != 0:
        message = result.stderr.decode("utf-8", errors="replace")[:500]
        raise RuntimeError(f"pdftotext failed for {path.name}: {message}")
    return result.stdout


def write_zip(
    path: Path,
    members: Iterable[tuple[str, Path | bytes]],
    compression: int,
) -> dict[str, object]:
    expected: dict[str, tuple[int, str]] = {}
    with zipfile.ZipFile(path, "w") as archive:
        for name, source in sorted(members, key=lambda row: row[0]):
            validate_member_name(name)
            data = source if isinstance(source, bytes) else source.read_bytes()
            if name in expected:
                raise RuntimeError(f"duplicate ZIP member: {name}")
            expected[name] = (len(data), sha256_bytes(data))
            archive.writestr(
                zip_info(name, compression),
                data,
                compress_type=compression,
                compresslevel=9 if compression == zipfile.ZIP_DEFLATED else None,
            )
    with zipfile.ZipFile(path) as archive:
        infos = archive.infolist()
        names = [info.filename for info in infos]
        if len(names) != len(set(names)) or set(names) != set(expected):
            raise RuntimeError(f"ZIP closure failed: {path.name}")
        if archive.testzip() is not None:
            raise RuntimeError(f"ZIP CRC replay failed: {path.name}")
        for name, (expected_bytes, expected_sha) in expected.items():
            data = archive.read(name)
            if len(data) != expected_bytes or sha256_bytes(data) != expected_sha:
                raise RuntimeError(f"ZIP member replay failed: {path.name}:{name}")
    return {
        "path": path.name,
        "bytes": path.stat().st_size,
        "sha256": sha256_path(path),
        "members": len(expected),
        "uncompressed_bytes": sum(value[0] for value in expected.values()),
        "replay_errors": [],
    }


def partition_projected(
    entries: list[ProjectedEntry], budget: int
) -> list[list[ProjectedEntry]]:
    parts: list[list[ProjectedEntry]] = []
    current: list[ProjectedEntry] = []
    current_bytes = 0
    for entry in entries:
        if entry.public_bytes is None:
            continue
        if entry.public_bytes > budget:
            raise RuntimeError(f"single projected file exceeds ZIP budget: {entry.original.relative_path}")
        if current and current_bytes + entry.public_bytes > budget:
            parts.append(current)
            current = []
            current_bytes = 0
        current.append(entry)
        current_bytes += entry.public_bytes
    if current:
        parts.append(current)
    return parts


def copy_controls(
    control_root: Path, output_root: Path
) -> tuple[list[dict[str, object]], list[tuple[str, str, int, int]]]:
    identities: list[dict[str, object]] = []
    all_actions: list[tuple[str, str, int, int]] = []
    for name, expected_bytes, expected_sha in CONTROL_SPECS:
        source = control_root / name
        data = source.read_bytes()
        actual_sha = sha256_bytes(data)
        if len(data) != expected_bytes or actual_sha != expected_sha:
            raise RuntimeError(
                f"control identity changed: {name} {len(data)} B {actual_sha}"
            )
        decoded = decode_text(data, name)
        if decoded is None:
            raise RuntimeError(f"control is not text: {name}")
        public_relative = f"archive_controls/{name}"
        projected, actions = redact_text(decoded[0], public_relative)
        public_data = encode_text(projected, decoded[1])
        if residual_text_findings(projected):
            raise RuntimeError(f"control privacy projection failed: {name}")
        target = output_root / "archive_controls" / name
        write_bytes(target, public_data)
        all_actions.extend(actions)
        identities.append(
            {
                "relative_path": public_relative,
                "original_bytes": len(data),
                "original_sha256": actual_sha,
                "public_bytes": len(public_data),
                "public_sha256": sha256_bytes(public_data),
                "privacy_action_count": len(actions),
                "status": "BOUND_EXACT_ORIGINAL_IDENTITY_WITH_PRIVACY_CLEAN_PUBLIC_PROJECTION",
            }
        )
    return identities, all_actions


def analyze_fac(stage: Path) -> dict[str, object]:
    status = (stage / "STATUS.md").read_text(encoding="utf-8-sig")
    status_units = [int(value) for value in re.findall(r"FAC-EN-U(\d{4})", status)]
    components = []
    component_root = stage / "english_source_first_workpass/source/components"
    for path in component_root.glob("*.tex"):
        match = re.match(r"(\d{3})_", path.name)
        if match:
            components.append(int(match.group(1)))
    validation_path = stage / "controls/CHECKPOINT_VALIDATION.json"
    validation = json.loads(validation_path.read_text(encoding="utf-8-sig"))
    validator_units = int(validation["scope"]["active_english_components"])
    identities_path = stage / "controls/CHECKPOINT_IDENTITIES.csv"
    validation_identity = validation["csv"]["CHECKPOINT_IDENTITIES.csv"]
    current_identity = {
        "bytes": identities_path.stat().st_size,
        "sha256": sha256_path(identities_path),
    }
    return {
        "classification": "LIVE_COMPOSITE_BYTE_CUSTODY_NOT_SEMANTIC_CHECKPOINT",
        "status_declared_highest_unit": f"U{max(status_units):04d}",
        "captured_highest_component": f"U{max(components):04d}",
        "validator_bound_highest_unit": f"U{validator_units:04d}",
        "status_component_lag": max(status_units) != max(components),
        "validator_status_lag": validator_units != max(status_units),
        "checkpoint_identities_current": current_identity,
        "checkpoint_identities_bound_by_validator": {
            "bytes": validation_identity["bytes"],
            "sha256": validation_identity["sha256"],
        },
        "validator_manifest_matches_captured_identity": current_identity
        == {
            "bytes": validation_identity["bytes"],
            "sha256": validation_identity["sha256"],
        },
        "validator_status": validation.get("status"),
        "validator_overall_work_status": validation.get("overall_work_status"),
        "claim": "no completion, publication readiness, semantic coherence, or QA certification inferred",
    }


def analyze_ega(stage: Path) -> dict[str, object]:
    successor = stage / "successor"
    french_canon = stage / "french_canon"
    manifest_path = successor / "controls/SOURCE_INPUT_SHA256_R9.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
    mismatches: list[dict[str, object]] = []
    for row in manifest["files"]:
        source_path = successor / "source" / PurePosixPath(row["relative_path"])
        if not source_path.is_file():
            mismatches.append(
                {
                    "relative_path": f"successor/source/{row['relative_path']}",
                    "reason": "missing_from_captured_tree",
                    "r9_bytes": row["bytes"],
                    "r9_sha256": row["sha256"],
                }
            )
            continue
        actual = {"bytes": source_path.stat().st_size, "sha256": sha256_path(source_path)}
        if actual != {"bytes": row["bytes"], "sha256": row["sha256"]}:
            mismatches.append(
                {
                    "relative_path": f"successor/source/{row['relative_path']}",
                    "reason": "captured_content_differs_from_r9_control",
                    "r9_bytes": row["bytes"],
                    "r9_sha256": row["sha256"],
                    "captured_bytes": actual["bytes"],
                    "captured_sha256": actual["sha256"],
                }
            )
    diff = json.loads(
        (successor / "controls/SOURCE_DIFF_VALIDATION_R9.json").read_text(
            encoding="utf-8-sig"
        )
    )
    canon_all_files = iter_source_files(french_canon)
    canon_controls = sorted(
        path for path in (french_canon / "controls").rglob("*") if path.is_file()
    )
    strict_paths = [french_canon / "controls" / name for name in EGA_R2_R9_STRICT_PROVENANCE]
    strict_missing = [path.name for path in strict_paths if not path.is_file()]
    strict_bytes = sum(path.stat().st_size for path in strict_paths if path.is_file())
    if strict_missing or len(strict_paths) != 23 or strict_bytes != 89_822:
        raise RuntimeError(
            f"EGA R2-R9 strict provenance boundary changed: missing={strict_missing}, "
            f"files={len(strict_paths)}, bytes={strict_bytes}"
        )
    policy_path = (
        french_canon
        / "controls/ENGLISH_NORMALIZATION_DECISION_AND_REVISION_POLICY_20260802.md"
    )
    if (
        policy_path.stat().st_size != 6628
        or sha256_path(policy_path)
        != "AE09C581B4EC6B0DFF647EBD367A2FA455C0895CCE43CC54D8A4315185677EE5"
    ):
        raise RuntimeError("EGA normalization/revision policy identity changed")
    return {
        "classification": "LIVE_COMPOSITE_BYTE_CUSTODY_WITH_R9_CONTROL_CONTENT_LAG",
        "r9_manifest": {
            "relative_path": "successor/controls/SOURCE_INPUT_SHA256_R9.json",
            "bytes": manifest_path.stat().st_size,
            "sha256": sha256_path(manifest_path),
            "declared_files": manifest["file_count"],
            "declared_bytes": manifest["total_bytes"],
            "declared_tree_sha256": manifest["canonical_tree_sha256"],
        },
        "r9_diff_control_status": diff.get("status"),
        "r9_diff_control_errors": diff.get("errors"),
        "r9_control_content_match": not mismatches,
        "r9_control_content_mismatch_count": len(mismatches),
        "r9_control_content_mismatches": mismatches,
        "french_canon_custody": {
            "files": len(canon_all_files),
            "bytes": sum(path.stat().st_size for path in canon_all_files),
            "controls_files": len(canon_controls),
            "controls_bytes": sum(path.stat().st_size for path in canon_controls),
            "strict_r2_r9_provenance_files": len(strict_paths),
            "strict_r2_r9_provenance_bytes": strict_bytes,
            "strict_r2_r9_provenance_paths": [
                f"french_canon/controls/{path.name}" for path in strict_paths
            ],
            "normalization_revision_policy": {
                "relative_path": "french_canon/controls/ENGLISH_NORMALIZATION_DECISION_AND_REVISION_POLICY_20260802.md",
                "bytes": policy_path.stat().st_size,
                "sha256": sha256_path(policy_path),
            },
            "all_controls_public_projected_and_dual_doi_bound": True,
            "all_source_files_public_projected_with_license_not_specified_caveat": True,
            "all_qa_files_private_custody_only_pending_rights_clearance": True,
        },
        "claim": "captured bytes are not certified as coherent R9, complete, rebuilt, reference-replayed, or publication-ready",
    }


def markdown_status(
    config: CorpusConfig,
    entries: list[TreeEntry],
    analysis: dict[str, object],
    projected: list[ProjectedEntry],
) -> bytes:
    withheld = [entry for entry in projected if entry.public_bytes is None]
    redacted = [entry for entry in projected if entry.action_count]
    lines = [
        f"# {config.title}",
        "",
        "Date: 2026-08-02",
        "",
        "Status: exact byte custody of a live sequential capture; not a production completion or validation claim.",
        "",
        "## Capture boundary",
        "",
        f"- Capture window: `{CAPTURE_START}` through `{CAPTURE_END}`.",
        f"- Component capture boundaries: `{json.dumps(CAPTURE_COMPONENTS, sort_keys=True)}`.",
        f"- Capture mode: `{CAPTURE_MODE}`. Because files were copied sequentially, the tree is a composite byte snapshot, not an asserted filesystem-atomic or semantic checkpoint.",
        f"- Exact captured files: {len(entries):,}; exact captured bytes: {sum(entry.bytes for entry in entries):,}; original manifest SHA-256: `{tree_identity(entries)}`.",
        "- Producer trees were not modified. Every captured byte is retained in the private exact-custody ZIP.",
        "",
        "## Generation/status caveat",
        "",
        "```json",
        json.dumps(analysis, indent=2, ensure_ascii=True, sort_keys=True),
        "```",
        "",
        "The identities above are preserved as disagreeing evidence. This archive does not repair, reinterpret, or certify production decisions.",
        "",
        "## Public projection",
        "",
        f"- Public-projected producer files: {len(projected) - len(withheld):,}.",
        f"- Text files mechanically redacted: {len(redacted):,}; total redaction actions: {sum(entry.action_count for entry in redacted):,}.",
        f"- Rights-withheld files: {len(withheld):,}; rights-withheld bytes: {sum(entry.original.bytes for entry in withheld):,}.",
        "- Every withheld file remains listed by exact path, bytes, and SHA-256 in `ORIGINAL_PUBLIC_MANIFEST.csv` with disposition `RIGHTS_UNCLEARED_PRIVATE_CUSTODY_ONLY`.",
        "- Public redaction changes only machine-local absolute roots, user-home prefixes, or detected secret values. All other bytes are preserved.",
        "- Project-authored provenance/control surfaces in the dual-DOI payload are marked CC0-1.0. Corpus source and build artifacts remain `License Not Specified`; packaging does not manufacture a rights grant.",
        "",
        "## Dual-DOI provenance route",
        "",
        f"The exact provenance ZIP under `dual_doi/` is intended for both methodology DOI `{METHODOLOGY_DOI}` and replication DOI `{REPLICATION_DOI}`. Packaging does not itself assert that either DOI has been updated.",
        "",
    ]
    return "\n".join(lines).encode("utf-8")


def build_private_custody(
    config: CorpusConfig,
    stage: Path,
    entries: list[TreeEntry],
    private_parent: Path,
    replace: bool,
) -> tuple[Path, dict[str, object]]:
    output = private_parent / config.slug
    prepare_output(output, private_parent, replace)
    manifest = tree_manifest(entries)
    write_bytes(output / "ORIGINAL_MANIFEST.csv", manifest)
    members: list[tuple[str, Path | bytes]] = [
        (f"payload/{entry.relative_path}", stage / PurePosixPath(entry.relative_path))
        for entry in entries
    ]
    members.append(("ORIGINAL_MANIFEST.csv", manifest))
    archive_path = output / f"{config.slug}-exact-private-custody.zip"
    archive = write_zip(archive_path, members, zipfile.ZIP_STORED)
    validation = {
        "schema": "fac_ega_exact_private_custody_v1",
        "corpus": config.key,
        "capture": {
            "start": CAPTURE_START,
            "end": CAPTURE_END,
            "mode": CAPTURE_MODE,
            "components": CAPTURE_COMPONENTS,
        },
        "source_root_label": stage.name,
        "files": len(entries),
        "bytes": sum(entry.bytes for entry in entries),
        "original_manifest": {
            "bytes": len(manifest),
            "sha256": sha256_bytes(manifest),
        },
        "archive": archive,
        "producer_source_mutated": False,
        "archive_member_replay": "PASS",
    }
    write_bytes(output / "PRIVATE_CUSTODY_VALIDATION.json", json_bytes(validation))
    sums = []
    for path in sorted(output.iterdir(), key=lambda item: item.name):
        if path.is_file() and path.name != "SHA256SUMS.csv":
            sums.append((path.name, path.stat().st_size, sha256_path(path)))
    write_bytes(output / "SHA256SUMS.csv", csv_bytes(("path", "bytes", "sha256"), sums))
    return output, validation


def is_project_authored_provenance(config: CorpusConfig, relative: str) -> bool:
    if config.key == "fac":
        return relative.startswith("controls/") or (
            "/" not in relative and PurePosixPath(relative).suffix.casefold() == ".md"
        )
    return (
        relative.startswith("successor/controls/")
        or relative.startswith("french_canon/controls/")
        or (
            relative.startswith(("successor/", "french_canon/"))
            and relative.count("/") == 1
            and PurePosixPath(relative).suffix.casefold() in {".md", ".json", ".jsonl"}
        )
    )


def dual_doi_provenance_paths(
    config: CorpusConfig, projected: list[ProjectedEntry]
) -> list[str]:
    available = {
        entry.original.relative_path
        for entry in projected
        if entry.public_bytes is not None
    }
    selected = {
        relative for relative in available if is_project_authored_provenance(config, relative)
    }
    selected.update(config.provenance_paths)
    missing = sorted(selected - available)
    if missing:
        raise RuntimeError(f"mandatory public provenance surfaces missing: {missing[:5]}")
    return sorted(selected)


def build_public_projection(
    config: CorpusConfig,
    stage: Path,
    entries: list[TreeEntry],
    control_root: Path,
    pdftotext: Path,
    replace: bool,
    temp_parent: Path,
) -> dict[str, object]:
    output = config.output_root
    prepare_output(output, REPO_ROOT, replace)
    projected_stage = temp_parent / f"{config.key}-public-projection"
    projected_stage.mkdir()

    actions: list[tuple[str, str, int, int]] = []
    projected: list[ProjectedEntry] = []
    binary_scan_rows: list[tuple[object, ...]] = []
    pdf_scan_rows: list[tuple[object, ...]] = []
    public_errors: list[str] = []

    for entry in entries:
        source = stage / PurePosixPath(entry.relative_path)
        data = source.read_bytes()
        withheld = config.withheld(entry.relative_path)
        decoded = decode_text(data, entry.relative_path)
        if decoded is not None:
            if withheld:
                public_data = data
                found = []
                rules = ()
            else:
                redacted, found = redact_text(decoded[0], entry.relative_path)
                public_data = encode_text(redacted, decoded[1])
                residual = residual_text_findings(redacted)
                if residual:
                    public_errors.append(f"text residual {entry.relative_path}: {residual}")
                rules = tuple(sorted({row[1] for row in found}))
                actions.extend(found)
            kind = "text"
            encoding = decoded[1]
            raw_findings = []
        else:
            raw_findings = binary_findings(data)
            if raw_findings and not withheld:
                public_errors.append(f"binary privacy finding {entry.relative_path}: {raw_findings}")
            public_data = data
            rules = ()
            found = []
            kind = "binary"
            encoding = ""
            binary_scan_rows.append(
                (
                    entry.relative_path,
                    entry.bytes,
                    entry.sha256,
                    sum(count for _name, count in raw_findings),
                    ";".join(name for name, _count in raw_findings),
                    "PRIVATE_ONLY" if withheld else "PUBLIC_PROJECTED",
                    "PASS_PRIVATE_CUSTODY_ONLY" if withheld else ("PASS" if not raw_findings else "FAIL"),
                )
            )

        if source.suffix.casefold() == ".pdf":
            extracted = extract_pdf_text(pdftotext, source)
            extracted_text = extracted.decode("utf-8", errors="replace")
            extracted_findings = residual_text_findings(extracted_text)
            if extracted_findings and not withheld:
                public_errors.append(
                    f"PDF extracted-text privacy finding {entry.relative_path}: {extracted_findings}"
                )
            pdf_scan_rows.append(
                (
                    entry.relative_path,
                    entry.bytes,
                    entry.sha256,
                    len(extracted),
                    sum(count for _name, count in extracted_findings),
                    ";".join(name for name, _count in extracted_findings),
                    "PRIVATE_ONLY" if withheld else "PUBLIC_PROJECTED",
                    "PASS_PRIVATE_CUSTODY_ONLY" if withheld else ("PASS" if not extracted_findings else "FAIL"),
                )
            )

        if withheld:
            projected.append(
                ProjectedEntry(
                    original=entry,
                    kind=kind,
                    encoding=encoding,
                    disposition="RIGHTS_UNCLEARED_PRIVATE_CUSTODY_ONLY",
                    public_bytes=None,
                    public_sha256=None,
                    action_count=0,
                    rules=(),
                )
            )
            continue

        target = projected_stage / PurePosixPath(entry.relative_path)
        write_bytes(target, public_data)
        projected.append(
            ProjectedEntry(
                original=entry,
                kind=kind,
                encoding=encoding,
                disposition=(
                    "PUBLIC_PROJECTION_REDACTED" if found else "PUBLIC_PROJECTION_BYTE_IDENTICAL"
                ),
                public_bytes=len(public_data),
                public_sha256=sha256_bytes(public_data),
                action_count=len(found),
                rules=rules,
            )
        )

    if public_errors:
        raise RuntimeError("public privacy scan failed: " + " | ".join(public_errors[:10]))

    parts = partition_projected(projected, PUBLIC_PART_BUDGET)
    part_receipts: list[dict[str, object]] = []
    zip_dir = output / "public_zip_parts"
    zip_dir.mkdir()
    for index, part in enumerate(parts, start=1):
        zip_name = f"{config.slug}-public-part-{index:03d}-of-{len(parts):03d}.zip"
        for entry in part:
            entry.zip_part = f"public_zip_parts/{zip_name}"
        part_manifest = csv_bytes(
            ("relative_path", "bytes", "sha256"),
            (
                (entry.original.relative_path, entry.public_bytes, entry.public_sha256)
                for entry in part
            ),
        )
        members: list[tuple[str, Path | bytes]] = [
            (
                f"payload/{entry.original.relative_path}",
                projected_stage / PurePosixPath(entry.original.relative_path),
            )
            for entry in part
        ]
        members.append(("PUBLIC_PART_MANIFEST.csv", part_manifest))
        receipt = write_zip(zip_dir / zip_name, members, zipfile.ZIP_DEFLATED)
        if receipt["bytes"] >= GITHUB_FILE_LIMIT:
            raise RuntimeError(f"public ZIP is not below GitHub 100 MiB limit: {zip_name}")
        receipt.update(
            {
                "relative_path": f"public_zip_parts/{zip_name}",
                "payload_files": len(part),
                "payload_bytes": sum(entry.public_bytes or 0 for entry in part),
                "embedded_manifest_bytes": len(part_manifest),
                "embedded_manifest_sha256": sha256_bytes(part_manifest),
                "github_100_mib_limit": GITHUB_FILE_LIMIT,
                "below_limit": True,
            }
        )
        part_receipts.append(receipt)

    mapping = csv_bytes(
        (
            "relative_path",
            "original_bytes",
            "original_sha256",
            "kind",
            "encoding",
            "disposition",
            "public_bytes",
            "public_sha256",
            "privacy_action_count",
            "privacy_rules",
            "public_zip_part",
            "rights_status",
            "withheld_reason",
        ),
        (
            (
                entry.original.relative_path,
                entry.original.bytes,
                entry.original.sha256,
                entry.kind,
                entry.encoding,
                entry.disposition,
                "" if entry.public_bytes is None else entry.public_bytes,
                "" if entry.public_sha256 is None else entry.public_sha256,
                entry.action_count,
                ";".join(entry.rules),
                entry.zip_part,
                (
                    "RIGHTS_UNCLEARED_PRIVATE_CUSTODY_ONLY"
                    if entry.public_bytes is None
                    else (
                        "CC0-1.0_PROJECT_AUTHORED_PROVENANCE"
                        if is_project_authored_provenance(config, entry.original.relative_path)
                        else "LICENSE_NOT_SPECIFIED_CORPUS_SOURCE_OR_BUILD_ARTIFACT"
                    )
                ),
                (
                    "RIGHTS_UNCLEARED_PRIVATE_CUSTODY_ONLY"
                    if entry.public_bytes is None
                    else ""
                ),
            )
            for entry in projected
        ),
    )
    write_bytes(output / "ORIGINAL_PUBLIC_MANIFEST.csv", mapping)

    controls, control_actions = copy_controls(control_root, output)
    actions.extend(control_actions)
    write_bytes(output / "ARCHIVE_CONTROL_IDENTITIES.json", json_bytes(controls))

    action_ledger = csv_bytes(
        ("relative_path", "rule", "rule_occurrence_in_file", "line"), actions
    )
    write_bytes(output / "PRIVACY_ACTION_LEDGER.csv", action_ledger)
    write_bytes(
        output / "BINARY_PRIVACY_SCAN.csv",
        csv_bytes(
            (
                "relative_path",
                "bytes",
                "sha256",
                "raw_finding_count",
                "finding_rules",
                "disposition",
                "scan_status",
            ),
            binary_scan_rows,
        ),
    )
    write_bytes(
        output / "PDF_EXTRACTED_TEXT_PRIVACY_SCAN.csv",
        csv_bytes(
            (
                "relative_path",
                "pdf_bytes",
                "pdf_sha256",
                "extracted_text_bytes",
                "finding_count",
                "finding_rules",
                "disposition",
                "scan_status",
            ),
            pdf_scan_rows,
        ),
    )

    analysis = analyze_fac(stage) if config.key == "fac" else analyze_ega(stage)
    status = markdown_status(config, entries, analysis, projected)
    write_bytes(output / "ARCHIVE_SNAPSHOT_STATUS.md", status)
    readme = (
        f"# {config.title}\n\n"
        "Start with `ARCHIVE_SNAPSHOT_STATUS.md`. `ORIGINAL_PUBLIC_MANIFEST.csv` "
        "binds every captured file to its private original and public disposition. "
        "Public ZIP parts contain every non-withheld projected file; no public ZIP "
        "reaches GitHub's 100 MiB file boundary. The `dual_doi/` ZIP contains the "
        "privacy-clean provenance/logbook surfaces for identical deposit into the "
        f"methodology ({METHODOLOGY_DOI}) and replication ({REPLICATION_DOI}) lineages.\n"
    ).encode("utf-8")
    write_bytes(output / "README.md", readme)

    provenance_paths = dual_doi_provenance_paths(config, projected)
    for relative in provenance_paths:
        source = projected_stage / PurePosixPath(relative)
        if not source.is_file():
            raise RuntimeError(f"mandatory provenance surface missing: {relative}")
        write_bytes(output / "provenance" / PurePosixPath(relative), source.read_bytes())

    privacy_counts = Counter(row[1] for row in actions)
    privacy_validation = {
        "schema": "fac_ega_public_privacy_projection_v1",
        "corpus": config.key,
        "captured_files": len(entries),
        "captured_bytes": sum(entry.bytes for entry in entries),
        "public_projected_files": sum(entry.public_bytes is not None for entry in projected),
        "rights_withheld_files": sum(entry.public_bytes is None for entry in projected),
        "rights_withheld_bytes": sum(
            entry.original.bytes for entry in projected if entry.public_bytes is None
        ),
        "redacted_text_files": sum(entry.action_count > 0 for entry in projected)
        + sum(identity["privacy_action_count"] > 0 for identity in controls),
        "redaction_actions": len(actions),
        "redaction_actions_by_rule": dict(sorted(privacy_counts.items())),
        "binary_files_scanned": len(binary_scan_rows),
        "pdf_files_extracted_and_scanned": len(pdf_scan_rows),
        "public_text_residual_findings": 0,
        "public_binary_raw_findings": 0,
        "public_pdf_extracted_text_findings": 0,
        "errors": [],
        "status": "PASS_PUBLIC_PROJECTION_PRIVACY_CLEAN",
    }
    write_bytes(output / "PRIVACY_VALIDATION.json", json_bytes(privacy_validation))

    part_manifest = csv_bytes(
        (
            "relative_path",
            "bytes",
            "sha256",
            "payload_files",
            "payload_bytes",
            "below_github_100_mib_limit",
        ),
        (
            (
                receipt["relative_path"],
                receipt["bytes"],
                receipt["sha256"],
                receipt["payload_files"],
                receipt["payload_bytes"],
                receipt["below_limit"],
            )
            for receipt in part_receipts
        ),
    )
    write_bytes(output / "PUBLIC_ARCHIVE_PARTS.csv", part_manifest)

    dual_paths = [
        "README.md",
        "ARCHIVE_SNAPSHOT_STATUS.md",
        "ARCHIVE_CONTROL_IDENTITIES.json",
        "ORIGINAL_PUBLIC_MANIFEST.csv",
        "PRIVACY_ACTION_LEDGER.csv",
        "PRIVACY_VALIDATION.json",
    ]
    dual_paths.extend(identity["relative_path"] for identity in controls)
    dual_paths.extend(f"provenance/{relative}" for relative in provenance_paths)
    dual_paths = sorted(set(dual_paths))
    dual_manifest = csv_bytes(
        (
            "relative_path",
            "bytes",
            "sha256",
            "license",
            "methodology_doi",
            "replication_doi",
        ),
        (
            (
                relative,
                (output / PurePosixPath(relative)).stat().st_size,
                sha256_path(output / PurePosixPath(relative)),
                "CC0-1.0",
                METHODOLOGY_DOI,
                REPLICATION_DOI,
            )
            for relative in dual_paths
        ),
    )
    write_bytes(output / "DUAL_DOI_PROVENANCE_MANIFEST.csv", dual_manifest)
    dual_members: list[tuple[str, Path | bytes]] = [
        (relative, output / PurePosixPath(relative)) for relative in dual_paths
    ]
    dual_members.append(("DUAL_DOI_PROVENANCE_MANIFEST.csv", dual_manifest))
    dual_dir = output / "dual_doi"
    dual_dir.mkdir()
    dual_path = dual_dir / f"{config.slug}-methodology-replication-provenance.zip"
    dual_receipt = write_zip(dual_path, dual_members, zipfile.ZIP_DEFLATED)

    validation = {
        "schema": "fac_ega_live_custody_public_snapshot_v1",
        "corpus": config.key,
        "capture": {
            "start": CAPTURE_START,
            "end": CAPTURE_END,
            "mode": CAPTURE_MODE,
            "components": CAPTURE_COMPONENTS,
            "atomic_snapshot_claimed": False,
        },
        "captured_tree": {
            "files": len(entries),
            "bytes": sum(entry.bytes for entry in entries),
            "original_manifest_bytes": len(tree_manifest(entries)),
            "original_manifest_sha256": tree_identity(entries),
        },
        "generation_analysis": analysis,
        "public_projection": {
            "files": sum(entry.public_bytes is not None for entry in projected),
            "bytes": sum(entry.public_bytes or 0 for entry in projected),
            "rights_withheld_files": sum(entry.public_bytes is None for entry in projected),
            "rights_withheld_bytes": sum(
                entry.original.bytes for entry in projected if entry.public_bytes is None
            ),
            "parts": part_receipts,
        },
        "privacy": privacy_validation,
        "controls": controls,
        "dual_doi": {
            "methodology_doi": METHODOLOGY_DOI,
            "replication_doi": REPLICATION_DOI,
            "manifest_bytes": len(dual_manifest),
            "manifest_sha256": sha256_bytes(dual_manifest),
            "archive": dual_receipt,
            "publication_claimed": False,
        },
        "producer_source_mutated": False,
        "completion_or_qa_certification_inferred": False,
        "errors": [],
        "status": "PASS_EXACT_CUSTODY_AND_DERIVED_PUBLIC_PROJECTION",
    }
    write_bytes(output / "SNAPSHOT_VALIDATION.json", json_bytes(validation))

    standalone_errors: list[str] = []
    for path in sorted(output.rglob("*")):
        if not path.is_file() or path.suffix.casefold() == ".zip":
            continue
        relative = path.relative_to(output).as_posix()
        decoded = decode_text(path.read_bytes(), relative)
        if decoded is not None:
            residual = residual_text_findings(decoded[0])
            if residual:
                standalone_errors.append(f"{relative}: {residual}")
    if standalone_errors:
        raise RuntimeError("generated public surface privacy failure: " + " | ".join(standalone_errors[:10]))

    sums = []
    for path in sorted(output.rglob("*"), key=lambda item: item.relative_to(output).as_posix()):
        if path.is_file() and path.name != "SHA256SUMS.csv":
            sums.append(
                (
                    path.relative_to(output).as_posix(),
                    path.stat().st_size,
                    sha256_path(path),
                )
            )
    write_bytes(output / "SHA256SUMS.csv", csv_bytes(("path", "bytes", "sha256"), sums))
    validation["outer_manifest"] = {
        "relative_path": "SHA256SUMS.csv",
        "rows": len(sums),
        "bytes": (output / "SHA256SUMS.csv").stat().st_size,
        "sha256": sha256_path(output / "SHA256SUMS.csv"),
    }
    return validation


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fac-root", type=Path, required=True)
    parser.add_argument("--ega-root", type=Path, required=True)
    parser.add_argument("--ega-canon-root", type=Path, required=True)
    parser.add_argument("--control-root", type=Path, required=True)
    parser.add_argument("--private-custody-root", type=Path, required=True)
    parser.add_argument("--pdftotext", type=Path)
    parser.add_argument("--replace-output", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    pdftotext = args.pdftotext or (Path(found) if (found := shutil.which("pdftotext")) else None)
    if pdftotext is None or not pdftotext.is_file():
        raise RuntimeError("pdftotext is required for extracted-PDF privacy scanning")

    private_root = args.private_custody_root.resolve()
    private_root.mkdir(parents=True, exist_ok=True)
    control_root = args.control_root.resolve()
    sources = {
        "fac": args.fac_root.resolve(),
        "ega": args.ega_root.resolve(),
        "ega_canon": args.ega_canon_root.resolve(),
    }

    for source in sources.values():
        if is_within(source, REPO_ROOT) or is_within(REPO_ROOT, source):
            raise RuntimeError("source roots and repository must be disjoint")
        if is_within(private_root, source):
            raise RuntimeError("private custody output must not be inside a source root")

    summaries: dict[str, object] = {}
    with tempfile.TemporaryDirectory(prefix="fac-ega-snapshot-", dir=private_root) as temporary:
        temp_root = Path(temporary)
        for config in (FAC_CONFIG, EGA_CONFIG):
            stage = temp_root / f"{config.key}-stable-original"
            if config.key == "fac":
                entries = stable_copy(sources["fac"], stage)
            else:
                stage.mkdir()
                stable_copy(sources["ega"], stage / "successor")
                stable_copy(sources["ega_canon"], stage / "french_canon")
                entries = scan_tree(stage)
            actual_files = len(entries)
            actual_bytes = sum(entry.bytes for entry in entries)
            if actual_files != config.expected_files or actual_bytes != config.expected_bytes:
                raise RuntimeError(
                    f"{config.key} frozen-root boundary changed: "
                    f"{actual_files} files/{actual_bytes} bytes"
                )
            private_output, private_validation = build_private_custody(
                config, stage, entries, private_root, args.replace_output
            )
            public_validation = build_public_projection(
                config,
                stage,
                entries,
                control_root,
                pdftotext,
                args.replace_output,
                temp_root,
            )
            summaries[config.key] = {
                "private_output": str(private_output),
                "public_output": str(config.output_root),
                "private_validation": private_validation,
                "public_validation": public_validation,
            }

    print(json.dumps(summaries, indent=2, ensure_ascii=True, sort_keys=True))


if __name__ == "__main__":
    main()

from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
TRANCHE = HERE.parents[1]
SOURCE_DIR = TRANCHE / "source"
TARGET_DIR = TRANCHE / "ko"
JSONL = HERE / "PRODUCER_STRUCTURAL_INDEX.jsonl"
CSV = HERE / "PRODUCER_STRUCTURAL_INDEX.csv"
REPORT = HERE / "PRODUCER_STRUCTURAL_INDEX_VALIDATION_REPORT.json"

AUTHORITY_PATH = Path(
    r"C:\Users\Floris\Documents\Codex\2026-06-01\we-are-currently-doing-a-massive"
    r"\Noether_P07_CurrentHead_SourceAdjudication_20260722\1\01_current"
    r"\Noether_P16_IndependentSecondPass_20260722_cum_de.tex"
)
AUTHORITY_SHA256 = "443EF950D7D45DC6D9E44A9B87501620C10DA873E50E5F2B253ECCAE6A946D27"
P32_INTERVAL_SHA256 = "1E1C2E6AA32B606EAB5B57737F60CE7CF649610B490098511C29498BE8CC7611"
WORK_ID = "noether.paper32.ko.translation_producer"
TOUCHED_AT = "2026-07-22"

PRODUCTION_DECISIONS = {
    1: "CJK-KO-P32-001",
    2: "CJK-KO-P32-003",
    3: "CJK-KO-P32-005",
    4: "CJK-KO-P32-007",
    5: "CJK-KO-P32-009",
    6: "CJK-KO-P32-011",
    7: "CJK-KO-P32-013",
    8: "CJK-KO-P32-015",
    9: "CJK-KO-P32-017",
    10: "CJK-KO-P32-019",
    11: "CJK-KO-P32-021",
    12: "CJK-KO-P32-023",
    13: "CJK-KO-P32-025",
    14: "CJK-KO-P32-026",
    15: "CJK-KO-P32-027",
    16: "CJK-KO-P32-028",
    17: "CJK-KO-P32-030",
    18: "CJK-KO-P32-031",
    19: "CJK-KO-P32-032",
}

TYPE_CODE = {
    "section": "SECTION",
    "paragraph": "PARA",
    "closed_prose_unit": "PROSE",
    "equation_display": "DISPLAY",
    "note": "NOTE",
    "bibliography_item": "BIB",
    "other": "OTHER",
}

REQUIRED = {
    "schema_version",
    "structural_id",
    "work_id",
    "unit_type",
    "title",
    "parent_id",
    "order",
    "authority",
    "targets",
    "relations",
    "completion_state",
    "review_state",
    "publication_state",
    "continuation_cursor",
    "boundary_confidence",
    "ambiguity",
    "decision_ids",
    "touched_at",
    "supersedes",
}
AUTH_REQUIRED = {"path", "locator", "sha256", "fragment_sha256", "language", "hash_basis"}
TARGET_EXTRA = {"match_method", "confidence", "ambiguity"}
LOCATOR_REQUIRED = {
    "description",
    "global_line_start",
    "global_line_end",
    "local_line_start",
    "local_line_end",
    "char_start",
    "char_end",
}
SHA_RE = re.compile(r"^[0-9A-F]{64}$")


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha_file(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def normalized_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def source_range(path: Path) -> tuple[int, int]:
    match = re.search(r"_lines?(\d+)(?:_(\d+))?_translation_input", path.name)
    if not match:
        raise ValueError(f"cannot parse authority range from {path.name}")
    start = int(match.group(1))
    end = int(match.group(2) or start)
    return start, end


def unit_number(path: Path) -> int:
    match = re.search(r"_U(\d{2})_", path.name)
    if not match:
        raise ValueError(f"cannot parse unit number from {path.name}")
    return int(match.group(1))


def line_number_at(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def line_end_offset(text: str, line_end_exclusive: int) -> int:
    while line_end_exclusive > 0 and text[line_end_exclusive - 1] in "\r\n":
        line_end_exclusive -= 1
    return line_end_exclusive


def body_line_bounds(lines: list[str], is_target: bool) -> tuple[int, int]:
    if not is_target:
        return 0, len(lines)
    start = 0
    end = len(lines)
    for index, line in enumerate(lines):
        if "\\begin{document}" in line:
            start = index + 1
            break
    for index in range(start, len(lines)):
        if "\\end{document}" in lines[index]:
            end = index
            break
    return start, end


def balanced_group(text: str, opening: int) -> int | None:
    if opening >= len(text) or text[opening] != "{":
        return None
    depth = 0
    escaped = False
    for index in range(opening, len(text)):
        char = text[index]
        if escaped:
            escaped = False
            continue
        if char == "\\":
            escaped = True
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return index
    return None


def note_spans(text: str, body_start: int, body_end: int) -> list[dict]:
    notes: list[dict] = []
    for match in re.finditer(r"\\footnote\{", text[body_start:body_end]):
        command_start = body_start + match.start()
        brace = body_start + match.end() - 1
        close = balanced_group(text, brace)
        if close is None or close >= body_end:
            continue
        content = text[brace + 1:close]
        kind = (
            "bibliography_item"
            if re.search(r"\b(Math\.|S\.|Vol\.|Bd\.|Berlin|Crelle|Transact|Papers|§)\b", content)
            else "note"
        )
        notes.append(
            {
                "type": kind,
                "start": command_start,
                "end": close + 1,
                "text": text[command_start:close + 1],
                "note_content_start": brace + 1,
                "note_content_end": close,
            }
        )
    return notes


def extract_components(path: Path, is_target: bool) -> list[dict]:
    text = normalized_text(path)
    lines = text.splitlines(keepends=True)
    offsets = []
    cursor = 0
    for line in lines:
        offsets.append(cursor)
        cursor += len(line)
    start_index, end_index = body_line_bounds(lines, is_target)
    body_start = offsets[start_index] if start_index < len(offsets) else len(text)
    body_end = offsets[end_index] if end_index < len(offsets) else len(text)
    notes = note_spans(text, body_start, body_end)
    components: list[dict] = []
    i = start_index
    while i < end_index:
        stripped = lines[i].strip()
        if not stripped:
            i += 1
            continue
        start = offsets[i]
        if stripped.startswith("\\section") or stripped.startswith("\\subsection"):
            end = line_end_offset(text, offsets[i] + len(lines[i]))
            components.append({"type": "section", "start": start, "end": end, "text": text[start:end]})
            i += 1
            continue
        if stripped == r"\begin{center}":
            j = i + 1
            while j < end_index and lines[j].strip() != r"\end{center}":
                j += 1
            if j < end_index:
                j += 1
            end = line_end_offset(text, offsets[j] if j < len(offsets) else len(text))
            components.append({"type": "section", "start": start, "end": end, "text": text[start:end]})
            i = j
            continue
        if stripped == r"\[":
            j = i + 1
            while j < end_index and lines[j].strip() != r"\]":
                j += 1
            if j < end_index:
                j += 1
            end = line_end_offset(text, offsets[j] if j < len(offsets) else len(text))
            components.append({"type": "equation_display", "start": start, "end": end, "text": text[start:end]})
            i = j
            continue
        j = i + 1
        while j < end_index:
            probe = lines[j].strip()
            if not probe or probe in {r"\[", r"\begin{center}"} or probe.startswith("\\section") or probe.startswith("\\subsection"):
                break
            j += 1
        end = line_end_offset(text, offsets[j] if j < len(offsets) else len(text))
        components.append({"type": "paragraph", "start": start, "end": end, "text": text[start:end]})
        i = j

    components.extend(notes)
    components.sort(key=lambda item: (item["start"], 0 if item["type"] == "section" else 1))
    for component in components:
        component["line_start"] = line_number_at(text, component["start"])
        component["line_end"] = line_number_at(text, max(component["start"], component["end"] - 1))
        component["fragment_sha256"] = sha_bytes(component["text"].encode("utf-8"))
    return components


def locator(
    description: str,
    global_start: int | None,
    global_end: int | None,
    local_start: int | None,
    local_end: int | None,
    char_start: int | None,
    char_end: int | None,
) -> dict:
    return {
        "description": description,
        "global_line_start": global_start,
        "global_line_end": global_end,
        "local_line_start": local_start,
        "local_line_end": local_end,
        "char_start": char_start,
        "char_end": char_end,
    }


def authority_side(
    path: Path,
    loc: dict,
    file_sha: str,
    fragment_sha: str,
    language: str,
    basis: str = "computed",
) -> dict:
    return {
        "path": str(path),
        "locator": loc,
        "sha256": file_sha,
        "fragment_sha256": fragment_sha,
        "language": language,
        "hash_basis": basis,
    }


def target_side(side: dict, method: str, confidence: str, ambiguity: str | None) -> dict:
    return {**side, "match_method": method, "confidence": confidence, "ambiguity": ambiguity}


def clean_title(text: str) -> str:
    cleaned = re.sub(r"\s+", " ", text).strip()
    return cleaned[:180] if cleaned else "structural unit"


def next_cursor(unit: int, ranges: list[tuple[int, int]]) -> str:
    if unit < len(ranges):
        return f"next routed source line {ranges[unit][0]} (P32-KO-U{unit + 1:02d})"
    return "routed substantive P32 prose exhausted; await next explicit Korean Noether route"


def build_records() -> list[dict]:
    sources = sorted(SOURCE_DIR.glob("P32_RoutedAuthority_*_translation_input.tex"), key=lambda p: source_range(p)[0])
    targets = sorted(TARGET_DIR.glob("Noether_Paper32_Korean_U*_translation_draft_v001.tex"), key=unit_number)
    if len(sources) != 19 or len(targets) != 19:
        raise ValueError(f"expected 19 source and 19 target files, found {len(sources)} and {len(targets)}")
    ranges = [source_range(path) for path in sources]
    records: list[dict] = []
    root_targets = []
    for target in targets:
        text = normalized_text(target)
        root_targets.append(
            target_side(
                authority_side(
                    target,
                    locator("complete editable Korean draft TeX unit", None, None, 1, len(text.splitlines()), 0, len(text)),
                    sha_file(target),
                    sha_bytes(text.encode("utf-8")),
                    "ko-KR",
                ),
                "routed unit membership",
                "high",
                "translation producer membership only; no review claim",
            )
        )
    records.append(
        {
            "schema_version": "1.0.0",
            "structural_id": "NOE-P32-KO-WORK",
            "work_id": WORK_ID,
            "unit_type": "work",
            "title": "Noether Paper 32 Korean translation-producer draft set",
            "parent_id": None,
            "order": 0,
            "authority": authority_side(
                AUTHORITY_PATH,
                locator(
                    "manager-routed P32 interval; routing metadata not audited by this translation lane",
                    16011,
                    16179,
                    None,
                    None,
                    None,
                    None,
                ),
                AUTHORITY_SHA256,
                P32_INTERVAL_SHA256,
                "de",
                "manager_supplied_unchecked",
            ),
            "targets": root_targets,
            "relations": [],
            "completion_state": "draft_text_coverage",
            "review_state": "unreviewed",
            "publication_state": "private_working",
            "continuation_cursor": "await next explicit non-overlapping Korean Noether translation route",
            "boundary_confidence": "high",
            "ambiguity": "U01-U19 cover routed substantive prose only; TeX control matter is not translated and no checker parity is claimed",
            "decision_ids": ["CJK-KO-P32-001", "CJK-KO-P32-033", "CJK-KO-P32-035"],
            "touched_at": TOUCHED_AT,
            "supersedes": [],
        }
    )

    global_order = 1
    for unit, (source, target, (global_start, global_end)) in enumerate(zip(sources, targets, ranges), 1):
        unit_id = f"NOE-P32-KO-U{unit:02d}"
        source_text = normalized_text(source)
        target_text = normalized_text(target)
        cursor = next_cursor(unit, ranges)
        decision = PRODUCTION_DECISIONS[unit]
        records.append(
            {
                "schema_version": "1.0.0",
                "structural_id": unit_id,
                "work_id": WORK_ID,
                "unit_type": "translation_unit",
                "title": f"P32 Korean translation draft U{unit:02d}, authority lines {global_start}-{global_end}",
                "parent_id": "NOE-P32-KO-WORK",
                "order": unit,
                "authority": authority_side(
                    source,
                    locator(
                        f"complete routed source slice for U{unit:02d}",
                        global_start,
                        global_end,
                        1,
                        len(source_text.splitlines()),
                        0,
                        len(source_text),
                    ),
                    sha_file(source),
                    sha_bytes(source_text.encode("utf-8")),
                    "de",
                ),
                "targets": [
                    target_side(
                        authority_side(
                            target,
                            locator(
                                f"complete editable Korean draft U{unit:02d}",
                                None,
                                None,
                                1,
                                len(target_text.splitlines()),
                                0,
                                len(target_text),
                            ),
                            sha_file(target),
                            sha_bytes(target_text.encode("utf-8")),
                            "ko-KR",
                        ),
                        "explicit routed unit pair",
                        "high",
                        "translation pair only; Korean/source parity remains unchecked",
                    )
                ],
                "relations": [{"type": "contained_by", "target_id": "NOE-P32-KO-WORK"}],
                "completion_state": "translated_draft",
                "review_state": "unreviewed",
                "publication_state": "private_working",
                "continuation_cursor": cursor,
                "boundary_confidence": "high",
                "ambiguity": "closed translation unit boundary is manager-routed; semantic parity remains unchecked",
                "decision_ids": [decision],
                "touched_at": TOUCHED_AT,
                "supersedes": [],
            }
        )

        source_components = extract_components(source, False)
        target_components = extract_components(target, True)
        source_by_type = Counter()
        target_by_type: dict[str, list[dict]] = {}
        for component in target_components:
            target_by_type.setdefault(component["type"], []).append(component)
        matched_target_keys: set[tuple[str, int]] = set()

        for local_order, component in enumerate(source_components, 1):
            kind = component["type"]
            source_by_type[kind] += 1
            ordinal = source_by_type[kind]
            code = TYPE_CODE[kind]
            sid = f"{unit_id}-{code}-{ordinal:03d}"
            target_candidates = target_by_type.get(kind, [])
            targets_for_record = []
            ambiguity = None
            confidence = "medium"
            if ordinal <= len(target_candidates):
                matched = target_candidates[ordinal - 1]
                matched_target_keys.add((kind, ordinal))
                targets_for_record.append(
                    target_side(
                        authority_side(
                            target,
                            locator(
                                f"machine-aligned {kind} ordinal {ordinal} in Korean U{unit:02d}",
                                None,
                                None,
                                matched["line_start"],
                                matched["line_end"],
                                matched["start"],
                                matched["end"],
                            ),
                            sha_file(target),
                            matched["fragment_sha256"],
                            "ko-KR",
                        ),
                        "same-type ordinal within explicit routed unit pair",
                        "medium",
                        "machine correspondence only; independent source/Korean checker parity required",
                    )
                )
                ambiguity = "source-target component correspondence is machine-aligned and unreviewed"
            else:
                confidence = "low"
                ambiguity = "no same-type target component; correspondence held for checker"

            parent_id = unit_id
            if kind in {"note", "bibliography_item"}:
                containing = [
                    prior
                    for prior in source_components
                    if prior["type"] == "paragraph"
                    and prior["start"] <= component["start"] < prior["end"]
                ]
                if containing:
                    para_ordinal = [
                        p for p in source_components
                        if p["type"] == "paragraph" and p["start"] <= containing[0]["start"]
                    ]
                    parent_id = f"{unit_id}-PARA-{len(para_ordinal):03d}"
            elif kind == "equation_display":
                containing_note = [
                    note
                    for note in source_components
                    if note["type"] in {"note", "bibliography_item"}
                    and note["start"] <= component["start"] < note["end"]
                ]
                if containing_note:
                    note = containing_note[0]
                    note_kind = note["type"]
                    note_ordinal = [
                        item
                        for item in source_components
                        if item["type"] == note_kind and item["start"] <= note["start"]
                    ]
                    parent_id = f"{unit_id}-{TYPE_CODE[note_kind]}-{len(note_ordinal):03d}"

            records.append(
                {
                    "schema_version": "1.0.0",
                    "structural_id": sid,
                    "work_id": WORK_ID,
                    "unit_type": kind,
                    "title": clean_title(component["text"]),
                    "parent_id": parent_id,
                    "order": local_order,
                    "authority": authority_side(
                        source,
                        locator(
                            f"{kind} {ordinal} within routed U{unit:02d}",
                            global_start + component["line_start"] - 1,
                            global_start + component["line_end"] - 1,
                            component["line_start"],
                            component["line_end"],
                            component["start"],
                            component["end"],
                        ),
                        sha_file(source),
                        component["fragment_sha256"],
                        "de",
                    ),
                    "targets": targets_for_record,
                    "relations": [{"type": "contained_by", "target_id": parent_id}],
                    "completion_state": "translated_draft",
                    "review_state": "unreviewed",
                    "publication_state": "private_working",
                    "continuation_cursor": cursor,
                    "boundary_confidence": confidence,
                    "ambiguity": ambiguity,
                    "decision_ids": [decision],
                    "touched_at": TOUCHED_AT,
                    "supersedes": [],
                }
            )
            global_order += 1

        target_seen = Counter()
        target_only_count = 0
        for component in target_components:
            kind = component["type"]
            target_seen[kind] += 1
            ordinal = target_seen[kind]
            if (kind, ordinal) in matched_target_keys:
                continue
            target_only_count += 1
            sid = f"{unit_id}-OTHER-{target_only_count:03d}"
            records.append(
                {
                    "schema_version": "1.0.0",
                    "structural_id": sid,
                    "work_id": WORK_ID,
                    "unit_type": "other",
                    "title": f"Unmatched Korean {kind}: {clean_title(component['text'])}",
                    "parent_id": unit_id,
                    "order": len(source_components) + target_only_count,
                    "authority": authority_side(
                        source,
                        locator(
                            "unit-level source fallback for unmatched target component",
                            global_start,
                            global_end,
                            1,
                            len(source_text.splitlines()),
                            0,
                            len(source_text),
                        ),
                        sha_file(source),
                        sha_bytes(source_text.encode("utf-8")),
                        "de",
                    ),
                    "targets": [
                        target_side(
                            authority_side(
                                target,
                                locator(
                                    f"target-only {kind} ordinal {ordinal}",
                                    None,
                                    None,
                                    component["line_start"],
                                    component["line_end"],
                                    component["start"],
                                    component["end"],
                                ),
                                sha_file(target),
                                component["fragment_sha256"],
                                "ko-KR",
                            ),
                            "unmatched target component retained",
                            "none",
                            "no same-type source component; checker must adjudicate",
                        )
                    ],
                    "relations": [{"type": "contained_by", "target_id": unit_id}],
                    "completion_state": "held",
                    "review_state": "unreviewed",
                    "publication_state": "private_working",
                    "continuation_cursor": "checker must adjudicate unmatched target component",
                    "boundary_confidence": "low",
                    "ambiguity": "target-only machine extraction retained; no source correspondence claimed",
                    "decision_ids": [decision],
                    "touched_at": TOUCHED_AT,
                    "supersedes": [],
                }
            )
    return records


def validate_side(side: dict, label: str, errors: list[str]) -> None:
    expected = AUTH_REQUIRED | (TARGET_EXTRA if "match_method" in side else set())
    if set(side) != expected:
        errors.append(f"{label}: invalid side fields")
        return
    if set(side["locator"]) != LOCATOR_REQUIRED:
        errors.append(f"{label}: invalid locator fields")
        return
    if not SHA_RE.fullmatch(side["sha256"]) or not SHA_RE.fullmatch(side["fragment_sha256"]):
        errors.append(f"{label}: malformed SHA-256")
        return
    path = Path(side["path"])
    if not path.is_file():
        errors.append(f"{label}: missing path {path}")
        return
    if side["hash_basis"] == "manager_supplied_unchecked":
        return
    if sha_file(path) != side["sha256"]:
        errors.append(f"{label}: file hash mismatch")
        return
    loc = side["locator"]
    if loc["char_start"] is None or loc["char_end"] is None:
        return
    text = normalized_text(path)
    start, end = loc["char_start"], loc["char_end"]
    if not (0 <= start <= end <= len(text)):
        errors.append(f"{label}: invalid character range {start}-{end}")
        return
    if sha_bytes(text[start:end].encode("utf-8")) != side["fragment_sha256"]:
        errors.append(f"{label}: fragment hash mismatch")


def csv_safe(value: object) -> str:
    if value is None:
        return ""
    text = str(value)
    return "'" + text if text.startswith(("=", "+", "-", "@")) else text


def validate(records: list[dict]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    ids = [record.get("structural_id") for record in records]
    known = set(ids)
    if len(ids) != len(known):
        errors.append("duplicate structural IDs")
    sibling_orders = Counter((r.get("parent_id"), r.get("order")) for r in records)
    for key, count in sibling_orders.items():
        if key[0] is not None and count > 1:
            errors.append(f"duplicate sibling order {key}")
    for line, record in enumerate(records, 1):
        if set(record) != REQUIRED:
            errors.append(f"record {line} fields missing={sorted(REQUIRED - set(record))} extra={sorted(set(record) - REQUIRED)}")
            continue
        sid = record["structural_id"]
        if record["parent_id"] is not None and record["parent_id"] not in known:
            errors.append(f"{sid}: unknown parent {record['parent_id']}")
        for relation in record["relations"]:
            if relation["target_id"] not in known:
                errors.append(f"{sid}: unknown relation target {relation['target_id']}")
        validate_side(record["authority"], f"{sid}/authority", errors)
        for index, target in enumerate(record["targets"]):
            validate_side(target, f"{sid}/target/{index}", errors)
            if target["confidence"] != "high":
                warnings.append(f"{sid}: {target['confidence']} target correspondence")
        if not record["decision_ids"] or not record["continuation_cursor"]:
            errors.append(f"{sid}: missing decision IDs or continuation cursor")
    return errors, warnings


def write_projection(records: list[dict]) -> None:
    fields = [
        "structural_id",
        "work_id",
        "unit_type",
        "title",
        "parent_id",
        "order",
        "authority_path",
        "authority_locator",
        "authority_sha256",
        "authority_language",
        "target_count",
        "target_languages",
        "target_paths",
        "target_locators",
        "completion_state",
        "review_state",
        "publication_state",
        "continuation_cursor",
        "boundary_confidence",
        "ambiguity",
        "decision_ids",
    ]
    with CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for record in records:
            targets = record["targets"]
            row = {
                "structural_id": record["structural_id"],
                "work_id": record["work_id"],
                "unit_type": record["unit_type"],
                "title": record["title"],
                "parent_id": record["parent_id"],
                "order": record["order"],
                "authority_path": record["authority"]["path"],
                "authority_locator": json.dumps(record["authority"]["locator"], ensure_ascii=False, separators=(",", ":")),
                "authority_sha256": record["authority"]["sha256"],
                "authority_language": record["authority"]["language"],
                "target_count": len(targets),
                "target_languages": "|".join(target["language"] for target in targets),
                "target_paths": "|".join(target["path"] for target in targets),
                "target_locators": "|".join(json.dumps(target["locator"], ensure_ascii=False, separators=(",", ":")) for target in targets),
                "completion_state": record["completion_state"],
                "review_state": record["review_state"],
                "publication_state": record["publication_state"],
                "continuation_cursor": record["continuation_cursor"],
                "boundary_confidence": record["boundary_confidence"],
                "ambiguity": record["ambiguity"],
                "decision_ids": "|".join(record["decision_ids"]),
            }
            writer.writerow({key: csv_safe(value) for key, value in row.items()})


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    try:
        records = build_records()
    except Exception as exc:
        records = []
        errors.append(f"build failure: {exc}")
    if records:
        built_errors, built_warnings = validate(records)
        errors.extend(built_errors)
        warnings.extend(built_warnings)
        JSONL.write_text(
            "".join(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n" for record in records),
            encoding="utf-8",
        )
        write_projection(records)
        with CSV.open(encoding="utf-8", newline="") as handle:
            csv_rows = list(csv.DictReader(handle))
        if [row["structural_id"] for row in csv_rows] != [record["structural_id"] for record in records]:
            errors.append("CSV projection ID/order mismatch")
    type_counts = Counter(record["unit_type"] for record in records)
    report = {
        "schema_version": "1.0.0",
        "record_count": len(records),
        "type_counts": dict(sorted(type_counts.items())),
        "latest_structural_id": records[-1]["structural_id"] if records else None,
        "errors": errors,
        "warnings": warnings,
        "status": "pass" if not errors else "fail",
        "known_limit": "component correspondence is machine same-type ordinal within explicit unit pairs; all Korean/source parity and semantics remain independently unchecked",
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

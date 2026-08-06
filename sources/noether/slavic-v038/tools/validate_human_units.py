#!/usr/bin/env python3
"""Validate structure and bounded language invariants for 31 translated units."""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path

import draft_translations as legacy


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "authority_units"
TARGET = ROOT / "translations" / "human_edited"
OUTPUT = ROOT / "evidence" / "human_unit_validation.json"
TARGETS = ("ru", "uk", "isv")

GERMAN_EXTENDED_RE = re.compile(
    r"\b(?:der|die|das|den|dem|des|ein|eine|einer|eines|einem|einen|und|oder|aber|"
    r"ist|sind|war|wird|werden|wenn|dann|durch|nach|nicht|auch|wir|man|welche|welcher|"
    r"welches|mit|für|von|zum|zur|nur|alle|aus|folgt|wegen|moduleigenschaft|"
    r"assoziativgesetzes|homomorphismenprodukt|gruppenprodukt|invariantengruppe|"
    r"invariantenbereich|seite|speziell|genauer|kurz|falls|zugehöriges|kleines|"
    r"faktorensystem|also|rang|hauptgeschlecht|geschlechtergruppe|minimalen|gruppe|"
    r"hilfssatz|sei|dargestellt)\b|w\.\s*z\.\s*b\.\s*w\.",
    re.IGNORECASE,
)
ISV_LANE_ADVERSE_RE = re.compile(
    r"\b(?:če|splošn\w*|poljubn\w*|takole|pridruž\w*|seštevanj\w*|množic\w*|"
    r"vsakemu|ki|sootvětstv\w*|sootvětn(?:y|ym|ymi|yh|ogo|omu|a|e)|"
    r"(?:pod)?gruppe|odpovědajuć\w*)\b",
    re.IGNORECASE,
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def prose_projection(text: str) -> str:
    protected, _values = legacy.protect(text)
    return re.sub(r"@@TEX\d{5}@@", " ", protected)


def mask_translatable_math_text(text: str) -> str:
    """Mask prose in balanced ``\\text{...}`` arguments, retaining nested math.

    Natural-language payloads in displays must be translated, while every
    surrounding mathematical byte remains fixed.  A whole-display protector
    would otherwise mistake the required prose translation for formula drift.
    Numeric markers such as ``\\text{(1)}`` remain exact.
    """

    marker = r"\text{"
    cursor = 0
    chunks: list[str] = []
    while True:
        start = text.find(marker, cursor)
        if start < 0:
            chunks.append(text[cursor:])
            break
        chunks.append(text[cursor:start])
        content_start = start + len(marker)
        depth = 1
        pos = content_start
        escaped = False
        while pos < len(text) and depth:
            char = text[pos]
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
            pos += 1
        if depth:
            # The brace validator will report this separately; retain the tail.
            chunks.append(text[start:])
            break
        content = text[content_start : pos - 1]
        if not content.strip() or re.search(r"[A-Za-zÀ-žА-Яа-яІіЇїЄєҐґЈј]", content):
            nested_math = re.findall(r"\\\(.*?\\\)", content, flags=re.DOTALL)
            chunks.append(r"\text{@@LANGTEXT@@" + "".join(nested_math) + "}")
        else:
            chunks.append(text[start:pos])
        cursor = pos
    return "".join(chunks)


def scan_projection(text: str) -> str:
    """Retain translated display prose while removing opaque control payloads."""

    current = re.sub(r"(?m)^%.*$", " ", text)
    current = re.sub(
        r"\\(?:label|ref|eqref|pageref|cite|url|href|srcfn|foreign)\{[^{}]*\}",
        " ",
        current,
    )
    return current


def paragraph_structures(text: str) -> list[list[str]]:
    paragraphs = re.split(r"\r?\n\s*\r?\n", text.strip())
    return [legacy.protect(mask_translatable_math_text(paragraph))[1] for paragraph in paragraphs]


def validate_unit(target: str, unit: str) -> dict:
    source_path = SOURCE / f"{unit}.texfrag"
    target_path = TARGET / target / f"{unit}.texfrag"
    source_text = source_path.read_text(encoding="utf-8-sig")
    target_text = target_path.read_text(encoding="utf-8-sig")
    source_structure = legacy.protect(mask_translatable_math_text(source_text))[1]
    target_structure = legacy.protect(mask_translatable_math_text(target_text))[1]
    source_paragraph_structures = paragraph_structures(source_text)
    target_paragraph_structures = paragraph_structures(target_text)
    errors: list[str] = []
    warnings: list[str] = []
    if len(source_paragraph_structures) != len(target_paragraph_structures):
        errors.append(
            f"paragraph count mismatch: {len(source_paragraph_structures)} versus {len(target_paragraph_structures)}"
        )
    else:
        mismatched_paragraphs = []
        for index, (source_tokens, target_tokens) in enumerate(
            zip(source_paragraph_structures, target_paragraph_structures), start=1
        ):
            source_counter = Counter(source_tokens)
            target_counter = Counter(target_tokens)
            if source_counter != target_counter:
                mismatched_paragraphs.append(
                    {
                        "paragraph_one_based": index,
                        "missing": dict(source_counter - target_counter),
                        "added": dict(target_counter - source_counter),
                    }
                )
        if mismatched_paragraphs:
            errors.append(
                f"TeX/math occurrence multiset mismatch in {len(mismatched_paragraphs)} paragraph(s): "
                + json.dumps(mismatched_paragraphs[:5], ensure_ascii=False)
            )
    # Ordered equality is intentionally advisory: idiomatic Slavic grammar can
    # move an inline mathematical noun before/after its apposition.  Exact
    # occurrences remain mandatory within the same aligned paragraph.
    if source_structure != target_structure and Counter(source_structure) == Counter(target_structure):
        warnings.append("TeX/math occurrences preserved but reordered within translated prose")
    balance = legacy.brace_balance(target_text)
    if balance != 0:
        errors.append(f"brace balance {balance}")
    projection = prose_projection(target_text)
    scan_text = scan_projection(target_text)
    german = sorted(
        set(match.group(0) for match in GERMAN_EXTENDED_RE.finditer(scan_text)),
        key=str.casefold,
    )
    if target == "isv":
        # ``rang`` is both the authority's German noun and the lane's established
        # standard Interslavic mathematical term; it is not a residual by itself.
        german = [item for item in german if item.casefold() != "rang"]
    if german:
        warnings.append(f"possible German residuals: {german}")
    if target == "ru":
        bad = sorted(set(re.findall(r"[іїєґІЇЄҐ]", projection)))
        if bad:
            errors.append(f"Ukrainian-only letters in Russian prose: {bad}")
    elif target == "uk":
        bad = sorted(set(re.findall(r"[ыэъёЫЭЪЁ]", projection)))
        if bad:
            errors.append(f"Russian-only letters in Ukrainian prose: {bad}")
    elif target == "isv":
        cyrillic = sorted(set(re.findall(r"[А-Яа-яЁёІіЇїЄєҐґЈј]", projection)))
        if cyrillic:
            errors.append(f"Cyrillic characters in Latin Interslavic prose: {cyrillic}")
        adverse = sorted(set(match.group(0) for match in ISV_LANE_ADVERSE_RE.finditer(projection)))
        if adverse:
            warnings.append(f"adverse normalization forms: {adverse}")
        non_lane = sorted(set(re.findall(r"[řůłąâôŘŮŁĄÂÔ]", projection)))
        if non_lane:
            errors.append(f"non-lane Czech/Polish letters: {non_lane}")
    source_paragraphs = len(source_paragraph_structures)
    target_paragraphs = len(target_paragraph_structures)
    return {
        "unit_id": unit,
        "target": target,
        "source": {
            "path": source_path.resolve().as_posix(),
            "bytes": source_path.stat().st_size,
            "sha256": sha256(source_path.read_bytes()),
        },
        "translation": {
            "path": target_path.resolve().as_posix(),
            "bytes": target_path.stat().st_size,
            "sha256": sha256(target_path.read_bytes()),
        },
        "source_structure_token_count": len(source_structure),
        "target_structure_token_count": len(target_structure),
        "source_paragraph_boundaries": source_paragraphs,
        "target_paragraph_boundaries": target_paragraphs,
        "errors": errors,
        "warnings": warnings,
        "pass": not errors,
    }


def main() -> int:
    missing = []
    for target in TARGETS:
        for section in range(1, 32):
            path = TARGET / target / f"BOOK_S{section:02d}.texfrag"
            if not path.exists():
                missing.append(path.as_posix())
    if missing:
        raise SystemExit(f"missing {len(missing)} target units; first={missing[0]}")
    records = [
        validate_unit(target, f"BOOK_S{section:02d}")
        for target in TARGETS
        for section in range(1, 32)
    ]
    summary = {
        target: {
            "units": sum(record["target"] == target for record in records),
            "pass": sum(record["target"] == target and record["pass"] for record in records),
            "error_count": sum(
                len(record["errors"]) for record in records if record["target"] == target
            ),
            "warning_count": sum(
                len(record["warnings"]) for record in records if record["target"] == target
            ),
        }
        for target in TARGETS
    }
    document = {
        "schema": "noether-slavic-v038-human-unit-validation/1.0",
        "generated_at": datetime.now().astimezone().isoformat(),
        "authority": {
            "pointer_id": "NOETH-DE-AUTH-v038-20260805",
            "id": "NOETH-DE-ED-0005",
            "sha256": "1A44F967B29972E8F99E5C323A479162AD82A23FC457395915A4BB9DDF51AD41",
            "post_p43_identity_sha256": "662BBFC0926381E0D45A2356BF19959FCAEE6282F6F049E85B0BD5D553E80B58",
        },
        "scope": "BOOK_S01--BOOK_S31, Russian/Ukrainian/Interslavic Latin",
        "summary": summary,
        "records": records,
    }
    OUTPUT.write_text(json.dumps(document, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    all_pass = all(record["pass"] for record in records)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    print(f"{'PASS' if all_pass else 'FAIL'} output={OUTPUT} sha256={sha256(OUTPUT.read_bytes())}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())

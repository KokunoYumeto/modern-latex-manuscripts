#!/usr/bin/env python3
"""Deterministic reference runner for the bundled conformance fixtures."""

from __future__ import annotations

import sys

sys.dont_write_bytecode = True
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", newline="\n")

import json
import unicodedata
from pathlib import Path

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parent


def load(name: str) -> object:
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def delimiter_scan(text: str) -> dict[str, int]:
    linebreaks = 0
    openers = 0
    index = 0
    while index < len(text):
        if text[index] != "\\":
            index += 1
            continue
        end = index
        while end < len(text) and text[end] == "\\":
            end += 1
        run = end - index
        if end < len(text) and text[end] == "[":
            linebreaks += run // 2
            openers += run % 2
        index = end
    return {"linebreak_commands": linebreaks, "display_openers": openers}


def braced(text: str, opening: int) -> tuple[str, int]:
    if opening >= len(text) or text[opening] != "{":
        raise ValueError("expected opening brace")
    depth = 1
    index = opening + 1
    while index < len(text) and depth:
        if text[index] == "{" and (index == 0 or text[index - 1] != "\\"):
            depth += 1
        elif text[index] == "}" and (index == 0 or text[index - 1] != "\\"):
            depth -= 1
        index += 1
    if depth:
        raise ValueError("unclosed brace")
    return text[opening + 1:index - 1], index


def prose_segments(text: str, commands: list[str]) -> list[str]:
    command_set = set(commands)
    segments: list[str] = []

    def walk(body: str, admitted: bool) -> None:
        buffer: list[str] = []
        index = 0
        while index < len(body):
            if body[index] == "\\":
                end = index + 1
                while end < len(body) and body[end].isalpha():
                    end += 1
                name = body[index + 1:end]
                if name in command_set and end < len(body) and body[end] == "{":
                    if admitted and buffer:
                        value = "".join(buffer)
                        if value:
                            segments.append(value)
                        buffer = []
                    inner, next_index = braced(body, end)
                    walk(inner, True)
                    index = next_index
                    continue
            if admitted:
                buffer.append(body[index])
            index += 1
        if admitted and buffer:
            value = "".join(buffer)
            if value:
                segments.append(value)

    walk(text, False)
    return segments


def has_final_consonant(pronunciation: str) -> bool:
    if not pronunciation:
        raise ValueError("empty pronunciation")
    code = ord(pronunciation[-1])
    if not 0xAC00 <= code <= 0xD7A3:
        raise ValueError("pronunciation must end in a Hangul syllable")
    return (code - 0xAC00) % 28 != 0


def execute(test: dict[str, object], report_schema: dict[str, object]) -> object:
    operation = test["operation"]
    data = test["input"]
    if operation == "delimiter_scan":
        return delimiter_scan(data["text"])
    if operation == "nested_prose_scan":
        return {
            "locale_prose_segments": prose_segments(data["text"], data["commands"]),
            "math_controls_unchanged": True,
        }
    if operation == "formula_token_compare":
        equal = data["source"] == data["target"]
        return {"result": "pass" if equal else "fail", "changed_feature": data["feature"]}
    if operation == "obligation_balance":
        unexplained = data["target"] - data["source"] - data["declared_repeats"]
        return {"result": "pass" if unexplained == 0 else "fail", "unexplained_delta": unexplained}
    if operation == "cmap_policy":
        if data["existing_to_unicode"]:
            return {"result": "pass", "action": "preserve_existing"}
        if data["subset"] not in data["known_subsets"]:
            return {"result": "fail", "action": "reject_unknown"}
        deterministic = (
            data["first_output_sha256"] is not None
            and data["first_output_sha256"] == data["second_output_sha256"]
        )
        return {
            "result": "pass" if deterministic and data["invariants_equal"] else "fail",
            "action": "inject_missing",
        }
    if operation == "profile_transfer":
        return {"result": "pass" if data["local_evidence"] else "unsupported"}
    if operation == "literal_preserve":
        return {"output": data["text"]}
    if operation == "term_dispatch":
        return {"terms": [data["mapping"][item] for item in data["expressions"]]}
    if operation == "unicode_normalize":
        mathematical = chr(int(data["mathematical_codepoint"][2:], 16))
        decomposed = "".join(chr(int(value[2:], 16)) for value in data["decomposed_codepoints"])
        nfc_mathematical = unicodedata.normalize("NFC", mathematical)
        return {
            "nfc_mathematical_codepoint": f"U+{ord(nfc_mathematical):04X}",
            "nfkc_mathematical": unicodedata.normalize("NFKC", mathematical),
            "nfc_decomposed": unicodedata.normalize("NFC", decomposed),
        }
    if operation == "note_once":
        return {"result": "pass" if data["source_notes"] == data["target_notes"] else "fail"}
    if operation == "state_schema":
        state_schema = {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "$defs": report_schema["$defs"],
            "$ref": "#/$defs/state",
        }
        errors = list(Draft202012Validator(state_schema).iter_errors(data["state"]))
        return {"result": "fail" if errors else "pass"}
    if operation == "korean_particle":
        particle = data["consonant_particle"] if has_final_consonant(data["pronunciation"]) else data["vowel_particle"]
        return {"output": data["math"] + particle}
    raise ValueError(f"unsupported operation: {operation}")


tests = load("tests.json")
tests_schema = load("tests.schema.json")
report_schema = load("report.schema.json")
schema_errors = sorted(
    Draft202012Validator(tests_schema).iter_errors(tests),
    key=lambda item: (list(item.absolute_path), item.message),
)
if schema_errors:
    print(json.dumps({"result": "FAIL", "schema_errors": [error.message for error in schema_errors]}, ensure_ascii=False, indent=2, sort_keys=True))
    raise SystemExit(1)

rows = []
for test in tests["tests"]:
    actual = execute(test, report_schema)
    passed = actual == test["expected"]
    rows.append({"id": test["id"], "passed": passed, "actual": actual})

failed = [row["id"] for row in rows if not row["passed"]]
result = {
    "schema": "cjk-notation-fixture-result-v1",
    "result": "PASS" if not failed else "FAIL",
    "tests_total": len(rows),
    "tests_passed": len(rows) - len(failed),
    "tests_failed": len(failed),
    "failed_ids": failed,
    "tests": rows,
}
print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
raise SystemExit(0 if not failed else 1)

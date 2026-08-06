from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
READER = HERE / "reader.tex"
VENDOR = ROOT / "tmp" / "tools" / "opencc_py"
EXPECTED = "50B212EA04061921607E13CB7B367DEBF4AAF2449CF5614F931E74AA1B5A5338"

sys.path.insert(0, str(VENDOR))
from opencc import OpenCC  # type: ignore  # noqa: E402


raw = READER.read_bytes()
actual = hashlib.sha256(raw).hexdigest().upper()
if len(raw) != 1_811_029 or actual != EXPECTED:
    raise SystemExit("candidate identity mismatch")
lines = raw.decode("utf-8").splitlines()
converter = OpenCC("t2s")
phrase_lines: list[int] = []
character_changes: list[dict[str, object]] = []
seen: set[tuple[str, str, int]] = set()
for number, line in enumerate(lines, 1):
    if number < 340 or line.lstrip().startswith("%"):
        continue
    if converter.convert(line) != line:
        phrase_lines.append(number)
    for char in line:
        code = ord(char)
        if not (0x3400 <= code <= 0x9FFF or 0x20000 <= code <= 0x2FFFF):
            continue
        output = converter.convert(char)
        key = (char, output, number)
        if output != char and key not in seen:
            seen.add(key)
            character_changes.append(
                {"line": number, "original": char, "converted": output}
            )
result = {
    "scan_id": "ZHCHK-CUM-R3-HANS-001",
    "reader_bytes": len(raw),
    "reader_sha256": actual,
    "phrase_changed_lines": phrase_lines,
    "phrase_false_positive": {
        "line": 916,
        "keep": "覆盖",
        "reason": "OpenCC MMSEG crossed the intended 双重|覆盖 word boundary",
    },
    "character_changes": character_changes,
    "mixed_wen_ti": raw.decode("utf-8").count("问題"),
    "traditional_ti": raw.decode("utf-8").count("題"),
    "all_pass": phrase_lines == [916] and not character_changes,
}
if not result["all_pass"]:
    raise SystemExit(json.dumps(result, ensure_ascii=False, indent=2))
print(json.dumps(result, ensure_ascii=False, indent=2))

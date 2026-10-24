"""Chinese script functions: GPT-5.6 Sol, Ultra, 2026-08-12.
Portable module: GPT-6 Astra, Ultra, 2026-10-24.
OpenCC is a separately installed dependency by its original authors.
"""

from opencc import OpenCC

NORMALIZATIONS = [
    ("爲", "為"),
    ("裏", "裡"),
    ("羣", "群"),
    ("衆", "眾"),
    ("纔", "才"),
    ("幷", "並"),
    ("代數無關係統", "代數無關系統"),
    ("超復", "超複"),
    ("一箇", "一個"),
    ("着手", "著手"),
]

def escaped(text: str, index: int) -> bool:
    count = 0
    index -= 1
    while index >= 0 and text[index] == "\\":
        count += 1
        index -= 1
    return count % 2 == 1

def find_close(text: str, start: int, closer: str) -> int:
    index = start
    while index < len(text):
        if text[index] == "%" and not escaped(text, index):
            newline = text.find("\n", index + 1)
            index = len(text) if newline == -1 else newline + 1
            continue
        if text.startswith(closer, index) and not escaped(text, index):
            return index
        index += 1
    return -1

def math_ranges(text: str) -> list[tuple[int, int, str]]:
    ranges: list[tuple[int, int, str]] = []
    index = 0
    while index < len(text):
        if text[index] == "%" and not escaped(text, index):
            newline = text.find("\n", index + 1)
            index = len(text) if newline == -1 else newline + 1
            continue
        kind = opener = closer = ""
        if text.startswith("\\[", index) and not escaped(text, index):
            kind, opener, closer = "display_bracket", "\\[", "\\]"
        elif text.startswith("\\(", index) and not escaped(text, index):
            kind, opener, closer = "inline_paren", "\\(", "\\)"
        elif text.startswith("$$", index) and not escaped(text, index):
            kind, opener, closer = "display_dollar", "$$", "$$"
        elif text[index] == "$" and not escaped(text, index):
            kind, opener, closer = "inline_dollar", "$", "$"
        if not kind:
            index += 1
            continue
        close_at = find_close(text, index + len(opener), closer)
        if close_at < 0:
            raise RuntimeError(f"Unclosed {kind} at character offset {index}")
        end = close_at + len(closer)
        ranges.append((index, end, kind))
        index = end
    return ranges

def convert_outside_math(
    text: str, converter: OpenCC
) -> tuple[str, list[tuple[int, int, str]]]:
    ranges = math_ranges(text)
    parts: list[str] = []
    cursor = 0
    for start, end, _kind in ranges:
        parts.append(converter.convert(text[cursor:start]))
        parts.append(text[start:end])
        cursor = end
    parts.append(converter.convert(text[cursor:]))
    return "".join(parts), ranges

def normalized(text: str) -> tuple[str, dict[str, int]]:
    counts: dict[str, int] = {}
    for old, new in NORMALIZATIONS:
        count = text.count(old)
        counts[f"{old}->{new}"] = count
        text = text.replace(old, new)
    return text, counts

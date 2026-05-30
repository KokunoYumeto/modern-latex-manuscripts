import re
from pathlib import Path

CHUNK = Path(r"local workspace\Documents\local repair pass PLEASE DONT DELETE WINDOWS 32\local repair pass_OUTPUTS\cayley_clean_per_volume\sources_tex_Vol_VII\cayley_vol07_pages_151_200.tex")
FIX = Path(r"local workspace\Documents\local repair pass PLEASE DONT DELETE WINDOWS 32\local repair pass_OUTPUTS\cayley_v2_fixes\sources_tex_Vol_VII\cayley_vol07_paper_445_RETYPE.tex")

chunk = CHUNK.read_text(encoding="utf-8", errors="replace")
fix = FIX.read_text(encoding="utf-8", errors="replace")

fix_match = re.search(r"\\begin\{document\}(.*?)\\end\{document\}", fix, re.S)
if not fix_match:
    raise SystemExit("No begin/end document in fix")
fix_body = fix_match.group(1).strip()

lines = chunk.split("\n")
start = None
end = None
for i, line in enumerate(lines):
    if start is None and re.search(r"%\s*ARTICLE\s+445", line, re.I):
        start = i
    elif start is not None and re.search(r"%\s*ARTICLE\s+44[67]", line, re.I):
        end = i
        break
if start is None:
    raise SystemExit("Couldn't find ARTICLE 445 in chunk")
if end is None:
    end = len(lines)

print(f"Replacing chunk lines {start+1}-{end} with fix body ({len(fix_body)} chars)")

bak = CHUNK.with_suffix(".tex.paper445_bak")
if not bak.exists():
    bak.write_text(chunk, encoding="utf-8")

new_lines = lines[:start] + [
    "% =================================================================",
    "% ARTICLE 445: A MEMOIR ON QUARTIC SURFACES (continued §§60-112)",
    "% SPLICED RETYPE from scan, 2026-05-29, replaces incorrectly reconstructed source system version",
    "% =================================================================",
] + fix_body.split("\n") + [""] + lines[end:]

CHUNK.write_text("\n".join(new_lines), encoding="utf-8")
print(f"Spliced. New line count: {len(new_lines)} (was {len(lines)})")

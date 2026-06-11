"""Unify Cayley's binary-quantic delimiter across all source TeX.

Audit found 5 different made-up substitutes for `)( )( ` (the literal scan glyph
between coefficient list and variable list, as in `(a,b,c,d,e )( x,y)^4`):
  \wr
  \flat\frown
  \widetilde{\phantom{a}}
  \between
  \mid

Canonical form chosen: `\mid` — already widely standard, renders as a vertical
bar in math mode, doesn't require macro definition. All other substitutes will
be replaced with `\mid` in the source TeX. This is reversible if a different
canonical is later preferred.

Run in foreground from local repair pass_OUTPUTS root. Backs up original files to .bak.
"""
import re
from pathlib import Path

ROOT = Path(r"local workspace\Documents\local repair pass PLEASE DONT DELETE WINDOWS 32\local repair pass_OUTPUTS\cayley_clean_per_volume")
patterns = [
    (r"\\wr\b", r"\\mid"),
    (r"\\flat\s*\\frown\b", r"\\mid"),
    (r"\\widetilde\{\\phantom\{a\}\}", r"\\mid"),
    (r"\\between\b", r"\\mid"),
    # Note: \mid is already canonical; no replacement needed for it
]

total_changes = 0
files_changed = 0
detail = []

for vol_dir in sorted(ROOT.glob("sources_tex_*")):
    for tex in sorted(vol_dir.glob("*.tex")):
        try:
            original = tex.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        new = original
        chunk_changes = 0
        for pat, repl in patterns:
            new, n = re.subn(pat, repl, new)
            if n > 0:
                chunk_changes += n
        if chunk_changes > 0:
            # Back up original
            bak = tex.with_suffix(tex.suffix + ".predelim_bak")
            if not bak.exists():
                bak.write_text(original, encoding="utf-8")
            tex.write_text(new, encoding="utf-8")
            files_changed += 1
            total_changes += chunk_changes
            detail.append((vol_dir.name, tex.name, chunk_changes))

print(f"Files changed: {files_changed}")
print(f"Total replacements: {total_changes}")
print()
for vol, name, n in detail:
    print(f"  {vol}/{name}: {n} replacements")

# Audit of ChatGPT batch-0 orthography diff before any codex-lane handoff.
# Checks: TeX command/label/cite contexts, bibliography lines, changed-word inventory,
# minus/plus symmetry, per-mapping correctness on real lines.
import re
import sys
import collections
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
B = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704\user made flr with chat web stuff\batch0_ortho")
d = (B / "NORMALIZATION_BATCH0_ORTHOGRAPHY_PATCH_PROPOSAL_v1.diff").read_text(encoding="utf-8")
lines = d.splitlines()
minus = [l for l in lines if l.startswith("-") and not l.startswith("---")]
plus = [l for l in lines if l.startswith("+") and not l.startswith("+++")]
print("diff lines:", len(lines), "| minus:", len(minus), "| plus:", len(plus))

CMD = re.compile(r"\\(cite|label|ref|bibitem|href|url|texttt|input|include|section\{)")
BIB = re.compile(r"\d{4}|zeitschr|annalen|math\.\s*ann|journal|verlag|akad|nachr|crelle", re.IGNORECASE)
sus_cmd, sus_bib = [], []
for l in minus:
    if CMD.search(l):
        sus_cmd.append(l[:140])
    elif BIB.search(l):
        sus_bib.append(l[:140])
print(f"\nlines with TeX cmd context: {len(sus_cmd)}")
for l in sus_cmd[:8]:
    print("  CMD:", l)
print(f"lines with bib-ish context: {len(sus_bib)}")
for l in sus_bib[:8]:
    print("  BIB:", l)

words = collections.Counter()
pats = [r"[\wÀ-ſ]*ob[šs]č[\wÀ-ſ]*", r"[\wÀ-ſ]*[vV]zet[\wÀ-ſ]*",
        r"[\wÀ-ſ]*dlugost[\wÀ-ſ]*", r"[vV]o?obče[\wÀ-ſ]*"]
for l in minus:
    for p in pats:
        for w in re.findall(p, l):
            words[w.lower()] += 1
print("\nchanged-word inventory (minus side):")
for w, c in words.most_common(40):
    print(f"  {w}: {c}")

# verify each minus/plus pair differs ONLY by the six sanctioned mappings
MAPS = [("vzet", "vzęt"), ("obšč", "obć"), ("dlugost", "dolgost"),
        ("vobče", "obće"), ("voobče", "obće"), ("Vobče", "Obće"), ("Voobče", "Obće")]
bad = 0
for m, p in zip(minus, plus):
    mm = m[1:]
    pp = p[1:]
    x = mm
    for a, b in [("voobče", "obće"), ("Voobče", "Obće"), ("vobče", "obće"), ("Vobče", "Obće"),
                 ("vzet", "vzęt"), ("Vzet", "Vzęt"), ("obšč", "obć"), ("Obšč", "Obć"),
                 ("dlugost", "dolgost"), ("Dlugost", "Dolgost")]:
        x = x.replace(a, b)
    if x != pp:
        bad += 1
        if bad <= 6:
            print("MISMATCH:\n  -", mm[:120], "\n  +", pp[:120], "\n  sim:", x[:120])
print(f"\npairs not explained by the sanctioned mappings: {bad} / {len(minus)}")

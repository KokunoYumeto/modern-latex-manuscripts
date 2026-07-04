# Extract every term decision from INTERSLAVIC_LOGBOOK.md into structured JSON + stats.
# Read-only on the logbook; outputs land in the program folder. CPU-only.
import json
import re
from pathlib import Path
from collections import Counter, defaultdict

SRC = Path(r"C:\Users\Floris\Downloads\codex backup dump 7-4\codex backup\logs\INTERSLAVIC_LOGBOOK.md")
OUT = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")

text = SRC.read_text(encoding="utf-8", errors="replace")
lines = text.splitlines()

# --- walk structure: ## entry headers, ### subsections, term bullets with sub-bullets ---
entries = []          # {header, subsection, term_src, term_dst, notes:[...]}
cur_h2 = ""
cur_h3 = ""
cur_term = None

TERM_RE = re.compile(r"^-\s*`([^`]+)`\s*(?:->|→)\s*`([^`]+)`\s*(.*)$")
TERM_RE2 = re.compile(r"^- \s*`([^`]+)`\s*(?:->|→)\s*(.+)$")  # dst not backticked
SUB_RE = re.compile(r"^\s+- \s*(.*)$")

def flush():
    global cur_term
    if cur_term:
        entries.append(cur_term)
        cur_term = None

for ln in lines:
    if ln.startswith("## "):
        flush(); cur_h2 = ln[3:].strip(); cur_h3 = ""
        continue
    if ln.startswith("### "):
        flush(); cur_h3 = ln[4:].strip()
        continue
    m = TERM_RE.match(ln) or TERM_RE2.match(ln)
    if m:
        flush()
        cur_term = {
            "entry": cur_h2, "section": cur_h3,
            "source_term": m.group(1).strip(),
            "chosen_form": (m.group(2) or "").strip().strip("`"),
            "trailing": (m.group(3).strip() if m.lastindex and m.lastindex >= 3 and m.group(3) else ""),
            "notes": [],
        }
        continue
    if cur_term:
        sm = SUB_RE.match(ln)
        if sm:
            cur_term["notes"].append(sm.group(1).strip())
            continue
        if ln.strip() == "" or ln.startswith("- ") or ln.startswith("|"):
            flush()
flush()

# --- classify each decision ---
REASON_CLASSES = {
    "pan_slavic_native": r"pan-?slav|all slavic|broad(ly)? (slavic|intelligib)|native|transparent to",
    "international": r"international|latinism|classical|matches .*international|greek|latin term",
    "mirrors_east_slavic": r"ukrainian|russian|ряд|mirrors uk|mirrors ru",
    "coinage": r"coinage|coined|neologism",
    "source_fidelity": r"source fidelity|historical term|noether'?s",
    "script_stability": r"script|cyrillic|translit",
    "disambiguation": r"ambigu|disambig|reduce ambiguity|avoids? confusion|clash|collide|false friend",
}
STATUS_CLASSES = {
    "solid": r"solid for pilot|solid\b|stable",
    "needs_review": r"needs? review|reviewer check|review but acceptable|check against|pending",
    "revised": r"revis|replaced|corrected|changed to",
    "rejected": r"reject|avoid|dropped|not used",
}
WITNESS_LANGS = {
    "russian": r"\brussian\b|\bru\b(?![a-z])|русск",
    "ukrainian": r"\bukrainian\b|\buk\b(?![a-z])|україн",
    "polish": r"\bpolish\b|\bpl\b(?![a-z])",
    "czech": r"\bczech\b|\bcs\b(?![a-z])",
    "slovak": r"\bslovak\b",
    "croatian": r"\bcroatian\b|\bhr\b(?![a-z])",
    "serbian": r"\bserbian\b|\bsr\b(?![a-z])",
    "bulgarian": r"\bbulgarian\b|\bbg\b(?![a-z])",
    "slovene": r"\bslovene\b|\bslovenian\b",
    "macedonian": r"\bmacedonian\b",
    "belarusian": r"\bbelarusian\b",
    "ocs_or_interslavic_ref": r"old church slavonic|interslavic dictionary|interslavic reference|medžuslovjansk|steen",
}

def classify(dec):
    blob = " ".join([dec.get("trailing", "")] + dec["notes"]).lower()
    dec["reason_classes"] = [k for k, rx in REASON_CLASSES.items() if re.search(rx, blob)]
    st = [k for k, rx in STATUS_CLASSES.items() if re.search(rx, blob)]
    dec["status_class"] = st[0] if st else "unstated"
    dec["witnesses_cited"] = [k for k, rx in WITNESS_LANGS.items() if re.search(rx, blob)]
    return dec

for d in entries:
    classify(d)

# --- stats ---
stats = {
    "total_term_decisions": len(entries),
    "entries_span": [entries[0]["entry"] if entries else None, entries[-1]["entry"] if entries else None],
    "status_distribution": dict(Counter(d["status_class"] for d in entries)),
    "reason_class_distribution": dict(Counter(rc for d in entries for rc in d["reason_classes"])),
    "witness_citation_counts": dict(Counter(w for d in entries for w in d["witnesses_cited"])),
    "decisions_citing_any_witness": sum(1 for d in entries if d["witnesses_cited"]),
    "east_slavic_only_citations": sum(
        1 for d in entries if d["witnesses_cited"]
        and set(d["witnesses_cited"]) <= {"russian", "ukrainian", "belarusian"}),
    "non_east_slavic_citations": sum(
        1 for d in entries if any(w in d["witnesses_cited"] for w in
        ["polish", "czech", "slovak", "croatian", "serbian", "bulgarian", "slovene", "macedonian"])),
}

# --- false-friend / rejection / policy line harvest (raw grep, for manual curation) ---
harvest = defaultdict(list)
for i, ln in enumerate(lines):
    low = ln.lower()
    if "false friend" in low or "falsefriend" in low:
        harvest["false_friend_lines"].append(f"{i+1}: {ln.strip()}")
    if re.search(r"\breject", low):
        harvest["rejection_lines"].append(f"{i+1}: {ln.strip()}")
    if re.search(r"non-erasure|authority|canon", low):
        harvest["governance_lines"].append(f"{i+1}: {ln.strip()}")
for k in harvest:
    harvest[k] = harvest[k][:120]

out = {
    "artifact": "interslavic_term_decision_extraction",
    "generated": "2026-07-04",
    "source": str(SRC),
    "stats": stats,
    "decisions": entries,
    "harvest": {k: v for k, v in harvest.items()},
}
(OUT / "interslavic_term_decisions_20260704.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

print(json.dumps(stats, indent=1))
print("harvest sizes:", {k: len(v) for k, v in harvest.items()})
print("wrote interslavic_term_decisions_20260704.json")

# v3.1 repair: adopt ChatGPT's v3 master structure; repair contaminated label columns
# (sentence-like cells moved to *_source_cue; clean lemmas restored from concept ledger/v1).
# Emits repaired table + defect report. No wording invented: labels come only from
# ledger-harvested corpus labels; rows without a clean label stay blank.
import csv
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
BASE = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")
DROP = BASE / "user made flr with chat web stuff"

theirs = list(csv.DictReader((DROP / "INTERLINGUAL_MARKER_TABLE_v3_MASTER_20260704.csv").open(encoding="utf-8-sig")))
mine = {r["concept"]: r for r in csv.DictReader((BASE / "INTERLINGUAL_MARKER_TABLE_v1.csv").open(encoding="utf-8-sig"))}
ledger = json.loads((BASE / "INTERLINGUAL_CONCEPT_LEDGER_20260704.json").read_text(encoding="utf-8"))
led_by_en = {c["en"].lower(): c for c in ledger["concepts"]}

LABEL_COLS = ["isv", "isv_cyr", "uk", "ru"]

def sentencey(v):
    v = (v or "").strip()
    return bool(v) and (len(v) > 34 or v.count(" ") >= 3 or any(ch in v for ch in ".;§/") and v.count(" ") >= 2)

moved = {c: 0 for c in LABEL_COLS}
restored = {c: 0 for c in LABEL_COLS}
rows_out = []
for r in theirs:
    r = dict(r)
    concept = r.get("concept", "")
    led = led_by_en.get(concept.lower())
    v1 = mine.get(concept)
    for col in LABEL_COLS:
        val = r.get(col, "")
        if sentencey(val):
            r[f"{col}_source_cue"] = val
            moved[col] += 1
            clean = ""
            if v1 and v1.get(col) and not sentencey(v1[col]):
                clean = v1[col]
            elif led:
                lk = {"isv": "isv", "isv_cyr": "isv_cyr", "uk": "uk", "ru": "ru"}[col]
                vals = led.get(lk) or []
                clean = vals[0] if vals and not sentencey(vals[0]) else ""
            r[col] = clean
            if clean:
                restored[col] += 1
        else:
            r.setdefault(f"{col}_source_cue", "")
    rows_out.append(r)

cols = list(rows_out[0].keys())
with (BASE / "INTERLINGUAL_MARKER_TABLE_v3_1_REPAIRED_20260704.csv").open("w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=cols)
    w.writeheader()
    for r in rows_out:
        w.writerow(r)
(BASE / "INTERLINGUAL_MARKER_TABLE_v3_1_REPAIRED_20260704.json").write_text(json.dumps({
    "artifact": "interlingual_marker_table_v3_1_repaired",
    "generated": "2026-07-04",
    "base": "ChatGPT v3 master (212 concepts, priority bands, source weights) — ADOPTED as master structure",
    "repair": "sentence-like label cells moved to *_source_cue; clean lemmas restored from concept ledger / v1 labels; blank = no clean label yet (honest gap)",
    "moved_counts": moved, "restored_counts": restored,
    "rows": rows_out}, ensure_ascii=False, indent=1), encoding="utf-8")

report = ["# Defect report for ChatGPT: v3 master label contamination", "",
          "2026-07-04. v3 STRUCTURE ADOPTED as master (212 concepts, bands, weights — good; the missing-QF catch was correct: v1 lacked the row). One systematic defect found and repaired in v3.1:",
          "",
          f"- Sentence/fragment cells in label columns (context cues leaked into lemma fields): isv {moved['isv']}, isv_cyr {moved['isv_cyr']}, uk {moved['uk']}, ru {moved['ru']} of 212 rows.",
          "- Example: ring.isv = 'Zato najprvo treba razsmotriti diskriminantne idealy primarnyh kolc.' (a sentence; lemma is kolco); theorem.isv = 'Hilbertov teorem o bazisu modula' (a title cue; lemma teorema).",
          f"- Repair: moved to new *_source_cue columns; lemmas restored from concept-ledger labels where available (isv {restored['isv']}, isv_cyr {restored['isv_cyr']}, uk {restored['uk']}, ru {restored['ru']}); remainder left blank (honest gap), NOT guessed.",
          "- Root cause guess: source-cue harvesting wrote into the label field when the ledger label was absent. For v4: keep 'label' and 'source_cue' as separate channels at extraction time; a label must be a lemma/citation form, never a sentence.",
          "- Triangulation log updated: this is the symmetric case to the Ränderung catch (you→me) and the missing-QF catch (you→me again); now me→you. The mutual-catch pattern is working as designed."]
(BASE / "V3_DEFECT_REPORT_FOR_CHATGPT_20260704.md").write_text("\n".join(report), encoding="utf-8")

print(f"rows {len(rows_out)} | moved {moved} | restored {restored}")

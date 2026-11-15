# CONSOLIDATED INTERLANGUAGE INTERFACE v1 — one per-concept artifact merging:
# marker v3.4 (forms+lemmas+CJK/AR), weight-ledger concept summary, global-register
# G-class, concept-history class, R1 decision + target-review verdict.
# Emits JSON + one self-contained sortable HTML. No promotions; statuses carried.
import csv
import html
import io
import json
import sys
import zipfile
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
BASE = Path(r"C:\Users\user\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")
DROP = BASE / "user made flr with chat web stuff"

def zread_csv(zname, member):
    with zipfile.ZipFile(DROP / zname) as z:
        return list(csv.DictReader(io.TextIOWrapper(z.open(member), encoding="utf-8-sig")))

mt = json.loads((BASE / "INTERLINGUAL_MARKER_TABLE_v3_4_20260705.json").read_text(encoding="utf-8"))
weights = zread_csv("INTERSLAVIC_FULL_TERM_WEIGHT_LEDGER_DELIVERABLE_v1_20260705.zip",
                    "INTERSLAVIC_CONCEPT_WEIGHT_SUMMARY_v1_20260705.csv")
greg = zread_csv("GLOBAL_MATH_REGISTER_AND_ROUTING_PASS_v1_CHATGPT_20260705.zip",
                 "GLOBAL_MATH_REGISTER_ATTRACTOR_TABLE_v1_CHATGPT_20260705.csv")
hist = zread_csv("CONCEPT_HISTORY_LAYER_PASS_v0_CHATGPT_20260705.zip",
                 "CONCEPT_HISTORY_LAYER_v0_CHATGPT_20260705.csv")
r1rev = zread_csv("INTERSLAVIC_TARGET_REVIEW_COMBINED_v1_20260706.zip",
                  "INTERSLAVIC_TARGET_REVIEW_PASS_v1_20260706/TARGET_REVIEW_R1_NORMALIZATION_DECISIONS_v1.csv")
r1 = json.loads((BASE / "NORMALIZATION_DECISIONS_R1_DRAFT_v1_20260705.json").read_text(encoding="utf-8"))
traps = zread_csv("GLOBAL_MATH_REGISTER_AND_ROUTING_PASS_v1_CHATGPT_20260705.zip",
                  "F14_TRAP_CONCEPT_LIST_v1_CHATGPT_20260705.csv")
trap_set = {str(r.get("concept","")).strip().lower() for r in traps}
v02 = {r["concept"].strip().lower(): r for r in json.loads((BASE / "GLOBAL_ATTRACTOR_PROBE_v0_2_20260710.json").read_text(encoding="utf-8"))["rows"]}
CROSSNOTES = {"noetherian": "eponym-override: Fable ATT stands; G3 was source-mass artifact",
              "artinian": "eponym-override: Fable ATT stands; G5 was source-mass artifact",
              "center": "ChatGPT G3 right: real S competitors (střed/središte); Fable v0.1 ATT was thin-family artifact",
              "group": "v0.1 folding artifact (groupe/grupa split); corrected in v0.2",
              "polynomial": "v0.1 folding artifact; v0.2 ATT",
              "isomorphism": "v0.1 folding artifact; v0.2 ATT"}

def key(r, *names):
    for n in names:
        if r.get(n):
            return str(r[n]).strip().lower()
    return ""

w_by = {key(r, "concept", "concept_label"): r for r in weights}
g_by = {key(r, "concept", "concept_label"): r for r in greg}
h_by = {key(r, "concept", "concept_label"): r for r in hist}
r1_by = {}
for r in r1["rows"]:
    # map by lemma-ish concept words: use row id and citation
    r1_by[r["id"].lower()] = r
r1rev_by = {key(r, "entry_id", "id", "row"): r for r in r1rev}

LANG_COLS = ["de", "en", "uk_lemma", "ru_lemma", "isv_lemma", "cs", "sk", "pl", "sl", "hr_sr", "bg",
             "es", "fr", "pt", "it", "ro", "ca", "gl", "rm", "ar", "fa", "ja", "zh_hans", "ko", "my_id"]
rows_out = []
matched = {"weights": 0, "greg": 0, "hist": 0}
for row in mt["rows"]:
    c = row["concept"].strip().lower()
    w = w_by.get(c)
    g = g_by.get(c)
    h = h_by.get(c)
    if w: matched["weights"] += 1
    if g: matched["greg"] += 1
    if h: matched["hist"] += 1
    out = {"concept": row["concept"], "stratum": row.get("stratum", ""), "C2": row.get("C2", "")}
    for lg in LANG_COLS:
        v = row.get(lg) or ""
        out[lg] = str(v)[:60]
    out["cjk_status"] = row.get("cjk_status", "")
    out["register_doublet_policy"] = str(row.get("register_doublet_policy", ""))[:100]
    out["weight_avg"] = (w or {}).get("avg_weight") or ""; out["ws_support"] = (w or {}).get("ws_support_hits") or ""
    out["weight_rows"] = (w or {}).get("term_rows") or ""
    out["global_class"] = (g or {}).get("global_class") or (g or {}).get("class") or ""
    out["g_score"] = (g or {}).get("global_attractor_score") or ""
    out["adverse_mass"] = (g or {}).get("adverse_mass") or ""
    out["competitor_mass"] = (g or {}).get("competitor_mass") or ""
    out["f14_trap"] = "TRAP" if c in trap_set else ""
    out["fable_v0_2"] = "ATT" if (v02.get(c) or {}).get("attractor") else ("no" if c in v02 else "")
    out["crosscheck_note"] = CROSSNOTES.get(c, "")
    out["history_class_descriptive"] = (h or {}).get("history_class") or ""  # weak predictor (pass-45 test): descriptive only
    out["lemma_note"] = str(row.get("lemma_note", ""))[:100]
    rows_out.append(out)

# attach R1 decisions to their concepts where the marker concept matches the R1 row semantics
R1_CONCEPT_MAP = {"step": "step?", "however": "however", "case-instance": "case", "length": "length"}
r1_summary = [{"row": r["id"], "citation": r["citation"], "dict": r["dict_status"][:80],
               "review": (r1rev_by.get(r["id"].lower(), {}) or {}).get("target_review_decision", "")}
              for r in r1["rows"]]

out = {"artifact": "consolidated_interlanguage_interface_v1_1", "generated": "2026-07-10",
       "boundary": "read-only consolidation of reviewed layers; candidate/witness tiers preserved in source artifacts; "
                   "nothing here is certified or community-approved",
       "sources": ["marker v3.4", "weight-ledger concept summary v1", "global-register pilot v1 (G-classes)",
                   "concept-history layer v0", "R1 draft v1 + target-review verdicts", "F14 trap list", "Fable attractor v0.2", "crosscheck v1 adjudications"],
       "join_stats": matched, "concepts": len(rows_out),
       "r1_register_decisions": r1_summary, "rows": rows_out}
(BASE / "CONSOLIDATED_INTERLANGUAGE_INTERFACE_v1_20260710.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

# ---- self-contained HTML ----
COLS = ["concept", "stratum", "global_class", "g_score", "fable_v0_2", "f14_trap", "history_class_descriptive", "weight_avg", "ws_support",
        "isv_lemma", "uk_lemma", "ru_lemma", "cs", "pl", "sl", "hr_sr", "bg",
        "es", "fr", "de", "ar", "fa", "ja", "zh_hans", "ko", "adverse_mass", "competitor_mass", "crosscheck_note", "register_doublet_policy", "lemma_note"]
head = "".join(f"<th onclick=\"srt({i})\">{c}</th>" for i, c in enumerate(COLS))
body = []
for r in rows_out:
    tds = "".join(f"<td>{html.escape(str(r.get(c) or ''))}</td>" for c in COLS)
    body.append(f"<tr>{tds}</tr>")
r1rows = "".join(f"<tr><td>{html.escape(x['row'])}</td><td>{html.escape(x['citation'])}</td>"
                 f"<td>{html.escape(x['dict'])}</td><td>{html.escape(x['review'])}</td></tr>" for x in r1_summary)
page = f"""<!doctype html><html><head><meta charset="utf-8"><title>Consolidated Interlanguage Interface v1.1</title>
<style>
body{{font-family:Segoe UI,system-ui,sans-serif;margin:16px;background:#fafafa;color:#222}}
h1{{font-size:20px}} .meta{{color:#666;font-size:12px;margin-bottom:10px}}
input{{padding:6px;width:340px;margin-bottom:10px;border:1px solid #bbb;border-radius:4px}}
table{{border-collapse:collapse;font-size:12px;background:#fff}}
th,td{{border:1px solid #ddd;padding:3px 6px;max-width:190px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}}
th{{background:#2d3e50;color:#fff;cursor:pointer;position:sticky;top:0}}
tr:nth-child(even){{background:#f3f6fa}} td:first-child{{font-weight:600}}
.wrap{{overflow-x:auto;max-height:78vh;overflow-y:auto}}
h2{{font-size:15px;margin-top:22px}}
</style></head><body>
<h1>Consolidated Interlanguage Interface v1.1</h1>
<div class="meta">2026-07-10 · {len(rows_out)} concepts · layers: marker v3.4 + weight ledger + global-register G-class + history class + R1 decisions ·
boundary: candidate/witness tiers only, nothing certified; history_class is descriptive (weak predictor, tested pass-45). Connective layer: see GLOBAL_CONNECTIVE_TABLE_v1_20260710.md (no cross-family attractors; formula substitutes first). Click headers to sort; type to filter.</div>
<input id="q" placeholder="filter (concept, form, class…)" oninput="flt()">
<div class="wrap"><table id="t"><thead><tr>{head}</tr></thead><tbody>
{''.join(body)}
</tbody></table></div>
<h2>R1 register decisions (Fable draft × internal target review)</h2>
<div class="wrap"><table><thead><tr><th>row</th><th>citation form</th><th>dictionary status</th><th>target-review verdict</th></tr></thead>
<tbody>{r1rows}</tbody></table></div>
<script>
let dir=1,last=-1;
function srt(i){{const tb=document.querySelector('#t tbody');dir=(last===i)?-dir:1;last=i;
[...tb.rows].sort((a,b)=>dir*a.cells[i].innerText.localeCompare(b.cells[i].innerText,undefined,{{numeric:true}}))
.forEach(r=>tb.appendChild(r));}}
function flt(){{const q=document.getElementById('q').value.toLowerCase();
document.querySelectorAll('#t tbody tr').forEach(r=>r.style.display=r.innerText.toLowerCase().includes(q)?'':'none');}}
</script></body></html>"""
(BASE / "CONSOLIDATED_INTERLANGUAGE_INTERFACE_v1_20260710.html").write_text(page, encoding="utf-8")
print(f"concepts: {len(rows_out)} | joins: {matched} | R1 rows: {len(r1_summary)}")
print("weight cols sample:", list(weights[0].keys())[:8] if weights else "none")
print("greg cols:", list(greg[0].keys())[:8] if greg else "none")
print("hist cols:", list(hist[0].keys())[:8] if hist else "none")

# F10-1 tail witness routing: join the under-witnessed retrofit rows (F10-1) with
# the expanded-anchor shelf reality (probe hits + shelf language inventory) and route
# each row: probeable-now / shelf-plausible / no-route (true collection gap).
# Classification only; no promotions, no new wording.
import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
BASE = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")
G = BASE / "user made flr with chat web stuff" / "expanded_grind_v1"

audit = json.loads((BASE / "F10_EAST_SLAVIC_SKEW_AUDIT_20260704.json").read_text(encoding="utf-8"))
retro = json.loads((BASE / "INTERSLAVIC_LEDGER_RETROFIT_20260704.json").read_text(encoding="utf-8"))
probes = json.loads((G / "EXPANDED_SOURCE_ANCHOR_C2_PROBES_v1_20260705.json").read_text(encoding="utf-8-sig"))["rows"]
ledger = json.loads((BASE / "INTERLINGUAL_CONCEPT_LEDGER_20260704.json").read_text(encoding="utf-8"))
spine = json.loads((BASE / "STRATIFIED_CORE_SPINE_PROPOSAL_20260704.json").read_text(encoding="utf-8"))

f10_1_ids = {r["term_id"] for r in audit["rows"] if r["bias_flag"] == "F10-1"}
retro_by_id = {r["term_id"]: r for r in retro["rows"]}
rows = [retro_by_id[i] for i in f10_1_ids if i in retro_by_id]
print(f"F10-1 rows joined: {len(rows)} of {len(f10_1_ids)} flagged")

# probe-covered concepts (already have shelf hits at concept level)
probe_concepts = defaultdict(set)
for p in probes:
    probe_concepts[p["concept"].lower()].add(p["lang"])

# concept-ledger German-key -> concept map (for routing via source_term)
def norm(s):
    s = unicodedata.normalize("NFC", (s or "").lower())
    return re.sub(r"[^a-zäöüßčšžě ]+", " ", s).strip()

de2concept = {}
for c in ledger["concepts"]:
    for dv in (c.get("de") or []):
        for w in norm(dv).split():
            if len(w) >= 6:
                de2concept.setdefault(w, c.get("en") or c["concept_id"])

de2keys = sorted(((k, v) for k, v in de2concept.items() if len(k) >= 6), key=lambda kv: -len(kv[0]))

# C2 spine concepts (priority band)
c2_concepts = {(r.get("concept_label") or r.get("concept_id") or "").lower() for r in spine["rows"]}

# international-stem heuristic: term whose latin form shares a long Latin/Greek stem
# is findable in ANY shelf language by stem search
INTL = re.compile(r"(algebr|matri[cx]|polynom|polinom|invariant|determinant|homomorf|izomorf|automorf|"
                  r"modul|ideal|teorem|funkci|grup|vektor|dimenzi|koeficient|element|form|sistem|metod|"
                  r"princip|relaci|konstru|reduk|transform|kongruen|kvadrat|linear|racional|iracional|"
                  r"diskriminant|rezultant|simetri|asimetri|geometri|aritmeti|logarit|eksponent|integral|"
                  r"differenci|diferenci|normal|maksimal|minimal|special|general|regular|singular|"
                  r"kompleks|kvaternion|skalar|tenzor|aksiom|hypote|hipote|definici|lema|korolar)")

def classify(r):
    term = (r.get("chosen_form_latin") or "").lower()
    src = norm(r.get("source_term"))
    # route 1: concept-level probe hit already exists
    cl = (r.get("concept_link") or "").lower()
    if cl and cl in probe_concepts:
        return "A_probe_covered_concept", cl, sorted(probe_concepts[cl])
    # route 2: German key maps to a ledger concept that has probe hits
    # (incl. compound containment: Hauptspur -> spur, Primärfaktoren -> faktor)
    for w in src.split():
        c = de2concept.get(w)
        if not c and len(w) >= 8:
            for k, v in de2keys:
                if k in w:
                    c = v
                    break
        if c and c.lower() in probe_concepts:
            return "A_probe_covered_concept", c.lower(), sorted(probe_concepts[c.lower()])
    # route 3: international stem -> findable by stem search in all shelves
    m = INTL.search(term)
    if m:
        return "B_intl_stem_probeable", m.group(1), ["all_shelves"]
    # route 4: German key maps to a concept (no probe yet) -> shelf-plausible via concept translation
    for w in src.split():
        c = de2concept.get(w)
        if not c and len(w) >= 8:
            for k, v in de2keys:
                if k in w:
                    c = v
                    break
        if c:
            return "C_concept_linked_shelf_plausible", c.lower(), []
    # route 5: phrase/date/title rows (workflow noise class)
    if re.search(r"\d{4}|§|\bs\.\b|band|seite", src) or len(src.split()) > 6:
        return "E_noise_or_bibliographic", "", []
    return "D_no_route_true_gap", "", []

routed = []
cnt = Counter()
lang_route = Counter()
for r in rows:
    route, key, langs = classify(r)
    cnt[route] += 1
    for l in langs:
        lang_route[l] += 1
    routed.append({"term_id": r["term_id"], "source_term": r.get("source_term"),
                   "chosen_form_latin": r.get("chosen_form_latin"),
                   "route": route, "route_key": key, "shelf_langs": langs,
                   "c2_priority": bool(key and key in c2_concepts)})

prio = [x for x in routed if x["c2_priority"]]
out = {"artifact": "tail_witness_routing_v1", "generated": "2026-07-05",
       "input": f"{len(rows)} F10-1 under-witnessed retrofit rows x expanded-anchor shelves",
       "route_counts": dict(cnt),
       "route_legend": {
           "A_probe_covered_concept": "concept already has expanded-shelf probe hits — witness routing = reuse probe files, per-row context check",
           "B_intl_stem_probeable": "international stem — findable by stem search across all shelves (bounded mechanical probe)",
           "C_concept_linked_shelf_plausible": "German key links to a ledger concept without probe hits yet — needs targeted per-concept probe",
           "D_no_route_true_gap": "no concept link, no international stem — true collection/curation gap",
           "E_noise_or_bibliographic": "dates/titles/phrase rows — workflow noise class, not witness targets"},
       "c2_priority_rows": len(prio),
       "shelf_lang_coverage_from_A": dict(lang_route),
       "rows": routed}
(BASE / "TAIL_WITNESS_ROUTING_v1_20260705.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

md = ["# F10-1 tail witness routing v1", "",
      f"2026-07-05. {len(rows)} under-witnessed (East-only) retrofit rows routed against the expanded-anchor shelves.",
      "", "| Route | Rows | Meaning |", "| --- | --- | --- |"]
for k, v in sorted(cnt.items()):
    md.append(f"| {k} | {v} | {out['route_legend'][k][:100]} |")
md += ["", f"C2-priority rows (route via a C2 spine concept): **{len(prio)}**", "",
       "## Bounded ChatGPT probe-task spec (routable rows)",
       "1. Input: routes A+C rows from TAIL_WITNESS_ROUTING_v1 json (term_id, route_key = concept).",
       "2. For each concept, probe the expanded shelves per language for the NATIVE lexeme families "
       "(reuse EXPANDED_SOURCE_ANCHOR probe machinery; do NOT search the ISV form — native forms witness the concept).",
       "3. Emit per-row: language, form, count, file_count, one KWIC window per (concept, language) — "
       "windows are mandatory (sense-audit lesson: binary form/ground form/complete system all failed on sense).",
       "4. Route B rows: single stem-search sweep per international stem across all shelves; emit same shape.",
       "5. NO promotions, NO bridge forms, NO summing diacritic-folded spellings; boundary text unchanged.",
       "", "Route D rows stay open as true gaps; route E rows are noise-class, excluded from witness targets."]
(BASE / "TAIL_WITNESS_ROUTING_v1_20260705.md").write_text("\n".join(md), encoding="utf-8")

print("route counts:", dict(cnt))
print("C2-priority rows:", len(prio))
print("sample A rows:", [(x['term_id'][:40], x['route_key']) for x in routed if x['route'].startswith('A')][:8])
print("sample D rows:", [(x['source_term'][:40] if x['source_term'] else '') for x in routed if x['route'] == 'D_no_route_true_gap'][:10])

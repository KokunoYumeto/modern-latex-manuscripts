# Normalization decision table v1 — fuse ChatGPT v4 policy classes (67 scatter
# groups) with Fable branch-evidence probe (34 doublet groups) into per-group
# decision inputs. Drafted verdicts are mechanical + noted; review layer decides.
import csv
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
BASE = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")
DROP = BASE / "user made flr with chat web stuff"

ev = json.loads((BASE / "REGISTER_DOUBLET_BRANCH_EVIDENCE_v1_20260704.json").read_text(encoding="utf-8"))["groups"]
props = list(csv.DictReader((DROP / "ISV_VARIANT_NORMALIZATION_PROPOSALS_v4_20260704.csv").open(encoding="utf-8-sig")))

# map lexicon entry ids -> probe group names (probe keys carry the id or lemma up front)
PROBE_FOR = {
    "reg-morati": "reg-morati (must)", "reg-imenno": "reg-imenno (namely)", "however": "však (however)",
    "entirely": "sovsěm (entirely)", "case-instance": "slučaj (case)",
    "reg-odnovrěmenno": "odnovrěmenno (simultaneously)",
    "exists-eksist": "existence family (eksistovati/suščestvovati/obstajati/postojati)",
    "power-exponent": "potęga/stepen/stupanj (power)", "follows-from": "slěduje (follows)",
    "is-called": "nazyvaje se (is called)", "holds-is-valid": "važi/velja/platiti (holds)",
    "reduce-to": "svesti/reducirati (reduce)", "foundation-basis": "osnova/baza (basis)",
    "length": "dlugost (length)", "generates": "porođati/generovati (generates)",
    "step": "korak/krok (step)", "curve": "kriva (curve)", "inner": "vnutrny (inner)",
    "work-paper": "dělo/praca (work/paper)", "take-vzeti": "vzęti (take)", "becomes": "stati (becomes)",
    "reg-prvy": "reg-prvy (first)", "lemma-noun": "lema (lemma)", "forms-constitutes": "tvori (forms/constitutes)",
    "remain-ostati": "ostati (remains)", "contrary": "protivno (conversely/contrary)",
    "well-defined": "jednoznačno oprěděljeny (well-defined)", "assumption-noun": "prědpoloženje (assumption)",
    "consequence": "poslědstvije (consequence)", "reg-pytanje": "pytanje/vprašanje (question)",
    "reg-rěšenje": "rěšenje (solution)",
}

NOTES = {
    "power-exponent": "CAUTION: stup- root in W = cs/sk 'stupeň' (degree), not the power operation; "
                      "operation words split mocnina(cs/sk)/potęga(pl)/степен(S+E) — three-way, no pan root.",
    "case-instance": "sl 'primer' collides with 'example' — S count inflated; slučaj is the honest S anchor (97).",
    "work-paper": "delo/rad/praca all noisy homographs; treat counts as indicative only.",
    "becomes": "postan-/postaj- root also feeds 'exists (postojati)' surfaces in S — counts overlap slightly.",
    "reg-imenno": "imenno- absent from ALL W/S prose (E-only via be); namreč/naime is the S form, totiž the cs form; "
                  "F12b poster child.",
    "exists-eksist": "four-lexeme field: internationalism (W-tilted 414/18), istnieje (pl-only), "
                     "postoji (S 268), obstaja (sl 218). suščestv- = 0 outside E. ISV doublet policy must "
                     "pick coverage set, not single winner.",
}

def verdict(groots):
    labels = []
    pan = []
    wonly = []
    sonly = []
    for label, d in groots.items():
        tot = d["W"] + d["S"] + d["E_be"]
        if tot < 3:
            continue
        if d["W"] >= 3 and d["S"] >= 3:
            pan.append(label)
        elif d["W"] >= 3 and d["S"] < 3:
            wonly.append(label)
        elif d["S"] >= 3 and d["W"] < 3:
            sonly.append(label)
        labels.append(label)
    if pan:
        return f"pan-root anchor: {', '.join(pan)}" + (f"; branch aliases: W={wonly} S={sonly}" if (wonly or sonly) else "")
    if wonly and sonly:
        return f"W/S doublet (F12b): keep both — W={', '.join(wonly)} | S={', '.join(sonly)}; dropping either costs that branch"
    if wonly:
        return f"W-specific only: {', '.join(wonly)} — S transparency unverified"
    if sonly:
        return f"S-specific only: {', '.join(sonly)} — W transparency unverified"
    return "insufficient native evidence in these genres (absence, not adverse)"

rows_out = []
for p in props:
    eid = p["entry_id"]
    probe = PROBE_FOR.get(eid)
    if probe and probe in ev:
        g = ev[probe]
        prof = "; ".join(f"{l}: W{d['W']}/S{d['S']}/E{d['E_be']}" for l, d in g.items())
        v = verdict(g)
    else:
        prof = ""
        v = ("orthography/inflection cluster — normalize citation form only, no branch decision needed"
             if p["policy_class"] == "inflectional_or_orthographic_cluster"
             else "not probed in v1 (queue for v2)")
    rows_out.append({
        "entry_id": eid, "lemma": p["lemma"], "class": p["class"], "policy_class": p["policy_class"],
        "variant_count": p["variant_count"], "variants": p["variants"],
        "branch_profile": prof, "draft_verdict": v, "note": NOTES.get(eid, ""),
        "status": "decision_input_needs_review",
    })

(BASE / "NORMALIZATION_DECISION_TABLE_v1_20260704.json").write_text(
    json.dumps({"artifact": "normalization_decision_table_v1", "generated": "2026-07-04",
                "boundary": "decision INPUTS: ChatGPT v4 policy classes + Fable branch evidence (mechanical probe 0.5); "
                            "draft verdicts are mechanical thresholds (>=3 hits/branch) + linguistic notes; no promotions",
                "rows": rows_out}, ensure_ascii=False, indent=1), encoding="utf-8")

md = ["# Normalization decision table v1 — F13 queue with branch weights", "",
      "2026-07-04. 67 scatter groups; 31 doublet groups carry branch-evidence profiles "
      "(W = cs+pl+sk, S = sl+hr+sr+bg+mk, E = be; native sources, mechanical probe 0.5). "
      "Draft verdicts: threshold >=3 hits per branch. Review layer decides; nothing promoted.", "",
      "| Group | Policy | Branch profile (per root) | Draft verdict | Note |", "| --- | --- | --- | --- | --- |"]
for r in rows_out:
    if r["branch_profile"]:
        md.append(f"| `{r['lemma']}` ({r['entry_id']}) | {r['policy_class']} | {r['branch_profile']} | {r['draft_verdict']} | {r['note']} |")
md += ["", "## Orthography/inflection clusters (no branch decision needed)",
       ", ".join(f"`{r['lemma']}`" for r in rows_out if not r["branch_profile"] and r["policy_class"] == "inflectional_or_orthographic_cluster"),
       "", "## Doublet groups not yet probed (v2 queue)",
       ", ".join(f"`{r['lemma']}`" for r in rows_out if not r["branch_profile"] and r["policy_class"] != "inflectional_or_orthographic_cluster")]
(BASE / "NORMALIZATION_DECISION_TABLE_v1_20260704.md").write_text("\n".join(md), encoding="utf-8")

probed = sum(1 for r in rows_out if r["branch_profile"])
print(f"rows: {len(rows_out)} | probed with branch profiles: {probed}")
for r in rows_out:
    if r["branch_profile"] and ("doublet" in r["draft_verdict"] or "pan-root" in r["draft_verdict"]):
        print(f"  {r['entry_id']:22s} -> {r['draft_verdict'][:100]}")

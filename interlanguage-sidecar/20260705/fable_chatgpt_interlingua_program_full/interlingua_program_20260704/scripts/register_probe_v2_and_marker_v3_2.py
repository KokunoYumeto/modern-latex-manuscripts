# Register-doublet probe v2 (16 groups left unprobed in v1, homograph checklist
# applied up front) + decision-table v1.1 patch + marker table v3.2 with register
# weight columns. Mechanical probe 0.5; no promotions.
import json
import re
import sys
import unicodedata
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
BASE = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")
SHELF = Path(r"C:\Users\Floris\Downloads\codex backup dump 7-4\$germanOut\sources\interslavic_triangulation\20260624_slavic_math_reference\text")
UND = BASE / "shelves" / "underrepresented_slavic"

LANGS = {"czech": "cs", "polish": "pl", "slovak": "sk", "slovenian": "sl",
         "croatian": "hr", "serbian": "sr", "bulgarian": "bg"}

def nfc(s):
    return unicodedata.normalize("NFC", s)

TAG = re.compile(r"<[^>]+>")
texts = {}
for f in sorted(SHELF.glob("*.txt")):
    for pref, lg in LANGS.items():
        if f.name.startswith(pref):
            texts[lg] = texts.get(lg, "") + "\n" + nfc(f.read_text(encoding="utf-8", errors="replace").lower())
texts["mk"] = nfc((UND / "macedonian" / "macedonian_ukim_math_lexicon.txt").read_text(encoding="utf-8", errors="replace").lower())
be = ""
for f in (UND / "belarusian").glob("*.html"):
    be += "\n" + TAG.sub(" ", f.read_text(encoding="utf-8", errors="replace"))
texts["be"] = nfc(be.lower())

# v2 groups. Homograph checklist applied at pattern level:
#  - ред(S/E)=order/row homograph of ręd=series -> probed separately and flagged
#  - sk 'rad'=series vs hr 'rad'=work -> cs/sk pattern requires řad-/rad[ay] word forms, flagged
#  - pl 'para'=steam vs pair -> flagged !
#  - hr 'sklada se'=agrees vs be 'складаецца'=consists -> split labels
G2 = {
    "reg-znati (known)": {
        "znan/poznat-": [r"znám", r"znan", r"poznat", r"познат"],
        "izvestn(E/bg)": [r"известн"],
        "wiadom/vedom-": [r"wiadom", r"vedom", r"вядом"],
    },
    "sootvětstvovati (corresponds)": {
        "odpovídá/odpowiada(W)": [r"odpovíd", r"odpovid", r"odpowiad", r"zodpoved"],
        "odgovara(S)": [r"odgovara", r"одговара"],
        "ustreza(sl)": [r"ustreza"],
        "sootvetstv(E/bg)": [r"соответств", r"съответств", r"адпавяда"],
    },
    "reg-ležati (lies)": {
        "lež-": [r"leží", r"lezí", r"leži", r"leż[yą]", r"лежи", r"ляж"],
    },
    "reg-sostojati (consists of)": {
        "sostoji/sastoji(S/E)": [r"sestoji", r"sastoji", r"састоји", r"състои", r"состои"],
        "skládá(cs/sk)": [r"skládá", r"sklad[áa] sa", r"skladá"],
        "składa(pl)": [r"składa", r"sklada si"],
        "skladajecca(be)": [r"складаецца"],
    },
    "provesti/izvesti (carry out)": {
        "provés/proved(cs/sk)": [r"provés", r"provedl", r"proved", r"prevedieme", r"uskutočn"],
        "przeprowadz(pl)": [r"przeprowadz"],
        "izved/izvesti(S)": [r"izved", r"izvest", r"изведе", r"извед"],
        "sprovesti(sr)": [r"sproved", r"sprovod", r"спровед", r"спровод"],
    },
    "reg-obći (general)": {
        "obecn/všeobecn(cs/sk)": [r"obecn", r"všeobecn", r"vseobecn"],
        "ogóln(pl)": [r"ogóln", r"ogoln"],
        "opći/opšti/obšt(S)": [r"opći", r"opci\b", r"opšt", r"општ", r"общ"],
        "splošn(sl)": [r"splošn", r"splosn"],
        "aguln(be)": [r"агульн"],
    },
    "ręd (series/sequence)": {
        "řada(cs)/!rad(sk)": [r"řad[ayě]", r"rad[ay]\b"],
        "szereg(pl)": [r"szereg"],
        "niz(hr/sr)": [r"niz\b", r"низ[ау]?\b", r"низа"],
        "zaporedje(sl)": [r"zapored"],
        "!ред(order-homograph)": [r"ред\b", r"рад\b"],
    },
    "tělo (body/division ring)": {
        "těleso(cs/sk)": [r"těles", r"teles"],
        "ciało(pl)": [r"ciał", r"cial"],
        "tijelo/telo/tjalo(S)": [r"tijel", r"тело", r"тяло", r"telo"],
    },
    "reg-davati (gives)": {
        "dává/dava-": [r"dává", r"dáva", r"dava", r"дава"],
        "daje-": [r"daje", r"даје", r"дае\b"],
    },
    "cěly (whole/integral)": {
        "cel- (pan, orthography scatter)": [r"celý", r"cel[aeoyáé]", r"cały", r"cał[ąe]", r"cal[aeyi]", r"cijel", r"цел", r"цео", r"цял", r"цэл"],
    },
    "reg-suma (sum)": {
        "suma-": [r"sum[aąyěu]", r"сум[аиу]"],
        "součet(cs/sk)": [r"souč", r"súč", r"sučet"],
        "vsota(sl)": [r"vsot"],
        "zbir/sbor(S)": [r"zbir", r"збир", r"сбор"],
    },
    "nula (zero)": {
        "nul-": [r"nul[aoyě]", r"нул"],
        "zero(pl)": [r"zer[oa]"],
    },
    "tip (type)": {
        "typ(W)": [r"typ"],
        "tip(S/E)": [r"tip\b", r"tip[aou]", r"тип"],
    },
    "vaga (weight of form)": {
        "vaga/váha(W+be)": [r"váh[ayu]", r"vah[ayu]", r"wag[aięou]", r"ваг[аіу]"],
        "teža/težina/teglo(S)": [r"tež[aei]", r"težin", r"тежин", r"тегло"],
        "вес(E)": [r"вес\b", r"веса\b"],
    },
    "!par (pair)": {
        "!par- (steam/couple homographs)": [r"pár", r"par\b", r"par[aąyou]\b", r"пар\b", r"пар[аиу]\b"],
        "dvojice(cs)": [r"dvojic"],
    },
    "reg-dopuščati (allows/admits)": {
        "dopušt/dopuszcz-": [r"dopuszcz", r"dopušt", r"dopust", r"допушт", r"допуска", r"dopušč", r"дапуска"],
        "připouští(cs)": [r"připouš", r"pripouš", r"pripúš", r"pripus"],
    },
}

def count(lg, pattern):
    return len(re.findall(r"(?<![\wа-яёіїєўѓќјљњџъ])" + pattern, texts.get(lg, "")))

order = ["cs", "pl", "sk", "sl", "hr", "sr", "bg", "mk", "be"]
res2 = {}
for gname, roots in G2.items():
    r = {}
    for label, pats in roots.items():
        per = {lg: sum(count(lg, p) for p in pats) for lg in order}
        r[label] = {"per_lang": per,
                    "W": per["cs"] + per["pl"] + per["sk"],
                    "S": per["sl"] + per["hr"] + per["sr"] + per["bg"] + per["mk"],
                    "E_be": per["be"]}
    res2[gname] = r

# merge into evidence artifact v2
ev1 = json.loads((BASE / "REGISTER_DOUBLET_BRANCH_EVIDENCE_v1_20260704.json").read_text(encoding="utf-8"))
ev2 = dict(ev1)
ev2["artifact"] = "register_doublet_branch_evidence_v2"
ev2["v2_note"] = ("v2 adds the 16 groups left unprobed in v1, with homograph guards pre-applied "
                  "(ред=order, sk rad vs hr rad, para=steam, sklada-se=agrees split from skladaecca=consists). "
                  "'!'-labels remain interpret-with-care.")
ev2["groups"] = {**ev1["groups"], **res2}
(BASE / "REGISTER_DOUBLET_BRANCH_EVIDENCE_v2_20260704.json").write_text(
    json.dumps(ev2, ensure_ascii=False, indent=1), encoding="utf-8")

def verdict(groots):
    pan, wonly, sonly = [], [], []
    for label, d in groots.items():
        if label.startswith("!"):
            continue
        tot = d["W"] + d["S"] + d["E_be"]
        if tot < 3:
            continue
        if d["W"] >= 3 and d["S"] >= 3:
            pan.append(label)
        elif d["W"] >= 3:
            wonly.append(label)
        elif d["S"] >= 3:
            sonly.append(label)
    if pan:
        return f"pan-root anchor: {', '.join(pan)}" + (f"; branch aliases: W={wonly} S={sonly}" if (wonly or sonly) else "")
    if wonly and sonly:
        return f"W/S doublet (F12b): keep both — W={', '.join(wonly)} | S={', '.join(sonly)}; dropping either costs that branch"
    if wonly:
        return f"W-specific only: {', '.join(wonly)}"
    if sonly:
        return f"S-specific only: {', '.join(sonly)}"
    return "insufficient native evidence in these genres (absence, not adverse)"

# patch decision table -> v1.1
PROBE2_FOR = {
    "reg-znati": "reg-znati (known)", "corresponds": "sootvětstvovati (corresponds)",
    "reg-ležati": "reg-ležati (lies)", "reg-sostojati": "reg-sostojati (consists of)",
    "carry-out": "provesti/izvesti (carry out)", "reg-obći": "reg-obći (general)",
    "series-sequence-red": "ręd (series/sequence)", "body-telo-infl": "tělo (body/division ring)",
    "reg-davati": "reg-davati (gives)", "integral-whole": "cěly (whole/integral)",
    "reg-suma": "reg-suma (sum)", "zero-noun": "nula (zero)", "type": "tip (type)",
    "weight-of-form": "vaga (weight of form)", "pair": "!par (pair)",
    "reg-dopuščati": "reg-dopuščati (allows/admits)",
}
NOTES2 = {
    "series-sequence-red": "HOMOGRAPH ZONE: ред(S/E)=order/row, sk rad ambiguous, hr rad=work. Series lexemes are "
                           "fully split: řada(cs)/szereg(pl)/niz(hr,sr)/zaporedje(sl) — NO pan root; ISV ręd leans E; "
                           "four-way branch decision, review required.",
    "pair": "par- counts include steam/couple homographs (flagged); dvojice(cs) is the W math-register alternative.",
    "weight-of-form": "vaga/váha/waga = W+be lexeme; S uses teža/težina/тегло — W/S doublet on a Noether-stratum term "
                      "(vaga was a held-word win; this confirms its W+be currency).",
    "body-telo-infl": "concept-layer probe (ws_witness_backfill v0/v1) already typed this; register layer agrees: "
                      "těleso(W-cs/sk) / ciało(pl) / tijelo-telo(S) — three-way, ISV tělo transparent to S+cs/sk, "
                      "pl ciało is the odd one out.",
    "type": "same lexeme, orthography split typ(W)/tip(S,E) — normalize citation form only.",
    "integral-whole": "single pan root cel- across all 9 langs — orthography scatter, not a doublet.",
}
dt = json.loads((BASE / "NORMALIZATION_DECISION_TABLE_v1_20260704.json").read_text(encoding="utf-8"))
patched = 0
for r in dt["rows"]:
    pk = PROBE2_FOR.get(r["entry_id"])
    if pk and pk in res2:
        g = res2[pk]
        r["branch_profile"] = "; ".join(f"{l}: W{d['W']}/S{d['S']}/E{d['E_be']}" for l, d in g.items())
        r["draft_verdict"] = verdict(g)
        if r["entry_id"] in NOTES2:
            r["note"] = (r.get("note", "") + " " if r.get("note") else "") + NOTES2[r["entry_id"]]
        patched += 1
dt["artifact"] = "normalization_decision_table_v1_1"
dt["v1_1_note"] = "v1.1: probe-v2 branch profiles patched into the 16 previously unprobed doublet groups; homograph guards applied."
(BASE / "NORMALIZATION_DECISION_TABLE_v1_20260704.json").write_text(
    json.dumps(dt, ensure_ascii=False, indent=1), encoding="utf-8")

# regenerate MD
md = ["# Normalization decision table v1.1 — F13 queue with branch weights", "",
      "2026-07-04. 67 scatter groups; 47 carry branch-evidence profiles (v1 probe 31 + v2 probe 16). "
      "W = cs+pl+sk, S = sl+hr+sr+bg+mk, E = be; native sources, mechanical probe 0.5; homograph guards in v2. "
      "Draft verdicts: threshold >=3 hits/branch, '!' roots excluded from verdicts. Review layer decides.", "",
      "| Group | Policy | Branch profile (per root) | Draft verdict | Note |", "| --- | --- | --- | --- | --- |"]
for r in dt["rows"]:
    if r["branch_profile"]:
        md.append(f"| `{r['lemma']}` ({r['entry_id']}) | {r['policy_class']} | {r['branch_profile']} | {r['draft_verdict']} | {r.get('note','')} |")
md += ["", "## Orthography/inflection clusters (no branch decision needed)",
       ", ".join(f"`{r['lemma']}`" for r in dt["rows"] if not r["branch_profile"] and r["policy_class"] == "inflectional_or_orthographic_cluster"),
       "", "## Auditor corrections (Fable, v1 run)",
       "- **however (však)**: jednak S-mass = hr/sr jednak=EQUAL homograph → W/S doublet (W: však/totiž | S: ipak/vendar/međutim).",
       "- **case-instance (slučaj)**: pripad S-mass = hr pripada=belongs homograph → W/S doublet (W: případ/przypadek | S: slučaj).",
       "- Every pan verdict requires a homograph audit (v2 probe applies guards at pattern level)."]
(BASE / "NORMALIZATION_DECISION_TABLE_v1_20260704.md").write_text("\n".join(md), encoding="utf-8")

# marker table v3.2: register columns on mappable concept rows
mt = json.loads((BASE / "INTERLINGUAL_MARKER_TABLE_v3_1_REPAIRED_20260704.json").read_text(encoding="utf-8"))
dt_by_id = {r["entry_id"]: r for r in dt["rows"]}
CONCEPT_MAP = {  # marker concept -> decision-table entry_id
    "lemma": "lemma-noun", "basis": "foundation-basis", "power": "power-exponent",
    "zero": "zero-noun", "corollary": "consequence", "assumption": "assumption-noun",
    "division ring / body": "body-telo-infl",
}
marked = 0
for row in mt["rows"]:
    eid = CONCEPT_MAP.get(row["concept"])
    if eid and eid in dt_by_id and dt_by_id[eid]["branch_profile"]:
        d = dt_by_id[eid]
        row["register_doublet_group"] = eid
        row["register_branch_profile"] = d["branch_profile"]
        row["register_doublet_policy"] = d["draft_verdict"]
        row["register_evidence"] = "REGISTER_DOUBLET_BRANCH_EVIDENCE_v2_20260704.json (mechanical_probe 0.5)"
        marked += 1
mt["artifact"] = "interlingual_marker_table_v3_2"
mt["v3_2_note"] = ("v3.2: register-layer weight columns (register_doublet_group/branch_profile/doublet_policy/evidence) "
                   "added to concept rows that coincide with F13 doublet groups; source = branch-evidence probe v1+v2; "
                   "decision inputs only, nothing promoted.")
(BASE / "INTERLINGUAL_MARKER_TABLE_v3_2_20260704.json").write_text(
    json.dumps(mt, ensure_ascii=False, indent=1), encoding="utf-8")

print(f"probe-v2 groups: {len(res2)} | decision rows patched: {patched} | marker rows with register columns: {marked}")
for gname, roots in res2.items():
    tops = sorted(((l, d) for l, d in roots.items()), key=lambda kv: -(kv[1]["W"] + kv[1]["S"] + kv[1]["E_be"]))
    print(f"  {gname}: " + ", ".join(f"{l}:W{d['W']}/S{d['S']}/E{d['E_be']}" for l, d in tops[:4]))

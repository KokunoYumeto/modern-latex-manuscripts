# Fable linguistic review + merge of ChatGPT pass-v4 proposal -> lexicon v2.4.
# Repairs: false root-prefix attaches, cross-group collisions, wrong dictionary
# glosses (prefix-match defect), per-token entries consolidated into lemma groups,
# failed attaches from the triage re-applied. v2 frozen before in-place update.
import json
import re
import shutil
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
BASE = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")
DROP = BASE / "user made flr with chat web stuff"

v23 = json.loads((DROP / "proof_prose_lexicon_v2_3_chatgpt_longtail_proposal.json").read_text(encoding="utf-8-sig"))
triage = json.loads((DROP / "ISV_LONGTAIL_TYPE_TRIAGE_PASS_v4_20260704.json").read_text(encoding="utf-8-sig"))
entries = v23["entries"]
by_id = {e["id"]: e for e in entries}

# --- decision tables (Fable review 2026-07-04) ---

EXCLUDE = {  # token -> reason
    "avgusta": "bibliographic month residue (dates in references)",
    "julija": "bibliographic month residue",
    "oktobra": "bibliographic month residue",
    "hamel": "eponym (Hamel basis) — covered by eponym rule; added to coverage EPONYMS",
}

# false attaches to strip: group_id -> variants to remove
STRIP = {
    "arbitrary": ["proizhodi", "proizhodit", "proizhodet", "proizvesti"],
    "series-sequence-red": ["reducirano", "reducira"],
    "exists-eksist": ["suščstveno"],
    "remain-ostati": ["nastal", "nastalo"],
    "starting-point": ["izhodet"],
}

# token -> existing group id (attach instead of new entry / re-home after strip)
ATTACH = {
    "dobyva": "reg-dobiti", "dobyvajut": "reg-dobiti", "dobyvamo": "reg-dobiti",
    "poraždžaje": "generates",
    "obščih": "reg-obći",
    "prethodnom": "preceding",
    "ležeče": "reg-ležati", "ležeči": "reg-ležati", "ležečih": "reg-ležati",
    "nužnym": "reg-nužno",
    "znanyh": "reg-znati", "znanym": "reg-znati",
    "vede": "reg-voditi", "vodet": "reg-voditi",
    "danu": "reg-davati",
    "neka": "reg-nehaj",
    "dakle": "reg-teda",
    "dozvalja": "reg-dopuščati", "dozvoljaje": "reg-dopuščati",
    "skazanom": "as-said",
    "postoji": "reg-obstajati",
    "potenca": "power-exponent",
    "reducirano": "reduce-to", "reducira": "reduce-to",
    "vzęti": "take-vzeti",
}
ATTACH_BY_LEMMA = {  # target resolved by lemma substring (id unknown/mangled)
    "proizhodi": "proizhod", "proizhodit": "proizhod", "proizhodet": "proizhod",
    "vvodet": "vvesti",
}

# consolidated lemma groups for retained v4 per-token entries:
# (id, lemma, en, class, [tokens])
G = [
    ("additive", "aditivny", "additive", "math_general", ["aditivna", "aditivne", "aditivny"]),
    ("aggregate", "agregat", "aggregate (Noether register: system/aggregate)", "noether_corpus", ["agregat", "agregaty"]),
    ("alternative", "alternativa", "alternative", "discourse_noun", ["alternativa"]),
    ("annulled", "anulovany", "annulled; cancelled", "math_general", ["anulovany"]),
    ("unconditionally", "bezuslovno", "unconditionally", "discourse_adverb", ["bezuslovno"]),
    ("block-adj", "blokovy", "block (matrix-block adj.)", "math_general", ["blokovu"]),
    ("more-bolj", "bolj", "more (sl.)", "comparison_marker", ["bolj"]),
    ("dissertation", "disertacija", "dissertation", "bibliographic", ["disertacije", "disertaciji"]),
    ("discontinuous", "diskontinuirny", "discontinuous", "math_general", ["diskontinuirne"]),
    ("divergence", "divergencija", "divergence", "math_general", ["divergencija", "divergencijami", "divergenciji", "divergencijnyh"]),
    ("divisor", "divizor", "divisor", "curriculum_algebra", ["divizorov"]),
    ("division-op", "děljenje", "division (operation)", "curriculum_algebra", ["děljenje"]),
    ("extremals", "ekstremala", "extremal(s)", "math_general", ["ekstremaly"]),
    ("extremely", "ekstremno", "extremely", "discourse_adverb", ["ekstremno"]),
    ("eliminated", "eliminovany", "eliminated", "proof_operation", ["eliminovane"]),
    ("energy-adj", "energijsky", "energy (adj.)", "math_general", ["energijskih", "energijskim"]),
    ("a-fortiori", "fortiori", "a fortiori (Latin proof connective)", "proof_connective", ["fortiori"]),
    ("generates-generovati", "generovati", "generates (internationalism doublet of porođati)", "construction_predicate", ["generuje"]),
    ("geometric", "geometričny", "geometric(ally)", "math_general", ["geometrična", "geometrično"]),
    ("limit-boundary", "granica", "boundary; limit", "math_general", ["granici", "granicu"]),
    ("characterize", "harakterizovati", "characterizes / is characterized", "proof_predicate", ["harakterizovana", "harakterizovane", "harakterizovati", "harakterizuje", "harakterno"]),
    ("have-imati", "imati", "to have", "auxiliary", ["imati"]),
    ("denominator", "imenitelj", "denominator", "curriculum_algebra", ["imenitelj"]),
    ("integration", "integriranje", "integration", "math_general", ["integriranje", "integriranjem"]),
    ("iteration", "iteracija", "iteration", "math_general", ["iteraciju"]),
    ("choose-izbrati", "izbrati", "choose; select (we choose)", "proof_operation", ["izberemo", "izbirati", "izbrana", "izbrane", "izbrano", "izbranyh", "vyberemo", "vybrati"]),
    ("omit-izpustiti", "izpustiti", "omit (details); leave out", "proof_operation", ["izpustiti", "izpuščene"]),
    ("statement-izreka", "izreka", "statement (sl. izrek: theorem statement)", "proof_grammar", ["izreka", "izrekti"]),
    ("execute-izvršiti", "izvršiti", "carries out; executes", "proof_operation", ["izvršaje", "izvršenja", "izvršiti"]),
    ("appears-javjati", "javjati se", "appears; presents itself", "proof_predicate", ["javja", "javjajut"]),
    ("quantity", "količstvo", "quantity", "math_general", ["količstvo"]),
    ("complexes", "kompleks", "complex(es)", "math_general", ["kompleksov"]),
    ("compositional", "kompozicijny", "compositional", "math_general", ["kompozicione"]),
    ("congruence", "kongruencija", "congruence", "curriculum_algebra", ["kongruencija", "kongruencije"]),
    ("construct", "konstruovati", "constructs / constructed", "proof_operation", ["konstruovane", "konstruovano", "konstruuje", "skonstruovana"]),
    ("contravariant", "kontravarianta", "contravariant (classical invariant theory)", "noether_corpus", ["kontravarianty"]),
    ("coordinates", "koordinata", "coordinate(s)", "math_general", ["koordinat", "koordinatah", "koordinaty"]),
    ("roots-eq", "korenj", "root(s) (of an equation)", "curriculum_algebra", ["koreneve", "korenov"]),
    ("coresidual", "koresidualny", "coresidual (classical invariant theory)", "noether_corpus", ["koresidualne", "koresidualnyh"]),
    ("curvature", "krivina", "curvature", "math_general", ["kriviny"]),
    ("latin-letters", "latinsky", "Latin (letters)", "proof_grammar", ["latinskymi"]),
    ("lines", "linija", "line(s)", "math_general", ["linije"]),
    ("literature", "literatura", "literature (in the literature)", "bibliographic", ["literaturi", "literaturu"]),
    ("any-ljuby", "ljuby", "any (quantifier; doublet of libovoljny)", "quantifier", ["ljubogo", "ljuby"]),
    ("thinks", "mysliti", "thinks / thoughts", "discourse_predicate", ["mysli"]),
    ("lowest", "najniži", "lowest", "comparison_marker", ["najniži"]),
    ("simplest", "najprostějši", "simplest; easiest", "comparison_marker", ["najprostějši"]),
    ("impose", "naložiti", "impose", "proof_operation", ["naložiti"]),
    ("in-conclusion", "naposlědku", "at last; in conclusion", "proof_sequence", ["naposlědku"]),
    ("current-nastoječi", "nastoječi", "current; present (sl.)", "proof_reference", ["nastoječa", "nastoječej"]),
    ("manner-nacin", "način", "manner; way", "discourse_noun", ["način", "načinom", "načinov"]),
    ("our", "naša", "our (fem.)", "pronoun_reference", ["naša"]),
    ("unchanged", "neizměnjeny", "unchanged (invariant-adjacent)", "math_general", ["neizměnjena"]),
    ("unnecessary", "nepotrěbno", "unnecessary", "modality", ["nepotrěbno"]),
    ("notes-bib", "nota", "note(s) (bibliographic)", "bibliographic", ["noty"]),
    ("new-fem", "nova", "new (fem.)", "modifier", ["nova"]),
    ("numbering", "numerovanje", "numbering", "math_general", ["numerovanju"]),
    ("someone", "někto", "someone (oblique forms)", "pronoun_reference", ["někom", "někomu"]),
    ("something", "něčto", "something", "pronoun_reference", ["něčto"]),
    ("explained", "objasnjeny", "explained", "proof_reference", ["objasnjeno"]),
    ("drops-out", "odpadati", "drops out; falls away (of cases)", "proof_predicate", ["odpada", "odpadajut"]),
    ("from-now", "odteper", "from now on", "proof_sequence", ["odteper"]),
    ("describe", "opisati", "describe", "proof_operation", ["opisati"]),
    ("indeed-opravdu", "opravdu", "indeed; truly (cz.)", "discourse_adverb", ["opravdu"]),
    ("pair-oblique", "para", "pair (oblique form)", "math_general", ["para"]),
    ("write-pisati", "pisati", "to write", "proof_operation", ["pisati"]),
    ("given-podany", "podany", "given; presented", "proof_reference", ["podane", "podati"]),
    ("subject-to", "podlagati", "is subject to / underlying", "proof_predicate", ["podlagajut", "podloženo"]),
    ("submodule", "podmodul", "submodule", "noether_corpus", ["podmodul", "podmodulov", "podmoduly"]),
    ("domains", "područje", "domain(s); region(s)", "math_general", ["područja"]),
    ("concept-pojetje", "pojętje", "notion; concept", "proof_grammar", ["pojętje"]),
    ("mediates", "posrědovati", "mediates / is mediated (by)", "proof_predicate", ["posrědkuje", "posrědovana", "posrědovane", "posrědovany", "posrěduje", "posrědujut"]),
    ("procedure-postupak", "postupak", "procedure; process", "proof_grammar", ["postupa", "postupak", "postupku"]),
    ("behaviour", "povedenje", "behaviour", "math_general", ["povedenje"]),
    ("by-repetition", "povtorjenje", "by repetition", "proof_operation", ["povtorjenjem"]),
    ("positive", "pozitivny", "positive(ly)", "math_general", ["pozitivno", "pozitivnyh"]),
    ("beginning-with", "počinati", "beginning (with)", "proof_sequence", ["počinaje", "počinajući"]),
    ("since-posto", "pošto", "since; because (hr.)", "causal_connective", ["pošto"]),
    ("work-praca", "praca", "work; paper (W spelling)", "proof_reference", ["praca"]),
    ("add-pridavati", "pridavati", "adds; attaches", "proof_operation", ["pridavajuči"]),
    ("in-doing-so", "pritom", "at the same time; in doing so", "discourse_connective", ["pritom"]),
    ("whereby", "pričem", "whereby; moreover", "discourse_connective", ["pričem"]),
    ("procedure", "procedura", "procedure", "proof_grammar", ["procedura", "procedury"]),
    ("passing", "prohodny", "passing; transient", "math_general", ["prohodny"]),
    ("conductor-ctx", "provodnik", "conductor/guide (CONTEXT REVIEW)", "context_review", ["provodnik", "provodnika", "provodnikami"]),
    ("verify", "prověriti", "verify; check", "proof_operation", ["prověriti"]),
    ("variable-premenna", "prěmenna", "variable (E-flavored prěmennaja)", "curriculum_algebra", ["prěmennoj"]),
    ("transform-preobraziti", "prěobraziti", "transform", "proof_operation", ["prěobraziti"]),
    ("intersection-presek", "prěsěk", "intersection; cross-section", "curriculum_algebra", ["prěseka"]),
    ("translation", "prěvod", "translation / translates", "proof_reference", ["prěvod", "prěvodet", "prěvodi"]),
    ("ordinary-redovy", "rędovy", "ordinary; of-a-series (context)", "math_general", ["rędovo", "rędovogo"]),
    ("realization", "realizacija", "realization", "math_general", ["realizaciju"]),
    ("respectively-resp", "respektivno", "respectively (internationalism doublet of odpovědno)", "proof_grammar", ["respektivno"]),
    ("solve-resiti", "rěšiti", "solves; solve", "proof_operation", ["rěšaje", "rěšiti"]),
    ("separable", "separabilny", "separable", "curriculum_algebra", ["separabilne", "separabilno", "separabilnogo", "separabilnym"]),
    ("union-sjediniti", "sjediniti", "unite(s); union", "proof_operation", ["sjedinenja", "sjediniti", "sjedinjene"]),
    ("scanned", "skanovany", "scanned", "bibliographic", ["skanovanogo"]),
    ("weak", "slaby", "weak", "math_general", ["slabyh"]),
    ("serves", "služiti", "serves (as)", "proof_predicate", ["služet", "služi"]),
    ("specially", "specijalno", "specially; in particular", "discourse_adverb", ["specijalno"]),
    ("together-spolu", "spolu", "together (W)", "discourse_adverb", ["spolu"]),
    ("together-skupaj", "skupaj", "together (sl.)", "discourse_adverb", ["skupaj"]),
    ("manner-sposob", "sposob", "manner; way; method", "discourse_noun", ["sposob", "sposobov", "sposoby"]),
    ("matter-sprava", "sprava", "matter / on-the-right (CONTEXT REVIEW)", "context_review", ["sprava"]),
    ("means", "srědstvo", "means; medium", "discourse_noun", ["srědstvo"]),
    ("old", "stary", "old (instr.pl)", "modifier", ["starymi"]),
    ("page-side", "strana", "page; side", "bibliographic", ["stran", "strana", "strani", "straně"]),
    ("structure", "struktura", "structure / structural", "math_general", ["struktura", "strukturne", "strukturny", "strukturu"]),
    ("create", "stvoriti", "create(d)", "proof_operation", ["stvorenih", "stvoriti"]),
    ("reduction-svod", "svod", "reduction/compendium (CONTEXT REVIEW)", "context_review", ["svod"]),
    ("transforms", "transformovati", "transforms", "proof_operation", ["transformuje", "transformujut"]),
    ("transitive", "tranzitivny", "transitive", "curriculum_algebra", ["tranzitivnom", "tranzitivny"]),
    ("claim-tvrditi", "tvrditi", "we claim / asserts", "proof_predicate", ["tvrdimo"]),
    ("succeeds", "uspěvati", "succeeds", "proof_predicate", ["uspěva"]),
    ("by-consideration", "uvažanje", "by consideration (of)", "proof_operation", ["uvažanjem"]),
    ("great-fem", "velika", "great; large (fem.)", "modifier", ["velika"]),
    ("chain-veriga", "veriga", "chain (NB chain conditions)", "noether_corpus", ["veriga"]),
    ("see-videti", "viděti", "to see (one sees)", "proof_predicate", ["viděti"]),
    ("embed-vloziti", "vložiti", "insert; embed (CONTEXT REVIEW: embedding?)", "context_review", ["vložimy"]),
    ("time", "vrěme", "time", "math_general", ["vrěme"]),
    ("introduction-vvod", "vvod", "introduction", "proof_reference", ["vvod"]),
    ("reads-glasiti", "glasiti", "reads (the statement reads)", "proof_predicate", ["glasi"]),
    ("closed-zakryto", "zakryty", "closed (CONTEXT REVIEW: closed set?)", "context_review", ["zakryto"]),
    ("sharpening", "zaostrenje", "sharpening (of a result)", "proof_grammar", ["zaostrenje"]),
    ("session-bib", "zasědanje", "session (bibliographic: Sitzungsberichte)", "bibliographic", ["zasědanju"]),
    ("we-know", "znajemo", "we know", "knowledge_marker", ["znajemo"]),
    ("sign-znak", "znak", "sign; symbol", "proof_grammar", ["znak"]),
    ("reduction-zvedenje", "zvedenje", "reduction (uk-flavored)", "proof_operation", ["zvedenje"]),
    ("consider-razsmatrjati", "razsmatrjati", "we consider / consideration", "proof_operation", ["razsmatramo", "razsmatranja"]),
    ("essentially", "suščestvenno", "essentially; substantially", "discourse_adverb", ["suščstveno"]),
    ("proceeds-izhoditi", "izhoditi", "proceeds/emanates from", "proof_predicate", ["izhodet"]),
    ("produce-proizvesti", "proizvesti", "produce", "proof_operation", ["proizvesti"]),
]

# review flags on kept-but-borderline attaches
FLAG = {
    "corresponds": "odgovorno kept (correspondingly, S-branch odgovarati) — review",
    "reg-obstajati": "obstava/obstavaje/obstavanje + postoji (hr postojati) kept as existence family — review doublet policy",
    "exists-eksist": "suščstvovanje kept (existence noun, root family)",
}

# --- apply ---
consumed = set()
log = {"strip": [], "attach": [], "exclude": [], "merge_groups": 0, "reapplied": [], "unresolved": [], "leftover_v4": []}

for gid, toks in STRIP.items():
    e = by_id.get(gid)
    if not e:
        log["unresolved"].append(("strip-missing-group", gid))
        continue
    before = len(e["variants"])
    e["variants"] = [v for v in e["variants"] if v.lower() not in {t.lower() for t in toks}]
    log["strip"].append((gid, before - len(e["variants"]), toks))

v4_by_lemma = {e["lemma"]: e for e in entries if str(e.get("id", "")).startswith("v4-")}

def attach(tok, target_id):
    e = by_id.get(target_id)
    if not e:
        log["unresolved"].append(("attach-missing-group", tok, target_id))
        return
    if tok.lower() not in {v.lower() for v in e["variants"]}:
        e["variants"].append(tok)
        e["variants"] = sorted(set(e["variants"]))
    prov = set(e.get("provenance", []))
    prov.add("fable_v4_review")
    e["provenance"] = sorted(prov)
    log["attach"].append((tok, target_id))
    if tok in v4_by_lemma:
        consumed.add(v4_by_lemma[tok]["id"])

for tok, tid in ATTACH.items():
    attach(tok, tid)
for tok, lemma_sub in ATTACH_BY_LEMMA.items():
    hits = [e for e in entries if lemma_sub in e["lemma"] and not str(e.get("id", "")).startswith("v4-")]
    if len(hits) == 1:
        attach(tok, hits[0]["id"])
    else:
        log["unresolved"].append(("attach-by-lemma", tok, lemma_sub, [h["id"] for h in hits]))

for tok, reason in EXCLUDE.items():
    if tok in v4_by_lemma:
        consumed.add(v4_by_lemma[tok]["id"])
        log["exclude"].append((tok, reason))

merged_entries = []
for gid, lemma, en, cls, toks in G:
    provs = {"chatgpt_v4_longtail", "fable_v4_review"}
    found = []
    for t in toks:
        if t in v4_by_lemma:
            consumed.add(v4_by_lemma[t]["id"])
            found.append(t)
        else:
            found.append(t)  # keep token anyway; it came from the triage list
    merged_entries.append({
        "id": gid if gid not in by_id else gid + "-v4",
        "lemma": lemma, "en": en, "class": cls,
        "variants": sorted(set(found)),
        "provenance": sorted(provs),
        "status": "proposed_internal_insert; needs linguistic review",
        "source_use": "generated_internal_consistency",
        "permitted_use_weight": 0.35,
        "en_source": "fable_v4_review (chatgpt dictionary prefix-gloss defect repaired)",
    })
    log["merge_groups"] += 1

entries = [e for e in entries if e["id"] not in consumed]
entries.extend(merged_entries)
by_id = {e["id"]: e for e in entries}

# re-apply failed triage attaches
have = {v.lower() for e in entries for v in e["variants"]}
pat = re.compile(r"Attach to existing lexicon group (\S+) \(")
overridden = set(ATTACH) | set(ATTACH_BY_LEMMA) | set(EXCLUDE)
for r in triage["rows"]:
    if r.get("recommended_action") != "attach_variant":
        continue
    tok = r["token"]
    if tok.lower() in have or tok in overridden:
        continue
    m = pat.search(r.get("note", ""))
    if not m:
        log["unresolved"].append(("noparse", tok))
        continue
    tid = m.group(1)
    if tid in by_id:
        e = by_id[tid]
        e["variants"] = sorted(set(e["variants"]) | {tok})
        have.add(tok.lower())
        log["reapplied"].append((tok, tid))
    else:
        log["unresolved"].append(("target-missing", tok, tid))

for gid, note in FLAG.items():
    if gid in by_id:
        by_id[gid]["review_flag"] = note

leftover = [e["id"] for e in entries if str(e.get("id", "")).startswith("v4-")]
log["leftover_v4"] = leftover

# freeze + write
shutil.copy(BASE / "data" / "proof_prose_lexicon_v2.json", BASE / "frozen" / "proof_prose_lexicon_v2_230_preV4.json")
v23["entries"] = entries
v23["entry_count"] = len(entries)
v23["artifact"] = "proof_prose_lexicon_v2_4"
v23["review_note"] = ("v2.4 = ChatGPT v2.3 proposal + Fable linguistic review 2026-07-04: 4 false root-prefix attach families "
                      "re-homed (proizhod->originates, reducir->reduce-to, suscstveno->essentially, nastal/nastalo->nastavati), "
                      "vzeti collision merged, 237 per-token candidates consolidated into lemma groups with corrected EN glosses "
                      "(dictionary prefix-gloss defect), failed triage attaches re-applied, months/eponym residue excluded. "
                      "Still proposal-layer: generated_internal_consistency, 0.35, needs linguistic review.")
(BASE / "data" / "proof_prose_lexicon_v2.json").write_text(json.dumps(v23, ensure_ascii=False, indent=1), encoding="utf-8")

(BASE / "V4_REVIEW_MERGE_LOG_20260704.json").write_text(
    json.dumps(log, ensure_ascii=False, indent=1, default=str), encoding="utf-8")

print(f"entries: {len(entries)} | merged groups: {log['merge_groups']} | attaches: {len(log['attach'])} "
      f"| reapplied failed attaches: {len(log['reapplied'])} | excluded: {len(log['exclude'])}")
print("strips:", [(g, n) for g, n, _ in log["strip"]])
print("unresolved:", log["unresolved"][:20])
print("leftover v4-* entries (uncovered by review):", leftover[:30], "count:", len(leftover))

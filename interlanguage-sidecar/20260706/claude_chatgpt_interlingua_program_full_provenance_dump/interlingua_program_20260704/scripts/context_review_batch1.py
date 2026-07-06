# Hand-adjudication batch 1 (Fable, KWIC-based) of the B2 context-review queue:
# the n>=6 band + obvious attaches. Remainder stays queued with windows.
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
BASE = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")

lex = json.loads((BASE / "data" / "proof_prose_lexicon_v2.json").read_text(encoding="utf-8"))
log = json.loads((BASE / "CONTEXT_REVIEW_ADJUDICATION_LOG_20260705.json").read_text(encoding="utf-8"))
by_id = {e["id"]: e for e in lex["entries"]}

ATTACH2 = {
    "novih": "reg-novy", "novo": "reg-novy",
    "nekoliko": "reg-několiko",
    "mogu": "reg-mogti", "moglo": "reg-mogti",
    "opět": "reg-znovu",
    "naše": "our", "našem": "our",
    "njim": "reg-njih", "njimi": "reg-njih",
    "dvěma": "reg-dva", "dvoma": "reg-dva",
    "tvoręt": "forms-constitutes",
    "sušstvovanje": "exists-eksist",
    "berut": "we-take",
    "krivu": "curve",
    "vloženo": "embed-vloziti",
    "vybira": "choose-izbrati",
    "izrečeny": "statement-izreka",
    "lahko": "reg-legko",
    "mysl": "thinks",
}

NEW2 = [
    ("strong-silny", "silny", "strong (strong prime ideal etc.)", "math_general", ["silny", "silno"]),
    ("survey-pregled", "pregled", "survey; overview", "bibliographic", ["pregled"]),
    ("diminish-umensiti", "umenšiti", "diminish; reduction (umenšenje)", "proof_operation", ["umenšenje", "umenšila"]),
    ("irreducible-nerazlozimy", "nerazložimy", "irreducible; indecomposable (NEVER attach to razložimy — polarity)", "curriculum_algebra", ["nerazlozime", "nerazložim", "nerazložimy"]),
    ("variable-varijabla", "varijabla", "variable (doublet of prěmenna)", "curriculum_algebra", ["varijablov", "varijabl"]),
    ("complete-dopolniti", "dopolniti", "complete; supplement", "proof_operation", ["dopolniti"]),
    ("fw-tri", "tri", "three (oblique forms)", "quantifier", ["tri", "treh", "trěh"]),
    ("want-hteti", "htěti", "want (I want to show...)", "discourse_predicate", ["hoču", "hočemo", "hče"]),
    ("fw-kojikoli", "kojikoli", "whichever; any", "quantifier", ["koja-koli", "kojikoli"]),
    ("adic-adicny", "adičny", "adic (p-adic register)", "noether_corpus", ["adično", "adičny"]),
    ("fw-tuto", "tuto", "this (tuta/tutu/tude forms)", "pronoun_reference", ["tuta", "tutu", "tude"]),
    ("connection-svez", "svęz", "connection (v svezi s = in connection with)", "discourse_noun", ["svez", "svezi", "svęz", "svęzi"]),
    ("cogredient-kogredientny", "kogredientny", "cogredient (classical invariant theory)", "noether_corpus", ["kogredientno", "kogredientne", "kogredientny", "kogredientnym"]),
    ("totality-vsesovokupnost", "vsesovokupnost", "totality; entirety", "math_general", ["vsesovokupnost", "vsesovokupnosti"]),
    ("fw-nejaky", "nějaky", "some kind of", "quantifier", ["nějaky"]),
    ("partition-razdelba", "razdělba", "division; partition", "math_general", ["razdělby", "razdělba"]),
    ("part-cest", "čęst", "part", "math_general", ["časti", "česti"]),
    ("mention-spomenuti", "spomenuti", "mention", "proof_reference", ["spomenuti", "spomenu"]),
    ("reach-dojti", "dojti", "come to; reach (a conclusion)", "proof_sequence", ["dojti", "dojde"]),
    ("go-idti", "idti", "go; proceed (ide o = it concerns)", "proof_predicate", ["idut", "idti"]),
    ("left-levy", "lěvy", "left (left ideal!)", "curriculum_algebra", ["lěvy", "lěvoj", "lěvogo", "lěvom", "lěvym"]),
    ("arises-vznikati", "vznikati", "arises (cs vzniká family)", "sequence_predicate", ["vznikaje", "vznika"]),
    ("quaternion", "kvaternion", "quaternion", "curriculum_algebra", ["kvaternion", "kvaternionnogo", "kvaternionov"]),
    ("in-force-sila", "sila", "force; v silě = in force / remains valid", "proof_grammar", ["sila", "sile", "silu", "silě"]),
    ("induce-inducirati", "inducirati", "induces", "proof_predicate", ["inducira", "inducirajut"]),
    ("surface-povrsina", "površina", "surface", "math_general", ["površina", "površiny"]),
    ("in-the-form-vid", "vid", "view/form (v vidě = in the form)", "proof_grammar", ["vid", "vidu", "vidě"]),
    ("entails-vlecti", "vlečti", "entails (za soboju vleče)", "proof_predicate", ["vleče"]),
    ("completion-zavrsenje", "završenje", "completion", "proof_grammar", ["završenje"]),
    ("language-nemecky", "německy", "German (language, bibliographic)", "bibliographic", ["německogo", "německy"]),
    ("greater-vecse", "věčše", "greater; more (comparative)", "comparison_marker", ["večše", "věčše"]),
    ("fw-moj", "moj", "my (oblique forms)", "pronoun_reference", ["mojej", "moj", "moje"]),
    ("fixed-fiksovany", "fiksovany", "fixed", "math_general", ["fiksovan", "fiksovany", "fiksovanom"]),
    ("always-vsegda", "vsegda", "always (incl. W doublet vždy)", "discourse_adverb", ["vsegda", "vsěgda", "vždy"]),
    ("problem-zadaca", "zadača", "problem; task", "math_general", ["zadača", "zadači", "zadaču"]),
    ("small-maly", "maly", "small", "modifier", ["maly", "mala", "malo", "malymi"]),
    ("in-fact-dejstvitelnost", "dějstvitelnost", "in reality (v dějstvitelnosti)", "discourse_adverb", ["dějstvitelnosti", "dějstvitelnost"]),
    ("permutation", "permutacija", "permutation", "curriculum_algebra", ["permutacija", "permutacije", "permutacij"]),
    ("fw-pokraj", "pokraj", "besides; alongside (hr)", "discourse_connective", ["pokraj"]),
    ("point-tocka", "točka", "point", "math_general", ["točka", "točce", "točkě", "točkah"]),
    ("nonintegral-necely", "necěly", "non-integral (own group — polarity rule)", "curriculum_algebra", ["necěly", "necěle"]),
    ("polygon-poligon", "poligon", "polygon", "math_general", ["poligon", "poligonov"]),
]

EXCLUDE2 = {
    "przez": "Polish source-language residue (quoted passage)",
    "erlangen": "place name (bibliographic)",
    "zermelovej": "eponym Zermelo (added to coverage EPONYMS)",
    "zermelovu": "eponym Zermelo",
    "klajna": "eponym Klein/Klajn (added)",
    "rocha": "eponym Roch (added)",
}

have = {v.lower() for e in lex["entries"] for v in e["variants"]}
applied = {"attach": [], "new": [], "exclude": [], "skipped": []}

for tok, tid in ATTACH2.items():
    e = by_id.get(tid)
    if not e:
        applied["skipped"].append((tok, tid, "missing group"))
        continue
    e["variants"] = sorted(set(e["variants"]) | {tok})
    e.setdefault("provenance", []).append("fable_pass27_kwic")
    e["provenance"] = sorted(set(e["provenance"]))
    have.add(tok.lower())
    applied["attach"].append((tok, tid))

for gid, lemma, en, cls, variants in NEW2:
    if gid in by_id:
        by_id[gid]["variants"] = sorted(set(by_id[gid]["variants"]) | set(variants))
        applied["attach"].append((f"{variants}", gid))
        continue
    e = {"id": gid, "lemma": lemma, "en": en, "class": cls, "variants": sorted(set(variants)),
         "provenance": ["fable_pass27_kwic"],
         "status": "proposed_internal_insert; needs linguistic review",
         "source_use": "generated_internal_consistency", "permitted_use_weight": 0.35}
    lex["entries"].append(e)
    by_id[gid] = e
    for v in variants:
        have.add(v.lower())
    applied["new"].append(gid)

for tok, why in EXCLUDE2.items():
    applied["exclude"].append((tok, why))

# rebuild remaining queue
rem = [x for x in log["B2_review"]
       if x["token"].lower() not in have and x["token"] not in EXCLUDE2 and x["token"] != "važje"]
queue = {"artifact": "context_review_queue_after_batch1", "generated": "2026-07-05",
         "note": "remaining B2 tokens with KWIC windows; adjudicate in later batches; važje kept here (window inconclusive)",
         "rows": rem + [x for x in log["B2_review"] if x["token"] == "važje"]}
(BASE / "CONTEXT_REVIEW_QUEUE_20260705.json").write_text(json.dumps(queue, ensure_ascii=False, indent=1), encoding="utf-8")

lex["artifact"] = "proof_prose_lexicon_v2_5"
lex["v2_5_note"] = ("v2.5 = v2.4 + function-word stratum (62 dict-confirmed tokens, unstoplist policy) + strict auto-attach (3) "
                    "+ Fable KWIC hand-adjudication batch 1 (n>=6 band: attaches, 43 new groups incl. left-ideal/adic/cogredient/"
                    "point/permutation math register, 4 eponyms excluded to EPONYMS, przez=residue).")
(BASE / "data" / "proof_prose_lexicon_v2.json").write_text(json.dumps(lex, ensure_ascii=False, indent=1), encoding="utf-8")
(BASE / "CONTEXT_REVIEW_BATCH1_LOG_20260705.json").write_text(json.dumps(applied, ensure_ascii=False, indent=1, default=str), encoding="utf-8")

print(f"attach2: {len(applied['attach'])} | new groups: {len(applied['new'])} | excluded: {len(applied['exclude'])} | skipped: {applied['skipped']}")
print(f"lexicon entries now: {len(lex['entries'])} | queue remaining: {len(rem)+1}")

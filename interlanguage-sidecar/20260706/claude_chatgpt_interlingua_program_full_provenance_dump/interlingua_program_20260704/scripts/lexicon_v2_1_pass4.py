# Insertion pass 4: extend proof_prose_lexicon v2 -> v2.1 with the triaged front
# (new lemma groups + variant additions to existing groups). Corpus-attested forms only.
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
BASE = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")
v2 = json.loads((BASE / "data" / "proof_prose_lexicon_v2.json").read_text(encoding="utf-8"))

NEW = [
    {"id": "lemma-noun", "lemma": "lema", "en": "lemma", "class": "proof_grammar",
     "variants": ["lema", "lemy", "lemi", "lemě", "lemou", "lemoju"]},
    {"id": "assertion", "lemma": "tvrdženje", "en": "assertion; statement", "class": "proof_grammar",
     "variants": ["tvrdženj", "tvrdzenj", "tvrđenj"]},
    {"id": "agree-consistent", "lemma": "soglasovati se", "en": "agree; be consistent (with)", "class": "proof_predicate",
     "variants": ["soglasuj", "soglaša", "soglasa"]},
    {"id": "holds-velja", "lemma": "veljati", "en": "holds; is valid (variant of važiti)", "class": "proof_predicate",
     "variants": ["velja", "veljaje"]},
    {"id": "assumption-noun", "lemma": "prědpoloženje", "en": "assumption; hypothesis", "class": "proof_grammar",
     "variants": ["prědpolož", "predpoloz", "prědpostav", "predpostav"]},
    {"id": "by-means-of", "lemma": "pomoću", "en": "by means of; with the help of", "class": "proof_connective",
     "variants": ["pomoću", "pomocju", "pomočju"]},
    {"id": "becomes", "lemma": "stati", "en": "becomes; comes to be", "class": "proof_predicate",
     "variants": ["stane", "stava", "stati", "staje"]},
    {"id": "type", "lemma": "tip", "en": "type", "class": "math_general",
     "variants": ["tipa", "tipu", "tipy", "tipov"]},
    {"id": "cf-abbrev", "lemma": "srav.", "en": "cf.; compare (abbreviation)", "class": "abbreviation",
     "variants": ["srav"]},
    {"id": "as-long-as", "lemma": "dokolě", "en": "as long as; while", "class": "proof_connective",
     "variants": ["dokolě", "dokole"]},
    {"id": "besides-pored", "lemma": "pored", "en": "besides; alongside", "class": "discourse_connective",
     "variants": ["pored"]},
    {"id": "contrary", "lemma": "protivno", "en": "conversely; to the contrary", "class": "proof_connective",
     "variants": ["protivno", "protivn"]},
    {"id": "axiom", "lemma": "aksiom", "en": "axiom", "class": "math_general",
     "variants": ["aksiom", "aksiomy", "aksiomov"]},
    {"id": "exists-eksist", "lemma": "eksistovati", "en": "exists (internationalism doublet of obstajati)", "class": "existence_predicate",
     "variants": ["eksistuj", "eksistenc"]},
    {"id": "derived-form", "lemma": "izvodny", "en": "derived (form/quantity)", "class": "noether_corpus",
     "variants": ["izvodn"]},
    {"id": "subfield", "lemma": "podtělo", "en": "subfield / sub-body", "class": "curriculum_algebra",
     "variants": ["podtěl", "podtel", "podpolj"]},
    {"id": "remark-verb", "lemma": "zamětiti", "en": "note; remark (verb)", "class": "proof_predicate",
     "variants": ["zamět", "zamet"]},
    {"id": "restrict", "lemma": "ograničiti", "en": "restrict; limit", "class": "proof_operation",
     "variants": ["ogranič", "ogranic"]},
    {"id": "set-put", "lemma": "postaviti", "en": "set; put (we set …)", "class": "proof_operation",
     "variants": ["postavim", "postavi", "polož", "poloz"]},
    {"id": "true-stvarno", "lemma": "stvarno", "en": "really; in fact", "class": "discourse_adverb",
     "variants": ["stvarno"]},
    {"id": "continuation", "lemma": "prodolženje", "en": "continuation", "class": "proof_grammar",
     "variants": ["prodolž", "prodolz"]},
    {"id": "zero-noun", "lemma": "nula", "en": "zero (noun)", "class": "math_general",
     "variants": ["nula", "nuli", "nulu", "nuly", "nulou"]},
]
ADD_VARIANTS = {
    "togda": ["tada"],                # hr/sr variant of 'then' — register, not stop
    "prvy": ["prva", "prve", "prvu"],
    "nazyvati": ["zove", "zovemo"],
    "sadržati": ["obsahuje", "sadrže"],
    "zadovoljajut": ["udovletvorja", "zadovolja"],
    "ręd": ["redy", "rědov"],
    "cěly": ["cělu", "cělo", "cěla"],
}

by_lemma_head = {e["lemma"].split()[0].split("/")[0].lower(): e for e in v2["entries"]}
added_v = 0
for head, vars_ in ADD_VARIANTS.items():
    tgt = by_lemma_head.get(head)
    if not tgt:
        for e in v2["entries"]:
            if head in [v.lower() for v in e["variants"]] or head in e["lemma"].lower():
                tgt = e
                break
    if tgt:
        before = set(tgt["variants"])
        tgt["variants"] = sorted(before | set(vars_))
        added_v += len(set(vars_) - before)

for n in NEW:
    n.update({"provenance": ["fable_pass4"], "status": "proposed_internal_insert; needs linguistic review",
              "source_use": "generated_internal_consistency", "permitted_use_weight": 0.35})
    v2["entries"].append(n)

v2["artifact"] = "proof_prose_lexicon_v2_1"
v2["entry_count"] = len(v2["entries"])
v2["pass4_note"] = f"+{len(NEW)} lemma groups, +{added_v} variants to existing groups (incl. tada->togda: hr variant of 'then' is register, not stopword)"
(BASE / "data" / "proof_prose_lexicon_v2.json").write_text(
    json.dumps(v2, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"v2.1: {len(v2['entries'])} groups (+{len(NEW)} new, +{added_v} variants)")

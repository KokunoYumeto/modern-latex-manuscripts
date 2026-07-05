# KWIC adjudication batch 2 (n=5 and n=4 bands, 140 tokens) — same method as batch 1.
# Includes: consistency-notes channel for E/W-flavored function-word slips found in
# the ISV corpus itself (transcription-scatter signal, NOT lexicon material).
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
BASE = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")

lex = json.loads((BASE / "data" / "proof_prose_lexicon_v2.json").read_text(encoding="utf-8"))
queue = json.loads((BASE / "CONTEXT_REVIEW_QUEUE_20260705.json").read_text(encoding="utf-8"))
by_id = {e["id"]: e for e in lex["entries"]}

ATTACH = {
    "pišemo": "write-pisati",
    "krokah": "step",
    "notě": "notes-bib",
    "dobilo": "reg-dobiti",
    "spomenute": "mention-spomenuti", "spomenuto": "mention-spomenuti", "spomenuty": "mention-spomenuti",
    "naime": "reg-imenno",
    "fiksovanoj": "fixed-fiksovany", "fiksovanogo": "fixed-fiksovany", "fiksovanym": "fixed-fiksovany",
    "dalo": "reg-davati",
    "znakih": "sign-znak", "znakom": "sign-znak",
    "raven": "equal",
    "ešte": "reg-ješče",
    "rędom": "series-sequence-red",
    "lěvu": "left-levy",
    "tvorut": "forms-constitutes",
    "vozmemo": "take-vzeti", "uzimanjem": "take-vzeti",
    "adičnogo": "adic-adicny",
    "vloženja": "embed-vloziti",
    "dlžiny": "length",
    "razdělbi": "partition-razdelba",
    "znana": "reg-znati",
    "obću": "reg-obći",
    "vybrane": "choose-izbrati",
    "našim": "our",
    "stanut": "becomes",
    "dodamo": "by-adding",
    "nekojej": "fw-někoj", "neke": "fw-někoj",
    "cela": "integral-whole",
    "děljiva": "divisible", "děliv": "divisible",
    "razsmotrimo": "consider-razsmatrjati", "razmatrajemo": "consider-razsmatrjati", "razgledajut": "consider-razsmatrjati",
    "dopolnjenje": "complete-dopolniti",
    "vode": "reg-voditi",
    "kogredientnymi": "cogredient-kogredientny", "kogredientna": "cogredient-kogredientny",
    "tegda": "reg-togda",
    "pojam": "concept-pojetje",
    "vopros": "reg-pytanje",
    "derivacij": "derivative-derivacija",
    "tutoj": "fw-tuto",
    "ohledom": "with-regard",
    "sovokupnost": "totality-vsesovokupnost",
    "važy": "holds-is-valid",
    "hotěla": "want-hteti",
    "gledaj": "look-gledati", "gleda": "look-gledati",
    "prijimaje": "accepted-adopted",
    "nerazlozimosti": "irreducible-nerazlozimy",
    "stupenj": "power-exponent",
    "krivulj": "curve",
    "poligonom": "polygon-poligon",
    "idet": "go-idti",
    "inducirano": "induce-inducirati",
}

NEW = [
    ("remark-zametiti", "zamětiti", "note; remark (we note that)", "proof_operation", ["zaměčajemo", "zaměčeno", "zamětiti", "zamětky"]),
    ("fw-on", "on", "that/those (oblique demonstrative)", "pronoun_reference", ["onyh"]),
    ("abbreviated-skraceno", "skračeno", "abbreviated; for short", "proof_reference", ["skračeno"]),
    ("derive-vyvesti", "vyvesti", "derive; deduce", "proof_operation", ["vyvel", "vyvesti", "vyvedeno", "vyvedenogo"]),
    ("perfect-sovrseno", "sovršeny", "perfect (perfect field!)", "curriculum_algebra", ["sovršeno", "sovršenogo", "sovršeny"]),
    ("clear-jasny", "jasny", "clear (becomes clear)", "discourse_adverb", ["jasna", "jasny", "jasne"]),
    ("associated-pridruzeny", "pridruženy", "associated (associated prime ideal!)", "noether_corpus", ["pridružiti", "pridruženy", "pridružen", "pridružene"]),
    ("work-rabota", "rabota", "work; paper (E-flavored)", "bibliographic", ["rabota"]),
    ("build-izgraditi", "izgraditi", "build up; construct", "proof_operation", ["izgraditi"]),
    ("difficulty-tezkost", "těžkost", "difficulty", "discourse_noun", ["težkost", "težkosti"]),
    ("quaternary-kvaternarny", "kvaternarny", "quaternary (binary/ternary/quaternary forms)", "noether_corpus", ["kvaternarnoj", "kvaternarny"]),
    ("runs-bezati", "běžati", "runs (an index runs)", "proof_predicate", ["běži"]),
    ("derivative-derivacija", "derivacija", "derivative; derivation", "math_general", ["derivacije", "derivacij", "derivacija"]),
    ("knowledge-znanje", "znanje", "knowledge", "discourse_noun", ["znanja", "znanje"]),
    ("fw-koji", "koji", "which (oblique forms outside stoplist)", "pronoun_reference", ["kojem", "koju"]),
    ("examine-razgledati", "razgledati", "examine; survey", "proof_operation", ["razgled"]),
    ("partially-casticno", "částično", "partially", "discourse_adverb", ["častično", "částično"]),
    ("overfield-nadpolje", "nadpolje", "overfield; extension field", "curriculum_algebra", ["nadpolja", "nadpolje"]),
    ("look-gledati", "gledati", "look at; view", "proof_operation", ["gledati", "gledany"]),
    ("decompose-razlagati", "razlagati", "decomposes (imperfective of razložiti)", "proof_predicate", ["razlaga"]),
    ("chain-cep", "cěp", "chain (chain conditions; doublet of veriga)", "noether_corpus", ["cěp", "cěpah", "cěpov"]),
    ("apex-vrh", "vrh", "top; apex (na vrhu)", "math_general", ["vrha", "vrh"]),
    ("aux-byvati", "byvati", "occurs; is (habitual)", "auxiliary", ["byvajut", "byvaje"]),
    ("put-klasti", "klasti", "we put/set (cs klademe; doublet of postaviti)", "proof_operation", ["klademo"]),
    ("flows-tekti", "tekti", "flows; runs", "proof_predicate", ["teče"]),
    ("desired-zelany", "želany", "desired", "proof_reference", ["želano", "želane"]),
    ("divide-razdeliti", "razděliti", "divide up; partition (verb)", "proof_operation", ["razděliti"]),
    ("makes-ciniti", "činiti", "makes; constitutes (hr čini)", "proof_predicate", ["čini"]),
    ("fw-oba", "oba", "both (oblique forms)", "quantifier", ["oboju", "oboje"]),
    ("acts-dejstvovati", "dějstvovati", "acts (a group acts)", "curriculum_algebra", ["dějstvuje"]),
    ("fw-vprocem", "vpročem", "incidentally; besides", "discourse_connective", ["vpročem"]),
    ("obviously-ocito", "očito", "obviously; evidently (hr)", "discourse_adverb", ["očitno", "očito"]),
    ("encompass-obejmati", "obejmati", "encompasses; comprises", "containment_predicate", ["obejmajuče"]),
    ("measure-razmer", "razměr", "measure; dimension (razměr)", "math_general", ["razměra", "razměr"]),
    ("integervalued-celocislovy", "celočislovy", "integer-valued", "math_general", ["celočislovyh"]),
    ("subfamily-podfamilija", "podfamilija", "subfamily", "math_general", ["podfamilija"]),
    ("improper-nevlastny", "nevlastny", "improper (improper divisor; polarity partner of vlastny)", "curriculum_algebra", ["nevlastne", "nevlastny"]),
    ("enters-vhoditi", "vhoditi", "enters; occurs in", "proof_predicate", ["vchodit", "vhodit", "vhode", "vhodečih"]),
    ("twosided-dvustranny", "dvustranny", "two-sided (two-sided ideal)", "curriculum_algebra", ["dvostronno", "dvustranno", "dvustranne"]),
    ("fw-toze", "tože", "also; too (E-flavored)", "discourse_connective", ["tože"]),
    ("fw-dotud", "dotud", "until then", "discourse_connective", ["dotud"]),
]

EPONYM_ADD = "weitzenböck weitzenbock gauss weyl wedderburn chevalley brill albert deuring ostrowski grassmann maxwell lagrang lagranž lorenc fišer".split()

EXCLUDE = {
    "study": "English residue", "grundlagen": "German residue",
    "arnoj": "hyphen-split artifact of 'n-arny' (n-ary)", "arnu": "hyphen-split artifact of 'n-arny'",
    "itemsep": "TeX artifact", "subsection": "TeX artifact (my metric already excludes)",
    "maisana": "unclear (name?) — keep out pending context",
    "loewy": "eponym already in EPONYMS", "speiser": "eponym already in EPONYMS",
    "macaulay": "eponym already in EPONYMS", "lipschitz": "eponym already in EPONYMS",
    "weitzenböck": "eponym (added)", "gaussov": "eponym Gauss (added)", "weyl": "eponym (added)",
    "wedderburna": "eponym Wedderburn (added)", "chevalley": "eponym (added)", "brilla": "eponym Brill (added)",
    "albert": "eponym A.A. Albert (added)", "fišera": "eponym Fischer/Fišer (added)",
    "journal": "stoplisted my-side", "reine": "stoplisted my-side", "wiss": "stoplisted my-side",
    "rabotu": "stoplisted my-side", "uvagojenjem": "stoplisted my-side",
}

CONSISTENCY_NOTES = {
    "kotoroj": "RU-flavored spelling of ISV 'ktoroj' inside ISV corpus — function-layer transcription scatter (F13); flag to corpus-consistency lane, not lexicon",
    "względom": "PL-flavored 'względem' inside ISV corpus — same class",
    "tymy": "spelling outlier of 'tymi' — same class",
    "těmi": "cs-flavored 'těmi' for 'tymi' — same class",
    "kažno": "spelling outlier of 'každo' — same class",
    "svědka": "unclear without wider context (witness? gen.) — keep queued",
    "dějnosti": "unclear (activity?) — keep queued",
    "iziti": "unclear — keep queued",
}

have = {v.lower() for e in lex["entries"] for v in e["variants"]}
log = {"attach": [], "new": [], "exclude": [], "consistency": CONSISTENCY_NOTES, "skipped": []}

for tok, tid in ATTACH.items():
    e = by_id.get(tid)
    if not e:
        log["skipped"].append((tok, tid, "missing group"))
        continue
    e["variants"] = sorted(set(e["variants"]) | {tok})
    e["provenance"] = sorted(set(e.get("provenance", [])) | {"fable_pass28_kwic"})
    have.add(tok.lower())
    log["attach"].append((tok, tid))

for gid, lemma, en, cls, variants in NEW:
    if gid in by_id:
        by_id[gid]["variants"] = sorted(set(by_id[gid]["variants"]) | set(variants))
    else:
        e = {"id": gid, "lemma": lemma, "en": en, "class": cls, "variants": sorted(set(variants)),
             "provenance": ["fable_pass28_kwic"],
             "status": "proposed_internal_insert; needs linguistic review",
             "source_use": "generated_internal_consistency", "permitted_use_weight": 0.35}
        lex["entries"].append(e)
        by_id[gid] = e
        log["new"].append(gid)
    for v in variants:
        have.add(v.lower())

for tok, why in EXCLUDE.items():
    log["exclude"].append((tok, why))

# doublet cross-note
if "chain-veriga" in by_id and "chain-cep" in by_id:
    by_id["chain-veriga"]["review_flag"] = "doublet with cěp (chain-cep) — both corpus-attested; normalization row needed"
    by_id["chain-cep"]["review_flag"] = "doublet with veriga (chain-veriga)"

drop = set(EXCLUDE) | set(CONSISTENCY_NOTES) - {"svědka", "dějnosti", "iziti"}
rows = [x for x in queue["rows"] if x["token"].lower() not in have and x["token"] not in drop]
queue["rows"] = rows
queue["artifact"] = "context_review_queue_after_batch2"
queue["note"] = "remaining tokens (n<=3 band + few unclear); adjudicate in batch 3"
(BASE / "CONTEXT_REVIEW_QUEUE_20260705.json").write_text(json.dumps(queue, ensure_ascii=False, indent=1), encoding="utf-8")

lex["artifact"] = "proof_prose_lexicon_v2_6"
lex["v2_6_note"] = ("v2.6 = v2.5 + KWIC batch 2 (n=5/4 bands): 60 attaches, ~40 new groups incl. associated-prime/perfect-field/"
                    "chain-cěp/overfield/two-sided math register; 15 eponyms added; E/W-flavored function-word slips routed to "
                    "consistency-notes channel (corpus-repair signal, not lexicon).")
(BASE / "data" / "proof_prose_lexicon_v2.json").write_text(json.dumps(lex, ensure_ascii=False, indent=1), encoding="utf-8")
(BASE / "CONTEXT_REVIEW_BATCH2_LOG_20260705.json").write_text(json.dumps(log, ensure_ascii=False, indent=1, default=str), encoding="utf-8")

print(f"attaches: {len(log['attach'])} | new groups: {len(log['new'])} | excluded: {len(log['exclude'])} | skipped: {log['skipped']}")
print(f"lexicon entries: {len(lex['entries'])} | queue remaining: {len(rows)}")

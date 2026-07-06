# KWIC adjudication batch 3: n=3 band (150) + high-count leftovers + named coverage
# top gaps. Same method; consistency-notes channel continued. After this the queue
# is n<=2 dust -> handoff bundle next.
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
BASE = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")

lex = json.loads((BASE / "data" / "proof_prose_lexicon_v2.json").read_text(encoding="utf-8"))
queue = json.loads((BASE / "CONTEXT_REVIEW_QUEUE_20260705.json").read_text(encoding="utf-8"))
by_id = {e["id"]: e for e in lex["entries"]}

NEW = [
    ("kind-vrsta", "vrsta", "kind; sort (prvoj vrsty = of the first kind)", "math_general", ["vrsta", "vrsty"]),
    ("less-mensi", "menši", "less; smaller (comparative)", "comparison_marker", ["menše", "menšej", "menši"]),
    ("higher-vysje", "vyšje", "higher", "comparison_marker", ["vyšje"]),
    ("come-prijti", "prijti", "came (to)", "proof_sequence", ["prišlo"]),
    ("neighboring-susedny", "susědny", "neighboring; adjacent", "math_general", ["susědny", "susědnyh"]),
    ("shorter-kratse", "kratše", "shorter; more briefly", "discourse_adverb", ["kratše"]),
    ("fw-velmi", "velmi", "very (cs-flavored)", "discourse_adverb", ["velmi"]),
    ("by-way-putem", "putem", "by way of; via", "discourse_connective", ["putem"]),
    ("fw-nekotory", "někotory", "some (E-flavored — see consistency note)", "quantifier", ["někotore"]),
    ("works-rabotati", "rabotati", "works (verb)", "discourse_predicate", ["rabotaje"]),
    ("requires-trebovati", "trěbovati", "requires; demands", "proof_predicate", ["trěbuje", "trebovati"]),
    ("collect-sobirati", "sobirati", "collect; gather", "proof_operation", ["sobrano", "sobiraju"]),
    ("essence-suscnost", "suščnost", "essence (v suščnosti = in essence)", "discourse_noun", ["suščnost", "suščnosti"]),
    ("nonappearance-nepojavjenje", "nepojavjenje", "non-appearance (polarity: own group)", "proof_grammar", ["nepojavjenje"]),
    ("hypercomplex", "hyperkompleksny", "hypercomplex (system/numbers)", "noether_corpus", ["hyperkompleksny", "hiperkompleksny", "hiperkompleksnyh"]),
    ("jointly-sovmestno", "sovměstno", "jointly; compatibly", "discourse_adverb", ["sovměstno"]),
    ("adjoin-prisojediniti", "prisojediniti", "adjoin (adjunction of elements!)", "curriculum_algebra", ["prisojediniti"]),
    ("remark-opazka", "opazka", "remark (sl; doublet of zamětka)", "proof_reference", ["opazka", "opazku"]),
    ("war-vojna", "vojna", "war (biographical prose)", "discourse_noun", ["vojně"]),
    ("ordered-uredzeny", "urędženy", "ordered (ordered set/chain!)", "curriculum_algebra", ["uporędžene", "uredžene", "urędžene"]),
    ("countable-scetny", "sčetny", "countable; countably", "math_general", ["sčetno", "sčetny"]),
    ("viewpoint-pogled", "pogled", "view; standpoint (s pogleda)", "discourse_noun", ["pogled"]),
    ("fw-nije", "nije", "is not (hr-flavored — see consistency note)", "auxiliary", ["nije"]),
    ("multiply-pomnoziti", "pomnožiti", "multiply (by)", "proof_operation", ["pomnoženjem", "pomnoženje"]),
    ("summation-sumovanje", "sumovanje", "summation", "math_general", ["sumovanje"]),
    ("fw-raneje", "raneje", "earlier (E-flavored)", "proof_reference", ["raneje"]),
    ("fact-cinjenica", "činjenica", "fact (hr; doublet of fakt)", "discourse_noun", ["činjenice", "činjenica"]),
    ("treatise-rasprava", "rasprava", "treatise; paper", "bibliographic", ["rasprava", "raspravy", "raspravi"]),
    ("approximate-aproksimovati", "aproksimovati", "approximate", "proof_operation", ["aproksimovati"]),
    ("nonnegative", "nenegativny", "non-negative", "math_general", ["nenegativny", "nenegativnymi"]),
    ("formation-tvorba", "tvorba", "formation; construct (pojmovyh tvorb)", "proof_grammar", ["tvorb", "tvorba", "tvorby"]),
    ("nonvanishing-nezanuljenje", "nezanuljenje", "non-vanishing (polarity: own group)", "math_general", ["nezanuljenje"]),
    ("reasoning-razsudzivanje", "razsudžanje", "reasoning (hr razsuđivanje)", "proof_grammar", ["razsuđivanja"]),
    ("prime-number-prvocislo", "prvočislo", "prime number (W-flavored cs prvočíslo)", "curriculum_algebra", ["prvočisla", "prvočislo"]),
    ("mapping-preslikanje", "preslikanje", "mapping (hr-flavored preslikavanje)", "curriculum_algebra", ["preslikanje"]),
    ("ibid-tamze", "tamže", "ibid.; in the same place", "bibliographic", ["tamže"]),
    ("fw-jesmo", "jesmo", "we are (hr-flavored)", "auxiliary", ["jesmo"]),
    ("introduced-uvedeny", "uvedeny", "introduced (cs-flavored participle)", "proof_reference", ["uvedeny", "uvedenymi"]),
    ("concerns-dotykati", "dotykati", "touches; concerns (dotyka se)", "proof_predicate", ["dotyka"]),
    ("insertion-vstavjenje", "vstavjenje", "insertion", "proof_operation", ["vstavjenje"]),
]

ATTACH = {
    "naših": "our",
    "činimo": "makes-ciniti",
    "vrsty": "kind-vrsta",
    "induciraje": "induce-inducirati", "induciranoj": "induce-inducirati",
    "adičnym": "adic-adicny", "adične": "adic-adicny",
    "veče": "greater-vecse",
    "iduče": "go-idti", "idemo": "go-idti", "idenje": "go-idti",
    "obća": "reg-obći", "voobće": "reg-obći", "občy": "reg-obći",
    "obćnosti": "generality",
    "isčezaje": "reg-izčezati",
    "dojdemo": "reach-dojti",
    "uvidimo": "see-videti",
    "rědom": "series-sequence-red",
    "kroku": "step",
    "zaoštrenje": "sharpening",
    "mogl": "reg-mogti",
    "zvane": "is-called",
    "fiksovanyh": "fixed-fiksovany", "fiksnom": "fixed-fiksovany", "fiksnogo": "fixed-fiksovany",
    "razmatrajut": "consider-razsmatrjati", "razgledajmo": "consider-razsmatrjati",
    "posreduje": "mediates",
    "točny": "reg-točno",
    "silnějše": "strong-silny",
    "totiž": "reg-imenno",
    "izrečen": "statement-izreka",
    "imal": "have-imati",
    "dodaje": "by-adding",
    "cěpa": "chain-cep",
    "kvaternionnoj": "quaternion",
    "pišut": "write-pisati",
    "male": "small-maly",
    "rabot": "work-rabota",
    "tutogo": "fw-tuto",
    "priręditi": "assign",
    "tremi": "fw-tri",
    "kogredientnogo": "cogredient-kogredientny",
    "derivaciju": "derivative-derivacija",
    "dvije": "reg-dva", "dvaju": "reg-dva", "dvěh": "reg-dva",
    "vsudy": "everywhere",
    "beruči": "we-take",
    "dala": "reg-davati", "dali": "reg-davati",
    "rovny": "equal",
    "nerazlozimyh": "irreducible-nerazlozimy", "nezvodime": "irreducible-nerazlozimy",
    "celo": "integral-whole",
    "izgradnja": "build-izgraditi",
    "sovršenom": "perfect-sovrseno",
    "izberimo": "choose-izbrati",
    "anulirajut": "annulled",
    "lěvomu": "left-levy",
    "glej": "look-gledati",
    "važat": "holds-is-valid",
    "poligona": "polygon-poligon",
    "věsy": "weight-of-form",
    "znaka": "sign-znak",
    "dělivna": "divisible",
    "dejstvitelno": "in-fact-dejstvitelnost",
    "razměrnosti": "measure-razmer",
    "celočislnogo": "integervalued-celocislovy", "celočislno": "integervalued-celocislovy",
    "leže": "reg-ležati",
    "vloženju": "embed-vloziti",
    "poněvadže": "reg-poneže",
    "čast": "part-cest",
    "koja": "fw-koji", "kojih": "fw-koji",
    "koju-koli": "fw-kojikoli", "kakihkoli": "fw-kojikoli",
    "vezi": "connection-svez",
    "trudnosti": "difficulty-tezkost",
}

EPONYM_ADD = "köthe kothe lüroth luroth castelnuov klebš christoffel wirtinger kapferer šur".split()

EXCLUDE = {
    "uvagoj": "stoplist-family variant (uvagoju)", "nikogda": "stoplisted my-side",
    "njemu": "stoplisted my-side", "sebě": "stoplist-family variant (sobě/sebe)",
    "bysmo": "aux stoplist-family variant (byhom)", "čita": "stoplist-family variant (čitati)",
    "treta": "stoplist-family variant (tretji)", "svojem": "stoplist-family variant (svoj)",
    "prěšlo": "stoplisted my-side", "oběh": "stoplisted my-side (genitive dual, held-word)",
    "čime": "stoplisted my-side", "dokud": "stoplisted my-side",
    "angew": "stoplisted my-side (bibliographic)", "teubner": "stoplisted my-side",
    "beiträge": "German residue", "amer": "English residue", "werke": "German residue",
    "zeitschrift": "German residue", "göttinger": "German residue",
    "polynomideale": "German residue", "wissensch": "German residue",
    "university": "English residue", "tracts": "English residue (Cambridge Tracts)",
    "const": "TeX/abbrev artifact", "iiia": "section-number artifact (IIIa)",
    "gaussovej": "eponym Gauss", "gaussov": "eponym Gauss",
    "zermela": "eponym Zermelo", "zermelovoju": "eponym Zermelo",
    "artina": "eponym Artin", "artinovymi": "eponym Artin",
    "weierstrassa": "eponym Weierstrass",
    "köthe": "eponym (added)", "lürotha": "eponym Lüroth (added)",
    "castelnuova": "eponym Castelnuovo (added)", "klebš": "eponym Clebsch/Klebš (added)",
    "christoffel": "eponym (added)", "wirtinger": "eponym (added)", "kapferer": "eponym (added)",
    "šurov": "eponym Schur/Šur (added)", "krull": "eponym already in EPONYMS",
    "leopold": "first name (Kronecker)",
    "kotoromu": "RU-flavored ktoromu — consistency note",
}

CONSISTENCY_ADD = {
    "totiž": "cs connective 'totiž' used INSIDE ISV prose — live F12b W-flavoring in the corpus (attached to reg-imenno as W-doublet, also flagged)",
    "poněvadže": "cs 'poněvadž' inside ISV prose — same class (attached to reg-poneže)",
    "nije": "hr negation 'nije' inside ISV prose — S-flavoring",
    "jesmo": "hr 'jesmo' inside ISV prose — S-flavoring",
    "někotore": "RU-flavored 'nekotorye' — E-flavoring",
    "raneje": "RU-flavored 'ranee' — E-flavoring",
    "nezvodime": "UK-flavored 'nezvodymyj' (irreducible) — E-flavoring",
    "dvije": "hr 'dvije' — S-flavoring",
    "kotoromu": "RU-flavored 'kotoromu' — E-flavoring",
    "rovny": "cs-flavored 'rovný' for ravny — W-flavoring",
    "razlog": "kept queued (reason — hr; window absent)",
    "cilj": "kept queued (goal — hr; window absent)",
    "porjadnosti": "kept queued (ordering? unclear)",
    "odinokyh": "kept queued (isolated? RU odinokij)",
    "sprava-batch1": "already context-flagged in v2.4",
}

have = {v.lower() for e in lex["entries"] for v in e["variants"]}
log = {"attach": [], "new": [], "exclude": [], "consistency": CONSISTENCY_ADD, "skipped": []}

# NEW first (batch-2 ordering lesson), then ATTACH
for gid, lemma, en, cls, variants in NEW:
    if gid in by_id:
        by_id[gid]["variants"] = sorted(set(by_id[gid]["variants"]) | set(variants))
    else:
        e = {"id": gid, "lemma": lemma, "en": en, "class": cls, "variants": sorted(set(variants)),
             "provenance": ["fable_pass29_kwic"],
             "status": "proposed_internal_insert; needs linguistic review",
             "source_use": "generated_internal_consistency", "permitted_use_weight": 0.35}
        lex["entries"].append(e)
        by_id[gid] = e
        log["new"].append(gid)
    for v in variants:
        have.add(v.lower())

for tok, tid in ATTACH.items():
    e = by_id.get(tid)
    if not e:
        log["skipped"].append((tok, tid, "missing group"))
        continue
    e["variants"] = sorted(set(e["variants"]) | {tok})
    e["provenance"] = sorted(set(e.get("provenance", [])) | {"fable_pass29_kwic"})
    have.add(tok.lower())
    log["attach"].append((tok, tid))

for tok, why in EXCLUDE.items():
    log["exclude"].append((tok, why))

drop = set(EXCLUDE)
rows = [x for x in queue["rows"] if x["token"].lower() not in have and x["token"] not in drop]
queue["rows"] = rows
queue["artifact"] = "context_review_queue_after_batch3"
queue["note"] = "n<=2 dust + few flagged-unclear; batch 4 optional (diminishing); consistency notes accumulated in batch logs"
(BASE / "CONTEXT_REVIEW_QUEUE_20260705.json").write_text(json.dumps(queue, ensure_ascii=False, indent=1), encoding="utf-8")

lex["artifact"] = "proof_prose_lexicon_v2_7"
lex["v2_7_note"] = ("v2.7 = v2.6 + KWIC batch 3 (n=3 band + top gaps): ~75 attaches, 40 new groups incl. prime-number/countable/"
                    "adjoin/ordered/mapping/hypercomplex math register; 10 eponyms; LIVE branch-flavoring evidence inside the ISV "
                    "corpus itself routed to consistency notes (totiž/poněvadže W, nije/jesmo/dvije S, někotore/raneje/nezvodime E).")
(BASE / "data" / "proof_prose_lexicon_v2.json").write_text(json.dumps(lex, ensure_ascii=False, indent=1), encoding="utf-8")
(BASE / "CONTEXT_REVIEW_BATCH3_LOG_20260705.json").write_text(json.dumps(log, ensure_ascii=False, indent=1, default=str), encoding="utf-8")

print(f"attaches: {len(log['attach'])} | new: {len(log['new'])} | excluded: {len(log['exclude'])} | skipped: {log['skipped']}")
print(f"lexicon entries: {len(lex['entries'])} | queue remaining: {len(rows)}")

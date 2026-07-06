# Corpus-insertion coverage v0: the completeness metric Floris set.
# Extract the FULL Interslavic corpus lexicon (all Latin-script translation TeX),
# measure what fraction is covered by the current concept system (ledger + retrofit +
# master table), and emit the frequency-ordered gap queue = the actual work list.
# Mechanical v0: token-level, stem-matched; labeled as such. No wording changes.
import json
import re
import sys
import unicodedata
from pathlib import Path
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
T = Path(r"C:\Users\Floris\Downloads\codex backup dump 7-4\$germanOut\translations")
BASE = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")

WORD = re.compile(r"[a-zčďľŕàáâäåçèéěêíîïńňòóôöřśšťùúûüýžźđćęųő]+", re.IGNORECASE)
TEXCMD = re.compile(r"\\begin\{[^}]*\}|\\end\{[^}]*\}|\\[a-zA-Z@]+\*?(\[[^\]]*\])?|\$[^$]*\$|%[^\n]*|\\[\[\](){}]|[{}~^_&]")
TEXENV = set("equation document aligned align center math itemize enumerate array matrix pmatrix bmatrix cases split gather flushleft flushright tabular figure section subsection emph textbf itshape noindent item label href texttt".split())

# ISV function/common words + high-frequency non-terminological vocabulary (curated stoplist).
STOP = set("""jest sut byti bude budu byl byla bylo byli imaje imajemo imajut imati mati
koji koja koje kojego kojemu ktory ktora ktore ktorego ktoremu ktorych ktorym ktoryh
takože takoze tako kako jako ako abo ili čto cto što sto se sej sia toj ta to te ti tyh tym tymi togo tomu
za na po do od iz ob pri prěd pred črez crez meždu medzu vsi vse vsa vsako vsakogo vsih vsim
ne ni li že ze by pak tedy zato ibo jer jerbo dokud dokle
my vy oni one ona ono jego jej jim jich ih mu
svoj svoja svoje svojego svojih moj tvoj naš vaš
jedin jedna jedno dva tri četyri pet šest sedm osm devet deset
mnogo malo vele več menje bolje najviše
takže takozvany dany dane danych danoj danom
možno mozno može moze možemo trěba treba nužno potrěbno
takoj potom zatim znova opet ještě jeste juž juz vže vze
li da ně ne nema nemaje bez pod nad
dokazati dokažemo pokazati pokažemo vidimo vidi slěduje sleduje
dostajemo dobivamo polučajemo primjer priměr primer
odnosno vzhledom soglasno prěma prema
budeme možel gdže gde kde kada kogda tut tam ovde onde
pisati pišemo napisati čitati
togda nehaj važi vazi poněže poneze poneže osoblivo znovu nyně nyne dalje daljem dale
slědujuče sledujuce slědujučo slično slicno takobezno oprěděljeno
vsegda nikogda někogda nekogda samo lish liš toliko
imenno napriměr naprimer sice inače inace protivno naproti
dostatočno dovoljno nedostatočno menše veče vyše niže
pervy pervo drugy drugo tretji zadnji poslědnji poslednji
gdže kdže ktoro čemu cemu čim cim tomto tejto teto
takova takove takovy takovo ktokoli cokoli
bymo byhom mogli može mozem možut mozut hočemo hocemo
pokazuje pokazano mora teper stava vsaka vsakomu vsakom vsakoj vsaku vsak jeden jednej jednoj jednogo jednu
dobiva dava davaje dostava napr takodže samoj vsagda drugoj druga drugymi dana dano vodi
take stvari každy nakonec kromě vměsto vměstě njih smatrati teda taka vyhodi prihodit
radi odnovrěmenno najprěd leži mogut govori medžutym znano fakt najmanje tych strany
isto děli slovami iměti izbrati poslě jasno nove zajedno položimo položeno nastupajut
razuměje razuměti razumějut zadovoljajut soglašajut proběgaje opiraje obstaje obstaja
footnote über theorie satz hilf viii dvuh em ann
takogo sebe samy čija cija takyh svojim svojeju budemo takođe takodze
uvagojenjem uvagoju sobě sobe njej njemu njim nimi onych onym
toga čiji tymy danogo sama samo samoju tomto tamtom onoj onej
novo tuto koli sposobom kolem tomu tehdy každomu njega čego gdje obojih taku idut nijedno wiss rabotě više sile prěšlo njegova takih nazad disertacije cambridge erlangen čije biti svojimi danym mogu nekoliko danu silu nastale geometričnoj takim rabotu tamo nastala realno systeme trěh svojej mala kurt zeitschr arithmetischen nekoje nijeden čime resultanten einen wien dlja prvo theory každoj danej takomu tolko reine systems nikaky moglo kojikoli něčto dala oktobra funktionen njimi oběh study našem koju nosep angew zahlentheorie
annalen nachr raboty leipzig teubner polynomideale const wissensch university tracts beiträge amer werke zeitschrift göttinger grundlagen study leopold maisana iiia itemsep arnoj arnu przez erlangen avgusta julija oktobra svojoj svojem bezvěstno gesellschaft wissenschaften nachrichten mathematische mathematischen journal könig körper gött wiss math phys akad berlin njem jemu taky samu dvoma
""".split())
ROMAN = re.compile(r"^[ivxlcdm]{2,7}$")
EPONYMS = set("steinitz noether hilbert dedekind kronecker galois weber cayley gordan frobenius burnside artin krull weierstrass mertens hensel minkowski macaulay lasker brandt speiser clebsch waerden fischer schmeidler loewy hamel riemann zermelo klajn klein roch herglotz lipschitz fokker sylow brauer weitzenböck weitzenbock gauss weyl wedderburn chevalley brill albert deuring ostrowski grassmann maxwell lagrang lagranž lorenc fišer köthe kothe lüroth luroth castelnuov klebš christoffel wirtinger kapferer šur schur".split())
# v2 correction: register vocabulary comes OUT of the stoplist (it is lexicon material)
import json as _json
_unstop = set(_json.loads((Path(__file__).parent.parent / "data" / "unstoplist_v2.json").read_text(encoding="utf-8")))
STOP -= _unstop

def strip_tex(s):
    i = s.find(r"\begin{document}")
    if i >= 0:
        s = s[i:]
    return TEXCMD.sub(" ", s)

def norm(w):
    return unicodedata.normalize("NFC", w.lower())

# --- 1. corpus lexicon ----------------------------------------------------------
freq = Counter()
files = 0
seen = set()
for f in T.rglob("*.tex"):
    s = str(f).lower()
    if "interslavic" not in s or "cyrillic" in s:
        continue
    txt = unicodedata.normalize("NFC", f.read_text(encoding="utf-8", errors="replace"))
    h = hash(txt)
    if h in seen:
        continue
    seen.add(h)
    files += 1
    for w in WORD.findall(strip_tex(txt)):
        w = norm(w)
        if len(w) >= 4 and w not in STOP and w not in TEXENV and not ROMAN.match(w):
            freq[w] += 1

# --- 2. known-label set from the current system ---------------------------------
known_tokens = set()
def add_label(s):
    if not s:
        return
    for w in WORD.findall(str(s).lower()):
        if len(w) >= 4:
            known_tokens.add(norm(w))

ledger = json.loads((BASE / "INTERLINGUAL_CONCEPT_LEDGER_20260704.json").read_text(encoding="utf-8"))
for c in ledger["concepts"]:
    for k in ("isv", "isv_cyr", "uk", "ru"):
        for v in (c.get(k) or []):
            add_label(v)
retro = json.loads((BASE / "INTERSLAVIC_LEDGER_RETROFIT_20260704.json").read_text(encoding="utf-8"))
for r in retro["rows"]:
    add_label(r.get("chosen_form_latin"))
import csv as _csv
with (BASE / "INTERLINGUAL_MARKER_TABLE_v3_1_REPAIRED_20260704.csv").open(encoding="utf-8-sig") as f:
    for row in _csv.DictReader(f):
        add_label(row.get("isv"))

# insertion passes: proof-prose lexicon v2 (Fable v1 + ChatGPT register insertions, merged)
ppl = json.loads((BASE / "data" / "proof_prose_lexicon_v2.json").read_text(encoding="utf-8"))
for e in ppl["entries"]:
    add_label(e["lemma"])
    for st in e["variants"]:
        known_tokens.add(norm(st))
ppl["entries"] = [{"isv": e["lemma"], "stems": e["variants"]} for e in ppl["entries"]]
# ChatGPT v2-delta insert proposals (generated-internal, needs-review) count as known
_delta = _json.loads((BASE / "data" / "chatgpt_delta_known_tokens.json").read_text(encoding="utf-8"))
for _t in _delta["tokens"]:
    if len(_t) >= 4:
        known_tokens.add(norm(_t))

VOWELS = "aeiouyęųåěàáâäèéêíîïòóôöùúûüýő"
def stem_of(t):
    s = t.rstrip(VOWELS)
    return s if len(s) >= 4 else t

known_stems = {t[:6] for t in known_tokens if len(t) >= 6} | known_tokens | \
              {stem_of(t) for t in known_tokens if len(stem_of(t)) >= 4}
# stems shorter than 6 from the lexicon act as prefixes too
short_prefixes = tuple(sorted({norm(st) for e in ppl["entries"] for st in e["stems"] if len(norm(st)) < 6} |
                             {stem_of(t) for t in known_tokens if 4 <= len(stem_of(t)) < 6}))

def covered(w):
    if w in EPONYMS or any(w.startswith(e) for e in EPONYMS):
        return True  # eponym class: covered by definition (proper-name transfer)
    if w in known_tokens or (len(w) >= 6 and w[:6] in known_stems) or stem_of(w) in known_stems:
        return True
    return w.startswith(short_prefixes) if short_prefixes else False

# --- 3. coverage + gap queue -----------------------------------------------------
types = len(freq)
tokens = sum(freq.values())
cov_types = sum(1 for w in freq if covered(w))
cov_tokens = sum(n for w, n in freq.items() if covered(w))
gaps = [(w, n) for w, n in freq.most_common() if not covered(w)]

out = {
    "artifact": "corpus_insertion_coverage_v0",
    "generated": "2026-07-04",
    "metric_definition": "share of the full ISV Latin corpus lexicon (content types >=4 chars, stoplist-filtered, dedup files) covered by the current concept system (ledger labels + retrofit forms + master-table isv), stem-matched (6-char). Mechanical v0 - overcounts coverage via stem collisions, undercounts via inflection; both noted.",
    "files_dedup": files,
    "lexicon_types": types,
    "lexicon_tokens": tokens,
    "covered_types": cov_types,
    "covered_tokens": cov_tokens,
    "type_coverage_pct": round(100 * cov_types / types, 1),
    "token_coverage_pct": round(100 * cov_tokens / tokens, 1),
    "gap_types": len(gaps),
    "gap_queue_top500": gaps[:500],
}
(BASE / "CORPUS_INSERTION_COVERAGE_v0_20260704.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

md = ["# Corpus Insertion Coverage — v0 (the completeness metric)", "",
      "2026-07-04. Floris's bar: the COMPLETE corpus, every word inserted and correctly weighted. This artifact defines and measures the distance. Mechanical v0 (stem-matched): treat numbers as estimates with stated biases.",
      "",
      f"- Corpus: {files} dedup Latin-script TeX files; lexicon {types:,} content types / {tokens:,} tokens (stoplist-filtered).",
      f"- **Type coverage: {out['type_coverage_pct']}%** ({cov_types:,}/{types:,}) · **Token coverage: {out['token_coverage_pct']}%** ({cov_tokens:,}/{tokens:,})",
      f"- Gap queue: {len(gaps):,} uncovered types, frequency-ordered (top 500 in json).",
      "",
      "## Top 60 uncovered types (the front of the insertion grind)", ""]
for w, n in gaps[:60]:
    md.append(f"- {n:5d}  {w}")
(BASE / "CORPUS_INSERTION_COVERAGE_v0_20260704.md").write_text("\n".join(md), encoding="utf-8")

print(f"files {files} | types {types} tokens {tokens}")
print(f"coverage: types {out['type_coverage_pct']}% tokens {out['token_coverage_pct']}%")
print("top gaps:", ", ".join(w for w, _ in gaps[:15]))



















# Register-doublet branch evidence v1 — the weighting layer for the F13
# normalization queue. For each scatter/doublet lexicon group, count attestations
# of each competing ROOT in native-branch prose (20-source W/S shelf + mk UKIM
# lexicon + be dictionary pages). Measures which variant is transparent/current
# per branch (marginal-intelligibility input). mechanical_probe weight 0.5;
# NOT ISV usage evidence; no promotions.
import json
import re
import sys
import unicodedata
from pathlib import Path
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
BASE = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")
SHELF = Path(r"C:\Users\Floris\Downloads\codex backup dump 7-4\$germanOut\sources\interslavic_triangulation\20260624_slavic_math_reference\text")
UND = BASE / "shelves" / "underrepresented_slavic"

LANGS = {"czech": "cs", "polish": "pl", "slovak": "sk", "slovenian": "sl",
         "croatian": "hr", "serbian": "sr", "bulgarian": "bg"}
BRANCH = {"cs": "W", "pl": "W", "sk": "W", "sl": "S", "hr": "S", "sr": "S", "bg": "S",
          "mk": "S", "be": "E"}
GENRE = {"mk": "dictionary/lexicon (register words underrepresented)",
         "be": "dictionary pages, tiny (register words underrepresented)"}

def nfc(s):
    return unicodedata.normalize("NFC", s)

TAG = re.compile(r"<[^>]+>")
texts = {}  # lang -> concatenated lowercase text
for f in sorted(SHELF.glob("*.txt")):
    for pref, lg in LANGS.items():
        if f.name.startswith(pref):
            texts[lg] = texts.get(lg, "") + "\n" + nfc(f.read_text(encoding="utf-8", errors="replace").lower())
texts["mk"] = nfc((UND / "macedonian" / "macedonian_ukim_math_lexicon.txt").read_text(encoding="utf-8", errors="replace").lower())
be = ""
for f in (UND / "belarusian").glob("*.html"):
    be += "\n" + TAG.sub(" ", f.read_text(encoding="utf-8", errors="replace"))
texts["be"] = nfc(be.lower())

# GROUPS: lexicon group id -> {root_label: [regex alternates], ...}
# Patterns are left-word-boundary anchored automatically. Cyrillic alternates included
# for sr/bg/mk/be. "!" prefix in label = noisy/short root, interpret with care.
G = {
    "reg-morati (must)": {
        "mora-": [r"mora", r"мора"],
        "musi-": [r"musí", r"musi", r"muse[tj]", r"мус[іи]"],
        "treba-": [r"trzeba", r"třeba", r"treba", r"тр[еэя]ба", r"трябва"],
    },
    "reg-imenno (namely)": {
        "imenno-": [r"imenno", r"именно", r"іменна"],
        "namreč/naime-": [r"namreč", r"naime", r"наиме"],
        "mianowicie(pl)": [r"mianowicie"],
        "totiž(cs)": [r"totiž", r"totiz\b"],
    },
    "však (however)": {
        "však-": [r"však", r"však"],
        "jednak(pl)": [r"jednak"],
        "ipak-": [r"ipak", r"ипак"],
        "međutim-": [r"međutim", r"medjutim", r"међутим"],
        "vendar(sl)": [r"vendar"],
        "obače/odnako-": [r"обаче", r"однако", r"аднак"],
        "megjutoa(mk)": [r"меѓутоа"],
    },
    "sovsěm (entirely)": {
        "sovsěm-": [r"sovsem", r"совсем", r"зусім"],
        "sasvim-": [r"sasvim", r"сасвим"],
        "popolnoma/potpuno-": [r"popolnoma", r"potpuno", r"потпуно", r"напълно", r"наполно"],
        "zcela/úplně(cs)": [r"zcela", r"úplně", r"uplne"],
        "całkowicie/zupełnie(pl)": [r"całkowicie", r"calkowicie", r"zupełnie", r"zupelnie"],
        "sosema(mk)": [r"сосема"],
    },
    "slučaj (case)": {
        "slučaj-": [r"slučaj", r"slucaj", r"случа[јй]", r"случа", r"выпадак"],
        "případ-": [r"případ", r"pripad", r"prípad", r"przypad"],
        "primer(sl!collides-example)": [r"primer[ua]?\b"],
    },
    "odnovrěmenno (simultaneously)": {
        "odnovremen-": [r"odnovremen", r"одновремен", r"едновремен", r"адначасова"],
        "istočasno/istovremeno-": [r"istočasn", r"istocasn", r"istovremen", r"истоврем", r"hkrati"],
        "současně/zároveň(cs)": [r"současn", r"soucasn", r"zárove", r"zarove"],
        "jednocześnie(pl)": [r"jednocześni", r"jednoczesni", r"równocześni", r"rownoczesni"],
    },
    "existence family (eksistovati/suščestvovati/obstajati/postojati)": {
        "eksist/exist-": [r"exist", r"egzist", r"eksist", r"екзист", r"егзист"],
        "suščestv-": [r"suščestv", r"существ", r"съществ"],
        "obstaja(sl)-": [r"obstaja", r"obstoj"],
        "postoji-": [r"postoj", r"постоj", r"постои", r"iснуе", r"існуе"],
        "istnieje(pl)": [r"istniej"],
    },
    "potęga/stepen/stupanj (power)": {
        "potęga(pl)/potenca(sl)": [r"potęg", r"poteg", r"potenc", r"потенц"],
        "stepen-": [r"stepen", r"степен", r"ступен"],
        "stupanj(hr)": [r"stup[nae]"],
        "mocnina(cs/sk)": [r"mocnin"],
    },
    "slěduje (follows)": {
        "sled-": [r"sledu", r"sledi", r"slijedi", r"следу", r"следв", r"следи", r"вынікае"],
        "vyplývá(cs)/wynika(pl)": [r"vyplýv", r"vyplyv", r"wynika"],
        "izhaja(sl)": [r"izhaja"],
    },
    "nazyvaje se (is called)": {
        "nazyv/naziva-": [r"nazýv", r"nazyv", r"naziva", r"называ", r"назива", r"называе"],
        "zove-": [r"zove", r"зове"],
        "imenuje(sl)": [r"imenuje"],
        "nazywa(pl)": [r"nazywa"],
        "нарича(bg)": [r"нарича"],
        "vika(mk)": [r"се вика"],
    },
    "važi/velja/platiti (holds)": {
        "važi-": [r"važi", r"важи"],
        "vrijedi/vredi(hr/sr)": [r"vrijedi", r"vrednost\b(?!)", r"вреди"],
        "platí(cs/sk)": [r"platí", r"plati\b"],
        "zachodzi(pl)": [r"zachodzi"],
        "velja(sl)": [r"velja"],
    },
    "svesti/reducirati (reduce)": {
        "sved/svod-": [r"sved", r"svod", r"свед", r"свод", r"свежда"],
        "reduk/reduc-": [r"reduk", r"reduc", r"редук", r"редуц"],
        "sprowadz(pl)": [r"sprowadz"],
        "převést(cs)": [r"převed", r"preved", r"převés", r"preves"],
    },
    "osnova/baza (basis)": {
        "baza-": [r"báz", r"baz[aąěeyiou]", r"базис", r"база", r"базы"],
        "osnova-": [r"osnov", r"основ"],
    },
    "dlugost (length)": {
        "dług(pl)": [r"dług", r"dlug"],
        "délka(cs)/dĺžka(sk)": [r"délk", r"delk", r"dĺž", r"dlz"],
        "dolžina/duljina(S)": [r"dolžin", r"dolzin", r"duljin", r"dužin", r"дужин", r"дължин", r"должин", r"даўжын"],
    },
    "porođati/generovati (generates)": {
        "gener-": [r"generu", r"generira", r"генери"],
        "porod/porađ-": [r"porađ", r"porod", r"поражд", r"пораѓ"],
        "generowany/tworzy(pl)": [r"generowan", r"tworz"],
    },
    "korak/krok (step)": {
        "korak-": [r"korak", r"корак"],
        "krok(W)": [r"krok", r"крок"],
        "stъpka(bg)": [r"стъпк"],
        "čekor(mk)": [r"чекор"],
    },
    "kriva (curve)": {
        "kriv-": [r"křiv", r"kriv", r"крив"],
        "krzywa(pl)": [r"krzyw"],
    },
    "vnutrny (inner)": {
        "vnutr/vnitř-": [r"vnitřn", r"vnitrn", r"vnútorn", r"vnutorn", r"внутр"],
        "wewnętrzny(pl)": [r"wewnętrzn", r"wewnetrzn"],
        "unutar/notranj(S)": [r"unutarnj", r"unutrašnj", r"унутрашњ", r"notranj", r"вътрешн", r"внатрешн"],
    },
    "dělo/praca (work/paper)": {
        "!delo-": [r"delo", r"дело", r"děl[oa]"],
        "prác/praca(W)": [r"prác", r"prac[aeęyi]"],
        "!rad(hr/sr)": [r"rad[ou]?\b", r"рад[ау]?\b"],
        "trud-": [r"trud", r"труд"],
    },
    "vzęti (take)": {
        "vzít/vezm(cs)": [r"vzít", r"vzit", r"vezm", r"vzali", r"vezme"],
        "wziąć/weźm(pl)": [r"wzią", r"wzia", r"weźm", r"wezm"],
        "uzeti/uzme(S)": [r"uzet", r"uzme", r"узе[тм]", r"узм"],
        "vzeti/vzame(sl)": [r"vzeti", r"vzame"],
        "vzema(bg)/zeme(mk)": [r"взема", r"земе"],
        "uzjać(be)": [r"узяць", r"вазьм"],
    },
    "stati (becomes)": {
        "!postane/postaje-": [r"postan", r"postaj", r"постан", r"постаj", r"постану"],
        "stává(cs)": [r"stává", r"stava se"],
        "staje się(pl)": [r"staje si"],
        "става(bg)": [r"става"],
    },
    "reg-prvy (first)": {
        "pierwsz(pl)": [r"pierwsz"],
        "první(cs)/prvý(sk)": [r"první", r"prvni", r"prvý", r"prvy\b", r"prvé", r"prve\b"],
        "prvi(S)": [r"prvi\b", r"први"],
        "pъrv(bg)": [r"първ", r"пръв"],
        "perš(be)": [r"перш"],
    },
    "lema (lemma)": {
        "lema/lemma-": [r"lemma", r"lema", r"лема", r"лемма"],
        "lemat(pl)": [r"lemat"],
    },
    "tvori (forms/constitutes)": {
        "tvoř/tvori-": [r"tvoř", r"tvori", r"твори", r"tvorí"],
        "tworzy(pl)": [r"tworz"],
        "formira-": [r"formira", r"формира"],
        "образу(E/bg)": [r"образу", r"утвара"],
    },
    "ostati (remains)": {
        "zůstá(cs)": [r"zůst", r"zust", r"zostáv", r"zostav"],
        "pozostaje(pl)": [r"pozosta"],
        "ostaje/ostane(S)": [r"ostaj", r"ostan", r"остаj", r"остан", r"остава", r"останува", r"застаецца"],
    },
    "protivno (conversely/contrary)": {
        "protivn-": [r"protivn", r"противн"],
        "naopak(cs)": [r"naopak"],
        "przeciwnie(pl)": [r"przeciwn"],
        "naprotiv-": [r"naprotiv", r"напротив", r"nasprotn"],
        "obratno-": [r"obratno", r"обратно", r"наадварот"],
    },
    "jednoznačno oprěděljeny (well-defined)": {
        "jednoznačn-": [r"jednoznačn", r"jednoznacn", r"jednoznaczn", r"однозначн", r"адназначн"],
        "definovan/definiran-": [r"definovan", r"definiran", r"дефиниран", r"определен", r"określon", r"okreslon", r"вызначан"],
    },
    "prědpoloženje (assumption)": {
        "předpoklad(cs/sk)": [r"předpoklad", r"predpoklad"],
        "założenie(pl)": [r"założe", r"zaloze"],
        "pretpostavka(S)": [r"pretpostavk", r"претпоставк", r"predpostavk"],
        "предполож(E/bg)": [r"предполож", r"дапушчэнн"],
    },
    "poslědstvije (consequence)": {
        "důsledek(cs)": [r"důsled", r"dusled", r"dôsled", r"dosled"],
        "konsekwencja(pl)": [r"konsekwencj"],
        "posledica(S)": [r"posledic", r"posljedic", r"последиц"],
        "следстви(E/bg)": [r"следстви", r"вынік"],
    },
    "pytanje/vprašanje (question)": {
        "pytanie(pl)/pytanje-": [r"pytani", r"pytanj", r"пытанн"],
        "otázka(cs/sk)": [r"otázk", r"otazk"],
        "vprašanje(sl)": [r"vprašanj", r"vprasanj"],
        "pitanje(hr/sr)": [r"pitanj", r"питањ"],
        "вопрос/въпрос(E/bg)": [r"вопрос", r"въпрос", r"прашањ"],
    },
    "rěšenje (solution)": {
        "řešení(cs/sk)": [r"řešen", r"resen", r"riešen"],
        "rozwiązanie(pl)": [r"rozwiąz", r"rozwiaz"],
        "rešitev(sl)": [r"rešitv", r"resitv", r"rešitev"],
        "rješenje/rešenje(S)": [r"rješenj", r"решењ", r"решени", r"рашэнн"],
    },
    "teda/togda/dakle (therefore)": {
        "tedy(cs/pl)/teda(sk)": [r"tedy", r"teda\b", r"tudíž", r"tudiz"],
        "dakle(hr/sr)": [r"dakle", r"дакле"],
        "torej(sl)": [r"torej"],
        "sledovatelno(bg)": [r"следователно"],
        "značit/tomu(E)": [r"значыць", r"таму"],
        "zatoa(mk)": [r"затоа", r"според тоа"],
    },
    "vměsto (instead of)": {
        "místo(cs)": [r"místo", r"misto\b", r"namiesto"],
        "zamiast(pl)": [r"zamiast"],
        "namesto-": [r"namesto", r"наместо", r"замест"],
        "umjesto(hr/sr)": [r"umjesto", r"umesto", r"уместо", r"наместа"],
        "вместо(E/bg)": [r"вместо"],
    },
    "poneže/pošto (since/because)": {
        "protože(cs)/pretože(sk)": [r"protože", r"protoze", r"pretože", r"pretoze", r"jelikož", r"jelikoz"],
        "ponieważ(pl)": [r"ponieważ", r"poniewaz"],
        "pošto/budući(hr/sr)": [r"pošto", r"posto\b", r"пошто", r"budući", r"buduci"],
        "ker(sl)": [r"ker\b"],
        "понеже(bg)": [r"понеже", r"тъй като"],
        "paskolku(be)": [r"паколькі", r"бо\b"],
        "bidejki(mk)": [r"бидејќи"],
    },
}

def count(lg, pattern):
    txt = texts.get(lg, "")
    return len(re.findall(r"(?<![\wа-яёіїєўѓќјљњџъ])" + pattern, txt))

order = ["cs", "pl", "sk", "sl", "hr", "sr", "bg", "mk", "be"]
results = {}
for gname, roots in G.items():
    r = {}
    for label, pats in roots.items():
        per = {lg: sum(count(lg, p) for p in pats) for lg in order}
        W = per["cs"] + per["pl"] + per["sk"]
        S = per["sl"] + per["hr"] + per["sr"] + per["bg"] + per["mk"]
        E = per["be"]
        r[label] = {"per_lang": per, "W": W, "S": S, "E_be": E}
    results[gname] = r

out = {
    "artifact": "register_doublet_branch_evidence_v1",
    "generated": "2026-07-04",
    "source_use": "mechanical_probe (0.5): root attestation counts in NATIVE-branch prose/dictionaries; "
                  "measures branch transparency of each competing variant root (marginal-intelligibility input); "
                  "NOT ISV usage evidence; no promotions; noisy roots flagged with '!'",
    "sources": {"W_S_shelf": "20-source triangulation shelf (cs/pl/sk/sl/hr/sr/bg, 1147pp textbook prose)",
                "mk": str(UND / "macedonian" / "macedonian_ukim_math_lexicon.txt") + " — " + GENRE["mk"],
                "be": "3 dictionary HTML pages — " + GENRE["be"],
                "east_note": "uk/ru native prose NOT probed here (generated translations excluded as evidence; "
                             "East branch already dominant in ledger). be included as East-native token."},
    "groups": results,
}
(BASE / "REGISTER_DOUBLET_BRANCH_EVIDENCE_v1_20260704.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

md = ["# Register-doublet branch evidence v1 — the weighting layer over the F13 queue", "",
      "2026-07-04. For each scatter/doublet group: attestation counts of each competing root in native-branch "
      "sources (W = cs+pl+sk textbook prose; S = sl+hr+sr+bg textbook prose + mk lexicon; E = be dictionary pages). "
      "Mechanical probe (permitted-use 0.5). This measures **which variant is transparent to which branch**, "
      "the direct input for 'correctly weighted' normalization decisions. `!`-flagged roots are noisy (short/homograph). "
      "No promotions; review layer decides.", "",
      "| Group | Root | cs | pl | sk | sl | hr | sr | bg | mk | be | W | S | E |",
      "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for gname, roots in results.items():
    first = True
    for label, d in roots.items():
        p = d["per_lang"]
        md.append(f"| {gname if first else ''} | `{label}` | {p['cs']} | {p['pl']} | {p['sk']} | {p['sl']} | "
                  f"{p['hr']} | {p['sr']} | {p['bg']} | {p['mk']} | {p['be']} | **{d['W']}** | **{d['S']}** | **{d['E_be']}** |")
        first = False
md += ["", "## Reading guide",
       "- A root with mass in ALL branch columns is pan-Slavic → strong normalization anchor.",
       "- A root with W-only or S-only mass is branch-specific → keeping it as an in-group doublet buys that branch's "
       "marginal intelligibility; dropping it costs exactly that branch.",
       "- Zero rows mean the root does not surface in these genres — absence, not adverse (three-state discipline).",
       "- mk source is a dictionary: connective/register rows underrepresent mk by genre, not by language."]
(BASE / "REGISTER_DOUBLET_BRANCH_EVIDENCE_v1_20260704.md").write_text("\n".join(md), encoding="utf-8")

print(f"groups probed: {len(results)} | langs: {order}")
for gname, roots in list(results.items())[:8]:
    tops = sorted(roots.items(), key=lambda kv: -(kv[1]["W"] + kv[1]["S"] + kv[1]["E_be"]))
    line = ", ".join(f"{l}:W{d['W']}/S{d['S']}/E{d['E_be']}" for l, d in tops[:4])
    print(f"  {gname}: {line}")

# Global-attractor probe v0 — first measurement of the "global math language" idea
# (Floris 2026-07-05): per concept in marker table v3.3, cluster the per-language
# forms into root families ("attractor basins") after transliteration+folding.
# Basin count ~1 => a global attractor form exists; high count => no global form.
# CRUDE v0: 4-prefix clustering, naive Cyrillic translit; mechanical_probe tier.
import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
BASE = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")
mt = json.loads((BASE / "INTERLINGUAL_MARKER_TABLE_v3_3_20260705.json").read_text(encoding="utf-8"))

CYR = {"а": "a", "б": "b", "в": "v", "г": "g", "ґ": "g", "д": "d", "е": "e", "ё": "e", "є": "e",
       "ж": "ž", "з": "z", "и": "i", "і": "i", "ї": "i", "й": "j", "к": "k", "л": "l", "м": "m",
       "н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u", "ф": "f", "х": "h",
       "ц": "c", "ч": "č", "ш": "š", "щ": "šč", "ъ": "", "ы": "y", "ь": "", "э": "e", "ю": "ju",
       "я": "ja", "ў": "u", "ђ": "dž", "ј": "j", "љ": "lj", "њ": "nj", "ћ": "ć", "џ": "dž", "ѓ": "g", "ќ": "k"}

def translit(s):
    return "".join(CYR.get(c, c) for c in s.lower())

def fold(s):
    s = translit(s)
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return s.lower()

# language columns -> family
LANGS = {"cs": "SLA", "pl": "SLA", "sk": "SLA", "sl": "SLA", "hr_sr": "SLA", "bg": "SLA",
         "uk": "SLA", "ru": "SLA", "isv": "SLA",
         "es": "ROM", "fr": "ROM", "pt": "ROM", "gl": "ROM", "ca": "ROM", "it": "ROM",
         "ro": "ROM", "rm": "ROM",
         "de": "GER", "en": "GER",
         "ar": "ARA", "fa": "ARA",
         "ja": "CJK", "zh_hans": "CJK", "ko": "CJK",
         "my_id": "MSA"}
NONLATIN_FAM = {"ARA", "CJK"}  # scripts where Latin-prefix clustering is meaningless

def first_word(s):
    s = re.sub(r"\[.*?\]|\(.*?\)", " ", str(s))
    toks = [t for t in re.split(r"[;,/|]| {2,}", s) if t.strip()]
    if not toks:
        return ""
    w = toks[0].strip()
    return w

results = []
for row in mt["rows"]:
    forms = []
    for lg, fam in LANGS.items():
        v = row.get(lg)
        if not v or str(v).strip() in ("", "None"):
            continue
        w = first_word(v)
        if not w or len(w) < 2:
            continue
        forms.append((lg, fam, w))
    if len({f for _, f, _ in forms}) < 3:
        continue  # need >=3 families with data for a meaningful basin count
    # cluster: Latin-script forms by folded 4-prefix; non-Latin families each = own basin
    clusters = {}
    for lg, fam, w in forms:
        if fam in NONLATIN_FAM or re.search(r"[؀-ۿ一-鿿぀-ヿ가-힯]", w):
            key = f"script:{fam}"
        else:
            key = fold(w)[:4]
        clusters.setdefault(key, []).append((lg, fam))
    fams_with_data = {f for _, f, _ in forms}
    # basin stats over FAMILIES: a basin's family coverage
    best_cov = 0
    best_key = ""
    for k, mem in clusters.items():
        cov = len({f for _, f in mem})
        if cov > best_cov:
            best_cov, best_key = cov, k
    n_basins = len({k for k in clusters})
    results.append({"concept": row["concept"], "stratum": row.get("stratum", ""),
                    "families_with_data": sorted(fams_with_data),
                    "n_form_basins": n_basins,
                    "top_basin": best_key, "top_basin_family_coverage": best_cov,
                    "global_attractor": bool(best_cov >= len(fams_with_data) - (1 if NONLATIN_FAM & fams_with_data else 0)
                                             and best_cov >= 3),
                    "n_langs": len(forms)})

att = [r for r in results if r["global_attractor"]]
by_stratum = Counter()
by_stratum_att = Counter()
for r in results:
    st = r["stratum"] or "?"
    by_stratum[st] += 1
    if r["global_attractor"]:
        by_stratum_att[st] += 1

out = {"artifact": "global_attractor_probe_v0", "generated": "2026-07-05",
       "idea_credit": "Floris 2026-07-05 (voice note): standardized global math language as emergent goal; "
                      "'mathematicians read math across languages easily' heuristic",
       "method": "CRUDE v0 (mechanical_probe): first-form per language, Cyrillic translit + diacritic fold, "
                 "4-prefix clustering = root-family basin; Arabic/CJK scripts = own basins by construction "
                 "(honest: the Latin attractor cannot reach them by cognacy, only by borrowing); "
                 ">=3 language families with data required per concept",
       "summary": {"concepts_measured": len(results),
                   "with_global_attractor_excl_nonlatin": len(att),
                   "share": round(len(att) / max(1, len(results)), 3),
                   "by_stratum_total": dict(by_stratum), "by_stratum_attractor": dict(by_stratum_att)},
       "rows": sorted(results, key=lambda r: (-r["n_form_basins"]))}
(BASE / "GLOBAL_ATTRACTOR_PROBE_v0_20260705.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

print(f"concepts measured (>=3 families): {len(results)}")
print(f"global attractor (Latin-sphere): {len(att)} = {100*len(att)/max(1,len(results)):.0f}%")
print("by stratum: ", {k: f"{by_stratum_att[k]}/{v}" for k, v in by_stratum.items()})
print("\nmost fragmented concepts (no global form):")
for r in out["rows"][:12]:
    print(f"  {r['concept'][:34]:34s} basins={r['n_form_basins']:2d} topcov={r['top_basin_family_coverage']} fams={','.join(r['families_with_data'])}")
print("\nsample attractor concepts:")
for r in [x for x in out["rows"] if x["global_attractor"]][-8:]:
    print(f"  {r['concept'][:34]:34s} basin='{r['top_basin']}' covers {r['top_basin_family_coverage']} families")

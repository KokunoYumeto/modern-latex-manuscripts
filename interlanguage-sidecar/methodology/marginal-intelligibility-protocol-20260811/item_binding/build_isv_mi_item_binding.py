#!/usr/bin/env python3
"""Build the bounded, non-adjudicative ISV marginal-intelligibility item binding.

This script reads pinned evidence and writes only beside itself.  It deliberately
does not construct participant prose, choose a winner, or claim native/community
validation.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path


HERE = Path(__file__).resolve().parent
IL = Path(r"C:\Users\user\Documents\interlanguage")
LANE = IL / "03_projects/language_management/slavic_interslavic"
NOETHER = IL / "03_projects/noether"
FABLE = Path(r"C:\Users\user\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")
PILOT = HERE.parent
V018 = LANE / "noether_slavic_v018/release"
BASE = V018 / "source/base-papers1-43-isv.tex"
GERMAN = NOETHER / "07_german_canon_control/candidates/ED0011/noether.tex"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest().upper()


def sha_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest().upper()


SOURCE_DEFS = [
    ("SRC-PROTOCOL", PILOT / "ISV_MARGINAL_INTELLIGIBILITY_PILOT_PROTOCOL.json", "frozen pilot protocol"),
    ("SRC-TREE", PILOT / "ISV_SYMMETRIC_FAMILY_COHORT_TREE.json", "declared family/cohort tree"),
    ("SRC-TYPED-GRAPH", NOETHER / "03_translation_workspaces/slavic_r823_book_reconciliation_20260717/evidence/TYPED_EVIDENCE_GRAPH.json", "typed provenance/routing graph"),
    ("SRC-R823-TERM", NOETHER / "03_translation_workspaces/slavic_r823_book_reconciliation_20260717/evidence/TERMINOLOGY_LEDGER.csv", "stale R823 terminology control retained as adverse evidence"),
    ("SRC-FABLE-R1", FABLE / "NORMALIZATION_DECISIONS_R1_DRAFT_v1_20260705.json", "Fable normalization decision draft"),
    ("SRC-FABLE-TABLE", FABLE / "NORMALIZATION_DECISION_TABLE_v1_20260704.json", "Fable decision table"),
    ("SRC-FABLE-BRANCH", FABLE / "REGISTER_DOUBLET_BRANCH_EVIDENCE_v2_20260704.json", "West/South/East branch evidence"),
    ("SRC-F10", FABLE / "F10_EAST_SLAVIC_SKEW_AUDIT_20260704.json", "East-skew audit"),
    ("SRC-RETROFIT", FABLE / "INTERSLAVIC_LEDGER_RETROFIT_20260704.json", "Interslavic concept/word-web retrofit"),
    ("SRC-CONCEPT-WEB", FABLE / "INTERLINGUAL_CONCEPT_LEDGER_20260704.json", "interlingual concept web"),
    ("SRC-FABLE-LOGBOOK", FABLE / "frozen/ORIGINATING_SESSION_INTERSLAVIC_LOGBOOK.md", "originating-session logbook"),
    ("SRC-OFFICIAL-ISV", FABLE / "data/isv_words_list.csv", "official-ISV dictionary export used by Fable"),
    ("SRC-V018-BASE", BASE, "current v018 Latin ISV Papers 1-43"),
    ("SRC-V018-BOOK", V018 / "source/44-book-isv.tex", "current v018 Latin ISV book component"),
    ("SRC-V018-P45", V018 / "source/45-isv.tex", "current v018 Latin ISV Paper 45"),
    ("SRC-V018-BIB", V018 / "source/bib-isv.tex", "current v018 Latin ISV bibliography"),
    ("SRC-GERMAN-ED0011", GERMAN, "German authority body against which v018 was assembled"),
    ("SRC-ASSEMBLY", V018 / "evidence/source_assembly.json", "v018 source assembly and authority lineage"),
    ("SRC-NORM-CROSSWALK", LANE / "00_lane_control/isv_normalization_20260811/ISV_NORMALIZATION_CROSSWALK.json", "current normalization crosswalk"),
    ("SRC-NORM-AUDIT", LANE / "normalization_20260718/final_audit_20260718/NORMALIZATION_STATUS_AUDIT_FINAL.json", "normalization final audit"),
    ("SRC-CHANGE-LEX", LANE / "normalization_20260718/tranche_002b_lexical_exact/evidence/CHANGE_LEDGER.csv", "positive-control lexical change ledger"),
    ("SRC-CHANGE-CORR", LANE / "normalization_20260718/tranche_003_correspondence/evidence/CHANGE_LEDGER.csv", "correspondence change ledger"),
    ("SRC-CHANGE-SIM", LANE / "normalization_20260718/tranche_004_simultaneity/evidence/CHANGE_LEDGER.csv", "simultaneity change ledger"),
    ("SRC-RING-REVIEW", LANE / "normalization_20260718/tranche_006_ring_competitor/evidence/LARGE_HELD_FAMILY_REVIEW_20260718.md", "held-family review including ring/ręd/jednako/važiti"),
]


def source_pins() -> list[dict]:
    pins = []
    for source_id, path, role in SOURCE_DEFS:
        if not path.is_file():
            raise FileNotFoundError(f"missing required evidence: {path}")
        pins.append({
            "source_id": source_id,
            "absolute_path": str(path),
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
            "role": role,
        })
    return pins


BASE_LINES = BASE.read_text(encoding="utf-8").splitlines()
GERMAN_LINES = GERMAN.read_text(encoding="utf-8").splitlines()


def german_paper_ranges() -> dict[int, dict]:
    starts: dict[int, int] = {}
    patterns = [
        re.compile(r"^\{\\Large\\bfseries\s+(\d+)\."),
        re.compile(r"^\\section\*\{(\d+)\.\s"),
    ]
    for number, line in enumerate(GERMAN_LINES, 1):
        for pat in patterns:
            match = pat.search(line)
            if match:
                paper = int(match.group(1))
                starts[paper] = min(number, starts.get(paper, number))
                break
        # Paper 19's retained source title does not carry its anthology number.
        if "{\\Large\\bfseries Idealtheorie in Ringbereichen.}" in line:
            starts[19] = min(number, starts.get(19, number))
    ordered = sorted(starts.items(), key=lambda item: item[1])
    ranges = {}
    for index, (paper, start) in enumerate(ordered):
        end = (ordered[index + 1][1] - 1) if index + 1 < len(ordered) else len(GERMAN_LINES)
        normalized = "\n".join(GERMAN_LINES[start - 1:end]) + "\n"
        ranges[paper] = {
            "paper_id": f"P{paper:02d}",
            "line_start": start,
            "line_end": end,
            "range_sha256_utf8_lf": sha_text(normalized),
            "precision": "exact_paper_range; exact sentence alignment not yet frozen",
        }
    return ranges


GERMAN_RANGES = german_paper_ranges()


def target_context(context_id: str, line_number: int, surface: str, kind: str) -> dict:
    if line_number < 1 or line_number > len(BASE_LINES):
        raise ValueError(f"bad line {line_number}")
    line = BASE_LINES[line_number - 1]
    if surface not in line:
        raise ValueError(f"surface {surface!r} absent at current v018 line {line_number}")
    source_line = None
    source_path = None
    for idx in range(line_number - 1, -1, -1):
        if BASE_LINES[idx].startswith("% Source: "):
            source_line = idx + 1
            source_path = BASE_LINES[idx][len("% Source: "):]
            break
    if not source_path:
        raise ValueError(f"no producer source locator before {line_number}")
    paper_match = re.search(r"paper(\d+)", source_path, re.IGNORECASE)
    if not paper_match:
        raise ValueError(f"no paper number in source path {source_path}")
    paper = int(paper_match.group(1))
    if paper not in GERMAN_RANGES:
        raise ValueError(f"German paper range missing for P{paper:02d}")
    producer = Path(source_path)
    return {
        "context_id": context_id,
        "context_kind": kind,
        "controlled_occurrence_surface": surface,
        "target_locator": {
            "source_id": "SRC-V018-BASE",
            "line": line_number,
            "line_sha256_utf8": sha_text(line),
            "producer_declaration_line": source_line,
            "producer_source_path": source_path,
            "producer_source_exists": producer.is_file(),
            "producer_source_sha256": sha256(producer) if producer.is_file() else None,
            "structural_unit": f"P{paper:02d}",
        },
        "german_authority_locator": {"source_id": "SRC-GERMAN-ED0011", **GERMAN_RANGES[paper]},
        "alignment_state": "target_occurrence_exact; German paper range exact; sentence-level German alignment held",
    }


ROLE_ORDER = [
    "exact_current_v018",
    "official_isv",
    "dominant_east_baseline",
    "branch_balanced_candidate",
    "native_control",
]


FAMILY_SPECS = [
    {
        "family_id": "MI-FAM-01", "family_class": "contested_technical", "concept_id": "ALGEBRA.RING",
        "sense_id": "algebra.ring.abstract_binary_operations", "label": "ring / kolco-prsten",
        "contexts": [(12451, "kolco", "definition_or_formula"), (12423, "kolceve", "running_prose")],
        "forms_regex": r"\bkolc\w*", "decision_key": "ring", "branch_key": "ring/kolco-prsten",
        "current": ["kolco"], "official": ["koljce", "pŕstėnj"], "east": ["kolco"],
        "west": ["prsten"], "south": ["prsten"], "balanced": ["kolco", "prsten"],
        "official_reason": "Official dictionary has only physical-ring entries koljce/pŕstėnj; no pinned algebraic sense.",
        "special_adverse": "Official physical-ring forms cannot be promoted to algebraic ring; typed graph holds kolco/prsten.",
    },
    {
        "family_id": "MI-FAM-02", "family_class": "contested_technical", "concept_id": "ALGEBRA.QUOTIENT_FIELD",
        "sense_id": "algebra.field_of_fractions.of_integral_domain", "label": "quotient field / kvocientno polje",
        "contexts": [(8349, "kvocientno polje", "definition_or_formula"), (8355, "kvocientno polje", "running_prose")],
        "forms_regex": r"\bkvocientn\w*\s+polj\w*", "decision_key": "quotient-field", "branch_key": "quotient field",
        "current": ["kvocientno polje"], "official": ["polje"], "east": [],
        "west": [], "south": [], "balanced": [],
        "official_reason": "Official polje is pinned only as generic field; kvocient technical compound is not attested there.",
        "special_adverse": "Generic field dictionary evidence does not establish the algebraic field-of-fractions compound.",
    },
    {
        "family_id": "MI-FAM-03", "family_class": "contested_technical", "concept_id": "INVARIANT_THEORY.FORM_SERIES",
        "sense_id": "invariant_theory.form_series.sequence_not_rank_or_row", "label": "ręd / series-sequence",
        "contexts": [(100, "rędom form", "definition_or_formula"), (69, "ręd modulov", "running_prose")],
        "forms_regex": r"\br[ęěe]d\w*", "decision_key": "series-sequence-red", "branch_key": "ręd (series/sequence)",
        "current": ["ręd"], "official": ["ręd"], "east": ["ręd"],
        "west": ["řada", "szereg"], "south": ["niz", "zaporedje"], "balanced": ["ręd", "řada", "szereg", "niz", "zaporedje"],
        "official_reason": "Official ręd has several senses; exact series/sequence sense must be isolated from order/row.",
        "special_adverse": "High-divergence four-way West/South split and South/East order homographs forbid lemma-only scoring.",
    },
    {
        "family_id": "MI-FAM-04", "family_class": "contested_technical", "concept_id": "ALGEBRA.DIVISION_RING",
        "sense_id": "algebra.noncommutative_division_ring.body_term", "label": "division ring / tělo",
        "contexts": [(19289, "nekomutativnogo těla", "definition_or_formula"), (19658, "komutativnom tělu", "running_prose")],
        "forms_regex": r"\btěl\w*", "decision_key": "body-telo-infl", "branch_key": "tělo (body/division ring)",
        "current": ["tělo"], "official": ["tělo"], "east": [],
        "west": ["těleso", "ciało"], "south": ["tijelo", "telo", "tjalo"], "balanced": ["tělo", "těleso", "ciało", "tijelo", "telo", "tjalo"],
        "official_reason": "Official tělo is body only; no pinned division-ring sense in the dictionary row.",
        "special_adverse": "Technical body/division-ring sense is authority-sensitive and Polish is an explicit branch outlier.",
    },
    {
        "family_id": "MI-FAM-05", "family_class": "proof_connective_or_predicate", "concept_id": "DISCOURSE.HOWEVER",
        "sense_id": "discourse.concessive.however_not_equal_or_simultaneous", "label": "jednako / however",
        "contexts": [(9811, "jednako može", "running_prose"), (10076, "jednako dajut", "running_prose")],
        "forms_regex": r"\bjednako(?:že)?\b", "decision_key": "however", "branch_key": "však (however)",
        "current": ["jednako"], "official": ["jednako", "jednakože"], "east": ["odnako"],
        "west": ["však", "jednak"], "south": ["ipak", "vendar", "međutim"], "balanced": ["však", "jednak", "ipak", "vendar", "međutim"],
        "official_reason": "Official concessive entry exists, but exact German sentence alignment and formula/definition context remain unfrozen.",
        "special_adverse": "Croatian/Serbian jednak means equal; current contexts may also conceal German zugleich, so sense alignment is held.",
    },
    {
        "family_id": "MI-FAM-06", "family_class": "proof_connective_or_predicate", "concept_id": "PROOF.HOLDS_VALID",
        "sense_id": "proof.predicate.holds_or_is_valid", "label": "važiti / holds",
        "contexts": [(1041, "ima važiti", "definition_or_formula"), (1174, "To samo važi", "running_prose")],
        "forms_regex": r"\bvaž\w*", "decision_key": "holds-is-valid", "branch_key": "važi/velja/platiti (holds)",
        "current": ["važiti", "važi"], "official": [], "east": [],
        "west": ["platí", "zachodzi"], "south": ["vrijedi", "vredi", "velja"], "balanced": ["platí", "zachodzi", "vrijedi", "vredi", "velja"],
        "official_reason": "Official važiti row means weigh/balance, not mathematical holds; technical arm absent.",
        "special_adverse": "Current važi is unattested in the probed W/S corpus while official sense points elsewhere.",
    },
    {
        "family_id": "MI-FAM-07", "family_class": "proof_connective_or_predicate", "concept_id": "DISCOURSE.NAMELY",
        "sense_id": "discourse.specification.namely", "label": "imenno / namely West-South split",
        "contexts": [(847, "imenno od svijanj", "definition_or_formula"), (1061, "imenno 1)", "running_prose")],
        "forms_regex": r"\bimenno\b", "decision_key": "reg-imenno", "branch_key": "reg-imenno (namely)",
        "current": ["imenno"], "official": ["imenno"], "east": ["imenno"],
        "west": ["totiž", "mianowicie"], "south": ["namreč", "naime"], "balanced": ["totiž", "mianowicie", "namreč", "naime"],
        "official_reason": "Official imenno exists, while Fable prose counts make it East-only in the tested branch corpus.",
        "special_adverse": "No single W/S attractor: West and South competitor families split and Polish is undercounted in the probe.",
    },
    {
        "family_id": "MI-FAM-08", "family_class": "proof_connective_or_predicate", "concept_id": "PROOF.FOLLOWS_FROM",
        "sense_id": "proof.inference.follows_from_not_physical_follow", "label": "slěduje / follows-from West-South split",
        "contexts": [(560, "Iz togo slěduje", "definition_or_formula"), (63, "dokaza konečnosti sistemov form slěduje", "running_prose")],
        "forms_regex": r"\bslěduj\w*", "decision_key": "follows-from", "branch_key": "slěduje (follows)",
        "current": ["slěduje"], "official": ["slědovati"], "east": ["slěduje"],
        "west": ["vyplývá", "wynika"], "south": ["sled-", "izhaja"], "balanced": ["vyplývá", "wynika", "slěduje", "izhaja"],
        "official_reason": "Official slědovati means follow generally; inferential follows-from requires a controlled sense context.",
        "special_adverse": "West vyplývá/wynika and South sled-/izhaja evidence split; physical-follow readings must be excluded.",
    },
    {
        "family_id": "MI-FAM-09", "family_class": "positive_control", "concept_id": "LOGIC.SIMULTANEOUSLY",
        "sense_id": "temporal.simultaneously", "label": "jednočasno positive control",
        "contexts": [(98, "jednočasno isčezajut", "definition_or_formula"), (1514, "jednočasno naležet", "running_prose")],
        "forms_regex": r"\bjednočas\w*", "decision_key": "simultaneously", "branch_key": "odnovrěmenno (simultaneously)",
        "current": ["jednočasno"], "official": ["jednočasno", "jednovrěmenno"], "east": ["odnovrěmenno"],
        "west": ["současně", "jednocześnie"], "south": ["istočasno", "istovremeno"], "balanced": ["jednočasno", "istočasno", "současně", "jednocześnie"],
        "official_reason": "Both jednočasno and jednovrěmenno are official; current execution does not prove optimality.",
        "special_adverse": "R823 labels are stale and five old simultaneous-family tokens remain in exact current v018 bytes.",
    },
    {
        "family_id": "MI-FAM-10", "family_class": "positive_control", "concept_id": "RELATION.CORRESPONDS",
        "sense_id": "relation.corresponds_or_is_equivalent_not_answers", "label": "odpovědati positive control",
        "contexts": [(1861, "odpovědaje relacija", "definition_or_formula"), (570, "odpovědajučego člena", "running_prose")],
        "forms_regex": r"\bodpověd\w*", "decision_key": "corresponds", "branch_key": "sootvětstvovati (corresponds)",
        "current": ["odpovědati"], "official": ["odpovědati"], "east": ["sootvětstvovati"],
        "west": ["odpovídá", "odpowiada"], "south": ["odgovara", "ustreza"], "balanced": ["odpovědati", "odgovarati", "ustrezati"],
        "official_reason": "Official dictionary separates answer/reply from correspond/equivalent; only the latter sense is eligible.",
        "special_adverse": "R823 labels are stale and eighteen soot- correspondence tokens remain in exact current v018 bytes.",
    },
    {
        "family_id": "MI-FAM-11", "family_class": "positive_control", "concept_id": "PROOF.STEP",
        "sense_id": "proof.procedural_step_not_gait", "label": "krok positive control",
        "contexts": [(5753, "jedinom kroku", "definition_or_formula"), (10534, "mnogih krokah", "running_prose")],
        "forms_regex": r"\bkrok\w*", "decision_key": "step", "branch_key": "korak/krok (step)",
        "current": ["krok"], "official": ["krok"], "east": ["šag"],
        "west": ["krok"], "south": ["korak", "stųpka", "čekor"], "balanced": ["krok", "korak", "stųpka", "čekor"],
        "official_reason": "Official krok is step; procedural mathematical sense remains the controlled sub-sense.",
        "special_adverse": "R823 labels are stale and one korakov residual remains in exact current v018 bytes.",
    },
    {
        "family_id": "MI-FAM-12", "family_class": "false_friend_or_trap_control", "concept_id": "COMPARISON.EQUAL",
        "sense_id": "comparison.equal_or_same_not_concessive_however", "label": "jednak equal vs however trap",
        "contexts": [(1051, "jednakogo poręda", "definition_or_formula"), (12925, "jednako često", "running_prose")],
        "forms_regex": r"\bjednak\w*", "decision_key": "however", "branch_key": "však (however)",
        "current": ["jednaky", "jednakogo", "jednako"], "official": ["jednaky"], "east": ["jednakovy"],
        "west": ["jednaky", "stejný", "rovnaký"], "south": ["enak", "jednak", "isti"], "balanced": ["jednaky", "stejný", "rovnaký", "enak", "jednak", "isti"],
        "official_reason": "Official jednaky=same is distinct from official jednako=however; context controls must keep them separate.",
        "special_adverse": "Croatian/Serbian jednak=equal creates a false pan-Slavic signal for Polish jednak=however.",
    },
]


LATIN_COMPONENTS = [
    V018 / "source/base-papers1-43-isv.tex",
    V018 / "source/44-book-isv.tex",
    V018 / "source/45-isv.tex",
    V018 / "source/bib-isv.tex",
]


def corpus_inventory(pattern: str) -> dict:
    regex = re.compile(pattern, re.IGNORECASE | re.UNICODE)
    forms: dict[str, int] = {}
    total = 0
    for path in LATIN_COMPONENTS:
        text = path.read_text(encoding="utf-8")
        for match in regex.finditer(text):
            value = match.group(0)
            forms[value] = forms.get(value, 0) + 1
            total += 1
    return {"pattern": pattern, "total": total, "forms": dict(sorted(forms.items(), key=lambda item: (item[0].casefold(), item[0])))}


def residual_evidence() -> dict:
    specs = {
        "simultaneous_pre_switch": {"lines": [5189, 11297, 15652, 15654, 15698], "pattern": r"\bodnov\w*", "expected": 5},
        "correspondence_pre_switch": {"lines": [15434, 15436, 15459, 15469, 15498, 15581, 15602], "pattern": r"\bsoot(?:vět|vęt)stv\w*", "expected": 18},
        "step_pre_switch": {"lines": [15323], "pattern": r"\bkorak\w*", "expected": 1},
    }
    result = {}
    for key, spec in specs.items():
        regex = re.compile(spec["pattern"], re.IGNORECASE | re.UNICODE)
        locators = []
        count = 0
        for line_number in spec["lines"]:
            line = BASE_LINES[line_number - 1]
            forms = regex.findall(line)
            count += len(forms)
            locators.append({"source_id": "SRC-V018-BASE", "line": line_number, "line_sha256_utf8": sha_text(line), "forms": forms})
        if count != spec["expected"]:
            raise ValueError(f"residual count mismatch for {key}: {count} != {spec['expected']}")
        result[key] = {"count": count, "locators": locators, "interpretation": "adverse residue; no acceptance or mutation inferred"}
    return result


def make_arm(role: str, spec: dict) -> dict:
    if role == "exact_current_v018":
        return {
            "role": role,
            "surface_candidates": spec["current"],
            "availability": "lexical_surface_and_exact_target_contexts_pinned; participant_passage_held",
            "absent_or_held_reason": "Exact German sentence alignment and coherent same-information passage have not been frozen.",
        }
    if role == "official_isv":
        return {
            "role": role,
            "surface_candidates": spec["official"],
            "availability": "lexical_authority_pinned; participant_passage_held" if spec["official"] else "absent_for_controlled_sense",
            "absent_or_held_reason": spec["official_reason"],
        }
    if role == "dominant_east_baseline":
        if not spec["east"]:
            return {
                "role": role,
                "surface_candidates": [],
                "availability": "absent_from_pinned_evidence",
                "absent_or_held_reason": "The pinned evidence does not license an exact controlled-sense dominant-East comparator surface.",
            }
        return {
            "role": role,
            "surface_candidates": spec["east"],
            "availability": "historical_or_branch_lexeme_family_pinned; participant_passage_held",
            "absent_or_held_reason": "No source-audited, morphology-complete matched passage is frozen; East baseline is a comparator, not a default.",
        }
    if role == "branch_balanced_candidate":
        if not spec["balanced"]:
            return {
                "role": role,
                "surface_candidates": [],
                "availability": "absent_from_pinned_evidence",
                "absent_or_held_reason": "The pinned branch evidence does not license a branch-balanced controlled-sense candidate set.",
            }
        return {
            "role": role,
            "surface_candidates": spec["balanced"],
            "availability": "candidate_set_pinned_without_choice; participant_passage_held",
            "absent_or_held_reason": "A branch-balanced set is not a token-by-token mosaic and no coherent global arm has been source-licensed.",
        }
    return {
        "role": role,
        "surface_candidates": [],
        "availability": "absent_requires_qualified_native_source",
        "absent_or_held_reason": "Zero native-speaker item authoring or review records exist; model prose cannot substitute.",
    }


def evidence_records(spec: dict) -> tuple[list[dict], dict]:
    fid = spec["family_id"]
    common = [
        {
            "evidence_id": f"EV-{fid}-CURRENT", "edge_type": "support", "fact_class": "source_fact",
            "source_ids": ["SRC-V018-BASE", "SRC-ASSEMBLY"],
            "locator": "family.contexts[] plus current corpus inventory",
            "claim": "Exact current target occurrences and current assembly lineage are pinned.",
        },
        {
            "evidence_id": f"EV-{fid}-OFFICIAL", "edge_type": "support", "fact_class": "source_fact",
            "source_ids": ["SRC-OFFICIAL-ISV"],
            "locator": f"dictionary search for {spec['official'] or spec['current']}",
            "claim": spec["official_reason"],
        },
        {
            "evidence_id": f"EV-{fid}-COMPETITOR", "edge_type": "competitor", "fact_class": "computation",
            "source_ids": ["SRC-FABLE-TABLE", "SRC-FABLE-BRANCH", "SRC-RETROFIT", "SRC-CONCEPT-WEB"],
            "locator": f"decision_key={spec['decision_key']}; branch_group={spec['branch_key']}",
            "claim": "Branch competitors are evidence inputs; they do not select a final arm.",
        },
        {
            "evidence_id": f"EV-{fid}-ADVERSE", "edge_type": "adverse", "fact_class": "source_fact_and_computation",
            "source_ids": ["SRC-F10", "SRC-FABLE-R1", "SRC-R823-TERM", "SRC-FABLE-LOGBOOK"],
            "locator": f"family={fid}; sense={spec['sense_id']}",
            "claim": spec["special_adverse"],
        },
        {
            "evidence_id": f"EV-{fid}-ABSENCE", "edge_type": "absence", "fact_class": "computation",
            "source_ids": ["SRC-PROTOCOL", "SRC-OFFICIAL-ISV"],
            "locator": f"arms[{fid}].availability and protocol hard gates",
            "claim": "Unavailable passage/native/sense-qualified arms remain explicitly absent or held.",
        },
        {
            "evidence_id": f"EV-{fid}-VETO", "edge_type": "veto", "fact_class": "editorial_inference",
            "source_ids": ["SRC-PROTOCOL", "SRC-TYPED-GRAPH", "SRC-TREE"],
            "locator": "no-token-mosaic rule; declared family tree; typed graph holds",
            "claim": "No scalar auto-decision, token mosaic, final choice, certification, or community approval is licensed.",
        },
    ]
    edges = {kind: [f"EV-{fid}-{kind.upper()}"] for kind in ["support", "competitor", "adverse", "absence", "veto"]}
    # Support has two independent pins.
    edges["support"] = [f"EV-{fid}-CURRENT", f"EV-{fid}-OFFICIAL"]
    return common, edges


def branch_records(spec: dict) -> list[dict]:
    # These surfaces are candidate evidence summaries from the pinned Fable table,
    # not native judgements and not participant arms.
    records = []
    for branch, surfaces in [("east", spec["east"]), ("west", spec["west"]), ("south", spec["south"])]:
        records.append({
            "branch": branch,
            "state": "partial_evidence_only" if surfaces else "absent_held_no_controlled_sense_surface",
            "surface_candidates": surfaces,
            "evidence_ids": [f"EV-{spec['family_id']}-COMPETITOR", f"EV-{spec['family_id']}-ADVERSE"] if branch == "east" else [f"EV-{spec['family_id']}-COMPETITOR"],
        })
    return records


def build_package() -> dict:
    evidence = []
    families = []
    for spec in FAMILY_SPECS:
        contexts = [
            target_context(f"{spec['family_id']}-CTX-{index:02d}", line, surface, kind)
            for index, (line, surface, kind) in enumerate(spec["contexts"], 1)
        ]
        ev_records, edges = evidence_records(spec)
        evidence.extend(ev_records)
        inventory = corpus_inventory(spec["forms_regex"])
        kinds = {context["context_kind"] for context in contexts}
        context_state = "met_at_binding_level" if {"definition_or_formula", "running_prose"}.issubset(kinds) else "held_missing_definition_or_formula_or_running_prose"
        families.append({
            "family_id": spec["family_id"],
            "family_class": spec["family_class"],
            "concept_id": spec["concept_id"],
            "sense_id": spec["sense_id"],
            "label": spec["label"],
            "status": "candidate_binding_preregistration_input_only",
            "contexts": contexts,
            "context_requirement_state": context_state,
            "required_inflected_forms": {
                "state": "exact_current_surface_inventory_only; morphology-complete participant requirement held",
                "current_inventory": inventory,
                "held_reason": "No source-audited five-arm passage set exists from which arm-specific required inflections can be derived.",
            },
            "evidence_edges": edges,
            "branch_evidence": branch_records(spec),
            "arms": [make_arm(role, spec) for role in ROLE_ORDER],
            "final_choice": None,
            "construction_cursor": "Freeze exact German sentence/display alignment; select identical-information item span; obtain qualified native-controlled arm; inflect coherently per arm; revalidate without token mosaics.",
        })

    controls = {
        "current_v018_positive_control_inventory": {
            "jednočas": corpus_inventory(r"\bjednočas\w*"),
            "odpověd": corpus_inventory(r"\bodpověd\w*"),
            "krok": corpus_inventory(r"\bkrok\w*"),
        },
        "exact_current_residual_adverse_evidence": residual_evidence(),
        "stale_control_contradiction": {
            "statement": "SRC-R823-TERM retains gated_not_applied labels while exact current v018 contains executed positive forms and residual pre-switch forms; neither source may silently override the other.",
            "source_ids": ["SRC-R823-TERM", "SRC-V018-BASE", "SRC-V018-BOOK", "SRC-V018-P45", "SRC-V018-BIB"],
        },
    }
    expected = {"jednočas": 159, "odpověd": 498, "krok": 44}
    for key, count in expected.items():
        actual = controls["current_v018_positive_control_inventory"][key]["total"]
        if actual != count:
            raise ValueError(f"current v018 count mismatch {key}: {actual} != {count}")

    morphology_scope_audit = {
        "direct_morphology_or_morphosyntax_contrast_count": 0,
        "families_with_direct_morphology_or_morphosyntax_contrast": [],
        "lexically_overconcentrated": True,
        "distinction": "The per-family inflection inventory is a requirement for making each lexical arm grammatical; it is not an experimental contrast between morphological or morphosyntactic alternatives.",
        "held_reason": "The frozen twelve-family frame contains lexical/terminological/connective choices and a false-friend control. It cannot support a claim that word morphology or global morphosyntactic integration has been tested.",
        "extension_loci": [
            {
                "locus_id": "MI-MORPH-GAP-01",
                "phenomenon": "adjective-noun case/number agreement and technical compound order in quotient-field phrases",
                "locator": target_context("MI-MORPH-GAP-01", 8349, "kvocientno polje", "definition_or_formula"),
                "held_design_question": "Compare coherent whole-phrase paradigms, not isolated adjective or noun substitutions.",
            },
            {
                "locus_id": "MI-MORPH-GAP-02",
                "phenomenon": "finite predicate versus modal/periphrastic holds-valid construction",
                "locator": target_context("MI-MORPH-GAP-02", 1041, "ima važiti", "definition_or_formula"),
                "held_design_question": "Test complete predicate/clause surfaces while preserving logical force and information structure.",
            },
            {
                "locus_id": "MI-MORPH-GAP-03",
                "phenomenon": "genitive/possessive chains and agreement inside the abstract ring definition",
                "locator": target_context("MI-MORPH-GAP-03", 12451, "elementov kolca", "definition_or_formula"),
                "held_design_question": "Keep the definition mathematically identical while contrasting coherent case and word-order systems.",
            },
            {
                "locus_id": "MI-MORPH-GAP-04",
                "phenomenon": "inferential clause linkage, complementizer choice, and word order",
                "locator": target_context("MI-MORPH-GAP-04", 63, "slěduje, že", "running_prose"),
                "held_design_question": "Separate inferential syntax from physical-follow lexical meaning and preserve proposition scope.",
            },
            {
                "locus_id": "MI-MORPH-GAP-05",
                "phenomenon": "case government and relative-clause integration in the form-series definition",
                "locator": target_context("MI-MORPH-GAP-05", 100, "Pod \"rędom form\"", "definition_or_formula"),
                "held_design_question": "Contrast complete definition sentences with branch-coherent morphology; no token mosaic.",
            },
        ],
        "extension_cursor": "Pre-register a separate, balanced morphology/morphosyntax extension after sentence-level German alignment and qualified branch/native construction; retain the frozen twelve lexical families unchanged.",
    }

    return {
        "schema_id": "ISV-MI-ITEM-BINDING-SCHEMA-v1",
        "package_id": "ISV-MI-ITEM-BINDING-v1-20260811",
        "recorded_at": "2026-08-11",
        "time_precision": "day",
        "timezone": "Europe/Berlin",
        "status": "candidate_binding_preregistration_input_only",
        "scope": "Twelve source-pinned candidate/control families over current v018; participant prose is held and no final choice exists.",
        "authority_state": "Current v018 is pinned to its declared ED0011 assembly basis; this package does not claim ED0011 is the present global German authority.",
        "claims": {
            "participant_ready": False,
            "human_response_records": 0,
            "qualified_native_review_records": 0,
            "community_approval": False,
            "certification": False,
            "publication_status": "not_a_publication_payload",
        },
        "source_pins": source_pins(),
        "evidence_registry": evidence,
        "families": families,
        "morphology_scope_audit": morphology_scope_audit,
        "control_reconciliation": controls,
        "rejected_assumptions": [
            "Current v018 frequency does not establish marginal intelligibility.",
            "Official-ISV dictionary presence does not establish a controlled mathematical sense.",
            "Dominant-East familiarity is not the optimization objective.",
            "Branch counts are evidence, not scalar automatic voting weights.",
            "A union of branch-favored tokens is not a coherent participant arm.",
            "Model-authored prose is not a native control.",
            "Executed positive controls are not proven globally optimal, and exact residuals remain adverse evidence.",
            "A paper-range German locator is not sentence-level alignment; item construction remains held.",
        ],
        "continuation_cursor": "Resolve each held sentence-level German alignment serially; freeze same-information spans; derive arm-specific morphology; obtain qualified native-control authoring/review; only then create randomized participant items and register human data separately.",
    }


SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "ISV-MI-ITEM-BINDING-SCHEMA-v1",
    "type": "object",
    "additionalProperties": False,
    "required": ["schema_id", "package_id", "recorded_at", "time_precision", "timezone", "status", "scope", "authority_state", "claims", "source_pins", "evidence_registry", "families", "morphology_scope_audit", "control_reconciliation", "rejected_assumptions", "continuation_cursor"],
    "properties": {
        "schema_id": {"const": "ISV-MI-ITEM-BINDING-SCHEMA-v1"},
        "package_id": {"type": "string", "minLength": 1},
        "recorded_at": {"type": "string", "pattern": "^2026-08-11$"},
        "time_precision": {"const": "day"},
        "timezone": {"const": "Europe/Berlin"},
        "status": {"const": "candidate_binding_preregistration_input_only"},
        "scope": {"type": "string", "minLength": 1},
        "authority_state": {"type": "string", "minLength": 1},
        "claims": {
            "type": "object", "additionalProperties": False,
            "required": ["participant_ready", "human_response_records", "qualified_native_review_records", "community_approval", "certification", "publication_status"],
            "properties": {
                "participant_ready": {"const": False}, "human_response_records": {"const": 0},
                "qualified_native_review_records": {"const": 0}, "community_approval": {"const": False},
                "certification": {"const": False}, "publication_status": {"const": "not_a_publication_payload"},
            },
        },
        "source_pins": {"type": "array", "minItems": 20, "items": {"$ref": "#/$defs/source_pin"}},
        "evidence_registry": {"type": "array", "minItems": 60, "items": {"$ref": "#/$defs/evidence"}},
        "families": {"type": "array", "minItems": 12, "maxItems": 12, "items": {"$ref": "#/$defs/family"}},
        "morphology_scope_audit": {
            "type": "object", "additionalProperties": False,
            "required": ["direct_morphology_or_morphosyntax_contrast_count", "families_with_direct_morphology_or_morphosyntax_contrast", "lexically_overconcentrated", "distinction", "held_reason", "extension_loci", "extension_cursor"],
            "properties": {
                "direct_morphology_or_morphosyntax_contrast_count": {"const": 0},
                "families_with_direct_morphology_or_morphosyntax_contrast": {"type": "array", "maxItems": 0},
                "lexically_overconcentrated": {"const": True},
                "distinction": {"type": "string", "minLength": 1}, "held_reason": {"type": "string", "minLength": 1},
                "extension_loci": {"type": "array", "minItems": 5, "items": {"type": "object", "required": ["locus_id", "phenomenon", "locator", "held_design_question"]}},
                "extension_cursor": {"type": "string", "minLength": 1},
            },
        },
        "control_reconciliation": {"type": "object"},
        "rejected_assumptions": {"type": "array", "minItems": 8, "items": {"type": "string", "minLength": 1}},
        "continuation_cursor": {"type": "string", "minLength": 1},
    },
    "$defs": {
        "source_pin": {
            "type": "object", "additionalProperties": False,
            "required": ["source_id", "absolute_path", "bytes", "sha256", "role"],
            "properties": {
                "source_id": {"type": "string", "pattern": "^SRC-"}, "absolute_path": {"type": "string", "minLength": 3},
                "bytes": {"type": "integer", "minimum": 1}, "sha256": {"type": "string", "pattern": "^[A-F0-9]{64}$"},
                "role": {"type": "string", "minLength": 1},
            },
        },
        "evidence": {
            "type": "object", "additionalProperties": False,
            "required": ["evidence_id", "edge_type", "fact_class", "source_ids", "locator", "claim"],
            "properties": {
                "evidence_id": {"type": "string", "pattern": "^EV-MI-FAM-"},
                "edge_type": {"enum": ["support", "competitor", "adverse", "absence", "veto"]},
                "fact_class": {"enum": ["source_fact", "computation", "editorial_inference", "source_fact_and_computation"]},
                "source_ids": {"type": "array", "minItems": 1, "uniqueItems": True, "items": {"type": "string", "pattern": "^SRC-"}},
                "locator": {"type": "string", "minLength": 1}, "claim": {"type": "string", "minLength": 1},
            },
        },
        "context": {
            "type": "object", "additionalProperties": False,
            "required": ["context_id", "context_kind", "controlled_occurrence_surface", "target_locator", "german_authority_locator", "alignment_state"],
            "properties": {
                "context_id": {"type": "string", "pattern": "^MI-FAM-[0-9]{2}-CTX-[0-9]{2}$"},
                "context_kind": {"enum": ["definition_or_formula", "running_prose"]},
                "controlled_occurrence_surface": {"type": "string", "minLength": 1},
                "target_locator": {"type": "object", "required": ["source_id", "line", "line_sha256_utf8", "producer_declaration_line", "producer_source_path", "producer_source_exists", "producer_source_sha256", "structural_unit"]},
                "german_authority_locator": {"type": "object", "required": ["source_id", "paper_id", "line_start", "line_end", "range_sha256_utf8_lf", "precision"]},
                "alignment_state": {"type": "string", "minLength": 1},
            },
        },
        "arm": {
            "type": "object", "additionalProperties": False,
            "required": ["role", "surface_candidates", "availability", "absent_or_held_reason"],
            "properties": {
                "role": {"enum": ROLE_ORDER},
                "surface_candidates": {"type": "array", "uniqueItems": True, "items": {"type": "string", "minLength": 1}},
                "availability": {"type": "string", "not": {"pattern": "(?i)(participant_ready|approved|certified|canonical|frozen_arm)"}},
                "absent_or_held_reason": {"type": "string", "minLength": 1},
            },
        },
        "family": {
            "type": "object", "additionalProperties": False,
            "required": ["family_id", "family_class", "concept_id", "sense_id", "label", "status", "contexts", "context_requirement_state", "required_inflected_forms", "evidence_edges", "branch_evidence", "arms", "final_choice", "construction_cursor"],
            "properties": {
                "family_id": {"type": "string", "pattern": "^MI-FAM-[0-9]{2}$"},
                "family_class": {"enum": ["contested_technical", "proof_connective_or_predicate", "positive_control", "false_friend_or_trap_control"]},
                "concept_id": {"type": "string", "minLength": 3}, "sense_id": {"type": "string", "minLength": 3},
                "label": {"type": "string", "minLength": 1}, "status": {"const": "candidate_binding_preregistration_input_only"},
                "contexts": {"type": "array", "minItems": 2, "items": {"$ref": "#/$defs/context"}},
                "context_requirement_state": {"enum": ["met_at_binding_level", "held_missing_definition_or_formula_or_running_prose"]},
                "required_inflected_forms": {"type": "object", "required": ["state", "current_inventory", "held_reason"]},
                "evidence_edges": {
                    "type": "object", "additionalProperties": False,
                    "required": ["support", "competitor", "adverse", "absence", "veto"],
                    "properties": {kind: {"type": "array", "minItems": 1, "uniqueItems": True, "items": {"type": "string", "pattern": "^EV-"}} for kind in ["support", "competitor", "adverse", "absence", "veto"]},
                },
                "branch_evidence": {"type": "array", "minItems": 3, "maxItems": 3, "items": {"type": "object", "required": ["branch", "state", "surface_candidates", "evidence_ids"]}},
                "arms": {"type": "array", "minItems": 5, "maxItems": 5, "items": {"$ref": "#/$defs/arm"}},
                "final_choice": {"type": "null"}, "construction_cursor": {"type": "string", "minLength": 1},
            },
        },
    },
}


def write_outputs(package: dict) -> None:
    package_path = HERE / "ISV_MI_ITEM_BINDING.json"
    schema_path = HERE / "ISV_MI_ITEM_BINDING.schema.json"
    csv_path = HERE / "ISV_MI_ITEM_BINDING.csv"
    package_path.write_text(json.dumps(package, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    schema_path.write_text(json.dumps(SCHEMA, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    with csv_path.open("w", encoding="utf-8", newline="") as fh:
        fields = ["family_id", "family_class", "concept_id", "sense_id", "context_count", "context_requirement_state", "role", "availability", "surface_candidates", "hold_reason", "support_ids", "competitor_ids", "adverse_ids", "absence_ids", "veto_ids", "continuation_cursor"]
        writer = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for family in package["families"]:
            for arm in family["arms"]:
                writer.writerow({
                    "family_id": family["family_id"], "family_class": family["family_class"],
                    "concept_id": family["concept_id"], "sense_id": family["sense_id"],
                    "context_count": len(family["contexts"]), "context_requirement_state": family["context_requirement_state"],
                    "role": arm["role"], "availability": arm["availability"],
                    "surface_candidates": " | ".join(arm["surface_candidates"]), "hold_reason": arm["absent_or_held_reason"],
                    "support_ids": " | ".join(family["evidence_edges"]["support"]),
                    "competitor_ids": " | ".join(family["evidence_edges"]["competitor"]),
                    "adverse_ids": " | ".join(family["evidence_edges"]["adverse"]),
                    "absence_ids": " | ".join(family["evidence_edges"]["absence"]),
                    "veto_ids": " | ".join(family["evidence_edges"]["veto"]),
                    "continuation_cursor": family["construction_cursor"],
                })


if __name__ == "__main__":
    write_outputs(build_package())
    print("BUILT ISV_MI_ITEM_BINDING.json, schema, and 60-row CSV projection")

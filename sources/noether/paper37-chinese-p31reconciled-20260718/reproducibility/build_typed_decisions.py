#!/usr/bin/env python3
"""Build the Paper 37 controlled-Hant typed decision without rewriting Hans records."""
from __future__ import annotations

from copy import deepcopy
from pathlib import Path
import hashlib
import json


ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT.parents[4]
DECISIONS = ROOT / "decisions"
BASE = (
    ROOT.parent
    / "noether_paper25_zh_rebase_001_20260718"
    / "decisions"
    / "NOE-P25-ZH-HANT-SCRIPT.json"
)
BASE_EXPECTED = "E32BCF31A3C32926B1031AC556F0B4C71509D62CE1445357A018092387F4DF99"
OUT = DECISIONS / "NOE-P37-ZH-HANT-SCRIPT.json"

P31_HASH = "A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F"
UNIT_HASH = "AF3B34ACF4FF8D91850AC56C4F86447ABC61E6641FF9795BEFBFDA004788585D"
HANS_HASH = "A4A0A97E548840915650FE813AED8FC120D2ABE79F3FA76F9ADF35D5EDAB1B0C"
HANT_HASH = "FC2493ADE14D66835C0EBAAD7C84C78AFFD33A357594F45384CD518C94F32012"
OPENCC_HASH = "6EB1A17122E9BA0C99A0F386AE9E0505587BFDF0E253F721E13E559F2CF05CDC"
DIFF_HASH = "C3104D31D2B9A464E6520979D9D5A4FB888B45BBF74654CB20A500849F6B164D"
FIELD_POLICY_HASH = "EDACDCFDBE4859CB833B2E8D8C0DFA7106C2D905A516ADF39A2BC0B4041A9350"
CREATED_AT = "2026-07-18T21:12:29+02:00"

HANS_EXPECTED = {
    "NOE-P37-ABELIANIZATION.zh-Hans-CN.json": "8324897F327F589AD51A1BA3009333DFB83288879A183AC1CA72F1C8D6AC3308",
    "NOE-P37-ARTIN-CONDUCTOR.zh-Hans-CN.json": "D2ADF9EA5C997B045EBB2F20D61BDFD33AA8FCA836B557746C786CBA5AB25268",
    "NOE-P37-CONJUGATE-DUAL-REPRESENTATION.zh-Hans-CN.json": "4B69CB40B6E63FF8A55AFDDC39D3BE6F06876B12BF72D1111BF0EB1D4189781D",
    "NOE-P37-GALOIS-MODULE.zh-Hans-CN.json": "E764216D81DC123ADEC0DC5C8F77C04A481BBB07273BB80B99B50A4AE9463D72",
    "NOE-P37-HAUPTORDNUNG.zh-Hans-CN.json": "DAC8EA0E1164DFBEE0B7CEB4FB3733B930070C7D0F051FB8B5B2F2696474EF76",
    "NOE-P37-HYPERCOMPLEX-SCALAR-EXTENSION.zh-Hans-CN.json": "911D5DB09CB22E25D49A4E8705A82F4D903A993AD168952525D69922E1A19487",
    "NOE-P37-INTEGRAL-ELEMENT.zh-Hans-CN.json": "89F374244E74B68C1B97ED4B017DDAEF0BFE58B1E447FA5DEBAC6A8FE403C6E6",
    "NOE-P37-LINEAR-DISJOINT-ACCESSORY-EXTENSION.zh-Hans-CN.json": "97702CEE88ED6170CA5273D9B77E5C12C8CEC2B4165D71D35CEBEDE40A4E39D2",
    "NOE-P37-LOCALIZATION-AT-PRIME.zh-Hans-CN.json": "3C69BD8D87820F4A5B8C66C68400C4AA7E581DE7E33A12E79FD62FD7D7DF460F",
    "NOE-P37-MODULE-ISOMORPHISM.zh-Hans-CN.json": "DE66CCC74E3C66DCB08E66DB5C723299A630E29FB522B54FB880ADDF48E640F5",
    "NOE-P37-P-ADIC-COMPLETION.zh-Hans-CN.json": "D81247846F92392066E691D20073E9F1620012794E8F49A6319DCB4840EFC668",
    "NOE-P37-PRINCIPAL-IDEAL-GENERATOR.zh-Hans-CN.json": "BD7C1D11D860855A8EE2ECBAFAFA6A825FDA48E147B2ABE729F12C4AF2F5538D",
    "NOE-P37-SEMISIMPLE-ALGEBRA.zh-Hans-CN.json": "D38FEAC522AA547B11C1E79BE8C26AE2ADEABC06C5ED0CF1D730711C7716316C",
    "NOE-P37-TAME-RAMIFICATION.zh-Hans-CN.json": "D23A5FD8AE8C06C0DE1FE1011DA8F6264CA0B07D88DD8F27EDF76DEA7F1C3A5C",
    "NOE-P37-TRIVIAL-REPRESENTATION.zh-Hans-CN.json": "DAAFE5C7084011CC75F2F685BA75B05394CCA65BF86510369462A5FDD48F151D",
    "NOE-P37-WURZELZAHL-RESOLVENT.zh-Hans-CN.json": "C87D184DE5BB07354CE7ACC0C71773CA1AD94E113AF2C223D31499B2C45FC903",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def require_hash(path: Path, expected: str, label: str) -> None:
    if not path.exists():
        raise SystemExit(f"Missing {label}: {path}")
    actual = sha(path)
    if actual != expected:
        raise SystemExit(f"{label} changed: expected {expected}, got {actual}: {path}")


require_hash(BASE, BASE_EXPECTED, "Paper 25 schema-shape base")
for name, expected in HANS_EXPECTED.items():
    require_hash(DECISIONS / name, expected, f"preserved Hans decision {name}")

source_unit = ROOT / "source/Noether_Paper37_German_P31_logical_article_exact_CRLF.tex"
hans_target = ROOT / "zh-Hans-CN/Noether_Paper37_Chinese_P31Reconciled_zh-Hans-CN_v001.tex"
hant_target = ROOT / "zh-Hant-controlled/Noether_Paper37_Chinese_P31Reconciled_zh-Hant-controlled_v001.tex"
opencc_record = ROOT / "qa/OPENCC_CONVERSION_RECORD.json"
diff_report = ROOT / "qa/HANS_HANT_SCRIPT_DIFF_REPORT.json"
field_policy = PROJECT / "03_projects/language_management/cjk/04_comparison_web/CJKV_CROSSWALK_FIELD_POLICY_20260718.md"

for path, expected, label in (
    (source_unit, UNIT_HASH, "Paper 37 exact source unit"),
    (hans_target, HANS_HASH, "Paper 37 Hans checkpoint"),
    (hant_target, HANT_HASH, "Paper 37 Hant checkpoint"),
    (opencc_record, OPENCC_HASH, "OpenCC custody record"),
    (diff_report, DIFF_HASH, "Hans/Hant diff report"),
    (field_policy, FIELD_POLICY_HASH, "CJKV field policy"),
):
    require_hash(path, expected, label)

diff = json.loads(diff_report.read_text(encoding="utf-8"))
required_diff_facts = {
    "input_sha256": HANS_HASH,
    "output_sha256": HANT_HASH,
    "ordered_math_span_count_hans": 15,
    "ordered_math_span_count_hant": 15,
    "tex_control_token_count_hans": 1107,
    "tex_control_token_count_hant": 1107,
    "environment_token_count_hans": 12,
    "environment_token_count_hant": 12,
    "script_integrity_status": "pass",
    "status": "pass",
}
for key, expected in required_diff_facts.items():
    if diff.get(key) != expected:
        raise SystemExit(f"Unexpected diff fact {key}: expected {expected!r}, got {diff.get(key)!r}")
if diff["build"].get("build_status") != "pass" or diff["build"].get("page_count_from_render_set") != 4:
    raise SystemExit("Hant build/render checkpoint is not the pinned four-page pass")

record = deepcopy(json.loads(BASE.read_text(encoding="utf-8")))
record.update(
    {
        "record_id": "NOE-P37-ZH-HANT-SCRIPT",
        "record_status": "active",
        "supersedes": None,
    }
)
record["work"] = {
    "work_id": "NOETHER-P37",
    "title": "Normalbasis bei Körpern ohne höhere Verzweigung",
    "author": "Emmy Noether",
    "source_language": "de",
    "source_unit_id": "NOE-P37-U000--U099",
    "source_snapshot": {
        "path_or_uri": "evidence://local-workspace/Codex/2026-06-01/we-are-currently-doing-a-massive/Noether_LocalCodex_20260718_P31_FullPaperCanonicalReaudit_WEB_DROP/1/01_current/cum_de_Local_20260718_P31.tex",
        "sha256_or_version": P31_HASH,
        "page_or_line_anchor": "Paper 37 cumulative lines 18613--18799; 48 indexed source units including receipt",
    },
}
record["lane"] = {
    "manager_lane_id": "cjk",
    "linguistic_sublane_id": "chinese.zh-Hant-controlled",
    "scope_note": "Controlled generic Traditional-script bridge only; no Taiwan, Hong Kong, or Macao localization and no external or human certification.",
}
record["concept"] = {
    "concept_id": "NOE-P37-CONTROLLED-HANT-SCRIPT",
    "preferred_gloss": "controlled non-localized Traditional Chinese script/register rendering",
    "intended_sense": "A separately compiled Hant rendering of the source-reconciled Paper 37 zh-Hans-CN text, preserving its mathematical sense while making no regional prose claim.",
    "excluded_senses": [
        "Taiwan-localized mathematical prose",
        "Hong Kong-localized mathematical prose",
        "Macao-localized mathematical prose",
        "external Traditional Chinese review",
        "human comprehension validation",
        "automatic evidence transfer from Simplified Chinese",
    ],
    "stratum": "metadata",
    "trap_flags": ["other"],
}
record["target"] = {
    "language": "Chinese",
    "language_tag": "zh-Hant",
    "script": "Hant",
    "register": "controlled generic mathematical prose",
    "audience": "mathematically trained reader requiring Traditional characters",
    "direction": "ltr",
}
record["intervention_type"] = "script_bridge"
record["candidates"] = [
    {
        "candidate_id": "C-HANT-CONTROLLED",
        "form": "OpenCC 0.1.7 s2t plus declared controlled character, font, and layout normalizations",
        "script_forms": {"Hant": "為 / 裡 / 群 / 眾 / 才 / 個"},
        "variants": [],
        "status": "internally_accepted",
        "definition_or_gloss": "generic controlled Hant artifact without regional localization",
    },
    {
        "candidate_id": "C-HANT-TW",
        "form": "zh-Hant-TW localization",
        "script_forms": {"Hant": "Taiwan standard"},
        "variants": [],
        "status": "held",
        "definition_or_gloss": "requires independent Taiwan terminology and prose review",
    },
    {
        "candidate_id": "C-HANT-HK-MO",
        "form": "zh-Hant-HK/MO localization",
        "script_forms": {"Hant": "Hong Kong or Macao standard"},
        "variants": [],
        "status": "held",
        "definition_or_gloss": "requires separate Hong Kong or Macao terminology and prose review",
    },
]


def evidence(
    evidence_id: str,
    candidate_id: str,
    source_id: str,
    path: str,
    source_class: str,
    digest: str,
    language: str,
    branch: str | None,
    observed: str | None,
    context: str,
    uses: list[str],
    notes: str,
) -> dict:
    return {
        "evidence_id": evidence_id,
        "candidate_id": candidate_id,
        "source": {
            "source_id": source_id,
            "path_or_uri": path,
            "source_class": source_class,
            "sha256_or_version": digest,
            "bibliographic_citation": (
                "Emmy Noether, Journal für die reine und angewandte Mathematik 167 (1932), 147--152"
                if source_id == "SRC-P31-P37"
                else None
            ),
        },
        "language": language,
        "branch_or_cohort": branch,
        "observed_form": observed,
        "concept_match": "exact",
        "context_window": context,
        "register": "historical algebra and number theory" if language == "de" else "mathematical translation/governance",
        "script": "Latn" if language in ("de", "en") else ("Hans" if "Hans" in language else "Hant"),
        "provenance_level": "internally_reviewed",
        "review_status": "internally_reviewed",
        "permitted_uses": uses,
        "weight_semantics": {
            "raw_mass": 1,
            "permitted_use_weight": 1,
            "is_truth_probability": False,
            "notes": notes,
        },
    }


record["evidence"] = {
    "support": [
        evidence(
            "EV-P31-HANT-MEANING",
            "C-HANT-CONTROLLED",
            "SRC-P31-P37",
            "source/Noether_Paper37_German_P31_logical_article_exact_CRLF.tex",
            "canonical_source_authority",
            UNIT_HASH,
            "de",
            None,
            None,
            "The exact Paper 37 unit controls formulas, apparatus, emphasis, and mathematical distinctions in both Chinese scripts.",
            ["source_normalization", "consistency_check"],
            "Source authority controls mathematical sense but cannot authorize a Hant regional form.",
        )
    ],
    "candidate": [
        evidence(
            "EV-HANS-SCRIPT-BASE",
            "C-HANT-CONTROLLED",
            "SRC-ZH-HANS-P37",
            "zh-Hans-CN/Noether_Paper37_Chinese_P31Reconciled_zh-Hans-CN_v001.tex",
            "draft_translation",
            HANS_HASH,
            "zh-Hans-CN",
            "PRC-oriented internal production",
            "source-reconciled Hans prose",
            "The complete audited Hans checkpoint is the declared script-conversion input.",
            ["candidate_discovery", "consistency_check"],
            "A Hans source can seed a script candidate but cannot serve as independent Hant regional usage evidence.",
        ),
        evidence(
            "EV-HANT-OUTPUT-CHECKPOINT",
            "C-HANT-CONTROLLED",
            "SRC-ZH-HANT-P37",
            "zh-Hant-controlled/Noether_Paper37_Chinese_P31Reconciled_zh-Hant-controlled_v001.tex",
            "draft_translation",
            HANT_HASH,
            "zh-Hant",
            "controlled generic nonregional artifact",
            "controlled generic Hant output",
            "The exact Hant checkpoint is tied to the Hans input by the pinned conversion and script-diff records.",
            ["consistency_check"],
            "This is an internal artifact checkpoint, not independent Hant usage evidence or regional validation.",
        ),
    ],
    "competitor": [],
    "adverse": [
        evidence(
            "EV-HANT-NO-LOCALIZATION",
            "C-HANT-CONTROLLED",
            "SRC-CJKV-FIELD-POLICY",
            "03_projects/language_management/cjk/04_comparison_web/CJKV_CROSSWALK_FIELD_POLICY_20260718.md",
            "language_family_reference_shelf",
            FIELD_POLICY_HASH,
            "en",
            None,
            "Mandarin Simplified evidence cannot fill Traditional Chinese regional channels",
            "The dominance rule prohibits cross-filling Taiwan, Hong Kong, or Macao support from Mandarin Simplified evidence.",
            ["adverse_evidence", "consistency_check"],
            "Hard qualitative control; never a readiness scalar.",
        )
    ],
    "veto": [],
    "absence": [
        {
            "language_or_branch": branch,
            "search_scope": "Paper 37 native shelf and lane records",
            "search_date": "2026-07-18",
            "status": "searched_no_evidence",
            "notes": f"No {label}-specific mathematical prose or reviewer return.",
        }
        for branch, label in (
            ("zh-Hant-TW", "Taiwan"),
            ("zh-Hant-HK", "Hong Kong"),
            ("zh-Hant-MO", "Macao"),
        )
    ],
}
record["risk_controls"] = {
    "sense": {"status": "clear", "notes": "Mathematical sense is controlled by the audited Hans unit and exact German source."},
    "false_friend": {"status": "risk", "notes": "Script conversion preserves any misleading Hans lexical choice; the 16 term-level Hans decisions remain controlling."},
    "homograph": {"status": "risk", "notes": "Shared Han forms do not prove identical regional usage or register."},
    "dominance": {"status": "adverse", "notes": "The artifact derives from PRC-oriented Mandarin-Simplified prose and has no independent regional Hant source; no numeric penalty or readiness scalar is computed."},
    "register": {"status": "risk", "notes": "Generic Hant prose may diverge from Taiwan, Hong Kong, or Macao preferences."},
    "script": {"status": "clear", "notes": "OpenCC 0.1.7 s2t is hash-custodied; declared controlled normalizations yield a passing, idempotent pipeline while raw s2t alone is explicitly not claimed idempotent."},
    "source_scarcity": {"status": "adverse", "notes": "No independent Hant Paper 37 source or regional reviewer return."},
}
record["readiness_gates"] = {
    "source_floor": {"status": "pass", "evidence_or_reason": "Sealed German authority, exact Paper 37 source unit, and fully audited Hans input exist."},
    "context_review": {"status": "pass", "evidence_or_reason": "The 48 indexed source units and the Hant script/TeX invariants are checked internally."},
    "adverse_review": {"status": "pass", "evidence_or_reason": "Mandarin-Simplified dominance and non-localization limits are explicit."},
    "branch_or_cohort_review": {"status": "pending", "evidence_or_reason": "Taiwan, Hong Kong, and Macao cohorts are absent."},
    "script_policy": {"status": "pass", "evidence_or_reason": "Artifact is labelled controlled generic zh-Hant, not regional."},
    "internal_qa": {"status": "pass", "evidence_or_reason": "Exact Hans SHA-256 A4A0A97E548840915650FE813AED8FC120D2ABE79F3FA76F9ADF35D5EDAB1B0C and Hant SHA-256 FC2493ADE14D66835C0EBAAD7C84C78AFFD33A357594F45384CD518C94F32012 are bound by the passing diff report: 15/15 ordered math spans preserve non-CJK skeletons, 1107/1107 TeX controls and 12/12 environment tokens match, two XeLaTeX passes are clean, and four render pages are present."},
    "external_review": {"status": "pending", "evidence_or_reason": "No external Hant reviewer return."},
    "human_comprehension": {"status": "pending", "evidence_or_reason": "No region-controlled reader study."},
}
record["decision"] = {
    "status": "candidate_after_context_check",
    "selected_candidate_id": "C-HANT-CONTROLLED",
    "rationale": "A separately labelled and compiled generic Hant rendering preserves the audited Paper 37 mathematical content while retaining strict non-localization and qualitative dominance-debt boundaries.",
    "reviewer_question": "Which terminology and prose changes are required separately for Taiwan, Hong Kong, and Macao standards?",
    "auto_promotion_prohibited": True,
    "decision_authority": "Chinese Noether production lane internal script and source audit",
    "decision_date": "2026-07-18",
}
record["invariants"] = [
    {
        "invariant_id": "INV-HANT-MATH-TEX",
        "must_preserve": "all formulas, TeX controls/environments, symbols, fields, and source-aligned apparatus loci",
        "may_change": "Chinese character forms and later locale-specific prose",
        "test": "qa/HANS_HANT_SCRIPT_DIFF_REPORT.json plus SOURCE_UNIT_MAP.csv",
        "status": "pass",
    },
    {
        "invariant_id": "INV-HANT-NONLOCAL",
        "must_preserve": "no Taiwan, Hong Kong, or Macao localization claim and no external or human certification claim",
        "may_change": None,
        "test": "lane scope, excluded senses, readiness gates, and graph claim-control validation",
        "status": "pass",
    },
]
record["provenance"] = {
    "created_by": "Codex Chinese Noether production session",
    "created_at": CREATED_AT,
    "input_artifacts": [
        {"path_or_uri": "source/Noether_Paper37_German_P31_logical_article_exact_CRLF.tex", "version_or_hash": UNIT_HASH, "role": "canonical source unit"},
        {"path_or_uri": "zh-Hans-CN/Noether_Paper37_Chinese_P31Reconciled_zh-Hans-CN_v001.tex", "version_or_hash": HANS_HASH, "role": "audited script base"},
        {"path_or_uri": "zh-Hant-controlled/Noether_Paper37_Chinese_P31Reconciled_zh-Hant-controlled_v001.tex", "version_or_hash": HANT_HASH, "role": "controlled generic Hant output checkpoint"},
        {"path_or_uri": "qa/OPENCC_CONVERSION_RECORD.json", "version_or_hash": OPENCC_HASH, "role": "converter runtime/config/dictionary custody"},
        {"path_or_uri": "qa/HANS_HANT_SCRIPT_DIFF_REPORT.json", "version_or_hash": DIFF_HASH, "role": "script, TeX, build, and render-set integrity gate"},
        {"path_or_uri": "03_projects/language_management/cjk/03_working_translations/noether_paper25_zh_rebase_001_20260718/decisions/NOE-P25-ZH-HANT-SCRIPT.json", "version_or_hash": BASE_EXPECTED, "role": "pinned schema-shape and control-pattern base"},
    ],
    "pre_change_snapshot_preserved": True,
    "applied_diff_path_or_uri": "zh-Hant-controlled/Noether_Paper37_Chinese_P31Reconciled_zh-Hant-controlled_v001.tex",
    "notes": "No Singapore, Taiwan, Hong Kong, Macao, external, community, or human certification is claimed. Qualitative dominance debt is never converted to a readiness scalar.",
}

OUT.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# The builder is required to leave all 16 pre-existing Hans decisions byte-identical.
for name, expected in HANS_EXPECTED.items():
    require_hash(DECISIONS / name, expected, f"post-build preserved Hans decision {name}")

print(
    json.dumps(
        {
            "path": str(OUT),
            "sha256": sha(OUT),
            "hans_preserved_count": len(HANS_EXPECTED),
            "bound_hans_sha256": HANS_HASH,
            "bound_hant_sha256": HANT_HASH,
        },
        ensure_ascii=True,
        indent=2,
    )
)

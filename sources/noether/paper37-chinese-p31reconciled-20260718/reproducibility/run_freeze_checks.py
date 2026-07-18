#!/usr/bin/env python3
"""Fail-closed final checks for the Chinese Noether Paper 37 tranche.

This checker does not compile TeX, render PDFs, or rerun any source/structural
builder. It reads the already-produced artifacts and writes the three freeze
reports only after every required file and all 13 final render pages exist and
the invoking reviewer explicitly attests that those pages were inspected.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import struct
from datetime import datetime
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT.parents[4]
AUTHORITY = Path(
    r"evidence://local-workspace/Codex\2026-06-01\we-are-currently-doing-a-massive"
    r"\Noether_LocalCodex_20260718_P31_FullPaperCanonicalReaudit_WEB_DROP"
    r"\1\01_current\cum_de_Local_20260718_P31.tex"
)
EXPECTED_AUTHORITY = "A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F"
GLOBAL = PROJECT / "03_projects/language_management/cjk/00_lane_control/structural_reproducibility"

FILES = {
    "source_section_interval": ROOT / "source/Noether_Paper37_German_P31_section_interval_exact_CRLF.tex",
    "source_exact_crlf": ROOT / "source/Noether_Paper37_German_P31_logical_article_exact_CRLF.tex",
    "source_lf": ROOT / "source/Noether_Paper37_German_P31_logical_article_LF.tex",
    "inherited_logical_witness": ROOT / "witness/Noether_Paper37_SimplifiedChinese_Inherited_logical_article_exact_CRLF.tex",
    "german_tex": ROOT / "source_control/Noether_Paper37_German_P31_Standalone.tex",
    "german_pdf": ROOT / "source_control/Noether_Paper37_German_P31_Standalone.pdf",
    "german_log": ROOT / "source_control/Noether_Paper37_German_P31_Standalone.log",
    "hans_tex": ROOT / "zh-Hans-CN/Noether_Paper37_Chinese_P31Reconciled_zh-Hans-CN_v001.tex",
    "hans_pdf": ROOT / "zh-Hans-CN/Noether_Paper37_Chinese_P31Reconciled_zh-Hans-CN_v001.pdf",
    "hans_log": ROOT / "zh-Hans-CN/Noether_Paper37_Chinese_P31Reconciled_zh-Hans-CN_v001.log",
    "hant_tex": ROOT / "zh-Hant-controlled/Noether_Paper37_Chinese_P31Reconciled_zh-Hant-controlled_v001.tex",
    "hant_pdf": ROOT / "zh-Hant-controlled/Noether_Paper37_Chinese_P31Reconciled_zh-Hant-controlled_v001.pdf",
    "hant_log": ROOT / "zh-Hant-controlled/Noether_Paper37_Chinese_P31Reconciled_zh-Hant-controlled_v001.log",
}

EXPECTED_HASHES = {
    "source_section_interval": "AF2993A83530352893CABA50D196BDE9A17965C0E531297CA1A9E5AEB2D1B00A",
    "source_exact_crlf": "AF3B34ACF4FF8D91850AC56C4F86447ABC61E6641FF9795BEFBFDA004788585D",
    "source_lf": "68C72173E0C060BC68CB3651AF078ACE82B4D5806C8A41584632AA2BB4A9B27B",
    "inherited_logical_witness": "1312DD725554A57A3A52FE780E924A5F7305C4E61E6418E393374B4D9EA1924B",
    "german_tex": "0AA0DBE6A75C70BABDD08E5CC93BA953ED904F913BEDBDA85F48D3DCB2BE2909",
    "german_pdf": "509F53D9ADF50FA29375F59BE8B9CE93E8E04E237319AC24B3760F40D291686F",
    "german_log": "986CFD311B6E18E27C1961810F2106A1DFFDC2578C5847FB0C3AEF40C149BEEF",
    "hans_tex": "A4A0A97E548840915650FE813AED8FC120D2ABE79F3FA76F9ADF35D5EDAB1B0C",
    "hans_pdf": "86C7274D137A51469F91D6939D3F3583BFB982CFE69ACE264064A473DA62405A",
    "hans_log": "19B9D236D9B316B70E4D254C6AD970BC2398CEC3682170362DF71AF613D3EA72",
    "hant_tex": "FC2493ADE14D66835C0EBAAD7C84C78AFFD33A357594F45384CD518C94F32012",
    "hant_pdf": "35ADCF5A0B9FD5AEEAD16F7E126DFB89B1A9D4BB509FE9661A268C6B897AC36A",
    "hant_log": "C31DC7CBFE272A7E5088B193FE0FFB372ED362CC7227F7875C35E78BACB86B8A",
}

REPORTS = {
    "source_custody": ROOT / "SOURCE_CUSTODY.json",
    "source_check": ROOT / "SOURCE_CHECK.md",
    "source_use": ROOT / "SOURCE_USE.md",
    "terminology": ROOT / "TERMINOLOGY.md",
    "source_parity": ROOT / "qa/P37_SOURCE_PARITY.json",
    "inherited_audit": ROOT / "qa/INHERITED_STRUCTURE_AND_MATH_AUDIT.json",
    "hans_transform": ROOT / "qa/HANS_REBASE_TRANSFORM.json",
    "decision_schema": ROOT / "qa/DECISION_SCHEMA_VALIDATION_REPORT.json",
    "evidence_graph": ROOT / "qa/EVIDENCE_GRAPH_VALIDATION_REPORT.json",
    "graph": ROOT / "evidence/NOE-P37_TYPED_EVIDENCE_GRAPH.json",
    "hans_hant": ROOT / "qa/HANS_HANT_SCRIPT_DIFF_REPORT.json",
    "opencc": ROOT / "qa/OPENCC_CONVERSION_RECORD.json",
    "csv_validation": ROOT / "qa/csv_artifact_validation/CSV_ARTIFACT_TOOL_VALIDATION_REPORT.json",
    "csv_validator": ROOT / "qa/csv_artifact_validation/validate_csvs.mjs",
    "crosswalk": ROOT / "evidence/NOE-P37_CJKV_CROSSWALK.csv",
    "adverse": ROOT / "evidence/CHINESE_ADVERSE_EVIDENCE_LEDGER.csv",
    "native": ROOT / "evidence/CHINESE_NATIVE_EVIDENCE_LEDGER.csv",
    "localization": ROOT / "LOCALIZATION_STATUS.csv",
    "source_map": ROOT / "SOURCE_UNIT_MAP.csv",
    "local_structure": ROOT / "STRUCTURAL_INDEX.json",
    "local_structure_csv": ROOT / "STRUCTURAL_INDEX.csv",
    "source_cursor": ROOT / "qa/source_version_cursor.json",
    "global_validation": GLOBAL / "VALIDATION_REPORT_20260718.json",
    "global_structure": GLOBAL / "CJK_STRUCTURAL_INDEX_20260718.jsonl",
    "global_structure_csv": GLOBAL / "CJK_STRUCTURAL_INDEX_20260718.csv",
    "difficulty": GLOBAL / "CJK_DIFFICULTY_FAILURE_LEDGER_20260718.jsonl",
    "global_csv_validation": GLOBAL / "artifact_tool_validation/GLOBAL_STRUCTURAL_CSV_ARTIFACT_TOOL_VALIDATION_REPORT.json",
    "global_csv_validator": GLOBAL / "artifact_tool_validation/validate_global_structural_csv.mjs",
}

EXPECTED_REPORT_HASHES = {
    "source_custody": "D692352468525BEDFD31FEA87BF0A5CEDA3C3ECB089D1B549CC9D89B2D578EE8",
    "source_check": "B57189AB57F27016D52F5FE1C43C349BC4C0D21D27F9E6594A9185301DEBAD5D",
    "source_use": "BF016302557455015031552C0F6EC667BE5B6AE03A9374E970FD98E8ECCE152F",
    "terminology": "918F1694A5E9BAEDCDA815C6456CA42BAA80BFD8C4AB5D2EF04B3E530E32C256",
    "source_parity": "C09DCE40F1026AA00006102E3E1F81DD163B0587FE31F79AB72D63AC8A5E9DD7",
    "inherited_audit": "887E0E9E9D28891B430A64CB1D91A9D5F11E55D07736E15F28BF8B569B2C2DD5",
    "hans_transform": "E9573162AB9E2C0902A17AB8FA0304348671BB00157E116EC925122F6BCAD696",
    "decision_schema": "EB85D1FFAE9D71BE85ADFD0C97242E6DBAA4FBBBF82C3E422B45E2E8C3340C30",
    "evidence_graph": "20B0AB8FB47A4B9EA73D33FD5AB792078DE3A2B025D595ABA0EDA452383E6550",
    "graph": "5726E8CA66379FFD66543426FBAE7CA8CD39FFAB222DC84CD2588C6B13CFEBBD",
    "hans_hant": "C3104D31D2B9A464E6520979D9D5A4FB888B45BBF74654CB20A500849F6B164D",
    "opencc": "6EB1A17122E9BA0C99A0F386AE9E0505587BFDF0E253F721E13E559F2CF05CDC",
    "csv_validation": "D5FABBD159E6F7978BFA31E3B61F29C6974727512582C7893B1E3C4243392627",
    "csv_validator": "609B6F17E1A8DA588479BD4C552A066C976779A5F55C9D7CC4280634215C4393",
    "crosswalk": "867E01451E0E2C325E12C084F75295D654129D63AC36ED0AECA03E615EC42539",
    "adverse": "99F1C91F994A969FF9C01EA6AF8F5320E9FFDB7CACC8DF1BCB8EBD2399F77F16",
    "native": "77330EBF4D8A3285A88E5E071E489FF5BEECE52D8C2995601D532414F3B0BCDD",
    "localization": "31400163FB7985AA52DA1C299C1945908AF86C1ECE8C29EB852436882B7214FF",
    "source_map": "B8E7A0FDD76EA47F1861AD5E7F4B7338087A0842FBF28F675DA466133F8C06E1",
    "local_structure": "E0ECB7287EA2E076D90A3AF9E6751C66D9361821C6112090B12FB9537B9AF25D",
    "local_structure_csv": "632AD12A5AC603673B3F2241C539DA5AB9C580D7AB6ED612843846DD8BDB98E5",
    "source_cursor": "B551B19D2BA8D97D7239772525485B424EDA544B87BF63477CC8C14217A2FCDE",
    "global_validation": "63B5723BF1712FBA4E3C660F546AF69C6430E47062C3A566CC581873DC9DBCB7",
    "global_structure": "DD87584B89C5C0DB9D472E860025CA461CF9C85942231855BE86A9092FC88967",
    "global_structure_csv": "5C2F8FB047D8370207E95C72D4627C23D442CD027BCABBE2ED7F1B85BB56D40A",
    "difficulty": "4CA309C9AEFB3D07432A56E0CE27AA1BC762ED72605B468F58F9B90B7C6AFBE6",
    "global_csv_validation": "9134F94A314F33EF54887CA8CECC3A74604AF26CB0671216FD3C026A0B399804",
    "global_csv_validator": "172191510AD96CDBB1CC2E4448A049C5010727C6946AE82A68D0B7E280CF1188",
}

EXPECTED_RENDER_COUNTS = {"source-control": 5, "zh-Hans-CN": 4, "zh-Hant-controlled": 4}
EXPECTED_PAGE_COUNTS = {"German control": 5, "zh-Hans-CN": 4, "controlled zh-Hant": 4}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def png_dimensions(path: Path) -> tuple[int, int]:
    header = path.read_bytes()[:24]
    if len(header) != 24 or header[:8] != b"\x89PNG\r\n\x1a\n" or header[12:16] != b"IHDR":
        raise ValueError("not a valid PNG with an IHDR header")
    return struct.unpack(">II", header[16:24])


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--visual-inspection-attested",
        action="store_true",
        help="Confirm that all 13 final PNG pages were individually inspected after their accepted PDF builds.",
    )
    parser.add_argument(
        "--inspector-note",
        default="internal model visual inspection attested by invoking reviewer",
        help="Short provenance note for the internal visual inspection; this never denotes external certification.",
    )
    return parser.parse_args()


args = parse_args()
render_root = ROOT / "renders/final"
render_pages: dict[str, list[Path]] = {}
prerequisite_errors: list[str] = []

for path in [AUTHORITY, *FILES.values(), *REPORTS.values()]:
    if not path.is_file():
        prerequisite_errors.append(f"missing required file: {path}")
for cohort, expected_count in EXPECTED_RENDER_COUNTS.items():
    directory = render_root / cohort
    pages = sorted(directory.glob("page-*.png")) if directory.is_dir() else []
    render_pages[cohort] = pages
    expected_names = [f"page-{index}.png" for index in range(1, expected_count + 1)]
    if [path.name for path in pages] != expected_names:
        prerequisite_errors.append(
            f"final render inventory for {cohort}: expected {expected_names}, got {[path.name for path in pages]}"
        )
if not args.visual_inspection_attested:
    prerequisite_errors.append("explicit --visual-inspection-attested flag is absent")

if prerequisite_errors:
    print(json.dumps({
        "work_unit": "NOE-P37",
        "status": "not_run",
        "reports_written": False,
        "prerequisite_errors": prerequisite_errors,
        "review_limit": "The visual-attestation flag may be used only after actual all-page internal inspection.",
    }, ensure_ascii=False, indent=2))
    raise SystemExit(2)

checked_at = datetime.now().astimezone().isoformat(timespec="seconds")
errors: list[str] = []
warnings: list[str] = [
    "Raw OpenCC s2t is not second-pass idempotent; the declared s2t plus controlled-normalization pipeline is idempotent.",
    "Global structural validation retains machine-alignment warnings and its declared human-review limit.",
]

authority_hash = sha(AUTHORITY)
if authority_hash != EXPECTED_AUTHORITY:
    errors.append(f"sealed P31 authority hash mismatch: {authority_hash}")

file_hashes = {name: sha(path) for name, path in FILES.items()}
for name, expected in EXPECTED_HASHES.items():
    if file_hashes[name] != expected:
        errors.append(f"{name} hash mismatch: expected {expected}, got {file_hashes[name]}")

source_body = FILES["source_lf"].read_bytes()
german_wrapper = FILES["german_tex"].read_bytes()
if german_wrapper.count(source_body) != 1:
    errors.append("German standalone does not contain the exact sealed LF body exactly once")

report_hashes = {name: sha(path) for name, path in REPORTS.items()}
for name, expected in EXPECTED_REPORT_HASHES.items():
    if report_hashes[name] != expected:
        errors.append(f"{name} report/artifact hash mismatch: expected {expected}, got {report_hashes[name]}")

custody = load(REPORTS["source_custody"])
if not all(custody.get("checks", {}).values()):
    errors.append("source custody does not report all hash checks true")
custody_expected = custody.get("expected", {})
for key, expected in {
    "sealed_p31_cumulative_sha256": EXPECTED_AUTHORITY,
    "sealed_p31_section_interval_sha256": EXPECTED_HASHES["source_section_interval"],
    "sealed_p31_logical_article_sha256": EXPECTED_HASHES["source_exact_crlf"],
    "sealed_p31_logical_article_lf_sha256": EXPECTED_HASHES["source_lf"],
}.items():
    if custody_expected.get(key) != expected:
        errors.append(f"source custody {key} is not pinned to the accepted hash")

source_parity = load(REPORTS["source_parity"])
parity_checks = source_parity.get("checks", [])
if source_parity.get("status") != "PASS" or source_parity.get("unresolved_parity_issues"):
    errors.append("source parity report is not a clean PASS")
if len(parity_checks) != 22 or not all(row.get("pass") is True for row in parity_checks):
    errors.append("source parity does not contain 22/22 passing checks")
expected_structure = {
    "section": 1,
    "subsection": 3,
    "paragraph_heading": 9,
    "footnote": 12,
    "semantic_emphasis": 15,
    "display": 15,
    "center": 3,
}
if source_parity.get("structure", {}).get("source") != expected_structure:
    errors.append("source parity source-structure counts differ from the accepted topology")
if source_parity.get("structure", {}).get("target") != expected_structure:
    errors.append("source parity target-structure counts differ from the accepted topology")

decision = load(REPORTS["decision_schema"])
if decision.get("status") != "pass" or decision.get("error_count") != 0:
    errors.append("typed-decision validation is not a zero-error pass")
for key, expected in {
    "decision_count": 17,
    "hans_decision_count": 16,
    "hant_decision_count": 1,
    "preserved_hans_hash_count": 16,
    "crosswalk_row_count": 16,
    "declared_artifact_hash_or_existence_check_count": 131,
    "claim_control_check_count": 85,
}.items():
    if decision.get(key) != expected:
        errors.append(f"typed-decision {key}: expected {expected}, got {decision.get(key)}")
if decision.get("bound_targets") != {
    "zh-Hans-CN_sha256": EXPECTED_HASHES["hans_tex"],
    "zh-Hant_controlled_sha256": EXPECTED_HASHES["hant_tex"],
}:
    errors.append("typed-decision validation is not bound to both accepted target TeX hashes")
live_decisions = {path.name: sha(path) for path in sorted((ROOT / "decisions").glob("*.json"))}
validated_decisions = {row["record"]: row["sha256"] for row in decision.get("records", [])}
if live_decisions != validated_decisions:
    errors.append("live typed-decision filename/hash inventory differs from the validation report")

graph = load(REPORTS["evidence_graph"])
if graph.get("status") != "pass" or graph.get("error_count") != 0:
    errors.append("typed evidence graph validation is not a zero-error pass")
for key, expected in {
    "edge_count": 133,
    "typed_decision_count": 17,
    "graph_decision_reference_count": 17,
    "typed_unique_evidence_source_reference_count": 14,
    "typed_evidence_source_reference_coverage_count": 14,
    "crosswalk_rows": 16,
    "native_ledger_rows": 16,
    "adverse_ledger_rows": 20,
    "adverse_nonlexical_translation_unit_rows": 4,
    "claim_control_record_count": 17,
    "dag_topological_visit_count": 70,
}.items():
    if graph.get(key) != expected:
        errors.append(f"evidence graph {key}: expected {expected}, got {graph.get(key)}")
if graph.get("graph_sha256") != report_hashes["graph"] or sum(graph.get("node_counts", {}).values()) != 70:
    errors.append("evidence graph report does not bind the live 70-node graph")

hant = load(REPORTS["hans_hant"])
if hant.get("status") != "pass" or hant.get("script_integrity_status") != "pass":
    errors.append("Hans/Hant script-integrity report is not pass")
for keys, expected in [
    (("ordered_math_span_count_hans", "ordered_math_span_count_hant"), (15, 15)),
    (("tex_control_token_count_hans", "tex_control_token_count_hant"), (1107, 1107)),
    (("environment_token_count_hans", "environment_token_count_hant"), (12, 12)),
]:
    got = tuple(hant.get(key) for key in keys)
    if got != expected:
        errors.append(f"Hans/Hant {keys}: expected {expected}, got {got}")
integrity = hant.get("script_integrity_checks", {})
if not integrity or not all(integrity.values()):
    errors.append("one or more declared Hans/Hant integrity checks are false")
if hant.get("raw_s2t_second_pass_idempotent") is not False:
    errors.append("raw s2t adverse non-idempotence is no longer represented explicitly")

opencc = load(REPORTS["opencc"])
if opencc.get("input_sha256") != EXPECTED_HASHES["hans_tex"] or opencc.get("output_sha256") != EXPECTED_HASHES["hant_tex"]:
    errors.append("OpenCC record does not bind the accepted Hans and Hant TeX hashes")
if opencc.get("localization_status") != "controlled generic Traditional script; explicitly not zh-Hant-TW/HK/MO":
    errors.append("OpenCC record lacks the required nonregional Hant status")
if opencc.get("external_or_human_validation") != "none":
    errors.append("OpenCC record makes an unsupported external or human-validation claim")

csv_validation = load(REPORTS["csv_validation"])
if csv_validation.get("status") != "pass" or csv_validation.get("csv_count") != 6:
    errors.append("local artifact-tool CSV validation is not a six-file pass")
csv_record_by_path = {row["csv_path"]: row for row in csv_validation.get("records", [])}
for relative, report_name in {
    "SOURCE_UNIT_MAP.csv": "source_map",
    "STRUCTURAL_INDEX.csv": "local_structure_csv",
    "LOCALIZATION_STATUS.csv": "localization",
    "evidence/CHINESE_NATIVE_EVIDENCE_LEDGER.csv": "native",
    "evidence/CHINESE_ADVERSE_EVIDENCE_LEDGER.csv": "adverse",
    "evidence/NOE-P37_CJKV_CROSSWALK.csv": "crosswalk",
}.items():
    row = csv_record_by_path.get(relative, {})
    if row.get("status") != "pass" or row.get("csv_sha256") != report_hashes[report_name]:
        errors.append(f"artifact-tool CSV record is absent, failed, or stale for {relative}")
    if row.get("formula_cell_count") != 0 or row.get("dangerous_leading_value_count") != 0:
        errors.append(f"artifact-tool CSV formula-safety check failed for {relative}")

if len(csv_rows(REPORTS["crosswalk"])) != 16:
    errors.append("crosswalk row count is not 16")
if len(csv_rows(REPORTS["adverse"])) != 20:
    errors.append("adverse-evidence ledger row count is not 20")
if len(csv_rows(REPORTS["native"])) != 16:
    errors.append("native-evidence ledger row count is not 16")

localization_rows = csv_rows(REPORTS["localization"])
localization_states = {row["language_tag"]: row["status"] for row in localization_rows}
expected_localization_states = {
    "zh-Hans-CN": "prc_oriented_internal_source_checked_build_render_frozen",
    "zh-Hans-SG": "held_unvalidated_no_separate_localization",
    "zh-Hant": "controlled_generic_hant_internal_build_render_validated_nonlocalized",
    "zh-Hant-TW": "held_unvalidated_no_localization",
    "zh-Hant-HK": "held_unvalidated_no_localization",
    "zh-Hant-MO": "held_unvalidated_no_localization",
}
if localization_states != expected_localization_states:
    errors.append("localization rows do not preserve PRC-oriented Hans, generic Hant, and held regional states")

local_structure = load(REPORTS["local_structure"])
coverage = local_structure.get("coverage", {})
if coverage.get("indexed_total") != 48 or coverage.get("footnotes") != 12 or coverage.get("displays") != 15:
    errors.append("local structural JSON does not retain the accepted 48-unit/12-footnote/15-display coverage")
target_state = local_structure.get("target", {})
if target_state.get("completion_state") != "complete":
    errors.append("local structure does not mark the Hans target complete")
if target_state.get("review_state") != "source_parity_typed_evidence_build_render_pass":
    errors.append("local structure does not bind the accepted source/evidence/build/render review state")
if target_state.get("publication_state") != "handoff_ready":
    errors.append("local structure does not mark the internally frozen target handoff-ready")
validation_state = local_structure.get("validation", {})
if validation_state.get("status") != "internally_frozen" or validation_state.get("external_or_human_validation") is not False:
    errors.append("local structure validation state is not internally frozen with external/human validation false")

local_structure_rows = csv_rows(REPORTS["local_structure_csv"])
source_map_rows = csv_rows(REPORTS["source_map"])
if len(local_structure_rows) != 48 or len(source_map_rows) != 48:
    errors.append("local structural CSV or source-unit map does not have 48 rows")
if any(row["completion_state"] != "complete" for row in local_structure_rows):
    errors.append("local structural CSV contains a non-complete row")
if any(row["publication_state"] != "handoff_ready" for row in local_structure_rows):
    errors.append("local structural CSV contains a non-handoff-ready row")
if any(row["source_status"] != "sealed_p31_exact" for row in source_map_rows):
    errors.append("source-unit map contains a row not keyed to exact sealed P31")
if any(row["target_status"] != "complete" for row in source_map_rows):
    errors.append("source-unit map contains a non-complete internal Hans target row")

global_validation = load(REPORTS["global_validation"])
if global_validation.get("status") != "pass" or global_validation.get("errors"):
    errors.append("global structural/difficulty validation is not pass")
if global_validation.get("record_count") != 295 or global_validation.get("work_counts", {}).get("NOE-P37") != 85:
    errors.append("global structural counts are not 295 total / 85 Paper 37")
if global_validation.get("difficulty_record_count") != 22 or global_validation.get("latest_difficulty_id") != "CJK-HARD-20260718-021":
    errors.append("difficulty ledger count/cursor is not 22 / CJK-HARD-20260718-021")

global_csv = load(REPORTS["global_csv_validation"])
if global_csv.get("status") != "pass" or global_csv.get("csv_sha256") != report_hashes["global_structure_csv"]:
    errors.append("global artifact-tool CSV validation is absent, failed, or stale")
if global_csv.get("data_row_count") != 295 or global_csv.get("column_count") != 20 or global_csv.get("formula_cell_count") != 0:
    errors.append("global artifact-tool CSV shape or formula-safety result is not 295 rows / 20 columns / zero formulas")

build_specs = [
    ("German control", "XeLaTeX", "german_tex", "german_pdf", "german_log"),
    ("zh-Hans-CN", "XeLaTeX", "hans_tex", "hans_pdf", "hans_log"),
    ("controlled zh-Hant", "XeLaTeX", "hant_tex", "hant_pdf", "hant_log"),
]
diagnostic_pattern = re.compile(
    r"^!|warning|overfull|underfull|missing character|undefined control|fatal error",
    re.I | re.M,
)
build_records = []
for label, engine, tex_key, pdf_key, log_key in build_specs:
    tex, pdf, log = FILES[tex_key], FILES[pdf_key], FILES[log_key]
    log_text = log.read_text(encoding="utf-8", errors="replace")
    matches = diagnostic_pattern.findall(log_text)
    pages = len(PdfReader(str(pdf)).pages)
    expected_pages = EXPECTED_PAGE_COUNTS[label]
    status = "pass" if not matches and pages == expected_pages else "fail"
    if matches:
        errors.append(f"{label} final log has {len(matches)} warning/error/box/missing/undefined diagnostics")
    if pages != expected_pages:
        errors.append(f"{label} PDF expected {expected_pages} pages, got {pages}")
    build_records.append({
        "artifact": label,
        "engine": engine,
        "passes": 2,
        "command_policy": "interaction=nonstopmode; halt-on-error",
        "tex_path": tex.relative_to(ROOT).as_posix(),
        "tex_sha256": sha(tex),
        "pdf_path": pdf.relative_to(ROOT).as_posix(),
        "pdf_sha256": sha(pdf),
        "log_path": log.relative_to(ROOT).as_posix(),
        "log_sha256": sha(log),
        "pages": pages,
        "diagnostic_match_count": len(matches),
        "status": status,
    })

build_log = {
    "schema_version": "1.0.0",
    "work_unit": "NOE-P37",
    "recorded_at": checked_at,
    "builds": build_records,
    "status": "pass" if all(row["status"] == "pass" for row in build_records) else "fail",
    "review_scope": "recorded two-pass compilation evidence and current final-log/page-count checks; not linguistic certification",
}

render_records = []
for cohort, pages in render_pages.items():
    for page in pages:
        try:
            width, height = png_dimensions(page)
        except ValueError as exc:
            errors.append(f"{page.relative_to(ROOT).as_posix()}: {exc}")
            width, height = 0, 0
        if width <= 0 or height <= 0:
            errors.append(f"{page.relative_to(ROOT).as_posix()} has nonpositive dimensions")
        render_records.append({
            "path": page.relative_to(ROOT).as_posix(),
            "bytes": page.stat().st_size,
            "sha256": sha(page),
            "width_px": width,
            "height_px": height,
        })

render_report = {
    "schema_version": "1.0.0",
    "work_unit": "NOE-P37",
    "recorded_at": checked_at,
    "dpi": 180,
    "page_counts": EXPECTED_RENDER_COUNTS,
    "render_count": len(render_records),
    "renders": render_records,
    "all_pages_individually_inspected": True,
    "inspection_attestation": args.inspector_note,
    "internal_visual_result": "pass",
    "observed_absences": [
        "clipping",
        "overlap",
        "missing glyph",
        "blank or duplicate page",
        "displaced formula",
        "broken hierarchy",
        "unreadable footnote",
        "page-number collision",
    ],
    "review_limits": "internal model visual inspection only; not external reader, regional-language, community, or human-expert certification",
}

(ROOT / "qa/BUILD_LOG.json").write_text(
    json.dumps(build_log, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
(ROOT / "qa/RENDER_VALIDATION_REPORT.json").write_text(
    json.dumps(render_report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)

decision_inventory = [
    {"path": path.relative_to(ROOT).as_posix(), "sha256": sha(path)}
    for path in sorted((ROOT / "decisions").glob("*.json"))
]
report = {
    "schema_version": "1.0.0",
    "work_unit": "NOE-P37",
    "checked_at": checked_at,
    "checker": {"path": "qa/run_freeze_checks.py", "sha256": sha(Path(__file__))},
    "authority": {
        "path": str(AUTHORITY),
        "sha256": authority_hash,
        "expected_sha256": EXPECTED_AUTHORITY,
        "stale_shared_pointer_used": False,
    },
    "file_hashes": file_hashes,
    "report_hashes": report_hashes,
    "decision_inventory": decision_inventory,
    "counts": {
        "typed_decisions": len(decision_inventory),
        "source_hans_structure": expected_structure,
        "hans_hant_ordered_math_spans": [15, 15],
        "local_structural_units": 48,
        "global_structural_records": 295,
        "global_paper37_records": 85,
        "difficulty_records": 22,
        "rendered_pages": len(render_records),
    },
    "build_log_path": "qa/BUILD_LOG.json",
    "build_log_sha256": sha(ROOT / "qa/BUILD_LOG.json"),
    "render_report_path": "qa/RENDER_VALIDATION_REPORT.json",
    "render_report_sha256": sha(ROOT / "qa/RENDER_VALIDATION_REPORT.json"),
    "warnings": warnings,
    "errors": errors,
    "status": "pass" if not errors else "fail",
    "review_limits": [
        "internal source/schema/build/render review only",
        "no external, community, or human-expert Chinese validation",
        "no zh-Hans-SG localization or validation",
        "controlled generic Hant is not Taiwan, Hong Kong, or Macao localization",
        "later transcription repairs are not represented as defects in the original German print",
        "no new original-print/body-text/formula defect was found by this freeze check",
        "SGA held and untouched",
    ],
    "witness_policy": "inherited_logical_witness is translation/adverse witness only and never source authority",
}
(ROOT / "qa/FREEZE_VALIDATION_REPORT.json").write_text(
    json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)

print(json.dumps({
    "path": str(ROOT / "qa/FREEZE_VALIDATION_REPORT.json"),
    "sha256": sha(ROOT / "qa/FREEZE_VALIDATION_REPORT.json"),
    "build_log_sha256": sha(ROOT / "qa/BUILD_LOG.json"),
    "render_report_sha256": sha(ROOT / "qa/RENDER_VALIDATION_REPORT.json"),
    "status": report["status"],
    "errors": len(errors),
}, ensure_ascii=False, indent=2))
raise SystemExit(1 if errors else 0)

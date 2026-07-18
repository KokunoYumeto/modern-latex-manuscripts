from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
import subprocess
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
QA = ROOT / "qa"
CONTROL = ROOT.parent / "00_lane_control"
LANE_REPORTS = ROOT.parent / "_agent_reports"
OUTPUT_PDF = ROOT.parents[3] / "output" / "pdf"

README = ROOT / "README.md"
CURSOR = ROOT / "CONTINUATION_CURSOR.md"
MATRIX = QA / "ACCEPTANCE_MATRIX_v11.md"
REPORT = ROOT / "_agent_reports" / "romance_acceptance_reaudit_v11.md"
MANIFEST_V11 = QA / "SHA256SUMS_v11.csv"
GATE_V11 = QA / "ROMANCE_ACCEPTANCE_GATE_v11.json"
GATE_LOG_V11 = QA / "ROMANCE_ACCEPTANCE_GATE_v11.log"

MANIFEST_V10 = QA / "SHA256SUMS_v10.csv"
GATE_V10 = QA / "ROMANCE_ACCEPTANCE_GATE_v10.json"
VALIDATOR_V10 = ROOT / "scripts" / "validate_romance_tranche_v10.py"
EXPECTED_V10 = {
    MANIFEST_V10: "2281E1FEBE190A5792524B881DED0E71706B82807F15D7DD34E45B631338935D",
    GATE_V10: "9A7F82D1FB2AC86DCB84A754A6C43E8255FA67DB426B71E0F33357DFC5733761",
    VALIDATOR_V10: "ECA42FDD7173CF32462E580E25B4682D14AF8E4657516E6D29E6DD105D71FC99",
}

MANAGER_VALIDATOR = CONTROL / "validate_manager_control_v2.py"
MANAGER_VALIDATION = CONTROL / "ROMANCE_MANAGER_CONTROL_VALIDATION_20260717.json"
MANAGER_MANIFEST = CONTROL / "ROMANCE_MANAGER_CONTROL_SHA256SUMS.csv"
MANAGER_TREE = CONTROL / "ROMANCE_FAMILY_COHORT_TREE_v2.json"
EXPECTED_COHORTS = [
    "C-ES-STD", "C-FR-STD", "C-PT-STD", "C-GL-STD", "C-CA-STD",
    "C-IT-STD", "C-RO-STD", "C-RM-RG", "C-RM-ID",
]

INTAKE = ROOT / "corpus" / "downloaded_curated" / "_intake_romansh_branch_acquisition_20260718"
INTAKE_VALIDATOR = INTAKE / "scripts" / "validate_intake.ps1"
INTAKE_VALIDATION = INTAKE / "qa" / "acquisition_intake_validation.json"
CORPUS_VALIDATOR = ROOT / "scripts" / "validate_corpus_branch_package_v3.py"
CORPUS_AUDIT = QA / "CORPUS_BRANCH_PACKAGE_AUDIT_v3.json"
CORPUS_V5 = ROOT / "corpus" / "ROMANCE_CONSOLIDATED_CORPUS_v5.csv"
BRANCH_V4 = ROOT / "corpus" / "ROMANCE_BRANCH_ROUTING_LEDGER_v4.csv"

PROFILE_VALIDATOR = ROOT / "scripts" / "validate_controlled_romance_spec_v3.py"
PROFILE_AUDIT = QA / "CONTROLLED_ROMANCE_LANGUAGE_PROFILE_AUDIT_v3.json"
PROFILE_SUMMARY = ROOT / "language" / "CONTROLLED_ROMANCE_LANGUAGE_PROFILE_T001_T008_v3.json"

RENDER_VALIDATOR = ROOT / "scripts" / "verify_pdf_renders_v12.py"
RENDER_REPORT = QA / "PDF_RENDER_REPRODUCIBILITY_v12.json"
RENDER_VISUAL = QA / "PDF_VISUAL_QA_v12.md"
EXPECTED_RENDER_REPORT = "CDE92C1D7A711379A871CB8E1D86D9A126036E3F7833A81878199FA5CDD005AF"

WORDWEB_V10 = ROOT / "wordweb" / "PAN_ROMANCE_WORDWEB_v10.json"
ACCESS_V10_JSON = ROOT / "access" / "PAN_ROMANCE_ACCESS_LEDGER_v10.json"
ACCESS_V10_CSV = ROOT / "access" / "PAN_ROMANCE_ACCESS_LEDGER_v10.csv"
MII_V10 = ROOT / "access" / "MII_METHOD_v10.md"
LINKS_V10_CSV = ROOT / "curation" / "CONTROLLED_ROMANCE_TERMINOLOGY_WORDWEB_LINKS_v10.csv"
LINKS_V10_JSON = ROOT / "curation" / "CONTROLLED_ROMANCE_TERMINOLOGY_WORDWEB_LINKS_v10.json"
CROSSWALK_V10_CSV = ROOT / "curation" / "NOETHER_ES_FR_WORDWEB_CROSSWALK_v10.csv"
CROSSWALK_V10_JSON = ROOT / "curation" / "NOETHER_ES_FR_WORDWEB_CROSSWALK_v10.json"
ALIGNMENT_V10 = QA / "ROMANCE_SEMANTIC_ALIGNMENT_v10.json"

WORDWEB_V11 = ROOT / "wordweb" / "PAN_ROMANCE_WORDWEB_v11.json"
ACCESS_V11_JSON = ROOT / "access" / "PAN_ROMANCE_ACCESS_LEDGER_v11.json"
ACCESS_V11_CSV = ROOT / "access" / "PAN_ROMANCE_ACCESS_LEDGER_v11.csv"
MII_V11 = ROOT / "access" / "MII_METHOD_v11.md"
SOURCE_AUDIT_V11_CSV = ROOT / "curation" / "WORDWEB_SOURCE_AUDIT_T10_T34_T35_T55_v11.csv"
SOURCE_AUDIT_V11_JSON = ROOT / "curation" / "WORDWEB_SOURCE_AUDIT_T10_T34_T35_T55_v11.json"
SOURCE_AUDIT_V11_MD = ROOT / "curation" / "WORDWEB_SOURCE_AUDIT_T10_T34_T35_T55_v11.md"
WORDWEB_BUILDER_V11 = ROOT / "scripts" / "build_wordweb_semantic_evidence_v11.py"
WORDWEB_VALIDATOR_V11 = ROOT / "scripts" / "validate_wordweb_semantic_evidence_v11.py"
WORDWEB_AUDIT_V11 = QA / "WORDWEB_SEMANTIC_EVIDENCE_AUDIT_v11.json"
WORDWEB_AUDIT_LOG_V11 = QA / "WORDWEB_SEMANTIC_EVIDENCE_AUDIT_v11.log"

EXPECTED_WORDWEB_V10 = "CF4521D7758C4B22E6260EA56BD04D57CF89B0F2083C70DDFE012BE50274F3E9"
EXPECTED_ACCESS_V10_JSON = "25F0724672E8C635E0CACE4F03579BAA46B0F4A3F86DEADAAE0AD1B802871236"
EXPECTED_ACCESS_V10_CSV = "277DFBBAB67C6161F491F93772FAD59472650F07A958B09043E98285C8F5436F"
EXPECTED_WORDWEB_V11 = "570822B02B2C713429C097CA526B87ACE39C2441A1DEB1B937E79FBA18303E26"
EXPECTED_ACCESS_V11_JSON = "2EB865261D3A769164EEAD60133B71E7D812419716CA9F9DD244C5593E1D92E3"
EXPECTED_ACCESS_V11_CSV = "463E66246A8EF22599689C0E58B985BD928BCA8D39015280AC554600100EF137"
EXPECTED_MII_V11 = "6B9E527E966F34EB9A6DB61FD743D54FB3BE073D0F3A8E98DD27B11B3910E861"
EXPECTED_OLD_ES_LEDGER = "395C18C21D53C3E439DF95891DE197866548F4EBD0D550453ED83D8CE7B5B9EA"
EXPECTED_OLD_FR_LEDGER = "0A7B1704481609CF5C4A8B3B7B5CC03EC59ADC4E511FF39D4A0D6AF910448B77"

TRANCHES = [f"R823_HG_T{i:03d}" for i in range(1, 9)]
SOURCE_RANGES = {
    "R823_HG_T001": "21047-21087",
    "R823_HG_T002": "21089-21097",
    "R823_HG_T003": "21099-21115",
    "R823_HG_T004": "21117-21146",
    "R823_HG_T005": "21148-21202",
    "R823_HG_T006": "21209-21254",
    "R823_HG_T007": "21256-21289",
    "R823_HG_T008": "21291-21307",
}
HUMAN_FIELDS = [
    "human_n", "human_correct", "human_incorrect", "human_abstain",
    "human_latency_ms", "human_confidence", "effect_interval",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def text_sha(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest().upper()


def rel(path: Path) -> str:
    return Path(path).resolve().relative_to(ROOT).as_posix()


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def csv_scalar(value) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


def csv_mirror_scalar(value) -> str:
    if isinstance(value, list):
        return ";".join(csv_scalar(item) for item in value)
    return csv_scalar(value)


def run_checked(label: str, command: list[str], cwd: Path = ROOT) -> dict:
    result = subprocess.run(command, cwd=cwd, text=True, capture_output=True)
    require(result.returncode == 0, f"{label} failed ({result.returncode}): {result.stdout}\n{result.stderr}")
    return {
        "label": label,
        "command": command,
        "exit_code": result.returncode,
        "stdout_tail": result.stdout.strip().splitlines()[-8:],
        "stderr": result.stderr.strip(),
    }


def verify_manifest_rows(manifest: Path, base: Path, allowed_mismatches: set[str] | None = None) -> tuple[list[dict[str, str]], list[str]]:
    rows = read_csv(manifest)
    require(rows and len(rows) == len({row.get("relative_path", row.get("path")) for row in rows}), f"duplicate/empty manifest labels: {manifest}")
    mismatches = []
    for row in rows:
        label = row.get("relative_path", row.get("path"))
        path = (base / label).resolve()
        if not path.exists() or path.stat().st_size != int(row["bytes"]) or sha(path) != row["sha256"].upper():
            mismatches.append(label)
    if allowed_mismatches is not None:
        require(set(mismatches) <= allowed_mismatches, f"unexpected manifest drift in {manifest}: {mismatches}")
    else:
        require(not mismatches, f"manifest drift in {manifest}: {mismatches}")
    return rows, mismatches


def write_manifest(rows: list[dict[str, str | int]]) -> None:
    with MANIFEST_V11.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["relative_path", "bytes", "sha256"], lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def validate_predecessor_v10() -> dict:
    for path, expected in EXPECTED_V10.items():
        require(path.exists() and sha(path) == expected, f"pinned v10 predecessor drift: {path}")
    rows, mismatches = verify_manifest_rows(
        MANIFEST_V10, ROOT, {"README.md", "CONTINUATION_CURSOR.md"}
    )
    require(len(rows) == 307, "v10 manifest row count changed")
    gate = read_json(GATE_V10)
    require(gate["artifact"] == "ROMANCE_ACCEPTANCE_GATE_v10", "wrong v10 gate artifact")
    require(gate["machine_validation"] == "PASS" and gate["goal_status"] == "ACTIVE_NOT_COMPLETE", "v10 predecessor boundary changed")
    require(gate["hash_target_count"] == 307 and gate["hash_manifest_sha256"] == sha(MANIFEST_V10), "v10 gate/manifest linkage failed")
    return {
        "gate_sha256": sha(GATE_V10),
        "manifest_sha256": sha(MANIFEST_V10),
        "manifest_rows": len(rows),
        "mutable_successor_pointer_paths": mismatches,
    }


def validate_manager() -> dict:
    validation = read_json(MANAGER_VALIDATION)
    tree = read_json(MANAGER_TREE)
    rows, _ = verify_manifest_rows(MANAGER_MANIFEST, CONTROL)
    actual_ids = [row["cohort_id"] for row in tree["reader_cohorts"]]
    root_leaves = [leaf for branch in tree["root"]["children"] for leaf in branch.get("children", [])]
    require(validation["pass"] is True and all(validation["semantic_checks"].values()) and all(validation["structural_checks"].values()), "manager validation not semantically PASS")
    require(len(rows) == validation["sha_manifest_design"]["managed_artifact_count"] == 9, "manager manifest shape changed")
    require(actual_ids == EXPECTED_COHORTS and set(root_leaves) == set(EXPECTED_COHORTS) and len(root_leaves) == 9, "manager cohort topology changed")
    require(tree["artifact"] == "ROMANCE_FAMILY_COHORT_TREE_v2" and tree["cohort_count"] == 9, "manager v2 tree identity/count failed")
    require(tree["romansh_distinction"]["current_human_observations"] == 0, "manager human-observation leak")
    require(tree["dependence_policy"]["scalar_readiness_allowed"] is False and tree["dependence_policy"]["MII_result_feeds_decisions"] is False, "manager scalar/MII decision leak")
    return {
        "manager_manifest_rows": len(rows),
        "manager_manifest_sha256": sha(MANAGER_MANIFEST),
        "validation_sha256": sha(MANAGER_VALIDATION),
        "tree_sha256": sha(MANAGER_TREE),
        "cohort_ids": actual_ids,
    }


def validate_corpus() -> dict:
    audit = read_json(CORPUS_AUDIT)
    intake = read_json(INTAKE_VALIDATION)
    require(audit["status"] == "PASS" and audit["check_count"] == audit["passed_check_count"] == 36 and all(audit["checks"].values()), "corpus audit not 36/36 PASS")
    require(intake["machine_status"] == "PASS" and intake["check_count"] == intake["passed_check_count"] == 31, "Romansh intake not 31/31 PASS")
    for row in intake["hash_targets"]:
        path = INTAKE / row["path"]
        require(path.exists() and path.stat().st_size == int(row["bytes"]) and sha(path) == row["sha256"].upper(), f"intake target drift: {row['path']}")

    corpus = read_csv(CORPUS_V5)
    branch = read_csv(BRANCH_V4)
    primary = [row for row in corpus if row["dedupe_status"] == "primary_unique"]
    aliases = [row for row in corpus if "representation_alias" in row["dedupe_status"]]
    counting = [row for row in corpus if row["counting_eligible"] == "true"]
    active = [row for row in corpus if row["active_body_eligible"] == "true"]
    require((len(corpus), len(primary), len(aliases), len(counting), len(active)) == (153, 147, 6, 71, 70), "corpus v5 totals changed")
    active_routes = [row for row in branch if int(row["current_active_body_count"]) > 0]
    zero_routes = [row for row in branch if int(row["current_active_body_count"]) == 0]
    require((len(branch), len(active_routes), len(zero_routes)) == (61, 11, 50), "branch v4 route totals changed")
    rm = {row["variety_code"]: row for row in branch if row["variety_code"].startswith("rm-")}
    require({key: int(row["current_active_body_count"]) for key, row in rm.items()} == {
        "rm-rg": 4, "rm-puter": 1, "rm-sursilvan": 1, "rm-vallader": 1,
        "rm-sutsilvan": 0, "rm-surmiran": 0,
    }, "Romansh route body counts changed")
    require(all(int(row["current_specialist_algebra_body_count"]) == 0 for row in rm.values()), "Romansh specialist-algebra claim leak")

    intake_manifest = read_json(INTAKE / "manifests" / "intake_manifest.json")
    accepted = [row for row in intake_manifest["records"] if row["decision"] == "accepted"]
    require(len(accepted) == 4 and sum(int(row["page_count"]) for row in accepted) == 60, "accepted Romansh body/page count changed")
    require(all("unresolved" in row["license_status"] and not row["specialist_algebra_eligible"] and not row["term_promotion_eligible"] for row in accepted), "Romansh rights/domain/promotion boundary changed")
    return {
        "audit_sha256": sha(CORPUS_AUDIT),
        "intake_validation_sha256": sha(INTAKE_VALIDATION),
        "corpus": {"records": 153, "primary": 147, "aliases": 6, "counting": 71, "active": 70},
        "routes": {"total": 61, "active": 11, "zero": 50},
        "romansh_general_school_pages": 60,
        "romansh_specialist_algebra_bodies": 0,
        "rights_status": "UNRESOLVED_NOT_PUBLICATION_CLEARED",
    }


def reconstruct_crosswalk() -> dict:
    rows = read_csv(CROSSWALK_V10_CSV)
    mirror = read_json(CROSSWALK_V10_JSON)
    require(len(rows) == 194 and mirror["rows"] == rows and mirror["row_count"] == 194, "crosswalk CSV/JSON mismatch")
    require([row["crosswalk_id"] for row in rows[:101]] == [f"ES-{i:03d}" for i in range(1, 102)], "Spanish crosswalk IDs changed")
    require([row["crosswalk_id"] for row in rows[101:]] == [f"FR-{i:03d}" for i in range(1, 94)], "French crosswalk IDs changed")
    expected_fields = {
        "es": ["source_term", "target_term", "sense", "status", "source_evidence", "source_excerpt", "german_source_evidence", "decision_note"],
        "fr": ["source_term", "target_term", "sense", "status", "source_evidence"],
    }
    for row in rows:
        frozen = {field: row[field] for field in expected_fields[row["language"]]}
        require(text_sha(json.dumps(frozen, ensure_ascii=False, sort_keys=True, separators=(",", ":"))) == row["production_row_sha256"], f"crosswalk frozen row hash mismatch: {row['crosswalk_id']}")
        expected_ledger = EXPECTED_OLD_ES_LEDGER if row["language"] == "es" else EXPECTED_OLD_FR_LEDGER
        require(row["production_ledger_sha256"] == expected_ledger, f"crosswalk frozen ledger identity drift: {row['crosswalk_id']}")
        require(row["attestation_effect"].startswith("none") and row["promotion_effect"] == "none" and row["human_or_MII_effect"] == "none", f"crosswalk claim leak: {row['crosswalk_id']}")
    counts = {
        lang: dict(Counter(row["mapping_status"] for row in rows if row["language"] == lang))
        for lang in ("es", "fr")
    }
    require(counts == {"es": {"mapped": 61, "unmapped_explicit": 40}, "fr": {"unmapped_explicit": 84, "mapped": 9}}, "crosswalk mapping counts changed")
    require(mirror["mapping_status_counts"] == counts and mirror["language_rows"] == {"es": 101, "fr": 93}, "crosswalk mirror counts changed")
    return {"rows": 194, "language_rows": {"es": 101, "fr": 93}, "mapping_status_counts": counts}


def validate_wordweb_access() -> dict:
    require(sha(WORDWEB_V10) == EXPECTED_WORDWEB_V10, "WordWeb v10 drift")
    require(sha(ACCESS_V10_JSON) == EXPECTED_ACCESS_V10_JSON and sha(ACCESS_V10_CSV) == EXPECTED_ACCESS_V10_CSV, "access v10 drift")
    wordweb = read_json(WORDWEB_V10)
    access = read_json(ACCESS_V10_JSON)
    access_csv = read_csv(ACCESS_V10_CSV)
    require((len(wordweb["core_concepts"]), len(wordweb["senses"]), len(wordweb["c2_extension_nodes"]), len(wordweb["evidence_records"])) == (60, 106, 39, 802), "WordWeb v10 topology changed")
    term_ids = {row["term_id"] for row in wordweb["core_concepts"]}
    sense_ids = {row["sense_id"] for row in wordweb["senses"]}
    c2_ids = {row["concept_id"] for row in wordweb["c2_extension_nodes"]}
    evidence_ids = [row["evidence_id"] for row in wordweb["evidence_records"]]
    require(len(term_ids) == 60 and len(sense_ids) == 106 and len(c2_ids) == 39 and len(evidence_ids) == len(set(evidence_ids)) == 802, "WordWeb IDs not unique")
    require(all(row["term_id"] in term_ids for row in wordweb["senses"]), "sense-to-concept membership unresolved")
    require(sum(len(row["sense_ids"]) for row in wordweb["core_concepts"]) == 106, "concept-to-sense membership count changed")
    supported = sum(bool(row["reviewed_supporting_occurrence_evidence_ids"]) for row in wordweb["senses"])
    require(supported == 73, "accepted sense support count changed")
    inherited = [row for row in wordweb["evidence_records"] if row["source_type"] == "union_spine_locator_claim"]
    require(len(inherited) == 120 and all(row.get("quote") is None and row.get("acceptance") == "unresolved_locator" for row in inherited), "core inherited-evidence boundary changed")
    relations = [relation for core in wordweb["core_concepts"] for relation in core.get("relations", [])]
    valid_nodes = term_ids | sense_ids | c2_ids
    valid_edges = [row for row in relations if row.get("target_id") in valid_nodes]
    invalid_edges = [row for row in relations if row.get("target_id") and row.get("target_id") not in valid_nodes]
    no_target = [row for row in relations if not row.get("target_id")]
    require((len(relations), len(valid_edges), len(invalid_edges), len(no_target)) == (402, 27, 0, 375), "WordWeb relation metrics changed")
    require(wordweb["relation_metrics"] == {
        "relation_records": 402,
        "valid_target_id_edges": 27,
        "invalid_target_id_edges": 0,
        "relation_records_without_target_id": 375,
        "concept_to_sense_membership_edges": 106,
        "total_id_resolved_references_including_memberships": 133,
        "reporting_boundary": "Relation records include descriptive/label relations without target IDs; they are not all graph edges. Any nonempty invalid target ID is a build error.",
    }, "WordWeb relation-metric declaration drift")
    relation_types = {row["type"] for row in relations}
    require({"derivation_or_compound", "language_variant_set", "historical_modern_register", "adverse_false_friend", "source_gloss_alias"} <= relation_types, "WordWeb required relation classes missing")
    require(len(wordweb["decisions"]) == 106 and all(row["pilot_eligible"] is False and row["human_validation_required"] is True for row in wordweb["decisions"]), "WordWeb decision claim boundary changed")

    require(len(access["rows"]) == len(access_csv) == 954 and access["row_count"] == 954 and access["sense_count"] == 106, "access grid shape changed")
    cohort_ids = [row["cohort_id"] for row in access["cohorts"]]
    require(cohort_ids == EXPECTED_COHORTS, "access cohort topology differs from manager")
    require(access["canonical_cohort_topology"]["sha256"] == sha(MANAGER_TREE) and access["canonical_cohort_topology"]["cohort_ids"] == EXPECTED_COHORTS, "access manager-tree binding failed")
    observed_pairs = {(row["sense_id"], row["cohort_id"]) for row in access["rows"]}
    require(observed_pairs == {(sense, cohort) for sense in sense_ids for cohort in EXPECTED_COHORTS}, "access grid is not exact 106x9 product")
    for json_row, csv_row in zip(access["rows"], access_csv, strict=True):
        require({key: csv_scalar(value) for key, value in json_row.items()} == csv_row, "access JSON/CSV row mismatch")
        require(all(json_row[field] is None for field in HUMAN_FIELDS) and json_row["pilot_eligible"] is False, "access human/pilot field leak")
    require(access["human_observation_count"] == access["pilot_eligible_count"] == access["form_promotion_count"] == 0, "access aggregate claim leak")
    method = MII_V10.read_text(encoding="utf-8").casefold()
    require(all(phrase in method for phrase in ["zero human observations", "954", "do not measure intelligibility", "no empirical-mii"]), "MII method boundary incomplete")

    sys.path.insert(0, str(ROOT / "scripts"))
    import validate_romance_tranche_v10 as v10  # noqa: PLC0415
    v9_core = v10.v9.validate_core(False)
    wordweb_v9 = v10.jread(v10.WORDWEB_V9)
    links = v10.validate_links(wordweb_v9)
    t006 = v10.validate_t006()
    successors = v10.validate_successors(wordweb_v9, links, reconstruct_crosswalk())
    v10.validate_audit(links, reconstruct_crosswalk(), successors)
    require(v9_core["stage_d"]["next_authority_line"] == 21256, "v9 production predecessor cursor changed")
    audit = read_json(ALIGNMENT_V10)
    require(audit["status"] == "PASS" and audit["wordweb_v10"]["supported_senses"] == 73 and audit["wordweb_v10"]["unsupported_senses"] == 33, "v10 alignment audit changed")

    require(sha(WORDWEB_V11) == EXPECTED_WORDWEB_V11, "WordWeb v11 drift")
    require(sha(ACCESS_V11_JSON) == EXPECTED_ACCESS_V11_JSON and sha(ACCESS_V11_CSV) == EXPECTED_ACCESS_V11_CSV, "access v11 drift")
    require(sha(MII_V11) == EXPECTED_MII_V11, "MII v11 drift")
    ww11 = read_json(WORDWEB_V11)
    ac11 = read_json(ACCESS_V11_JSON)
    ac11_csv = read_csv(ACCESS_V11_CSV)
    audit11 = read_json(WORDWEB_AUDIT_V11)
    require(audit11["status"] == "PASS" and audit11["checks_total"] == audit11["checks_passed"] == 34 and all(audit11["checks"].values()), "WordWeb v11 audit not 34/34 PASS")
    require(ww11["artifact"] == "PAN_ROMANCE_WORDWEB_v11" and ww11["supersedes_for_semantic_use"] == "PAN_ROMANCE_WORDWEB_v10", "WordWeb v11 predecessor link failed")
    require((len(ww11["core_concepts"]), len(ww11["senses"]), len(ww11["c2_extension_nodes"]), len(ww11["evidence_records"])) == (60, 106, 39, 811), "WordWeb v11 topology changed")
    require([row["term_id"] for row in ww11["core_concepts"]] == [row["term_id"] for row in wordweb["core_concepts"]] and [row["sense_id"] for row in ww11["senses"]] == [row["sense_id"] for row in wordweb["senses"]], "WordWeb v11 IDs differ from v10")
    v11_evidence_ids = [row["evidence_id"] for row in ww11["evidence_records"]]
    require(len(v11_evidence_ids) == len(set(v11_evidence_ids)) == 811, "WordWeb v11 evidence IDs not unique")
    inherited11 = [row for row in ww11["evidence_records"] if row["source_type"] == "union_spine_locator_claim"]
    require(len(inherited11) == 120 and all(row.get("quote") is None and row.get("acceptance") == "unresolved_locator" for row in inherited11), "WordWeb v11 inherited quotation-free core boundary changed")
    supported11 = {
        row["sense_id"] for row in ww11["senses"]
        if row.get("reviewed_supporting_occurrence_evidence_ids") or row.get("source_audited_support_evidence_ids_v11")
    }
    require(len(supported11) == 78 and len(ww11["senses"]) - len(supported11) == 28, "WordWeb v11 support split changed")
    require({"T10-S1", "T10-S2", "T34-S1", "T35-S1", "T55-S1"} <= supported11, "WordWeb v11 exact new support missing")
    senses11 = {row["sense_id"]: row for row in ww11["senses"]}
    require(senses11["T35-S2"]["source_audited_support_evidence_ids_v11"] == ["E-OCC-1351B5D65CB3CD74"], "T35-S2 revalidation changed")
    require(not senses11["T35-S3"].get("source_audited_support_evidence_ids_v11") and not senses11["T55-S2"].get("source_audited_support_evidence_ids_v11"), "cross-sense adverse boundary leaked")
    relations11 = [relation for core in ww11["core_concepts"] for relation in core.get("relations", [])]
    valid_nodes11 = {row["term_id"] for row in ww11["core_concepts"]} | {row["sense_id"] for row in ww11["senses"]} | {row["concept_id"] for row in ww11["c2_extension_nodes"]}
    valid_edges11 = [row for row in relations11 if row.get("target_id") in valid_nodes11]
    invalid_edges11 = [row for row in relations11 if row.get("target_id") and row.get("target_id") not in valid_nodes11]
    no_target11 = [row for row in relations11 if not row.get("target_id")]
    require((len(relations11), len(valid_edges11), len(invalid_edges11), len(no_target11)) == (406, 27, 0, 379), "WordWeb v11 relation metrics changed")
    require(ww11["relation_metrics"]["concept_to_sense_membership_edges"] == 106 and ww11["relation_metrics"]["total_id_resolved_references_including_memberships"] == 133, "WordWeb v11 ID-reference metrics changed")
    require(len(ww11["decisions"]) == 106 and all(row["pilot_eligible"] is False and row["human_validation_required"] is True for row in ww11["decisions"]), "WordWeb v11 decision claim boundary changed")

    require(ac11["artifact"] == "PAN_ROMANCE_ACCESS_LEDGER_v11" and ac11["supersedes"] == "PAN_ROMANCE_ACCESS_LEDGER_v10", "access v11 predecessor link failed")
    require(len(ac11["rows"]) == len(ac11_csv) == ac11["row_count"] == 954 and ac11["sense_count"] == 106, "access v11 shape changed")
    require([row["cohort_id"] for row in ac11["cohorts"]] == EXPECTED_COHORTS, "access v11 cohort topology differs from manager")
    require(ac11["canonical_cohort_topology"]["sha256"] == sha(MANAGER_TREE), "access v11 manager tree hash mismatch")
    require({(row["sense_id"], row["cohort_id"]) for row in ac11["rows"]} == {(sense, cohort) for sense in sense_ids for cohort in EXPECTED_COHORTS}, "access v11 is not exact 106x9 product")
    for json_row, csv_row in zip(ac11["rows"], ac11_csv, strict=True):
        require({key: csv_scalar(value) for key, value in json_row.items()} == csv_row, "access v11 JSON/CSV mismatch")
        require(all(json_row[field] is None for field in HUMAN_FIELDS) and json_row["pilot_eligible"] is False and json_row["source_audit_v11_human_observations"] == 0, "access v11 human/pilot claim leak")
    require(ac11["human_observation_count"] == ac11["pilot_eligible_count"] == ac11["form_promotion_count"] == 0, "access v11 aggregate claim leak")
    method11 = MII_V11.read_text(encoding="utf-8")
    require("106 senses × 9 cohorts = 954 rows" in method11 and "zero human observations" in method11 and "do not measure comprehension or intelligibility" in method11, "MII v11 boundary incomplete")

    source_audit = read_json(SOURCE_AUDIT_V11_JSON)
    source_audit_csv = read_csv(SOURCE_AUDIT_V11_CSV)
    require(len(source_audit["rows"]) == len(source_audit_csv) == 10 and all({key: csv_mirror_scalar(value) for key, value in json_row.items()} == csv_row for json_row, csv_row in zip(source_audit["rows"], source_audit_csv, strict=True)) and source_audit["audit_rows"] == 10 and source_audit["accepted_exact_rows"] == 8 and source_audit["rejected_scope_mismatch_rows"] == 1 and source_audit["revalidated_existing_rows"] == 1, "WordWeb v11 source-audit mirror/counts changed")
    for row in source_audit["rows"]:
        source_path = Path(row["source_path"])
        require(source_path.exists() and sha(source_path) == row["source_sha256"], f"WordWeb v11 source drift: {row['audit_id']}")
        body = source_path.read_text(encoding="utf-8-sig").splitlines()
        quote = "\n".join(body[int(row["line_start"]) - 1:int(row["line_end"])])
        require(quote == row["quote"] and text_sha(quote) == row["quote_sha256"], f"WordWeb v11 source range/quote mismatch: {row['audit_id']}")
        require(("unresolved" in row["license_status"] or "not_reuse_cleared" in row["license_status"]) and not row["human_observation"] and not row["pilot_claim"] and not row["core_form_promotion"] and not row["bridge_form_promotion"], f"WordWeb v11 rights/claim boundary changed: {row['audit_id']}")
    return {
        "version": "v11",
        "wordweb_sha256": sha(WORDWEB_V11),
        "access_json_sha256": sha(ACCESS_V11_JSON),
        "access_csv_sha256": sha(ACCESS_V11_CSV),
        "concepts": 60,
        "senses": 106,
        "c2_nodes": 39,
        "evidence_records": 811,
        "reviewed_occurrences": 682,
        "source_audited_evidence_records_v11": 9,
        "supported_senses": 78,
        "unsupported_senses": 28,
        "relation_records": 406,
        "relation_records_without_target_id": 379,
        "valid_target_id_edges": 27,
        "concept_to_sense_memberships": 106,
        "total_id_resolved_references": 133,
        "access_rows": 954,
        "human_observations": 0,
        "form_promotions": 0,
        "link_rows": links["rows"],
        "link_corrections": links["corrections"],
        "t006_metadata": t006,
        "crosswalk": reconstruct_crosswalk(),
        "wordweb_evidence_audit_sha256": sha(WORDWEB_AUDIT_V11),
        "source_audit_rows": 10,
        "source_audit_rights_status": "UNRESOLVED_NOT_DIRECT_PUBLIC_PAYLOAD",
        "frozen_crosswalk_source_boundary": "All 194 preserved rows reproduce their row hashes. The live external French production ledger has moved beyond the v10-pinned 0A7B snapshot, so v11 does not claim byte-replay from that mutable external path.",
    }


def extract_exact_source(manifest: dict, exact_path: Path) -> bool:
    authority = Path(manifest["authority_path"])
    lines = authority.read_text(encoding="utf-8").splitlines(keepends=True)
    start, end = int(manifest["line_start"]), int(manifest["line_end"])
    return "".join(lines[start - 1:end]).encode("utf-8") == exact_path.read_bytes()


def validate_t007() -> dict:
    t = ROOT / "R823_HG_T007"
    data = read_json(t / "qa" / "R823_HG_T007_validation.json")
    manifest = read_json(t / "source" / "R823_HG_T007_SOURCE_MANIFEST.json")
    require(data["status"] == "PASS_INTERNAL_MECHANICAL_AND_SOURCE_CONTROLS", "T007 validator status changed")
    require(manifest["line_start"] == 21256 and manifest["line_end"] == 21289 and manifest["next_line"] == 21291, "T007 source range changed")
    require(sha(Path(manifest["authority_path"])) == manifest["authority_sha256"] == data["authority_sha256"], "T007 authority drift")
    require(extract_exact_source(manifest, t / "source" / "R823_HG_T007_de_exact.tex"), "T007 exact source slice not reproducible")
    mapping = {
        "authority_slice_sha256": t / "source" / "R823_HG_T007_de_exact.tex",
        "numbered_source_sha256": t / "source" / "R823_HG_T007_de_numbered.txt",
        "source_metadata_sha256": t / "source" / "R823_HG_T007_SOURCE_METADATA.json",
        "source_manifest_sha256": t / "source" / "R823_HG_T007_SOURCE_MANIFEST.json",
        "target_tex_sha256": t / "tex" / "R823_HG_T007_romance.tex",
        "pdf_sha256": t / "build" / "R823_HG_T007_romance.pdf",
        "repeat_pdf_sha256": t / "build_repeat" / "R823_HG_T007_romance.pdf",
        "output_pdf_sha256": OUTPUT_PDF / "R823_HG_T007_controlled_romance.pdf",
        "clause_seed_sha256": t / "semantic" / "R823_HG_T007_clause_map_seed.csv",
        "clause_map_sha256": t / "semantic" / "R823_HG_T007_clause_map.csv",
        "terminology_sha256": t / "terminology" / "R823_HG_T007_TERMINOLOGY_v1.csv",
        "grammar_delta_sha256": t / "grammar" / "CONTROLLED_ROMANCE_GRAMMAR_T007_DELTA_v1.csv",
        "wordweb_v10_sha256": WORDWEB_V10,
        "effective_wordweb_link_contract_v10_sha256": LINKS_V10_JSON,
        "access_ledger_v10_sha256": ACCESS_V10_JSON,
        "extracted_text_sha256": t / "qa" / "R823_HG_T007_extracted.txt",
        "pdfinfo_sha256": t / "qa" / "R823_HG_T007_pdfinfo.txt",
        "final_lualatex_log_sha256": t / "build" / "R823_HG_T007_romance.log",
        "lualatex_console_sha256": t / "build" / "R823_HG_T007_lualatex_console.log",
        "lualatex_pass1_sha256": t / "build" / "R823_HG_T007_lualatex_pass1.log",
        "repeat_final_lualatex_log_sha256": t / "build_repeat" / "R823_HG_T007_romance.log",
        "repeat_lualatex_console_sha256": t / "build_repeat" / "R823_HG_T007_lualatex_console.log",
        "repeat_lualatex_pass1_sha256": t / "build_repeat" / "R823_HG_T007_lualatex_pass1.log",
        "prepare_script_sha256": t / "scripts" / "prepare_source.py",
        "build_script_sha256": t / "scripts" / "build_t007.ps1",
        "validator_sha256": t / "scripts" / "validate_t007.py",
        "visual_qa_sha256": t / "qa" / "R823_HG_T007_VISUAL_QA.md",
        "continuation_cursor_sha256": t / "CONTINUATION_CURSOR.md",
    }
    require(all(sha(path) == data[key] for key, path in mapping.items()), "T007 embedded hash mismatch")
    for name, digest in data["rendered_page_sha256"].items():
        require(sha(t / "qa" / "rendered" / name) == digest, f"T007 render drift: {name}")
    require(data["page_count"] == 2 and data["human_observations"] == 0 and data["native_validation"] is False and data["pilot_claim"] is False and data["whole_work_completion_claim"] is False, "T007 claim boundary changed")
    require((t / "build" / "R823_HG_T007_romance.pdf").read_bytes() == (t / "build_repeat" / "R823_HG_T007_romance.pdf").read_bytes() == (OUTPUT_PDF / "R823_HG_T007_controlled_romance.pdf").read_bytes(), "T007 PDF copies differ")
    return {"validation_sha256": sha(t / "qa" / "R823_HG_T007_validation.json"), "source_slice_sha256": data["authority_slice_sha256"], "pdf_sha256": data["pdf_sha256"], "pages": 2}


def validate_t008() -> dict:
    t = ROOT / "R823_HG_T008"
    data = read_json(t / "qa" / "R823_HG_T008_validation.json")
    manifest = read_json(t / "source" / "R823_HG_T008_SOURCE_MANIFEST.json")
    require(data["status"] == "PASS_BOUNDED_PROVISIONAL_UNIT_ONLY" and all(data["checks"].values()), "T008 validator not semantically PASS")
    require(manifest["line_start"] == 21291 and manifest["line_end"] == 21307 and manifest["next_line"] == 21309, "T008 source range changed")
    require(sha(Path(manifest["authority_path"])) == manifest["authority_sha256"] == data["authority_sha256"], "T008 authority drift")
    require(extract_exact_source(manifest, t / "source" / "R823_HG_T008_de_exact.tex"), "T008 exact source slice not reproducible")
    mapping = {
        "source_exact": t / "source" / "R823_HG_T008_de_exact.tex",
        "source_numbered": t / "source" / "R823_HG_T008_de_numbered.txt",
        "source_metadata": t / "source" / "R823_HG_T008_SOURCE_METADATA.json",
        "source_manifest": t / "source" / "R823_HG_T008_SOURCE_MANIFEST.json",
        "clause_seed": t / "semantic" / "R823_HG_T008_clause_map_seed.csv",
        "clause_map": t / "semantic" / "R823_HG_T008_clause_map.csv",
        "terminology": t / "terminology" / "R823_HG_T008_TERMINOLOGY_v1.csv",
        "grammar": t / "grammar" / "CONTROLLED_ROMANCE_GRAMMAR_T008_DELTA_v1.csv",
        "wordweb_v10": WORDWEB_V10,
        "effective_links_v10": LINKS_V10_JSON,
        "access_ledger_v10": ACCESS_V10_JSON,
        "target_tex": t / "tex" / "R823_HG_T008_romance.tex",
        "prepare_script": t / "scripts" / "prepare_source.py",
        "build_script": t / "scripts" / "build_t008.ps1",
        "validator_script": t / "scripts" / "validate_t008.py",
        "build_pdf": t / "build" / "R823_HG_T008_romance.pdf",
        "repeat_pdf": t / "build_repeat" / "R823_HG_T008_romance.pdf",
        "output_pdf": OUTPUT_PDF / "R823_HG_T008_controlled_romance.pdf",
        "extracted_text": t / "qa" / "R823_HG_T008_extracted.txt",
        "pdfinfo": t / "qa" / "R823_HG_T008_pdfinfo.txt",
        "build_tex_log": t / "build" / "R823_HG_T008_romance.log",
        "repeat_tex_log": t / "build_repeat" / "R823_HG_T008_romance.log",
        "build_console_log": t / "build" / "R823_HG_T008_lualatex_console.log",
        "build_passone_log": t / "build" / "R823_HG_T008_lualatex_pass1.log",
        "repeat_console_log": t / "build_repeat" / "R823_HG_T008_lualatex_console.log",
        "repeat_passone_log": t / "build_repeat" / "R823_HG_T008_lualatex_pass1.log",
        "visual_qa": t / "qa" / "R823_HG_T008_VISUAL_QA.md",
        "cursor": t / "CONTINUATION_CURSOR.md",
    }
    require(all(sha(path) == data["hashes"][key] for key, path in mapping.items()), "T008 embedded hash mismatch")
    for name, digest in data["render_sha256"].items():
        require(sha(t / "qa" / "rendered" / name) == digest, f"T008 render drift: {name}")
    tex = (t / "tex" / "R823_HG_T008_romance.tex").read_text(encoding="utf-8")
    require("iste es contenite" in tex and not re.search(r"(?<![\w])istes(?![\w])", tex, re.IGNORECASE), "T008 invariant iste repair absent")
    require(data["counts"]["pdf_pages"] == 2 and data["counts"]["human_observations"] == data["counts"]["term_promotions"] == 0, "T008 count/claim boundary changed")
    require((t / "build" / "R823_HG_T008_romance.pdf").read_bytes() == (t / "build_repeat" / "R823_HG_T008_romance.pdf").read_bytes() == (OUTPUT_PDF / "R823_HG_T008_controlled_romance.pdf").read_bytes(), "T008 PDF copies differ")
    return {"validation_sha256": sha(t / "qa" / "R823_HG_T008_validation.json"), "source_slice_sha256": data["authority_slice_sha256"], "pdf_sha256": data["hashes"]["build_pdf"], "pages": 2, "invariant_iste": "PASS"}


def validate_profile() -> dict:
    audit = read_json(PROFILE_AUDIT)
    summary = read_json(PROFILE_SUMMARY)
    require(audit["status"] == "PASS" and audit["counts"]["checks"] == audit["counts"]["checks_passed"] == 58 and all(audit["checks"].values()), "language profile v3 not 58/58 PASS")
    counts = audit["counts"]
    require((counts["grammar_decisions"], counts["function_word_decisions"], counts["terminology_decisions"]) == (65, 63, 147), "language profile decision counts changed")
    require((counts["linked_terminology_rows"], counts["explicitly_unlinked_terminology_rows"], counts["effective_wordweb_identifier_references"]) == (122, 25, 148), "language profile link counts changed")
    require(counts["source_keyed_tranches"] == 8 and counts["rendered_pages"] == 19 and summary["next_source_line"] == 21309, "language profile production surface changed")
    require(counts["human_observations"] == counts["native_validations"] == counts["form_promotions"] == 0, "language profile empirical claim leak")
    require(summary["empirical_claim_boundary"] == {"human_observations": 0, "native_validated": False, "intelligibility_claim": False, "MII_claim": False, "pilot_claim": False, "full_R823_translation_claim": False}, "language profile claim boundary changed")
    for label, digest in audit["artifact_hashes"].items():
        require((ROOT / label).exists() and sha(ROOT / label) == digest, f"language profile artifact drift: {label}")
    return {"audit_sha256": sha(PROFILE_AUDIT), "counts": {key: counts[key] for key in ["grammar_decisions", "function_word_decisions", "terminology_decisions", "linked_terminology_rows", "explicitly_unlinked_terminology_rows", "effective_wordweb_identifier_references", "source_keyed_tranches", "rendered_pages"]}, "next_source_line": 21309, "human_observations": 0}


def validate_render() -> dict:
    require(sha(RENDER_REPORT) == EXPECTED_RENDER_REPORT, "render v12 report drift")
    data = read_json(RENDER_REPORT)
    expected = {"tranches": 8, "build_pdfs": 8, "final_output_pdfs": 8, "pinned_pages": 19, "fresh_pages": 19, "all_build_output_pdfs_byte_identical": True, "all_fresh_pinned_pngs_byte_identical": True}
    require(data["status"] == "PASS" and data["totals"] == expected, "render v12 totals changed")
    require([row["tranche"] for row in data["tranches"]] == TRANCHES, "render v12 tranche order changed")
    for row in data["tranches"]:
        tranche = row["tranche"]
        require(row["build_pdf"]["sha256"] == sha(ROOT / tranche / "build" / f"{tranche}_romance.pdf"), f"render build PDF drift: {tranche}")
        require(row["final_output_pdf"]["sha256"] == sha(OUTPUT_PDF / f"{tranche}_controlled_romance.pdf"), f"render output PDF drift: {tranche}")
        for page in row["pages"]:
            require(page["pinned_render"]["sha256"] == page["fresh_render_sha256"] and page["hash_match"] is True and page["byte_identical"] is True, f"fresh/pinned render mismatch: {tranche}")
    return {"report_sha256": sha(RENDER_REPORT), "visual_note_sha256": sha(RENDER_VISUAL), "pages": 19, "outputs": 8}


def run_dependencies() -> list[dict]:
    powershell = shutil.which("pwsh") or shutil.which("powershell") or "powershell"
    return [
        run_checked("manager_control_v2", [sys.executable, str(MANAGER_VALIDATOR)], CONTROL),
        run_checked("romansh_intake", [powershell, "-NoProfile", "-File", str(INTAKE_VALIDATOR)], INTAKE),
        run_checked("corpus_branch_v3", [sys.executable, str(CORPUS_VALIDATOR)]),
        run_checked("wordweb_evidence_builder_v11", [sys.executable, str(WORDWEB_BUILDER_V11)]),
        run_checked("wordweb_evidence_validator_v11", [sys.executable, str(WORDWEB_VALIDATOR_V11)]),
        run_checked("T007", [sys.executable, str(ROOT / "R823_HG_T007" / "scripts" / "validate_t007.py")]),
        run_checked("T008", [sys.executable, str(ROOT / "R823_HG_T008" / "scripts" / "validate_t008.py")]),
        run_checked("render_v12", [sys.executable, str(RENDER_VALIDATOR)]),
        run_checked("language_profile_v3", [sys.executable, str(PROFILE_VALIDATOR)]),
    ]


def add_target(targets: dict[str, Path], path: Path, label: str | None = None) -> None:
    if label is None:
        try:
            label = path.resolve().relative_to(ROOT).as_posix()
        except ValueError:
            label = Path(shutil.os.path.relpath(path.resolve(), ROOT)).as_posix()
    targets[label] = path.resolve()


def build_manifest() -> list[dict[str, str | int]]:
    targets = {
        row["relative_path"]: (ROOT / row["relative_path"]).resolve()
        for row in read_csv(MANIFEST_V10)
        if row["relative_path"] not in {"README.md", "CONTINUATION_CURSOR.md"}
    }
    for path in [README, CURSOR, MATRIX, REPORT, GATE_V10, MANIFEST_V10, Path(__file__).resolve()]:
        add_target(targets, path)

    for path in [
        CONTROL / "ROMANCE_MANAGER_README_20260717.md",
        CONTROL / "WORK_CORPUS_LOCATION_REGISTER_v1.csv",
        CONTROL / "DISK_WORK_ROOT_INVENTORY_v1.csv",
        CONTROL / "ROMANCE_FAMILY_COHORT_TREE_v1.json",
        CONTROL / "ROMANCE_FAMILY_COHORT_TREE_v2.json",
        CONTROL / "ROMANCE_MANAGER_EVIDENCE_GRAPH_v1.json",
        MANAGER_VALIDATOR, MANAGER_VALIDATION, MANAGER_MANIFEST,
        CONTROL / "NOETHER_FR_ES_RECOVERY_AUDIT_20260717.md",
        LANE_REPORTS / "manager_control_reconciliation_v2.md",
    ]:
        add_target(targets, path)

    corpus_paths = [
        CORPUS_V5, ROOT / "corpus" / "ROMANCE_CONSOLIDATED_CORPUS_v5.json",
        ROOT / "corpus" / "ROMANCE_CORPUS_LANGUAGE_DOMAIN_COVERAGE_v5.csv",
        ROOT / "corpus" / "ROMANCE_CORPUS_LANGUAGE_VARIETY_DOMAIN_COVERAGE_v1.csv",
        ROOT / "corpus" / "CURATED_EXTERNAL_SOURCE_MANIFEST_v3.csv",
        ROOT / "corpus" / "ROMANCE_CORPUS_REJECTED_OR_EXCLUDED_v4.csv",
        BRANCH_V4, ROOT / "corpus" / "ROMANCE_BRANCH_ROUTING_LEDGER_v4.json",
        ROOT / "corpus" / "CORPUS_PROVENANCE_AND_BRANCH_ROUTING_v8.md",
        ROOT / "scripts" / "build_consolidated_corpus_v5.py",
        ROOT / "scripts" / "build_branch_routing_ledger_v4.py",
        ROOT / "scripts" / "build_corpus_provenance_v8.py",
        CORPUS_VALIDATOR, CORPUS_AUDIT, QA / "CORPUS_BRANCH_PACKAGE_AUDIT_v3.log",
        QA / "CORPUS_BRANCH_PACKAGE_AUDIT_v3_replay1.log", QA / "CORPUS_BRANCH_PACKAGE_AUDIT_v3_replay2.log",
        QA / "CORPUS_BUILD_v5.log", QA / "BRANCH_ROUTING_BUILD_v4.log", QA / "CORPUS_PROVENANCE_BUILD_v8.log",
        QA / "RM_IDIOM_2025_ACQUISITION_VISUAL_QA_v1.md",
        ROOT / "_agent_reports" / "corpus_v4_branch_v3_replay_audit_20260718.md",
        ROOT / "_agent_reports" / "romansh_acquisition_intake_root_ready_audit_20260718.md",
    ]
    for path in corpus_paths:
        add_target(targets, path)
    for row in read_json(INTAKE_VALIDATION)["hash_targets"]:
        add_target(targets, INTAKE / row["path"])
    add_target(targets, INTAKE_VALIDATION)
    add_target(targets, INTAKE / "qa" / "acquisition_intake_validation.log")

    for path in [
        WORDWEB_V11, ACCESS_V11_JSON, ACCESS_V11_CSV, MII_V11,
        SOURCE_AUDIT_V11_CSV, SOURCE_AUDIT_V11_JSON, SOURCE_AUDIT_V11_MD,
        WORDWEB_BUILDER_V11, WORDWEB_VALIDATOR_V11, WORDWEB_AUDIT_V11,
        WORDWEB_AUDIT_LOG_V11,
        ROOT / "_agent_reports" / "wordweb_evidence_batch_v11_20260718.md",
    ]:
        add_target(targets, path)

    profile_paths = [
        ROOT / "language" / "CONTROLLED_ROMANCE_GRAMMAR_DECISIONS_T001_T008_v3.csv",
        ROOT / "language" / "CONTROLLED_ROMANCE_FUNCTION_WORDS_T001_T008_v3.csv",
        ROOT / "language" / "CONTROLLED_ROMANCE_TERM_INVENTORY_T001_T008_v3.csv",
        ROOT / "language" / "CONTROLLED_ROMANCE_LANGUAGE_PROFILE_T001_T008_v3.md",
        PROFILE_SUMMARY,
        ROOT / "scripts" / "build_controlled_romance_spec_v3.py", PROFILE_VALIDATOR,
        QA / "CONTROLLED_ROMANCE_LANGUAGE_PROFILE_BUILD_v3.log", PROFILE_AUDIT,
        QA / "CONTROLLED_ROMANCE_LANGUAGE_PROFILE_AUDIT_v3.log",
        QA / "CONTROLLED_ROMANCE_LANGUAGE_PROFILE_AUDIT_v2_replay1.log",
        QA / "CONTROLLED_ROMANCE_LANGUAGE_PROFILE_AUDIT_v2_replay2.log",
        QA / "CONTROLLED_ROMANCE_LANGUAGE_PROFILE_v2_REPLAY_LOG_STATUS.md",
        ROOT / "_agent_reports" / "controlled_romance_language_profile_v2_root_audit_20260718.md",
        ROOT / "_agent_reports" / "controlled_romance_language_profile_v3_root_audit_20260718.md",
    ]
    for path in profile_paths:
        if path.exists():
            add_target(targets, path)

    for tranche in ("R823_HG_T007", "R823_HG_T008"):
        base = ROOT / tranche
        for subdir in ["source", "semantic", "terminology", "grammar", "tex", "scripts", "qa"]:
            for path in (base / subdir).rglob("*"):
                if path.is_file():
                    add_target(targets, path)
        add_target(targets, base / "CONTINUATION_CURSOR.md")
        for build_dir in ["build", "build_repeat"]:
            for suffix in ["_romance.pdf", "_romance.log", "_lualatex_console.log", "_lualatex_pass1.log"]:
                add_target(targets, base / build_dir / f"{tranche}{suffix}")
        add_target(targets, OUTPUT_PDF / f"{tranche}_controlled_romance.pdf")
    for path in [
        ROOT / "_agent_reports" / "t007_source_semantic_visual_root_audit_20260718.md",
        ROOT / "_agent_reports" / "t008_post_repair_root_audit_20260718.md",
        RENDER_VALIDATOR, RENDER_REPORT, RENDER_VISUAL,
        QA / "PDF_RENDER_REPRODUCIBILITY_v12_replay1.log",
        QA / "PDF_RENDER_REPRODUCIBILITY_v12_replay2.log",
    ]:
        add_target(targets, path)

    rows = []
    for label in sorted(targets, key=lambda value: value.casefold()):
        path = targets[label]
        require(path.exists(), f"v11 manifest target missing: {label}")
        rows.append({"relative_path": label, "bytes": path.stat().st_size, "sha256": sha(path)})
    require(len(rows) == len({row["relative_path"] for row in rows}), "v11 manifest duplicate label")
    write_manifest(rows)
    return rows


def validate_docs() -> None:
    texts = {
        "README": README.read_text(encoding="utf-8"),
        "cursor": CURSOR.read_text(encoding="utf-8"),
        "matrix": MATRIX.read_text(encoding="utf-8"),
        "audit": REPORT.read_text(encoding="utf-8"),
    }
    required = [
        "v11", "ACTIVE_NOT_COMPLETE", "61", "11", "50", "153", "147", "71", "70",
        "60", "106", "811", "78", "28", "406", "27", "133", "954", "zero human",
        "T001–T008", "19", "21309", "Surmiran", "Sutsilvan", "specialist", "not 406 graph edges",
    ]
    for label, text in texts.items():
        for phrase in required:
            require(phrase.casefold() in text.casefold(), f"{label} missing v11 fact: {phrase}")
        require("full-R823".casefold() in text.casefold() and "not complete" in text.casefold(), f"{label} completion boundary missing")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--core-only", action="store_true", help="replay all semantic dependencies before advancing mutable docs")
    args = parser.parse_args()

    dependency_replays = run_dependencies()
    predecessor = validate_predecessor_v10()
    manager = validate_manager()
    corpus = validate_corpus()
    semantic = validate_wordweb_access()
    t007 = validate_t007()
    t008 = validate_t008()
    render = validate_render()
    profile = validate_profile()
    if args.core_only:
        print("PASS ROMANCE_V11_CORE_GATE")
        print("stage_A=NOT_COMPLETE routes=61 active=11 zero=50 rm_specialist=0 rm_surmiran=0 rm_sutsilvan=0")
        print("stage_B=PASS_CURRENT_TRANCHE records=153 primary=147 aliases=6 counting=71 active=70")
        print("stage_C=PASS_STRUCTURAL wordweb=v11 60/106 evidence=811 support=78/106 relations=406 records/27 target-ID edges access=954 human=0")
        print("stage_D=T001_T008_PASS pages=19 outputs=8 next=21309 language_profile=65/63/147")
        return

    validate_docs()
    manifest_rows = build_manifest()
    checked_rows, mismatches = verify_manifest_rows(MANIFEST_V11, ROOT)
    require(not mismatches and len(checked_rows) == len(manifest_rows), "v11 manifest final verification failed")
    gate = {
        "artifact": "ROMANCE_ACCEPTANCE_GATE_v11",
        "machine_validation": "PASS",
        "romance_infrastructure_status": "PASS_MAINTAINED_EMPIRICAL_RESEARCH_INCOMPLETE",
        "goal_status": "ACTIVE_NOT_COMPLETE",
        "predecessor_v10": {"status": "PRESERVED_IMMUTABLE_VERSIONED_PREDECESSOR", **predecessor},
        "dependency_replays": dependency_replays,
        "manager_control": {"status": "PASS_CANONICAL_NINE_COHORT_TOPOLOGY_ZERO_HUMAN", **manager},
        "stage_A": {
            "status": "NOT_COMPLETE", "explicit_routes": 61, "active_routes": 11, "zero_body_routes": 50,
            "romansh_general_school_math_active_bodies": 7, "romansh_2025_new_bodies": 4,
            "romansh_2025_new_physical_pages": 60, "romansh_specialist_algebra_bodies": 0,
            "surmiran_active_bodies": 0, "sutsilvan_active_bodies": 0,
            "rights_status": "UNRESOLVED_NOT_PUBLICATION_CLEARED",
        },
        "stage_B": {"status": "CURRENT_CORPUS_TRANCHE_PASS", **corpus["corpus"], "excluded_or_noncounting": 82},
        "stage_C": {
            "status": "STRUCTURAL_AND_SOURCE_REVIEW_PASS_NOT_HUMAN_VALIDATED",
            "wordweb_version": semantic["version"], "core_concepts": 60, "senses": 106, "c2_nodes": 39,
            "evidence_records": semantic["evidence_records"], "reviewed_occurrences": semantic["reviewed_occurrences"],
            "source_audited_evidence_records_v11": semantic["source_audited_evidence_records_v11"],
            "senses_with_accepted_support": semantic["supported_senses"], "senses_without_accepted_support": semantic["unsupported_senses"],
            "relation_records": 406, "valid_target_id_edges": 27, "relation_records_without_target_id": 379,
            "concept_to_sense_membership_edges": 106, "total_id_resolved_references_including_memberships": 133,
            "relation_reporting_boundary": "406 relation records are not 406 graph edges.",
            "human_observations": 0, "core_form_promotions": 0,
            "controlled_terminology_rows_v10": semantic["link_rows"], "corrected_semantic_links_v10": semantic["link_corrections"],
            "production_crosswalk": semantic["crosswalk"], "frozen_crosswalk_source_boundary": semantic["frozen_crosswalk_source_boundary"],
            "source_audit_rows_v11": semantic["source_audit_rows"],
            "source_audit_rights_status": semantic["source_audit_rights_status"],
            "wordweb_evidence_audit_sha256": semantic["wordweb_evidence_audit_sha256"],
        },
        "access_and_MII": {
            "sense_count": 106, "cohort_count": 9, "rows": 954,
            "human_result_fields_nonnull": 0, "human_observations": 0, "pilot_eligible_rows": 0,
            "form_promotions": 0, "empirical_MII_status": "ZERO_OBSERVATIONS_NOT_IMPLEMENTED",
            "diagnostic_boundary": "Orthographic proxy values are design diagnostics and do not measure intelligibility.",
        },
        "stage_D": {
            "status": "T001_T008_PRODUCTION_TRANCHES_PASS_NOT_LANGUAGE_VALIDATED",
            "source_lines": SOURCE_RANGES, "next_authority_line": 21309,
            "output_copy_exact_matches": 8, "render_reproducibility": "T001_T008_PASS_19_OF_19_PAGES",
            "T007": t007, "T008": t008,
            "language_profile_v3": profile, "human_validation": 0,
        },
        "render_v12": render,
        "corpus_v5_branch_v4": corpus,
        "documentation_status": "CURRENT_V11",
        "pilot_claim": False,
        "full_R823_romance_translation_claim": False,
        "lane_completion_claim": False,
        "hash_target_count": len(manifest_rows),
        "hash_manifest_sha256": sha(MANIFEST_V11),
        "key_hashes": {row["relative_path"]: row["sha256"] for row in manifest_rows},
    }
    GATE_V11.write_text(json.dumps(gate, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    lines = [
        "PASS machine_validation romance_infrastructure=PASS_MAINTAINED goal_status=ACTIVE_NOT_COMPLETE",
        "stage_A=NOT_COMPLETE routes=61 active=11 zero=50 rm_general_active=7 rm_new_2025=4/60pages rm_specialist=0 rm_surmiran=0 rm_sutsilvan=0 rights=UNRESOLVED",
        "stage_B=PASS records=153 primary=147 aliases=6 counting=71 active=70",
        "stage_C=PASS_STRUCTURAL concepts=60 senses=106 c2=39 evidence=811 reviewed_occurrences=682 source_audited_new=9 supported=78/106 relation_records=406 target_ID_edges=27 total_ID_refs=133 human=0 promotions=0",
        "relation_boundary=406_relation_records_are_not_406_graph_edges",
        "access=PASS rows=954 cohorts=9 human=0 pilot_eligible=0 empirical_MII=ZERO_OBSERVATIONS",
        "stage_D=T001_T008_PASS outputs=8 render_pages=19/19 next=21309 human_validation=0",
        "language_profile_v3=PASS grammar=65 functions=63 terms=147 linked=122 unlinked=25 identifier_refs=148",
        f"render_v12_sha256={render['report_sha256']}",
        f"profile_v3_audit_sha256={profile['audit_sha256']}",
        f"corpus_v3_audit_sha256={corpus['audit_sha256']}",
        f"hash_targets={len(manifest_rows)} sha256_manifest={sha(MANIFEST_V11)}",
        f"gate_v11_sha256={sha(GATE_V11)}",
    ]
    GATE_LOG_V11.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()

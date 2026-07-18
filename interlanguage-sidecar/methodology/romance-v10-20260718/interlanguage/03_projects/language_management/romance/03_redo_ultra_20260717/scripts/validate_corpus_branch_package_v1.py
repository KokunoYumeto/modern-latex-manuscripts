#!/usr/bin/env python3
"""Independent acceptance audit for consolidated corpus v3 + branch routing v2.

This validator reads the frozen products directly.  It does not import either
builder and does not construct the top-level Romance gate.
"""

from __future__ import annotations

import csv
import hashlib
import json
import logging
import sys
from collections import defaultdict
from pathlib import Path

from pypdf import PdfReader

logging.getLogger("pypdf").setLevel(logging.ERROR)


ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "corpus"
QA = ROOT / "qa"
REPORTS = ROOT / "_agent_reports"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def integer(value: str) -> int:
    return int(value or 0)


def truth(value: str) -> bool:
    return value.strip().lower() == "true"


checks: list[dict[str, object]] = []


def check(check_id: str, condition: bool, evidence: object) -> None:
    checks.append({"check_id": check_id, "pass": bool(condition), "evidence": evidence})


corpus_csv = CORPUS / "ROMANCE_CONSOLIDATED_CORPUS_v3.csv"
corpus_json_path = CORPUS / "ROMANCE_CONSOLIDATED_CORPUS_v3.json"
coverage_csv = CORPUS / "ROMANCE_CORPUS_LANGUAGE_DOMAIN_COVERAGE_v3.csv"
excluded_csv = CORPUS / "ROMANCE_CORPUS_REJECTED_OR_EXCLUDED_v3.csv"
curated_csv = CORPUS / "CURATED_EXTERNAL_SOURCE_MANIFEST_v2.csv"
route_csv = CORPUS / "ROMANCE_BRANCH_ROUTING_LEDGER_v2.csv"
route_json_path = CORPUS / "ROMANCE_BRANCH_ROUTING_LEDGER_v2.json"
query_log_csv = CORPUS / "WIKIMEDIA_HTML_QUERY_LOG_v1.csv"
wiki_manifest_csv = CORPUS / "WIKIMEDIA_HTML_CORPUS_MANIFEST_v1.csv"
wiki_coverage_csv = CORPUS / "WIKIMEDIA_HTML_COVERAGE_v1.csv"
provenance_v6 = CORPUS / "CORPUS_PROVENANCE_AND_BRANCH_ROUTING_v6.md"

rows = read_csv(corpus_csv)
summary = json.loads(corpus_json_path.read_text(encoding="utf-8"))
coverage = read_csv(coverage_csv)
excluded = read_csv(excluded_csv)
curated = read_csv(curated_csv)
routes = read_csv(route_csv)
route_summary = json.loads(route_json_path.read_text(encoding="utf-8"))
queries = read_csv(query_log_csv)
wiki_manifest = read_csv(wiki_manifest_csv)
wiki_coverage = read_csv(wiki_coverage_csv)

expected_hashes = {
    "corpus/ROMANCE_CONSOLIDATED_CORPUS_v3.csv": "F754A4402F91DA045A222C041C52F1E7FCF993F8B983C7C6C628E6A7FC379639",
    "corpus/ROMANCE_CONSOLIDATED_CORPUS_v3.json": "B0B6C772C00449A94713AD128B091F6801AFB13E39707A09284F17A9AD308037",
    "corpus/ROMANCE_CORPUS_LANGUAGE_DOMAIN_COVERAGE_v3.csv": "27E59D6B12562C9DADC5DCDF8210081EF027D8F200272A03192A952A5D19C33D",
    "corpus/ROMANCE_CORPUS_REJECTED_OR_EXCLUDED_v3.csv": "AE99FF27CAC6755E10D88F3D814BFFB5AD3F7C46D184DDE110CD8F05432BC7ED",
    "corpus/CURATED_EXTERNAL_SOURCE_MANIFEST_v2.csv": "3870079115BC397FC765D05A41B49920FF786B795096B64912F6371F12B7C62F",
    "corpus/ROMANCE_BRANCH_ROUTING_LEDGER_v2.csv": "889A4C949D4D535F5683758A6B19614529DAA9EAFAE8D7B19FFE747C6469EDC3",
    "corpus/ROMANCE_BRANCH_ROUTING_LEDGER_v2.json": "6E541CE057B0213582C8BCB37F259D9CAB6219C4BD0142B0E33955C17BAFFF38",
    "qa/CORPUS_BUILD_v3.log": "2FD4E2ABDC054B196ED96A5756FBB7BAD58DEB875DE332A73A92D9F9C8308604",
    "qa/BRANCH_ROUTING_BUILD_v2.log": "6BF803BA6A5E10DF3E5210642D9AB72069F452F92CAD6DB04C3E5D3476BD3168",
    "qa/RM_RG_SOURCE_VISUAL_QA_v1.md": "57F21E701E42E1F34E5515A66F3576E4E32F34B765FEBC9FD0ED14A2D2B04913",
    "qa/RM_RG_SOURCE_VISUAL_QA_v2.md": "B9E8F232191AB0A73D36CA76B048F4C017B1FAF67C26B9FFFB3957E6C877B35B",
    "qa/CORPUS_BRANCH_TABULAR_QA_v1.png": "155A9F5ABE611FB589BDDA4FA5448463AF517E0FC841955E70F3DD95A1DB3A0A",
    "qa/CORPUS_BRANCH_TABULAR_QA_v1.json": "707DF55D1E82A8D84419AADBD3696D2B9B26A8A99EED60F4BBFE8A8CC811CD7C",
}
actual_hashes = {rel: sha256(ROOT / rel) for rel in expected_hashes}
check("frozen_artifact_hashes", actual_hashes == expected_hashes, actual_hashes)

record_ids = [row["record_id"] for row in rows]
primary = [row for row in rows if row["dedupe_status"] == "primary_unique"]
counted = [row for row in rows if truth(row["counting_eligible"])]
aliases = [row for row in rows if row["dedupe_status"].startswith("representation_alias_of:")]
byte_aliases = [row for row in rows if row["dedupe_status"].startswith("byte_alias")]

check("corpus_record_count", len(rows) == 148, len(rows))
check("corpus_record_ids_unique", len(set(record_ids)) == 148, len(set(record_ids)))
check("primary_unique_count", len(primary) == 142, len(primary))
check("representation_alias_count", len(aliases) == 6, len(aliases))
check("byte_alias_count", len(byte_aliases) == 0, len(byte_aliases))
check("counting_eligible_count", len(counted) == 66, len(counted))
check("excluded_count", len(excluded) == 5, len(excluded))
check("coverage_row_count", len(coverage) == 9, len(coverage))
check("term_promotion_zero", not any(truth(row["term_promotion_eligible"]) for row in rows), 0)
check(
    "summary_counts_match",
    summary["record_count"] == len(rows)
    and summary["primary_unique_count"] == len(primary)
    and summary["representation_alias_count"] == len(aliases)
    and summary["byte_alias_count"] == len(byte_aliases)
    and summary["excluded_count"] == len(excluded),
    {
        "record_count": summary["record_count"],
        "primary_unique_count": summary["primary_unique_count"],
        "representation_alias_count": summary["representation_alias_count"],
        "byte_alias_count": summary["byte_alias_count"],
        "excluded_count": summary["excluded_count"],
    },
)

path_errors: list[dict[str, str]] = []
for row in rows:
    original = Path(row["absolute_path"])
    if not original.is_file():
        path_errors.append({"record_id": row["record_id"], "error": "missing_original"})
        continue
    if original.stat().st_size != integer(row["bytes"]):
        path_errors.append({"record_id": row["record_id"], "error": "original_byte_mismatch"})
    if sha256(original) != row["sha256"]:
        path_errors.append({"record_id": row["record_id"], "error": "original_hash_mismatch"})
    search_value = row["search_text_path"].strip()
    if truth(row["counting_eligible"]) and not search_value:
        path_errors.append({"record_id": row["record_id"], "error": "counting_search_path_blank"})
    if search_value:
        search_path = Path(search_value)
        if not search_path.is_file():
            path_errors.append({"record_id": row["record_id"], "error": "missing_search_text"})
        elif sha256(search_path) != row["search_text_sha256"]:
            path_errors.append({"record_id": row["record_id"], "error": "search_hash_mismatch"})
check("all_source_and_search_paths_hash_verified", not path_errors, path_errors)

by_language: dict[str, list[dict[str, str]]] = defaultdict(list)
for row in rows:
    by_language[row["language"]].append(row)


def recompute_language(language: str) -> dict[str, object]:
    language_rows = by_language[language]
    primary_rows = [row for row in language_rows if row["dedupe_status"] == "primary_unique"]
    counting_rows = [row for row in language_rows if truth(row["counting_eligible"])]
    if language == "rm" and not counting_rows:
        body_status = "explicit_zero_body_gap"
    elif counting_rows:
        body_status = "substantive_body_present"
    else:
        body_status = "auxiliary_or_generated_only"
    return {
        "language": language,
        "records": len(language_rows),
        "primary_unique_records": len(primary_rows),
        "unique_logical_sources": len({row["logical_source_id"] for row in language_rows}),
        "bytes": sum(integer(row["bytes"]) for row in counting_rows),
        "all_primary_bytes": sum(integer(row["bytes"]) for row in primary_rows),
        "declared_open_license_primary": sum(
            row["license_status"].startswith("declared_cc") for row in primary_rows
        ),
        "license_unresolved_primary": sum(
            "unresolved" in row["license_status"] or "not_reuse_clear" in row["license_status"]
            for row in primary_rows
        ),
        "domains": ";".join(
            sorted(
                {
                    tag
                    for row in counting_rows
                    for tag in row["domain_tags"].split(";")
                    if tag
                }
            )
        ),
        "counting_eligible": len(counting_rows),
        "term_promotion_eligible": 0,
        "body_status": body_status,
    }


recomputed_coverage = [recompute_language(language) for language in sorted(by_language)]
normalized_coverage = [
    {
        key: integer(value)
        if key
        in {
            "records",
            "primary_unique_records",
            "unique_logical_sources",
            "bytes",
            "all_primary_bytes",
            "declared_open_license_primary",
            "license_unresolved_primary",
            "counting_eligible",
            "term_promotion_eligible",
        }
        else value
        for key, value in row.items()
    }
    for row in coverage
]
check("coverage_csv_recomputed_exactly", recomputed_coverage == normalized_coverage, recomputed_coverage)
check("coverage_json_matches_csv", summary["languages"] == recomputed_coverage, summary["languages"])

rm_source_ids = [
    "CURATED-RM-RG-GRCH-AP1G-2021-M1",
    "CURATED-RM-RG-GRCH-AP1G-2024-M1",
    "CURATED-RM-RG-GRCH-AP1G-2024-M2",
]
rm_rows = [row for row in rows if row["language"] == "rm"]
rm_expected_common = all(
    row["variety_code"] == "rm-rg"
    and row["domain"] == "mathematics_education"
    and row["register"] == "secondary_school_admissions_exam"
    and row["dedupe_status"] == "primary_unique"
    and truth(row["counting_eligible"])
    and not truth(row["term_promotion_eligible"])
    and row["license_status"] == "unresolved_no_explicit_reuse_grant"
    and row["upstream_locator"].startswith("https://www.gr.ch/")
    for row in rm_rows
)
specialist_tags = {"abstract_algebra", "field_theory", "group_theory", "module_theory", "ring_theory", "specialist_algebra"}
rm_observed_tags = {tag for row in rm_rows for tag in row["domain_tags"].split(";") if tag}
check("romansh_exact_three_source_ids", [row["record_id"] for row in rm_rows] == rm_source_ids, [row["record_id"] for row in rm_rows])
check("romansh_common_provenance_fields", rm_expected_common, {"records": len(rm_rows), "bytes": sum(integer(row["bytes"]) for row in rm_rows)})
check("romansh_general_school_math_not_specialist", not (rm_observed_tags & specialist_tags), sorted(rm_observed_tags))

curated_by_id = {row["source_id"]: row for row in curated}
curated_errors: list[dict[str, object]] = []
for source_id in rm_source_ids:
    manifest_row = curated_by_id.get(source_id)
    corpus_row = next((row for row in rm_rows if row["record_id"] == source_id), None)
    if manifest_row is None or corpus_row is None:
        curated_errors.append({"source_id": source_id, "error": "missing_manifest_or_corpus_row"})
        continue
    pdf_path = ROOT / manifest_row["local_relative_path"]
    text_path = ROOT / manifest_row["search_text_relative_path"]
    observed = {
        "pdf_bytes": pdf_path.stat().st_size,
        "pdf_sha256": sha256(pdf_path),
        "pages": len(PdfReader(str(pdf_path)).pages),
        "text_bytes": text_path.stat().st_size,
        "text_sha256": sha256(text_path),
    }
    expected = {
        "pdf_bytes": integer(manifest_row["bytes"]),
        "pdf_sha256": manifest_row["sha256"],
        "pages": integer(manifest_row["page_count"]),
        "text_bytes": integer(manifest_row["search_text_bytes"]),
        "text_sha256": manifest_row["search_text_sha256"],
    }
    if observed != expected:
        curated_errors.append({"source_id": source_id, "observed": observed, "expected": expected})
    if corpus_row["sha256"] != manifest_row["sha256"] or corpus_row["search_text_sha256"] != manifest_row["search_text_sha256"]:
        curated_errors.append({"source_id": source_id, "error": "manifest_corpus_identity_mismatch"})
check("curated_manifest_three_sources_hash_bytes_pages_text", len(curated) == 3 and not curated_errors, curated_errors)

expected_visual_hashes = {
    "qa/rm_source_render/AP21_1G_M1_RG_page_01.png": "ED4390C3F576397F51B50DBC8859206C57379F9FC24D795DEDFA087BED63733D",
    "qa/rm_source_render/AP21_1G_M1_RG_page_04.png": "F31DCD760846C2F74B9F9E32C44488B9843AAC8A483BBCC01AECED705A983794",
    "qa/rm_source_render/AP21_1G_M1_RG_page_08.png": "FA766F005F31BF9748E61633DCE6F4434C2AB218F10BE6FFEC7A07F72B2F7692",
    "qa/rm_source_render/AP21_1G_M1_RG_page_13.png": "22C05A4CA002E5AB2EC808B0406C2C59A392F3CD1C652CF16491A87DA5510C10",
    "qa/rm_source_render_2024/M1_p01-01.png": "B74E514111065AC92D2B579AFF56747545B42AEE4B3B6CA16941C19142F840EC",
    "qa/rm_source_render_2024/M1_p05.png": "CA788D6AED0977007A01EE0FF7C54AFA47BC970A8CD662AA50445013DAA47212",
    "qa/rm_source_render_2024/M1_p10.png": "FB9EE56154FAF07AD7D680F976BFB3523214235709E45DECA242BE17A86299BB",
    "qa/rm_source_render_2024/M1_p15.png": "98FFEB05197B6064C47791CD918565473F1DAABF6E06B1A1CE4CA716C18DE024",
    "qa/rm_source_render_2024/M2_p01-1.png": "056BEBDB53943FC36DE4F1A1A699617D183EF80EC775D45B812EFBA386CCDD65",
    "qa/rm_source_render_2024/M2_p03.png": "784ED46EFFE1FBB623320E4EAE80B80832E50C627DF239E3F6DFBAB5A49D1CD4",
    "qa/rm_source_render_2024/M2_p06.png": "D0BF62DF991A00849E48A6B824B36A829982D3F5664D26B2AC6C34F44B034BFB",
}
actual_visual_hashes = {rel: sha256(ROOT / rel) for rel in expected_visual_hashes}
qa_text = (QA / "RM_RG_SOURCE_VISUAL_QA_v1.md").read_text(encoding="utf-8") + (QA / "RM_RG_SOURCE_VISUAL_QA_v2.md").read_text(encoding="utf-8")
check("visual_sample_hashes_pinned", actual_visual_hashes == expected_visual_hashes, actual_visual_hashes)
check("visual_sample_hashes_recorded_in_qa", all(value in qa_text for value in expected_visual_hashes.values()), len(expected_visual_hashes))

tabular_qa = json.loads((QA / "CORPUS_BRANCH_TABULAR_QA_v1.json").read_text(encoding="utf-8"))
tabular_checks = tabular_qa["checks"]
check(
    "artifact_tool_tabular_import_and_render",
    tabular_qa["imported_rows"] == {"corpus": 148, "coverage": 9, "excluded": 5, "routes": 61}
    and tabular_checks["corpus_record_ids_unique"] is True
    and tabular_checks["rm_coverage_records"] == 3
    and tabular_checks["rm_coverage_counting_eligible"] == 3
    and tabular_checks["rm_route_active_bodies"] == 3
    and tabular_checks["rm_route_general_school_math_bodies"] == 3
    and tabular_checks["rm_route_specialist_algebra_bodies"] == 0
    and tabular_checks["rm_route_inherited_form_attestations"] == 0
    and tabular_checks["rm_regional_idiom_active_bodies"] == 0,
    {"imported_rows": tabular_qa["imported_rows"], "checks": tabular_checks, "preview": tabular_qa["preview"]},
)

active_routes = [row for row in routes if integer(row["current_active_body_count"]) > 0]
zero_routes = [row for row in routes if integer(row["current_active_body_count"]) == 0]
rm_route = next(row for row in routes if row["variety_code"] == "rm-rg")
idiom_codes = ["rm-sursilvan", "rm-sutsilvan", "rm-surmiran", "rm-puter", "rm-vallader"]
idiom_routes = [row for row in routes if row["variety_code"] in idiom_codes]
check("route_counts", len(routes) == 61 and len(active_routes) == 8 and len(zero_routes) == 53, {"routes": len(routes), "active": len(active_routes), "zero": len(zero_routes)})
check(
    "rm_route_exact_metrics",
    integer(rm_route["current_active_body_count"]) == 3
    and integer(rm_route["current_general_school_math_body_count"]) == 3
    and integer(rm_route["current_specialist_algebra_body_count"]) == 0
    and integer(rm_route["inherited_form_attestation_count"]) == 0
    and not truth(rm_route["inherited_forms_are_corpus_attestation"])
    and rm_route["current_source_ids"].split(";") == rm_source_ids
    and integer(rm_route["current_active_bytes"]) == 2_482_929,
    {key: rm_route[key] for key in ["current_active_body_count", "current_active_bytes", "current_source_ids", "current_general_school_math_body_count", "current_specialist_algebra_body_count", "inherited_form_attestation_count", "inherited_forms_are_corpus_attestation"]},
)
check(
    "five_romansh_idiom_routes_zero_and_unproxied",
    len(idiom_routes) == 5
    and {row["variety_code"] for row in idiom_routes} == set(idiom_codes)
    and all(
        integer(row["current_active_body_count"]) == 0
        and integer(row["current_active_bytes"]) == 0
        and integer(row["inherited_form_attestation_count"]) == 0
        and truth(row["dominant_standard_not_proxy"])
        for row in idiom_routes
    ),
    [{"variety_code": row["variety_code"], "active": integer(row["current_active_body_count"]), "proxy_blocked": truth(row["dominant_standard_not_proxy"])} for row in idiom_routes],
)
check(
    "route_json_links_frozen_inputs",
    route_summary["route_count"] == 61
    and route_summary["active_routes"] == 8
    and route_summary["explicit_zero_routes"] == 53
    and route_summary["romansh_active_body_count"] == 3
    and route_summary["romansh_general_school_math_body_count"] == 3
    and route_summary["romansh_specialist_algebra_body_count"] == 0
    and route_summary["romansh_inherited_form_attestation_count"] == 0
    and route_summary["romansh_regional_idiom_active_body_count"] == 0
    and route_summary["corpus_manifest_sha256"] == actual_hashes["corpus/ROMANCE_CONSOLIDATED_CORPUS_v3.csv"]
    and route_summary["coverage_sha256"] == actual_hashes["corpus/ROMANCE_CORPUS_LANGUAGE_DOMAIN_COVERAGE_v3.csv"]
    and route_summary["curated_source_manifest_sha256"] == actual_hashes["corpus/CURATED_EXTERNAL_SOURCE_MANIFEST_v2.csv"]
    and route_summary["ledger_sha256"] == actual_hashes["corpus/ROMANCE_BRANCH_ROUTING_LEDGER_v2.csv"],
    route_summary,
)

query_failures = [row for row in queries if row["status"] == "no_article_result_zero_page_or_revision"]
query_rejections = [row for row in queries if row["status"].startswith("rejected_nonmathematical_result:")]
check(
    "romansh_search_failures_quarantined",
    len(query_failures) == 2
    and {row["query"] for row in query_failures} == {"algebra matematica", "rintg algebra"}
    and not any(row["language_code"] == "rm" for row in wiki_manifest),
    {"zero_result_queries": [row["query"] for row in query_failures], "active_rm_wikimedia_rows": sum(row["language_code"] == "rm" for row in wiki_manifest)},
)
check(
    "automatic_search_false_hits_rejected",
    len(query_rejections) == 4
    and sum(row["reason"].startswith("nonmathematical_automatic_search_result:rm:") for row in excluded) == 4,
    [row["status"] for row in query_rejections],
)
check(
    "wikimedia_manifest_identifiable_no_placeholders",
    len(wiki_manifest) == 42
    and all(row["title"].strip() for row in wiki_manifest)
    and all(integer(row["page_id"]) > 0 for row in wiki_manifest)
    and all(integer(row["revision_id"]) > 0 for row in wiki_manifest),
    {"rows": len(wiki_manifest), "blank_titles": sum(not row["title"].strip() for row in wiki_manifest), "zero_page": sum(integer(row["page_id"]) == 0 for row in wiki_manifest), "zero_revision": sum(integer(row["revision_id"]) == 0 for row in wiki_manifest)},
)
rm_wiki_coverage = next(row for row in wiki_coverage if row["language_code"] == "rm")
check(
    "wikimedia_rm_coverage_zero_after_topic_review",
    integer(rm_wiki_coverage["downloaded"]) == 0
    and integer(rm_wiki_coverage["unique_pages"]) == 0
    and integer(rm_wiki_coverage["bytes"]) == 0,
    rm_wiki_coverage,
)

provenance_text = provenance_v6.read_text(encoding="utf-8")
required_boundary_phrases = [
    "does not assert that every active standard has a specialist-algebra body",
    "general school mathematics only; specialist algebra zero",
    "The five regional Romansh idioms remain separate zero-body routes",
    "No inherited form, search string, orthographic score, or corpus occurrence is promoted",
    "This document is **not** the top-level acceptance gate",
]
check("provenance_v6_claim_boundaries", all(phrase in provenance_text for phrase in required_boundary_phrases), required_boundary_phrases)

all_passed = all(item["pass"] for item in checks)
artifact_meta = {
    rel: {"bytes": (ROOT / rel).stat().st_size, "sha256": actual_hashes[rel]}
    for rel in expected_hashes
}
artifact_meta["corpus/CORPUS_PROVENANCE_AND_BRANCH_ROUTING_v6.md"] = {
    "bytes": provenance_v6.stat().st_size,
    "sha256": sha256(provenance_v6),
}

result = {
    "artifact": "CORPUS_BRANCH_PACKAGE_AUDIT_v1",
    "scope": "ROMANCE_CONSOLIDATED_CORPUS_v3 + ROMANCE_BRANCH_ROUTING_LEDGER_v2 + three official Rumantsch Grischun school-mathematics sources",
    "independence": "direct CSV/JSON/path/PDF/hash recomputation; neither builder imported; top-level gate not built",
    "status": "PASS" if all_passed else "FAIL",
    "counts": {
        "records": len(rows),
        "primary_unique": len(primary),
        "representation_aliases": len(aliases),
        "counting_eligible": len(counted),
        "excluded": len(excluded),
        "coverage_rows": len(coverage),
        "routes": len(routes),
        "active_routes": len(active_routes),
        "zero_routes": len(zero_routes),
        "rm_counting_eligible": len(rm_rows),
        "rm_general_school_math": integer(rm_route["current_general_school_math_body_count"]),
        "rm_specialist_algebra": integer(rm_route["current_specialist_algebra_body_count"]),
        "rm_inherited_form_attestation": integer(rm_route["inherited_form_attestation_count"]),
        "rm_regional_idiom_active_bodies": sum(integer(row["current_active_body_count"]) for row in idiom_routes),
    },
    "coverage_recomputed": recomputed_coverage,
    "artifacts": artifact_meta,
    "source_urls": {row["source_id"]: row["source_url"] for row in curated},
    "visual_sample_hashes": actual_visual_hashes,
    "checks": checks,
    "claim_boundary": "The three active rm-rg bodies are official general school-mathematics examination parts, not specialist algebra. The five regional idioms remain zero-body. No human intelligibility or term-promotion claim is made.",
    "continuation_cursor": "Acquire a source-licensed specialist Rumantsch Grischun algebra body, then idiom-specific mathematics bodies for Sursilvan, Sutsilvan, Surmiran, Puter, and Vallader; keep each route zero until a native body is hash-verified and reviewed.",
}

QA.mkdir(parents=True, exist_ok=True)
REPORTS.mkdir(parents=True, exist_ok=True)
json_path = QA / "CORPUS_BRANCH_PACKAGE_AUDIT_v1.json"
log_path = QA / "CORPUS_BRANCH_PACKAGE_AUDIT_v1.log"
report_path = REPORTS / "corpus_v3_branch_v2_audit.md"
json_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

failed = [item for item in checks if not item["pass"]]
log_lines = [
    f"{'PASS' if all_passed else 'FAIL'} checks={len(checks)} failed={len(failed)}",
    f"records={len(rows)} primary_unique={len(primary)} counting_eligible={len(counted)} excluded={len(excluded)} coverage_rows={len(coverage)}",
    f"routes={len(routes)} active={len(active_routes)} zero={len(zero_routes)}",
    f"rm_active={len(rm_rows)} rm_general_school_math=3 rm_specialist_algebra=0 rm_inherited_form_attestation=0 rm_regional_idiom_active_bodies=0",
    f"corpus_sha256={sha256(corpus_csv)}",
    f"route_ledger_sha256={sha256(route_csv)}",
    f"provenance_v6_sha256={sha256(provenance_v6)}",
]
log_lines.extend(f"FAIL {item['check_id']}" for item in failed)
log_path.write_text("\n".join(log_lines) + "\n", encoding="utf-8")

coverage_lines = [
    f"| {row['language']} | {row['records']} | {row['primary_unique_records']} | {row['counting_eligible']} | {row['bytes']} | {row['body_status']} |"
    for row in recomputed_coverage
]
source_lines = [
    f"| `{row['source_id']}` | {row['publication_date']} | {row['page_count']} | {row['bytes']} | `{row['sha256']}` | `{row['search_text_sha256']}` |"
    for row in curated
]
report = f"""# Independent corpus v3 / branch v2 audit

Status: **{'PASS' if all_passed else 'FAIL'}** — {len(checks)} direct checks, {len(failed)} failures. This audit reads the frozen outputs, source files, PDFs, search derivatives, QA images, and routing rows directly. It imports neither builder and does not build or claim the top-level v8 gate.

## Acceptance result

- Corpus: **148** records, **142** primary unique, **6** representation aliases, **66** counting eligible, **5** excluded candidates, and **9** coverage rows.
- Branch routing: **61** routes, **8** active and **53** explicit zero-body/gap routes.
- Rumantsch Grischun: exactly **3** active/counting bodies, all official general-school admissions mathematics; **3** general-school-math, **0** specialist algebra, **0** inherited-form attestations.
- Regional Romansh idioms: Sursilvan, Sutsilvan, Surmiran, Putèr, and Vallader remain five separate zero-body routes; Rumantsch Grischun is not counted as their proxy.
- Evidence boundary: every corpus row is term-promotion false. No human intelligibility claim is made. `substantive_body_present` means a reviewed mathematics body exists, not that every standard has specialist depth.

## Independently recomputed coverage

| Key | Records | Primary unique | Counting eligible | Counting bytes | Status |
|---|---:|---:|---:|---:|---|
{chr(10).join(coverage_lines)}

The RM row is 3/3/3 with 2,482,929 counting bytes, all `mathematics_education` / `secondary_school_admissions_exam`. Its reviewed tags are school arithmetic, fractions, geometry, measurement, number-line/instruction/solution-register, and word-problem tags; no abstract-, field-, group-, module-, ring-, or specialist-algebra tag occurs.

## Source identity and visual evidence

| Source | Year | Pages | PDF bytes | PDF SHA-256 | Search-text SHA-256 |
|---|---:|---:|---:|---|---|
{chr(10).join(source_lines)}

All three URLs resolve to the recorded official `gr.ch` paths in `CURATED_EXTERNAL_SOURCE_MANIFEST_v2.csv`. Page counts were independently read from the PDFs; local PDF and text bytes/hashes match the manifest and corpus rows. Public access is verified, but no explicit reuse grant was located, so all three remain `unresolved_no_explicit_reuse_grant` and term-promotion false.

The eleven pinned 120-dpi sample PNGs hash-match their QA records. During this audit, the seven 2024 samples were freshly rendered and exactly reproduced the pinned hashes, then inspected at original detail: titles/instructions and task pages were legible, with no clipping, corruption, or missing glyphs. The crossed 2024 M1 scratch page and whitespace on 2024 M2 page 6 are intentional. The imported coverage table was separately rendered through the spreadsheet workbook engine as `qa/CORPUS_BRANCH_TABULAR_QA_v1.png` (SHA-256 `{actual_hashes['qa/CORPUS_BRANCH_TABULAR_QA_v1.png']}`) and visually inspected; all nine rows and the RM 3/3 counts are readable.

## Provenance and routing successor

Current narrative successor: `corpus/CORPUS_PROVENANCE_AND_BRANCH_ROUTING_v6.md`, SHA-256 `{sha256(provenance_v6)}`. It preserves v2–v5, records exact official URLs, file/text hashes and sizes, page counts, license caveats, visual-QA hashes, v3 corpus hashes/counts, and v2 routing. It explicitly denies specialist-depth equivalence and keeps all five regional idioms at zero body.

Current frozen product hashes:

- `ROMANCE_CONSOLIDATED_CORPUS_v3.csv`: `{sha256(corpus_csv)}`
- `ROMANCE_CORPUS_LANGUAGE_DOMAIN_COVERAGE_v3.csv`: `{sha256(coverage_csv)}`
- `ROMANCE_BRANCH_ROUTING_LEDGER_v2.csv`: `{sha256(route_csv)}`
- `CURATED_EXTERNAL_SOURCE_MANIFEST_v2.csv`: `{sha256(curated_csv)}`

The two no-article Romansh searches remain only in `WIKIMEDIA_HTML_QUERY_LOG_v1.csv`; the current Wikimedia source manifest has 42 identifiable rows, no blank titles, no zero page/revision IDs, and no active RM rows after the four non-mathematics false hits were quarantined.

## Continuation cursor

This corpus/branch package is accepted for integration by the parent task; it is not the top-level gate. Next acquisition priority is a source-licensed specialist Rumantsch Grischun algebra body. After that, acquire and review native mathematics bodies separately for Sursilvan, Sutsilvan, Surmiran, Putèr, and Vallader. Keep every route at zero until its own native body is locally preserved, hash-verified, licensed/status-marked, and content-reviewed; inherited forms remain non-attestations.

Machine evidence: `qa/CORPUS_BRANCH_PACKAGE_AUDIT_v1.json`; concise log: `qa/CORPUS_BRANCH_PACKAGE_AUDIT_v1.log`.
"""
report_path.write_text(report, encoding="utf-8")

print("\n".join(log_lines))
if not all_passed:
    sys.exit(1)

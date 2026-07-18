# Successor build: preserves v1 and binds consolidated corpus v3.
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SEED = ROOT / "curation" / "ROMANCE_BRANCH_ROUTE_SEED_v1.csv"
CORPUS = ROOT / "corpus" / "ROMANCE_CONSOLIDATED_CORPUS_v3.csv"
CURATED = ROOT / "corpus" / "CURATED_EXTERNAL_SOURCE_MANIFEST_v2.csv"
COVERAGE = ROOT / "corpus" / "ROMANCE_CORPUS_LANGUAGE_DOMAIN_COVERAGE_v3.csv"
OUT = ROOT / "corpus" / "ROMANCE_BRANCH_ROUTING_LEDGER_v2.csv"
SUMMARY = ROOT / "corpus" / "ROMANCE_BRANCH_ROUTING_LEDGER_v2.json"
LOG = ROOT / "qa" / "BRANCH_ROUTING_BUILD_v2.log"

SPECIALIST_ALGEBRA_TAGS = {
    "abstract_algebra",
    "field_theory",
    "group_theory",
    "module_theory",
    "ring_theory",
}
EXPECTED_RM_SOURCE_IDS = {
    "CURATED-RM-RG-GRCH-AP1G-2021-M1",
    "CURATED-RM-RG-GRCH-AP1G-2024-M1",
    "CURATED-RM-RG-GRCH-AP1G-2024-M2",
}
RM_REGIONAL_IDIOMS = {
    "rm-sursilvan",
    "rm-sutsilvan",
    "rm-surmiran",
    "rm-puter",
    "rm-vallader",
}


def read_csv(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def sha(path: Path):
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def tags(row: dict[str, str]) -> set[str]:
    return {tag for tag in row["domain_tags"].split(";") if tag}


def is_general_school_math(row: dict[str, str]) -> bool:
    return (
        row["domain"] == "mathematics_education"
        and row["register"] == "secondary_school_admissions_exam"
    )


def is_specialist_algebra(row: dict[str, str]) -> bool:
    return row["domain"] in SPECIALIST_ALGEBRA_TAGS or bool(
        tags(row) & SPECIALIST_ALGEBRA_TAGS
    )


def is_inherited_form_attestation(row: dict[str, str]) -> bool:
    descriptor = " ".join(
        row.get(field, "")
        for field in (
            "record_id",
            "logical_source_id",
            "source_use_status",
            "sense_review_status",
        )
    ).lower()
    return "inherited_form" in descriptor or "inherited_seed" in descriptor


seed = read_csv(SEED)
corpus = read_csv(CORPUS)
rows = []
for route in seed:
    key = route["corpus_language_key"]
    active = [r for r in corpus if key and r["language"] == key and r["counting_eligible"] == "true"]
    general_school_math = [r for r in active if is_general_school_math(r)]
    specialist_algebra = [r for r in active if is_specialist_algebra(r)]
    inherited_form_attestations = [r for r in active if is_inherited_form_attestation(r)]
    licenses = sorted({r["license_status"] for r in active})
    if active:
        evidence_status = "active_substantive_body_present"
        gap_reason = ""
    elif route["scope_status"] == "historical_diachronic":
        evidence_status = "explicit_zero_historical_source_gap"
        gap_reason = route["gap_reason"]
    elif route["scope_status"] == "contact_comparator":
        evidence_status = "explicit_zero_contact_comparator_gap"
        gap_reason = route["gap_reason"]
    else:
        evidence_status = "explicit_zero_body_gap"
        gap_reason = route["gap_reason"]
    row = dict(route)
    row.update(
        current_active_body_count=str(len(active)),
        current_active_bytes=str(sum(int(r["bytes"]) for r in active)),
        current_domains=";".join(sorted({tag for r in active for tag in r["domain_tags"].split(";") if tag})),
        current_source_ids=";".join(sorted(r["record_id"] for r in active)),
        current_general_school_math_body_count=str(len(general_school_math)),
        current_specialist_algebra_body_count=str(len(specialist_algebra)),
        inherited_form_attestation_count=str(len(inherited_form_attestations)),
        inherited_forms_are_corpus_attestation="false",
        current_license_status=";".join(licenses) if licenses else "no_active_source",
        evidence_status=evidence_status,
        gap_reason=gap_reason,
        corpus_manifest_sha256=sha(CORPUS),
        review_status="route_implemented_20260717_needs_source_acquisition" if not active else "route_implemented_active_corpus",
    )
    if route["variety_code"] == "rm-rg":
        row["gap_reason"] = "Specialist algebra remains a zero-body gap; the five regional idioms are separate zero-body routes"
        row["notes"] = (
            "Three individually verified official Rumantsch Grischun general "
            "school-mathematics examination parts are active; specialist algebra "
            "remains a zero-body gap; inherited forms are not corpus attestation"
        )
        row["review_status"] = (
            "route_implemented_three_general_school_math_bodies_specialist_algebra_gap"
        )
    rows.append(row)

fields = list(rows[0])
with OUT.open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

rm_row = next(r for r in rows if r["variety_code"] == "rm-rg")
rm_idiom_rows = [r for r in rows if r["variety_code"] in RM_REGIONAL_IDIOMS]
summary = {
    "artifact": "ROMANCE_BRANCH_ROUTING_LEDGER_v2",
    "route_count": len(rows),
    "active_routes": sum(r["current_active_body_count"] != "0" for r in rows),
    "explicit_zero_routes": sum(r["current_active_body_count"] == "0" for r in rows),
    "macrobranches": sorted({r["macrobranch"] for r in rows}),
    "gallo_italic_routes": [r["variety_name"] for r in rows if r["subbranch"] == "Gallo-Italic"],
    "istriot_route_present": any(r["variety_code"] == "ist" for r in rows),
    "romansh_active_body_count": int(rm_row["current_active_body_count"]),
    "romansh_general_school_math_body_count": int(rm_row["current_general_school_math_body_count"]),
    "romansh_specialist_algebra_body_count": int(rm_row["current_specialist_algebra_body_count"]),
    "romansh_inherited_form_attestation_count": int(rm_row["inherited_form_attestation_count"]),
    "romansh_active_source_ids": rm_row["current_source_ids"].split(";"),
    "romansh_regional_idiom_routes": [r["variety_code"] for r in rm_idiom_rows],
    "romansh_regional_idiom_active_body_count": sum(int(r["current_active_body_count"]) for r in rm_idiom_rows),
    "dominant_standard_proxy_violations": sum(r["dominant_standard_not_proxy"] != "true" for r in rows),
    "corpus_manifest_sha256": sha(CORPUS),
    "coverage_sha256": sha(COVERAGE),
    "curated_source_manifest_sha256": sha(CURATED),
    "claim_boundary": (
        "The three active rm-rg bodies are official general school-mathematics "
        "examination parts, not specialist algebra; inherited forms are not corpus "
        "attestation and the five regional idiom routes remain zero-body."
    ),
    "ledger_sha256": sha(OUT),
}
SUMMARY.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

assert len({r["route_id"] for r in rows}) == len(rows)
assert len({r["variety_code"] for r in rows}) == len(rows)
assert summary["istriot_route_present"]
assert set(summary["gallo_italic_routes"]) >= {"Piedmontese", "Lombard", "Ligurian", "Emilian-Romagnol"}
assert summary["active_routes"] == 8 and summary["explicit_zero_routes"] == 53
assert summary["romansh_active_body_count"] == 3
assert summary["romansh_general_school_math_body_count"] == 3
assert summary["romansh_specialist_algebra_body_count"] == 0
assert summary["romansh_inherited_form_attestation_count"] == 0
assert set(summary["romansh_active_source_ids"]) == EXPECTED_RM_SOURCE_IDS
assert summary["romansh_regional_idiom_active_body_count"] == 0
assert set(summary["romansh_regional_idiom_routes"]) == RM_REGIONAL_IDIOMS
assert all(r["term_promotion_eligible"] == "false" for r in corpus if r["language"] == "rm")
assert summary["dominant_standard_proxy_violations"] == 0

lines = [
    f"PASS routes={len(rows)}",
    f"active_routes={summary['active_routes']}",
    f"explicit_zero_routes={summary['explicit_zero_routes']}",
    f"romansh_active_bodies={summary['romansh_active_body_count']}",
    f"romansh_general_school_math_bodies={summary['romansh_general_school_math_body_count']}",
    f"romansh_specialist_algebra_bodies={summary['romansh_specialist_algebra_body_count']}",
    f"romansh_inherited_form_attestations={summary['romansh_inherited_form_attestation_count']}",
    f"romansh_regional_idiom_active_bodies={summary['romansh_regional_idiom_active_body_count']}",
    f"corpus_manifest_sha256={summary['corpus_manifest_sha256']}",
    f"ledger_sha256={summary['ledger_sha256']}",
]
LOG.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))

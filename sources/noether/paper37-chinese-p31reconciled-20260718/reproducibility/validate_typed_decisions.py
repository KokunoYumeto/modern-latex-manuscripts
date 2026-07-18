#!/usr/bin/env python3
"""Validate Paper 37 typed decisions, bindings, joins, and claim controls."""
from __future__ import annotations

from datetime import datetime
from pathlib import Path
import csv
import hashlib
import importlib.metadata
import json

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT.parents[4]
SCHEMA = PROJECT / "01_methodology/research_department/OPERATIONAL_DECISION_INTERFACE.schema.json"
SCHEMA_EXPECTED = "6891F9E689FD14A77AF4EE33F3C45E1D293BC68BCDCEB3524640B69C6AFCCAF1"
DECISIONS = ROOT / "decisions"
CROSSWALK = ROOT / "evidence/NOE-P37_CJKV_CROSSWALK.csv"
OUT = ROOT / "qa/DECISION_SCHEMA_VALIDATION_REPORT.json"
EXPECTED_TOTAL = 17
EXPECTED_HANS = 16
EXPECTED_HANT = 1
HANS_TARGET_HASH = "A4A0A97E548840915650FE813AED8FC120D2ABE79F3FA76F9ADF35D5EDAB1B0C"
HANT_TARGET_HASH = "FC2493ADE14D66835C0EBAAD7C84C78AFFD33A357594F45384CD518C94F32012"
HANT_RECORD_HASH = "6DCACC6A7BC51FDABD796AC154157F8A0E86D0B40F12707774B4736283F18372"

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


def is_sha256(value: object) -> bool:
    return isinstance(value, str) and len(value) == 64 and all(ch in "0123456789ABCDEFabcdef" for ch in value)


def resolve(path_text: str) -> Path | None:
    text = path_text.replace("\\", "/")
    candidate = Path(text)
    if candidate.is_absolute():
        return candidate
    if text.startswith(("03_projects/", "01_methodology/")):
        return PROJECT / candidate
    if text.startswith(
        (
            "source/",
            "witness/",
            "evidence/",
            "qa/",
            "decisions/",
            "zh-Hans-CN/",
            "zh-Hant-controlled/",
        )
    ):
        return ROOT / candidate
    return None


schema_hash = sha(SCHEMA)
schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
validator = Draft202012Validator(schema, format_checker=FormatChecker())
errors: list[dict] = []
records: list[dict] = []
hash_cache: dict[Path, str] = {}
paths = sorted(DECISIONS.glob("*.json"))
hans_paths: list[Path] = []
hant_paths: list[Path] = []
declared_artifact_checks = 0
claim_control_checks = 0


def cached_sha(path: Path) -> str:
    if path not in hash_cache:
        hash_cache[path] = sha(path)
    return hash_cache[path]


for path in paths:
    data = json.loads(path.read_text(encoding="utf-8"))
    schema_errors = sorted(validator.iter_errors(data), key=lambda error: list(error.absolute_path))
    for error in schema_errors:
        errors.append(
            {
                "record": path.name,
                "kind": "schema",
                "location": "/".join(map(str, error.absolute_path)),
                "message": error.message,
            }
        )

    language_tag = data["target"]["language_tag"]
    if language_tag == "zh-Hans-CN":
        hans_paths.append(path)
    elif language_tag == "zh-Hant":
        hant_paths.append(path)
    else:
        errors.append({"record": path.name, "kind": "unsupported_target_tag", "language_tag": language_tag})

    candidate_ids = {candidate["candidate_id"] for candidate in data["candidates"]}
    if data["decision"]["selected_candidate_id"] not in candidate_ids:
        errors.append({"record": path.name, "kind": "selected_candidate", "message": "selected candidate is absent from candidates"})
    if data["readiness_gates"]["internal_qa"]["status"] != "pass":
        errors.append({"record": path.name, "kind": "internal_qa", "message": "internal QA is not pass"})

    # Unsupported regional/external/human promotion is structurally prohibited.
    claim_checks = {
        "external_review_pending": data["readiness_gates"]["external_review"]["status"] == "pending",
        "human_comprehension_pending": data["readiness_gates"]["human_comprehension"]["status"] == "pending",
        "branch_review_not_pass": data["readiness_gates"]["branch_or_cohort_review"]["status"] != "pass",
        "auto_promotion_prohibited": data["decision"].get("auto_promotion_prohibited") is True,
        "no_regional_target_tag": language_tag not in {"zh-Hans-SG", "zh-Hant-TW", "zh-Hant-HK", "zh-Hant-MO"},
    }
    claim_control_checks += len(claim_checks)
    failed_claim_checks = sorted(key for key, value in claim_checks.items() if not value)
    if failed_claim_checks:
        errors.append({"record": path.name, "kind": "unsupported_claim_control", "failed_checks": failed_claim_checks})

    declared: list[tuple[str, str, str]] = [
        (
            "work.source_snapshot",
            data["work"]["source_snapshot"]["path_or_uri"],
            data["work"]["source_snapshot"]["sha256_or_version"],
        )
    ]
    for channel in ("support", "candidate", "competitor", "adverse", "veto"):
        for item in data["evidence"][channel]:
            declared.append(
                (
                    f"evidence.{channel}.{item['evidence_id']}",
                    item["source"]["path_or_uri"],
                    item["source"]["sha256_or_version"],
                )
            )
    for artifact in data["provenance"]["input_artifacts"]:
        declared.append(("provenance.input_artifacts", artifact["path_or_uri"], artifact["version_or_hash"]))

    for locus, path_text, expected in declared:
        declared_artifact_checks += 1
        resolved = resolve(path_text)
        if resolved is None:
            errors.append({"record": path.name, "kind": "unresolved_path", "location": locus, "path": path_text})
        elif not resolved.exists():
            errors.append({"record": path.name, "kind": "missing_path", "location": locus, "path": str(resolved)})
        elif is_sha256(expected):
            actual = cached_sha(resolved)
            if actual != expected.upper():
                errors.append(
                    {
                        "record": path.name,
                        "kind": "hash_mismatch",
                        "location": locus,
                        "path": str(resolved),
                        "expected": expected.upper(),
                        "actual": actual,
                    }
                )

    records.append(
        {
            "record": path.name,
            "sha256": sha(path),
            "schema_error_count": len(schema_errors),
            "decision_status": data["decision"]["status"],
            "target_language_tag": language_tag,
            "internal_qa": data["readiness_gates"]["internal_qa"]["status"],
            "claim_control_status": "pass" if not failed_claim_checks else "fail",
        }
    )

with CROSSWALK.open("r", encoding="utf-8", newline="") as handle:
    crosswalk_rows = list(csv.DictReader(handle))
crosswalk_concepts: set[str] = set()
for row in crosswalk_rows:
    concept_id = row["concept_id"]
    if concept_id in crosswalk_concepts:
        errors.append({"kind": "crosswalk_duplicate_concept", "concept_id": concept_id})
    crosswalk_concepts.add(concept_id)
    decision_path = ROOT / row["decision_record_path"]
    if not decision_path.exists():
        errors.append({"kind": "crosswalk_decision_missing", "concept_id": concept_id, "path": str(decision_path)})
        continue
    decision = json.loads(decision_path.read_text(encoding="utf-8"))
    if decision["concept"]["concept_id"] != concept_id:
        errors.append(
            {
                "kind": "crosswalk_concept_mismatch",
                "concept_id": concept_id,
                "decision_concept_id": decision["concept"]["concept_id"],
            }
        )
    if decision["target"]["language_tag"] != "zh-Hans-CN":
        errors.append({"kind": "crosswalk_non_hans_record", "concept_id": concept_id, "language_tag": decision["target"]["language_tag"]})

if len(paths) != EXPECTED_TOTAL:
    errors.append({"kind": "decision_count", "expected": EXPECTED_TOTAL, "actual": len(paths)})
if len(hans_paths) != EXPECTED_HANS:
    errors.append({"kind": "hans_decision_count", "expected": EXPECTED_HANS, "actual": len(hans_paths)})
if len(hant_paths) != EXPECTED_HANT:
    errors.append({"kind": "hant_decision_count", "expected": EXPECTED_HANT, "actual": len(hant_paths)})
if len(crosswalk_rows) != EXPECTED_HANS:
    errors.append({"kind": "crosswalk_row_count", "expected": EXPECTED_HANS, "actual": len(crosswalk_rows)})
if schema_hash != SCHEMA_EXPECTED:
    errors.append({"kind": "schema_hash", "expected": SCHEMA_EXPECTED, "actual": schema_hash})

for name, expected in HANS_EXPECTED.items():
    path = DECISIONS / name
    if not path.exists():
        errors.append({"kind": "preserved_hans_missing", "record": name})
    elif sha(path) != expected:
        errors.append({"kind": "preserved_hans_hash", "record": name, "expected": expected, "actual": sha(path)})

hant_path = DECISIONS / "NOE-P37-ZH-HANT-SCRIPT.json"
if not hant_path.exists():
    errors.append({"kind": "hant_record_missing"})
else:
    if sha(hant_path) != HANT_RECORD_HASH:
        errors.append({"kind": "hant_record_hash", "expected": HANT_RECORD_HASH, "actual": sha(hant_path)})
    hant = json.loads(hant_path.read_text(encoding="utf-8"))
    provenance_bindings = {item["path_or_uri"]: item["version_or_hash"] for item in hant["provenance"]["input_artifacts"]}
    required_bindings = {
        "zh-Hans-CN/Noether_Paper37_Chinese_P31Reconciled_zh-Hans-CN_v001.tex": HANS_TARGET_HASH,
        "zh-Hant-controlled/Noether_Paper37_Chinese_P31Reconciled_zh-Hant-controlled_v001.tex": HANT_TARGET_HASH,
    }
    for artifact, expected in required_bindings.items():
        if provenance_bindings.get(artifact) != expected:
            errors.append({"kind": "hant_binding_missing", "artifact": artifact, "expected": expected, "actual": provenance_bindings.get(artifact)})
    if hant["concept"]["concept_id"] != "NOE-P37-CONTROLLED-HANT-SCRIPT":
        errors.append({"kind": "hant_concept_id", "actual": hant["concept"]["concept_id"]})
    excluded = " ".join(hant["concept"]["excluded_senses"])
    for required in ("Taiwan", "Hong Kong", "Macao", "external", "human"):
        if required not in excluded:
            errors.append({"kind": "hant_exclusion_missing", "required": required})

report = {
    "schema_version": "1.0.0",
    "validation_id": "NOE-P37-ZH-TYPED-DECISIONS-20260718",
    "recorded_at": datetime.now().astimezone().isoformat(timespec="seconds"),
    "validator": {"library": "jsonschema", "version": importlib.metadata.version("jsonschema"), "format_checker": True},
    "schema": {"path": str(SCHEMA), "sha256": schema_hash},
    "decision_count": len(paths),
    "hans_decision_count": len(hans_paths),
    "hant_decision_count": len(hant_paths),
    "preserved_hans_hash_count": sum(1 for name, expected in HANS_EXPECTED.items() if (DECISIONS / name).exists() and sha(DECISIONS / name) == expected),
    "crosswalk_row_count": len(crosswalk_rows),
    "crosswalk_sha256": sha(CROSSWALK),
    "declared_artifact_hash_or_existence_check_count": declared_artifact_checks,
    "claim_control_check_count": claim_control_checks,
    "bound_targets": {"zh-Hans-CN_sha256": HANS_TARGET_HASH, "zh-Hant_controlled_sha256": HANT_TARGET_HASH},
    "records": records,
    "error_count": len(errors),
    "errors": errors,
    "status": "pass" if not errors else "fail",
    "validation_scope": "Operational-decision schema, selected candidate, internal QA, exact preservation of 16 Hans records, explicit Hans/Hant checkpoint binding, 16-row Hans crosswalk joins, declared artifact existence/hashes, and structural prohibition of unsupported regional/external/human promotion; not external linguistic certification.",
}
OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"path": str(OUT), "sha256": sha(OUT), "status": report["status"], "records": len(paths), "errors": len(errors)}, ensure_ascii=True, indent=2))
raise SystemExit(0 if not errors else 1)

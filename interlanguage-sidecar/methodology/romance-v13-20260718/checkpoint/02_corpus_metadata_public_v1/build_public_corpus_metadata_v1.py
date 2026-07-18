from __future__ import annotations

import csv
import hashlib
import json
import re
import shutil
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CORPUS = ROOT / "corpus" / "ROMANCE_CONSOLIDATED_CORPUS_v5.csv"
ROUTES = ROOT / "corpus" / "ROMANCE_BRANCH_ROUTING_LEDGER_v4.csv"
LANGUAGE_COVERAGE = ROOT / "corpus" / "ROMANCE_CORPUS_LANGUAGE_DOMAIN_COVERAGE_v5.csv"
VARIETY_COVERAGE = ROOT / "corpus" / "ROMANCE_CORPUS_LANGUAGE_VARIETY_DOMAIN_COVERAGE_v1.csv"
REJECTED = ROOT / "corpus" / "ROMANCE_CORPUS_REJECTED_OR_EXCLUDED_v4.csv"
CORPUS_AUDIT = ROOT / "qa" / "CORPUS_BRANCH_PACKAGE_AUDIT_v3.json"
BUILDER = Path(__file__).resolve()
VALIDATOR = ROOT / "scripts" / "validate_public_corpus_metadata_v1.py"
OUT = ROOT / "outputs" / "romance_corpus_metadata_checkpoint_v1_20260718"

PUBLIC_CORPUS = OUT / "ROMANCE_CORPUS_METADATA_v1.csv"
PUBLIC_ROUTES = OUT / "ROMANCE_BRANCH_ROUTES_v1.csv"
PUBLIC_LANGUAGE = OUT / "ROMANCE_LANGUAGE_COVERAGE_v1.csv"
PUBLIC_VARIETY = OUT / "ROMANCE_VARIETY_COVERAGE_v1.csv"
PUBLIC_REJECTED = OUT / "ROMANCE_REJECTED_EVIDENCE_METADATA_v1.csv"
SOURCE_BINDING = OUT / "SOURCE_BINDING_v1.json"
README = OUT / "README.md"
BUILDER_COPY = OUT / "build_public_corpus_metadata_v1.py"
VALIDATOR_COPY = OUT / "validate_public_corpus_metadata_v1.py"


CORPUS_FIELDS = [
    "record_id", "logical_source_id", "language", "variety_code",
    "standard_or_idiom", "region", "script", "secondary_language",
    "institution", "publication_date", "retrieved_at", "domain",
    "domain_tags", "domain_review_status", "register", "title_or_query",
    "representation", "source_bytes", "source_sha256", "search_text_sha256",
    "search_text_contract", "public_upstream_locator", "locator_visibility",
    "revision_or_version", "source_use_status", "license_signal",
    "license_status", "hash_verification", "sense_review_status",
    "corpus_topic_eligible", "native_source", "generated", "dedupe_status",
    "counting_eligible", "term_promotion_eligible", "corpus_role",
    "active_body_eligible", "official_lexical_reference",
    "translation_family_id", "translation_sibling_status",
    "specialist_algebra_eligible", "intake_source_id",
    "intake_manifest_sha256",
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def public_locator(value: str) -> tuple[str, str]:
    value = (value or "").strip()
    if value.lower().startswith(("https://", "http://")):
        return value, "public_http_locator_preserved"
    if value:
        return "", "local_or_non_http_locator_omitted"
    return "", "no_locator_recorded"


def normalize_tags(value: str) -> str:
    value = (value or "").strip()
    if value.startswith("["):
        quoted = re.findall(r"['\"]([^'\"]+)['\"]", value)
        if quoted:
            return ";".join(dict.fromkeys(quoted))
    return ";".join(part.strip(" '[]\"") for part in value.split(";") if part.strip(" '[]\""))


def sanitize_corpus(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    output: list[dict[str, str]] = []
    for row in rows:
        locator, visibility = public_locator(row["upstream_locator"])
        public = {field: row.get(field, "") for field in CORPUS_FIELDS}
        public.update({
            "source_bytes": row["bytes"],
            "source_sha256": row["sha256"],
            "public_upstream_locator": locator,
            "locator_visibility": visibility,
            "domain_tags": normalize_tags(row["domain_tags"]),
        })
        output.append(public)
    return output


def sanitize_rejected(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    output = []
    for row in rows:
        locator, visibility = public_locator(row["locator"])
        output.append({
            "source": row["source"],
            "public_locator": locator,
            "locator_visibility": visibility,
            "reason": row["reason"],
        })
    return output


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    corpus = read_csv(CORPUS)
    routes = read_csv(ROUTES)
    language = read_csv(LANGUAGE_COVERAGE)
    variety = read_csv(VARIETY_COVERAGE)
    rejected = read_csv(REJECTED)
    audit = json.loads(CORPUS_AUDIT.read_text(encoding="utf-8"))

    public_corpus = sanitize_corpus(corpus)
    public_rejected = sanitize_rejected(rejected)
    write_csv(PUBLIC_CORPUS, public_corpus, CORPUS_FIELDS)
    write_csv(PUBLIC_ROUTES, routes, list(routes[0]))
    public_language = [{**row, "domains": normalize_tags(row["domains"])} for row in language]
    public_variety = [{**row, "domains": normalize_tags(row["domains"])} for row in variety]
    write_csv(PUBLIC_LANGUAGE, public_language, list(language[0]))
    write_csv(PUBLIC_VARIETY, public_variety, list(variety[0]))
    write_csv(
        PUBLIC_REJECTED,
        public_rejected,
        ["source", "public_locator", "locator_visibility", "reason"],
    )

    source_hashes = {
        path.relative_to(ROOT).as_posix(): sha(path)
        for path in (CORPUS, ROUTES, LANGUAGE_COVERAGE, VARIETY_COVERAGE, REJECTED, CORPUS_AUDIT)
    }
    counts = {
        "records": len(corpus),
        "primary_unique": sum(row["dedupe_status"] == "primary_unique" for row in corpus),
        "representation_aliases": sum("representation_alias" in row["dedupe_status"] for row in corpus),
        "counting_eligible": sum(row["counting_eligible"] == "true" for row in corpus),
        "active_body_eligible": sum(row["active_body_eligible"] == "true" for row in corpus),
        "official_lexical_references": sum(row["official_lexical_reference"] == "true" for row in corpus),
        "routes": len(routes),
        "active_routes": sum(int(row["current_active_body_count"]) > 0 for row in routes),
        "zero_body_routes": sum(int(row["current_active_body_count"]) == 0 for row in routes),
        "rejected_or_excluded_metadata_rows": len(rejected),
        "languages": dict(sorted(Counter(row["language"] for row in corpus).items())),
    }
    binding = {
        "artifact": "ROMANCE_CORPUS_PUBLIC_METADATA_SOURCE_BINDING_v1",
        "status": "METADATA_ONLY_RIGHTS_AWARE_CHECKPOINT",
        "source_hashes": source_hashes,
        "source_audit_status": audit["status"],
        "source_audit_checks": [audit["passed_check_count"], audit["check_count"]],
        "counts": counts,
        "omitted_fields": ["absolute_path", "search_text_path"],
        "omitted_payload_classes": [
            "source PDFs and other source bytes",
            "extracted or search text",
            "quotations and quotation-bearing workbooks",
            "local and non-HTTP locators",
        ],
        "claim_boundary": {
            "human_observations": 0,
            "native_validations": 0,
            "term_promotions": 0,
            "intelligibility_claim": False,
            "lane_completion_claim": False,
        },
    }
    SOURCE_BINDING.write_text(
        json.dumps(binding, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )

    shutil.copyfile(BUILDER, BUILDER_COPY)
    shutil.copyfile(VALIDATOR, VALIDATOR_COPY)
    readme = f"""# Romance corpus metadata checkpoint v1

This is a publication-safe, metadata-only projection of the internal Romance corpus v5 and branch-routing ledger v4. It contains **{counts['records']} corpus records** and **{counts['routes']} explicit branch routes** ({counts['active_routes']} active, {counts['zero_body_routes']} zero-body). It does not redistribute source PDFs, extracted text, quotations, or quotation-bearing workbooks.

## What is included

- `ROMANCE_CORPUS_METADATA_v1.csv`: deduplicated source identities, language/variety/domain/register metadata, source and search-text SHA-256 values, license/status fields, public HTTP locators where available, and explicit eligibility/status flags.
- `ROMANCE_BRANCH_ROUTES_v1.csv`: 61 named standards/varieties, including explicit zero-body routes rather than dominant-language substitution.
- `ROMANCE_LANGUAGE_COVERAGE_v1.csv` and `ROMANCE_VARIETY_COVERAGE_v1.csv`: per-language and per-variety coverage.
- `ROMANCE_REJECTED_EVIDENCE_METADATA_v1.csv`: rejected searches, adverse evidence, and catalog-only records that do not count as corpus bodies.
- `SOURCE_BINDING_v1.json`: hashes of the internal inputs and exact projection boundary.

The eight initial standards—Spanish, French, Portuguese, Catalan, Italian, Galician, Romanian, and Romansh—each have at least one active reviewed mathematics body. Coverage is not equal: Romansh has seven active general-school bodies but **zero specialist-algebra bodies**; Surmiran and Sutsilvan remain explicit zero-body routes. The four 2025 branch-native Romansh documents total 60 pages but form one translation family and must not be treated as four independent exam designs.

## Rights and claim boundary

The source hash and license/status metadata are published for provenance. A source URL is not a reuse grant. Rights-unresolved bodies remain excluded from this payload. No corpus row is term-promotion eligible. This checkpoint contains zero human observations, zero native validation, zero empirical marginal-intelligibility results, and no lane-completion claim. Corpus occurrence is evidence requiring sense/register review, never canon.

Internal source checkpoint hashes are recorded in `SOURCE_BINDING_v1.json`. Run `python build_public_corpus_metadata_v1.py` inside the live lane, then `python validate_public_corpus_metadata_v1.py`, to reproduce and validate the projection.
"""
    README.write_text(readme, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()

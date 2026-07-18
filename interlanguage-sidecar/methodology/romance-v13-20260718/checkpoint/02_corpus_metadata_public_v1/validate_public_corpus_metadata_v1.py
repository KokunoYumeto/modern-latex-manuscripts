from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "outputs" / "romance_corpus_metadata_checkpoint_v1_20260718"
BUILDER = ROOT / "scripts" / "build_public_corpus_metadata_v1.py"
VALIDATOR = Path(__file__).resolve()
REPORT = OUT / "PUBLICATION_VALIDATION_v1.json"
MANIFEST = OUT / "CHECKPOINT_SHA256SUMS_v1.csv"
PUBLIC_FILES = [
    OUT / "ROMANCE_CORPUS_METADATA_v1.csv",
    OUT / "ROMANCE_BRANCH_ROUTES_v1.csv",
    OUT / "ROMANCE_LANGUAGE_COVERAGE_v1.csv",
    OUT / "ROMANCE_VARIETY_COVERAGE_v1.csv",
    OUT / "ROMANCE_REJECTED_EVIDENCE_METADATA_v1.csv",
    OUT / "SOURCE_BINDING_v1.json",
    OUT / "README.md",
    OUT / "build_public_corpus_metadata_v1.py",
    OUT / "validate_public_corpus_metadata_v1.py",
    OUT / "ROMANCE_CORPUS_METADATA_v1.xlsx",
    OUT / "build_public_corpus_workbook_v1.mjs",
    OUT / "normalize_xlsx_deterministic_v1.py",
    OUT / "qa" / "WORKBOOK_MACHINE_QA_v1.ndjson",
    OUT / "qa" / "WORKBOOK_VISUAL_QA_v1.md",
]
PREVIEWS = sorted((OUT / "qa" / "workbook_previews_v1").glob("*.png"))


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def rel(path: Path) -> str:
    return path.relative_to(OUT).as_posix()


def public_data_text() -> str:
    chunks = []
    # Scan the exported data and documentation.  The validator source itself
    # necessarily contains the forbidden-path detector's literal tokens.
    for path in PUBLIC_FILES[:7]:
        chunks.append(path.read_text(encoding="utf-8", errors="strict"))
    return "\n".join(chunks)


def main() -> None:
    checks: dict[str, bool] = {}
    before = {rel(path): sha(path) for path in PUBLIC_FILES if path.exists()}
    replay = subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, capture_output=True, text=True)
    after = {rel(path): sha(path) for path in PUBLIC_FILES if path.exists()}
    checks["builder_exit_zero"] = replay.returncode == 0
    checks["builder_byte_stable"] = before == after and len(after) == len(PUBLIC_FILES)

    corpus = read_csv(OUT / "ROMANCE_CORPUS_METADATA_v1.csv")
    routes = read_csv(OUT / "ROMANCE_BRANCH_ROUTES_v1.csv")
    language = read_csv(OUT / "ROMANCE_LANGUAGE_COVERAGE_v1.csv")
    variety = read_csv(OUT / "ROMANCE_VARIETY_COVERAGE_v1.csv")
    rejected = read_csv(OUT / "ROMANCE_REJECTED_EVIDENCE_METADATA_v1.csv")
    binding = json.loads((OUT / "SOURCE_BINDING_v1.json").read_text(encoding="utf-8"))

    checks["corpus_exact_153"] = len(corpus) == 153 and len({row["record_id"] for row in corpus}) == 153
    checks["corpus_partition_exact"] = (
        sum(row["dedupe_status"] == "primary_unique" for row in corpus),
        sum("representation_alias" in row["dedupe_status"] for row in corpus),
        sum(row["counting_eligible"] == "true" for row in corpus),
        sum(row["active_body_eligible"] == "true" for row in corpus),
        sum(row["official_lexical_reference"] == "true" for row in corpus),
    ) == (147, 6, 71, 70, 1)
    checks["all_term_promotion_false"] = all(row["term_promotion_eligible"] == "false" for row in corpus)
    checks["source_hashes_complete"] = all(re.fullmatch(r"[0-9A-F]{64}", row["source_sha256"]) for row in corpus)
    checks["domain_tags_publicly_normalized"] = all("[" not in row["domain_tags"] and "]" not in row["domain_tags"] for row in corpus) and all("[" not in row["domains"] and "]" not in row["domains"] for row in [*language, *variety])
    checks["search_hashes_complete_when_contract_present"] = all(
        bool(re.fullmatch(r"[0-9A-F]{64}", row["search_text_sha256"])) == bool(row["search_text_contract"])
        for row in corpus
    )
    checks["no_internal_path_columns"] = "absolute_path" not in corpus[0] and "search_text_path" not in corpus[0]
    checks["locators_http_or_blank"] = all(
        not row["public_upstream_locator"] or row["public_upstream_locator"].startswith(("https://", "http://"))
        for row in corpus
    )
    checks["route_exact_61_11_50"] = (
        len(routes),
        sum(int(row["current_active_body_count"]) > 0 for row in routes),
        sum(int(row["current_active_body_count"]) == 0 for row in routes),
    ) == (61, 11, 50)
    rm = {row["variety_code"]: row for row in routes if row["variety_code"].startswith("rm-")}
    checks["romansh_topology_and_gaps_exact"] = set(rm) == {
        "rm-rg", "rm-puter", "rm-sursilvan", "rm-vallader", "rm-surmiran", "rm-sutsilvan"
    } and {key: int(row["current_active_body_count"]) for key, row in rm.items()} == {
        "rm-rg": 4, "rm-puter": 1, "rm-sursilvan": 1, "rm-vallader": 1,
        "rm-surmiran": 0, "rm-sutsilvan": 0,
    } and all(row["current_specialist_algebra_body_count"] == "0" for row in rm.values())
    checks["language_and_variety_tables_present"] = len(language) == 9 and len(variety) >= 13
    checks["rejected_exact_9_and_public_locators"] = len(rejected) == 9 and all(
        not row["public_locator"] or row["public_locator"].startswith(("https://", "http://"))
        for row in rejected
    )
    checks["binding_source_audit_pass"] = binding["source_audit_status"] == "PASS" and binding["source_audit_checks"] == [36, 36]
    checks["binding_zero_claims"] = binding["claim_boundary"] == {
        "human_observations": 0,
        "intelligibility_claim": False,
        "lane_completion_claim": False,
        "native_validations": 0,
        "term_promotions": 0,
    }
    text = public_data_text()
    # A drive path has exactly one slash after the colon.  Requiring the next
    # character not to be another slash prevents the final `s://` in an HTTPS
    # locator from being mistaken for a Windows drive prefix.
    checks["no_windows_absolute_paths"] = not re.search(
        r"(?:[A-Za-z]:[\\/](?![\\/])|file:///|[Cc]%3[Aa]%5[Cc]Users)",
        text,
    )
    checks["rights_boundary_explicit"] = all(
        phrase in text.lower()
        for phrase in ("metadata-only", "rights-unresolved", "not a reuse grant", "zero human observations", "never canon")
    )
    checks["script_copies_exact"] = sha(OUT / BUILDER.name) == sha(BUILDER) and sha(OUT / VALIDATOR.name) == sha(VALIDATOR)
    workbook_path = OUT / "ROMANCE_CORPUS_METADATA_v1.xlsx"
    with ZipFile(workbook_path, "r") as archive:
        workbook_xml = archive.read("xl/workbook.xml").decode("utf-8")
        public_xml = "\n".join(
            archive.read(name).decode("utf-8", errors="ignore")
            for name in archive.namelist()
            if name.endswith((".xml", ".rels"))
        )
    required_sheets = {"Corpus", "Routes", "Language Coverage", "Variety Coverage", "Rejected Evidence", "Overview"}
    checks["workbook_six_sheets_exact"] = all(f'name="{name}"' in workbook_xml for name in required_sheets) and len(re.findall(r"<(?:\w+:)?sheet\b", workbook_xml)) == 6
    checks["workbook_no_personal_absolute_paths"] = not re.search(r"(?:[A-Za-z]:[\\/](?![\\/])|file:///|[Cc]%3[Aa]%5[Cc]Users)", public_xml)
    machine_qa = (OUT / "qa" / "WORKBOOK_MACHINE_QA_v1.ndjson").read_text(encoding="utf-8")
    checks["workbook_formula_values_and_error_scan"] = all(token in machine_qa for token in ('"Corpus records",153', '"Primary unique",147', '"Representation aliases",6', '"Zero-body routes",50', "Cell search matched 0 entries"))
    visual_qa = (OUT / "qa" / "WORKBOOK_VISUAL_QA_v1.md").read_text(encoding="utf-8")
    checks["workbook_visual_qa_six_previews_bound"] = len(PREVIEWS) == 6 and all(sha(path) in visual_qa for path in PREVIEWS)
    checks["workbook_current_hash_bound_and_honest"] = sha(workbook_path) in visual_qa and "byte-identical xlsx rebuild is **not claimed**" in visual_qa.lower()

    passed = all(checks.values())
    payload = {
        "artifact": "ROMANCE_CORPUS_METADATA_PUBLICATION_VALIDATION_v1",
        "status": "PASS" if passed else "FAIL",
        "checks": checks,
        "check_count": len(checks),
        "passed_check_count": sum(checks.values()),
        "counts": binding["counts"],
        "builder_replay": {
            "exit_code": replay.returncode,
            "stdout": replay.stdout,
            "stderr": replay.stderr,
            "before": before,
            "after": after,
        },
        "public_file_hashes": {rel(path): sha(path) for path in PUBLIC_FILES},
        "claim_boundary": binding["claim_boundary"],
    }
    REPORT.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )

    targets = [*PUBLIC_FILES, REPORT]
    with MANIFEST.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["relative_path", "bytes", "sha256"], lineterminator="\n")
        writer.writeheader()
        for path in targets:
            writer.writerow({"relative_path": rel(path), "bytes": path.stat().st_size, "sha256": sha(path)})

    failed = [name for name, value in checks.items() if not value]
    print(f"{'PASS' if passed else 'FAIL'} public corpus metadata v1 checks={len(checks)} passed={sum(checks.values())}")
    print("records=153 primary=147 aliases=6 counting=71 active=70 routes=61 active_routes=11 zero_routes=50")
    print(f"validation_sha256={sha(REPORT)} manifest_sha256={sha(MANIFEST)}")
    for name in failed:
        print(f"FAIL {name}")
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

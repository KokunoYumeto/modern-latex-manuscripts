from __future__ import annotations

import csv
import hashlib
import json
import logging
from pathlib import Path

from PIL import Image, ImageStat
from pypdf import PdfReader

logging.getLogger("pypdf").setLevel(logging.ERROR)


INTAKE = Path(__file__).resolve().parent.parent
RAW = INTAKE / "raw"
EXTRACTED = INTAKE / "extracted"
MANIFEST_PATH = INTAKE / "manifests/intake_manifest.json"
COVERAGE_PATH = INTAKE / "manifests/coverage_delta.json"
VISUAL_QA = INTAKE / "qa/VISUAL_QA.md"
REPORT = INTAKE / "qa/intake_validation.json"
HASH_MANIFEST = INTAKE / "qa/SHA256SUMS_v1.csv"
DECISION_LEDGER = INTAKE.parents[3] / "00_lane_control/ROMANCE_DECISION_LEDGER_v1.jsonl"

RAW_EXPECTED = {
    "matematica_landing.html": "1DE796600DE3E6896E1B662053F950C7EDC4B2BF134AAC6A3B927DD18275451B",
    "MA_1_A_4_terms_equations.html": "26D4A1DE9F897B0139319EC665391126C4CBC8B54054EEA6BACF50F29EA63AFB",
    "MA_1_A_4_terms_equations_printout.pdf": "47402DF6127CA3F18725704DAED58DE5412BAD7D1639CD67FE4D59B0524EEED0",
    "Matematica_full_subject_printout.pdf": "809FA86CEA7AE27DC2DAD0EAF7467F776CBD6303EB54B436E3E087971881FE05",
}
PDF_TEXT_EXPECTED = {
    "MA_1_A_4_terms_equations_printout.txt": "588919211E43F9E5BB0834306B9B25DC146D13057F7EEEB4A0062805C49A6D67",
    "Matematica_full_subject_printout.txt": "8412A95D48113CF58C0BBC145D21D66543AB4C554BB6F0699F34229B67E66513",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def check(results: dict[str, bool], name: str, value: bool) -> None:
    results[name] = bool(value)


def nonblank_image(path: Path) -> bool:
    with Image.open(path) as image:
        image = image.convert("L")
        stat = ImageStat.Stat(image)
        return image.width > 500 and image.height > 700 and stat.var[0] > 10


def main() -> None:
    results: dict[str, bool] = {}
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    coverage = json.loads(COVERAGE_PATH.read_text(encoding="utf-8"))

    check(results, "raw_four_hashes", all(sha256(RAW / name) == expected for name, expected in RAW_EXPECTED.items()))
    check(results, "pdf_text_hashes", all(sha256(EXTRACTED / name) == expected for name, expected in PDF_TEXT_EXPECTED.items()))
    check(results, "pdf_pages_2_30", len(PdfReader(RAW / "MA_1_A_4_terms_equations_printout.pdf").pages) == 2 and len(PdfReader(RAW / "Matematica_full_subject_printout.pdf").pages) == 30)

    competency = (EXTRACTED / "MA_1_A_4_terms_equations_printout.txt").read_text(encoding="utf-8")
    full = (EXTRACTED / "Matematica_full_subject_printout.txt").read_text(encoding="utf-8")
    html_text = (EXTRACTED / "MA_1_A_4_terms_equations_html.txt").read_text(encoding="utf-8")
    terms = [
        "terms algebraics",
        "equaziuns linearas",
        "polinoms",
        "equaziuns quadratas",
        "terms fracziunals",
        "sistems d'equaziuns linearas",
    ]
    check(results, "school_algebra_terms_in_competency_pdf", all(term in competency for term in terms))
    check(results, "school_algebra_terms_in_full_pdf", all(term in full for term in terms))
    check(results, "school_algebra_terms_in_html", all(term in html_text for term in terms))

    records = manifest["records"]
    check(results, "manifest_topology_4_1_3", manifest["record_count"] == len(records) == 4 and manifest["primary_counting_body_count"] == 1 and manifest["active_representation_count"] == 3)
    check(results, "exact_variety_rm_rg", manifest["variety_code"] == "rm-rg" and {row["variety_code"] for row in records} == {"rm-rg"})
    check(results, "official_https_urls", manifest["authority_domain"] == "gr-r.lehrplan.ch" and all(row["url"].startswith("https://gr-r.lehrplan.ch/") for row in records))
    check(results, "dedup_primary_aliases", sum(row["counting_eligible"] for row in records) == 1 and sum(row["alias_of"] is not None for row in records) == 2 and {row["alias_of"] for row in records if row["alias_of"]} == {"CURATED-RM-RG-PI21-MATEMATICA-FULL"})
    classification = manifest["classification"]
    check(results, "school_algebra_not_abstract_algebra", classification["specialist_school_algebra_body_present"] is True and classification["abstract_algebra_ring_field_module_research_body_present"] is False)
    check(results, "no_idiom_proxy", classification["non_rm_rg_idiom_proxy_authorized"] is False and coverage["other_romansh_idiom_body_delta"] == 0)
    check(results, "rights_unresolved", "not_cleared" in manifest["rights_status"] and manifest["redistribution_status"] == "internal_evidence_only_pending_rights_review")
    check(results, "server_dynamic_pdf_boundary", "not expected to be byte-identical" in manifest["server_pdf_replay_boundary"])
    check(results, "coverage_delta_exact", coverage["new_deduplicated_counting_bodies"] == 1 and coverage["new_deduplicated_pages"] == 30 and coverage["school_algebra_body_delta"] == 1 and coverage["abstract_algebra_body_delta"] == 0 and coverage["human_observations"] == 0)

    competency_renders = sorted((INTAKE / "qa/rendered/competency").glob("*.png"))
    full_renders = sorted((INTAKE / "qa/rendered/full_subject").glob("*.png"))
    check(results, "render_counts_2_30", len(competency_renders) == 2 and len(full_renders) == 30)
    check(results, "all_renders_nonblank", all(nonblank_image(path) for path in competency_renders + full_renders))
    check(results, "contact_sheet_nonblank", nonblank_image(INTAKE / "qa/full_subject_contact_sheet.png"))
    visual = VISUAL_QA.read_text(encoding="utf-8")
    check(results, "visual_QA_exact_scope", "2/2" in visual and "30/30" in visual and "partially clipped continuation header" in visual and "PASS_WITH_RECORDED_SOURCE_LAYOUT_DEFECT" in visual)
    check(results, "decision_log_link", "RDL-0015" in DECISION_LEDGER.read_text(encoding="utf-8") and "Plan d'instrucziun 21" in DECISION_LEDGER.read_text(encoding="utf-8"))

    excluded = {REPORT.resolve(), HASH_MANIFEST.resolve()}
    targets = sorted(
        path for path in INTAKE.rglob("*")
        if path.is_file() and path.resolve() not in excluded
    )
    with HASH_MANIFEST.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(["relative_path", "bytes", "sha256"])
        for path in targets:
            writer.writerow([path.relative_to(INTAKE).as_posix(), path.stat().st_size, sha256(path)])
    rows = list(csv.DictReader(HASH_MANIFEST.open(encoding="utf-8", newline="")))
    check(results, "hash_manifest_unique_complete", len(rows) == len(targets) and len({row["relative_path"] for row in rows}) == len(rows) and all((INTAKE / row["relative_path"]).stat().st_size == int(row["bytes"]) and sha256(INTAKE / row["relative_path"]) == row["sha256"] for row in rows))

    status = "PASS" if all(results.values()) else "FAIL"
    report = {
        "artifact": "ROMANSH_CURRICULUM_INTAKE_VALIDATION_v1",
        "status": status,
        "checks_passed": sum(results.values()),
        "checks_total": len(results),
        "checks": results,
        "counts": {
            "raw_sources": 4,
            "primary_counting_bodies": 1,
            "active_representations": 3,
            "deduplicated_pages": 30,
            "physical_pdf_pages_including_excerpt": 32,
            "competency_renders": len(competency_renders),
            "full_subject_renders": len(full_renders),
            "school_algebra_bodies": 1,
            "abstract_algebra_bodies": 0,
            "human_observations": 0,
        },
        "hashes": {
            "intake_manifest": sha256(MANIFEST_PATH),
            "coverage_delta": sha256(COVERAGE_PATH),
            "README": sha256(INTAKE / "README.md"),
            "visual_QA": sha256(VISUAL_QA),
            "build_script": sha256(INTAKE / "scripts/build_intake.py"),
            "render_script": sha256(INTAKE / "scripts/render_intake.ps1"),
            "validator": sha256(Path(__file__).resolve()),
            "sha256_manifest": sha256(HASH_MANIFEST),
        },
        "claim_boundary": "Validated official Rumantsch Grischun school-algebra curriculum intake only; abstract algebra, other Romansh idioms, human intelligibility, native validation, and rights clearance remain unproven.",
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{status} ROMANSH_CURRICULUM_INTAKE checks={report['checks_passed']}/{report['checks_total']} hash_targets={len(rows)}")
    if status != "PASS":
        failed = [name for name, value in results.items() if not value]
        raise SystemExit("failed checks: " + ", ".join(failed))


if __name__ == "__main__":
    main()

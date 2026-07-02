import hashlib
import json
import sys
import zipfile
from pathlib import Path


REQUIRED_SUBSTRINGS = [
    ".codex/config.toml",
    "logs/JAPANESE_REPRESENTATION_EXACT_SOURCE_RETRY_20260630T081000Z.json",
    "logs/JAPANESE_REPRESENTATION_EXACT_SOURCE_RETRY_20260630T081000Z.md",
    "logs/CHINESE_JAPANESE_CUMULATIVE_STATUS_MANIFEST_20260701T170500Z.json",
    "logs/CHINESE_JAPANESE_CUMULATIVE_STATUS_MANIFEST_20260701T170500Z.md",
    "tmp/build_chinese_japanese_cumulative_status_manifest_20260701.py",
    "logs/ARABIC_PERSIANATE_LANE_STATUS_MANIFEST_20260701T200500Z.json",
    "logs/ARABIC_PERSIANATE_LANE_STATUS_MANIFEST_20260701T200500Z.md",
    "tmp/build_arabic_persianate_lane_status_manifest_20260701.py",
    "logs/SLAVIC_MAINTENANCE_STATUS_MANIFEST_20260701T204500Z.json",
    "logs/SLAVIC_MAINTENANCE_STATUS_MANIFEST_20260701T204500Z.md",
    "tmp/build_slavic_maintenance_status_manifest_20260701.py",
    "logs/RESEARCH_PUBLICATION_LANE_STATUS_MANIFEST_20260701T213000Z.json",
    "logs/RESEARCH_PUBLICATION_LANE_STATUS_MANIFEST_20260701T213000Z.md",
    "tmp/build_research_publication_lane_status_manifest_20260701.py",
    "logs/JULY1_CANONICAL_HANDOFF_INDEX_20260701T220000Z.json",
    "logs/JULY1_CANONICAL_HANDOFF_INDEX_20260701T220000Z.md",
    "tmp/build_july1_canonical_handoff_index_20260701.py",
    "tmp/capture_japanese_representation_exact_search_20260630.py",
    "tmp/build_japanese_representation_exact_source_retry_20260630.py",
    "tmp/update_japanese_representation_exact_source_retry_coordination_20260630.py",
    "sources/non_slavic_reference_corpus/20260630T081000Z_japanese_representation_exact_source_retry/manifest.json",
    "sources/non_slavic_reference_corpus/20260630T081000Z_japanese_representation_exact_source_retry/search_capture_manifest.json",
    "sources/non_slavic_reference_corpus/20260630T081000Z_japanese_representation_exact_source_retry/raw_candidates/T2sp__rep__doc__rep_main.tex",
    "logs/SPANISH_COVARIANT_TEX_BROADER_RETRY_20260630T083000Z.json",
    "logs/SPANISH_COVARIANT_TEX_BROADER_RETRY_20260630T083000Z.md",
    "tmp/build_spanish_covariant_tex_broader_retry_20260630.py",
    "tmp/update_spanish_covariant_tex_broader_retry_coordination_20260630.py",
    "sources/non_slavic_reference_corpus/20260630T083000Z_spanish_covariant_tex_broader_retry/manifest.json",
    "sources/non_slavic_reference_corpus/20260630T083000Z_spanish_covariant_tex_broader_retry/search_results/covariante_tex.json",
    "sources/non_slavic_reference_corpus/20260630T083000Z_spanish_covariant_tex_broader_retry/raw_candidates/Chencho1561__Apuntes-Campos-Cuanticos__main.tex",
    "logs/TAJIK_CYRILLIC_MATH_SOURCE_RETRY_20260630T104800Z.json",
    "logs/TAJIK_CYRILLIC_MATH_SOURCE_RETRY_20260630T104800Z.md",
    "tmp/build_tajik_cyrillic_math_source_retry_20260630.py",
    "tmp/update_tajik_cyrillic_source_retry_coordination_20260630.py",
    "sources/non_slavic_reference_corpus/20260630T104800Z_tajik_cyrillic_math_source_retry/manifest.json",
    "sources/non_slavic_reference_corpus/20260630T104800Z_tajik_cyrillic_math_source_retry/search_results/locator_sources.json",
    "sources/non_slavic_reference_corpus/20260630T104800Z_tajik_cyrillic_math_source_retry/downloads/algebra_10_2023.pdf",
    "sources/non_slavic_reference_corpus/20260630T104800Z_tajik_cyrillic_math_source_retry/contexts/tj-alg10-2023_contexts.json",
    "logs/CONTROLLED_ARABIC_ABSTRACT_ALGEBRA_SOURCE_RETRY_20260630T092000Z.json",
    "logs/CONTROLLED_ARABIC_ABSTRACT_ALGEBRA_SOURCE_RETRY_20260630T092000Z.md",
    "tmp/build_controlled_arabic_abstract_algebra_source_retry_20260630.py",
    "tmp/update_controlled_arabic_abstract_algebra_source_retry_coordination_20260630.py",
    "sources/non_slavic_reference_corpus/20260630T092000Z_controlled_arabic_abstract_algebra_source_retry/manifest.json",
    "sources/non_slavic_reference_corpus/20260630T092000Z_controlled_arabic_abstract_algebra_source_retry/search_results/search_manifest.json",
    "sources/non_slavic_reference_corpus/20260630T092000Z_controlled_arabic_abstract_algebra_source_retry/downloads/mustansiriyah_abstract_algebra_2019.pdf",
    "sources/non_slavic_reference_corpus/20260630T092000Z_controlled_arabic_abstract_algebra_source_retry/normalized_text/ar-must-abstract-algebra-2019.normalized.txt",
    "sources/non_slavic_reference_corpus/20260630T092000Z_controlled_arabic_abstract_algebra_source_retry/contexts/ar-must-abstract-algebra-2019_contexts.json",
    "logs/CONTROLLED_ARABIC_ALGEBRA_SOURCE_REFRESH_20260702T013000Z.json",
    "logs/CONTROLLED_ARABIC_ALGEBRA_SOURCE_REFRESH_20260702T013000Z.md",
    "logs/ARABIC_PERSIANATE_LANE_STATUS_MANIFEST_20260702T014000Z.json",
    "logs/ARABIC_PERSIANATE_LANE_STATUS_MANIFEST_20260702T014000Z.md",
    "tmp/build_controlled_arabic_algebra_source_refresh_20260702.py",
    "tmp/build_arabic_persianate_lane_status_manifest_20260702.py",
    "sources/non_slavic_reference_corpus/20260702T013000Z_controlled_arabic_algebra_source_refresh/downloads/mustansiriyah_ring_theory_2019.pdf",
    "sources/non_slavic_reference_corpus/20260702T013000Z_controlled_arabic_algebra_source_refresh/normalized_text/mustansiriyah_ring_theory_2019.normalized.txt",
    "sources/non_slavic_reference_corpus/20260702T013000Z_controlled_arabic_algebra_source_refresh/contexts/mustansiriyah_ring_theory_2019_contexts.json",
    "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260630T175501Z.json",
    "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260630T175501Z.md",
    "sources/zenodo_updates/20260630_record20836874/zenodo_20836874_api_latest_20260630T175501Z.json",
    "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260630T181153Z.json",
    "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260630T181153Z.md",
    "sources/zenodo_updates/20260630_record20836874/zenodo_20836874_api_latest_20260630T181153Z.json",
    "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260630T184304Z.json",
    "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260630T184304Z.md",
    "sources/zenodo_updates/20260630_record20836874/zenodo_20836874_api_latest_20260630T184304Z.json",
    "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260630T213655Z.json",
    "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260630T213655Z.md",
    "sources/zenodo_updates/20260630_record20836874/zenodo_20836874_api_latest_20260630T213655Z.json",
    "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260701T143642Z.json",
    "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260701T143642Z.md",
    "sources/zenodo_updates/20260630_record20836874/zenodo_20836874_api_latest_20260701T143642Z.json",
    "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260701T145738Z.json",
    "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260701T145738Z.md",
    "sources/zenodo_updates/20260630_record20836874/zenodo_20836874_api_latest_20260701T145738Z.json",
    "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260701T194000Z.json",
    "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260701T194000Z.md",
    "sources/zenodo_updates/20260630_record20836874/zenodo_20836874_api_latest_20260701T194000Z.json",
    "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260701T222409Z.json",
    "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260701T222409Z.md",
    "sources/zenodo_updates/20260630_record20836874/zenodo_20836874_api_latest_20260701T222409Z.json",
    "logs/GOAL_SCOPE_STATUS_AUDIT_20260701T150000Z.json",
    "logs/GOAL_SCOPE_STATUS_AUDIT_20260701T150000Z.md",
    "tmp/build_goal_scope_status_audit_20260701.py",
    "logs/FRENCH_SPANISH_LANE_STATUS_AUDIT_20260701T153500Z.json",
    "logs/FRENCH_SPANISH_LANE_STATUS_AUDIT_20260701T153500Z.md",
    "tmp/build_french_spanish_lane_status_audit_20260701.py",
    "logs/SPANISH_CUMULATIVE_STATUS_MANIFEST_20260701T160000Z.json",
    "logs/SPANISH_CUMULATIVE_STATUS_MANIFEST_20260701T160000Z.md",
    "tmp/build_spanish_cumulative_status_manifest_20260701.py",
    "logs/FRENCH_CUMULATIVE_STATUS_MANIFEST_20260701T161500Z.json",
    "logs/FRENCH_CUMULATIVE_STATUS_MANIFEST_20260701T161500Z.md",
    "tmp/build_french_cumulative_status_manifest_20260701.py",
    "logs/R7_LAO_HIGHER_MATH_AND_AES_EXTRACTION_RETRY_20260630T212919Z.json",
    "logs/R7_LAO_HIGHER_MATH_AND_AES_EXTRACTION_RETRY_20260630T212919Z.md",
    "logs/R7_LAO_JICA_OFFICIAL_MATH_SOURCE_CAPTURE_20260701.json",
    "logs/R7_LAO_JICA_OFFICIAL_MATH_SOURCE_CAPTURE_AUDIT_20260701T144500Z.json",
    "logs/R7_LAO_JICA_OFFICIAL_MATH_SOURCE_CAPTURE_AUDIT_20260701T144500Z.md",
    "logs/R7_LAO_JICA_OCR_SPOTCHECK_AUDIT_20260701T145500Z.json",
    "logs/R7_LAO_JICA_OCR_SPOTCHECK_AUDIT_20260701T145500Z.md",
    "tmp/audit_r7_lao_jica_official_math_shelf_20260701.py",
    "tmp/build_r7_lao_jica_ocr_spotcheck_audit_20260701.py",
    "sources/non_slavic_reference_corpus/20260630T214900Z_r7_lao_jica_math_source_capture/metadata/jica_lao_math_source_capture_audit_manifest_20260701T144500Z.json",
    "sources/non_slavic_reference_corpus/20260630T214900Z_r7_lao_jica_math_source_capture/ocr_spotcheck/grade5_textbook_pages_001_003/page-001.png",
    "sources/non_slavic_reference_corpus/20260630T214900Z_r7_lao_jica_math_source_capture/ocr_spotcheck/grade5_textbook_pages_001_003/page-001.txt",
    "logs/PERMISSION_CONFIG_DOCUMENTED_REWRITE_20260630T214000Z.md",
    "logs/PERMISSION_CONFIG_DOCUMENTED_REASSERTION_20260630T215802Z.md",
    "logs/DEPENDENCY_REPAIR_20260701.md",
    "logs/WORKFLOW_LOG.md",
    "tmp/dependency_smoke_test_20260701.tex",
    "tmp/dependency_smoke_test_20260701/dependency_smoke_test_20260701.pdf",
    "tmp/dependency_smoke_test_20260701_rerun/dependency_smoke_test_20260701.pdf",
    "sources/non_slavic_reference_corpus/20260629T061500Z_r7_philippine_tai_hmong_austroasiatic_source_status/copied_prior_evidence/tai_kadai/lao_mathematics_teacher_manual.pdf",
    "sources/non_slavic_reference_corpus/20260629T061500Z_r7_philippine_tai_hmong_austroasiatic_source_status/extracted_text/lao_mathematics_teacher_manual.txt",
    "sources/non_slavic_reference_corpus/20260630T214900Z_r7_lao_jica_math_source_capture/raw_pages/jica_laos_math_materials_lao.html",
    "sources/non_slavic_reference_corpus/20260630T214900Z_r7_lao_jica_math_source_capture/downloads/Grade5_textbook_1.pdf",
    "sources/non_slavic_reference_corpus/20260630T214900Z_r7_lao_jica_math_source_capture/downloads/Grade5_teachers_guide_book_No_1_1.pdf",
    "sources/non_slavic_reference_corpus/20260630T214900Z_r7_lao_jica_math_source_capture/normalized_text/Grade5_textbook_1.txt",
    "sources/non_slavic_reference_corpus/20260630T214900Z_r7_lao_jica_math_source_capture/normalized_text/Grade5_teachers_guide_book_No_1_1.txt",
    "logs/CONTROLLED_ARABIC_INVARIANT_REGISTER_SWEEP_20260630T180627Z.json",
    "logs/CONTROLLED_ARABIC_INVARIANT_REGISTER_SWEEP_20260630T180627Z.md",
    "tmp/build_controlled_arabic_invariant_register_sweep_20260630.py",
    "tmp/update_controlled_arabic_invariant_register_sweep_coordination_20260630.py",
    "sources/non_slavic_reference_corpus/20260630T180627Z_controlled_arabic_invariant_register_sweep/manifest.json",
    "sources/non_slavic_reference_corpus/20260630T180627Z_controlled_arabic_invariant_register_sweep/search_results/search_manifest.json",
    "sources/non_slavic_reference_corpus/20260630T180627Z_controlled_arabic_invariant_register_sweep/normalized_text/shamra_geometric_invariant_theory_arabic_abstract.normalized.txt",
    "sources/non_slavic_reference_corpus/20260630T180627Z_controlled_arabic_invariant_register_sweep/contexts/shamra_geometric_invariant_theory_arabic_abstract_contexts.json",
    "logs/DARI_AFGHAN_MATH_PDF_FALLBACK_SHELF_20260630T182039Z.json",
    "logs/DARI_AFGHAN_MATH_PDF_FALLBACK_SHELF_20260630T182039Z.md",
    "tmp/build_dari_afghan_math_pdf_fallback_shelf_20260630.py",
    "tmp/update_dari_afghan_math_pdf_fallback_shelf_coordination_20260630.py",
    "sources/non_slavic_reference_corpus/20260630T182039Z_dari_afghan_math_pdf_fallback_shelf/manifest.json",
    "sources/non_slavic_reference_corpus/20260630T182039Z_dari_afghan_math_pdf_fallback_shelf/search_results/source_probe_pdf_selection_manifest.json",
    "sources/non_slavic_reference_corpus/20260630T182039Z_dari_afghan_math_pdf_fallback_shelf/downloads/ecampus_algebra_abdullah_momand.pdf",
    "sources/non_slavic_reference_corpus/20260630T182039Z_dari_afghan_math_pdf_fallback_shelf/downloads/moe_dari_math_grade_10_12.pdf",
    "sources/non_slavic_reference_corpus/20260630T182039Z_dari_afghan_math_pdf_fallback_shelf/normalized_text/ecampus_algebra_abdullah_momand.normalized.txt",
    "sources/non_slavic_reference_corpus/20260630T182039Z_dari_afghan_math_pdf_fallback_shelf/contexts/ecampus_algebra_abdullah_momand_contexts.json",
    "logs/SPANISH_P14_SOURCE_NATIVE_PATCH_20260630.json",
    "logs/SPANISH_P14_SOURCE_NATIVE_PATCH_20260630.md",
    "logs/R3_EXPANDED_TRANSLATION_AND_BRIDGE_REFRESH_20260630T182908Z.json",
    "logs/R3_EXPANDED_TRANSLATION_AND_BRIDGE_REFRESH_20260630T182908Z.md",
    "logs/R3_EXPANDED_TRANSLATION_AND_BRIDGE_REFRESH_VALIDATION_20260630T182908Z.json",
    "logs/R3_EXPANDED_TRANSLATION_AND_BRIDGE_REFRESH_VALIDATION_20260630T182908Z.md",
    "logs/REGIONAL_INTERLANGUAGE_CONTINUATION_WORKBOOK_20260630T174530Z.json",
    "logs/REGIONAL_INTERLANGUAGE_CONTINUATION_WORKBOOK_20260630T174530Z.md",
    "logs/REGIONAL_EVIDENCE_SIGNOFF_QUEUE_20260630T175625Z.json",
    "logs/REGIONAL_EVIDENCE_SIGNOFF_QUEUE_20260630T175625Z.md",
    "logs/REGIONAL_EXTERNAL_SESSION_INGEST_LEDGER_20260630T180056Z.json",
    "logs/REGIONAL_EXTERNAL_SESSION_INGEST_LEDGER_20260630T180056Z.md",
    "logs/CONTROLLED_ARABIC_INVARIANT_COVARIANT_BINARY_FORM_EXACT_SOURCE_CAPTURE_QUEUE_20260630T182511Z.json",
    "logs/CONTROLLED_ARABIC_INVARIANT_COVARIANT_BINARY_FORM_EXACT_SOURCE_CAPTURE_QUEUE_20260630T182511Z.md",
    "logs/R3_ALL13_EIGEN_SOURCE_FIRST_REVIEW_BUNDLE_20260630T182528Z.json",
    "logs/R3_ALL13_EIGEN_SOURCE_FIRST_REVIEW_BUNDLE_20260630T182528Z.md",
    "logs/R3_ALL13_EIGEN_SOURCE_FIRST_REVIEW_BUNDLE_VALIDATION_20260630T182528Z.json",
    "logs/R3_ALL13_EIGEN_SOURCE_FIRST_REVIEW_BUNDLE_VALIDATION_20260630T182528Z.md",
    "logs/R3_HIGH_RISK_LANE_SOURCE_RECOVERY_20260630T182147Z.json",
    "logs/R3_HIGH_RISK_LANE_SOURCE_RECOVERY_20260630T182147Z.md",
    "logs/CHINESE_JAPANESE_INTERLANGUAGE_WORKFLOW_INTEGRATION_20260629.json",
    "logs/CHINESE_JAPANESE_INTERLANGUAGE_WORKFLOW_INTEGRATION_20260629.md",
    "review_bundles/R3_All13_Eigen_Source_First_Review_Packet_20260630T182528Z/manifest.json",
    "review_bundles/R3_All13_Eigen_Source_First_Review_Packet_20260630T182528Z/source_quality_matrix.csv",
    "review_bundles/R3_All13_Eigen_Source_First_Review_Packet_20260630T182528Z/reviewer_return_template.json",
    "logs/R3_FULL_REGION_EIGEN_COVERAGE_AND_HINDUSTANI_SLICE_20260630T183821Z.json",
    "logs/R3_FULL_REGION_EIGEN_COVERAGE_AND_HINDUSTANI_SLICE_20260630T183821Z.md",
    "logs/R3_FULL_REGION_EIGEN_COVERAGE_AND_HINDUSTANI_SLICE_VALIDATION_20260630T183821Z.json",
    "logs/R3_FULL_REGION_EIGEN_COVERAGE_AND_HINDUSTANI_SLICE_VALIDATION_20260630T183821Z.md",
    "translations/non_slavic/r3_full_region_eigen_coverage_and_hindustani_slice_20260630T183821Z/r3_full_region_eigen_coverage_and_hindustani_slice_20260630T183821Z.json",
    "logs/R3_DARI_NONPDF_EIGEN_RETRY_20260630T184039Z.json",
    "logs/R3_DARI_NONPDF_EIGEN_RETRY_20260630T184039Z.md",
    "logs/R3_DARI_NONPDF_EIGEN_RETRY_VALIDATION_20260630T184039Z.json",
    "logs/R3_DARI_NONPDF_EIGEN_RETRY_VALIDATION_20260630T184039Z.md",
    "translations/non_slavic/r3_dari_nonpdf_eigen_retry_20260630T184039Z/r3_dari_nonpdf_eigen_retry_20260630T184039Z.json",
    "logs/R9_AF05_SOUTH_SUDAN_EXTERNAL_PACKET_INGEST_20260630T183911Z.json",
    "logs/R9_AF05_SOUTH_SUDAN_EXTERNAL_PACKET_INGEST_20260630T183911Z.md",
    "logs/SPANISH_P13_SOURCE_NATIVE_PATCH_20260630.json",
    "logs/SPANISH_P13_SOURCE_NATIVE_PATCH_20260630.md",
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: validate_language_planning_checkpoint_20260630.py <zip>")
    zip_path = Path(sys.argv[1])
    sha_path = zip_path.with_suffix(zip_path.suffix + ".sha256")
    validation_path = zip_path.with_suffix(zip_path.suffix + ".validation.json")

    sha = sha256_file(zip_path)
    sha_text = sha_path.read_text(encoding="ascii").split()[0].upper()
    with zipfile.ZipFile(zip_path, "r") as zf:
        bad_file = zf.testzip()
        names = zf.namelist()
    required_present = {
        req: any(name.endswith(req) for name in names)
        for req in REQUIRED_SUBSTRINGS
    }
    builder_validation = json.loads(validation_path.read_text(encoding="utf-8"))
    result = {
        "zip": str(zip_path).replace("\\", "/"),
        "sha256": sha,
        "sha256_file_value": sha_text,
        "sha256_matches": sha == sha_text,
        "zip_test_bad_file": bad_file,
        "entry_count": len(names),
        "required_present": required_present,
        "builder_validation_overall_pass": builder_validation.get("overall_pass"),
        "builder_validation_required_missing": builder_validation.get("required_missing"),
        "builder_validation_credential_scan_hits": builder_validation.get("credential_scan_hits"),
        "overall_pass": (
            sha == sha_text
            and bad_file is None
            and all(required_present.values())
            and builder_validation.get("overall_pass") is True
            and not builder_validation.get("required_missing")
            and not builder_validation.get("credential_scan_hits")
        ),
    }
    out_path = zip_path.with_suffix(zip_path.suffix + ".independent_validation.json")
    out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=True, indent=2))
    if not result["overall_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

import hashlib
import json
import re
import zipfile
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOW = datetime.now(timezone.utc)
STAMP = NOW.strftime("%Y%m%dT%H%M%SZ")
PACKAGE_ID = f"Noether_LanguagePlanning_SourceEvidence_Checkpoint_{STAMP}"
OUT_DIR = ROOT / "packages"
ZIP_PATH = OUT_DIR / f"{PACKAGE_ID}.zip"
SHA_PATH = OUT_DIR / f"{PACKAGE_ID}.zip.sha256"
VALIDATION_PATH = OUT_DIR / f"{PACKAGE_ID}.zip.validation.json"

CREDENTIAL_PATTERNS = [
    re.compile(b"BEGIN " + b"OPENSSH " + b"PRIVATE KEY"),
    re.compile(b"BEGIN " + b"RSA " + b"PRIVATE KEY"),
    re.compile(b"BEGIN " + b"DSA " + b"PRIVATE KEY"),
    re.compile(b"BEGIN " + b"EC " + b"PRIVATE KEY"),
    re.compile(b"github_" + b"pat_" + rb"[A-Za-z0-9_]{20,}"),
    re.compile(b"gh" + b"p_" + rb"[A-Za-z0-9_]{20,}"),
]

REQUIRED_RELATIVE_FILES = [
    "README.md",
    ".codex/config.toml",
    "status.json",
    "MANIFEST_SUMMARY.json",
    "MANIFEST_FILES.csv",
    "logs/GLOBAL_LANGUAGE_COMPLETION_AND_EDUCATIONAL_TRANSLATION_LANE_20260628.json",
    "logs/GLOBAL_LANGUAGE_COMPLETION_AND_EDUCATIONAL_TRANSLATION_LANE_20260628.md",
    "logs/PUBLICATION_AI_SEMICONSTRUCTED_LANGUAGE_RESEARCH_AGENDA_20260628.json",
    "logs/PUBLICATION_AI_SEMICONSTRUCTED_LANGUAGE_RESEARCH_AGENDA_20260628.md",
    "logs/INTERLANGUAGE_METHODOLOGY_AND_OPEN_SOURCE_EDUCATION_NOTE_20260628.json",
    "logs/INTERLANGUAGE_METHODOLOGY_AND_OPEN_SOURCE_EDUCATION_NOTE_20260628.md",
    "logs/INTERLANGUAGE_CANDIDATE_MATRIX_20260628.json",
    "logs/INTERLANGUAGE_CANDIDATE_MATRIX_20260628.md",
    "logs/INTERLANGUAGE_PUBLICATION_SECTION_DRAFT_20260628.md",
    "logs/INTERLANGUAGE_CANDIDATE_MATRIX_20260628T213951Z_WORLD_FAMILY_CONSTRUCTION.json",
    "logs/INTERLANGUAGE_CANDIDATE_MATRIX_20260628T213951Z_WORLD_FAMILY_CONSTRUCTION.md",
    "logs/INTERLANGUAGE_PUBLICATION_SECTION_DRAFT_20260628T213951Z_WORLD_FAMILY_CONSTRUCTION.md",
    "logs/WORLD_FAMILY_INTERLANGUAGE_COORDINATION_INDEX_20260628T214958Z.json",
    "logs/WORLD_FAMILY_INTERLANGUAGE_COORDINATION_INDEX_20260628T214958Z.md",
    "logs/WORLD_FAMILY_TECHNICAL_BRIDGE_ACTIONABLE_ROADMAP_20260628T215240Z.json",
    "logs/WORLD_FAMILY_TECHNICAL_BRIDGE_ACTIONABLE_ROADMAP_20260628T215240Z.md",
    "logs/WORLD_FAMILY_MISSING_REGION_GAP_AUDIT_20260628T215240Z.json",
    "logs/WORLD_FAMILY_MISSING_REGION_GAP_AUDIT_20260628T215240Z.md",
    "logs/WORLD_FAMILY_COVERAGE_CLOSURE_AUDIT_20260629T015305Z.json",
    "logs/WORLD_FAMILY_COVERAGE_CLOSURE_AUDIT_20260629T015305Z.md",
    "logs/WORLD_FAMILY_LEAST_SERVED_READER_LEGIBILITY_POLICY_20260629T015305Z.json",
    "logs/WORLD_FAMILY_LEAST_SERVED_READER_LEGIBILITY_POLICY_20260629T015305Z.md",
    "logs/WORLD_FAMILY_OPTIMAL_ACCESS_RESEARCH_NOTE_20260629T020750Z.json",
    "logs/WORLD_FAMILY_OPTIMAL_ACCESS_RESEARCH_NOTE_20260629T020750Z.md",
    "logs/WORLD_FAMILY_BRIDGE_REGISTER_CONSTRUCTION_TARGETS_20260628T221253Z.json",
    "logs/WORLD_FAMILY_BRIDGE_REGISTER_CONSTRUCTION_TARGETS_20260628T221253Z.md",
    "logs/WORLD_FAMILY_PARALLEL_HANDOFF_PROMPTS_20260628T215810Z.json",
    "logs/WORLD_FAMILY_PARALLEL_HANDOFF_PROMPTS_20260628T215810Z.md",
    "logs/WORLD_FAMILY_BRIDGE_LANE_STATUS_DASHBOARD_20260628T215810Z.json",
    "logs/WORLD_FAMILY_BRIDGE_LANE_STATUS_DASHBOARD_20260628T215810Z.md",
    "logs/WORLD_FAMILY_GOAL_COMPLETION_AUDIT_20260628T220603Z.json",
    "logs/WORLD_FAMILY_GOAL_COMPLETION_AUDIT_20260628T220603Z.md",
    "logs/WORLD_FAMILY_LIVE_DISPATCH_TRACKER_20260628T220603Z.json",
    "logs/WORLD_FAMILY_LIVE_DISPATCH_TRACKER_20260628T220603Z.md",
    "logs/ARABIC_SCRIPT_NON_ERASURE_GUARDRAIL_20260629.json",
    "logs/ARABIC_SCRIPT_NON_ERASURE_GUARDRAIL_20260629.md",
    "logs/PAN_ROMANCE_TECHNICAL_BRIDGE_CONSTRUCTION_DECISIONS_20260628T221717Z.json",
    "logs/PAN_ROMANCE_TECHNICAL_BRIDGE_CONSTRUCTION_DECISIONS_20260628T221717Z.md",
    "logs/CONTROLLED_ARABIC_TECHNICAL_REGISTER_DECISIONS_20260628T222119Z.json",
    "logs/CONTROLLED_ARABIC_TECHNICAL_REGISTER_DECISIONS_20260628T222119Z.md",
    "logs/CONTROLLED_ARABIC_NATIVE_MATH_REGISTER_SHELF_20260628T232000Z.json",
    "logs/CONTROLLED_ARABIC_NATIVE_MATH_REGISTER_SHELF_20260628T232000Z.md",
    "logs/CONTROLLED_ARABIC_60_TERM_SPINE_20260629T021500Z.json",
    "logs/CONTROLLED_ARABIC_60_TERM_SPINE_20260629T021500Z.md",
    "logs/CONTROLLED_ARABIC_INVARIANT_THEORY_EVIDENCE_AND_REVIEW_PLAN_20260630T054955Z.json",
    "logs/CONTROLLED_ARABIC_INVARIANT_THEORY_EVIDENCE_AND_REVIEW_PLAN_20260630T054955Z.md",
    "logs/CONTROLLED_ARABIC_INVARIANT_THEORY_SPECIALIST_SOURCE_RETRY_20260630T060636Z.json",
    "logs/CONTROLLED_ARABIC_INVARIANT_THEORY_SPECIALIST_SOURCE_RETRY_20260630T060636Z.md",
    "logs/CONTROLLED_ARABIC_INVARIANT_REVIEWER_TERM_PROPOSAL_20260630T060636Z.json",
    "logs/CONTROLLED_ARABIC_INVARIANT_REVIEWER_TERM_PROPOSAL_20260630T060636Z.md",
    "logs/CONTROLLED_ARABIC_COVARIANT_BINARY_FORM_SOURCE_RETRY_20260630T063033Z.json",
    "logs/CONTROLLED_ARABIC_COVARIANT_BINARY_FORM_SOURCE_RETRY_20260630T063033Z.md",
    "logs/CONTROLLED_ARABIC_COVARIANT_BINARY_FORM_REVIEWER_ADDENDUM_20260630T063033Z.json",
    "logs/CONTROLLED_ARABIC_COVARIANT_BINARY_FORM_REVIEWER_ADDENDUM_20260630T063033Z.md",
    "logs/CONTROLLED_ARABIC_ABSTRACT_ALGEBRA_SOURCE_RETRY_20260630T092000Z.json",
    "logs/CONTROLLED_ARABIC_ABSTRACT_ALGEBRA_SOURCE_RETRY_20260630T092000Z.md",
    "logs/CONTROLLED_ARABIC_INVARIANT_REGISTER_SWEEP_20260630T180627Z.json",
    "logs/CONTROLLED_ARABIC_INVARIANT_REGISTER_SWEEP_20260630T180627Z.md",
    "logs/ARABIC_PERSIANATE_EVIDENCE_SPLIT_INDEX_20260629T013531Z.json",
    "logs/ARABIC_PERSIANATE_EVIDENCE_SPLIT_INDEX_20260629T013531Z.md",
    "logs/CONTROLLED_ARABIC_EVIDENCE_SPLIT_20260629T013531Z.json",
    "logs/CONTROLLED_ARABIC_EVIDENCE_SPLIT_20260629T013531Z.md",
    "logs/PERSIANATE_FARSI_DARI_TAJIK_EVIDENCE_SPLIT_20260629T013531Z.json",
    "logs/PERSIANATE_FARSI_DARI_TAJIK_EVIDENCE_SPLIT_20260629T013531Z.md",
    "logs/R3_DARI_AFGHAN_PERSIAN_INVARIANT_PDF_LEAD_CAPTURE_20260630T064253Z.json",
    "logs/R3_DARI_AFGHAN_PERSIAN_INVARIANT_PDF_LEAD_CAPTURE_20260630T064253Z.md",
    "logs/DARI_AFGHAN_MATH_PDF_FALLBACK_SHELF_20260630T182039Z.json",
    "logs/DARI_AFGHAN_MATH_PDF_FALLBACK_SHELF_20260630T182039Z.md",
    "logs/TAJIK_CYRILLIC_MATH_SOURCE_RETRY_20260630T104800Z.json",
    "logs/TAJIK_CYRILLIC_MATH_SOURCE_RETRY_20260630T104800Z.md",
    "logs/ARABIC_SCRIPT_NEIGHBOR_INFRASTRUCTURE_EVIDENCE_SPLIT_20260629T013531Z.json",
    "logs/ARABIC_SCRIPT_NEIGHBOR_INFRASTRUCTURE_EVIDENCE_SPLIT_20260629T013531Z.md",
    "logs/PERSIANATE_SCRIPT_AND_STANDARD_POLICY_20260628T222119Z.json",
    "logs/PERSIANATE_SCRIPT_AND_STANDARD_POLICY_20260628T222119Z.md",
    "logs/NON_SLAVIC_ARXIV_REFERENCE_SHELF_20260628.json",
    "logs/NON_SLAVIC_ARXIV_REFERENCE_SHELF_20260628.md",
    "logs/CHINESE_JAPANESE_PERSIAN_ARABIC_FALLBACK_SOURCE_SHELF_20260628.json",
    "logs/CHINESE_JAPANESE_PERSIAN_ARABIC_FALLBACK_SOURCE_SHELF_20260628.md",
    "logs/CHINESE_JAPANESE_NATIVE_MATH_REGISTER_SHELF_20260628.json",
    "logs/CHINESE_JAPANESE_NATIVE_MATH_REGISTER_SHELF_20260628.md",
    "logs/CHINESE_JAPANESE_HARDTERM_SOURCE_RETRY_20260630T080000Z.json",
    "logs/CHINESE_JAPANESE_HARDTERM_SOURCE_RETRY_20260630T080000Z.md",
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
    "logs/FRENCH_SPANISH_NATIVE_MATH_REGISTER_SHELF_20260628.json",
    "logs/FRENCH_SPANISH_NATIVE_MATH_REGISTER_SHELF_20260628.md",
    "logs/FRENCH_SPANISH_LATEX_SOURCE_CORPUS_20260628.json",
    "logs/FRENCH_SPANISH_LATEX_SOURCE_CORPUS_20260628.txt",
    "logs/FRENCH_SPANISH_LATEX_SOURCE_CORPUS_EXPANDED_20260628.json",
    "logs/FRENCH_SPANISH_LATEX_SOURCE_CORPUS_EXPANDED_20260628.txt",
    "logs/PAN_ROMANCE_NATIVE_MATH_REGISTER_SOURCE_SCOPE_20260629.json",
    "logs/PAN_ROMANCE_NATIVE_MATH_REGISTER_SOURCE_SCOPE_20260629.md",
    "logs/PAN_ROMANCE_CORE_CONTROL_SOURCE_CONSOLIDATION_20260630T073020Z.json",
    "logs/PAN_ROMANCE_CORE_CONTROL_SOURCE_CONSOLIDATION_20260630T073020Z.md",
    "logs/PAN_ROMANCE_60_TERM_SPINE_DRAFT_20260629.json",
    "logs/PAN_ROMANCE_60_TERM_SPINE_DRAFT_20260629.md",
    "logs/PAN_ROMANCE_FALLBACK_TERM_HIT_REVIEW_20260629.json",
    "logs/PAN_ROMANCE_FALLBACK_TERM_HIT_REVIEW_20260629.md",
    "logs/PAN_ROMANCE_FAMILY_COMPLETENESS_SOURCE_BACKLOG_20260629.json",
    "logs/PAN_ROMANCE_FAMILY_COMPLETENESS_SOURCE_BACKLOG_20260629.md",
    "logs/PAN_ROMANCE_FAMILY_SOURCE_MATRIX_20260629.json",
    "logs/PAN_ROMANCE_FAMILY_SOURCE_MATRIX_20260629.md",
    "logs/PAN_ROMANCE_FAMILY_SOURCE_PACKET_MANIFEST_20260629.json",
    "logs/PAN_ROMANCE_FAMILY_SOURCE_PACKET_MANIFEST_20260629.md",
    "logs/PAN_ROMANCE_OPTIMAL_ACCESS_HEURISTIC_INTEGRATION_20260629.json",
    "logs/PAN_ROMANCE_OPTIMAL_ACCESS_HEURISTIC_INTEGRATION_20260629.md",
    "logs/PAN_ROMANCE_PROMOTED_INTERLANGUAGE_MATH_EXAMPLES_20260629.json",
    "logs/PAN_ROMANCE_PROMOTED_INTERLANGUAGE_MATH_EXAMPLES_20260629.md",
    "logs/PAN_ROMANCE_PROMOTED_MATH_LITERATURE_SCOUT_20260629.json",
    "logs/PAN_ROMANCE_PROMOTED_MATH_LITERATURE_SCOUT_20260629.md",
    "logs/PAN_ROMANCE_PROMOTED_MATH_LITERATURE_TERM_HITS_20260629.json",
    "logs/PAN_ROMANCE_PROMOTED_MATH_LITERATURE_TERM_HITS_20260629.md",
    "logs/PAN_ROMANCE_PROMOTED_REGISTER_60_TERM_SOURCE_HIT_TABLE_20260629.json",
    "logs/PAN_ROMANCE_PROMOTED_REGISTER_60_TERM_SOURCE_HIT_TABLE_20260629.md",
    "logs/PAN_ROMANCE_PROMOTED_REGISTER_OCR_RETRY_20260629.json",
    "logs/PAN_ROMANCE_PROMOTED_REGISTER_OCR_RETRY_20260629.md",
    "logs/PAN_ROMANCE_PROMOTED_REGISTER_ROW_LEVEL_SOURCE_EXAMPLES_20260629.json",
    "logs/PAN_ROMANCE_PROMOTED_REGISTER_ROW_LEVEL_SOURCE_EXAMPLES_20260629.md",
    "logs/PAN_ROMANCE_PROMOTED_REGISTER_SOURCE_RETRY_20260629.json",
    "logs/PAN_ROMANCE_PROMOTED_REGISTER_SOURCE_RETRY_20260629.md",
    "logs/PAN_ROMANCE_PROMOTED_SPECIAL_REGISTER_SOURCE_EXAMPLES_20260629.json",
    "logs/PAN_ROMANCE_PROMOTED_SPECIAL_REGISTER_SOURCE_EXAMPLES_20260629.md",
    "logs/PAN_ROMANCE_HIGH_REGISTER_MATH_LITERATURE_EVIDENCE_INTEGRATION_20260629.json",
    "logs/PAN_ROMANCE_HIGH_REGISTER_MATH_LITERATURE_EVIDENCE_INTEGRATION_20260629.md",
    "logs/PAN_ROMANCE_INTERLANGUAGE_AND_SOUTH_AMERICA_BREADTH_RETRY_20260629.json",
    "logs/PAN_ROMANCE_INTERLANGUAGE_AND_SOUTH_AMERICA_BREADTH_RETRY_20260629.md",
    "logs/PAN_ROMANCE_ROMANICA_NEOLATINO_MATH_LITERATURE_RETRY_20260629.json",
    "logs/PAN_ROMANCE_ROMANICA_NEOLATINO_MATH_LITERATURE_RETRY_20260629.md",
    "logs/PAN_ROMANCE_SECONDARY_BRANCH_SOURCE_INTAKE_20260629.json",
    "logs/PAN_ROMANCE_SECONDARY_BRANCH_SOURCE_INTAKE_20260629.md",
    "logs/PAN_ROMANCE_T56_FRENCH_TIER0_CLOSURE_20260629.json",
    "logs/PAN_ROMANCE_T56_FRENCH_TIER0_CLOSURE_20260629.md",
    "logs/FRENCH_SPANISH_TRANSLATION_LANE_WORKLOG_20260629.json",
    "logs/FRENCH_SPANISH_TRANSLATION_LANE_WORKLOG_20260629.md",
    "logs/FRENCH_SPANISH_INVARIANT_HARDTERM_EVIDENCE_20260630T065920Z.json",
    "logs/FRENCH_SPANISH_INVARIANT_HARDTERM_EVIDENCE_20260630T065920Z.md",
    "logs/SPANISH_COVARIANT_HARDTERM_RETRY_20260630T071100Z.json",
    "logs/SPANISH_COVARIANT_HARDTERM_RETRY_20260630T071100Z.md",
    "logs/SPANISH_COVARIANT_TEX_SOURCE_RETRY_20260630T072204Z.json",
    "logs/SPANISH_COVARIANT_TEX_SOURCE_RETRY_20260630T072204Z.md",
    "logs/SPANISH_COVARIANT_TEX_BROADER_RETRY_20260630T083000Z.json",
    "logs/SPANISH_COVARIANT_TEX_BROADER_RETRY_20260630T083000Z.md",
    "logs/SPANISH_P40_INTRO_SOURCE_RESYNC_20260629.json",
    "logs/SPANISH_P40_INTRO_SOURCE_RESYNC_20260629.md",
    "logs/PERSIAN_ARABIC_NATIVE_MATH_REGISTER_SHELF_20260628T210457Z.json",
    "logs/PERSIAN_ARABIC_NATIVE_MATH_REGISTER_SHELF_20260628T210457Z.md",
    "logs/PERSIAN_ARABIC_NATIVE_MATH_REGISTER_TEX_SOURCE_FIRST_SHELF_20260628T211612Z.json",
    "logs/PERSIAN_ARABIC_NATIVE_MATH_REGISTER_TEX_SOURCE_FIRST_SHELF_20260628T211612Z.md",
    "logs/PERSIAN_ARABIC_DARI_TAJIK_DEEP_TEX_SOURCE_REGISTER_SHELF_20260628T213737Z.json",
    "logs/PERSIAN_ARABIC_DARI_TAJIK_DEEP_TEX_SOURCE_REGISTER_SHELF_20260628T213737Z.md",
    "logs/CHINESE_JAPANESE_TRANSLATION_LANE_UPDATE_AGENDA_20260628.json",
    "logs/CHINESE_JAPANESE_TRANSLATION_LANE_UPDATE_AGENDA_20260628.md",
    "logs/CHINESE_JAPANESE_TRANSLATION_LANE_STATUS_AUDIT_20260628.json",
    "logs/CHINESE_JAPANESE_TRANSLATION_LANE_STATUS_AUDIT_20260628.md",
    "logs/CHINESE_JAPANESE_COMPLETION_METHODOLOGY_20260629.json",
    "logs/CHINESE_JAPANESE_COMPLETION_METHODOLOGY_20260629.md",
    "logs/CHINESE_JAPANESE_COMPLETION_INVENTORY_20260629.json",
    "logs/CHINESE_JAPANESE_COMPLETION_INVENTORY_20260629.md",
    "logs/CHINESE_JAPANESE_COMPLETION_WORKLOG_20260629.md",
    "logs/SIMPLIFIED_CHINESE_PAPER20_RENDER_VALIDATION_20260629.json",
    "logs/SIMPLIFIED_CHINESE_PAPER20_RENDER_VALIDATION_20260629.md",
    "logs/SIMPLIFIED_CHINESE_PAPER21_RENDER_VALIDATION_20260629.json",
    "logs/SIMPLIFIED_CHINESE_PAPER21_RENDER_VALIDATION_20260629.md",
    "logs/JAPANESE_P19S04_SOURCE_CORRECTIONS_APPLIED_20260629.json",
    "logs/JAPANESE_P19S04_SOURCE_CORRECTIONS_APPLIED_20260629.md",
    "logs/JAPANESE_P19S04_P19S06_COMBINED_RENDER_VALIDATION_20260629.json",
    "logs/JAPANESE_P19S04_P19S06_COMBINED_RENDER_VALIDATION_20260629.md",
    "logs/EAST_SOUTHEAST_ASIA_NATIVE_MATH_REGISTER_SHELF_20260628.json",
    "logs/EAST_SOUTHEAST_ASIA_NATIVE_MATH_REGISTER_SHELF_20260628.md",
    "logs/JAPANESE_P19S06_TAU_CORRECTION_APPLIED_20260629.json",
    "logs/JAPANESE_P19S06_TAU_CORRECTION_APPLIED_20260629.md",
    "logs/JAPANESE_P19S06_TAU_CORRECTION_RENDERED_20260629.json",
    "logs/JAPANESE_P19S06_TAU_CORRECTION_RENDERED_20260629.md",
    "logs/SOUTH_AMERICAN_ADJACENT_LANGUAGE_MATH_TEX_AUDIT_20260628.json",
    "logs/SOUTH_AMERICAN_ADJACENT_LANGUAGE_MATH_TEX_AUDIT_20260628.txt",
    "logs/ASIA_WIDE_TEX_SOURCE_MATH_REGISTER_SHELF_20260628T215200Z.json",
    "logs/ASIA_WIDE_TEX_SOURCE_MATH_REGISTER_SHELF_20260628T215200Z.md",
    "logs/REGIONAL_LANGUAGE_EVIDENCE_COORDINATION_LOGBOOK_20260628.md",
    "sources/zenodo_updates/20260628_record20836874/zenodo_20836874_latest_check_summary_20260628T215857Z.json",
    "sources/zenodo_updates/20260628_record20836874/zenodo_20836874_api_latest_20260628T215857Z.json",
    "sources/zenodo_updates/20260628_record20836874/zenodo_20836874_api_latest_20260628T_current.json",
    "sources/zenodo_updates/20260629_record20836874/zenodo_20836874_api_latest_20260629T_current.json",
    "logs/NON_SLAVIC_EXISTING_TRANSLATION_INVENTORY_20260628.json",
    "logs/NON_SLAVIC_EXISTING_TRANSLATION_INVENTORY_20260628.md",
    "logs/NON_SLAVIC_EXISTING_TRANSLATION_ARTIFACT_IMPORT_20260628.json",
    "logs/NON_SLAVIC_EXISTING_TRANSLATION_ARTIFACT_IMPORT_20260628.md",
    "logs/NON_SLAVIC_IMPORTED_ARTIFACT_AUDIT_QUEUE_20260628.json",
    "logs/NON_SLAVIC_IMPORTED_ARTIFACT_AUDIT_QUEUE_20260628.md",
    "logs/NON_SLAVIC_CROSS_LANE_SOURCE_CORRECTION_QUEUE_20260628.json",
    "logs/NON_SLAVIC_CROSS_LANE_SOURCE_CORRECTION_QUEUE_20260628.md",
    "logs/NON_SLAVIC_PDF_VISUAL_CONTACT_SHEETS_LATEST.json",
    "logs/NON_SLAVIC_PDF_VISUAL_CONTACT_SHEETS_LATEST.md",
    "logs/NON_SLAVIC_VISUAL_INSPECTION_SUMMARY_20260628.json",
    "logs/NON_SLAVIC_VISUAL_INSPECTION_SUMMARY_20260628.md",
    "logs/NON_SLAVIC_TERMINOLOGY_RATIONALE_SEED_LEDGER_20260628.json",
    "logs/NON_SLAVIC_TERMINOLOGY_RATIONALE_SEED_LEDGER_20260628.md",
    "logs/NON_SLAVIC_TARGETED_GAP_SOURCE_INTEGRATION_20260628.json",
    "logs/NON_SLAVIC_TARGETED_GAP_SOURCE_INTEGRATION_20260628.md",
    "logs/NON_SLAVIC_TARGETED_GAP_EXTERNAL_EVIDENCE_LATEST.json",
    "logs/NON_SLAVIC_TARGETED_GAP_EXTERNAL_EVIDENCE_LATEST.md",
    "logs/NON_SLAVIC_TARGETED_GAP_SOURCE_INTEGRATION_SUPPLEMENT_20260629.json",
    "logs/NON_SLAVIC_TARGETED_GAP_SOURCE_INTEGRATION_SUPPLEMENT_20260629.md",
    "logs/PARALLEL_CODEX_OTHER_SESSION_COORDINATION_CHECK_20260629.json",
    "logs/PARALLEL_CODEX_OTHER_SESSION_COORDINATION_CHECK_20260629.md",
    "logs/PARALLEL_CODEX_LOCAL_DROP_WORLD_FAMILY_COORDINATION_20260629.json",
    "logs/PARALLEL_CODEX_LOCAL_DROP_WORLD_FAMILY_COORDINATION_20260629.md",
    "logs/PARALLEL_CODEX_LOCAL_DROP_CHINESE_JAPANESE_20260629.json",
    "logs/PARALLEL_CODEX_LOCAL_DROP_CHINESE_JAPANESE_20260629.md",
    "logs/CODEX_LAPTOP_PERMISSION_BASELINE_20260630.md",
    "logs/PERMISSION_AND_WORKFLOW_INSTRUCTIONS_20260627.md",
    "logs/WORKFLOW_LOG.md",
    "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260628T230854Z.json",
    "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260628T230854Z.md",
    "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260630T055420Z.json",
    "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260630T055420Z.md",
    "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260630T063457Z.json",
    "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260630T063457Z.md",
    "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260630T074714Z.json",
    "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260630T074714Z.md",
    "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260630T175501Z.json",
    "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260630T175501Z.md",
    "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260630T181153Z.json",
    "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260630T181153Z.md",
    "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260630T184304Z.json",
    "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260630T184304Z.md",
    "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260630T213655Z.json",
    "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260630T213655Z.md",
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
    "sources/non_slavic_reference_corpus/20260630T214900Z_r7_lao_jica_math_source_capture/metadata/jica_lao_math_source_capture_audit_manifest_20260701T144500Z.json",
    "tmp/audit_r7_lao_jica_official_math_shelf_20260701.py",
    "tmp/build_r7_lao_jica_ocr_spotcheck_audit_20260701.py",
    "sources/non_slavic_reference_corpus/20260630T214900Z_r7_lao_jica_math_source_capture/ocr_spotcheck/grade5_textbook_pages_001_003/page-001.png",
    "sources/non_slavic_reference_corpus/20260630T214900Z_r7_lao_jica_math_source_capture/ocr_spotcheck/grade5_textbook_pages_001_003/page-001.txt",
    "logs/PERMISSION_CONFIG_DOCUMENTED_REWRITE_20260630T214000Z.md",
    "logs/PERMISSION_CONFIG_DOCUMENTED_REASSERTION_20260630T215802Z.md",
    "logs/DEPENDENCY_REPAIR_20260701.md",
    "tmp/dependency_smoke_test_20260701.tex",
    "tmp/dependency_smoke_test_20260701/dependency_smoke_test_20260701.pdf",
    "tmp/dependency_smoke_test_20260701_rerun/dependency_smoke_test_20260701.pdf",
    "sources/non_slavic_reference_corpus/20260629T061500Z_r7_philippine_tai_hmong_austroasiatic_source_status/copied_prior_evidence/tai_kadai/lao_mathematics_teacher_manual.pdf",
    "sources/non_slavic_reference_corpus/20260629T061500Z_r7_philippine_tai_hmong_austroasiatic_source_status/extracted_text/lao_mathematics_teacher_manual.txt",
    "logs/PARALLEL_CODEX_LOCAL_DROP_NON_SLAVIC_SOURCE_STATUS_20260628.json",
    "logs/PARALLEL_CODEX_LOCAL_DROP_NON_SLAVIC_SOURCE_STATUS_20260628.md",
    "logs/SLAVIC_MAINTENANCE_WATCHDOG_20260628.json",
    "logs/SLAVIC_MAINTENANCE_WATCHDOG_20260628.md",
    "logs/PARALLEL_CODEX_HANDOFF_PROMPTS_20260628.json",
    "logs/PARALLEL_CODEX_HANDOFF_PROMPTS_20260628.md",
    "tmp/build_non_slavic_arxiv_reference_shelf_20260628.py",
    "tmp/build_non_slavic_pdf_visual_contact_sheets_20260628.py",
    "tmp/build_non_slavic_terminology_rationale_seed_ledger_20260628.py",
    "tmp/build_persian_arabic_native_math_register_shelf_20260628.py",
    "tmp/build_persian_arabic_tex_first_register_shelf_20260628.py",
    "tmp/build_deep_tex_source_register_shelf_20260628.py",
    "tmp/build_non_slavic_targeted_gap_source_integration_20260628.py",
    "tmp/build_targeted_gap_external_evidence_20260629.py",
    "tmp/build_french_spanish_invariant_hardterm_evidence_20260630.py",
    "tmp/update_french_spanish_invariant_hardterm_coordination_20260630.py",
    "tmp/build_spanish_covariant_hardterm_retry_20260630.py",
    "tmp/update_spanish_covariant_hardterm_retry_coordination_20260630.py",
    "tmp/build_spanish_covariant_tex_source_retry_20260630.py",
    "tmp/update_spanish_covariant_tex_source_retry_coordination_20260630.py",
    "tmp/build_spanish_covariant_tex_broader_retry_20260630.py",
    "tmp/update_spanish_covariant_tex_broader_retry_coordination_20260630.py",
    "tmp/build_tajik_cyrillic_math_source_retry_20260630.py",
    "tmp/update_tajik_cyrillic_source_retry_coordination_20260630.py",
    "tmp/build_pan_romance_core_control_consolidation_20260630.py",
    "tmp/update_pan_romance_core_control_consolidation_20260630.py",
    "tmp/french_spanish_native_math_register/build_romance_bridge_register_seed.py",
    "tmp/build_dari_afghan_persian_invariant_pdf_lead_capture_20260630.py",
    "tmp/update_dari_afghan_persian_pdf_lead_capture_coordination_20260630.py",
    "tmp/build_dari_afghan_math_pdf_fallback_shelf_20260630.py",
    "tmp/update_dari_afghan_math_pdf_fallback_shelf_coordination_20260630.py",
    "tmp/build_controlled_arabic_register_shelf_20260629.py",
    "tmp/build_controlled_arabic_60_term_spine_20260629.py",
    "tmp/build_controlled_arabic_invariant_gap_review_20260630.py",
    "tmp/update_controlled_arabic_invariant_gap_coordination_20260630.py",
    "tmp/build_controlled_arabic_invariant_specialist_retry_and_proposal_20260630.py",
    "tmp/update_controlled_arabic_invariant_specialist_retry_coordination_20260630.py",
    "tmp/build_controlled_arabic_covariant_binary_form_retry_20260630.py",
    "tmp/update_controlled_arabic_covariant_binary_form_coordination_20260630.py",
    "tmp/build_controlled_arabic_abstract_algebra_source_retry_20260630.py",
    "tmp/update_controlled_arabic_abstract_algebra_source_retry_coordination_20260630.py",
    "tmp/build_controlled_arabic_invariant_register_sweep_20260630.py",
    "tmp/update_controlled_arabic_invariant_register_sweep_coordination_20260630.py",
    "tmp/build_other_session_coordination_check_20260629.py",
    "tmp/rebuild_chinese_japanese_source_shelf_20260628.py",
    "tmp/build_chinese_japanese_hardterm_source_retry_20260630.py",
    "tmp/update_chinese_japanese_hardterm_source_retry_coordination_20260630.py",
    "tmp/capture_japanese_representation_exact_search_20260630.py",
    "tmp/build_japanese_representation_exact_source_retry_20260630.py",
    "tmp/update_japanese_representation_exact_source_retry_coordination_20260630.py",
    "tmp/render_japanese_p19s06_tau_with_tectonic_20260629.py",
    "tmp/french_spanish_native_math_register/build_south_american_adjacent_audit.py",
    "tmp/build_asia_wide_tex_source_register_shelf_20260628.py",
    "tmp/discover_regional_math_repos_20260628.py",
    "tmp/update_zenodo_and_coordination_status_20260628.py",
    "tmp/check_zenodo_20836874_latest_20260630_languageplanning.py",
    "tmp/import_non_slavic_existing_translation_artifacts_20260628.py",
    "tmp/validate_language_planning_checkpoint_20260630.py",
    "tmp/package_language_planning_checkpoint_20260628.py",
]


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT.resolve()).as_posix()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def scan_credentials(paths: list[Path]) -> list[str]:
    hits = []
    for path in paths:
        data = path.read_bytes()
        for pattern in CREDENTIAL_PATTERNS:
            if pattern.search(data):
                hits.append(rel(path))
                break
    return hits


def add_tree(
    files: set[Path],
    root: Path,
    *,
    suffixes: set[str] | None = None,
    exclude_parts: set[str] | None = None,
    max_bytes: int | None = None,
) -> None:
    if not root.exists():
        return
    exclude_parts = exclude_parts or set()
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if exclude_parts and any(part in exclude_parts for part in path.parts):
            continue
        if suffixes is not None and path.suffix.lower() not in suffixes:
            continue
        if max_bytes is not None and path.stat().st_size > max_bytes:
            continue
        files.add(path)


def collect_files() -> list[Path]:
    files = {ROOT / relative for relative in REQUIRED_RELATIVE_FILES}
    add_tree(files, ROOT / "logs", suffixes={".md", ".json", ".txt", ".csv"})
    add_tree(files, ROOT / "tmp", suffixes={".py"})
    add_tree(files, ROOT / "review_bundles", suffixes={".zip", ".json", ".pdf", ".png", ".tex", ".csv", ".md", ".sha256"})
    add_tree(
        files,
        ROOT / "renders" / "non_slavic",
        suffixes={".pdf", ".tex", ".log", ".json", ".md", ".txt", ".conf", ".sha256"},
        exclude_parts={"tmp_pages", "pages", "page_images", "raster_pages"},
    )
    source_root = ROOT / "sources/non_slavic_reference_corpus/20260628_arxiv_native_math"
    if source_root.exists():
        for path in source_root.rglob("*"):
            if path.is_file():
                files.add(path)
    fallback_root = ROOT / "sources/non_slavic_reference_corpus/20260628_fallback_native_math"
    if fallback_root.exists():
        for path in fallback_root.rglob("*"):
            if path.is_file():
                files.add(path)
    additional_source_roots = [
        ROOT / "sources/non_slavic_reference_corpus/20260628_chinese_japanese_native_math",
        ROOT / "sources/non_slavic_reference_corpus/20260630T080000Z_chinese_japanese_hardterm_source_retry",
        ROOT / "sources/non_slavic_reference_corpus/20260630T081000Z_japanese_representation_exact_source_retry",
        ROOT / "sources/non_slavic_reference_corpus/20260628_french_spanish_native_math_register",
        ROOT / "sources/non_slavic_reference_corpus/20260630T065920Z_french_spanish_invariant_hardterm_evidence",
        ROOT / "sources/non_slavic_reference_corpus/20260630T071100Z_spanish_covariant_hardterm_retry",
        ROOT / "sources/non_slavic_reference_corpus/20260630T072204Z_spanish_covariant_tex_source_retry",
        ROOT / "sources/non_slavic_reference_corpus/20260630T083000Z_spanish_covariant_tex_broader_retry",
        ROOT / "sources/non_slavic_reference_corpus/20260628T210457Z_persian_arabic_native_math",
        ROOT / "sources/non_slavic_reference_corpus/20260628T211612Z_persian_arabic_tex_source_first",
        ROOT / "sources/non_slavic_reference_corpus/20260628T213737Z_deep_tex_source_register",
        ROOT / "sources/non_slavic_reference_corpus/20260630T064253Z_r3_dari_afghan_persian_invariant_pdf_lead_capture",
        ROOT / "sources/non_slavic_reference_corpus/20260630T182039Z_dari_afghan_math_pdf_fallback_shelf",
        ROOT / "sources/non_slavic_reference_corpus/20260630T104800Z_tajik_cyrillic_math_source_retry",
        ROOT / "sources/non_slavic_reference_corpus/20260628_south_american_adjacent_math_register",
        ROOT / "sources/non_slavic_reference_corpus/20260628T214313Z_east_southeast_asia_regional_math",
        ROOT / "sources/non_slavic_reference_corpus/20260628T215200Z_asia_wide_tex_source_register",
        ROOT / "sources/non_slavic_reference_corpus/20260629_targeted_gap_external_evidence",
        ROOT / "sources/non_slavic_reference_corpus/20260630T214900Z_r7_lao_jica_math_source_capture",
        ROOT / "sources/non_slavic_reference_corpus/20260628T232000Z_controlled_arabic_math_register",
        ROOT / "sources/non_slavic_reference_corpus/20260630T054955Z_controlled_arabic_invariant_theory_gap",
        ROOT / "sources/non_slavic_reference_corpus/20260630T060636Z_controlled_arabic_invariant_specialist_retry",
        ROOT / "sources/non_slavic_reference_corpus/20260630T063033Z_controlled_arabic_covariant_binary_form_retry",
        ROOT / "sources/non_slavic_reference_corpus/20260630T092000Z_controlled_arabic_abstract_algebra_source_retry",
        ROOT / "sources/non_slavic_reference_corpus/20260630T180627Z_controlled_arabic_invariant_register_sweep",
        ROOT / "sources/non_slavic_reference_corpus/20260702T013000Z_controlled_arabic_algebra_source_refresh",
        ROOT / "sources/non_slavic_reference_corpus/20260629T013531Z_arabic_persianate_evidence_split",
        ROOT / "sources/non_slavic_reference_corpus/20260629_pan_romance_math_register_candidates",
        ROOT / "sources/zenodo_updates/20260629_record20836874",
        ROOT / "sources/zenodo_updates/20260630_record20836874",
        ROOT / "sources/paper19",
        ROOT / "sources/paper20",
        ROOT / "sources/paper21",
        ROOT / "sources/paper40/source_fidelity",
        ROOT / "translations/non_slavic",
    ]
    for source_dir in additional_source_roots:
        if source_dir.exists():
            for path in source_dir.rglob("*"):
                if path.is_file():
                    files.add(path)
    import_root = ROOT / "sources/non_slavic_existing_translation_artifacts/zenodo_20836874_20260628"
    if import_root.exists():
        for path in import_root.rglob("*"):
            if path.is_file():
                files.add(path)
    visual = read_json("logs/NON_SLAVIC_PDF_VISUAL_CONTACT_SHEETS_LATEST.json")
    visual_root = ROOT / visual.get("output_root", "")
    if visual_root.exists():
        for path in visual_root.rglob("*"):
            if path.is_file() and "tmp_pages" not in path.parts:
                files.add(path)
    japanese_render_root = ROOT / "renders/non_slavic/japanese_p19s06_tau_correction_20260629"
    if japanese_render_root.exists():
        for path in japanese_render_root.rglob("*"):
            if path.is_file():
                files.add(path)
    additional_render_roots = [
        ROOT / "renders/non_slavic/simplified_chinese_paper20_source_fidelity_20260629",
        ROOT / "renders/non_slavic/simplified_chinese_paper21_source_fidelity_20260629",
        ROOT / "renders/non_slavic/japanese_p19s04_p19s06_combined_validation_20260629",
        ROOT / "renders/non_slavic_existing_translation_artifacts/spanish_ra10_source_patch_20260629",
        ROOT / "renders/non_slavic_existing_translation_artifacts/spanish_ra10_p40_intro_resync_20260629",
        ROOT / "renders/paper19/section07/french/v001",
        ROOT / "renders/non_slavic_existing_translation_artifacts/french_p19s07_20260629",
    ]
    for render_dir in additional_render_roots:
        if render_dir.exists():
            for path in render_dir.rglob("*"):
                if path.is_file():
                    files.add(path)
    for pattern in [
        "logs/NON_SLAVIC_TARGETED_GAP_EXTERNAL_EVIDENCE_*.json",
        "logs/NON_SLAVIC_TARGETED_GAP_EXTERNAL_EVIDENCE_*.md",
    ]:
        for path in ROOT.glob(pattern):
            if path.is_file():
                files.add(path)
    return sorted(path.resolve() for path in files if path.is_file())


def read_json(relative: str):
    return json.loads((ROOT / relative).read_text(encoding="utf-8-sig"))


def write_json(relative: str, data) -> None:
    (ROOT / relative).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def summarize_inventory(inventory: dict) -> dict:
    lanes = inventory.get("lanes", [])
    if not isinstance(lanes, list):
        lanes = []
    classification_counts: dict[str, int] = {}
    corpus_first_lanes = []
    upgrade_lanes = []
    for lane in lanes:
        if not isinstance(lane, dict):
            continue
        classification = lane.get("classification") or "unclassified"
        classification_counts[classification] = classification_counts.get(classification, 0) + 1
        next_action = str(lane.get("next_action") or "")
        language_id = lane.get("language_id")
        if "corpus" in next_action.lower() and language_id:
            corpus_first_lanes.append(language_id)
        if classification in {"cumulative partial", "rendered partial"} and language_id:
            upgrade_lanes.append(language_id)
    return {
        "lane_count": len(lanes),
        "overall_conclusion": inventory.get("overall_conclusion"),
        "classification_counts": classification_counts,
        "corpus_first_lanes": corpus_first_lanes,
        "upgrade_or_audit_lanes": upgrade_lanes,
    }


def update_status(package_record: dict, validation: dict) -> None:
    shelf = read_json("logs/NON_SLAVIC_ARXIV_REFERENCE_SHELF_20260628.json")
    fallback = read_json("logs/CHINESE_JAPANESE_PERSIAN_ARABIC_FALLBACK_SOURCE_SHELF_20260628.json")
    chinese_japanese_shelf = read_json("logs/CHINESE_JAPANESE_NATIVE_MATH_REGISTER_SHELF_20260628.json")
    chinese_japanese_hardterm_source_retry = read_json(
        "logs/CHINESE_JAPANESE_HARDTERM_SOURCE_RETRY_20260630T080000Z.json"
    )
    japanese_representation_exact_source_retry = read_json(
        "logs/JAPANESE_REPRESENTATION_EXACT_SOURCE_RETRY_20260630T081000Z.json"
    )
    french_spanish_shelf = read_json("logs/FRENCH_SPANISH_NATIVE_MATH_REGISTER_SHELF_20260628.json")
    french_spanish_latex = read_json("logs/FRENCH_SPANISH_LATEX_SOURCE_CORPUS_20260628.json")
    french_spanish_latex_expanded = read_json("logs/FRENCH_SPANISH_LATEX_SOURCE_CORPUS_EXPANDED_20260628.json")
    pan_romance_source_scope = read_json("logs/PAN_ROMANCE_NATIVE_MATH_REGISTER_SOURCE_SCOPE_20260629.json")
    pan_romance_core_consolidation = read_json(
        "logs/PAN_ROMANCE_CORE_CONTROL_SOURCE_CONSOLIDATION_20260630T073020Z.json"
    )
    pan_romance_60_term_spine = read_json("logs/PAN_ROMANCE_60_TERM_SPINE_DRAFT_20260629.json")
    pan_romance_fallback_hit_review = read_json("logs/PAN_ROMANCE_FALLBACK_TERM_HIT_REVIEW_20260629.json")
    pan_romance_family_matrix = read_json("logs/PAN_ROMANCE_FAMILY_SOURCE_MATRIX_20260629.json")
    pan_romance_source_packet_manifest = read_json("logs/PAN_ROMANCE_FAMILY_SOURCE_PACKET_MANIFEST_20260629.json")
    pan_romance_promoted_register_hit_table = read_json(
        "logs/PAN_ROMANCE_PROMOTED_REGISTER_60_TERM_SOURCE_HIT_TABLE_20260629.json"
    )
    pan_romance_special_register_examples = read_json(
        "logs/PAN_ROMANCE_PROMOTED_SPECIAL_REGISTER_SOURCE_EXAMPLES_20260629.json"
    )
    french_spanish_worklog = read_json("logs/FRENCH_SPANISH_TRANSLATION_LANE_WORKLOG_20260629.json")
    french_spanish_invariant_hardterm = read_json(
        "logs/FRENCH_SPANISH_INVARIANT_HARDTERM_EVIDENCE_20260630T065920Z.json"
    )
    spanish_covariant_hardterm_retry = read_json("logs/SPANISH_COVARIANT_HARDTERM_RETRY_20260630T071100Z.json")
    spanish_covariant_tex_source_retry = read_json("logs/SPANISH_COVARIANT_TEX_SOURCE_RETRY_20260630T072204Z.json")
    spanish_covariant_tex_broader_retry = read_json(
        "logs/SPANISH_COVARIANT_TEX_BROADER_RETRY_20260630T083000Z.json"
    )
    spanish_p40_resync = read_json("logs/SPANISH_P40_INTRO_SOURCE_RESYNC_20260629.json")
    persian_arabic_shelf = read_json("logs/PERSIAN_ARABIC_NATIVE_MATH_REGISTER_SHELF_20260628T210457Z.json")
    persian_arabic_tex_first = read_json(
        "logs/PERSIAN_ARABIC_NATIVE_MATH_REGISTER_TEX_SOURCE_FIRST_SHELF_20260628T211612Z.json"
    )
    persian_arabic_deep = read_json(
        "logs/PERSIAN_ARABIC_DARI_TAJIK_DEEP_TEX_SOURCE_REGISTER_SHELF_20260628T213737Z.json"
    )
    dari_afghan_persian_invariant_pdf_capture = read_json(
        "logs/R3_DARI_AFGHAN_PERSIAN_INVARIANT_PDF_LEAD_CAPTURE_20260630T064253Z.json"
    )
    dari_afghan_math_pdf_fallback_shelf = read_json(
        "logs/DARI_AFGHAN_MATH_PDF_FALLBACK_SHELF_20260630T182039Z.json"
    )
    tajik_cyrillic_source_retry = read_json("logs/TAJIK_CYRILLIC_MATH_SOURCE_RETRY_20260630T104800Z.json")
    chinese_japanese_agenda = read_json("logs/CHINESE_JAPANESE_TRANSLATION_LANE_UPDATE_AGENDA_20260628.json")
    chinese_japanese_status_audit = read_json("logs/CHINESE_JAPANESE_TRANSLATION_LANE_STATUS_AUDIT_20260628.json")
    chinese_japanese_methodology = read_json("logs/CHINESE_JAPANESE_COMPLETION_METHODOLOGY_20260629.json")
    chinese_japanese_inventory = read_json("logs/CHINESE_JAPANESE_COMPLETION_INVENTORY_20260629.json")
    simplified_chinese_p20_render = read_json("logs/SIMPLIFIED_CHINESE_PAPER20_RENDER_VALIDATION_20260629.json")
    simplified_chinese_p21_render = read_json("logs/SIMPLIFIED_CHINESE_PAPER21_RENDER_VALIDATION_20260629.json")
    japanese_p19s04_applied = read_json("logs/JAPANESE_P19S04_SOURCE_CORRECTIONS_APPLIED_20260629.json")
    japanese_p19_combined_render = read_json("logs/JAPANESE_P19S04_P19S06_COMBINED_RENDER_VALIDATION_20260629.json")
    east_southeast_asia = read_json("logs/EAST_SOUTHEAST_ASIA_NATIVE_MATH_REGISTER_SHELF_20260628.json")
    japanese_tau_applied = read_json("logs/JAPANESE_P19S06_TAU_CORRECTION_APPLIED_20260629.json")
    japanese_tau_rendered = read_json("logs/JAPANESE_P19S06_TAU_CORRECTION_RENDERED_20260629.json")
    south_american = read_json("logs/SOUTH_AMERICAN_ADJACENT_LANGUAGE_MATH_TEX_AUDIT_20260628.json")
    asia_wide = read_json("logs/ASIA_WIDE_TEX_SOURCE_MATH_REGISTER_SHELF_20260628T215200Z.json")
    world_family_matrix = read_json("logs/INTERLANGUAGE_CANDIDATE_MATRIX_20260628T213951Z_WORLD_FAMILY_CONSTRUCTION.json")
    world_family_index = read_json("logs/WORLD_FAMILY_INTERLANGUAGE_COORDINATION_INDEX_20260628T214958Z.json")
    world_family_roadmap = read_json("logs/WORLD_FAMILY_TECHNICAL_BRIDGE_ACTIONABLE_ROADMAP_20260628T215240Z.json")
    world_family_gap_audit = read_json("logs/WORLD_FAMILY_MISSING_REGION_GAP_AUDIT_20260628T215240Z.json")
    world_family_coverage_closure = read_json("logs/WORLD_FAMILY_COVERAGE_CLOSURE_AUDIT_20260629T015305Z.json")
    world_family_least_served = read_json(
        "logs/WORLD_FAMILY_LEAST_SERVED_READER_LEGIBILITY_POLICY_20260629T015305Z.json"
    )
    world_family_optimal_access = read_json("logs/WORLD_FAMILY_OPTIMAL_ACCESS_RESEARCH_NOTE_20260629T020750Z.json")
    world_family_targets = read_json("logs/WORLD_FAMILY_BRIDGE_REGISTER_CONSTRUCTION_TARGETS_20260628T221253Z.json")
    world_family_handoff = read_json("logs/WORLD_FAMILY_PARALLEL_HANDOFF_PROMPTS_20260628T215810Z.json")
    world_family_dashboard = read_json("logs/WORLD_FAMILY_BRIDGE_LANE_STATUS_DASHBOARD_20260628T215810Z.json")
    world_family_goal_audit = read_json("logs/WORLD_FAMILY_GOAL_COMPLETION_AUDIT_20260628T220603Z.json")
    world_family_live_tracker = read_json("logs/WORLD_FAMILY_LIVE_DISPATCH_TRACKER_20260628T220603Z.json")
    arabic_script_guardrail = read_json("logs/ARABIC_SCRIPT_NON_ERASURE_GUARDRAIL_20260629.json")
    pan_romance_decisions = read_json("logs/PAN_ROMANCE_TECHNICAL_BRIDGE_CONSTRUCTION_DECISIONS_20260628T221717Z.json")
    controlled_arabic_decisions = read_json(
        "logs/CONTROLLED_ARABIC_TECHNICAL_REGISTER_DECISIONS_20260628T222119Z.json"
    )
    controlled_arabic_native_shelf = read_json(
        "logs/CONTROLLED_ARABIC_NATIVE_MATH_REGISTER_SHELF_20260628T232000Z.json"
    )
    controlled_arabic_60_term_spine = read_json(
        "logs/CONTROLLED_ARABIC_60_TERM_SPINE_20260629T021500Z.json"
    )
    controlled_arabic_covariant_binary_form_retry = read_json(
        "logs/CONTROLLED_ARABIC_COVARIANT_BINARY_FORM_SOURCE_RETRY_20260630T063033Z.json"
    )
    controlled_arabic_covariant_binary_form_addendum = read_json(
        "logs/CONTROLLED_ARABIC_COVARIANT_BINARY_FORM_REVIEWER_ADDENDUM_20260630T063033Z.json"
    )
    controlled_arabic_abstract_algebra_source_retry = read_json(
        "logs/CONTROLLED_ARABIC_ABSTRACT_ALGEBRA_SOURCE_RETRY_20260630T092000Z.json"
    )
    controlled_arabic_invariant_register_sweep = read_json(
        "logs/CONTROLLED_ARABIC_INVARIANT_REGISTER_SWEEP_20260630T180627Z.json"
    )
    arabic_persianate_split_index = read_json("logs/ARABIC_PERSIANATE_EVIDENCE_SPLIT_INDEX_20260629T013531Z.json")
    controlled_arabic_evidence_split = read_json("logs/CONTROLLED_ARABIC_EVIDENCE_SPLIT_20260629T013531Z.json")
    persianate_evidence_split = read_json("logs/PERSIANATE_FARSI_DARI_TAJIK_EVIDENCE_SPLIT_20260629T013531Z.json")
    arabic_script_neighbor_split = read_json(
        "logs/ARABIC_SCRIPT_NEIGHBOR_INFRASTRUCTURE_EVIDENCE_SPLIT_20260629T013531Z.json"
    )
    persianate_decisions = read_json("logs/PERSIANATE_SCRIPT_AND_STANDARD_POLICY_20260628T222119Z.json")
    latest_zenodo = read_json("logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260701T222409Z.json")
    targeted_gap_integration = read_json("logs/NON_SLAVIC_TARGETED_GAP_SOURCE_INTEGRATION_20260628.json")
    local_drop = read_json("logs/PARALLEL_CODEX_LOCAL_DROP_NON_SLAVIC_SOURCE_STATUS_20260628.json")
    prompts = read_json("logs/PARALLEL_CODEX_HANDOFF_PROMPTS_20260628.json")
    interlanguage = read_json("logs/INTERLANGUAGE_METHODOLOGY_AND_OPEN_SOURCE_EDUCATION_NOTE_20260628.json")
    interlanguage_matrix = read_json("logs/INTERLANGUAGE_CANDIDATE_MATRIX_20260628.json")
    inventory = read_json("logs/NON_SLAVIC_EXISTING_TRANSLATION_INVENTORY_20260628.json")
    artifact_import = read_json("logs/NON_SLAVIC_EXISTING_TRANSLATION_ARTIFACT_IMPORT_20260628.json")
    artifact_audit_queue = read_json("logs/NON_SLAVIC_IMPORTED_ARTIFACT_AUDIT_QUEUE_20260628.json")
    correction_queue = read_json("logs/NON_SLAVIC_CROSS_LANE_SOURCE_CORRECTION_QUEUE_20260628.json")
    visual = read_json("logs/NON_SLAVIC_PDF_VISUAL_CONTACT_SHEETS_LATEST.json")
    visual_summary = read_json("logs/NON_SLAVIC_VISUAL_INSPECTION_SUMMARY_20260628.json")
    terminology_ledger = read_json("logs/NON_SLAVIC_TERMINOLOGY_RATIONALE_SEED_LEDGER_20260628.json")
    targeted_gap_external = read_json("logs/NON_SLAVIC_TARGETED_GAP_EXTERNAL_EVIDENCE_LATEST.json")
    targeted_gap_supplement = read_json("logs/NON_SLAVIC_TARGETED_GAP_SOURCE_INTEGRATION_SUPPLEMENT_20260629.json")
    other_session_check = read_json("logs/PARALLEL_CODEX_OTHER_SESSION_COORDINATION_CHECK_20260629.json")
    world_family_local_drop = read_json("logs/PARALLEL_CODEX_LOCAL_DROP_WORLD_FAMILY_COORDINATION_20260629.json")
    chinese_japanese_local_drop = read_json("logs/PARALLEL_CODEX_LOCAL_DROP_CHINESE_JAPANESE_20260629.json")
    watchdog = read_json("logs/SLAVIC_MAINTENANCE_WATCHDOG_20260628.json")
    summary = {
        "recorded_at_utc": package_record["recorded_at_utc"],
        "non_slavic_arxiv_reference_shelf": {
            "json": "logs/NON_SLAVIC_ARXIV_REFERENCE_SHELF_20260628.json",
            "markdown": "logs/NON_SLAVIC_ARXIV_REFERENCE_SHELF_20260628.md",
            "language_count": len(shelf.get("languages", [])),
            "candidate_counts": {
                language["language_id"]: len(language.get("candidates", []))
                for language in shelf.get("languages", [])
            },
            "download_counts": {
                language["language_id"]: {
                    "pdf": sum(1 for item in language.get("downloads", []) if item.get("pdf", {}).get("downloaded")),
                    "source": sum(1 for item in language.get("downloads", []) if item.get("source", {}).get("downloaded")),
                }
                for language in shelf.get("languages", [])
            },
        },
        "global_language_completion_lane": {
            "json": "logs/GLOBAL_LANGUAGE_COMPLETION_AND_EDUCATIONAL_TRANSLATION_LANE_20260628.json",
            "markdown": "logs/GLOBAL_LANGUAGE_COMPLETION_AND_EDUCATIONAL_TRANSLATION_LANE_20260628.md",
            "named_examples": read_json("logs/GLOBAL_LANGUAGE_COMPLETION_AND_EDUCATIONAL_TRANSLATION_LANE_20260628.json")
            .get("immediate_non_slavic_lane", {})
            .get("named_examples", []),
        },
        "fallback_source_shelf": {
            "json": "logs/CHINESE_JAPANESE_PERSIAN_ARABIC_FALLBACK_SOURCE_SHELF_20260628.json",
            "markdown": "logs/CHINESE_JAPANESE_PERSIAN_ARABIC_FALLBACK_SOURCE_SHELF_20260628.md",
            "downloaded_count": fallback.get("summary", {}).get("downloaded_count"),
            "failed_count": fallback.get("summary", {}).get("failed_count"),
            "language_counts": fallback.get("summary", {}).get("language_counts"),
        },
        "expanded_native_register_shelves": {
            "chinese_japanese": {
                "json": "logs/CHINESE_JAPANESE_NATIVE_MATH_REGISTER_SHELF_20260628.json",
                "markdown": "logs/CHINESE_JAPANESE_NATIVE_MATH_REGISTER_SHELF_20260628.md",
                "summary": chinese_japanese_shelf.get("summary"),
            },
            "chinese_japanese_hardterm_source_retry_20260630": {
                "json": "logs/CHINESE_JAPANESE_HARDTERM_SOURCE_RETRY_20260630T080000Z.json",
                "markdown": "logs/CHINESE_JAPANESE_HARDTERM_SOURCE_RETRY_20260630T080000Z.md",
                "builder": "tmp/build_chinese_japanese_hardterm_source_retry_20260630.py",
                "updater": "tmp/update_chinese_japanese_hardterm_source_retry_coordination_20260630.py",
                "source_root": chinese_japanese_hardterm_source_retry.get("source_root"),
                "status": chinese_japanese_hardterm_source_retry.get("status"),
                "summary": chinese_japanese_hardterm_source_retry.get("summary"),
                "lane_impact": chinese_japanese_hardterm_source_retry.get("lane_impact"),
                "promotion_boundary": chinese_japanese_hardterm_source_retry.get("promotion_boundary"),
            },
            "japanese_representation_exact_source_retry_20260630": {
                "json": "logs/JAPANESE_REPRESENTATION_EXACT_SOURCE_RETRY_20260630T081000Z.json",
                "markdown": "logs/JAPANESE_REPRESENTATION_EXACT_SOURCE_RETRY_20260630T081000Z.md",
                "capture": "tmp/capture_japanese_representation_exact_search_20260630.py",
                "builder": "tmp/build_japanese_representation_exact_source_retry_20260630.py",
                "updater": "tmp/update_japanese_representation_exact_source_retry_coordination_20260630.py",
                "source_root": japanese_representation_exact_source_retry.get("source_root"),
                "status": japanese_representation_exact_source_retry.get("status"),
                "accepted_exact_field_label_count": japanese_representation_exact_source_retry.get(
                    "accepted_exact_field_label_count"
                ),
                "accepted_auxiliary_representation_register_count": japanese_representation_exact_source_retry.get(
                    "accepted_auxiliary_representation_register_count"
                ),
                "term_values": japanese_representation_exact_source_retry.get("term_values"),
                "term_totals": japanese_representation_exact_source_retry.get("term_totals"),
                "lane_impact": japanese_representation_exact_source_retry.get("lane_impact"),
                "boundary": japanese_representation_exact_source_retry.get("boundary"),
            },
            "french_spanish": {
                "json": "logs/FRENCH_SPANISH_NATIVE_MATH_REGISTER_SHELF_20260628.json",
                "markdown": "logs/FRENCH_SPANISH_NATIVE_MATH_REGISTER_SHELF_20260628.md",
                "source_catalog_count": len(french_spanish_shelf.get("source_catalog", []))
                if isinstance(french_spanish_shelf.get("source_catalog"), list)
                else None,
                "weak_or_excluded_count": len(french_spanish_shelf.get("weak_or_excluded_candidates", []))
                if isinstance(french_spanish_shelf.get("weak_or_excluded_candidates"), list)
                else None,
                "terminology_starter_count": len(french_spanish_shelf.get("terminology_starter", []))
                if isinstance(french_spanish_shelf.get("terminology_starter"), list)
                else None,
            },
            "french_spanish_latex_first_pass": {
                "json": "logs/FRENCH_SPANISH_LATEX_SOURCE_CORPUS_20260628.json",
                "text_manifest": "logs/FRENCH_SPANISH_LATEX_SOURCE_CORPUS_20260628.txt",
                "summary": french_spanish_latex.get("summary"),
            },
            "french_spanish_latex_expanded_validated": {
                "json": "logs/FRENCH_SPANISH_LATEX_SOURCE_CORPUS_EXPANDED_20260628.json",
                "text_manifest": "logs/FRENCH_SPANISH_LATEX_SOURCE_CORPUS_EXPANDED_20260628.txt",
                "summary": french_spanish_latex_expanded.get("summary"),
                "source_directories": french_spanish_latex_expanded.get("source_directories"),
            },
            "french_spanish_invariant_hardterm_evidence_20260630": {
                "json": "logs/FRENCH_SPANISH_INVARIANT_HARDTERM_EVIDENCE_20260630T065920Z.json",
                "markdown": "logs/FRENCH_SPANISH_INVARIANT_HARDTERM_EVIDENCE_20260630T065920Z.md",
                "source_root": french_spanish_invariant_hardterm.get("source_root"),
                "status": french_spanish_invariant_hardterm.get("status"),
                "remote_summary": french_spanish_invariant_hardterm.get("remote_summary"),
                "local_validated_tex_counts": french_spanish_invariant_hardterm.get(
                    "local_validated_tex_corpus", {}
                ).get("aggregate_counts"),
                "decisions": french_spanish_invariant_hardterm.get("decisions"),
                "boundary": french_spanish_invariant_hardterm.get("decisions", {}).get("global_boundary"),
            },
            "spanish_covariant_hardterm_retry_20260630": {
                "json": "logs/SPANISH_COVARIANT_HARDTERM_RETRY_20260630T071100Z.json",
                "markdown": "logs/SPANISH_COVARIANT_HARDTERM_RETRY_20260630T071100Z.md",
                "source_root": spanish_covariant_hardterm_retry.get("source_root"),
                "status": spanish_covariant_hardterm_retry.get("status"),
                "remote_summary": spanish_covariant_hardterm_retry.get("remote_summary"),
                "decision": spanish_covariant_hardterm_retry.get("decision"),
                "previous_local_scan": spanish_covariant_hardterm_retry.get("previous_local_scan"),
                "boundary": spanish_covariant_hardterm_retry.get("decision", {}).get("promotion_boundary"),
            },
            "spanish_covariant_tex_source_retry_20260630": {
                "json": "logs/SPANISH_COVARIANT_TEX_SOURCE_RETRY_20260630T072204Z.json",
                "markdown": "logs/SPANISH_COVARIANT_TEX_SOURCE_RETRY_20260630T072204Z.md",
                "source_root": spanish_covariant_tex_source_retry.get("source_root"),
                "status": spanish_covariant_tex_source_retry.get("status"),
                "validated_spanish_tex_scan": spanish_covariant_tex_source_retry.get("validated_spanish_tex_scan"),
                "github_code_search_observations": spanish_covariant_tex_source_retry.get(
                    "github_code_search_observations"
                ),
                "rejected_github_ocr_hits": spanish_covariant_tex_source_retry.get("rejected_github_ocr_hits"),
                "decision": spanish_covariant_tex_source_retry.get("decision"),
                "boundary": spanish_covariant_tex_source_retry.get("decision", {}).get("promotion_boundary"),
            },
            "spanish_covariant_tex_broader_retry_20260630": {
                "json": "logs/SPANISH_COVARIANT_TEX_BROADER_RETRY_20260630T083000Z.json",
                "markdown": "logs/SPANISH_COVARIANT_TEX_BROADER_RETRY_20260630T083000Z.md",
                "builder": "tmp/build_spanish_covariant_tex_broader_retry_20260630.py",
                "updater": "tmp/update_spanish_covariant_tex_broader_retry_coordination_20260630.py",
                "source_root": spanish_covariant_tex_broader_retry.get("source_root"),
                "status": spanish_covariant_tex_broader_retry.get("status"),
                "unique_candidate_count": spanish_covariant_tex_broader_retry.get("unique_candidate_count"),
                "download_attempt_count": spanish_covariant_tex_broader_retry.get("download_attempt_count"),
                "accepted_classical_tex_source_count": spanish_covariant_tex_broader_retry.get(
                    "accepted_tex_source_count"
                ),
                "adjacent_general_covariant_tex_count": spanish_covariant_tex_broader_retry.get(
                    "adjacent_general_covariant_tex_count"
                ),
                "adjacent_general_covariant_tex_counts": spanish_covariant_tex_broader_retry.get(
                    "adjacent_general_covariant_tex_counts"
                ),
                "decision": spanish_covariant_tex_broader_retry.get("decision"),
                "boundary": spanish_covariant_tex_broader_retry.get("decision", {}).get("promotion_boundary"),
            },
            "tajik_cyrillic_math_source_retry_20260630": {
                "json": "logs/TAJIK_CYRILLIC_MATH_SOURCE_RETRY_20260630T104800Z.json",
                "markdown": "logs/TAJIK_CYRILLIC_MATH_SOURCE_RETRY_20260630T104800Z.md",
                "builder": "tmp/build_tajik_cyrillic_math_source_retry_20260630.py",
                "updater": "tmp/update_tajik_cyrillic_source_retry_coordination_20260630.py",
                "source_root": tajik_cyrillic_source_retry.get("source_root"),
                "decision": tajik_cyrillic_source_retry.get("summary", {}).get("decision"),
                "summary": tajik_cyrillic_source_retry.get("summary"),
                "policy": tajik_cyrillic_source_retry.get("policy"),
                "strongest_source_ids": tajik_cyrillic_source_retry.get("strongest_source_ids"),
                "term_values": tajik_cyrillic_source_retry.get("term_values"),
                "boundary": "Tajik Cyrillic PDF/source evidence strengthened for algebra and linear-algebra register; TeX/source-code, rings/ideals/modules/representation/invariant theory, native review, and translation promotion remain open.",
            },
            "pan_romance_native_math_register_source_scope_20260629": {
                "json": "logs/PAN_ROMANCE_NATIVE_MATH_REGISTER_SOURCE_SCOPE_20260629.json",
                "markdown": "logs/PAN_ROMANCE_NATIVE_MATH_REGISTER_SOURCE_SCOPE_20260629.md",
                "status": pan_romance_source_scope.get("status"),
                "candidate_root": pan_romance_source_scope.get("candidate_root"),
                "summary": pan_romance_source_scope.get("summary"),
                "boundary": pan_romance_source_scope.get("boundary"),
            },
            "pan_romance_core_control_source_consolidation_20260630": {
                "json": "logs/PAN_ROMANCE_CORE_CONTROL_SOURCE_CONSOLIDATION_20260630T073020Z.json",
                "markdown": "logs/PAN_ROMANCE_CORE_CONTROL_SOURCE_CONSOLIDATION_20260630T073020Z.md",
                "builder": "tmp/build_pan_romance_core_control_consolidation_20260630.py",
                "status": pan_romance_core_consolidation.get("status"),
                "decision": pan_romance_core_consolidation.get("decision"),
                "summary": pan_romance_core_consolidation.get("summary"),
                "included_pan_romance_ledgers": {
                    "spine_60_term_json": "logs/PAN_ROMANCE_60_TERM_SPINE_DRAFT_20260629.json",
                    "spine_60_term_markdown": "logs/PAN_ROMANCE_60_TERM_SPINE_DRAFT_20260629.md",
                    "fallback_hit_review_json": "logs/PAN_ROMANCE_FALLBACK_TERM_HIT_REVIEW_20260629.json",
                    "fallback_hit_review_markdown": "logs/PAN_ROMANCE_FALLBACK_TERM_HIT_REVIEW_20260629.md",
                    "family_source_matrix_json": "logs/PAN_ROMANCE_FAMILY_SOURCE_MATRIX_20260629.json",
                    "family_source_matrix_markdown": "logs/PAN_ROMANCE_FAMILY_SOURCE_MATRIX_20260629.md",
                    "family_source_packet_manifest_json": "logs/PAN_ROMANCE_FAMILY_SOURCE_PACKET_MANIFEST_20260629.json",
                    "family_source_packet_manifest_markdown": "logs/PAN_ROMANCE_FAMILY_SOURCE_PACKET_MANIFEST_20260629.md",
                    "promoted_register_60_term_hit_table_json": (
                        "logs/PAN_ROMANCE_PROMOTED_REGISTER_60_TERM_SOURCE_HIT_TABLE_20260629.json"
                    ),
                    "promoted_register_60_term_hit_table_markdown": (
                        "logs/PAN_ROMANCE_PROMOTED_REGISTER_60_TERM_SOURCE_HIT_TABLE_20260629.md"
                    ),
                },
                "spine_summary": pan_romance_60_term_spine.get("summary"),
                "fallback_hit_review_summary": pan_romance_fallback_hit_review.get("summary"),
                "family_matrix_status": pan_romance_family_matrix.get("status"),
                "source_packet_manifest_status": pan_romance_source_packet_manifest.get("status"),
                "promoted_register_hit_table_summary": pan_romance_promoted_register_hit_table.get("summary"),
                "special_register_examples_status": pan_romance_special_register_examples.get("status"),
            },
            "french_spanish_translation_lane_worklog_20260629": {
                "json": "logs/FRENCH_SPANISH_TRANSLATION_LANE_WORKLOG_20260629.json",
                "markdown": "logs/FRENCH_SPANISH_TRANSLATION_LANE_WORKLOG_20260629.md",
                "status": french_spanish_worklog.get("status"),
                "spanish_render": french_spanish_worklog.get("spanish", {}).get("render"),
                "french_render": french_spanish_worklog.get("french", {}).get("render"),
                "spanish_p40_resync": {
                    "json": "logs/SPANISH_P40_INTRO_SOURCE_RESYNC_20260629.json",
                    "markdown": "logs/SPANISH_P40_INTRO_SOURCE_RESYNC_20260629.md",
                    "status": spanish_p40_resync.get("status"),
                    "scope": spanish_p40_resync.get("scope"),
                    "render": spanish_p40_resync.get("verification", {}).get("render"),
                },
            },
            "persian_arabic_dari_tajik": {
                "json": "logs/PERSIAN_ARABIC_NATIVE_MATH_REGISTER_SHELF_20260628T210457Z.json",
                "markdown": "logs/PERSIAN_ARABIC_NATIVE_MATH_REGISTER_SHELF_20260628T210457Z.md",
                "summary": persian_arabic_shelf.get("summary"),
            },
            "persian_arabic_tex_source_first": {
                "json": "logs/PERSIAN_ARABIC_NATIVE_MATH_REGISTER_TEX_SOURCE_FIRST_SHELF_20260628T211612Z.json",
                "markdown": "logs/PERSIAN_ARABIC_NATIVE_MATH_REGISTER_TEX_SOURCE_FIRST_SHELF_20260628T211612Z.md",
                "summary": persian_arabic_tex_first.get("summary"),
                "scope_note": persian_arabic_tex_first.get("scope_note"),
            },
            "persian_arabic_dari_tajik_deep_tex": {
                "json": "logs/PERSIAN_ARABIC_DARI_TAJIK_DEEP_TEX_SOURCE_REGISTER_SHELF_20260628T213737Z.json",
                "markdown": "logs/PERSIAN_ARABIC_DARI_TAJIK_DEEP_TEX_SOURCE_REGISTER_SHELF_20260628T213737Z.md",
                "summary": persian_arabic_deep.get("summary"),
                "scope_note": persian_arabic_deep.get("scope_note"),
            },
            "dari_afghan_persian_invariant_pdf_lead_capture_20260630": {
                "json": "logs/R3_DARI_AFGHAN_PERSIAN_INVARIANT_PDF_LEAD_CAPTURE_20260630T064253Z.json",
                "markdown": "logs/R3_DARI_AFGHAN_PERSIAN_INVARIANT_PDF_LEAD_CAPTURE_20260630T064253Z.md",
                "source_root": dari_afghan_persian_invariant_pdf_capture.get("source_root"),
                "status": dari_afghan_persian_invariant_pdf_capture.get("status"),
                "summary": dari_afghan_persian_invariant_pdf_capture.get("summary"),
                "gate_decision": dari_afghan_persian_invariant_pdf_capture.get("gate_decision"),
            },
            "dari_afghan_math_pdf_fallback_shelf_20260630": {
                "json": "logs/DARI_AFGHAN_MATH_PDF_FALLBACK_SHELF_20260630T182039Z.json",
                "markdown": "logs/DARI_AFGHAN_MATH_PDF_FALLBACK_SHELF_20260630T182039Z.md",
                "builder": "tmp/build_dari_afghan_math_pdf_fallback_shelf_20260630.py",
                "updater": "tmp/update_dari_afghan_math_pdf_fallback_shelf_coordination_20260630.py",
                "source_root": dari_afghan_math_pdf_fallback_shelf.get("source_root"),
                "status": dari_afghan_math_pdf_fallback_shelf.get("status"),
                "summary": dari_afghan_math_pdf_fallback_shelf.get("summary"),
                "policy": dari_afghan_math_pdf_fallback_shelf.get("policy"),
                "boundary": "Afghan Arabic-script/Dari-Pashto PDF fallback math-register context is strengthened; direct Dari invariant theory, TeX/source-code, native/domain review, glossary, bridge, translation, and pilot gates remain open.",
            },
            "controlled_arabic_native_math_register": {
                "json": "logs/CONTROLLED_ARABIC_NATIVE_MATH_REGISTER_SHELF_20260628T232000Z.json",
                "markdown": "logs/CONTROLLED_ARABIC_NATIVE_MATH_REGISTER_SHELF_20260628T232000Z.md",
                "source_root": controlled_arabic_native_shelf.get("source_root"),
                "downloaded_count": controlled_arabic_native_shelf.get("downloaded_count"),
                "text_extracted_count": controlled_arabic_native_shelf.get("text_extracted_count"),
                "aggregate_term_counts": controlled_arabic_native_shelf.get("aggregate_term_counts"),
                "decisions": controlled_arabic_native_shelf.get("decisions"),
                "pilot_boundary": controlled_arabic_native_shelf.get("promotion_boundary")
                or controlled_arabic_native_shelf.get("pilot_boundary"),
            },
            "controlled_arabic_60_term_spine": {
                "json": "logs/CONTROLLED_ARABIC_60_TERM_SPINE_20260629T021500Z.json",
                "markdown": "logs/CONTROLLED_ARABIC_60_TERM_SPINE_20260629T021500Z.md",
                "status": controlled_arabic_60_term_spine.get("status"),
                "summary": controlled_arabic_60_term_spine.get("summary"),
                "promotion_boundary": controlled_arabic_60_term_spine.get("promotion_boundary"),
                "pilot_ready": controlled_arabic_60_term_spine.get("pilot_ready"),
            },
            "controlled_arabic_covariant_binary_form_retry_20260630": {
                "json": "logs/CONTROLLED_ARABIC_COVARIANT_BINARY_FORM_SOURCE_RETRY_20260630T063033Z.json",
                "markdown": "logs/CONTROLLED_ARABIC_COVARIANT_BINARY_FORM_SOURCE_RETRY_20260630T063033Z.md",
                "reviewer_addendum_json": "logs/CONTROLLED_ARABIC_COVARIANT_BINARY_FORM_REVIEWER_ADDENDUM_20260630T063033Z.json",
                "reviewer_addendum_markdown": "logs/CONTROLLED_ARABIC_COVARIANT_BINARY_FORM_REVIEWER_ADDENDUM_20260630T063033Z.md",
                "source_root": controlled_arabic_covariant_binary_form_retry.get("source_root"),
                "status": controlled_arabic_covariant_binary_form_retry.get("status"),
                "strong_direct_arabic_specialist_source_count": controlled_arabic_covariant_binary_form_retry.get(
                    "strong_direct_arabic_specialist_source_count"
                ),
                "gate_decision": controlled_arabic_covariant_binary_form_retry.get("gate_decision"),
                "reviewer_addendum_status": controlled_arabic_covariant_binary_form_addendum.get("status"),
                "reviewer_term_rows": controlled_arabic_covariant_binary_form_addendum.get("term_rows"),
            },
            "controlled_arabic_abstract_algebra_source_retry_20260630": {
                "json": "logs/CONTROLLED_ARABIC_ABSTRACT_ALGEBRA_SOURCE_RETRY_20260630T092000Z.json",
                "markdown": "logs/CONTROLLED_ARABIC_ABSTRACT_ALGEBRA_SOURCE_RETRY_20260630T092000Z.md",
                "builder": "tmp/build_controlled_arabic_abstract_algebra_source_retry_20260630.py",
                "updater": "tmp/update_controlled_arabic_abstract_algebra_source_retry_coordination_20260630.py",
                "source_root": controlled_arabic_abstract_algebra_source_retry.get("source_root"),
                "status": controlled_arabic_abstract_algebra_source_retry.get("status"),
                "summary": controlled_arabic_abstract_algebra_source_retry.get("summary"),
                "accepted_direct_source_ids": controlled_arabic_abstract_algebra_source_retry.get(
                    "accepted_direct_source_ids"
                ),
                "accepted_course_register_source_ids": controlled_arabic_abstract_algebra_source_retry.get(
                    "accepted_course_register_source_ids"
                ),
                "policy": controlled_arabic_abstract_algebra_source_retry.get("policy"),
                "boundary": "Arabic abstract-algebra/ring/field/ideal/module evidence is strengthened; classical invariant theory, covariant, binary-form, ring-of-invariants, native-review, glossary, and translation gates remain open.",
            },
            "controlled_arabic_invariant_register_sweep_20260630": {
                "json": "logs/CONTROLLED_ARABIC_INVARIANT_REGISTER_SWEEP_20260630T180627Z.json",
                "markdown": "logs/CONTROLLED_ARABIC_INVARIANT_REGISTER_SWEEP_20260630T180627Z.md",
                "builder": "tmp/build_controlled_arabic_invariant_register_sweep_20260630.py",
                "updater": "tmp/update_controlled_arabic_invariant_register_sweep_coordination_20260630.py",
                "source_root": controlled_arabic_invariant_register_sweep.get("source_root"),
                "status": controlled_arabic_invariant_register_sweep.get("status"),
                "summary": controlled_arabic_invariant_register_sweep.get("summary"),
                "accepted_weak_secondary_or_public_register_source_ids": (
                    controlled_arabic_invariant_register_sweep.get(
                        "accepted_weak_secondary_or_public_register_source_ids"
                    )
                ),
                "strong_direct_arabic_specialist_source_ids": controlled_arabic_invariant_register_sweep.get(
                    "strong_direct_arabic_specialist_source_ids"
                ),
                "policy": controlled_arabic_invariant_register_sweep.get("policy"),
                "boundary": "Weak/secondary Arabic invariant-theory/GIT register evidence is documented; classical invariant theory, covariant, binary-form, ring-of-invariants, native-review, glossary, translation, and pilot gates remain open.",
            },
            "arabic_persianate_evidence_split_20260629": {
                "index_json": "logs/ARABIC_PERSIANATE_EVIDENCE_SPLIT_INDEX_20260629T013531Z.json",
                "index_markdown": "logs/ARABIC_PERSIANATE_EVIDENCE_SPLIT_INDEX_20260629T013531Z.md",
                "controlled_arabic_json": "logs/CONTROLLED_ARABIC_EVIDENCE_SPLIT_20260629T013531Z.json",
                "controlled_arabic_markdown": "logs/CONTROLLED_ARABIC_EVIDENCE_SPLIT_20260629T013531Z.md",
                "persianate_json": "logs/PERSIANATE_FARSI_DARI_TAJIK_EVIDENCE_SPLIT_20260629T013531Z.json",
                "persianate_markdown": "logs/PERSIANATE_FARSI_DARI_TAJIK_EVIDENCE_SPLIT_20260629T013531Z.md",
                "arabic_script_neighbor_json": (
                    "logs/ARABIC_SCRIPT_NEIGHBOR_INFRASTRUCTURE_EVIDENCE_SPLIT_20260629T013531Z.json"
                ),
                "arabic_script_neighbor_markdown": (
                    "logs/ARABIC_SCRIPT_NEIGHBOR_INFRASTRUCTURE_EVIDENCE_SPLIT_20260629T013531Z.md"
                ),
                "status": arabic_persianate_split_index.get("status"),
                "controlled_arabic_status": controlled_arabic_evidence_split.get("status"),
                "persianate_status": persianate_evidence_split.get("status"),
                "neighbor_split_status": arabic_script_neighbor_split.get("status"),
            },
            "south_american_adjacent_language_math_tex_audit": {
                "json": "logs/SOUTH_AMERICAN_ADJACENT_LANGUAGE_MATH_TEX_AUDIT_20260628.json",
                "text_manifest": "logs/SOUTH_AMERICAN_ADJACENT_LANGUAGE_MATH_TEX_AUDIT_20260628.txt",
                "summary": south_american.get("summary"),
                "status": south_american.get("status"),
            },
            "asia_wide_tex_source_math_register_shelf": {
                "json": "logs/ASIA_WIDE_TEX_SOURCE_MATH_REGISTER_SHELF_20260628T215200Z.json",
                "markdown": "logs/ASIA_WIDE_TEX_SOURCE_MATH_REGISTER_SHELF_20260628T215200Z.md",
                "summary": asia_wide.get("summary"),
                "scope_note": asia_wide.get("scope_note"),
                "regional_coordination_logbook": "logs/REGIONAL_LANGUAGE_EVIDENCE_COORDINATION_LOGBOOK_20260628.md",
            },
            "east_southeast_asia_native_math_register_shelf": {
                "json": "logs/EAST_SOUTHEAST_ASIA_NATIVE_MATH_REGISTER_SHELF_20260628.json",
                "markdown": "logs/EAST_SOUTHEAST_ASIA_NATIVE_MATH_REGISTER_SHELF_20260628.md",
                "summary": east_southeast_asia.get("summary"),
                "status": east_southeast_asia.get("status"),
            },
            "chinese_japanese_translation_lane_update_agenda": {
                "json": "logs/CHINESE_JAPANESE_TRANSLATION_LANE_UPDATE_AGENDA_20260628.json",
                "markdown": "logs/CHINESE_JAPANESE_TRANSLATION_LANE_UPDATE_AGENDA_20260628.md",
                "status": chinese_japanese_agenda.get("status"),
                "source_evidence_updates": chinese_japanese_agenda.get("source_evidence_updates"),
                "finish_criteria": chinese_japanese_agenda.get("finish_criteria"),
                "boundary": chinese_japanese_agenda.get("boundary"),
            },
            "chinese_japanese_translation_lane_status_audit": {
                "json": "logs/CHINESE_JAPANESE_TRANSLATION_LANE_STATUS_AUDIT_20260628.json",
                "markdown": "logs/CHINESE_JAPANESE_TRANSLATION_LANE_STATUS_AUDIT_20260628.md",
                "status": chinese_japanese_status_audit.get("status"),
                "updated_at_utc": chinese_japanese_status_audit.get("updated_at_utc"),
                "source_evidence_updates": chinese_japanese_status_audit.get("source_evidence_updates"),
                "label_update_recommendation": chinese_japanese_status_audit.get("label_update_recommendation"),
                "boundary": chinese_japanese_status_audit.get("boundary"),
            },
            "chinese_japanese_completion_lane_20260629": {
                "methodology_json": "logs/CHINESE_JAPANESE_COMPLETION_METHODOLOGY_20260629.json",
                "methodology_markdown": "logs/CHINESE_JAPANESE_COMPLETION_METHODOLOGY_20260629.md",
                "inventory_json": "logs/CHINESE_JAPANESE_COMPLETION_INVENTORY_20260629.json",
                "inventory_markdown": "logs/CHINESE_JAPANESE_COMPLETION_INVENTORY_20260629.md",
                "worklog_markdown": "logs/CHINESE_JAPANESE_COMPLETION_WORKLOG_20260629.md",
                "methodology_status": chinese_japanese_methodology.get("status"),
                "inventory_status": chinese_japanese_inventory.get("status"),
                "expected_review_units": chinese_japanese_inventory.get("expected_scope_from_slavic_method", {}).get(
                    "expected_review_units"
                ),
            },
            "chinese_japanese_render_validations_20260629": {
                "simplified_chinese_paper20_json": "logs/SIMPLIFIED_CHINESE_PAPER20_RENDER_VALIDATION_20260629.json",
                "simplified_chinese_paper20_markdown": "logs/SIMPLIFIED_CHINESE_PAPER20_RENDER_VALIDATION_20260629.md",
                "simplified_chinese_paper20_status": simplified_chinese_p20_render.get("status"),
                "simplified_chinese_paper20_pdf": simplified_chinese_p20_render.get("local_font_proof_render", {}).get(
                    "pdf"
                ),
                "simplified_chinese_paper21_json": "logs/SIMPLIFIED_CHINESE_PAPER21_RENDER_VALIDATION_20260629.json",
                "simplified_chinese_paper21_markdown": "logs/SIMPLIFIED_CHINESE_PAPER21_RENDER_VALIDATION_20260629.md",
                "simplified_chinese_paper21_status": simplified_chinese_p21_render.get("status"),
                "simplified_chinese_paper21_pdf": simplified_chinese_p21_render.get("local_font_proof_render", {}).get(
                    "pdf"
                ),
                "japanese_p19s04_correction_json": "logs/JAPANESE_P19S04_SOURCE_CORRECTIONS_APPLIED_20260629.json",
                "japanese_p19s04_correction_markdown": "logs/JAPANESE_P19S04_SOURCE_CORRECTIONS_APPLIED_20260629.md",
                "japanese_p19s04_status": japanese_p19s04_applied.get("status"),
                "japanese_p19s04_p19s06_render_json": (
                    "logs/JAPANESE_P19S04_P19S06_COMBINED_RENDER_VALIDATION_20260629.json"
                ),
                "japanese_p19s04_p19s06_render_markdown": (
                    "logs/JAPANESE_P19S04_P19S06_COMBINED_RENDER_VALIDATION_20260629.md"
                ),
                "japanese_p19s04_p19s06_render_status": japanese_p19_combined_render.get("status"),
                "japanese_p19s04_p19s06_render_pdf": japanese_p19_combined_render.get(
                    "local_font_proof_render", {}
                ).get("pdf"),
            },
            "japanese_p19s06_tau_correction": {
                "applied_json": "logs/JAPANESE_P19S06_TAU_CORRECTION_APPLIED_20260629.json",
                "applied_markdown": "logs/JAPANESE_P19S06_TAU_CORRECTION_APPLIED_20260629.md",
                "render_json": "logs/JAPANESE_P19S06_TAU_CORRECTION_RENDERED_20260629.json",
                "render_markdown": "logs/JAPANESE_P19S06_TAU_CORRECTION_RENDERED_20260629.md",
                "applied_status": japanese_tau_applied.get("status"),
                "render_status": japanese_tau_rendered.get("status"),
                "rendered_pdf": japanese_tau_rendered.get("rendered_pdf"),
                "rendered_pdf_sha256": japanese_tau_rendered.get("pdf_sha256"),
                "pdf_pages": japanese_tau_rendered.get("pdf_pages"),
                "visual_inspection": japanese_tau_rendered.get("visual_inspection"),
                "remaining_work": japanese_tau_rendered.get("remaining_work"),
            },
        },
        "existing_non_slavic_translation_inventory": {
            "json": "logs/NON_SLAVIC_EXISTING_TRANSLATION_INVENTORY_20260628.json",
            "markdown": "logs/NON_SLAVIC_EXISTING_TRANSLATION_INVENTORY_20260628.md",
            **summarize_inventory(inventory),
        },
        "existing_non_slavic_translation_artifact_import": {
            "json": "logs/NON_SLAVIC_EXISTING_TRANSLATION_ARTIFACT_IMPORT_20260628.json",
            "markdown": "logs/NON_SLAVIC_EXISTING_TRANSLATION_ARTIFACT_IMPORT_20260628.md",
            "artifact_count": artifact_import.get("artifact_count"),
            "language_counts": artifact_import.get("language_counts"),
            "zip_count": artifact_import.get("zip_count"),
            "pdf_count": artifact_import.get("pdf_count"),
            "boundary": artifact_import.get("boundary"),
        },
        "non_slavic_imported_artifact_audit_queue": {
            "json": "logs/NON_SLAVIC_IMPORTED_ARTIFACT_AUDIT_QUEUE_20260628.json",
            "markdown": "logs/NON_SLAVIC_IMPORTED_ARTIFACT_AUDIT_QUEUE_20260628.md",
            "lane_count": len(artifact_audit_queue.get("lanes", []))
            if isinstance(artifact_audit_queue.get("lanes"), list)
            else None,
            "cross_lane_findings": artifact_audit_queue.get("cross_lane_findings"),
        },
        "non_slavic_cross_lane_source_correction_queue": {
            "json": "logs/NON_SLAVIC_CROSS_LANE_SOURCE_CORRECTION_QUEUE_20260628.json",
            "markdown": "logs/NON_SLAVIC_CROSS_LANE_SOURCE_CORRECTION_QUEUE_20260628.md",
            "queued_correction_count": len(correction_queue.get("queued_corrections", []))
            if isinstance(correction_queue.get("queued_corrections"), list)
            else None,
            "coverage_notes": correction_queue.get("coverage_notes"),
        },
        "non_slavic_visual_inspection": {
            "contact_sheet_log_json": "logs/NON_SLAVIC_PDF_VISUAL_CONTACT_SHEETS_LATEST.json",
            "contact_sheet_log_markdown": "logs/NON_SLAVIC_PDF_VISUAL_CONTACT_SHEETS_LATEST.md",
            "summary_json": "logs/NON_SLAVIC_VISUAL_INSPECTION_SUMMARY_20260628.json",
            "summary_markdown": "logs/NON_SLAVIC_VISUAL_INSPECTION_SUMMARY_20260628.md",
            "contact_sheet_root": visual.get("output_root"),
            "rendered_count": visual.get("rendered_count"),
            "failed_count": visual.get("failed_count"),
            "hard_failure": visual_summary.get("hard_failure"),
            "boundary": visual_summary.get("boundary"),
        },
        "non_slavic_terminology_rationale_seed_ledger": {
            "json": "logs/NON_SLAVIC_TERMINOLOGY_RATIONALE_SEED_LEDGER_20260628.json",
            "markdown": "logs/NON_SLAVIC_TERMINOLOGY_RATIONALE_SEED_LEDGER_20260628.md",
            "record_count": terminology_ledger.get("record_count"),
            "concept_count": terminology_ledger.get("concept_count"),
            "language_counts": terminology_ledger.get("language_counts"),
            "gaps_and_review_requirements": terminology_ledger.get("gaps_and_review_requirements"),
            "targeted_gap_source_supplement_20260628": terminology_ledger.get(
                "targeted_gap_source_supplement_20260628"
            ),
            "authority_boundary": terminology_ledger.get("authority_boundary"),
        },
        "non_slavic_targeted_gap_source_integration": {
            "json": "logs/NON_SLAVIC_TARGETED_GAP_SOURCE_INTEGRATION_20260628.json",
            "markdown": "logs/NON_SLAVIC_TARGETED_GAP_SOURCE_INTEGRATION_20260628.md",
            "status": targeted_gap_integration.get("status"),
            "remaining_gaps_after_this_integration": targeted_gap_integration.get(
                "remaining_gaps_after_this_integration"
            ),
        },
        "non_slavic_targeted_gap_external_evidence": {
            "latest_json": "logs/NON_SLAVIC_TARGETED_GAP_EXTERNAL_EVIDENCE_LATEST.json",
            "latest_markdown": "logs/NON_SLAVIC_TARGETED_GAP_EXTERNAL_EVIDENCE_LATEST.md",
            "source_root": targeted_gap_external.get("source_root"),
            "download_summary": targeted_gap_external.get("summary", {}).get("lane_counts"),
            "decisions": targeted_gap_external.get("summary", {}).get("decisions"),
            "boundary": targeted_gap_external.get("boundary"),
        },
        "non_slavic_targeted_gap_source_integration_supplement_20260629": {
            "json": "logs/NON_SLAVIC_TARGETED_GAP_SOURCE_INTEGRATION_SUPPLEMENT_20260629.json",
            "markdown": "logs/NON_SLAVIC_TARGETED_GAP_SOURCE_INTEGRATION_SUPPLEMENT_20260629.md",
            "status": targeted_gap_supplement.get("status"),
            "remaining_gaps": targeted_gap_supplement.get("remaining_gaps"),
        },
        "slavic_maintenance_watchdog": {
            "json": "logs/SLAVIC_MAINTENANCE_WATCHDOG_20260628.json",
            "markdown": "logs/SLAVIC_MAINTENANCE_WATCHDOG_20260628.md",
            "decision": watchdog.get("decision"),
            "zenodo_change_detected": watchdog.get("zenodo", {}).get("change_detected"),
            "external_review_returns": watchdog.get("external_review_returns", {}),
            "slavic_package_validation": watchdog.get("slavic_package", {}).get("validation", {}),
            "review_bundle_validation": watchdog.get("review_bundle", {}).get("validation", {}),
        },
        "interlanguage_methodology_note": {
            "json": "logs/INTERLANGUAGE_METHODOLOGY_AND_OPEN_SOURCE_EDUCATION_NOTE_20260628.json",
            "markdown": "logs/INTERLANGUAGE_METHODOLOGY_AND_OPEN_SOURCE_EDUCATION_NOTE_20260628.md",
            "category_count": len(interlanguage.get("categories", [])),
            "source_note_count": len(interlanguage.get("source_notes", [])),
        },
        "interlanguage_candidate_matrix": {
            "json": "logs/INTERLANGUAGE_CANDIDATE_MATRIX_20260628.json",
            "markdown": "logs/INTERLANGUAGE_CANDIDATE_MATRIX_20260628.md",
            "publication_section_draft": "logs/INTERLANGUAGE_PUBLICATION_SECTION_DRAFT_20260628.md",
            "candidate_count": len(interlanguage_matrix.get("candidates", []))
            if isinstance(interlanguage_matrix.get("candidates"), list)
            else None,
            "recommended_next_comparator": interlanguage_matrix.get("recommended_next_comparator"),
        },
        "world_family_interlanguage_construction_lane": {
            "matrix_json": "logs/INTERLANGUAGE_CANDIDATE_MATRIX_20260628T213951Z_WORLD_FAMILY_CONSTRUCTION.json",
            "matrix_markdown": "logs/INTERLANGUAGE_CANDIDATE_MATRIX_20260628T213951Z_WORLD_FAMILY_CONSTRUCTION.md",
            "publication_section_draft": (
                "logs/INTERLANGUAGE_PUBLICATION_SECTION_DRAFT_20260628T213951Z_WORLD_FAMILY_CONSTRUCTION.md"
            ),
            "coordination_index_json": "logs/WORLD_FAMILY_INTERLANGUAGE_COORDINATION_INDEX_20260628T214958Z.json",
            "coordination_index_markdown": "logs/WORLD_FAMILY_INTERLANGUAGE_COORDINATION_INDEX_20260628T214958Z.md",
            "actionable_roadmap_json": "logs/WORLD_FAMILY_TECHNICAL_BRIDGE_ACTIONABLE_ROADMAP_20260628T215240Z.json",
            "actionable_roadmap_markdown": "logs/WORLD_FAMILY_TECHNICAL_BRIDGE_ACTIONABLE_ROADMAP_20260628T215240Z.md",
            "missing_region_gap_audit_json": "logs/WORLD_FAMILY_MISSING_REGION_GAP_AUDIT_20260628T215240Z.json",
            "missing_region_gap_audit_markdown": "logs/WORLD_FAMILY_MISSING_REGION_GAP_AUDIT_20260628T215240Z.md",
            "coverage_closure_audit_json": "logs/WORLD_FAMILY_COVERAGE_CLOSURE_AUDIT_20260629T015305Z.json",
            "coverage_closure_audit_markdown": "logs/WORLD_FAMILY_COVERAGE_CLOSURE_AUDIT_20260629T015305Z.md",
            "least_served_reader_legibility_policy_json": (
                "logs/WORLD_FAMILY_LEAST_SERVED_READER_LEGIBILITY_POLICY_20260629T015305Z.json"
            ),
            "least_served_reader_legibility_policy_markdown": (
                "logs/WORLD_FAMILY_LEAST_SERVED_READER_LEGIBILITY_POLICY_20260629T015305Z.md"
            ),
            "optimal_access_research_note_json": (
                "logs/WORLD_FAMILY_OPTIMAL_ACCESS_RESEARCH_NOTE_20260629T020750Z.json"
            ),
            "optimal_access_research_note_markdown": (
                "logs/WORLD_FAMILY_OPTIMAL_ACCESS_RESEARCH_NOTE_20260629T020750Z.md"
            ),
            "construction_targets_json": "logs/WORLD_FAMILY_BRIDGE_REGISTER_CONSTRUCTION_TARGETS_20260628T221253Z.json",
            "construction_targets_markdown": "logs/WORLD_FAMILY_BRIDGE_REGISTER_CONSTRUCTION_TARGETS_20260628T221253Z.md",
            "dashboard_json": "logs/WORLD_FAMILY_BRIDGE_LANE_STATUS_DASHBOARD_20260628T215810Z.json",
            "dashboard_markdown": "logs/WORLD_FAMILY_BRIDGE_LANE_STATUS_DASHBOARD_20260628T215810Z.md",
            "handoff_prompts_json": "logs/WORLD_FAMILY_PARALLEL_HANDOFF_PROMPTS_20260628T215810Z.json",
            "handoff_prompts_markdown": "logs/WORLD_FAMILY_PARALLEL_HANDOFF_PROMPTS_20260628T215810Z.md",
            "live_dispatch_tracker_json": "logs/WORLD_FAMILY_LIVE_DISPATCH_TRACKER_20260628T220603Z.json",
            "live_dispatch_tracker_markdown": "logs/WORLD_FAMILY_LIVE_DISPATCH_TRACKER_20260628T220603Z.md",
            "goal_completion_audit_json": "logs/WORLD_FAMILY_GOAL_COMPLETION_AUDIT_20260628T220603Z.json",
            "goal_completion_audit_markdown": "logs/WORLD_FAMILY_GOAL_COMPLETION_AUDIT_20260628T220603Z.md",
            "arabic_script_non_erasure_guardrail_json": "logs/ARABIC_SCRIPT_NON_ERASURE_GUARDRAIL_20260629.json",
            "arabic_script_non_erasure_guardrail_markdown": "logs/ARABIC_SCRIPT_NON_ERASURE_GUARDRAIL_20260629.md",
            "matrix_status": world_family_matrix.get("status"),
            "coordination_status": world_family_index.get("status"),
            "roadmap_status": world_family_roadmap.get("status"),
            "gap_audit_status": world_family_gap_audit.get("status"),
            "coverage_closure_status": world_family_coverage_closure.get("status"),
            "least_served_policy_status": world_family_least_served.get("status"),
            "optimal_access_note_status": world_family_optimal_access.get("status"),
            "construction_targets_status": world_family_targets.get("status"),
            "dashboard_status": world_family_dashboard.get("status"),
            "handoff_prompt_count": len(world_family_handoff.get("prompts", []))
            if isinstance(world_family_handoff.get("prompts"), list)
            else None,
            "live_dispatch_count": len(world_family_live_tracker.get("dispatch", []))
            if isinstance(world_family_live_tracker.get("dispatch"), list)
            else None,
            "goal_audit_status": world_family_goal_audit.get("status"),
            "all_dashboard_lanes_pilot_ready": all(
                lane.get("pilot_ready") is True for lane in world_family_dashboard.get("lanes", [])
            )
            if isinstance(world_family_dashboard.get("lanes"), list)
            else False,
            "arabic_script_guardrail_status": arabic_script_guardrail.get("status"),
        },
        "world_family_current_construction_decisions": {
            "pan_romance_json": "logs/PAN_ROMANCE_TECHNICAL_BRIDGE_CONSTRUCTION_DECISIONS_20260628T221717Z.json",
            "pan_romance_markdown": "logs/PAN_ROMANCE_TECHNICAL_BRIDGE_CONSTRUCTION_DECISIONS_20260628T221717Z.md",
            "pan_romance_status": pan_romance_decisions.get("status"),
            "pan_romance_pilot_ready": pan_romance_decisions.get("pilot_ready"),
            "controlled_arabic_json": "logs/CONTROLLED_ARABIC_TECHNICAL_REGISTER_DECISIONS_20260628T222119Z.json",
            "controlled_arabic_markdown": "logs/CONTROLLED_ARABIC_TECHNICAL_REGISTER_DECISIONS_20260628T222119Z.md",
            "controlled_arabic_status": controlled_arabic_decisions.get("status"),
            "controlled_arabic_pilot_ready": controlled_arabic_decisions.get("pilot_ready"),
            "persianate_json": "logs/PERSIANATE_SCRIPT_AND_STANDARD_POLICY_20260628T222119Z.json",
            "persianate_markdown": "logs/PERSIANATE_SCRIPT_AND_STANDARD_POLICY_20260628T222119Z.md",
            "persianate_status": persianate_decisions.get("status"),
            "persianate_pilot_ready": persianate_decisions.get("pilot_ready"),
            "shared_boundary": "construction decisions only; no translation pilot-ready claim",
        },
        "latest_zenodo_source_freshness": {
            "summary_json": "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260701T222409Z.json",
            "summary_markdown": "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260701T222409Z.md",
            "latest_snapshot": latest_zenodo.get("latest_snapshot"),
            "current_alias_snapshot": (
                "sources/zenodo_updates/20260630_record20836874/"
                "zenodo_20836874_api_latest_20260701T222409Z.json"
            ),
            "current_20260629_alias_snapshot": (
                "sources/zenodo_updates/20260629_record20836874/"
                "zenodo_20836874_api_latest_20260629T_current.json"
            ),
            "checked_at_utc": latest_zenodo.get("checked_at_utc"),
            "no_source_replacement_required": latest_zenodo.get("no_source_replacement_required"),
            "file_count": latest_zenodo.get("file_count"),
            "added_files": latest_zenodo.get("added_files"),
            "removed_files": latest_zenodo.get("removed_files"),
            "size_changed_files": latest_zenodo.get("size_changed_files"),
            "checksum_changed_files": latest_zenodo.get("checksum_changed_files"),
        },
        "parallel_codex_handoff_prompts": {
            "json": "logs/PARALLEL_CODEX_HANDOFF_PROMPTS_20260628.json",
            "markdown": "logs/PARALLEL_CODEX_HANDOFF_PROMPTS_20260628.md",
            "recommended_parallel_task_count": len(prompts.get("recommended_parallel_tasks", [])),
        },
        "parallel_codex_local_drop_non_slavic_source_status": {
            "json": "logs/PARALLEL_CODEX_LOCAL_DROP_NON_SLAVIC_SOURCE_STATUS_20260628.json",
            "markdown": "logs/PARALLEL_CODEX_LOCAL_DROP_NON_SLAVIC_SOURCE_STATUS_20260628.md",
            "status": local_drop.get("status"),
            "claims_allowed": local_drop.get("claims_allowed"),
            "claims_not_allowed": local_drop.get("claims_not_allowed"),
        },
        "parallel_codex_world_family_coordination_check": {
            "json": "logs/PARALLEL_CODEX_OTHER_SESSION_COORDINATION_CHECK_20260629.json",
            "markdown": "logs/PARALLEL_CODEX_OTHER_SESSION_COORDINATION_CHECK_20260629.md",
            "status": other_session_check.get("status"),
            "checked_artifacts": other_session_check.get("checked_artifacts"),
            "review_decision": other_session_check.get("review_decision"),
        },
        "parallel_codex_local_drop_world_family_coordination": {
            "json": "logs/PARALLEL_CODEX_LOCAL_DROP_WORLD_FAMILY_COORDINATION_20260629.json",
            "markdown": "logs/PARALLEL_CODEX_LOCAL_DROP_WORLD_FAMILY_COORDINATION_20260629.md",
            "status": world_family_local_drop.get("status"),
            "read_first": world_family_local_drop.get("read_first"),
            "do_not_do": world_family_local_drop.get("do_not_do"),
        },
        "parallel_codex_local_drop_chinese_japanese": {
            "json": "logs/PARALLEL_CODEX_LOCAL_DROP_CHINESE_JAPANESE_20260629.json",
            "markdown": "logs/PARALLEL_CODEX_LOCAL_DROP_CHINESE_JAPANESE_20260629.md",
            "status": chinese_japanese_local_drop.get("status"),
            "read_first": chinese_japanese_local_drop.get("read_first"),
            "source_evidence_updates": chinese_japanese_local_drop.get("source_evidence_updates"),
            "do_not_claim": chinese_japanese_local_drop.get("do_not_claim"),
            "next_useful_work": chinese_japanese_local_drop.get("next_useful_work"),
        },
        "checkpoint_package": package_record,
        "checkpoint_validation": {
            "validation_json": rel(VALIDATION_PATH),
            "overall_pass": validation["overall_pass"],
            "credential_scan_hits": validation["credential_scan_hits"],
            "required_missing": validation["required_missing"],
        },
    }
    for relative in ["status.json", "MANIFEST_SUMMARY.json"]:
        path = ROOT / relative
        data = read_json(relative)
        data["updated_at_utc"] = package_record["recorded_at_utc"]
        data["latest_language_planning_source_evidence_checkpoint"] = summary
        write_json(relative, data)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    files = collect_files()
    relative_files = [rel(path) for path in files]
    missing = [relative for relative in REQUIRED_RELATIVE_FILES if not (ROOT / relative).is_file()]
    credential_hits = scan_credentials(files)
    if credential_hits:
        raise RuntimeError(f"credential-like material selected for checkpoint: {credential_hits}")
    if ZIP_PATH.exists():
        ZIP_PATH.unlink()
    with zipfile.ZipFile(ZIP_PATH, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        zf.writestr(
            f"{PACKAGE_ID}/CHECKPOINT_MANIFEST.json",
            json.dumps(
                {
                    "package_id": PACKAGE_ID,
                    "generated_at_utc": NOW.replace(microsecond=0).isoformat().replace("+00:00", "Z"),
                    "scope": "Language-planning, non-Slavic source-evidence, interlanguage methodology, and parallel-Codex handoff prompts.",
                    "files": relative_files,
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
        )
        for path in files:
            zf.write(path, f"{PACKAGE_ID}/{rel(path)}")
    with zipfile.ZipFile(ZIP_PATH, "r") as zf:
        bad_file = zf.testzip()
        entry_count = len(zf.infolist())
    sha = sha256_file(ZIP_PATH)
    SHA_PATH.write_text(f"{sha}  {ZIP_PATH.name}\n", encoding="ascii")
    validation = {
        "package_id": PACKAGE_ID,
        "generated_at_utc": NOW.replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "zip": rel(ZIP_PATH),
        "zip_bytes": ZIP_PATH.stat().st_size,
        "sha256": sha,
        "sha256_file": rel(SHA_PATH),
        "validation_json": rel(VALIDATION_PATH),
        "zip_test_bad_file": bad_file,
        "zip_entry_count": entry_count,
        "selected_file_count": len(files),
        "required_missing": missing,
        "credential_scan_hits": credential_hits,
        "overall_pass": bad_file is None and not missing and not credential_hits,
    }
    VALIDATION_PATH.write_text(json.dumps(validation, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    package_record = {
        "recorded_at_utc": validation["generated_at_utc"],
        "package_id": PACKAGE_ID,
        "zip": validation["zip"],
        "sha256": sha,
        "sha256_file": validation["sha256_file"],
        "validation_json": validation["validation_json"],
        "zip_bytes": validation["zip_bytes"],
        "zip_entry_count": entry_count,
        "selected_file_count": len(files),
    }
    update_status(package_record, validation)
    print(json.dumps({**package_record, "overall_pass": validation["overall_pass"]}, ensure_ascii=True, indent=2))


if __name__ == "__main__":
    main()

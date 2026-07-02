import base64
import json
import subprocess
import time
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
REPO = "KokunoYumeto/modern-latex-manuscripts"
BRANCH = "codex/laptop-noether-language-planning-20260701"
DEST_ROOT = "workflow/codex-laptop-handoffs/20260701T223800Z"

LOCAL_TO_REMOTE = {
    "logs/POST_CHECKPOINT_GITHUB_HANDOFF_20260701T223800Z.md": f"{DEST_ROOT}/POST_CHECKPOINT_GITHUB_HANDOFF_20260701T223800Z.md",
    "logs/POST_CHECKPOINT_GITHUB_HANDOFF_20260701T223800Z.json": f"{DEST_ROOT}/POST_CHECKPOINT_GITHUB_HANDOFF_20260701T223800Z.json",
    "logs/WORKFLOW_LOG.md": f"{DEST_ROOT}/WORKFLOW_LOG.md",
    "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260701T222409Z.md": f"{DEST_ROOT}/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260701T222409Z.md",
    "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260701T222409Z.json": f"{DEST_ROOT}/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260701T222409Z.json",
    "packages/Noether_LanguagePlanning_SourceEvidence_Checkpoint_20260701T222757Z.zip.sha256": f"{DEST_ROOT}/Noether_LanguagePlanning_SourceEvidence_Checkpoint_20260701T222757Z.zip.sha256",
    "packages/Noether_LanguagePlanning_SourceEvidence_Checkpoint_20260701T222757Z.zip.validation.json": f"{DEST_ROOT}/Noether_LanguagePlanning_SourceEvidence_Checkpoint_20260701T222757Z.zip.validation.json",
    "packages/Noether_LanguagePlanning_SourceEvidence_Checkpoint_20260701T222757Z.zip.independent_validation.json": f"{DEST_ROOT}/Noether_LanguagePlanning_SourceEvidence_Checkpoint_20260701T222757Z.zip.independent_validation.json",
    "tmp/build_post_checkpoint_github_handoff_20260701.py": f"{DEST_ROOT}/build_post_checkpoint_github_handoff_20260701.py",
    "logs/CROSS_LANE_PROMOTION_READINESS_AUDIT_20260702T003500Z.md": f"{DEST_ROOT}/CROSS_LANE_PROMOTION_READINESS_AUDIT_20260702T003500Z.md",
    "logs/CROSS_LANE_PROMOTION_READINESS_AUDIT_20260702T003500Z.json": f"{DEST_ROOT}/CROSS_LANE_PROMOTION_READINESS_AUDIT_20260702T003500Z.json",
    "tmp/build_cross_lane_promotion_readiness_audit_20260702.py": f"{DEST_ROOT}/build_cross_lane_promotion_readiness_audit_20260702.py",
    "logs/REVIEW_CORRECTION_INTAKE_LEDGER_20260702T005500Z.md": f"{DEST_ROOT}/REVIEW_CORRECTION_INTAKE_LEDGER_20260702T005500Z.md",
    "logs/REVIEW_CORRECTION_INTAKE_LEDGER_20260702T005500Z.json": f"{DEST_ROOT}/REVIEW_CORRECTION_INTAKE_LEDGER_20260702T005500Z.json",
    "tmp/build_review_correction_intake_ledger_20260702.py": f"{DEST_ROOT}/build_review_correction_intake_ledger_20260702.py",
    "logs/VISUAL_INSPECTION_COVERAGE_LEDGER_20260702T011500Z.md": f"{DEST_ROOT}/VISUAL_INSPECTION_COVERAGE_LEDGER_20260702T011500Z.md",
    "logs/VISUAL_INSPECTION_COVERAGE_LEDGER_20260702T011500Z.json": f"{DEST_ROOT}/VISUAL_INSPECTION_COVERAGE_LEDGER_20260702T011500Z.json",
    "tmp/build_visual_inspection_coverage_ledger_20260702.py": f"{DEST_ROOT}/build_visual_inspection_coverage_ledger_20260702.py",
    "logs/SIMPLIFIED_CHINESE_VISUAL_QUEUE_CONTACT_SHEET_20260702T013500Z.md": f"{DEST_ROOT}/SIMPLIFIED_CHINESE_VISUAL_QUEUE_CONTACT_SHEET_20260702T013500Z.md",
    "logs/SIMPLIFIED_CHINESE_VISUAL_QUEUE_CONTACT_SHEET_20260702T013500Z.json": f"{DEST_ROOT}/SIMPLIFIED_CHINESE_VISUAL_QUEUE_CONTACT_SHEET_20260702T013500Z.json",
    "logs/SIMPLIFIED_CHINESE_VISUAL_QUEUE_TRIAGE_20260702T014500Z.md": f"{DEST_ROOT}/SIMPLIFIED_CHINESE_VISUAL_QUEUE_TRIAGE_20260702T014500Z.md",
    "logs/SIMPLIFIED_CHINESE_VISUAL_QUEUE_TRIAGE_20260702T014500Z.json": f"{DEST_ROOT}/SIMPLIFIED_CHINESE_VISUAL_QUEUE_TRIAGE_20260702T014500Z.json",
    "tmp/build_simplified_chinese_visual_queue_contact_sheet_20260702.py": f"{DEST_ROOT}/build_simplified_chinese_visual_queue_contact_sheet_20260702.py",
    "visual_inspection/simplified_chinese_visual_queue_20260702T013500Z/simplified_chinese_visual_queue_contact_sheet_page001.png": f"{DEST_ROOT}/simplified_chinese_visual_queue_contact_sheet_page001.png",
    "logs/VISUAL_TRIAGE_INTEGRATION_STATUS_20260702T020000Z.md": f"{DEST_ROOT}/VISUAL_TRIAGE_INTEGRATION_STATUS_20260702T020000Z.md",
    "logs/VISUAL_TRIAGE_INTEGRATION_STATUS_20260702T020000Z.json": f"{DEST_ROOT}/VISUAL_TRIAGE_INTEGRATION_STATUS_20260702T020000Z.json",
    "tmp/build_visual_triage_integration_status_20260702.py": f"{DEST_ROOT}/build_visual_triage_integration_status_20260702.py",
    "logs/LAST_DAY_REDO_REPRODUCIBILITY_AUDIT_20260702T005153Z.md": f"{DEST_ROOT}/LAST_DAY_REDO_REPRODUCIBILITY_AUDIT_20260702T005153Z.md",
    "logs/LAST_DAY_REDO_REPRODUCIBILITY_AUDIT_20260702T005153Z.json": f"{DEST_ROOT}/LAST_DAY_REDO_REPRODUCIBILITY_AUDIT_20260702T005153Z.json",
    "tmp/redo_last_day_reproducibility_audit_20260702.py": f"{DEST_ROOT}/redo_last_day_reproducibility_audit_20260702.py",
    "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260702T005824Z.md": f"{DEST_ROOT}/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260702T005824Z.md",
    "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260702T005824Z.json": f"{DEST_ROOT}/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260702T005824Z.json",
    "sources/zenodo_updates/20260630_record20836874/zenodo_20836874_api_latest_20260702T005824Z.json": f"{DEST_ROOT}/zenodo_20836874_api_latest_20260702T005824Z.json",
    "packages/Noether_LanguagePlanning_SourceEvidence_Checkpoint_20260702T010851Z.zip.sha256": f"{DEST_ROOT}/Noether_LanguagePlanning_SourceEvidence_Checkpoint_20260702T010851Z.zip.sha256",
    "packages/Noether_LanguagePlanning_SourceEvidence_Checkpoint_20260702T010851Z.zip.validation.json": f"{DEST_ROOT}/Noether_LanguagePlanning_SourceEvidence_Checkpoint_20260702T010851Z.zip.validation.json",
    "packages/Noether_LanguagePlanning_SourceEvidence_Checkpoint_20260702T010851Z.zip.independent_validation.json": f"{DEST_ROOT}/Noether_LanguagePlanning_SourceEvidence_Checkpoint_20260702T010851Z.zip.independent_validation.json",
    "logs/LAST_DAY_REDO_CHECKPOINT_20260702T011000Z.md": f"{DEST_ROOT}/LAST_DAY_REDO_CHECKPOINT_20260702T011000Z.md",
    "logs/LAST_DAY_REDO_CHECKPOINT_20260702T011000Z.json": f"{DEST_ROOT}/LAST_DAY_REDO_CHECKPOINT_20260702T011000Z.json",
    "tmp/build_last_day_redo_checkpoint_20260702.py": f"{DEST_ROOT}/build_last_day_redo_checkpoint_20260702.py",
    "logs/POST_REDO_FINAL_HANDOFF_20260702T011800Z.md": f"{DEST_ROOT}/POST_REDO_FINAL_HANDOFF_20260702T011800Z.md",
    "logs/POST_REDO_FINAL_HANDOFF_20260702T011800Z.json": f"{DEST_ROOT}/POST_REDO_FINAL_HANDOFF_20260702T011800Z.json",
    "tmp/build_post_redo_final_handoff_20260702.py": f"{DEST_ROOT}/build_post_redo_final_handoff_20260702.py",
    "logs/CONTROLLED_ARABIC_ALGEBRA_SOURCE_REFRESH_20260702T013000Z.md": f"{DEST_ROOT}/CONTROLLED_ARABIC_ALGEBRA_SOURCE_REFRESH_20260702T013000Z.md",
    "logs/CONTROLLED_ARABIC_ALGEBRA_SOURCE_REFRESH_20260702T013000Z.json": f"{DEST_ROOT}/CONTROLLED_ARABIC_ALGEBRA_SOURCE_REFRESH_20260702T013000Z.json",
    "tmp/build_controlled_arabic_algebra_source_refresh_20260702.py": f"{DEST_ROOT}/build_controlled_arabic_algebra_source_refresh_20260702.py",
    "logs/ARABIC_PERSIANATE_LANE_STATUS_MANIFEST_20260702T014000Z.md": f"{DEST_ROOT}/ARABIC_PERSIANATE_LANE_STATUS_MANIFEST_20260702T014000Z.md",
    "logs/ARABIC_PERSIANATE_LANE_STATUS_MANIFEST_20260702T014000Z.json": f"{DEST_ROOT}/ARABIC_PERSIANATE_LANE_STATUS_MANIFEST_20260702T014000Z.json",
    "tmp/build_arabic_persianate_lane_status_manifest_20260702.py": f"{DEST_ROOT}/build_arabic_persianate_lane_status_manifest_20260702.py",
    "logs/LAST_DAY_REDO_REPRODUCIBILITY_AUDIT_20260702T015853Z.md": f"{DEST_ROOT}/LAST_DAY_REDO_REPRODUCIBILITY_AUDIT_20260702T015853Z.md",
    "logs/LAST_DAY_REDO_REPRODUCIBILITY_AUDIT_20260702T015853Z.json": f"{DEST_ROOT}/LAST_DAY_REDO_REPRODUCIBILITY_AUDIT_20260702T015853Z.json",
    "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260702T020816Z.md": f"{DEST_ROOT}/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260702T020816Z.md",
    "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260702T020816Z.json": f"{DEST_ROOT}/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260702T020816Z.json",
    "sources/zenodo_updates/20260630_record20836874/zenodo_20836874_api_latest_20260702T020816Z.json": f"{DEST_ROOT}/zenodo_20836874_api_latest_20260702T020816Z.json",
    "packages/Noether_LanguagePlanning_SourceEvidence_Checkpoint_20260702T020954Z.zip.sha256": f"{DEST_ROOT}/Noether_LanguagePlanning_SourceEvidence_Checkpoint_20260702T020954Z.zip.sha256",
    "packages/Noether_LanguagePlanning_SourceEvidence_Checkpoint_20260702T020954Z.zip.validation.json": f"{DEST_ROOT}/Noether_LanguagePlanning_SourceEvidence_Checkpoint_20260702T020954Z.zip.validation.json",
    "packages/Noether_LanguagePlanning_SourceEvidence_Checkpoint_20260702T020954Z.zip.independent_validation.json": f"{DEST_ROOT}/Noether_LanguagePlanning_SourceEvidence_Checkpoint_20260702T020954Z.zip.independent_validation.json",
    "logs/FULL_REDO_AFTER_MODE_RESET_CHECKPOINT_20260702T022209Z.md": f"{DEST_ROOT}/FULL_REDO_AFTER_MODE_RESET_CHECKPOINT_20260702T022209Z.md",
    "logs/FULL_REDO_AFTER_MODE_RESET_CHECKPOINT_20260702T022209Z.json": f"{DEST_ROOT}/FULL_REDO_AFTER_MODE_RESET_CHECKPOINT_20260702T022209Z.json",
    "tmp/build_full_redo_after_mode_reset_checkpoint_20260702.py": f"{DEST_ROOT}/build_full_redo_after_mode_reset_checkpoint_20260702.py",
    "logs/FULL_REDO_AFTER_MODE_RESET_PUBLISH_VERIFICATION_20260702T025500Z.md": f"{DEST_ROOT}/FULL_REDO_AFTER_MODE_RESET_PUBLISH_VERIFICATION_20260702T025500Z.md",
    "logs/FULL_REDO_AFTER_MODE_RESET_PUBLISH_VERIFICATION_20260702T025500Z.json": f"{DEST_ROOT}/FULL_REDO_AFTER_MODE_RESET_PUBLISH_VERIFICATION_20260702T025500Z.json",
    "tmp/build_full_redo_publish_verification_20260702.py": f"{DEST_ROOT}/build_full_redo_publish_verification_20260702.py",
    "logs/LOCAL_DISK_CLEANUP_SUPERSEDED_PACKAGES_20260702T030000Z.md": f"{DEST_ROOT}/LOCAL_DISK_CLEANUP_SUPERSEDED_PACKAGES_20260702T030000Z.md",
    "logs/LOCAL_DISK_CLEANUP_SUPERSEDED_PACKAGES_20260702T030000Z.json": f"{DEST_ROOT}/LOCAL_DISK_CLEANUP_SUPERSEDED_PACKAGES_20260702T030000Z.json",
    "tmp/package_language_planning_checkpoint_20260628.py": f"{DEST_ROOT}/package_language_planning_checkpoint_20260628.py",
    "tmp/validate_language_planning_checkpoint_20260630.py": f"{DEST_ROOT}/validate_language_planning_checkpoint_20260630.py",
    "tmp/publish_post_checkpoint_github_handoff_20260701.py": f"{DEST_ROOT}/publish_post_checkpoint_github_handoff_20260701.py",
}

DIRS_TO_REMOTE = {
    "sources/non_slavic_reference_corpus/20260702T013000Z_controlled_arabic_algebra_source_refresh": f"{DEST_ROOT}/source_shelves/20260702T013000Z_controlled_arabic_algebra_source_refresh",
}


def gh_json(*args: str, check: bool = True):
    result = subprocess.run(["gh", "api", *args], text=True, encoding="utf-8", errors="replace", capture_output=True)
    if check and result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip())
    if result.returncode != 0 or not result.stdout.strip():
        return None
    return json.loads(result.stdout)


def gh(*args: str, input_text: str | None = None, check: bool = True):
    result = subprocess.run(
        ["gh", *args],
        text=True,
        encoding="utf-8",
        errors="replace",
        input=input_text,
        capture_output=True,
    )
    if check and result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip())
    return result


def ensure_branch() -> None:
    existing = gh_json(f"repos/{REPO}/git/ref/heads/{BRANCH}", check=False)
    if existing:
        return
    main = gh_json(f"repos/{REPO}/git/ref/heads/main")
    main_sha = main["object"]["sha"]
    gh(
        "api",
        f"repos/{REPO}/git/refs",
        "-X",
        "POST",
        "-f",
        f"ref=refs/heads/{BRANCH}",
        "-f",
        f"sha={main_sha}",
    )


def existing_file_sha(remote_path: str) -> str | None:
    data = gh_json(f"repos/{REPO}/contents/{remote_path}?ref={quote(BRANCH, safe='')}", check=False)
    if isinstance(data, dict):
        return data.get("sha")
    return None


def upload_file(local_rel: str, remote_path: str) -> None:
    local_path = ROOT / local_rel
    raw = local_path.read_bytes()
    encoded = base64.b64encode(raw).decode("ascii")
    message = f"Codex laptop handoff: update {remote_path}"
    last_error = None
    for attempt in range(1, 6):
        sha = existing_file_sha(remote_path)
        body = {
            "message": message,
            "branch": BRANCH,
            "content": encoded,
        }
        if sha:
            body["sha"] = sha
        try:
            gh(
                "api",
                f"repos/{REPO}/contents/{remote_path}",
                "-X",
                "PUT",
                "--input",
                "-",
                input_text=json.dumps(body),
            )
            return
        except RuntimeError as exc:
            last_error = exc
            text = str(exc)
            retryable = (
                '"sha" wasn' in text
                or "connection was forcibly closed" in text.lower()
                or "stream error" in text.lower()
                or "timeout" in text.lower()
                or "temporarily unavailable" in text.lower()
                or "502" in text
                or "503" in text
                or "504" in text
            )
            if not retryable or attempt == 5:
                raise
            time.sleep(2 * attempt)
    if last_error:
        raise last_error


def main() -> None:
    ensure_branch()
    uploaded_files = dict(LOCAL_TO_REMOTE)
    for local_rel, remote_path in LOCAL_TO_REMOTE.items():
        upload_file(local_rel, remote_path)
    for local_root_rel, remote_root in DIRS_TO_REMOTE.items():
        local_root = ROOT / local_root_rel
        for path in sorted(p for p in local_root.rglob("*") if p.is_file()):
            child_rel = path.relative_to(local_root).as_posix()
            local_rel = path.relative_to(ROOT).as_posix()
            remote_path = f"{remote_root}/{child_rel}"
            upload_file(local_rel, remote_path)
            uploaded_files[local_rel] = remote_path
    result = {
        "repo": REPO,
        "branch": BRANCH,
        "remote_root": DEST_ROOT,
        "uploaded_files": uploaded_files,
        "uploaded_dirs": DIRS_TO_REMOTE,
        "branch_url": f"https://github.com/{REPO}/tree/{BRANCH}/{DEST_ROOT}",
    }
    print(json.dumps(result, ensure_ascii=True, indent=2))


if __name__ == "__main__":
    main()

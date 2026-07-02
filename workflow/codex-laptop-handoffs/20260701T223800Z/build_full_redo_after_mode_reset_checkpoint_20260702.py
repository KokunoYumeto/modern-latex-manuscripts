import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STAMP = datetime.now(timezone.utc).replace(microsecond=0).strftime("%Y%m%dT%H%M%SZ")
OUT_JSON = ROOT / "logs" / f"FULL_REDO_AFTER_MODE_RESET_CHECKPOINT_{STAMP}.json"
OUT_MD = ROOT / "logs" / f"FULL_REDO_AFTER_MODE_RESET_CHECKPOINT_{STAMP}.md"


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT.resolve()).as_posix()


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def latest(pattern: str) -> Path:
    matches = sorted(ROOT.glob(pattern), key=lambda p: p.stat().st_mtime)
    if not matches:
        raise FileNotFoundError(pattern)
    return matches[-1]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def write_workflow_entry(payload: dict) -> None:
    workflow = ROOT / "logs" / "WORKFLOW_LOG.md"
    entry = [
        "",
        f"### {payload['generated_utc']} - Full redo after mode reset",
        "",
        "- Repaired and verified the local dependency lane after Windows/OpenAI reset behavior:",
        f"  - MiKTeX binary root: `{payload['dependency_repair']['miktex_bin']}`.",
        f"  - Portable Perl paths prepended for `latexmk`: `{payload['dependency_repair']['perl_bin']}` and `{payload['dependency_repair']['perl_c_bin']}`.",
        f"  - XeLaTeX smoke PDF: `{payload['dependency_repair']['smoke_pdf']}`.",
        "- Reran the previous-day local builders through the reproducibility audit:",
        f"  - Replay audit: `{payload['local_replay']['audit_json']}`.",
        f"  - Commands run/failed: `{payload['local_replay']['commands_run']}` / `{payload['local_replay']['commands_failed']}`.",
        "- Rechecked Zenodo live after the redo:",
        f"  - Check: `{payload['zenodo']['check_json']}`.",
        f"  - Record DOI `{payload['zenodo']['doi']}`, revision `{payload['zenodo']['revision']}`, modified `{payload['zenodo']['modified']}`.",
        f"  - Action: `{payload['zenodo']['action']}`; source replacement required: `{payload['zenodo']['source_replacement_required']}`.",
        "- Reran the July 2 Arabic/Persianate algebra-register refresh:",
        f"  - Refresh log: `{payload['arabic_refresh']['refresh_json']}`.",
        f"  - Downloaded/text-extracted: `{payload['arabic_refresh']['downloaded_count']}` / `{payload['arabic_refresh']['text_extracted_count']}`.",
        f"  - Strong direct invariant-theory witnesses remain `{payload['arabic_refresh']['strong_direct_invariant_theory_source_count']}`.",
        "- Patched the package builder/validator to include the July 2 Arabic algebra source shelf, rebuilt the checkpoint archive, and independently validated it:",
        f"  - ZIP: `{payload['package']['zip']}`.",
        f"  - Bytes: `{payload['package']['bytes']}`.",
        f"  - SHA256: `{payload['package']['sha256']}`.",
        f"  - Builder/independent validation: `{payload['package']['builder_pass']}` / `{payload['package']['independent_pass']}`.",
        "- Boundary: this is a reproducibility/source-evidence/package checkpoint, not a native-review closure, term-promotion closure, or completion of the active multilingual goal.",
        "",
    ]
    workflow.write_text(workflow.read_text(encoding="utf-8") + "\n".join(entry), encoding="utf-8")


def main() -> None:
    replay_path = latest("logs/LAST_DAY_REDO_REPRODUCIBILITY_AUDIT_20260702T*.json")
    zenodo_path = latest("logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260702T*.json")
    arabic_refresh_path = ROOT / "logs" / "CONTROLLED_ARABIC_ALGEBRA_SOURCE_REFRESH_20260702T013000Z.json"
    arabic_manifest_path = ROOT / "logs" / "ARABIC_PERSIANATE_LANE_STATUS_MANIFEST_20260702T014000Z.json"
    package_validation_path = latest("packages/Noether_LanguagePlanning_SourceEvidence_Checkpoint_20260702T*.zip.validation.json")
    package_independent_path = Path(str(package_validation_path).replace(".validation.json", ".independent_validation.json"))

    replay = load(replay_path)
    zenodo = load(zenodo_path)
    arabic = load(arabic_refresh_path)
    arabic_manifest = load(arabic_manifest_path)
    package_validation = load(package_validation_path)
    package_independent = load(package_independent_path)
    zip_path = ROOT / package_validation["zip"]
    smoke_pdf = ROOT / "tmp" / "dependency_smoke_out_20260702" / "dependency_smoke_test_20260701.pdf"

    payload = {
        "artifact": "full_redo_after_mode_reset_checkpoint",
        "generated_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "scope": (
            "Redo/revalidate previous-day Noether language-planning work after user-requested mode-reset redo, "
            "including dependency repair, builder replay, live Zenodo check, Arabic refresh rerun, package rebuild, "
            "and independent archive validation."
        ),
        "dependency_repair": {
            "status": "repaired_for_current_codex_process",
            "miktex_bin": "C:/Users/memo_/AppData/Local/Programs/MiKTeX/miktex/bin/x64",
            "perl_c_bin": "C:/Users/memo_/Documents/Codex/2026-06-09/could-you-look-online-for-me/work/noether-slavic-canonical/tools/strawberry-perl/strawberry-perl-5.42.2.1-64bit-portable/c/bin",
            "perl_bin": "C:/Users/memo_/Documents/Codex/2026-06-09/could-you-look-online-for-me/work/noether-slavic-canonical/tools/strawberry-perl/strawberry-perl-5.42.2.1-64bit-portable/perl/bin",
            "latexmk_version_checked": True,
            "xelatex_version_checked": True,
            "miktex_fndb_and_package_db_refreshed": True,
            "smoke_pdf": rel(smoke_pdf),
            "smoke_pdf_present": smoke_pdf.exists(),
            "smoke_pdf_sha256": sha256(smoke_pdf) if smoke_pdf.exists() else None,
            "note": "The user PATH already contained MiKTeX and portable Perl, but the running Codex process did not inherit them after reset; redo commands prepend both explicitly.",
        },
        "local_replay": {
            "audit_json": rel(replay_path),
            "audit_markdown": rel(replay_path.with_suffix(".md")),
            "commands_run": replay["summary"]["commands_run"],
            "commands_failed": replay["summary"]["commands_failed"],
            "watched_files_added": replay["summary"]["watched_files_added"],
            "watched_files_changed": replay["summary"]["watched_files_changed"],
            "watched_files_removed": replay["summary"]["watched_files_removed"],
        },
        "zenodo": {
            "check_json": rel(zenodo_path),
            "check_markdown": rel(zenodo_path.with_suffix(".md")),
            "doi": zenodo["doi"],
            "conceptdoi": zenodo["conceptdoi"],
            "revision": zenodo["revision"],
            "version": zenodo["version"],
            "modified": zenodo["modified"],
            "file_count": zenodo["file_count"],
            "action": zenodo["action"],
            "source_replacement_required": not zenodo["no_source_replacement_required"],
            "added_files": zenodo["added_files"],
            "removed_files": zenodo["removed_files"],
            "size_changed_files": zenodo["size_changed_files"],
            "checksum_changed_files": zenodo["checksum_changed_files"],
            "latest_snapshot": zenodo["latest_snapshot"],
        },
        "arabic_refresh": {
            "refresh_json": rel(arabic_refresh_path),
            "refresh_markdown": rel(arabic_refresh_path.with_suffix(".md")),
            "manifest_json": rel(arabic_manifest_path),
            "manifest_markdown": rel(arabic_manifest_path.with_suffix(".md")),
            "source_root": arabic["source_root"],
            "downloaded_count": arabic["summary"]["downloaded_count"],
            "text_extracted_count": arabic["summary"]["text_extracted_count"],
            "official_or_direct_algebra_register_count": arabic["summary"]["official_or_direct_algebra_register_count"],
            "direct_ring_or_rings_fields_count": arabic["summary"]["direct_ring_or_rings_fields_count"],
            "strong_direct_invariant_theory_source_count": arabic["summary"]["strong_direct_invariant_theory_source_count"],
            "decision": arabic["summary"]["decision"],
            "lane_status": arabic_manifest["status"],
        },
        "package": {
            "zip": package_validation["zip"],
            "bytes": package_validation["zip_bytes"],
            "sha256": package_validation["sha256"],
            "sha256_file": package_validation["sha256_file"],
            "builder_validation": rel(package_validation_path),
            "independent_validation": rel(package_independent_path),
            "zip_entry_count": package_validation["zip_entry_count"],
            "selected_file_count": package_validation["selected_file_count"],
            "builder_pass": package_validation["overall_pass"],
            "independent_pass": package_independent["overall_pass"],
            "sha256_matches": package_independent["sha256_matches"],
            "zip_test_bad_file": package_independent["zip_test_bad_file"],
            "builder_required_missing": package_validation["required_missing"],
            "builder_credential_scan_hits": package_validation["credential_scan_hits"],
            "validator_required_present_count": len(package_independent["required_present"]),
            "validator_required_missing_count": sum(1 for ok in package_independent["required_present"].values() if not ok),
        },
        "github_publish_target": {
            "repo": "KokunoYumeto/modern-latex-manuscripts",
            "branch": "codex/laptop-noether-language-planning-20260701",
            "handoff_root": "workflow/codex-laptop-handoffs/20260701T223800Z",
            "release_tag": "codex-laptop-noether-language-planning-20260702T020954Z",
        },
        "decision": {
            "redo_checkpoint_passed": (
                replay["summary"]["commands_failed"] == 0
                and zenodo["no_source_replacement_required"]
                and package_validation["overall_pass"]
                and package_independent["overall_pass"]
                and not package_validation["credential_scan_hits"]
            ),
            "promotion_claim_added": False,
            "active_goal_complete": False,
        },
        "boundary": (
            "This checkpoint verifies reproducibility and packaging after reset. It does not assert final native-review "
            "quality for any language lane and does not close the active multilingual canonical-edition goal."
        ),
    }

    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Full Redo After Mode Reset Checkpoint",
        "",
        f"Generated UTC: `{payload['generated_utc']}`",
        "",
        "## Result",
        "",
        f"- Redo checkpoint passed: `{payload['decision']['redo_checkpoint_passed']}`",
        f"- Local replay commands failed: `{payload['local_replay']['commands_failed']}`",
        f"- Zenodo action: `{payload['zenodo']['action']}`",
        f"- Zenodo revision/version: `{payload['zenodo']['revision']}` / `{payload['zenodo']['version']}`",
        f"- Arabic refresh decision: `{payload['arabic_refresh']['decision']}`",
        f"- Package: `{payload['package']['zip']}`",
        f"- Package SHA256: `{payload['package']['sha256']}`",
        f"- Builder/independent validation: `{payload['package']['builder_pass']}` / `{payload['package']['independent_pass']}`",
        "",
        "## Dependency Repair",
        "",
        f"- MiKTeX bin: `{payload['dependency_repair']['miktex_bin']}`",
        f"- Smoke PDF: `{payload['dependency_repair']['smoke_pdf']}`",
        f"- Smoke PDF present: `{payload['dependency_repair']['smoke_pdf_present']}`",
        "",
        "## Publish Target",
        "",
        f"- Branch: `{payload['github_publish_target']['branch']}`",
        f"- Handoff root: `{payload['github_publish_target']['handoff_root']}`",
        f"- Release tag: `{payload['github_publish_target']['release_tag']}`",
        "",
        "## Boundary",
        "",
        payload["boundary"],
        "",
    ]
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")
    write_workflow_entry(payload)
    print(json.dumps({"json": rel(OUT_JSON), "markdown": rel(OUT_MD), "passed": payload["decision"]["redo_checkpoint_passed"]}, indent=2))
    if not payload["decision"]["redo_checkpoint_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

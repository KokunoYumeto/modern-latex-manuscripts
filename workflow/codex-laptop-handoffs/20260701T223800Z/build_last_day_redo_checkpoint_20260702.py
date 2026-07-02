import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STAMP = "20260702T011000Z"
OUT_JSON = ROOT / "logs" / f"LAST_DAY_REDO_CHECKPOINT_{STAMP}.json"
OUT_MD = ROOT / "logs" / f"LAST_DAY_REDO_CHECKPOINT_{STAMP}.md"

LOCAL_REPLAY = ROOT / "logs" / "LAST_DAY_REDO_REPRODUCIBILITY_AUDIT_20260702T005153Z.json"
ZENODO_CHECK = ROOT / "logs" / "ZENODO_NOETHER_LATEST_LIVE_CHECK_20260702T005824Z.json"
PACKAGE_VALIDATION = ROOT / "packages" / "Noether_LanguagePlanning_SourceEvidence_Checkpoint_20260702T005841Z.zip.validation.json"
PACKAGE_INDEPENDENT = ROOT / "packages" / "Noether_LanguagePlanning_SourceEvidence_Checkpoint_20260702T005841Z.zip.independent_validation.json"


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT.resolve()).as_posix()


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def main() -> None:
    replay = load(LOCAL_REPLAY)
    zenodo = load(ZENODO_CHECK)
    package_validation = load(PACKAGE_VALIDATION)
    package_independent = load(PACKAGE_INDEPENDENT)
    payload = {
        "artifact": "last_day_redo_checkpoint",
        "generated_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "scope": "Redo and revalidation of the previous day's Noether language-planning artifacts after model/mode concern.",
        "inputs": {
            "local_replay_audit": rel(LOCAL_REPLAY),
            "fresh_zenodo_check": rel(ZENODO_CHECK),
            "package_builder_validation": rel(PACKAGE_VALIDATION),
            "package_independent_validation": rel(PACKAGE_INDEPENDENT),
        },
        "results": {
            "local_replay_commands_run": replay["summary"]["commands_run"],
            "local_replay_commands_failed": replay["summary"]["commands_failed"],
            "fresh_zenodo_action": zenodo["action"],
            "fresh_zenodo_no_source_replacement_required": zenodo["no_source_replacement_required"],
            "fresh_zenodo_revision": zenodo["revision"],
            "fresh_zenodo_file_count": zenodo["file_count"],
            "new_package_zip": package_validation["zip"],
            "new_package_bytes": package_validation["zip_bytes"],
            "new_package_sha256": package_validation["sha256"],
            "builder_validation_pass": package_validation["overall_pass"],
            "builder_required_missing_count": len(package_validation["required_missing"]),
            "builder_credential_scan_hit_count": len(package_validation["credential_scan_hits"]),
            "independent_validation_pass": package_independent["overall_pass"],
            "independent_sha256_matches": package_independent["sha256_matches"],
            "independent_zip_test_bad_file": package_independent["zip_test_bad_file"],
            "independent_entry_count": package_independent["entry_count"],
        },
        "visual_replay_note": (
            "The redo found and fixed an idempotency bug: once the Simplified Chinese contact-sheet evidence "
            "exists, the visual coverage ledger has zero queued Simplified Chinese PDFs. The contact-sheet and "
            "integration builders now preserve/reconcile the existing first-page triage instead of failing."
        ),
        "decision": {
            "redo_checkpoint_passed": (
                replay["summary"]["commands_failed"] == 0
                and zenodo["no_source_replacement_required"]
                and package_validation["overall_pass"]
                and package_independent["overall_pass"]
            ),
            "source_replacement_required": not zenodo["no_source_replacement_required"],
            "promotion_claim_added": False,
        },
        "boundary": (
            "This redo validates and refreshes the handoff/package layer. It does not convert local cumulative "
            "baselines into public/native-reviewed final editions and does not close external review gates."
        ),
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Last-day redo checkpoint",
        "",
        f"Generated UTC: `{payload['generated_utc']}`",
        "",
        "## Result",
        "",
        f"- Redo checkpoint passed: `{payload['decision']['redo_checkpoint_passed']}`",
        f"- Local replay commands: `{payload['results']['local_replay_commands_run']}`",
        f"- Local replay failures: `{payload['results']['local_replay_commands_failed']}`",
        f"- Fresh Zenodo action: `{payload['results']['fresh_zenodo_action']}`",
        f"- New package: `{payload['results']['new_package_zip']}`",
        f"- New package bytes: `{payload['results']['new_package_bytes']}`",
        f"- New package SHA256: `{payload['results']['new_package_sha256']}`",
        f"- Builder validation pass: `{payload['results']['builder_validation_pass']}`",
        f"- Independent validation pass: `{payload['results']['independent_validation_pass']}`",
        "",
        "## Visual Replay Note",
        "",
        payload["visual_replay_note"],
        "",
        "## Inputs",
        "",
    ]
    for key, value in payload["inputs"].items():
        lines.append(f"- {key}: `{value}`")
    lines.extend(["", "## Boundary", "", payload["boundary"], ""])
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({"json": rel(OUT_JSON), "markdown": rel(OUT_MD), "passed": payload["decision"]["redo_checkpoint_passed"]}, indent=2))
    if not payload["decision"]["redo_checkpoint_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

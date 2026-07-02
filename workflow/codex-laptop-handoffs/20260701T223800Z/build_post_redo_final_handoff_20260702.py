import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STAMP = "20260702T011800Z"
OUT_JSON = ROOT / "logs" / f"POST_REDO_FINAL_HANDOFF_{STAMP}.json"
OUT_MD = ROOT / "logs" / f"POST_REDO_FINAL_HANDOFF_{STAMP}.md"

PACKAGE_VALIDATION = ROOT / "packages" / "Noether_LanguagePlanning_SourceEvidence_Checkpoint_20260702T010851Z.zip.validation.json"
PACKAGE_INDEPENDENT = ROOT / "packages" / "Noether_LanguagePlanning_SourceEvidence_Checkpoint_20260702T010851Z.zip.independent_validation.json"
REDO_CHECKPOINT = ROOT / "logs" / "LAST_DAY_REDO_CHECKPOINT_20260702T011000Z.json"
LOCAL_REPLAY = ROOT / "logs" / "LAST_DAY_REDO_REPRODUCIBILITY_AUDIT_20260702T005153Z.json"
ZENODO_CHECK = ROOT / "logs" / "ZENODO_NOETHER_LATEST_LIVE_CHECK_20260702T005824Z.json"


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT.resolve()).as_posix()


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def main() -> None:
    package_validation = load(PACKAGE_VALIDATION)
    package_independent = load(PACKAGE_INDEPENDENT)
    redo = load(REDO_CHECKPOINT)
    replay = load(LOCAL_REPLAY)
    zenodo = load(ZENODO_CHECK)
    payload = {
        "artifact": "post_redo_final_handoff",
        "generated_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "purpose": "Final sidecar for the post-redo package; intentionally outside the zip to avoid self-reference.",
        "final_package": {
            "zip": package_validation["zip"],
            "bytes": package_validation["zip_bytes"],
            "sha256": package_validation["sha256"],
            "builder_validation": rel(PACKAGE_VALIDATION),
            "independent_validation": rel(PACKAGE_INDEPENDENT),
            "builder_pass": package_validation["overall_pass"],
            "independent_pass": package_independent["overall_pass"],
            "sha256_matches": package_independent["sha256_matches"],
            "zip_test_bad_file": package_independent["zip_test_bad_file"],
        },
        "redo_summary": {
            "redo_checkpoint": rel(REDO_CHECKPOINT),
            "redo_checkpoint_passed": redo["decision"]["redo_checkpoint_passed"],
            "local_replay": rel(LOCAL_REPLAY),
            "local_replay_commands_run": replay["summary"]["commands_run"],
            "local_replay_commands_failed": replay["summary"]["commands_failed"],
            "fresh_zenodo_check": rel(ZENODO_CHECK),
            "fresh_zenodo_action": zenodo["action"],
            "fresh_zenodo_revision": zenodo["revision"],
            "fresh_zenodo_file_count": zenodo["file_count"],
        },
        "publish_target": {
            "repo": "KokunoYumeto/modern-latex-manuscripts",
            "branch": "codex/laptop-noether-language-planning-20260701",
            "handoff_root": "workflow/codex-laptop-handoffs/20260701T223800Z",
            "release_tag": "codex-laptop-noether-language-planning-20260702T010851Z",
        },
        "boundary": (
            "This sidecar is post-package metadata. The zip contains the redo audit and checkpoint files "
            "available before the final archive build; this sidecar records the final archive hash and upload target."
        ),
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Post-redo final handoff",
        "",
        f"Generated UTC: `{payload['generated_utc']}`",
        "",
        "## Final Package",
        "",
        f"- Zip: `{payload['final_package']['zip']}`",
        f"- Bytes: `{payload['final_package']['bytes']}`",
        f"- SHA256: `{payload['final_package']['sha256']}`",
        f"- Builder validation: `{payload['final_package']['builder_pass']}`",
        f"- Independent validation: `{payload['final_package']['independent_pass']}`",
        "",
        "## Redo Summary",
        "",
        f"- Redo checkpoint passed: `{payload['redo_summary']['redo_checkpoint_passed']}`",
        f"- Local replay commands failed: `{payload['redo_summary']['local_replay_commands_failed']}`",
        f"- Fresh Zenodo action: `{payload['redo_summary']['fresh_zenodo_action']}`",
        "",
        "## Publish Target",
        "",
        f"- Branch: `{payload['publish_target']['branch']}`",
        f"- Handoff root: `{payload['publish_target']['handoff_root']}`",
        f"- Release tag: `{payload['publish_target']['release_tag']}`",
        "",
        "## Boundary",
        "",
        payload["boundary"],
        "",
    ]
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({"json": rel(OUT_JSON), "markdown": rel(OUT_MD)}, indent=2))


if __name__ == "__main__":
    main()

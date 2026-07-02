import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STAMP = "20260702T025500Z"
OUT_JSON = ROOT / "logs" / f"FULL_REDO_AFTER_MODE_RESET_PUBLISH_VERIFICATION_{STAMP}.json"
OUT_MD = ROOT / "logs" / f"FULL_REDO_AFTER_MODE_RESET_PUBLISH_VERIFICATION_{STAMP}.md"

REPO = "KokunoYumeto/modern-latex-manuscripts"
BRANCH = "codex/laptop-noether-language-planning-20260701"
DEST_ROOT = "workflow/codex-laptop-handoffs/20260701T223800Z"
RELEASE_TAG = "codex-laptop-noether-language-planning-20260702T020954Z"
ZIP_NAME = "Noether_LanguagePlanning_SourceEvidence_Checkpoint_20260702T020954Z.zip"
LOCAL_SHA_PATH = ROOT / "packages" / f"{ZIP_NAME}.sha256"
FULL_REDO_CHECKPOINT = ROOT / "logs" / "FULL_REDO_AFTER_MODE_RESET_CHECKPOINT_20260702T022209Z.json"


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT.resolve()).as_posix()


def gh_json(*args: str) -> dict:
    result = subprocess.run(["gh", *args], text=True, encoding="utf-8", errors="replace", capture_output=True)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip())
    return json.loads(result.stdout)


def write_workflow_entry(payload: dict) -> None:
    workflow = ROOT / "logs" / "WORKFLOW_LOG.md"
    entry = [
        "",
        f"### {payload['generated_utc']} - Full redo GitHub publish verification",
        "",
        f"- Published branch metadata to `{payload['branch']['url']}`.",
        f"- Uploaded draft release asset `{payload['release']['zip_asset_url']}`.",
        f"- Local SHA-256: `{payload['release']['local_zip_sha256']}`.",
        f"- GitHub asset digest: `{payload['release']['github_zip_digest']}`.",
        f"- Digest match: `{payload['release']['zip_digest_matches_local_sha256']}`.",
        "- Boundary: release remains draft and this verifies package handoff only; no native-review or term-promotion closure is implied.",
        "",
    ]
    workflow.write_text(workflow.read_text(encoding="utf-8") + "\n".join(entry), encoding="utf-8")


def main() -> None:
    release = gh_json(
        "release",
        "view",
        RELEASE_TAG,
        "--repo",
        REPO,
        "--json",
        "tagName,name,isDraft,url,assets",
    )
    local_sha = LOCAL_SHA_PATH.read_text(encoding="ascii").split()[0].upper()
    zip_asset = next((asset for asset in release["assets"] if asset["name"] == ZIP_NAME), None)
    if zip_asset is None:
        raise RuntimeError(f"missing release asset {ZIP_NAME}")
    github_digest = str(zip_asset.get("digest") or "")
    github_sha = github_digest.removeprefix("sha256:").upper()
    payload = {
        "artifact": "full_redo_after_mode_reset_publish_verification",
        "generated_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "input_checkpoint": rel(FULL_REDO_CHECKPOINT),
        "branch": {
            "repo": REPO,
            "branch": BRANCH,
            "remote_root": DEST_ROOT,
            "url": f"https://github.com/{REPO}/tree/{BRANCH}/{DEST_ROOT}",
        },
        "release": {
            "tag_name": release["tagName"],
            "name": release["name"],
            "is_draft": release["isDraft"],
            "url": release["url"],
            "zip_asset_url": zip_asset["url"],
            "zip_asset_size": zip_asset["size"],
            "zip_asset_state": zip_asset["state"],
            "local_zip_sha256": local_sha,
            "github_zip_digest": github_digest,
            "zip_digest_matches_local_sha256": github_sha == local_sha,
            "asset_names": [asset["name"] for asset in release["assets"]],
        },
        "decision": {
            "publish_verification_passed": github_sha == local_sha and zip_asset["state"] == "uploaded",
            "release_is_draft": release["isDraft"],
        },
        "boundary": (
            "This verifies GitHub branch and release-asset handoff for the full redo checkpoint. "
            "It does not close the active multilingual goal or any native/external review gate."
        ),
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Full Redo Publish Verification",
        "",
        f"Generated UTC: `{payload['generated_utc']}`",
        "",
        "## Result",
        "",
        f"- Publish verification passed: `{payload['decision']['publish_verification_passed']}`",
        f"- Branch URL: `{payload['branch']['url']}`",
        f"- Release URL: `{payload['release']['url']}`",
        f"- ZIP asset URL: `{payload['release']['zip_asset_url']}`",
        f"- Local SHA256: `{payload['release']['local_zip_sha256']}`",
        f"- GitHub digest: `{payload['release']['github_zip_digest']}`",
        f"- Release draft: `{payload['release']['is_draft']}`",
        "",
        "## Boundary",
        "",
        payload["boundary"],
        "",
    ]
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")
    write_workflow_entry(payload)
    print(json.dumps({"json": rel(OUT_JSON), "markdown": rel(OUT_MD), "passed": payload["decision"]["publish_verification_passed"]}, indent=2))
    if not payload["decision"]["publish_verification_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

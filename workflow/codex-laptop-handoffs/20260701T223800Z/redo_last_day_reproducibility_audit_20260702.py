import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STAMP = datetime.now(timezone.utc).replace(microsecond=0).strftime("%Y%m%dT%H%M%SZ")
OUT_JSON = ROOT / "logs" / f"LAST_DAY_REDO_REPRODUCIBILITY_AUDIT_{STAMP}.json"
OUT_MD = ROOT / "logs" / f"LAST_DAY_REDO_REPRODUCIBILITY_AUDIT_{STAMP}.md"

COMMANDS = [
    ["python", "tmp/audit_r7_lao_jica_official_math_shelf_20260701.py"],
    ["python", "tmp/build_r7_lao_jica_ocr_spotcheck_audit_20260701.py"],
    ["python", "tmp/build_goal_scope_status_audit_20260701.py"],
    ["python", "tmp/build_french_spanish_lane_status_audit_20260701.py"],
    ["python", "tmp/build_spanish_cumulative_status_manifest_20260701.py"],
    ["python", "tmp/build_french_cumulative_status_manifest_20260701.py"],
    ["python", "tmp/build_chinese_japanese_cumulative_status_manifest_20260701.py"],
    ["python", "tmp/build_arabic_persianate_lane_status_manifest_20260701.py"],
    ["python", "tmp/build_slavic_maintenance_status_manifest_20260701.py"],
    ["python", "tmp/build_research_publication_lane_status_manifest_20260701.py"],
    ["python", "tmp/build_july1_canonical_handoff_index_20260701.py"],
    ["python", "tmp/build_post_checkpoint_github_handoff_20260701.py"],
    ["python", "tmp/build_cross_lane_promotion_readiness_audit_20260702.py"],
    ["python", "tmp/build_review_correction_intake_ledger_20260702.py"],
    ["python", "tmp/build_visual_inspection_coverage_ledger_20260702.py"],
    ["python", "tmp/build_simplified_chinese_visual_queue_contact_sheet_20260702.py"],
    ["python", "tmp/build_visual_triage_integration_status_20260702.py"],
]

WATCH_PATTERNS = [
    "logs/*20260701*.json",
    "logs/*20260701*.md",
    "logs/*20260702*.json",
    "logs/*20260702*.md",
    "tmp/*20260701*.py",
    "tmp/*20260702*.py",
    "visual_inspection/simplified_chinese_visual_queue_20260702T013500Z/*.png",
]


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT.resolve()).as_posix()


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def snapshot() -> dict[str, dict]:
    files = {}
    for pattern in WATCH_PATTERNS:
        for path in ROOT.glob(pattern):
            if path.is_file() and "__pycache__" not in path.parts:
                files[rel(path)] = {
                    "bytes": path.stat().st_size,
                    "sha256": sha256(path),
                }
    return dict(sorted(files.items()))


def run_command(command: list[str]) -> dict:
    started = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    proc = subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
    )
    finished = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    return {
        "command": command,
        "started_utc": started,
        "finished_utc": finished,
        "returncode": proc.returncode,
        "stdout_tail": proc.stdout[-4000:],
        "stderr_tail": proc.stderr[-4000:],
    }


def diff_snapshots(before: dict, after: dict) -> dict:
    before_keys = set(before)
    after_keys = set(after)
    added = sorted(after_keys - before_keys)
    removed = sorted(before_keys - after_keys)
    changed = sorted(k for k in before_keys & after_keys if before[k]["sha256"] != after[k]["sha256"])
    unchanged = sorted(k for k in before_keys & after_keys if before[k]["sha256"] == after[k]["sha256"])
    return {
        "added": added,
        "removed": removed,
        "changed": changed,
        "unchanged_count": len(unchanged),
    }


def write_outputs(payload: dict) -> None:
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Last-day redo reproducibility audit",
        "",
        f"Generated UTC: `{payload['generated_utc']}`",
        "",
        "## Result",
        "",
        f"- Commands run: `{payload['summary']['commands_run']}`",
        f"- Commands failed: `{payload['summary']['commands_failed']}`",
        f"- Watched files added: `{payload['summary']['watched_files_added']}`",
        f"- Watched files changed: `{payload['summary']['watched_files_changed']}`",
        f"- Watched files removed: `{payload['summary']['watched_files_removed']}`",
        f"- Package rebuild included: `{payload['package_rebuild_included']}`",
        "",
        "## Failed commands",
        "",
    ]
    failures = [item for item in payload["commands"] if item["returncode"] != 0]
    if failures:
        for item in failures:
            lines.append(f"- `{' '.join(item['command'])}` returned `{item['returncode']}`")
    else:
        lines.append("- None.")
    lines.extend(
        [
            "",
            "## Changed watched files",
            "",
        ]
    )
    if payload["diff"]["changed"]:
        for item in payload["diff"]["changed"]:
            lines.append(f"- `{item}`")
    else:
        lines.append("- None; fixed-name watched artifacts reproduced byte-identically.")
    lines.extend(
        [
            "",
            "## Added watched files",
            "",
        ]
    )
    if payload["diff"]["added"]:
        for item in payload["diff"]["added"]:
            lines.append(f"- `{item}`")
    else:
        lines.append("- None.")
    lines.extend(
        [
            "",
            "## Boundary",
            "",
            payload["boundary"],
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    before = snapshot()
    commands = [run_command(command) for command in COMMANDS]
    after = snapshot()
    diff = diff_snapshots(before, after)
    payload = {
        "artifact": "last_day_redo_reproducibility_audit",
        "generated_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "scope": "Replay reproducible last-day local builders and record whether fixed-name artifacts regenerate cleanly.",
        "package_rebuild_included": False,
        "commands": commands,
        "diff": diff,
        "summary": {
            "commands_run": len(commands),
            "commands_failed": sum(1 for item in commands if item["returncode"] != 0),
            "watched_files_added": len(diff["added"]),
            "watched_files_changed": len(diff["changed"]),
            "watched_files_removed": len(diff["removed"]),
        },
        "boundary": (
            "This audit reruns local builders only. The large checkpoint package and a fresh live Zenodo "
            "check are handled as separate redo steps because they are timestamped/heavy artifacts."
        ),
    }
    write_outputs(payload)
    print(json.dumps({"json": rel(OUT_JSON), "markdown": rel(OUT_MD), "summary": payload["summary"]}, indent=2))
    if payload["summary"]["commands_failed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

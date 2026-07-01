import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STAMP = "20260701T223800Z"
PACKAGE = ROOT / "packages" / "Noether_LanguagePlanning_SourceEvidence_Checkpoint_20260701T222757Z.zip"
OUT_JSON = ROOT / "logs" / f"POST_CHECKPOINT_GITHUB_HANDOFF_{STAMP}.json"
OUT_MD = ROOT / "logs" / f"POST_CHECKPOINT_GITHUB_HANDOFF_{STAMP}.md"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT.resolve()).as_posix()


def main() -> None:
    validation_path = PACKAGE.with_suffix(PACKAGE.suffix + ".validation.json")
    independent_path = PACKAGE.with_suffix(PACKAGE.suffix + ".independent_validation.json")
    sha_path = PACKAGE.with_suffix(PACKAGE.suffix + ".sha256")
    zenodo_path = ROOT / "logs" / "ZENODO_NOETHER_LATEST_LIVE_CHECK_20260701T222409Z.json"

    validation = read_json(validation_path)
    independent = read_json(independent_path)
    zenodo = read_json(zenodo_path)
    sha = sha256_file(PACKAGE)
    sha_text = sha_path.read_text(encoding="ascii").split()[0].upper()

    payload = {
        "kind": "post_checkpoint_github_handoff",
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "session": {
            "machine_lane": "Codex laptop local workspace",
            "workspace_root": str(ROOT),
            "policy": "No credentials are included in this manifest; upload branch should stay separate from main.",
        },
        "current_checkpoint": {
            "zip": rel(PACKAGE),
            "zip_bytes": PACKAGE.stat().st_size,
            "sha256": sha,
            "sha256_file_value": sha_text,
            "sha256_matches_sidecar": sha == sha_text,
            "builder_validation": rel(validation_path),
            "builder_overall_pass": validation.get("overall_pass"),
            "builder_required_missing": validation.get("required_missing"),
            "builder_credential_scan_hits": validation.get("credential_scan_hits"),
            "independent_validation": rel(independent_path),
            "independent_overall_pass": independent.get("overall_pass"),
            "independent_sha256_matches": independent.get("sha256_matches"),
            "independent_zip_test_bad_file": independent.get("zip_test_bad_file"),
        },
        "source_freshness": {
            "zenodo_check": rel(zenodo_path),
            "doi": zenodo.get("doi"),
            "record_id": zenodo.get("record_id"),
            "revision": zenodo.get("revision"),
            "version": zenodo.get("version"),
            "file_count": zenodo.get("file_count"),
            "no_source_replacement_required": zenodo.get("no_source_replacement_required"),
            "added_files": zenodo.get("added_files"),
            "removed_files": zenodo.get("removed_files"),
            "size_changed_files": zenodo.get("size_changed_files"),
            "checksum_changed_files": zenodo.get("checksum_changed_files"),
        },
        "required_handoff_files": [
            "logs/WORKFLOW_LOG.md",
            "logs/JULY1_CANONICAL_HANDOFF_INDEX_20260701T220000Z.md",
            "logs/SLAVIC_MAINTENANCE_STATUS_MANIFEST_20260701T204500Z.md",
            "logs/RESEARCH_PUBLICATION_LANE_STATUS_MANIFEST_20260701T213000Z.md",
            "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260701T222409Z.md",
            "tmp/dependency_smoke_test_20260701.tex",
            "tmp/dependency_smoke_test_20260701/dependency_smoke_test_20260701.pdf",
            "tmp/dependency_smoke_test_20260701_rerun/dependency_smoke_test_20260701.pdf",
        ],
        "next_work_queue": [
            {
                "lane": "Slavic maintenance",
                "next": "Keep watching Zenodo/source updates and external review returns; rebuild Slavic cumulative readers only when source/review evidence changes.",
            },
            {
                "lane": "French/Spanish",
                "next": "Use existing native-register shelves to continue cumulative reader upgrade, render validation, and term-rationale tightening.",
            },
            {
                "lane": "Chinese/Japanese",
                "next": "Do source-fidelity/native-register reread before any public-edition promotion; preserve current cumulative status as proof artifact only.",
            },
            {
                "lane": "Arabic/Persianate",
                "next": "Keep Arabic controlled and evidence-limited; separate Iranian Persian, Dari, and Tajik Cyrillic register decisions.",
            },
            {
                "lane": "Research/publication",
                "next": "Turn the interlanguage/open-source education notes into a citable methods section with authority and anti-colonial framing.",
            },
            {
                "lane": "GitHub/Drive/Zenodo handoff",
                "next": "Publish this manifest to a laptop-specific branch; upload the full checkpoint zip as a release asset or external archive where file-size limits allow.",
            },
        ],
        "boundary": [
            "This sidecar is a handoff and coordination artifact, not a final language-edition completion claim.",
            "The full objective remains active.",
            "Native/external authority review remains distinct from local mechanical validation.",
        ],
    }

    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Post-Checkpoint GitHub Handoff",
        "",
        f"- Generated UTC: `{payload['generated_at_utc']}`",
        f"- Package: `{payload['current_checkpoint']['zip']}`",
        f"- SHA256: `{sha}`",
        f"- Package bytes: `{payload['current_checkpoint']['zip_bytes']}`",
        f"- Builder validation pass: `{payload['current_checkpoint']['builder_overall_pass']}`",
        f"- Independent validation pass: `{payload['current_checkpoint']['independent_overall_pass']}`",
        f"- Credential scan hits: `{payload['current_checkpoint']['builder_credential_scan_hits']}`",
        "",
        "## Zenodo Freshness",
        "",
        f"- DOI: `{payload['source_freshness']['doi']}`",
        f"- Record/revision: `{payload['source_freshness']['record_id']}` / `{payload['source_freshness']['revision']}`",
        f"- Version: `{payload['source_freshness']['version']}`",
        f"- File count: `{payload['source_freshness']['file_count']}`",
        f"- No source replacement required: `{payload['source_freshness']['no_source_replacement_required']}`",
        "",
        "## Next Work Queue",
        "",
    ]
    for item in payload["next_work_queue"]:
        lines.append(f"- **{item['lane']}**: {item['next']}")
    lines.extend(
        [
            "",
            "## Boundary",
            "",
        ]
    )
    for item in payload["boundary"]:
        lines.append(f"- {item}")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"json": rel(OUT_JSON), "markdown": rel(OUT_MD), "sha256": sha}, ensure_ascii=True, indent=2))


if __name__ == "__main__":
    main()

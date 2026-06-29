import hashlib
import json
import pathlib
import sys


BASE = pathlib.Path(__file__).resolve().parents[1]
MANIFEST = BASE / "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json"


EXPECTED = {
    "source_seed_entries": 24,
    "url_validation_total": 24,
    "url_validation_accessible": 20,
    "url_validation_inaccessible": 4,
    "chinese_reinforcement_entries": 7,
    "arabic_reinforcement_sources": 6,
    "term_rows": {
        "simplified_chinese": 34,
        "romance_french_spanish": 46,
        "japanese": 41,
        "persian_family_arabic": 32,
        "total_term_anchor_rows": 153,
    },
    "pages": {
        "simplified_chinese": 787,
        "romance_french_spanish": 1283,
        "japanese": 242,
        "persian_family_arabic": 1630,
        "total_pages_analyzed_for_term_anchors": 3942,
    },
}


def sha256(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def fail(errors: list[str]) -> None:
    print(json.dumps({"ok": False, "errors": errors}, indent=2), file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    errors: list[str] = []
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    if manifest.get("artifact") != "noether_pc_multilingual_status_manifest":
        errors.append("unexpected manifest artifact name")
    if manifest.get("status") != "active_goal_progress_manifest_not_completion_claim":
        errors.append("manifest must remain a progress manifest, not a completion claim")

    source = manifest["source_evidence"]
    for key in [
        "source_seed_entries",
        "url_validation_total",
        "url_validation_accessible",
        "url_validation_inaccessible",
        "chinese_reinforcement_entries",
        "arabic_reinforcement_sources",
    ]:
        if source.get(key) != EXPECTED[key]:
            errors.append(f"{key}: expected {EXPECTED[key]}, got {source.get(key)}")

    for key, expected in EXPECTED["term_rows"].items():
        got = manifest["term_anchor_totals"].get(key)
        if got != expected:
            errors.append(f"term rows {key}: expected {expected}, got {got}")

    for key, expected in EXPECTED["pages"].items():
        got = manifest["source_pages_analyzed"].get(key)
        if got != expected:
            errors.append(f"pages {key}: expected {expected}, got {got}")

    for artifact_group in ["json", "markdown", "scripts"]:
        for item in manifest["artifacts"][artifact_group]:
            rel = item["path"].split("20260629/", 1)[-1]
            path = BASE / rel
            if not path.exists():
                errors.append(f"missing indexed artifact: {item['path']}")
                continue
            if path.stat().st_size != item["bytes"]:
                errors.append(f"size mismatch for {item['path']}")
            if sha256(path) != item["sha256"]:
                errors.append(f"sha256 mismatch for {item['path']}")

    if manifest["reproducibility"].get("source_pdfs_committed") is not False:
        errors.append("source_pdfs_committed must be false")
    if manifest["reproducibility"].get("source_passages_committed") is not False:
        errors.append("source_passages_committed must be false")

    pdfs = list(BASE.rglob("*.pdf"))
    if pdfs:
        errors.append("PDFs found inside handoff payload: " + ", ".join(str(path) for path in pdfs))

    if errors:
        fail(errors)

    print(
        json.dumps(
            {
                "ok": True,
                "manifest": str(MANIFEST),
                "term_rows": manifest["term_anchor_totals"]["total_term_anchor_rows"],
                "pages_analyzed": manifest["source_pages_analyzed"]["total_pages_analyzed_for_term_anchors"],
                "json_artifacts": len(manifest["artifacts"]["json"]),
                "markdown_artifacts": len(manifest["artifacts"]["markdown"]),
                "scripts": len(manifest["artifacts"]["scripts"]),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()

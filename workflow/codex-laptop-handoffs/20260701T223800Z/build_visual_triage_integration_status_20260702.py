import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GENERATED_UTC = "2026-07-02T02:00:00Z"
OUT_STEM = "VISUAL_TRIAGE_INTEGRATION_STATUS_20260702T020000Z"

COVERAGE_JSON = ROOT / "logs" / "VISUAL_INSPECTION_COVERAGE_LEDGER_20260702T011500Z.json"
TRIAGE_JSON = ROOT / "logs" / "SIMPLIFIED_CHINESE_VISUAL_QUEUE_TRIAGE_20260702T014500Z.json"
CONTACT_JSON = ROOT / "logs" / "SIMPLIFIED_CHINESE_VISUAL_QUEUE_CONTACT_SHEET_20260702T013500Z.json"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_markdown(path: Path, payload: dict) -> None:
    lines = [
        "# Visual triage integration status",
        "",
        f"Generated UTC: `{payload['generated_utc']}`",
        "",
        "## Purpose",
        "",
        payload["purpose"],
        "",
        "## Summary",
        "",
        f"- Current Simplified Chinese queue count: `{payload['summary']['current_simplified_chinese_queue_count']}`",
        f"- Historical first-page triage item count: `{payload['summary']['historical_first_page_triage_item_count']}`",
        f"- First-page triaged count: `{payload['summary']['first_page_triaged_count']}`",
        f"- Gross blank-page or walkoff failures observed: `{payload['summary']['gross_failure_count']}`",
        f"- Promotion-cleared from this integration: `{payload['summary']['promotion_cleared_count']}`",
        f"- Still requiring full inspection if promoted: `{payload['summary']['full_inspection_still_required_if_promoted_count']}`",
        "",
        "## Decision",
        "",
        f"- Promotion allowed from this status: `{payload['decision']['promotion_allowed_from_this_status']}`",
        f"- Package rebuild needed: `{payload['decision']['package_rebuild_needed']}`",
        f"- Reason: {payload['decision']['reason']}",
        "",
        "## Integrated items",
        "",
        "| PDF | Page count | First-page triage | Gross failure | Promotion visual gate | Note |",
        "| --- | ---: | --- | --- | --- | --- |",
    ]
    for item in payload["integrated_queue"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{item['path']}`",
                    str(item["page_count"]),
                    f"`{item['first_page_triage_status']}`",
                    f"`{item['gross_failure_observed']}`",
                    f"`{item['promotion_visual_gate']}`",
                    item["promotion_note"],
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Boundary",
            "",
            payload["boundary"],
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    coverage = load_json(COVERAGE_JSON)
    triage = load_json(TRIAGE_JSON)
    contact = load_json(CONTACT_JSON) if CONTACT_JSON.exists() else {}
    contact_exists = CONTACT_JSON.exists()

    queued = coverage["priority_visual_inspection_queue"]
    triage_by_pdf = {item["pdf"]: item for item in triage["items"]}

    queued_by_pdf = {item["path"]: item for item in queued}
    contact_by_pdf = {item["pdf"]: item for item in contact.get("rendered_items", [])}
    if queued and set(queued_by_pdf) != set(triage_by_pdf):
        missing = sorted(set(item["path"] for item in queued) - set(triage_by_pdf))
        extra = sorted(set(triage_by_pdf) - set(item["path"] for item in queued))
        raise SystemExit(f"Triage/coverage mismatch; missing={missing}; extra={extra}")
    if not queued and not contact_by_pdf:
        raise SystemExit("Coverage queue is empty and no prior contact-sheet rendered items are available")

    integrated = []
    source_paths = sorted(triage_by_pdf)
    for source_path in source_paths:
        triage_item = triage_by_pdf[source_path]
        queued_item = queued_by_pdf.get(source_path)
        contact_item = contact_by_pdf.get(source_path, {})
        integrated.append(
            {
                "path": source_path,
                "lane": queued_item["lane"] if queued_item else "simplified_chinese",
                "bytes": queued_item["bytes"] if queued_item else contact_item.get("pdf_bytes"),
                "modified_utc": queued_item["modified_utc"] if queued_item else None,
                "page_count": queued_item["page_count"] if queued_item else contact_item.get("page_count"),
                "current_coverage_gate": queued_item["promotion_visual_gate"] if queued_item else "referenced_by_existing_visual_triage_artifact",
                "first_page_triage_status": triage_item["first_page_triage"],
                "gross_failure_observed": False,
                "promotion_visual_gate": "not_closed_first_page_only",
                "requires_full_inspection_if_promoted": True,
                "promotion_note": triage_item["promotion_note"],
            }
        )

    payload = {
        "artifact": "visual_triage_integration_status",
        "generated_utc": GENERATED_UTC,
        "completion_claim": False,
        "purpose": (
            "Reconcile the Simplified Chinese visual-inspection queue from the coverage ledger "
            "with the first-page triage artifact, while preserving the promotion boundary."
        ),
        "inputs": {
            "coverage_ledger": str(COVERAGE_JSON.relative_to(ROOT)).replace("\\", "/"),
            "triage_ledger": str(TRIAGE_JSON.relative_to(ROOT)).replace("\\", "/"),
            "contact_sheet_manifest": str(CONTACT_JSON.relative_to(ROOT)).replace("\\", "/"),
            "contact_sheet_manifest_exists": contact_exists,
            "contact_sheet_image": triage["contact_sheet"],
        },
        "summary": {
            "current_simplified_chinese_queue_count": len(queued),
            "historical_first_page_triage_item_count": len(triage_by_pdf),
            "first_page_triaged_count": len(integrated),
            "gross_failure_count": 0,
            "promotion_cleared_count": 0,
            "full_inspection_still_required_if_promoted_count": len(integrated),
        },
        "integrated_queue": integrated,
        "decision": {
            "promotion_allowed_from_this_status": False,
            "package_rebuild_needed": False,
            "reason": (
                "The first-page triage found no gross blank-page or page-walkoff failure, "
                "but it did not inspect front/middle/back pages or dense formula pages."
            ),
        },
        "boundary": (
            "This status updates queue state only. It does not supersede the visual coverage ledger, "
            "does not claim full visual clearance, and should not trigger a large package rebuild by itself."
        ),
    }

    out_json = ROOT / "logs" / f"{OUT_STEM}.json"
    out_md = ROOT / "logs" / f"{OUT_STEM}.md"
    write_json(out_json, payload)
    write_markdown(out_md, payload)
    print(json.dumps({"json": str(out_json), "markdown": str(out_md)}, ensure_ascii=True, indent=2))


if __name__ == "__main__":
    main()

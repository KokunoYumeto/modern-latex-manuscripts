import json
import re
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STAMP = "20260702T005500Z"
OUT_JSON = ROOT / "logs" / f"REVIEW_CORRECTION_INTAKE_LEDGER_{STAMP}.json"
OUT_MD = ROOT / "logs" / f"REVIEW_CORRECTION_INTAKE_LEDGER_{STAMP}.md"


KEYWORDS = re.compile(
    r"(accepted|correction|review return|review_return|accepted_pair|return_file|blocking|native review|external review)",
    re.IGNORECASE,
)


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT.resolve()).as_posix()


def read_json(rel_path: str) -> dict:
    return json.loads((ROOT / rel_path).read_text(encoding="utf-8-sig"))


def file_digest(path: Path) -> dict:
    return {
        "path": rel(path),
        "bytes": path.stat().st_size,
        "modified_utc": datetime.fromtimestamp(path.stat().st_mtime, timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z"),
    }


def list_files(root: Path, suffixes: tuple[str, ...] | None = None) -> list[Path]:
    if not root.exists():
        return []
    out = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if suffixes and path.suffix.lower() not in suffixes:
            continue
        out.append(path)
    return sorted(out)


def keyword_hits(paths: list[Path], *, limit: int = 120) -> list[dict]:
    hits = []
    for path in paths:
        if len(hits) >= limit:
            break
        if path.stat().st_size > 2_000_000:
            continue
        try:
            text = path.read_text(encoding="utf-8-sig", errors="ignore")
        except OSError:
            continue
        match_count = len(KEYWORDS.findall(text))
        if match_count:
            item = file_digest(path)
            item["keyword_hit_count"] = match_count
            hits.append(item)
    return hits


def main() -> None:
    external_returns = list_files(ROOT / "external_review_returns")
    review_text_files = list_files(ROOT / "review_bundles", (".json", ".md", ".csv", ".txt"))
    log_files = list_files(ROOT / "logs", (".json", ".md", ".txt", ".csv"))
    glossary_files = list_files(ROOT / "glossary", (".json", ".md", ".txt", ".csv"))

    slavic = read_json("logs/SLAVIC_MAINTENANCE_STATUS_MANIFEST_20260701T204500Z.json")
    cross_lane = read_json("logs/CROSS_LANE_PROMOTION_READINESS_AUDIT_20260702T003500Z.json")
    arabic_persianate = read_json("logs/ARABIC_PERSIANATE_LANE_STATUS_MANIFEST_20260701T200500Z.json")
    chinese_japanese = read_json("logs/CHINESE_JAPANESE_CUMULATIVE_STATUS_MANIFEST_20260701T170500Z.json")

    accepted_templates = [
        p for p in review_text_files if "ACCEPTED_DECISIONS_LEDGER_TEMPLATE" in p.name
    ]
    return_templates = [
        p for p in review_text_files if "RETURN" in p.name.upper() or "TEMPLATE" in p.name.upper()
    ]

    selected_correction_logs = []
    for path in log_files:
        name = path.name.upper()
        if any(token in name for token in ["CORRECTION", "PATCH", "REVIEW", "RETURN", "ACCEPTED"]):
            selected_correction_logs.append(path)
    selected_correction_logs = sorted(selected_correction_logs, key=lambda p: p.stat().st_mtime, reverse=True)[:160]

    result = {
        "artifact": "review_correction_intake_ledger",
        "generated_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "completion_claim": False,
        "external_review_returns": {
            "root": "external_review_returns",
            "file_count": len(external_returns),
            "files": [file_digest(p) for p in external_returns[:200]],
            "ingestion_available_now": len(external_returns) > 0,
            "decision": (
                "No external review-return files are present; no accepted external review decisions can be ingested."
                if not external_returns
                else "External review-return files are present and must be schema-validated before ingestion."
            ),
        },
        "slavic_review_state": {
            "status_manifest": "logs/SLAVIC_MAINTENANCE_STATUS_MANIFEST_20260701T204500Z.json",
            "expected_form_count": slavic["review_status"]["expected_form_count"],
            "return_file_count": slavic["review_status"]["return_file_count"],
            "schema_valid_return_file_count": slavic["review_status"]["schema_valid_return_file_count"],
            "accepted_pair_count": slavic["review_status"]["accepted_pair_count"],
            "blocking_issue_count": slavic["review_status"]["blocking_issue_count"],
            "complete_for_all_units": slavic["review_status"]["complete_for_all_units"],
            "rebuild_required_from_review_returns": False,
        },
        "cross_lane_gate_summary": {
            "readiness_audit": "logs/CROSS_LANE_PROMOTION_READINESS_AUDIT_20260702T003500Z.json",
            "lanes_with_open_review_or_authority_gates": [
                lane["lane"]
                for lane in cross_lane["lanes"]
                if any(gate["pass"] is not True for gate in lane["promotion_gates"])
            ],
        },
        "known_local_correction_ledgers": {
            "selected_log_count": len(selected_correction_logs),
            "selected_logs": [file_digest(p) for p in selected_correction_logs],
            "keyword_hits_sample": keyword_hits(log_files + glossary_files, limit=80),
        },
        "review_packet_templates": {
            "review_text_file_count": len(review_text_files),
            "accepted_decision_template_count": len(accepted_templates),
            "accepted_decision_templates": [file_digest(p) for p in accepted_templates],
            "return_or_template_file_count": len(return_templates),
            "return_or_template_files": [file_digest(p) for p in return_templates[:120]],
        },
        "non_slavic_review_boundaries": {
            "arabic_persianate": {
                "manifest": "logs/ARABIC_PERSIANATE_LANE_STATUS_MANIFEST_20260701T200500Z.json",
                "native_external_review_open": True,
                "summary": arabic_persianate["edition_decision"]["why_not_final"],
            },
            "chinese_japanese": {
                "manifest": "logs/CHINESE_JAPANESE_CUMULATIVE_STATUS_MANIFEST_20260701T170500Z.json",
                "native_external_review_open": True,
                "summary": chinese_japanese["edition_decision"]["why_not_final"],
            },
        },
        "ingestion_rules": [
            "Treat files in external_review_returns as the only direct reviewer-return input root unless a future log explicitly designates another root.",
            "Do not copy reviewer-facing templates into accepted ledgers.",
            "Only schema-valid returns with explicit accept/accept_with_sidecar decisions may become accepted decisions.",
            "Any required correction from a review return must create a correction ledger entry, TeX/source patch if applicable, render/visual validation if rendered output changes, and a package or branch handoff update.",
            "Local source-critical corrections and glossary rationales remain local editorial evidence unless externally reviewed.",
        ],
        "current_decision": {
            "accepted_external_review_ingestion_performed": False,
            "reason": "No external review-return files are present.",
            "slavic_rebuild_required_now": False,
            "non_slavic_promotion_from_review_now": False,
        },
    }

    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Review and Correction Intake Ledger",
        "",
        f"- Generated UTC: `{result['generated_utc']}`",
        f"- External review-return files present: `{result['external_review_returns']['file_count']}`",
        f"- Accepted external review ingestion performed: `{result['current_decision']['accepted_external_review_ingestion_performed']}`",
        f"- Slavic rebuild required from review returns: `{result['slavic_review_state']['rebuild_required_from_review_returns']}`",
        "",
        "## Slavic Review State",
        "",
        f"- Expected forms: `{result['slavic_review_state']['expected_form_count']}`",
        f"- Return files: `{result['slavic_review_state']['return_file_count']}`",
        f"- Schema-valid returns: `{result['slavic_review_state']['schema_valid_return_file_count']}`",
        f"- Accepted pairs: `{result['slavic_review_state']['accepted_pair_count']}`",
        f"- Blocking issues: `{result['slavic_review_state']['blocking_issue_count']}`",
        f"- Complete for all units: `{result['slavic_review_state']['complete_for_all_units']}`",
        "",
        "## Decision",
        "",
        f"- {result['external_review_returns']['decision']}",
        "- No accepted-correction promotion was made in this pass.",
        "- Keep local correction/rationale logs separate from external reviewer acceptance.",
        "",
        "## Open Review Or Authority Gates",
        "",
    ]
    for lane in result["cross_lane_gate_summary"]["lanes_with_open_review_or_authority_gates"]:
        lines.append(f"- {lane}")
    lines.extend(["", "## Ingestion Rules", ""])
    for rule in result["ingestion_rules"]:
        lines.append(f"- {rule}")

    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"json": rel(OUT_JSON), "markdown": rel(OUT_MD)}, ensure_ascii=True, indent=2))


if __name__ == "__main__":
    main()

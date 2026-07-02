"""Build the local PC branch coordination audit.

This script is deliberately local-only. It records branch-of-record and
orientation pointers without reading remote branches, copying source text, or
using credentials.
"""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_JSON = ROOT / "LOCAL_PC_BRANCH_COORDINATION_AUDIT_20260630.json"
OUT_MD = ROOT / "LOCAL_PC_BRANCH_COORDINATION_AUDIT_20260630.md"


def build_payload() -> dict:
    return {
        "artifact": "local_pc_branch_coordination_audit",
        "status": "local_only_branch_coordination_audit_not_remote_branch_state_not_completion_claim",
        "generated_date": date(2026, 6, 30).isoformat(),
        "bandwidth_mode": "local_only_no_network_actions",
        "no_network_actions_performed": True,
        "credentials_or_tokens_copied": False,
        "source_text_copied": False,
        "source_language_terms_copied": False,
        "current_pc_branch": {
            "repo": "KokunoYumeto/modern-latex-manuscripts",
            "branch": "codex/noether-pc-20260629",
            "base_branch": "codex/noether-slavic-handoff-20260628",
            "draft_pr": "https://github.com/KokunoYumeto/modern-latex-manuscripts/pull/1",
            "last_successfully_pushed_head_before_local_only_work": "db7ffc6ca62116d9f8dd8c5ba156e7e2c7c953a2",
            "branch_role": "branch_of_record_for_this_pc_noether_multilingual_and_interlanguage_work",
        },
        "orientation": {
            "exact_predecessor_thread_id": "019ead97-38c8-7112-9b9c-e8c176d526a1",
            "primary_predecessor_session_log": r"C:\Users\memo_\.codex\sessions\2026\06\09\rollout-2026-06-09T20-13-49-019ead97-38c8-7112-9b9c-e8c176d526a1.jsonl",
            "primary_predecessor_session_log_sha256": "061220838BEA470DAA775E6920EFE96B1E2518EBDB8F1C0480D3AD0F1125530B",
            "parallel_handoff_thread_id": "019f1007-406b-7cc3-a3cf-ac23517cd8a6",
            "current_takeover_thread_id": "019f121c-5214-7042-a218-4fd204bd333c",
            "orientation_evidence_artifact": "PREVIOUS_SESSION_ORIENTATION_AND_GITHUB_SYNC_QUEUE_20260630.json",
            "orientation_boundary": "records_pointers_and_hashes_only_no_prior_chat_or_source_passage_copy",
        },
        "included_pc_workstreams": [
            {
                "id": "slavic_lane",
                "scope": "maintain completed/review-ready Ukrainian, Russian, and Interslavic/Panslavic Latin+Cyrillic lane; ingest later corrections and review returns when available",
            },
            {
                "id": "simplified_chinese_lane",
                "scope": "source-evidence shelves, term anchors, glossary/rationale preparation, page inspection, render/script validation planning, review handoff",
            },
            {
                "id": "romance_french_spanish_lanes",
                "scope": "French and Spanish source witnesses, term anchors, glossary/rationale preparation, page inspection, review handoff",
            },
            {
                "id": "japanese_lane",
                "scope": "Japanese source witnesses, term anchors, glossary/rationale preparation, page inspection, review handoff",
            },
            {
                "id": "persian_family_arabic_lanes",
                "scope": "Persian/Farsi/Dari/Tajik-related registers and Arabic source witnesses, term anchors, RTL/script governance, review handoff",
            },
            {
                "id": "support_language_cohorts",
                "scope": "Africa, East/Southeast Asia/Pacific, Pan-Turkic-adjacent, South Asia, source-first textbook cohorts, and methodology cohorts as scoped by support authority notes",
            },
            {
                "id": "interlanguage_constructed_language_methodology",
                "scope": "semi-constructed/constructed/interlanguage authority, educational utility, geographic language-family usefulness, anti-colonial/open-source ownership framing, publication lane",
            },
            {
                "id": "source_core_and_handoff",
                "scope": "small text/TeX/workbook/source-core upload planning, manifests, ledgers, validation scripts, GitHub/Drive/Zenodo handoff pointers",
            },
        ],
        "other_branch_coordination": {
            "local_workspace_git_checkout": False,
            "payload_workspace_is_git_checkout": False,
            "remote_branch_fetch_performed": False,
            "remote_branch_state_claim": False,
            "local_other_branch_claim": False,
            "coordination_rule": "treat codex/noether-pc-20260629 as this PC instance branch of record until an explicit network-approved branch inventory proves a different branch owns a specific workstream",
            "bandwidth_reason_for_deferral": "user reported phone data/rate constraint; avoid fetch, push, clone, or large remote inspection unless explicitly approved",
            "next_network_branch_checks_when_allowed": [
                "fetch the draft PR branch head and compare it with db7ffc6ca62116d9f8dd8c5ba156e7e2c7c953a2",
                "list remote noether/codex branches with a small heads-only query",
                "compare branch names and commit dates against the workstream list before pushing",
                "push small text/json/md/script batches before any large source-core archive",
            ],
        },
        "current_local_progress_evidence": {
            "status_manifest": "NOETHER_PC_MULTILINGUAL_STATUS_MANIFEST_20260629.json",
            "github_sync_ledger": "GITHUB_PC_BRANCH_SYNC_LEDGER_20260630.json",
            "offline_commit_batch_plan": "OFFLINE_GITHUB_COMMIT_BATCH_PLAN_20260630.json",
            "canonical_promotion_gate_audit": "CANONICAL_EDITION_PROMOTION_GATE_AUDIT_20260630.json",
            "render_script_validation_preflight": "RENDER_SCRIPT_VALIDATION_PREFLIGHT_20260630.json",
            "render_script_validation_execution_queue": "RENDER_SCRIPT_VALIDATION_EXECUTION_QUEUE_20260630.json",
            "support_cohort_authority_notes": "SUPPORT_COHORT_AUTHORITY_NOTES_20260630.json",
        },
        "boundaries": [
            "This artifact is a local coordination audit and does not update GitHub.",
            "This artifact is not a remote branch inventory and does not claim other branches were checked.",
            "This artifact records no credentials, tokens, private keys, source passages, or source-language term copies.",
            "This artifact is not native/external review, not term approval, not translation completion, and not canonical-edition promotion.",
            "The active Noether multilingual goal remains open.",
        ],
    }


def build_markdown(payload: dict) -> str:
    workstreams = "\n".join(
        f"| `{row['id']}` | {row['scope']}. |" for row in payload["included_pc_workstreams"]
    )
    checks = "\n".join(
        f"{idx}. {item}." for idx, item in enumerate(payload["other_branch_coordination"]["next_network_branch_checks_when_allowed"], start=1)
    )
    evidence = "\n".join(
        f"- `{item}`" for item in payload["current_local_progress_evidence"].values()
    )
    boundaries = "\n".join(f"- {item}" for item in payload["boundaries"])
    branch = payload["current_pc_branch"]
    orientation = payload["orientation"]
    other = payload["other_branch_coordination"]

    return f"""# Local PC Branch Coordination Audit - 2026-06-30

Status: local-only branch coordination audit. This is not a GitHub update, not a remote branch inventory, and not a completion claim.

## Branch Of Record

- Repository: `{branch['repo']}`
- Branch: `{branch['branch']}`
- Base branch: `{branch['base_branch']}`
- Draft PR: {branch['draft_pr']}
- Last successfully pushed head before local-only work: `{branch['last_successfully_pushed_head_before_local_only_work']}`
- Role: branch of record for this PC's Noether multilingual and interlanguage work.

## Exact Orientation Pointer

- Exact predecessor thread: `{orientation['exact_predecessor_thread_id']}`
- Primary predecessor session log: `{orientation['primary_predecessor_session_log']}`
- Predecessor session log SHA-256: `{orientation['primary_predecessor_session_log_sha256']}`
- Parallel handoff thread: `{orientation['parallel_handoff_thread_id']}`
- Current takeover thread: `{orientation['current_takeover_thread_id']}`
- Orientation evidence artifact: `{orientation['orientation_evidence_artifact']}`

This records pointers and hashes only. It does not copy prior chat passages, source-language passages, or credentials.

## Included PC Workstreams

| Workstream | Scope |
| --- | --- |
{workstreams}

## Other Branch Coordination

- Current workspace is not a git checkout.
- Payload workspace is not a git checkout.
- Remote branch fetch performed: `{str(other['remote_branch_fetch_performed']).lower()}`
- Remote branch state claim: `{str(other['remote_branch_state_claim']).lower()}`
- Local other-branch ownership claim: `{str(other['local_other_branch_claim']).lower()}`

Coordination rule: treat `codex/noether-pc-20260629` as this PC instance branch of record until an explicit network-approved branch inventory proves a different branch owns a specific workstream.

When bandwidth is acceptable, the small branch checks should be:

{checks}

## Local Evidence Pointers

{evidence}

## Boundaries

{boundaries}
"""


def main() -> None:
    payload = build_payload()
    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(build_markdown(payload), encoding="utf-8")
    print(json.dumps({
        "artifact": payload["artifact"],
        "json": str(OUT_JSON),
        "markdown": str(OUT_MD),
        "no_network_actions_performed": payload["no_network_actions_performed"],
    }, indent=2))


if __name__ == "__main__":
    main()

# ARTIFACT_INDEX builder: every file in the program folder with role, hash, flags.
import hashlib
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
P = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")

ROLES = {
    "CORPUS_MAP.md": ("corpus map, strata A-D + caveats", "derived", "yes", "yes"),
    "PROGRAM.md": ("program proposal (superseded in part by atlas/draft)", "derived", "yes", "yes"),
    "STATUS.md": ("session cursor / pass log", "derived", "no", "no"),
    "ISLAND_ATLAS.md": ("global synthesis; findings F1-F12", "derived", "yes", "yes"),
    "CONCORDANCE.md": ("blind-atlas x sidecar delta + triangulation hit log", "derived", "yes", "yes"),
    "CLAIM_LEDGER.md": ("typed claims CLM-* with tests", "derived", "yes", "yes"),
    "HEURISTIC_REGISTER.md": ("heuristics HEU-* raw->clean->measure", "derived", "yes", "yes"),
    "INTERSLAVIC_GATE_MAP.md": ("lane gates G1-G15 + audit B1-B3", "derived", "yes", "yes"),
    "UNION_TERM_SPINE_20260704.json": ("union spine v1 (superseded; frozen copy is baseline)", "derived", "no", "no"),
    "UNION_TERM_SPINE_20260704.md": ("union spine v1 summary (superseded)", "derived", "no", "no"),
    "UNION_TERM_SPINE_v2_WITH_SLAVIC.json": ("union spine v2, ledger-routed Slavic column", "derived", "yes", "yes"),
    "UNION_TERM_SPINE_v2_WITH_SLAVIC.csv": ("spine v2 spreadsheet view", "derived", "yes", "yes"),
    "STRATIFIED_CORE_SPINE_PROPOSAL_20260704.json": ("C2 core spine, 67 rows", "derived", "yes", "yes"),
    "STRATIFIED_CORE_SPINE_PROPOSAL_20260704.md": ("C2 summary table", "derived", "yes", "yes"),
    "INTERSLAVIC_LEDGER_RETROFIT_20260704.json": ("1229 term rows, retrofit schema", "derived", "yes", "review"),
    "INTERSLAVIC_LEDGER_RETROFIT_20260704.csv": ("retrofit spreadsheet view", "derived", "yes", "review"),
    "F10_EAST_SLAVIC_SKEW_AUDIT_20260704.json": ("F10 audit rows (baseline state)", "derived", "yes", "review"),
    "F10_EAST_SLAVIC_SKEW_AUDIT_20260704.md": ("F10 audit headline + reading", "derived", "yes", "yes"),
    "F10_AUDIT_postwriteback_20260704.json": ("audit annotated with shelf-level witnesses", "derived", "yes", "review"),
    "DO_NOT_USE_LEDGER_20260704.json": ("123 typed adverse relations", "derived", "yes", "yes"),
    "DO_NOT_USE_LEDGER_20260704.md": ("adverse ledger summary", "derived", "yes", "yes"),
    "WS_WITNESS_BACKFILL_v0_20260704.json": ("backfill v0, 15 concepts (superseded by v1)", "derived", "no", "no"),
    "WS_WITNESS_BACKFILL_v0_20260704.md": ("backfill v0 summary (superseded)", "derived", "no", "no"),
    "WS_WITNESS_BACKFILL_v1_20260704.json": ("backfill v1, 37 concepts, per-file hits", "derived", "yes", "yes"),
    "WS_WITNESS_BACKFILL_v1_20260704.md": ("backfill v1 branch table", "derived", "yes", "yes"),
    "WITNESS_WRITEBACK_v0_20260704.json": ("state-c re-measurement, 1.255->1.754", "derived", "yes", "yes"),
    "branch_weighting_v0_20260704.json": ("concentration stats (post re-key run)", "derived", "yes", "yes"),
    "BRANCH_WEIGHTING_SPEC.md": ("math-lane spec: dependence-corrected weighting", "derived", "yes", "yes"),
    "INTERLINGUAL_CONCEPT_LEDGER_20260704.json": ("concept ledger v1.1, 6-language labels", "derived", "yes", "yes"),
    "INTERLINGUAL_CONCEPT_LEDGER_20260704.csv": ("concept ledger spreadsheet", "derived", "yes", "yes"),
    "INTERLINGUAL_CONCEPT_LEDGER_20260704.md": ("concept ledger table + unmapped tail", "derived", "yes", "yes"),
    "RING_TERM_DECISION_MEMO_20260704.md": ("flagship review memo — REVIEW PROPOSAL, no verdict", "derived", "yes", "review"),
    "COMPARATIVE_TERM_ANALYSIS_v1_20260704.json": ("37-concept current-vs-alternatives evidence", "derived", "yes", "yes"),
    "COMPARATIVE_TERM_ANALYSIS_v1_20260704.md": ("comparative packet backbone", "derived", "yes", "yes"),
    "SITING_TABLE_v1.md": ("findings->actions + 18-lane siting + do_not_use design", "derived", "yes", "yes"),
    "C2_FILL_DISPATCH_20260704.md": ("per-lane C2 work orders", "derived", "yes", "yes"),
    "C2_FILL_DISPATCH_20260704.json": ("dispatch machine form", "derived", "yes", "yes"),
    "F7_FRENCH_INTERLOCK_NOTE_20260704.md": ("3-lane French cross-reference actions", "derived", "yes", "yes"),
    "PAN_ROMANCE_ACCESS_LEDGER_HANDOFF_20260704.md": ("codex-lane handoff spec", "derived", "yes", "yes"),
    "CHATGPT_PRO_TASK_SPEC_20260704.md": ("outsourcing spec: weighted scoring", "derived", "yes", "yes"),
    "CHATNOTES_STRATUM_D_INVENTORY_20260704.md": ("Stratum-D scan: 827K files/914GB, anchor authors", "derived", "yes", "yes"),
    "chatnotes_stratum_d_scan_20260704.json": ("raw folder scan", "derived", "yes", "yes"),
    "FRAMEWORK_PAPER_SKELETON_20260704.md": ("paper skeleton (superseded by draft)", "derived", "no", "no"),
    "FRAMEWORK_DRAFT_20260704.md": ("draft v0.1 (sections out of order; superseded by ORDERED)", "derived", "no", "no"),
    "FRAMEWORK_DRAFT_ORDERED_20260704.md": ("PAPER DRAFT v0.2, paper order + appendices", "derived", "yes", "review"),
    "AUTHORSHIP.md": ("model/human provenance + idea table", "derived", "yes", "yes"),
    "interslavic_term_decisions_20260704.json": ("222 logbook decisions extraction", "derived", "yes", "yes"),
    "slavic_term_dataset_20260704.json": ("1310 glossary records aggregation", "derived", "yes", "review"),
    "SOURCE_USE_POLICY.md": ("evidence-category policy", "derived", "yes", "yes"),
    "ARTIFACT_INDEX.md": ("this index", "derived", "yes", "yes"),
}
FROZEN_NOTE = "frozen baseline (archaeology; never overwrite)"

lines = ["# Artifact Index", "",
         "2026-07-04. Every file in the program package: role, provenance, sha256 (first 12), citation/externality flags.",
         "`safe_to_show_external: review` = content is sound but contains unreviewed term material or review-sensitive rows; include in reviewer packets, not in public-facing summaries without the honest-limits page.",
         "",
         "| File | Role | Kind | sha256:12 | KB | cite? | external? |",
         "| --- | --- | --- | --- | ---: | --- | --- |"]
entries = []
for f in sorted(P.rglob("*")):
    if not f.is_file() or f.suffix == ".zip":
        continue
    rel = f.relative_to(P).as_posix()
    h = hashlib.sha256(f.read_bytes()).hexdigest()[:12]
    kb = round(f.stat().st_size / 1024, 1)
    if rel.startswith("frozen/"):
        role, kind, cite, ext = FROZEN_NOTE, "frozen", "yes", "yes"
    elif rel.startswith("scripts/"):
        role, kind, cite, ext = "build script (CPU-only)", "script", "yes", "yes"
    elif rel.startswith("data/"):
        role, kind, cite, ext = "curated seed data", "curated", "yes", "yes"
    else:
        role, kind, cite, ext = ROLES.get(rel, ("working artifact", "derived", "no", "review"))[0], \
            ROLES.get(rel, ("", "derived", "no", "review"))[1], \
            ROLES.get(rel, ("", "", "no", "review"))[2], ROLES.get(rel, ("", "", "", "review"))[3]
    lines.append(f"| {rel} | {role} | {kind} | {h} | {kb} | {cite} | {ext} |")
    entries.append({"file": rel, "role": role, "kind": kind, "sha256_12": h, "kb": kb,
                    "safe_to_cite": cite, "safe_to_show_external": ext})

(P / "ARTIFACT_INDEX.md").write_text("\n".join(lines), encoding="utf-8")
(P / "artifact_index_20260704.json").write_text(json.dumps(
    {"artifact": "artifact_index", "generated": "2026-07-04", "entries": entries},
    ensure_ascii=False, indent=1), encoding="utf-8")
print(f"indexed {len(entries)} files")

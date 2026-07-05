# Arabic RTL Zenodo / Completed-Reader Integration Fix Pass

Draft / non-canonical / not native reviewed / not approved. Created 2026-07-04 after Arabic queue draft coverage was verified.

## Why This Pass Was Started

The Arabic RTL queue was verified from disk as exactly six active rows, all draft-covered by corpus slices `AR-SLICE-001` through `AR-SLICE-008`. The coordinator directive then required moving to SGA5/Zenodo or another completed-reader integration/fix pass rather than idling.

The recovery report explicitly warns that SGA5 is not the active Noether translation/interlanguage lane. Therefore this pass takes the Zenodo/source-reader integration route, not an SGA5-led route.

## Live Zenodo Check

Live record checked: `https://zenodo.org/records/20836874`

Observed on the live Zenodo page:

- Version line reports `2026-07-02 R569 current source-control head; R570 no-patch checkpoint; language-lane handoff triaged`.
- The record describes R569 as the current packaged local TeX-changing German source-control head and R570 as the latest no-patch checkpoint.
- The record says R560-R570 are queued for curated rollup because the record is at the Zenodo 100-file ceiling.
- The record explicitly says these are working source-control/support materials, not Noether closure, whole-corpus certification, multilingual synchronization, or critical editions.
- The language-lane handoff says Arabic/Persianate is source-evidence only, with no cumulative Noether reader or final terminology authority.

## Local Reader / Source-Core Findings

Local search under `C:\Users\memo_\Documents\Codex` did not find filenames matching:

- `R569`
- `R570`
- `Noether_R569`
- `Noether_R570`
- `cum_de_R569`
- `cum_de_R570`

Local handoff/source-core notes inspected:

- `NOETHER_SOURCE_CORE_TEXT_TEX_WORKBOOKS_SNAPSHOT_20260629.md`
- `NOETHER_PC_REMOTE_BRANCH_COORDINATION_AUDIT_20260703T124501Z.md`
- `NOETHER_TRANSLATION_INTERLANGUAGE_RECOVERY_REPORT_20260704.md`

Relevant local findings:

- The 2026-06-29 source-core snapshot is a compact source-core package, not a Zenodo replacement.
- It excludes PDFs/images/archive payloads and notes that upload was deferred because of bandwidth constraints.
- The 2026-07-03 remote branch audit reports package frontier 141 and a source-heavy branch with additional docs/manifests/Zenodo metadata scaffolding, but says not to auto-merge it.
- The recovery report says the latest draft language-planning release had CJK codepoint-redo package files, Zenodo live checks, and a multilingual current-release-index refresh, but SGA5 should not drive this wing.

## Integration Risk / Fix Notes

1. Arabic draft corpus slices are correctly anchored to the German baseline explicitly supplied by the parent thread:

   `cum_de_R124plus_localcodex_current_candidate_20260624.tex`

2. Zenodo live metadata now reports later R569/R570 source-control status, but those payloads were not found locally by filename. Therefore this lane must not silently rebase Arabic draft slices to R569/R570.

3. Because R569/R570 are described as tail source-control/no-patch checks and queued for curated rollup, the Arabic draft slices should be labeled as:

   `R124plus-parent-baseline anchored; requires future source-drift comparison against R569/R570 when local payloads are available`.

4. Zenodo's own language-lane status says Arabic/Persianate has no cumulative Noether reader or final terminology authority. The Arabic artifacts produced in this lane are therefore draft corpus translation slices and source-evidence sidecars only, not a reader release.

5. No source/reader fix should be applied to canonical TeX from this lane. Session B or the designated packaging loop should handle Git/Zenodo packaging after review.

## Draft Sidecar Action Taken

This note records the stale-reader/source integration state as a draft sidecar only. It does not modify canonical source, public metadata, reviewer packets, Zenodo records, Git branches, or gate ledgers.

## Follow-Up Ledger

| Item | Action for future packaging/session |
| --- | --- |
| R569/R570 local payloads absent | Locate or fetch through approved packaging workflow before any source-drift comparison. |
| Arabic slices R124plus anchored | Compare affected German anchors against R569/R570 once payloads exist. |
| Arabic no cumulative reader | Do not label Arabic outputs as reader release; keep as draft corpus slices. |
| Zenodo 100-file ceiling | Do not attempt direct loose-file upload from this lane. |
| Source-heavy branch | Reconcile deliberately only if requested; no auto-merge. |


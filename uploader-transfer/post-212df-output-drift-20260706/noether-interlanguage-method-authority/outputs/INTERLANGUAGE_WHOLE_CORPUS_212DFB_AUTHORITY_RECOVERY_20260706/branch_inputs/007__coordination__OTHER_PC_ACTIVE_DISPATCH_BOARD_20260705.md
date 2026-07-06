# OTHER-PC ACTIVE DISPATCH BOARD

Date: 2026-07-05

This file is for the other-PC coordinator and every sibling session it can see.

## Rule

Every session needs a task. Every task needs an output path. Every output needs a logbook entry. Every archive-relevant output needs source bodies or a clear statement that no bodies exist.

Do not let sessions sit idle. If a visible session is waiting, assign it work immediately and record the assignment.

## Coordinator Duties

Maintain these files in the other-PC working folder and push/copy public-safe versions to GitHub:

- `ACTIVE_SESSIONS.md`
- `SIBLING_TASKS.md`
- `SOURCE_BODY_UPLOAD_QUEUE.md`
- `ACKNOWLEDGED_DIRECTIVES.md`
- one `SESSION_LOGBOOK_YYYYMMDD.md` per active session or lane

## Required Row For Every Session

Use one row per visible session:

| Session | Machine | Lane | Current task | Last output path | Logbook path | Blocker | Next action | Last checked |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |

## Dispatch Queue

Assign idle sessions from this queue:

1. Collect literal TeX/source-body corpora for one language or script.
2. Package real source bodies with manifest, byte size, and SHA256.
3. Audit a package for whether it contains real file bodies or only indexes/logs.
4. Apply Fable/ChatGPT-Pro marginal-intelligibility and branch-weight constraints to one terminology block.
5. Repair interlanguage/Interslavic choices that fail source-use or dominance-collapse checks.
6. Inspect generated translations for missing prose, missing formulas, missing tables, missing diagrams, compression, or false completeness.
7. Build a clean web/pro handoff ZIP with bodies, logs, manifests, and a short status file.
8. Update `SOURCE_BODY_UPLOAD_QUEUE.md` with what is still missing.

## Source-Body Rule

Indexes are not enough. URL lists are not enough. Summaries are not enough.

When source bodies exist, upload/push the literal bodies:

- `.tex`, `.ltx`, `.sty`, `.cls`, `.bib`, `.bbl`, `.dtx`, `.ins`
- source archives such as `.zip`, `.tar`, `.tar.gz`, `.source`
- PDFs/scans when they are source witnesses
- lexicons, corpora, term tables, and native mathematical prose sources

Generated drafts are useful only when labeled as generated drafts. OCR witnesses are useful only when labeled as OCR witnesses.

## Interlanguage Blocking Requirement

Any interlanguage or Interslavic session must acknowledge and use:

- `interlanguage-sidecar/FABLE_INTERLANGUAGE_PROGRAM_BLOCKING_DIRECTIVE_20260705.md`
- `interlanguage-sidecar/UPLOAD_ALL_LATEX_SOURCE_BODIES_NOW_20260705.md`
- `coordination/TO_OTHER_AI_LATEX_SOURCE_DIRECTIVE_20260705.md`
- `coordination/OTHER_PC_SESSION_MANAGER_AND_LOGBOOK_DIRECTIVE_20260705.md`

If those are not acknowledged, do not treat the output as coordinated.

## Escalation

If a session cannot push to GitHub, it must still write a local package with:

- task state;
- output paths;
- ZIPs created;
- byte sizes;
- SHA256 hashes;
- source-body counts by extension;
- blockers;
- next action.

Then another session should upload that package.

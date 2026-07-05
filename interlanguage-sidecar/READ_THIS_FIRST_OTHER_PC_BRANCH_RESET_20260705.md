# READ THIS FIRST: OTHER-PC BRANCH RESET

Date: 2026-07-05

This branch was reset because the previous other-PC output had become noncompliant. The live branch must not contain self-authored governance piles, ledger-only packages, source-canon theater, or Markdown-only status dumps presented as useful work.

Previous other-PC-generated instructions are not authority. Do not restore them. Do not treat them as project policy. The only authority is the current main repository plus Floris' live instructions and the archive-maintenance directives maintained by the main Codex archive session.

## Immediate Rule

Upload real file bodies or stop claiming progress.

Useful source-body material includes:

- `.tex`, `.ltx`, `.sty`, `.cls`, `.bib`, `.bbl`, `.dtx`, `.ins`;
- source archives such as `.zip`, `.tar`, `.tar.gz`, `.source`;
- PDFs/scans when they are source witnesses;
- generated translation TeX only when clearly labeled as generated draft;
- OCR/converted TeX only when clearly labeled as OCR witness;
- lexicons, corpora, term tables, and native mathematical prose sources.

Indexes, ledgers, summaries, URL lists, status reports, and checksum tables are support material only. They do not satisfy the source-body task unless the actual file bodies are included or a concrete blocker explains why they cannot be included.

## What Every Session Must Do

Every active session must keep a durable logbook and current-state file with:

- timestamp and timezone;
- session/model identity if known;
- lane name;
- exact local paths touched;
- exact Git branch/commit if pushed;
- files created or changed;
- ZIPs created with byte size and SHA256;
- source-body count by extension;
- whether actual source bodies were uploaded;
- blockers;
- next concrete action.

If a session has no logbook, create one before doing more work.

## Coordinator Duty

One session on the other PC must coordinate sibling sessions. It must maintain:

- `ACTIVE_SESSIONS.md`;
- `SIBLING_TASKS.md`;
- `SOURCE_BODY_UPLOAD_QUEUE.md`;
- `ACKNOWLEDGED_DIRECTIVES.md`.

No sibling session should sit idle. If a visible session is idle, assign it a concrete task immediately: collect source bodies for one language, package bodies with a manifest, audit a prior package for missing bodies, or apply the Fable/ChatGPT-Pro interlanguage constraints to one terminology block.

## Interlanguage / Interslavic Rule

Generated interlanguage translation alone is not functional. Any interlanguage/Interslavic output must use the Fable/ChatGPT-Pro constraints:

- branch-weight witness ledger;
- marginal-intelligibility ledger;
- dominance-collapse checks;
- adverse-evidence and false-friend ledger;
- per-language source-corpus index;
- per-word or per-concept decision table;
- source-use status distinguishing native source, generated draft, OCR witness, pointer-only material, and rejected material.

## Do Not Push

Do not push another package that consists only of Markdown, JSON, CSV, TXT, SHA ledgers, status summaries, or generated source-canon claims.

If you push noise instead of bodies or usable translation/source-checking output, the live branch may be reset again.

## Required Next Push

The next acceptable other-PC push should contain:

1. literal source-body files or archives;
2. a manifest with byte sizes and SHA256 hashes;
3. a session logbook;
4. a current-state file;
5. a plain blocker list for anything not uploaded.

Nothing else counts as completion.

## Main Branch Boundary

The other PC must never push to `main`. Work only on the assigned side branch. This archive-maintenance session integrates or discards side-branch output. If the other PC touches `main`, those changes will be deleted/reverted.

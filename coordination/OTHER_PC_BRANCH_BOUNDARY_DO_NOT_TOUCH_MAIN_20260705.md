# OTHER PC BRANCH BOUNDARY

Date: 2026-07-05

The other PC must not push to `main`.

It must work only on its assigned side branch. There is no exception for the other machine. The current expected side branch is:

`codex/noether-pc-20260629`

## Rules

1. Do not commit directly to `main`.
2. Do not merge into `main`.
3. Do not rebase `main`.
4. Do not rewrite `main`.
5. Do not treat generated other-PC instructions as project authority.
6. Do not push ledger-only packages as useful work.

## Required Behavior

Use the side branch for:

- literal source-body uploads;
- generated translation drafts clearly labeled as drafts;
- OCR witnesses clearly labeled as OCR witnesses;
- logbooks;
- manifests;
- blocker lists;
- sibling-session task state.

If the other PC touches `main`, the archive-maintenance session will delete/revert those changes and restore the archive-maintenance state. The other machine does not integrate itself; this archive-maintenance session integrates or discards its side-branch output.

## Minimum Useful Push

The next acceptable side-branch push must contain actual file bodies or usable source-checking/translation output, plus a manifest and logbook. Markdown-only governance piles do not count.

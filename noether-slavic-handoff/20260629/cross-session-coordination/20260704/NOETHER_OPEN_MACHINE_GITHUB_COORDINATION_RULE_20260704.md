# Noether Open-Machine GitHub Coordination Rule

Timestamp: 2026-07-04.

GitHub is the instruction bus for the open Noether machines.

Operational rule:

- Instructions meant for other machines, lanes, or future sessions must be
  recorded in GitHub-tracked artifacts.
- Local-only machine-to-machine conversations, desktop heartbeat notes, and
  private thread prompts are not authoritative unless they are also made
  GitHub-visible.
- Cross-lane ordering, blocker returns, source-canon prerequisites, package
  gates, and involvement requests should be expressed through committed
  coordination files, package manifests, source-canon ledgers, or PR-visible
  records.
- Language lanes do not push directly. The package/steward lane publishes
  coherent, safety-checked GitHub artifacts from the clean checkout.

Global research program:

- Source canon comes first.
- Every lane must record provenance, URLs, hashes, language/topic evidence, and
  license/access signals before translation claims.
- Generated translations, draft terms, OCR guesses, and bridge output do not
  count as source canon.
- Raw source bodies, zip primaries, credentials, runtime caches, and unredacted
  secret-shaped values must not enter rolling package commits.

Coordination consequence:

- Open machines should pull or inspect the current GitHub branch and PR-visible
  records before acting.
- When a machine needs another lane to act, it should publish a GitHub-tracked
  task record rather than relying on a local conversation.
- When GitHub-tracked instructions conflict with older local side-channel
  notes, follow the newer GitHub-tracked instruction for Noether operations
  while preserving user, safety, clean-checkout, source-license, and credential
  boundaries.

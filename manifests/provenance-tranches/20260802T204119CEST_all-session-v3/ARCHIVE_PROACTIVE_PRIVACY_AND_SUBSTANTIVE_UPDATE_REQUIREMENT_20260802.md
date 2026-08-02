# Archive proactive privacy and substantive-update requirement

Date: 2026-08-02

Status: CONTROLLING USER CORRECTION

## Correction

Archive maintenance is not a passive staging or handoff-waiting role. It owns
the work required to turn a bounded substantive producer update into a safe
archive transport object. A producer's privacy errors are archive-maintenance
work; they are not a reason to wait for the producer to supply an already-clean
package.

## Required archive behavior

For every substantive producer update:

1. Identify the newest bounded coherent source/control generation. A live
   half-written file set is not a coherent snapshot, but no separate formal
   handoff is required once exact bytes can be bounded and replayed.
2. Preserve producer source bytes unchanged. Build a separate derived archive
   projection rather than silently editing or overwriting production history.
3. Perform the privacy audit and remediation in the derived projection. Remove
   or replace private home paths, usernames, machine-local absolute paths,
   temporary directories, credentials/tokens, private correspondence, and any
   other non-public operational residue. Record every transformation and prove
   that the resulting package is privacy-clean.
4. Bind the derived package by exact relative path, byte count, SHA-256,
   manifest membership, provenance, rights/caveats, and supersession state.
5. Include privacy-clean human-readable logbooks, decision rationale,
   append-only revision/reversal/error history, and continuation records.
6. Preserve and publish all in-scope substantive work under the already
   established GitHub and Zenodo concepts. Organize it by corpus, generation,
   provenance, and supersession; do not editorially curate, select, rank,
   summarize away, or omit work. Never create a duplicate concept, competing
   draft, or parallel archive lineage merely because the producer tree changed.
7. Publish and publicly read back the exact provenance/logbook surfaces on both
   the methodology concept DOI `10.5281/zenodo.21124403` and the replication
   concept DOI `10.5281/zenodo.20461174`, as required by
   `PROJECT_LOGBOOK_METHODOLOGY_REPLICATION_DOI_REQUIREMENT_20260802.md`.
8. Verify anonymous public readback of every published file, manifest, DOI,
   GitHub raw URL, and supersession link before closing the update.

## Mandatory reporting granularity

Every substantive archive update must report each identity separately and
exactly. Reports must enumerate:

- every GitHub branch, commit, push/ref, pull request, merge commit, and URL;
- every Zenodo concept, deposition or draft, record/version, DOI, file set, and
  anonymous public-readback identity;
- exact package, manifest, receipt, and provenance-log bytes and SHA-256; and
- explicit unchanged results for categories with no new identity.

A generic statement such as “GitHub/Zenodo updated” is insufficient.

## Boundary retained

Production continues to own translation, transcription, source correction,
mathematical QA, and visual QA. Archive maintenance does not rewrite those
decisions. It does own custody, privacy remediation, derived packaging,
publication transport, catalogs, decision logs, and public readback.

Archive maintenance organizes and preserves; it does not curate. Concept and
transport deduplication prevent duplicate containers but never authorize the
loss of distinct source bytes, drafts, decisions, errors, reversals, or
superseded generations. Privacy redactions in a public projection must be
minimal, mechanically documented, and paired with preserved private custody of
the unchanged original.

An incoherent mid-write state must not be published. This is a byte-coherence
rule, not a requirement to wait for a producer-created privacy-clean package or
formal handoff.

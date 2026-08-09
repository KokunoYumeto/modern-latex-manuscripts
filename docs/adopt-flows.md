# Reusable Adoption Workflows

These protocols give every `workflow` token in the
[adoption board](../manifests/adopt.json) an inspectable meaning. They do not
certify any source, transcription, translation, or mathematical claim. A work
row selects one or more protocols; its map, source basis, prerequisites, and
cursor still define the actual scope.

Use one human-approved exact Git commit. Open an
[adoption issue](https://github.com/KokunoYumeto/modern-latex-manuscripts/issues/new?template=adopt.yml)
with the Board ID, chosen workflow, bounded scope, starting generation, and
stop point. Preserve inputs and predecessors. Return every result, partial
checkpoint, pause, or withdrawal through the
[handback form](https://github.com/KokunoYumeto/modern-latex-manuscripts/issues/new?template=handback.yml).

Every handback must identify the exact achieved scope; output and manifest
paths, bytes, and hashes; checks actually run; failures and reversals; the next
cursor or a terminal statement; and reusable method findings. Do not replace a
missing check with a completion claim. Parallel mirrors are welcome when their
overlap and independent chronology are explicit.

The machine definitions below live inside `manifests/adopt.json`, so the
existing exact four-file consumer remains sufficient. Validation requires
every row token to resolve here and every registered workflow to be used.

## `assembly_review`

Start when existing units or readers may form a coherent whole but their order,
membership, or build closure is uncertain. Replay the exact inventory, compare
it with the claimed scope, and record missing, extra, duplicated, or
contradictory members. Return assembly identities, build or no-build state,
discrepancies, and the next unresolved member.

## `bounded_continuation`

Start only from the exact cursor named by the current map. Freeze the
predecessor and authority, advance one coherent range, preserve decisions and
errors, and stop at the declared boundary or first unresolved source problem.
Return achieved coverage, output identities, decisions, and the next cursor.

## `bounded_pilot`

Use a small representative range when source quality, language feasibility,
layout, or method is not established. State success and failure criteria before
production, freeze the pilot inputs, and keep findings bounded to the pilot.
Return the result, criteria-by-criteria disposition, costs/failures, and a
recommendation to proceed, revise, or stop.

## `bounded_repair`

Start from a reproducible defect and authority witness. Apply the smallest
source-supported change, check local dependencies, and preserve the rejected
preimage and rationale. Stop if the defect cannot be reproduced, authority is
insufficient, or the repair expands into an undefined rewrite. Return before
and after identities, regression evidence, residual defects, and supersession.

## `bounded_transcription`

Freeze one source identity and exact page or line range. Transcribe all
substantive content in order while retaining uncertain glyphs and structural
ambiguities explicitly. Verify coverage against the source. Return editable
text, source-to-target locators, omission/uncertainty ledgers, and the next
source cursor.

## `bounded_translation`

Translate one stable source-aligned range while preserving hypotheses,
numbering, displays, references, and logical force. Record difficult terms and
alternatives; keep process commentary outside the mathematical reader. Return
editable target text, exact source binding, terminology/reversal history,
checks, unresolved risks, and the next cursor.

## `correction_propagation`

Use only after a correction is accepted in the authority or canonical source
layer. Freeze the correction and dependent-target list, update each target
independently, and preserve nonaffected bytes and language-specific decisions.
Return per-target identities, deferred or divergent targets, and remaining
dependency closure.

## `independent_mirror`

Declare scope and overlap before broad production. Preserve independence from
the existing target where claimed, freeze the independent result before
comparison, and then adjudicate disagreements against the source. Return the
mirror URL/commit, chronology, manifest, comparison ledger, and
returned/paused/withdrawn state.

## `independent_review`

Replay a frozen target and check it without editing its bytes. State the source,
structure, language, formula, table, reference, or visual criteria used.
Separate observations from source-adjudicated findings. Return reviewed
identities, per-finding locators, passes/failures/uncertainties, or an explicit
zero-change result.

## `source_audit`

Bind each target unit to the stated ultimate or page-local authority. Check the
bounded text, formulas, numbering, tables, diagrams, and references that the
scope requires. Distinguish target error from source ambiguity. Return locator
coverage, findings and nonfindings, correction candidates, and the next audit
cursor.

## `source_discovery`

Use when no trusted source baseline is bound. Search authoritative repositories
and catalogs, record edition/provenance/access/completeness/quality, and
deduplicate witnesses. Do not present discovery as intake or transcription.
Return candidate identities and dispositions, a selected intake recommendation
or explicit no-source result, and the next lead.

## `source_intake`

Freeze a selected source and record its provenance, exact bytes or remote
identity, page/structure coverage, defects, and applicable rights notes. Keep
OCR and other derivatives distinct from authority. Return the source receipt,
manifest, exclusions, and recommended transcription or audit cursor without
claiming downstream work.

## `source_recovery`

Use when target bytes survive but source, build, manifest, or generation links
are missing. Keep the target unchanged, inspect only bounded candidate roots or
public records, and classify links as proven, probable, conflicting, or
unknown. Return the identity table, proof, conflict ledger, and remaining
lineage cursor.

## `table_audit`

Bind every material table to its source locator. Check headings, cells, order,
continuations, notes, alignment, and symbols; distinguish presentation defects
from content defects. Return row/column coverage, cell-level findings,
unresolved geometry, and the next table or terminal cursor.

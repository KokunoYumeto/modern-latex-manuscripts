# Paper 3 structural build and tool notes

This file is append-only. Corrections must be appended rather than silently replacing earlier entries.

## CJK-KO-P03-STRUCT-FAIL-001

- Time precision: 2026-08-04 (date precision only; no reliable minute was captured).
- Stage: spreadsheet-runtime dependency discovery before CSV projection inspection.
- Symptom: the dependency-loader call returned no payload through repeated bounded waits and was intentionally terminated rather than allowed to block production.
- Attempt rejected: waiting indefinitely for the same call.
- Resolution: reuse the loader-provided `node_modules` junction already established earlier in this same production session at `C:/tmp/codex_p01_csv_019f757c_a43b/node_modules`, whose recorded target is `C:/Users/Floris/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules`.
- Consequence: none for source, target, JSONL, CSV, or the deterministic PowerShell builder/validator. The bounded `@oai/artifact-tool` CSV inspection remains separately evidenced.
- Review state: operational event only; not a source, Korean, formula, or publication finding.
- Revisit condition: only if the established loader-provided runtime becomes unavailable or the CSV inspection fails.

## CJK-KO-P03-STRUCT-FAIL-002

- Time precision: 2026-08-04 (date precision only).
- Stage: first deterministic structural-validator run.
- Symptom: the validator exited 1 with `Index was outside the bounds of the array` at `Validate-Locator`, line 121, before it could emit a report.
- Cause evidence: an invalid or empty inline-fragment occurrence produced a negative/out-of-range position; the existing guard checked only the upper bound before indexing.
- Failed approach preserved: index the extracted fragment after checking only `position >= count`.
- Repair: extend the guard to reject `position < 0` as well as `position >= count`; no JSONL, CSV, source, or target byte was changed by this repair.
- State: validator-tooling crash repaired; any underlying record error remains for the rerun to report and is not prejudged here.
- Review boundary: operational metadata only, not source, Korean, or formula review.
- Revisit condition: rerun the validator and preserve any machine-reported record error or later repair separately.

## CJK-KO-P03-STRUCT-FAIL-003

- Time precision: 2026-08-04 (date precision only).
- Stage: second structural-validator run after FAIL-002 guard repair.
- Symptom: the validator exited 1 at line 178 because a one-item `Sort-Object -Unique` pipeline returned a scalar without a `Count` property under strict mode.
- Cause evidence: the pipeline result itself was not array-wrapped before `.Count`; this is validator control flow, not indexed source/target content.
- Failed approach preserved: call `.Count` directly on a possibly scalar pipeline result.
- Repair: wrap the pipeline result in an array before comparing unique and total basis counts.
- Consequence: validator script and notes changed; JSONL/CSV were deterministically regenerated but source and target TeX were untouched.
- Review boundary: operational metadata only, not source, Korean, or formula review.
- Revisit condition: rerun and preserve the resulting PASS/FAIL without suppressing record-level errors.

## CJK-KO-P03-STRUCT-FAIL-004

- Time precision: 2026-08-04 (date precision only).
- Stage: first validator run that completed and emitted a machine FAIL report.
- Symptom: non-fragment records were serialized with empty-string fragment fields, empty-string parents/relations, and empty-string hashes; this generated many invalid-fragment, root-parent, relation, and expected-formula-count errors.
- Cause evidence: nullable PowerShell parameters were typed as `string`, so bound nulls collapsed to empty strings before locator and hierarchy construction.
- Failed approach preserved: use nullable typed-string parameters for parent and optional fragment values.
- Repair: change only nullable parent/fragment/hash-helper inputs to object-valued parameters so null remains null. Expected formula-count rules are not weakened; the builder must regenerate and satisfy them.
- Consequence: builder-generated JSONL/CSV identities will change; target/source bytes remain untouched.
- Review boundary: metadata serialization repair only, not source, Korean, or formula review.
- Revisit condition: regenerate and rerun the unchanged substantive validator expectations.

## CJK-KO-P03-STRUCT-RES-001

- Time precision: 2026-08-04 (date precision only).
- Exact runtime resolution supplied by the active root session: Node `C:/Users/Floris/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe`; node_modules `C:/Users/Floris/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules`.
- Structural result after FAIL-002 through FAIL-004 repairs: deterministic validator PASS, 148/148 unique records, expected formula inventory restored, errors empty.
- This resolution changes no target/source text and authorizes no review, render, archive release, or publication.

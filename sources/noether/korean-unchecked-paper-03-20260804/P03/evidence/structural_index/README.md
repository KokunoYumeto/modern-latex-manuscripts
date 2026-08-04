# Noether Paper 3 Korean producer structural index

This directory is a mechanical reproducibility layer for the translation producer. It does not perform or imply German source checking, Korean review, formula review, compilation, rendering, publication review, certification, or approval.

## Authoritative and projected forms

- `PRODUCER_STRUCTURAL_INDEX.jsonl` is the hierarchy-preserving authoritative index.
- `PRODUCER_STRUCTURAL_INDEX.csv` is a flat projection. Nested target locators, relations, and record-basis values remain JSON strings in their corresponding CSV fields.
- `PRODUCER_STRUCTURAL_INDEX.schema.json` documents every record field and enumerates structure and relation types.
- `build_structural_index.ps1` deterministically regenerates JSONL and CSV from the fixed specification and current bound inputs.
- `validate_structural_index.ps1` independently checks identities, line-slice and fragment hashes, hierarchy, relations, state constraints, record hashes, exact unit coverage, and the CSV projection.
- `PRODUCER_STRUCTURAL_INDEX_VALIDATION_REPORT.json` is deterministic: it contains no wall-clock timestamp.
- `CSV_ARTIFACT_TOOL_VALIDATION_REPORT.json` records a bounded `@oai/artifact-tool` import/inspection of the CSV projection. Rendering is prohibited by the translation-only role and is not claimed.

## Basis distinctions

- `source_fact` marks explicit TeX structure or wording such as title macros, footnote macros, displays, inline-math delimiters, and citations.
- `computation` marks byte identities, line slices, extracted inline-math occurrences, and container construction.
- `producer_editorial_inference` marks paragraph-internal closed-prose segmentation, descriptive labels, theorem/proof/definition classification where the source uses prose rather than a formal environment, and source/target structural pairing.

All formula pairings use same-line occurrence order only. They are deliberately marked unchecked and are not semantic or formula verification. Record `NOE-P03-KO-U02-FORMULA-028` preserves one mechanically observed target-only inline-math occurrence in the line 3588 / target-line-14 pairing; this is a reproducibility observation, not a defect judgment.

## Cursor

The producer cursor is closed after whole-authority line 3608. Whole-authority lines 3609--3610 are excluded controls. The next action is an independently assigned Korean checker; this index itself authorizes no review work.

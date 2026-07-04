# Computational Pivot Evaluation Protocol

Generated: 2026-07-04T06:21:45Z

Route: D-NOVEL-004

Owner: Session D NOVEL/OWNERLESS

Status: tooling-method only, research-only. This artifact is not a human language standard, not an MT output approval, not a translation lane, and not a term-governance approval.

## Source Basis

- `INTERLANGUAGE_METHOD_BIBLIOGRAPHY_AUTHORITY_MATRIX_20260629.md/json`
- `INTERLANGUAGE_REVIEWER_AUTHORITY_DECISION_FRAMEWORK_20260629.md/json`
- `AI_INTERLANGUAGE_TECHNICAL_REGISTER_METHOD_NOTE_20260703T101500Z.md/json`
- `NOETHER_NOVEL_PACKET_D_NOVEL_004_COMPUTATIONAL_PIVOT_20260704.md`

## Protocol

### 1. Corpus Scope

Record before any computation:

| Field | Required |
| --- | --- |
| Languages/standards | exact list |
| Scripts | exact list |
| Source types | TeX, PDF, HTML, wikitext, glossary, reviewer return, or other |
| License/data rights | captured or unknown |
| Local file hashes | required for local files |
| Exclusion list | rejected or out-of-scope sources |

### 2. Alignment and Normalization

| Component | Required record |
| --- | --- |
| Segmentation | method and version |
| Tokenization | method and version |
| Script normalization | reversible rules or no normalization |
| Formula handling | preserve, mask, align, or exclude |
| Bibliography/labels | protected zones |
| Error log | required |

### 3. Model or Tool Record

| Field | Required |
| --- | --- |
| Tool/model name | required |
| Version/hash | required |
| Parameters | required |
| Training/evaluation split | required if training occurs |
| Prompt/config | required if prompting occurs |
| Runtime notes | required |

### 4. Evaluation

Allowed evaluation claims:

- corpus coverage;
- alignment quality;
- reproducibility;
- extraction recall/precision;
- script-normalization behavior;
- candidate list for human review.

Forbidden evaluation claims:

- human readability;
- native acceptability;
- community acceptance;
- term approval;
- translation readiness;
- language-standard authority.

### 5. Human Review Gate

Any user-facing generated text requires:

- native or near-native technical reviewer;
- domain mathematician reviewer;
- script/orthography reviewer if script is transformed;
- accepted-correction ingestion if anything is to be reused.

### 6. Generated Text Quarantine

Generated text must be stored only as:

- `machine_candidate_not_reviewed`;
- `review_prompt_material`;
- `rejected_candidate`;
- `accepted_by_reviewer_not_yet_ingested`, if a return exists.

It must not be stored as approved translation text.

## Not Approved

This protocol does not approve generated text, terms, bridge surfaces, MT outputs, community consent, native review, pilot readiness, or canonical publication.

## Next Task

Next Session D Priority 1 task:

- D-ACCESS-005: `ACCESS_GAIN_CHILD_LANE_WORKSHEET_BUNDLE_<timestamp>.md/json`.

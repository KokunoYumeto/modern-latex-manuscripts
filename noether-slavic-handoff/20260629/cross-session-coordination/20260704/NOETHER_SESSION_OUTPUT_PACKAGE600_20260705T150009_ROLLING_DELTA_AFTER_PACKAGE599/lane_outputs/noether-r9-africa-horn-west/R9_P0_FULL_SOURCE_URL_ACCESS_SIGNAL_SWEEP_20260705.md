# R9 P0 Full Source URL Access-Signal Sweep

Generated: 2026-07-05T12:59:43.833328+00:00 UTC

## Boundary

This artifact performs a metadata-only HEAD/header sweep for all `P0` rows in `R9_OCR_SOURCE_OWNER_PRIORITY_QUEUE_20260705.csv`: hashable local math source bodies that already have text layers but still need source-owner, license/access, and reviewer gates. It records current URL access signals and header hashes only. It does not download source bodies, save source text, approve licenses, claim review, translate, promote gates, package, stage, commit, or push.

## Summary

- P0 rows swept: 188
- Header JSON records used in final rebuild: 188
- Current 2xx metadata responses: 187
- Non-2xx/error rows: 1
- Rows with local source path still present: 188
- Rows with `body_saved=false`: 188
- Rows with `source_text_saved=false`: 188
- Rows with `promotion_allowed=false`: 188

Validation note: the final CSV/MD was rebuilt from settled header JSON records after stopping an orphaned timed-out probe process. No additional source body or text capture was performed during rebuild.

## Counts By Language

| language/access target | count |
|---|---:|
| Amharic | 3 |
| Oromo | 70 |
| Somali | 62 |
| Tigrigna/Tigrinya | 53 |

## Counts By HTTP Status

| HTTP status | count |
|---|---:|
| 200 | 187 |
| no_status | 1 |

## Counts By Content Type

| content type | count |
|---|---:|
| application/pdf | 187 |
| missing | 1 |

## Counts By Decision

| source gate decision | count |
|---|---:|
| not_admitted_access_probe_failed_or_non_2xx | 1 |
| not_admitted_access_signal_only | 187 |

## Non-2xx Or Error Rows

| probe | language | status | error | url |
|---|---|---:|---|---|
| R9-P0-FULL-ACCESS-188 | Tigrigna/Tigrinya |  | URLError(TimeoutError('timed out')) | https://files.ethiopialearning.com/textbooks/Grade%2008/Grade_8_Subject_MATH_TEACHER_GUIDE_Language_TIGRIGNA_Retrieved_20150101.pdf |

## Source-Gate Reading

A 2xx `application/pdf` response is a current access signal only. It does not clear source-owner, attribution, license/reuse, reviewer, OCR/register, or translation gates. Rows remain local-body provenance and source-return work orders, not accepted translation evidence.

CSV: `C:\Users\memo_\Documents\Codex\2026-07-04\noether-r9-africa-horn-west\outputs\R9_P0_FULL_SOURCE_URL_ACCESS_SIGNAL_SWEEP_20260705.csv`

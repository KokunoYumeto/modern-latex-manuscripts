# Manual/source review triage - 2026-06-30

This artifact triages extraction-mismatch rows that remain blocked before reviewer-packet population. It is not native review, not a populated packet, and not a term approval ledger.

Companion machine-readable file: `MANUAL_SOURCE_REVIEW_TRIAGE_20260630.json`

## Totals

- Manual/source-review rows: 37
- High-priority rows: 34
- Medium-priority rows: 3
- Pages checked in blocked rows: 836
- Cache-missing source records: 0
- Hash-mismatch source records: 0
- Approved terms: 0
- Accepted corrections: 0

## Issue Classes

| Issue class | Rows |
| --- | ---: |
| rtl_register_or_extraction_variant_manual_review | 16 |
| specialist_term_variant_or_anchor_manual_review | 21 |

## Lane Summary

| Lane | Rows | High | Medium | Pages checked | Issue classes |
| --- | ---: | ---: | ---: | ---: | --- |
| arabic | 3 | 3 | 0 | 36 | rtl_register_or_extraction_variant_manual_review:3 |
| fa_IR | 10 | 7 | 3 | 316 | rtl_register_or_extraction_variant_manual_review:10 |
| prs_AF | 3 | 3 | 0 | 34 | rtl_register_or_extraction_variant_manual_review:3 |
| simplified_chinese | 11 | 11 | 0 | 188 | specialist_term_variant_or_anchor_manual_review:11 |
| spanish | 10 | 10 | 0 | 262 | specialist_term_variant_or_anchor_manual_review:10 |

## Triage Rows

| Term ID | Lane | English concept | Domain | Priority | Pages | Issue class | Recommended action |
| --- | --- | --- | --- | --- | ---: | --- | --- |
| `term-zh-hans-0011` | simplified_chinese | right module | module_theory | high | 1 | specialist_term_variant_or_anchor_manual_review | perform_specialist_term_manual_review_and_record_context_note_without_source_quote |
| `term-zh-hans-0012` | simplified_chinese | submodule | module_theory | high | 1 | specialist_term_variant_or_anchor_manual_review | perform_specialist_term_manual_review_and_record_context_note_without_source_quote |
| `term-zh-hans-0013` | simplified_chinese | tensor product | module_theory | high | 10 | specialist_term_variant_or_anchor_manual_review | perform_specialist_term_manual_review_and_record_context_note_without_source_quote |
| `term-zh-hans-0014` | simplified_chinese | module | module_theory | high | 39 | specialist_term_variant_or_anchor_manual_review | perform_specialist_term_manual_review_and_record_context_note_without_source_quote |
| `term-zh-hans-0015` | simplified_chinese | module homomorphism | module_theory | high | 3 | specialist_term_variant_or_anchor_manual_review | perform_specialist_term_manual_review_and_record_context_note_without_source_quote |
| `term-zh-hans-0021` | simplified_chinese | Noether/Noetherian | noetherian | high | 3 | specialist_term_variant_or_anchor_manual_review | perform_specialist_term_manual_review_and_record_context_note_without_source_quote |
| `term-zh-hans-0022` | simplified_chinese | irreducible representation | representation_theory | high | 43 | specialist_term_variant_or_anchor_manual_review | perform_specialist_term_manual_review_and_record_context_note_without_source_quote |
| `term-zh-hans-0023` | simplified_chinese | semisimple | representation_theory | high | 8 | specialist_term_variant_or_anchor_manual_review | perform_specialist_term_manual_review_and_record_context_note_without_source_quote |
| `term-zh-hans-0024` | simplified_chinese | completely reducible | representation_theory | high | 10 | specialist_term_variant_or_anchor_manual_review | perform_specialist_term_manual_review_and_record_context_note_without_source_quote |
| `term-zh-hans-0025` | simplified_chinese | character | representation_theory | high | 44 | specialist_term_variant_or_anchor_manual_review | perform_specialist_term_manual_review_and_record_context_note_without_source_quote |
| `term-zh-hans-0026` | simplified_chinese | group algebra | representation_theory | high | 26 | specialist_term_variant_or_anchor_manual_review | perform_specialist_term_manual_review_and_record_context_note_without_source_quote |
| `term-es-0008` | spanish | module | module_theory | high | 21 | specialist_term_variant_or_anchor_manual_review | perform_specialist_term_manual_review_and_record_context_note_without_source_quote |
| `term-es-0009` | spanish | quotient module | module_theory | high | 6 | specialist_term_variant_or_anchor_manual_review | perform_specialist_term_manual_review_and_record_context_note_without_source_quote |
| `term-es-0010` | spanish | tensor product | module_theory | high | 1 | specialist_term_variant_or_anchor_manual_review | perform_specialist_term_manual_review_and_record_context_note_without_source_quote |
| `term-es-0011` | spanish | submodule | module_theory | high | 21 | specialist_term_variant_or_anchor_manual_review | perform_specialist_term_manual_review_and_record_context_note_without_source_quote |
| `term-es-0016` | spanish | Noetherian ring | noetherian | high | 42 | specialist_term_variant_or_anchor_manual_review | perform_specialist_term_manual_review_and_record_context_note_without_source_quote |
| `term-es-0017` | spanish | Noetherian | noetherian | high | 58 | specialist_term_variant_or_anchor_manual_review | perform_specialist_term_manual_review_and_record_context_note_without_source_quote |
| `term-es-0018` | spanish | irreducible | representation_theory | high | 63 | specialist_term_variant_or_anchor_manual_review | perform_specialist_term_manual_review_and_record_context_note_without_source_quote |
| `term-es-0019` | spanish | representation | representation_theory | high | 29 | specialist_term_variant_or_anchor_manual_review | perform_specialist_term_manual_review_and_record_context_note_without_source_quote |
| `term-es-0020` | spanish | irreducible representation | representation_theory | high | 2 | specialist_term_variant_or_anchor_manual_review | perform_specialist_term_manual_review_and_record_context_note_without_source_quote |
| `term-es-0021` | spanish | semisimple | representation_theory | high | 19 | specialist_term_variant_or_anchor_manual_review | perform_specialist_term_manual_review_and_record_context_note_without_source_quote |
| `term-fa-ir-0004` | fa_IR | submodule | module_theory | high | 42 | rtl_register_or_extraction_variant_manual_review | perform_rtl_register_manual_review_and_record_context_note_without_source_quote |
| `term-fa-ir-0005` | fa_IR | tensor product | module_theory | high | 17 | rtl_register_or_extraction_variant_manual_review | perform_rtl_register_manual_review_and_record_context_note_without_source_quote |
| `term-fa-ir-0006` | fa_IR | module | module_theory | high | 51 | rtl_register_or_extraction_variant_manual_review | perform_rtl_register_manual_review_and_record_context_note_without_source_quote |
| `term-fa-ir-0007` | fa_IR | free module | module_theory | high | 23 | rtl_register_or_extraction_variant_manual_review | perform_rtl_register_manual_review_and_record_context_note_without_source_quote |
| `term-fa-ir-0009` | fa_IR | left module | module_theory | high | 22 | rtl_register_or_extraction_variant_manual_review | perform_rtl_register_manual_review_and_record_context_note_without_source_quote |
| `term-fa-ir-0013` | fa_IR | Noetherian | noetherian | high | 38 | rtl_register_or_extraction_variant_manual_review | perform_rtl_register_manual_review_and_record_context_note_without_source_quote |
| `term-fa-ir-0015` | fa_IR | representation | representation_theory | high | 41 | rtl_register_or_extraction_variant_manual_review | perform_rtl_register_manual_review_and_record_context_note_without_source_quote |
| `term-prs-af-0002` | prs_AF | field | field_theory | high | 20 | rtl_register_or_extraction_variant_manual_review | perform_rtl_register_manual_review_and_record_context_note_without_source_quote |
| `term-prs-af-0003` | prs_AF | simple | representation_theory | high | 2 | rtl_register_or_extraction_variant_manual_review | perform_rtl_register_manual_review_and_record_context_note_without_source_quote |
| `term-prs-af-0004` | prs_AF | ring | ring_theory | high | 12 | rtl_register_or_extraction_variant_manual_review | perform_rtl_register_manual_review_and_record_context_note_without_source_quote |
| `term-ar-0003` | arabic | Artinian | finiteness | high | 4 | rtl_register_or_extraction_variant_manual_review | perform_rtl_register_manual_review_and_record_context_note_without_source_quote |
| `term-ar-0004` | arabic | homomorphism | morphism | high | 12 | rtl_register_or_extraction_variant_manual_review | perform_rtl_register_manual_review_and_record_context_note_without_source_quote |
| `term-ar-0005` | arabic | isomorphism | morphism | high | 20 | rtl_register_or_extraction_variant_manual_review | perform_rtl_register_manual_review_and_record_context_note_without_source_quote |
| `term-fa-ir-0017` | fa_IR | ideal | ring_theory | medium | 41 | rtl_register_or_extraction_variant_manual_review | perform_rtl_register_manual_review_and_record_context_note_without_source_quote |
| `term-fa-ir-0018` | fa_IR | prime ideal | ring_theory | medium | 23 | rtl_register_or_extraction_variant_manual_review | perform_rtl_register_manual_review_and_record_context_note_without_source_quote |
| `term-fa-ir-0019` | fa_IR | maximal ideal | ring_theory | medium | 18 | rtl_register_or_extraction_variant_manual_review | perform_rtl_register_manual_review_and_record_context_note_without_source_quote |

## Boundaries

- No source-language term strings or source passages are copied here.
- No credentials or tokens are copied here.
- No network action, GitHub upload, or reviewer send is performed here.
- Triage classes are local workflow labels, not reviewer decisions.
- Rows remain blocked until manual/source review notes are recorded.
- No term is approved for canonical use by this artifact.

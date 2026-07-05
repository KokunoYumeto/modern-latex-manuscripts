# R9 Tigrigna/Tigrinya Script OCR Triage

Generated: 2026-07-04

Lane: Session H - Africa/Horn/West Africa source-return.

Scope: continuation of the R9 Tigrigna/Tigrinya source-return lane after the whole-lane coverage proof. This artifact does not approve terms, does not draft canonical Noether prose, does not claim native/community review, and does not clear license reuse. It records exact source/OCR/Unicode decisions so reviewers and Session B can see what is usable as source support and what remains blocked.

## Source Basis

- Canonical report: `C:\Users\memo_\Documents\Codex\2026-06-09\could-you-look-online-for-me\work\noether-slavic-canonical\logs\R9_TIGRIGNA_TIGRINYA_CURRENT_SOURCE_RETURN_PASS2_20260703T172503Z.md`
- Canonical CSV: `C:\Users\memo_\Documents\Codex\2026-06-09\could-you-look-online-for-me\work\noether-slavic-canonical\logs\R9_TIGRIGNA_TIGRINYA_CURRENT_SOURCE_RETURN_PASS2_20260703T172503Z.csv`
- Source root: `C:\Users\memo_\Documents\Codex\2026-06-09\could-you-look-online-for-me\work\noether-slavic-canonical\sources\non_slavic_reference_corpus\20260703T172503Z_r9_tigrigna_tigrinya_pass2`
- Canonical pass result: 84 candidates, 82 downloaded PDFs, 3420 pages, 53 extractable Ethiopic-text rows, 33 seed rows reconfirmed.

## Tooling Notes

- Direct Poppler executable rendering worked from `C:\Users\memo_\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe`.
- Rendered visual samples:
  - `work\tmp\pdfs\tigrigna_triage\003_extractable_g1_teacher-001.png`
  - `work\tmp\pdfs\tigrigna_triage\005_weak_g1_ch11-1.png`
- Visual inspection showed real Ethiopic/Tigrigna script on both sampled pages.
- Pypdf extraction was used only as a text-layer diagnostic. It is not treated as translation evidence.

## Decisions

| Slice | Source index | Source item | Canonical text status | Pypdf text-layer finding | OCR/Unicode decision | Responsible use | Next action |
| --- | ---: | --- | --- | --- | --- | --- | --- |
| TG-OCR-001 | 3 | Grade 1 Tigrigna teacher guide | `extractable_ethiopic_text`; 1002 Ethiopic chars; 2 Latin mojibake markers | 146 pages; 2704424 chars; 1004 Ethiopic chars; 2 mojibake markers; Ethiopic appears on pages 2, 3, 11, 144 | Visible Tigrigna source is present, but the ASCII-heavy text layer is too noisy to trust as corpus text without cleanup. | Source pointer and reviewer-facing visual evidence only. No term/prose extraction. | Run font/text-layer audit before any line-level extraction; ask reviewer to verify page wording. |
| TG-OCR-002 | 4 | Grade 1 Chapter 10 | `extractable_ethiopic_text`; 247 Ethiopic chars; 0 mojibake markers | 13 pages; 552 chars; 337 Ethiopic chars; Ethiopic appears on every page | Small clean-text candidate, but the canonical and pypdf counts differ enough to require page-level spot checks. | Non-canonical arithmetic/register support candidate after page audit. | Compare rendered pages to extracted text before creating reviewer prompts. |
| TG-OCR-003 | 5 | Grade 1 Chapter 11 | `weak_or_empty_text_extraction`; 85 Ethiopic chars | 5 pages; 217 chars; 130 Ethiopic chars; visible page sample has clear Tigrigna script | Weak extraction despite visible source. Treat as OCR/transcription work, not reusable text. | Source-return blocker row and visual pointer. | OCR or manual transcription pass, then reviewer verification. |
| TG-OCR-004 | 6 | Grade 1 Chapter 12 | `weak_or_empty_text_extraction`; 36 Ethiopic chars | 3 pages; 88 chars; 36 Ethiopic chars | Weak text layer with very small source text count. | Blocked closure row only. | OCR or manual transcription pass. |
| TG-OCR-005 | 7 | Grade 1 Chapter 13 | `extractable_ethiopic_text`; 120 Ethiopic chars | 4 pages; 196 chars; 120 Ethiopic chars; Ethiopic appears on every page | Clean small extraction candidate for page-level audit. | Non-canonical source support candidate only. | Page-render/text comparison before reviewer-facing corpus slice. |
| TG-OCR-006 | 14 | Grade 1 Chapter 7 | `weak_or_empty_text_extraction`; 48 Ethiopic chars | 4 pages; 106 chars; 48 Ethiopic chars | Weak text layer; do not promote. | Blocked closure row only. | OCR or manual transcription pass. |

## Reviewer Questions

- Confirm whether `Tigrigna` vs `Tigrinya` should remain dual-labeled for this source shelf or be normalized for reviewer-facing work orders.
- For rows 004 and 007, verify line-level wording after text/render comparison before any Noether/German concept prompt uses the source terms.
- For rows 003, 005, 006, and 014, decide whether OCR repair or reviewer transcription is the least risky closure route.

## Boundary

All rows in the companion CSV have `promotion_allowed=false`. The only permitted downstream use is non-canonical source support, OCR repair, reviewer-question preparation, or Session-B package hygiene. No native/community review, license approval, accepted term ledger, pilot readiness, or Git push is claimed here.

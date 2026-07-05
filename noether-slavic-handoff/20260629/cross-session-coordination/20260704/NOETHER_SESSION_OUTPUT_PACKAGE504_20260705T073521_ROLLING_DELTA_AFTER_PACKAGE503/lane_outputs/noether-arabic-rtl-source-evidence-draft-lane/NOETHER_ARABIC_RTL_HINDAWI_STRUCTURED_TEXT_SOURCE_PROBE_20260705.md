# Noether Arabic RTL Hindawi / Safahat Structured Text Source Probe

Created: 2026-07-05

Status: draft source-canon/provenance bookkeeping only. Non-canonical, not native reviewed, not approved, not license-cleared, not a translation artifact, not a package, and not a completion claim.

## Purpose

This heartbeat continuation checks whether Arabic Hindawi/Safahat structured book material can add target-language source-canon provenance for the Arabic lane. It is deliberately typed as a weak fallback: two PDFs and derived text extracts were captured, while HTML and EPUB access remained blocked from the lane shell. No TeX, LaTeX, arXiv, e-print, or source archive was found or admitted.

## Cached Witnesses

| Row | Source | Local hash | Use |
| --- | --- | --- | --- |
| `AR-HIND-20260705-003` | Ian Stewart, `ما الفائدة؟: الفعالية اللامعقولة للرياضيات` | `02FBED157F08BC88993B16E881D5AF0EF0235EF13AA615A950ED36D9ECB4C5C4` | Weak popular-math PDF fallback with adjacent Arabic ring/field vocabulary. |
| `AR-HIND-20260705-004` | Peter M. Higgins, `الأعداد: مقدمة قصيرة جدًّا` | `9CB2E39B9EEED600169E8E585F03B971000010C6BA6CE05A1FF925ECE1A6007F` | Weak popular-math PDF fallback with matrix/linear-operation vocabulary. |
| `AR-HIND-20260705-005` | Derived fulltext extracts | `E08C5125C3C06E5D23DD6EF74D15A0510C4B64F9275AE53AFA6830F67E460F86`; `E3E4D9864402FF5F2A4A0DD785D2AFC791379D6BA13B9ECCFF0E2DADCBE48E7C` | Verification artifacts only; not layout-safe. |

Direct PDF `HEAD` checks returned HTTP `200`, `application/pdf`, and content lengths matching the local cached files:

- `https://downloads.hindawi.org/books/94717039.pdf` -> `20543647` bytes.
- `https://downloads.hindawi.org/books/40259539.pdf` -> `5263323` bytes.

## Verification Text Signals

The PDF extracts contain Arabic presentation forms and bidi controls. Exact searches were therefore run after Unicode NFKC normalization.

`ما الفائدة؟` normalized extract counts:

- `حلقة`: 14
- `حقل`: 12
- `الحقول`: 10
- `مصفوف`: 5
- `الخطية`: 12

`الأعداد` normalized extract counts:

- `حلقة`: 1
- `حقل`: 5
- `مصفوف`: 20
- `الخطية`: 5
- `التحولات الخطية`: 1
- `نظرية التمثيل`: 1

These counts support coarse provenance only. They do not authorize target terms, formula placement, punctuation, or translation choices.

## Access Blockers

The chapter URLs redirect to Safahat/Hindawi HTML and are visible through browser/web metadata, but shell `HEAD`/`GET` checks returned HTTP `403 Forbidden`:

- `https://www.hindawi.org/books/94717039/5/`
- `https://www.hindawi.org/books/40259539/8/`

EPUB attempts also returned HTTP `403 Forbidden`; only 80-byte blocker notes were cached, both with hash `2620B98BF76B8E804CE5DD6AF9DCC757E171901332B55CD7B0C04AE07BE7A829`. No EPUB payload is counted as a witness.

## Source-Package Status

This pass found no Arabic mathematical TeX/LaTeX/arXiv/e-print/source archive. The admitted evidence is:

- 2 accessible Arabic PDFs.
- 2 derived fulltext extracts.
- 2 EPUB blocker notes.
- 1 explicit source-package/gap row.

The PDFs are useful as weak Arabic mathematical prose provenance, not as specialist algebra/invariant-theory source canon. The direct Arabic source-package gap remains open.

## RTL / Layout Notes

The extracted text has Arabic presentation forms, bidi controls, mixed Arabic/Latin/math segments, and formula-neighboring layout risks. NFKC normalization recovers searchable vocabulary, but the extracts must not be used for canonical RTL punctuation, TeX formula-neighboring layout, PDF line breaking, or reviewer-packet text.

No visual PDF QA was performed in this pass.

## Boundary

No raw source bodies are placed in `outputs`. Local cached PDFs, derived text, and blocker notes stay under `sources/...` for provenance hashing. This pass makes no translation, glossary, term approval, bridge promotion, native-review, canonical-approval, license-clearance, gate-promotion, reviewer-packet, package, Git staging, commit, or push claim.

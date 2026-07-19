# Deligne and Griffiths IAS Force-OCR Intake

Date: 2026-07-19

Classification: metadata-only OCR witness, locator, and local completeness
control. This is not a transcription authority, source-audited edition,
critical edition, mathematical certification, or publication of the OCR text.

## Why this intake exists

Claude reran the born-digital IAS `[text]` PDFs for Deligne and Griffiths with
Marker's `force_ocr` path. The earlier OCR had lifted damaged embedded text
layers, preserving malformed accents and loose Unicode mathematics. The rerun
rendered the pages and applied fresh Surya OCR instead.

The result is useful for locating words, estimating expected prose extent,
checking whether a candidate transcription has skipped material, and checking
whether the locally enumerated born-digital subset has a corresponding OCR
output. It does not establish what the source says at formula or glyph level.

## Recomputed inventory

| Author and set | Works / batches | Pages | Files | Bytes | Set digest |
|---|---:|---:|---:|---:|---|
| Deligne combined Markdown | 24 works | 656 | 24 Markdown | 1,838,499 | `7EC766C950036CA3E5B674B9686D78ADB353B7AA8CD5957B0862D4E195BF748F` |
| Deligne raw force-OCR | 46 batches | 656 | 46 Markdown, 46 JSON, 48 JPEG | 2,795,472 | `80AD441CD37A7C5293ED31FDD2D6E4C070989095BD878B290F388DA79D9F41BA` |
| Griffiths combined Markdown | 23 works | 913 | 23 Markdown | 2,000,655 | `644D1D62BBAFB5C06554F0E259244C5445582367774FB52863D0FE9F8AA128B1` |
| Griffiths raw force-OCR | 56 batches | 913 | 56 Markdown, 56 JSON, 104 JPEG | 3,979,153 | `5DC873039481ECA742A1A8118F0DD4EEA1C0DF21286FE3F4128EAA9A1A18D3F0` |
| **All inventoried sets** | **47 works / 102 batches** | **1,569** | **403** | **10,613,779** | `A9022DAE0AF8FB261DA092DCF0A804A1110C48479725727C4B447838A64950DF` |

Each digest is SHA-256 over UTF-8, without a BOM, of the set's rows sorted by
`relative_path` using ordinal comparison, serialized as
`SHA256<TAB>bytes<TAB>relative_path<LF>`. The complete 403-row member inventory
is
`20260719_claude_ias_force_ocr_deligne_griffiths_files.csv` (135,738 bytes,
SHA-256
`ADBF6AA7763D2BA7B971877C7289BC00A369F6592982188AD072C9A3FA2C524C`).

## Producer-reported QA delta

| Author | Metric | Earlier lifted-text OCR | New force-OCR |
|---|---|---:|---:|
| Deligne | Broken accents | 3,610 | 0 |
| Deligne | Flagged artifact rate | 27% | 0% |
| Deligne | Loose/stray math glyphs | 2,319 | 17 |
| Griffiths | Broken accents | 68 | 1 |
| Griffiths | Flagged artifact rate | 32% | 0% |
| Griffiths | Loose/stray math glyphs | 1,164 | 15 |
| Griffiths | Approximate characters | 1,452k | 1,965k |

These quality counts are producer-reported diagnostics, not an independent
word- or formula-accuracy certification. Archive maintenance independently
recomputed file counts, bytes, SHA-256 values, subset page totals, extension
counts, and the set digests above.

## Completeness boundary

- Deligne covers all 24 born-digital `[text]` works in the local page-count
  control, totaling 656 pages. It is not a claim about every Deligne work,
  every IAS item, or source-level completeness.
- Griffiths covers all 23 born-digital `[text]` works in the local page-count
  control, totaling 913 pages. The earlier parked OCR omitted parts of several
  works, including the 211-page `PUTangSp`; the force-OCR subset fills that
  local born-digital gap.
- The separate Griffiths image-scan grind remains incomplete. Those scans are
  a different plain-OCR job and are not made complete by this receipt.
- Parent-PDF hashes and work-to-source-page maps were not supplied in this
  bounded intake. That is a remaining evidence gap for page-level promotion.

## Rights and public projection

The combined Markdown and raw Markdown/JSON contain full modern scholarly
works. The JPEGs are OCR-derived or source-linked visual material. Their
redistribution rights are unresolved, so all 403 members are recorded as
`metadata_only_rights_unresolved`; none of those bodies or images is copied
into this repository by this intake.

Public GitHub receives only this receipt, the machine-readable summary, and
the per-file hash inventory. No Zenodo object is created from this metadata
alone. A Deligne production manager received the local witness location as a
receipt-only note without restarting the production task.

## Control hashes

- Deligne producer README: 2,369 bytes, SHA-256
  `AF5C7F99FA7916864921CC0AF5AE7316D41E2124067F25649329031353B29842`.
- Griffiths producer README: 2,054 bytes, SHA-256
  `6E6E2C18341F9D71361FF66E60CAA4289994C33844B608419191D98B76EBD3D0`.
- Producer conversation receipt: 8,431 bytes, SHA-256
  `138CD1DE2EDF07875BCEFD35DD11D9D897A40EC77EF8CA1B21CC19807262D530`.

Use the OCR to locate and measure. Before changing a mathematical text, return
to the source page and record the accepted or rejected reading.

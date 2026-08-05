# EGA 0–IV complete linked English reader

Date: 2026-08-01

Status: **TECHNICAL PASS — complete global reader; rights/publication decision remains separate**.

## Scope and result

This no-overwrite successor combines the complete English readers for EGA 0,
I, II, III, and IV into one continuously navigable PDF. It has one title page,
one global table of contents, explicit volume title pages, counter resets at
each volume, working same-volume and cross-volume references, and one
consolidated bibliography.

The standalone readers remain separate, valid deliverables. This successor
does not overwrite or duplicate their prior archive handoffs.

## Exact identities

- Active source: 127 files / 7,279,735 B.
- Active-source manifest: `controls/ACTIVE_SOURCE_SHA256.csv` — 127 rows /
  13,797 B — SHA-256
  `E5614FC0F8DF1E1CFC39EDA6C921ADC8513949BA05B4FB7875C93B619A2944F5`.
- Master: `source/EGA_English_Global_0_IV.tex` — 1,688 B —
  SHA-256 `8147C8FDB1B5EBEA69FDB02AA7C192F8267CCA9ABE887AFD3B11B179CE7A7CC1`.
- Reader: `build/EGA_English_Global_0_IV.pdf` — 1,356 A4 pages /
  8,588,550 B — SHA-256
  `3B9D399515AA074C22D3DF6C6F0F7349954444D7BCF980B87CCE5CAED671928A`.
- Validation: `controls/GLOBAL_READER_VALIDATION.json`.

## Build and reference closure

The final two XeLaTeX passes produced byte-identical AUX, OUT, and TOC state.
Fatal errors, undefined references, multiply-defined labels, duplicate
destinations, missing characters, rerun requests, and overfull boxes are all
zero.

PDF replay found 15,383 named destinations and 17,808 internal GoTo actions,
with zero broken actions. References unavailable within EGA 0–IV remain
visible and deliberately unlinked rather than being routed to false targets.

## PDF and visual closure

The PDF contains no image objects. All 29 font resources are embedded Type 1C
fonts; Type 3 count is zero. Active source and PDF privacy scans found zero
private-path hits.

Lead visual review covered 31 context pages spanning front matter, every volume
boundary, long tables, and the terminal bibliography. Seventeen direct
1,100-dpi crops checked every reformatted formula/table site. No clipping,
collision, malformed formula, or broken volume seam was found.

## Honest hold

The package makes no blanket license claim. French authority PDFs and OCR
witnesses are excluded. A public-rights decision and any archive/publication
action remain outside this technical PASS.

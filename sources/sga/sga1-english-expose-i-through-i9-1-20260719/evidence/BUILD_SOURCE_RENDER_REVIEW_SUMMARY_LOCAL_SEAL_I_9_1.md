# Build, source, render, and review summary — SGA 1 through I.9.1

Date: 2026-07-19 (Europe/Berlin).

## Final local build

Build root:
`build/i9_1_working_r7_isolated_final_source_20260719`.

- Input cumulative TeX: 18,709 bytes, SHA-256
  `C6B9C7BF1F204E706E7B06889414651A8510B9E376CD6099599467A4E911C2B1`.
- Final I.9.1 fragment: 2,848 bytes, SHA-256
  `BBDE49C52927FE7817B5B5D788488144B21DA1B5481CDFF8D4F5212D8098A4F8`.
- Final PDF: 16 A4 pages / 544,941 bytes, SHA-256
  `69BA64D47E4FE5AE9F65C461C15F7F523FF385B32636CBCAFA7D9FE0C2504364`.

Three isolated LaTeX passes were retained separately:

| Pass | Exit | Recorded diagnostics | Log SHA-256 | PDF result |
|---|---:|---:|---|---|
| 1 | 0 | 62 bootstrap reference/rerun diagnostics | `25995FDFF3E662869CC92D108B43AE3835665A09378CD70537E6BE4EFF6D6F90` | 552,486 bytes |
| 2 | 0 | 0 | `C0D2997DFB6A61846E3F1794587782228C646698730FDB9BB0587D23902936E1` | 544,941 bytes |
| 3 | 0 | 0 | `C0D2997DFB6A61846E3F1794587782228C646698730FDB9BB0587D23902936E1` | 544,941 bytes |

Passes 2 and 3 have byte-identical console and log evidence. Their PDFs have
the same byte count but different creation metadata, so their file hashes are
not expected to match. The pass-3 PDF is the selected local reader.

## Rejected and superseded build history

- r1: rejected math-delimiter failure.
- r2: rejected because stale root auxiliary state produced a false successful
  compiler exit with unresolved references.
- r3: rejected isolated-copy path failure.
- r4: compiled, but superseded after visual review found a stranded closing
  paragraph on a sparse final page.
- r5: visually clean, but rejected by independent source-structure review.
- r6: rejected because `LiteralPath` treated a wildcard literally and copied
  no fragments.
- r7: final local successor after source correction and enumerated-file copy.

Every failed surface remains preserved and is marked non-promotable in the
JSONL revision history.

## PDF controls

Direct PDF inspection reports a populated title, author, subject, creator, and
keywords; PDF 1.5; 16 unrotated A4 pages; unencrypted; no forms, JavaScript,
or suspects. All 30 fonts are embedded, subset, and Unicode-mapped.

## Render controls

- Render A and B: 16 pages each / 6,262,810 bytes each.
- 16/16 page images are byte-identical.
- Ordered `name|bytes|sha256` manifest digest:
  `AC2110CA1B093A75092C7F5FE1E0FB326FB678F78F023D62DDECEF79E9F9F331`.
- New page 16 PNG: 300,087 bytes, SHA-256
  `6E797F6C81B5348AFF82C44AFA381721D26116384ED6EFC35769D03A95812A25`.
- Cumulative body pages 4--15 are 12/12 byte-identical to the frozen I.8 r4
  render evidence; ordered comparison digest
  `9CF9CC6F694DE7746C4A8234E97645F87B162137536985F4733BC5B7D6BE25B4`.

## Machine gate

The current validator passes 382 CSV data rows and 176 JSONL records with
zero failures. This is a local unit seal; public exact-set freeze, custody,
publication, and remote readback are separate gates.

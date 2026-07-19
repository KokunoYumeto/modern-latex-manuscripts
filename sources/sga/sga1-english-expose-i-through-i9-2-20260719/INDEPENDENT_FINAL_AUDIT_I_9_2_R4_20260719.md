# Independent final audit — SGA 1 duplicate-numbered I.9.2 r4

Result: **PASS — no blocker to the bounded local seal.**

This receipt does not claim a public exact-set freeze, archive acceptance,
publication, mathematical certification, human scholarly peer review, or
complete SGA 1 coverage.

## Source and target

- French authority envelope: `smf_doc-math_3_01.tex` lines 1704--1721,
  539 bytes, SHA-256
  `55F044CF7103997F3B2705898EAAF4CBDD40B4551C44A1A10C3C5509AE1D5980`.
- Exact excluded cursor: line 1722, 19 bytes, SHA-256
  `50DC75EA126D97F233DCA54B8E8DE47B2BB2E4ADF795965DCDF362804F05D174`.
- Fragment: 1,370 bytes, SHA-256
  `510FB1A44CAE30C12ADDB0046EB31B232A93550493A00405CBDF4C7AF3395579`.
- Cumulative TeX: 18,833 bytes, SHA-256
  `7C7FD36084FF4891F943508620D20A91BCDE669114C3C149FADF99E1B95F23B2`.

The corrected `orig=false` branch, theorem hierarchy, two visible I.9.2
numbers, implication directions, surjectivity conditions, page coordinates,
and statement-complete/proof-deferred boundary all pass. French TeX remains
sole text authority; external English witnesses are target controls only.

## Build, anchors, and render

- Clean r4 PDF: 16 A4 pages / 545,957 bytes; SHA-256
  `A5C59DB6149BA82A443F919DFCF5952277D994FFF07B2B614A34BB150525C904`.
- Pass-two and pass-three logs: each 28,556 bytes; SHA-256
  `0181AD5749C6BD3F9F76BED4ABAF49583FDFE928B5DA3109897355C04018E981`;
  zero converged diagnostics.
- AUX destinations are distinct: `proposition.1.9.2` and
  `proposition.1.9.2.second`; both visible headings remain I.9.2.
- Render: 16 PNG / 6,346,588 bytes; ordered digest
  `0DC7C1D8473EAF69860CF6C12F173CBE11D44078DE1C05B154A300A18339BB3B`.
  Pages 3--15 are 13/13 byte-identical to frozen I.9.1 r2; changed pages 1,
  2, and 16 pass visual inspection.
- Metadata is populated; the PDF is unencrypted and has no forms, JavaScript,
  suspects, or embedded files; 30/30 fonts are embedded, subsetted, and
  Unicode-mapped.

r1 and r2 remain rejected build-isolation/copy evidence. r3 remains rejected
despite clean visible pixels because its pass-two/pass-three logs retain the
duplicate destination `proposition.1.9.2`. r4 is the clean successor.

## Machine evidence

- CSV: 19 files / 405 rows / 166,655 bytes; ordered digest
  `EEEA21E91612B57E4A2DA38DA13BD80C37BEFAFDC653C88E9383EDA0BE42A65F`.
- JSONL: 8 files / 192 unique records / 303,279 bytes; ordered digest
  `21B675E58C35F0C4A0CD70A99402C59E65E4B157450B011EDF944B880F19180D`.
- I.9.2 graph: 4 records / 6,385 bytes; SHA-256
  `5D84945ECCFAC387F94D2F7715B37F9057D9A465A842BD4AB9DBBF078AE69F20`.
- Difficulty ledger: 116 records / 212,104 bytes; SHA-256
  `1C5EC1DB330358958F0104E3B64F3BF44062A00756E22D9D4B25F0FC9BCCB57C`.
- Result: zero CSV rectangularity/ID/formula-safety failures and zero JSONL
  parse/schema/hash/reference/parent-child/supersession/closure failures.

All four I.9.2 graph records are `closed_corrected`. Six bounded difficulty
records are reciprocally closed by `SGA1-I92-VERIFY-0001`; r1/r2/r3 remain
rejected and unclosed. The workpass-root PDF is intentionally the prior public
I.9.1-r2 locator; local I.9.2 closure uses the isolated r4 reader.

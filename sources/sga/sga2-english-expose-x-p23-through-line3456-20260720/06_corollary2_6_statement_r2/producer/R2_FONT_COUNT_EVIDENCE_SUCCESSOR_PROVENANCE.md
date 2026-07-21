# SGA2 Exposé X Corollary 2.6 statement — R2 evidence successor

## Disposition

This is a no-overwrite append-only producer successor. It corrects one
evidence-only inconsistency and remains pending fresh independent review.
It is not sealed, publication-ready, or an archive handoff.

The predecessor producer and its independent fail review remain in the
sibling `unit_X_corollary2_6_statement` tree. The independent review passed
the source, translation, formulas, target, build, render, extracted text, and
actual fonts, but failed closed because two producer claims said 12 font rows
while the actual font table and producer validation said 11.

## Exact correction

- Predecessor audit SHA-256:
  `CAACB9F310F341AB009B85696C5ACD4B5617468F61AF02054D9A29E1CC8F1899`.
- Predecessor JSONL SHA-256:
  `E5CF11A0BA63E3658D3CD88107DC820899500A928E747AA5B1B13EFCAD663F39`.
- Independent fail audit SHA-256:
  `B1EEBE40CDEA502BA019B627CA1D2DDE744B80C08B7D32288646524C0D286BB8`.
- Independent validation SHA-256:
  `B9B0FBCAD774AA9F6E63F7A6CC12AA35A721F1068BF97DC35E5C6481E14B15E6`.
- Actual `PDFFONTS.txt`: 1,235 bytes, SHA-256
  `FDBA2D33215659347C6F00F1F00A6C9C849B96281E50C660FD969287373EF37E`,
  exactly 11 data rows, all embedded, subsetted, and Unicode-mapped.
- Active R2 audit SHA-256:
  `5F47FB8F3648DB43186F43DF35344425DFFA5879C35CEE6AC2039337EB7B135B`;
  it says 11 font rows.
- Active R2 JSONL record `SGA2-X-C26-RENDER@2` says 11 font rows and
  reciprocally supersedes `SGA2-X-C26-RENDER@1`, whose historical 12-row
  claim remains visible.
- Review-defect revision `SGA2-X-C26-STATEMENT-IR-FONTCOUNT@2`
  reciprocally supersedes `SGA2-X-C26-STATEMENT-IR-FONTCOUNT@1` and records
  that the target bytes did not change.

## Unchanged authority and target

- French authority SHA-256:
  `C2F899E92A904E312B550C6452A117FF23D30AF984B2254A0961D2DF0DACD042`.
- French lines 3446–3453 slice SHA-256:
  `61B57A0A871EAC4F2D19BFF482133A0F47ECB3DE80CBD877BD05878E9AD38B0E`.
- Target TeX SHA-256:
  `C9A674ED0B8D5E7237552AA471DC83E5FF51420389BCD507A580848648DAB927`.
- Target PDF SHA-256:
  `266BD66E2A8464B7E31C533A81887C445950EC831AE09BE6BB991FF8409BA0A1`.
- The 13-row unchanged-artifact ledger is SHA-256
  `BB2A4E50F5F195759428472CEC91F02DE54354821C2286AFAD441080FD446B19`
  and validates byte identity for the source, target, build, font, text, and
  render artifacts.
- The 73-row predecessor producer/review identity manifest is SHA-256
  `21015C8864D04AACECC57AFCCD76A3735B2E58292665FF5CF8165D890C651EF6`.

Coordinates remain printed page 117, source-PDF physical page 101, and
recomposed running page 93. Continue at raw cursor 3454 and substantive
cursor 3455.

## Release and review gate

The two copied build logs and final TeX engine log contain private local
paths. They must be sanitized or excluded before public use. This R2 package
requires a fresh independent PASS before any seal or archive handoff.

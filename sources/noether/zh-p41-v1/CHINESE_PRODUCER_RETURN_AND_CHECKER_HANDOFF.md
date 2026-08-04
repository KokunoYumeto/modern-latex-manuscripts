# Noether Paper 41 — Chinese producer return and independent-checker handoff

Producer state: **complete Chinese translation and mechanical builds; independent check pending**.

This lane translated the supplied current German Paper 41 interval. It did not collate scans, check the German source, check the translation or formulas, inspect rendered pages, localize regional Hant prose, approve, or certify the work.

## Authority and cursor

- Current German whole TeX SHA-256: `443EF950D7D45DC6D9E44A9B87501620C10DA873E50E5F2B253ECCAE6A946D27`.
- Exact local Paper 41 interval: `source/Noether_Paper41_CurrentGermanAuthority_interval.tex`.
- Interval SHA-256: `C265058425E5E2D1A2289CC03A9DDEDDDF4803A3215DC3F173B93E7AB69D60ED`.
- Inherited Simplified-Chinese drafting-witness interval SHA-256: `C6A2B4E40700A7E1A32AAEB76227DCD4335777616A595AAB6A4909BAB83554DB`.
- Source-custody record SHA-256: `BB9DEB51AFF725E26DBB5A07B157C09BD1AC02E98A43A58FD1D42ABB872FD668`.
- The stale shared R821 pointer was not used.

## Translation deliverables

- `zh-Hans-CN/Noether_Paper41_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex`
  - SHA-256: `97142978B30DC21C27D6C30A9CF18C0408F514C08D7A2CEF5649299D3B91E9F0`
- `zh-Hans-CN/Noether_Paper41_Chinese_CurrentAuthority_zh-Hans-CN_v001.pdf`
  - SHA-256: `F7F6A8F50C781A73131E45B09D40EA89E84BAEE179FAE2E9A9BA1DAA9E5426A3`
- `zh-Hant-controlled/Noether_Paper41_Chinese_CurrentAuthority_zh-Hant-controlled_v001.tex`
  - SHA-256: `C5EB70BF90AA824D9B8281BB68780B0BA7269D3A8BCD3CD30A3F1BBEB2AE5F23`
- `zh-Hant-controlled/Noether_Paper41_Chinese_CurrentAuthority_zh-Hant-controlled_v001.pdf`
  - SHA-256: `209489E484DE479A1646530226AF7DB92A26F0B1D9A575EE928FCE5A39BD4C33`

The Hant deliverable is a controlled-generic script derivative, not `zh-Hant-TW`, `zh-Hant-HK`, or `zh-Hant-MO` localization.

## Mechanical build and adverse production history

- `BUILD_REPORT.md` — SHA-256 `3BDC5149C1965C8D791380924FE93745DD8C9533EFC16771A84FC85E393517C8`.
- Both targets completed two successful XeLaTeX passes and produced five-page PDFs. Each final log has one unavailable italic-shape warning plus the summary substitution warning.
- The initial producer TeX contained mathematical notation in plain parentheses and failed compilation. Compiler-driven production converted 329 math spans to TeX inline math and flattened 38 nested delimiters. The exact transformation records are in `qa/INLINE_MATH_MARKUP_RECORD.json` and `qa/INLINE_MATH_NESTING_RECORD.json`.
- The line containing theorem 90 received a direct producer markup/prose repair to `$N(a)=1$` and `$a=b^{1-S}$`; the checker should review this locus explicitly.
- No PDF was rendered or viewed by this lane.

## Producer evidence for the checker

- `TRANSLATION_NOTES.md` — SHA-256 `1287AF6699B89BD2EAF8AB79F9CCFD2E593DBDDDBDE2665270A9A8DE4DB7E945`.
- `STATUS.md` — SHA-256 `8A35BA4F0C2B37389D3E698A675F0CD3F050ADC87026BAA8EB027748C86AD4B7`.
- `PRODUCER_STRUCTURAL_INDEX.json` — SHA-256 `58B2A5A0366585BBDDA8EE81DA011F2264097E8D57CD48D0F4C6F9A4E41B6783`.
- `evidence/PRODUCER_TERMINOLOGY_LEDGER.csv` — SHA-256 `05C4A761720E8EA907986558C7629F455F5BAD0A8F2F30BED113D7E6A17423E5`.
- `evidence/ADVERSE_SENSE_LEDGER.csv` — SHA-256 `360CAE054B98D7290812C8749C1BDC24362181F73B3D3BAE1331DE5150CDE24C`.
- `evidence/CJKV_CROSSWALK_P41_ZH.csv` — SHA-256 `42B122392C3B4AD46C2C0D395CF64A7AA88C1945AB4219A776077963EA55DE8C`.
- `evidence/PRODUCER_CONCEPT_GRAPH.json` — SHA-256 `1697C916F6369B8D11097CDCAFABE5B7A33D951010CD0CBE8B52596DF32D9491`.

The three CSVs each contain 20 mechanically parseable producer rows; the graph contains 100 typed nodes and 100 edges and records `independent_check: absent`. These artifacts document editorial choices, sense windows, adverse attractors, provisional lexical basins, and qualitative Mandarin-Simplified dominance debt; they do not validate any choice. Japanese and Korean were not used as Chinese authority.

## Independent checker requested

Please check Hans against the exact German interval; verify formula and note fidelity; review all compiler-normalized parenthesized math, especially the theorem-90 locus; evaluate terminology and adverse-sense choices; render and visually inspect both PDFs; and assess the controlled-Hant derivative and its nonregional limits. Return corrections separately and preserve append-only producer history.

No new source-defect claim was made by this translator. If checking discovers one, the checking/source-owner workflow should deduplicate and route it; this lane does not adjudicate it.

Lane log: `C:/Users/Floris/Documents/interlanguage/03_projects/language_management/cjk/00_lane_control/CHINESE_DECISION_LOGBOOK_20260718.md`, latest production decision `ZH-D068`.

Scope remains Noether only. SGA is held until Floris explicitly confirms it.

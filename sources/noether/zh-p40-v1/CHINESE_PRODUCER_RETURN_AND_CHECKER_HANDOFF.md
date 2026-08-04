# Noether Paper 40 — Chinese producer return and independent-checker handoff

Producer state: **complete Chinese translation and mechanical builds; independent check pending**.

Floris's controlling instruction is: `you do not check - you translate - other sessions CHEWCK`. This lane translated the supplied current German Paper 40 interval. It did not collate scans, source-check or adjudicate the German, validate translation/formulas/terminology, inspect rendered pages, localize regional Hant prose, approve, archive, publish, or certify the work.

## Authority and cursor

- Current German whole TeX SHA-256: `443EF950D7D45DC6D9E44A9B87501620C10DA873E50E5F2B253ECCAE6A946D27`.
- Exact Paper 40 interval: lines 19061–19708, UTF-8 bytes `[1704074,1787529)`, 83,455 bytes.
- Exact local source: `source/Noether_Paper40_CurrentGermanAuthority_interval.tex`.
- Exact German interval SHA-256: `7965805D3A75C3354C85BC7A3E4725F07BF869A8833FC19D74E32BE369427937`.
- Inherited Simplified-Chinese drafting-witness interval SHA-256: `3DAD18CAB878BDFA62ED4FCC634E21AF92AF22BC8E11DF8A36888088D0A608AB`.
- `SOURCE_CUSTODY.md` SHA-256: `B7A32493D458FEC32A7ADBB1B2FC4D34887C6CDBD9C7353DF8E00C0E5A4933E2`.
- The stale shared R821 pointer was not used.

## Translation deliverables

- `zh-Hans-CN/Noether_Paper40_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex`
  - SHA-256: `73E05D631EBA59BDCD69770275586833FA0546D8D7E4A262F9048D10D5B44147`.
- `zh-Hans-CN/Noether_Paper40_Chinese_CurrentAuthority_zh-Hans-CN_v001.pdf`
  - SHA-256: `632F52F7C19AC731E359AF73AF6BA00171E0C65142454EB878A398EF72A6515B`.
- `zh-Hant-controlled/Noether_Paper40_Chinese_CurrentAuthority_zh-Hant-controlled_v001.tex`
  - SHA-256: `B2C71E1CFC48D232D45FF164FD60008837DDDFD3D9279E5CA3A168B221EAB8C6`.
- `zh-Hant-controlled/Noether_Paper40_Chinese_CurrentAuthority_zh-Hant-controlled_v001.pdf`
  - SHA-256: `DD5FC4BCDA5426949647A94F14935FD32A4EFF11AB9EC2EB21C043B3BD6B81C4`.

The Hant deliverable is controlled generic only, not `zh-Hant-TW`, `zh-Hant-HK`, or `zh-Hant-MO` localization.

## Mechanical production

- `BUILD_REPORT.md` SHA-256: `E846BAB9E5B0DA152D3AEC97ACE361319F91A2F091BF6BF9C4065674368ADA8F`.
- Both final targets completed two successful XeLaTeX passes and produced 15-page PDFs.
- Hans final log SHA-256: `9AA906CF10E4903F2EA3B8A9EB12C49B2352855C2E164B1589935931E0EC3E74`.
- Hant final log SHA-256: `2C7C6088F16DE5E68EFB68138A99A941792798E3262CF5E2F6EA5FEFAB8F7A94`.
- Each final log records an unavailable italic CJK font shape, the summary substitution warning, and one 7.08952pt overfull box; no fatal, undefined-control, or missing-character diagnostic was found in the compiler transcripts.
- Hans assembly record SHA-256: `838AB87AA92EB7612D425FFD2D59FFDDCB32C9484247DE1B4F4DFEDDE113DEA5`.
- Cross-segment terminology-normalization record SHA-256: `CC1D6320628159A007A7D7B880133539F1A5240D647975AB0B2970267084EB87`.
- Controlled-Hant OpenCC producer record SHA-256: `0362A5BB8C51A0CAAD95355CB0EDAE48DB9EE82CAB50DD042469671DC3717756`.
- No PDF page was rendered to an image or viewed by this lane.

## Producer evidence for the checker

- `TRANSLATION_NOTES.md` — SHA-256 `B6D49E7EE1E1A3ACCFC69610C2E7A938BD3CF23EB7A86FDF17BD0334E2556474`.
- `STATUS.md` — SHA-256 `FDFA68870087A80F42BED8D6FD39FDD2BCD66E86186EE4EAA197EC91F7EDDEFA`.
- `evidence/PRODUCER_TERMINOLOGY_LEDGER.csv` — SHA-256 `9323C26F140FE4E257CF39369DAFED505389EB2BBDD7EC2E2D08BA33B38CF22D`.
- `evidence/ADVERSE_SENSE_LEDGER.csv` — SHA-256 `7F0B61646E3482B00FBC1D4A05A2C695389DA9B715148DB07ADA377B91372B07`.
- `evidence/CJKV_CROSSWALK_P40_ZH.csv` — SHA-256 `49AFACA6EB96D926BB191E0BF99ABA4CADFFAF68F19EDF17857B4CBDDD382EDF`.
- `evidence/PRODUCER_CONCEPT_GRAPH.json` — SHA-256 `7BF69FDB0144D74A48D9015E246EB3E9E3E766AD16BA27350C871E17E233D621`.

The three CSVs each contain 20 producer rows. The local graph parses as 20 nodes and 10 edges. Every entry is explicitly a producer proposal with `independent_check=absent`; trap-prone entries have a sense window, alternatives, qualitative Mandarin-Simplified dominance debt, and provisional lexical-attractor basin. Japanese and Korean were not consulted and are not Chinese authority.

## Independent checker requested

Please check Hans against the exact German interval; verify every formula, footnote, title, theorem statement, segment boundary, and terminology choice; render and visually inspect both PDFs; and separately assess the controlled-generic Hant derivative. Mandatory terminology attention includes:

- historical noncommutative `Körper` → `除环` versus ordinary commutative `域`;
- `reziprok` → `反向` versus inherited `互反`;
- source `Automorphism` in passages that include noninvertible self-maps → `自同态`;
- `Zerfällungskörper` / `Abspaltungskörper` → `分裂域` / `析出域`;
- `Normalbasis`, `Verengungsmodul`, `Erweiterungsmodul`, `Darstellungsmodul`;
- `ähnliche Algebren`, `Algebrenklasse`, `komplementäre Basis`, `operatorisomorph`;
- technical `Differente`, which must not be interpreted as everyday “different”;
- the authority's reuse of (Z) for isomorphic copies, which can make Chinese sentences look reflexive.

Please return corrections in a checker-owned append rather than silently rewriting producer history. The 7.08952pt overfull-box loci and italic-shape substitutions also require checker-owned visual handling.

No source defect was adjudicated or asserted by this lane. If a checking session identifies a precise possible Noether source defect, it must first deduplicate it and then ensure that `4 -nterslav` receives it under Floris's instruction; this producer lane must not self-adjudicate or duplicate-route it.

Lane log: `C:/Users/Floris/Documents/interlanguage/03_projects/language_management/cjk/00_lane_control/CHINESE_DECISION_LOGBOOK_20260718.md`, production-freeze decision `ZH-D074`.

Scope remains Noether only. SGA is held until Floris explicitly confirms it.

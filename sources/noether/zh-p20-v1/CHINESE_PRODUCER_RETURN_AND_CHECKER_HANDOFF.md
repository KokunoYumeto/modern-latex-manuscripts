# Noether Paper 20 — Chinese producer return and independent-checker handoff

Producer state: **complete Chinese translation and mechanical builds; independent checking pending**.

Floris's controlling instruction is exact:

> you do not check - you translate - other sessions CHEWCK

This lane produced the Chinese translation and mechanical build artifacts only. It did not collate scans, source-check or adjudicate the German, compare or audit the inherited witness, validate translation, formulas, terminology, citations, or historical notation, open or render a PDF, perform visual QA, regionalize Traditional-Chinese prose, approve, archive, publish, or certify this work.

## Authority and exact source custody

- Current authority pointer: C:/Users/Floris/Documents/Codex/2026-06-01/we-are-currently-doing-a-massive/Noether_P07_CurrentHead_SourceAdjudication_20260722/1/03_audit/NOETHER_CURRENT_AUTHORITY_POINTER_20260722.md
  - SHA-256: FAC89D076DCE1C24B534595595B75BA1C88A8956E370EF848B307E731633EED1
- Current German whole TeX: C:/Users/Floris/Documents/Codex/2026-06-01/we-are-currently-doing-a-massive/Noether_P07_CurrentHead_SourceAdjudication_20260722/1/01_current/Noether_P16_IndependentSecondPass_20260722_cum_de.tex
  - Bytes: 2,132,486
  - SHA-256: 443EF950D7D45DC6D9E44A9B87501620C10DA873E50E5F2B253ECCAE6A946D27
- Exact Paper 20 German interval: current-authority lines 12377–12588, UTF-8 bytes [980360,1001524), 21,164 bytes.
  - Local slice: source/P20_CurrentGerman_lines12377_12588.tex
  - SHA-256: CBC9E9CF34E6475F4256C935A58378FCDBF85A09ACC0E592FC64F3FCFDF8744D
- Exact inherited Simplified-Chinese drafting-witness interval: witness lines 13142–13378, UTF-8 bytes [896162,914175), 18,013 bytes.
  - Local slice: witness/P20_InheritedHans_content_lines13142_13378.tex
  - SHA-256: B7DA9DBB83BC2B9793263987F14D7E67C91324EE83FEA26FBCDC82979FE5F97C
- The inherited Chinese interval was a drafting witness only. No comparison or audit is claimed.
- The stale shared R821 pointer was not used.

### Source and witness slices supplied to translators

| Segment | Current German source slice | SHA-256 | Drafting-witness slice | SHA-256 |
|---|---|---|---|---|
| A | segments/source/P20_A_lines12377_12437.tex | DFD92DE298F422E2D993CC3162E3B031D41E4ECB67E32CB967FE0A1FD6CF237E | segments/witness/P20_A_witness_lines13142_13213.tex | F70FEE111C012F8150A4857003B147F9F1DB775F6ECACAFC7EBED4BF2D6E435D |
| B | segments/source/P20_B_lines12438_12519.tex | 25D5BCDA8B4A35D789A8A33D256BC08FB779E057567A1673761FD7D7F97AD81E | segments/witness/P20_B_witness_lines13214_13306.tex | 2C16DF8FF56AB931AEF611B2A3AF2D758CACDC8EAB9A4EDA167CF83079235714 |
| C | segments/source/P20_C_lines12520_12588.tex | D7B2FC4C6FB95125109A83F5F856F27B319FE25F4ABF13B3AAE6D33A99D5C2C1 | segments/witness/P20_C_witness_lines13307_13378.tex | 918DD045B8E3752E285EF7182A08EED54D83AA943DF09C1347AA03BE14029BCF |

## Final translation deliverables

The Simplified-Chinese target is PRC-oriented zh-Hans-CN producer prose. The Traditional-script target is a mechanically transported, controlled-generic, nonregional zh-Hant derivative. It is not Taiwan-, Hong Kong-, or Macao-localized prose.

| Artifact | Bytes | SHA-256 | Mechanical state |
|---|---:|---|---|
| zh-Hans-CN/Noether_Paper20_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex | 20,245 | 262430D0A092818F859516F3FD5DE612D897D0BD8AAC49605BE047E389963065 | editable assembled TeX |
| zh-Hans-CN/Noether_Paper20_Chinese_CurrentAuthority_zh-Hans-CN_v001.pdf | 235,218 | DF04B292EB1DDC80B8B1637406B7416EBF4CA947E06018D865F98424B72EA54D | two successful XeLaTeX passes; compiler reports 5 pages |
| zh-Hans-CN/Noether_Paper20_Chinese_CurrentAuthority_zh-Hans-CN_v001.log | 21,148 | D4599B1218F1BC885E6F7CA3322BE71B5F9CAAA94D97E6C8B311917BFE884D13 | final engine log |
| zh-Hant-controlled/Noether_Paper20_Chinese_CurrentAuthority_zh-Hant-controlled_v001.tex | 20,587 | 17EE7ECD25A298D8818144CE41273A31DEB85F3E49A02F08D5335B6815FF20C0 | editable controlled-generic TeX |
| zh-Hant-controlled/Noether_Paper20_Chinese_CurrentAuthority_zh-Hant-controlled_v001.pdf | 257,407 | 286400FD8AECE3D86AABC06855B53E9817A2C58AC1ED5952DF14086FAB7488EA | two successful XeLaTeX passes; compiler reports 5 pages |
| zh-Hant-controlled/Noether_Paper20_Chinese_CurrentAuthority_zh-Hant-controlled_v001.log | 21,222 | 12A88EA8BCD7FA0BB52AF870CF82DE475B1D65D5C054714203DEF0A8B6931999 | final engine log |

Successful compilation is mechanical production evidence only. This producer did not open, render, or visually inspect either PDF.

## Complete four-failure delimiter-repair history

This is append-only compile-driven mechanical history, not formula-content or translation checking.

| Order | Failed pass-1 event | Segment-A state before event | Exact mechanical consequence |
|---:|---|---|---|
| 1 | XeLaTeX stopped at the first literal (n\ge2) outside inline math; no pages were produced. | B637B38DBD55BCF8BA6862F000B48D9108FC77F8D42D083762A5AE97081559FC | Only its inline-math delimiters were restored; intermediate SHA-256 51BDBA85125DC72494746B49540FD6EF5DE21D7DD2854F86558B726E06586B3F. |
| 2 | XeLaTeX stopped at the second literal (n\ge2) outside inline math; no pages were produced. | 51BDBA85125DC72494746B49540FD6EF5DE21D7DD2854F86558B726E06586B3F | Only its inline-math delimiters were restored; intermediate SHA-256 F4317188496FE61F220343C1C941E7D6F7EF02707F463D3FA208203963BD1AC6. |
| 3 | XeLaTeX stopped at the third literal (n\ge2) outside inline math; no pages were produced. | F4317188496FE61F220343C1C941E7D6F7EF02707F463D3FA208203963BD1AC6 | Only its inline-math delimiters were restored; intermediate SHA-256 80AA4F63166554C74EB29806CF1DCE77A6C98F1DB31EC181FD1BF9A372CCC4DC. |
| 4 | XeLaTeX produced one page and then stopped at malformed inline token (F(x,y)\). The incomplete PDF was not opened or rendered. | 80AA4F63166554C74EB29806CF1DCE77A6C98F1DB31EC181FD1BF9A372CCC4DC | Only the malformed token's opening delimiter was restored; current segment-A SHA-256 DC694B77A78B1D12E12BC5A3DA315147538847F23F0E46772D85A7BAE9181834. |

No prose choice changed in these four repairs. The current A/B/C segments were then assembled into final Hans TeX SHA-256 262430D0A092818F859516F3FD5DE612D897D0BD8AAC49605BE047E389963065, after which both final XeLaTeX passes exited successfully.

## Worker returns

| Return | SHA-256 | Current translated segment SHA-256 |
|---|---|---|
| worker_returns/P20_A_TRANSLATOR_RETURN.md | 94E5A487D08A67BD692D4BC283F1C8770231D5A96F6553B8FEECD43658AD0662 | DC694B77A78B1D12E12BC5A3DA315147538847F23F0E46772D85A7BAE9181834 |
| worker_returns/P20_B_TRANSLATOR_RETURN.md | 4E924E588A08B14806DC5D3812D852DEAA67F23F2E8A516A1FFB7D30C9FB1816 | 143C7386FCB9DDA7159C2F7D9A2C9547530D9AED786648A85ACD488D14A8A491 |
| worker_returns/P20_C_TRANSLATOR_RETURN.md | E0C5631F520867B2BB37E78E8593453091447573AC5ECECE96A60EAE615D8520 | 8972FC4AA515FF93047D0F686DFD9CCB4003287E2F815313F02BAC079ED9D734 |
| qa/WORKER_RETURNS.md | D10D17EF498A0B0C72D46B304B3E803C6CC9059EEF4389585E185B69FA3C6EF4 | A/B/C manifest |

The worker returns retain producer lexical choices, alternatives, and uncertainty for checker-owned adjudication.

## Mechanical build and documentation custody

| Artifact | SHA-256 |
|---|---|
| BUILD_REPORT.md | 1B8C767015EE557CC7C18CE6234ADB45161B65D63A8A134777B20CB1030596AE |
| qa/HANS_ASSEMBLY_RECORD.json | 39A4D15DEBEC4E45D3032B9554A6D83B552957031074264ECC5D3DB66A673B2D |
| qa/HANS_MECHANICAL_BUILD_RECORD.json | 78CE6579A83531D42FBD3007042AA69BF742DCEF35D68F558234DF91F685B779 |
| qa/HANS_COMPILE_SYNTAX_REPAIR_RECORD.md | B2D4F1CA51ADE150BAA7AB895CB821458B2E40C2F180CE2DD2F50D288CD95652 |
| qa/OPENCC_PRODUCER_RECORD.json | 80A7FC6B1D859A63CC4BC602CC289860098EA317BE158D32D3BEE048CD541B76 |
| qa/HANT_BUILD_RECORD.json | D71DB684736DCE854A98C1FBF5548A8CC00D173F244F95D8C9CEB8F31BEB2FF9 |
| qa/SOURCE_CUSTODY_RECORD.json | 5160E31529C3502D33406EFE9968EC8ABAE18175A907F37F3C8B80B3A721B79A |
| qa/SOURCE_SEGMENTATION_RECORD.json | 5A786961ED8F08C90552FB8D6842509F16BB59375CECCEEB2185282328E459EF |
| SOURCE_CUSTODY.md | BDB538768F7A5D5756CDF707632AA91517A834A0E7EBC27C195F967D7500F2AD |
| TRANSLATION_NOTES.md | 1A9C1FBF46788316E889035A191FDA7207B41123B0DC818BC0E45ACFB6E2C155 |
| STATUS.md | 83661794E4413D5C176755D839010070E54B1807AB02C60EEB4E2448DBD9904D |

Producer script hashes are retained in BUILD_REPORT.md: extract_exact_slices.ps1 F0565D771C40D252B90FFB2E99A0B2B33ACB540A347F704BC08FFB8CFC1C1489; assemble_hans_producer.ps1 DB928612D71EED2589EFDE9DE115BDCFD8BB010DE220D1469F7BA1A3416BD102; compile_hans_producer.ps1 DF784B173F6D5D2B8CAC6918B49A0941476CBD11D8E4EF5BD1A6B67FEBA2B3A4; build_hant_producer.py 11E74A3830A8EB0A181328C94A2FCC1E97F7C38563C9D4A4AD29FC875E7031C2; compile_hant_producer.py 2FDD1925C403563AEB93C3F4B1EE8DE1031D2A9F05E85F95104BFD74967C9626.

## Producer evidence for the checker

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| evidence/TERMINOLOGY_LEDGER.csv | 30,165 | 151D75CCD62040506D559B89B303CBF2D59C8C06F92268824CFE06A731DFF84D |
| evidence/ADVERSE_EVIDENCE_LEDGER.csv | 25,382 | 6A7A6C09851ECF20059FC61E8C34C681B9A091C180BFFE1009002E42DCE43E85 |
| evidence/CJKV_CROSSWALK.csv | 26,058 | 22118C8DF787D5FA0998693D57E66FBB2968CA41E97E9F1271EC6AABEE11DB64 |
| evidence/CONCEPT_EVIDENCE_GRAPH.json | 63,588 | C612D1BA648E6FD241E05CA1F2568FE2C259916E9FA5A3849ECCDDB9F41DD4A5 |
| qa/build_p20_evidence_pack.py | 40,772 | FE3BBFC38B9383629FC9B8FD717D1C9CCFCE55D681F2727AFA2684C5B7105544 |

The three CSVs contain 23 producer rows each. The graph contains 115 nodes and 115 edges. These counts and hashes are producer-custody facts only; this handoff does not evaluate the entries or claim independent checking. The files retain producer terminology proposals, adverse-evidence fields, sense windows, alternatives, qualitative Mandarin-Simplified dominance debt, and provisional lexical-attractor basins. Japanese and Korean are not Chinese authority.

## Independent checker requested

The independent checker, not this producer lane, should compare Hans against the exact current German interval; verify every formula, footnote, citation, title, historical notation, and terminology choice; render and visually inspect both PDFs; and separately assess the controlled-generic Hant derivative. Corrections should be returned in a checker-owned append rather than silently rewriting producer history.

No source defect was adjudicated or asserted by this producer lane. If a checking session identifies a precise possible Noether source defect, apply Floris's route exactly: **deduplicate; ensure 4 -nterslav sees it**. This producer lane must not self-check, self-adjudicate, or duplicate-route it.

Lane decision reference: ZH-D104 in C:/Users/Floris/Documents/interlanguage/03_projects/language_management/cjk/00_lane_control/CHINESE_DECISION_LOGBOOK_20260718.md.

Scope remains Noether only. SGA is held until Floris explicitly confirms it.

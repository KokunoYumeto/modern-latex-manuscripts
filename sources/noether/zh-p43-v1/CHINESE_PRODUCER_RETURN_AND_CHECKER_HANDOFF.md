# Noether Paper 43 — Chinese producer return and independent-checker handoff

Producer state: **complete Chinese translation and mechanical builds; independent check pending**.

Floris's controlling instruction is: `you do not check - you translate - other sessions CHEWCK`. This lane translated the supplied current German Paper 43 interval. It did not collate scans, source-check or adjudicate the German, validate translation/formulas/terminology, inspect rendered pages, localize regional Hant prose, approve, archive, publish, or certify the work.

## Authority and cursor

- Current German authority pointer SHA-256: `FAC89D076DCE1C24B534595595B75BA1C88A8956E370EF848B307E731633EED1`.
- Current German whole TeX SHA-256: `443EF950D7D45DC6D9E44A9B87501620C10DA873E50E5F2B253ECCAE6A946D27`.
- Exact Paper 43 interval: lines 20096–20906, UTF-8 bytes `[1838551,1927253)`, 88,702 bytes.
- Exact local source: `source/Noether_Paper43_CurrentGermanAuthority_interval.tex`.
- Exact German interval SHA-256: `657799FA62D58538E6AFC810221DE2C9E1F7DC481E7DDEF2CAD76506DDEB8176`.
- Inherited Simplified-Chinese drafting-witness interval SHA-256: `130646F67B105205CD783EDA2928A7FC45B14840D84D93DDC1AF9E1D725005CB`.
- `SOURCE_CUSTODY.md` SHA-256: `B4E6146CDF7AF0E2523F90E612FC11F05ACD0B96E1F7C7BFB7F7AD612ADBCE4E`.
- Post44, Post45, bibliography, and later endmatter are excluded. The stale shared R821 pointer was not used.

## Translation deliverables

- `zh-Hans-CN/Noether_Paper43_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex`
  - SHA-256: `FDAF1A0B9F55DD5A972396E41A03F69DD966CC9BEDA8D82365B7010EBC3501D7`.
- `zh-Hans-CN/Noether_Paper43_Chinese_CurrentAuthority_zh-Hans-CN_v001.pdf`
  - SHA-256: `673088FCDC3AFB5620279ABA2667305AF95B18CB141F1608058A9E7F0DE72EE9`.
- `zh-Hant-controlled/Noether_Paper43_Chinese_CurrentAuthority_zh-Hant-controlled_v001.tex`
  - SHA-256: `4896BE04492C3BB5EBE2AAA7668F70E45D50A6224721EF4B873B6BB21F93156E`.
- `zh-Hant-controlled/Noether_Paper43_Chinese_CurrentAuthority_zh-Hant-controlled_v001.pdf`
  - SHA-256: `E75110A64B5A8532347FDF92C42BEDAC4D762CAD2973ECA3773C01B4204B5B21`.

The Hant deliverable is controlled generic only, not `zh-Hant-TW`, `zh-Hant-HK`, or `zh-Hant-MO` localization.

## Mechanical production

- `BUILD_REPORT.md` SHA-256: `0ED5075598C1D8BE352C13E2ED1BBF247B83C964BED4CF9A5479F1EBD6B0A528`.
- Both final targets completed two successful XeLaTeX passes and produced compiler-reported 17-page PDFs.
- Hans final log SHA-256: `D58CA102FE30A81D987DCF21F7DC916CBCCFA4707F03306CE3C782F76FF869AE`.
- Hant final log SHA-256: `9BB0272A00377BC2369EFFB890B917D7C6C2627983E1E234EB3CA3AB886A63BC`.
- Each final log has zero error/fatal/missing-dollar, package-warning, ordinary LaTeX-warning, overfull, underfull, and missing-character matches. Each records the unavailable italic CJK font shape and the corresponding summary warning.
- Hans assembly record SHA-256: `EBD8BFEDD4646FDC514517EC55698540A97EE5A95FE1FAD3B6270C57BBA2BEBB`.
- Controlled-Hant OpenCC producer record SHA-256: `C4A9D30486624794AFDC1D13412A4B2B3781B9564D1FB1C43FD2ABBE18D3C3DB`.
- Producer TeX syntax-repair record SHA-256: `AFD3DC6F025072A04D7954E5EAF8D3AD55C03DB04418A4B2FB5438B8762383A4`.
- No PDF page was rendered to an image or viewed by this lane.

## Producer evidence for the checker

- `TRANSLATION_NOTES.md` — SHA-256 `0B8884A808D3917252A0A7ADD55955DE10E688C323701C603A1326247D5B14E1`.
- `STATUS.md` — SHA-256 `DA1C6108E378E8C75687BBA592BB8E098552220451672317B86810788C145588`.
- `evidence/TERMINOLOGY_LEDGER.csv` — SHA-256 `ABE6DEE3E67637CF284366DDB8441B90456A83403DF91F8F06ABD4A280316B21`.
- `evidence/ADVERSE_EVIDENCE_LEDGER.csv` — SHA-256 `D046125A86AA1D3563E01453F5075237CC11FEDDF3EE6704D7779F2D59D4C49B`.
- `evidence/CJKV_CROSSWALK.csv` — SHA-256 `00C07997ED183981D88ED21D6D52A0A4D53C0B0E59F52250B8AE00BDE869FD8D`.
- `evidence/CONCEPT_EVIDENCE_GRAPH.json` — SHA-256 `957A188D2D57D258637561240029C75EA1445851E6A77C4251A678006A6A9B23`.

The three CSVs each contain 20 producer rows. The graph mechanically parses as 100 nodes and 100 edges. Entries are producer proposals with independent checking absent; trap-prone entries include a sense window, alternatives, qualitative Mandarin-Simplified dominance debt, and provisional lexical-attractor basin. Japanese and Korean were not consulted and are not Chinese authority.

## Independent checker requested

Please check Hans against the exact German interval; verify every formula, footnote, title, section, theorem/proposition statement, historical parenthetical notation, and terminology choice; render and visually inspect both PDFs; and separately assess the controlled-generic Hant derivative. Mandatory terminology attention includes:

- technical `Differente` → `不同`, whose ordinary-language collision is the highest-priority sense trap;
- `Idealdifferentiation`, `Differenzenideal`, `Differenzenquotient`, and `Differentialquotient` → `理想微分`, `差分理想`, `差分商`, and `微分商`;
- `Verengungsmodul` → `收缩模` and `Umfassungskörper` → provisional `包络域`;
- `Vertauschungen` → `置换`, `absoluter Modul` → provisional `绝对模`, and `abhängige Modulbasis` → `非独立模基`;
- `Ordnung`, `Hauptordnung`, `Komplementärmodul`, `Komplementärbasis`, `direktes Produkt`, and `direkte Summenzerlegung`;
- distinctions among plain historical parentheses and actual TeX math delimiters in segment D.

Please return corrections in a checker-owned append rather than silently rewriting producer history. The italic-shape substitutions require checker-owned visual handling.

No source defect was adjudicated or asserted by this lane. If a checking session identifies a precise possible Noether source defect, it must first deduplicate it and then ensure that `4 -nterslav` receives it under Floris's instruction; this producer lane must not self-adjudicate or duplicate-route it.

Lane log: `C:/Users/Floris/Documents/interlanguage/03_projects/language_management/cjk/00_lane_control/CHINESE_DECISION_LOGBOOK_20260718.md`, producer-freeze decision `ZH-D077`.

Scope remains Noether only. SGA is held until Floris explicitly confirms it.

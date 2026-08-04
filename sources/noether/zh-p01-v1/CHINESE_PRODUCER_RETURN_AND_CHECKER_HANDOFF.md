# Noether Paper 1 — Chinese producer return and independent-checker handoff

Producer state: **complete Chinese translation and mechanical builds; independent check pending**.

Floris's controlling instruction is: `you do not check - you translate - other sessions CHEWCK`. This lane translated the supplied current German Paper 1 interval. It did not collate scans, source-check or adjudicate the German, validate translation/formulas/terminology, inspect rendered pages, localize regional Hant prose, approve, archive, publish, or certify the work.

## Authority and cursor

- Current German authority pointer SHA-256: `FAC89D076DCE1C24B534595595B75BA1C88A8956E370EF848B307E731633EED1`.
- Current German whole TeX SHA-256: `443EF950D7D45DC6D9E44A9B87501620C10DA873E50E5F2B253ECCAE6A946D27`.
- Exact Paper 1 interval: lines 381–460, raw UTF-8 bytes `[12505,20587)`, 8,082 bytes.
- Exact local source: `source/Noether_Paper01_CurrentGermanAuthority_interval.tex`.
- Exact German interval SHA-256: `0499985866E646747EC31533775FF31B55556F2C694F4C2608384829DE248D2F`.
- Inherited Simplified-Chinese drafting-witness interval: lines 339–466, raw UTF-8 bytes `[13119,21535)`, SHA-256 `566D05E74A03113F77EC75986115F2D7D71914E09B80C96AD5DF537D26F152E3`.
- The witness raw offsets include the cumulative file's three-byte UTF-8 BOM; `ZH-D080` corrects the earlier decoded-text coordinate statement.
- `SOURCE_CUSTODY.md` SHA-256: `8AFE5BC676B48F76EE48F251F8E753B1ADCD6EA2500D1AD4927F4B531DD6F632`.
- Paper 2 is excluded. The stale shared R821 pointer was not used.

## Translation deliverables

- `zh-Hans-CN/Noether_Paper01_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex`
  - SHA-256: `5C9B88F787C447E32B1CFDF6FCFC101A69C0CB87BC7B92F703AFAC9D4C618171`.
- `zh-Hans-CN/Noether_Paper01_Chinese_CurrentAuthority_zh-Hans-CN_v001.pdf`
  - SHA-256: `0B0EB73647981EB9FFC745C65A9AC29B0B4D1CE03C8F9BEB1D0D2E977E302303`.
- `zh-Hant-controlled/Noether_Paper01_Chinese_CurrentAuthority_zh-Hant-controlled_v001.tex`
  - SHA-256: `3659576C350D38F9CE2B682FB0E011A5547485A62CEEC544BAB3FA997CD0A082`.
- `zh-Hant-controlled/Noether_Paper01_Chinese_CurrentAuthority_zh-Hant-controlled_v001.pdf`
  - SHA-256: `838CBA98C6DB190C03522D1B60C39C863C18AF528D59A454984551EAC3CD6F83`.

The Hant deliverable is controlled generic only, not `zh-Hant-TW`, `zh-Hant-HK`, or `zh-Hant-MO` localization.

## Mechanical production

- `BUILD_REPORT.md` SHA-256: `0410FD2CD74F88618511747E0A41EA5CABEBBFE0539D141454A8E69DC697AF0F`.
- Both final targets completed two successful XeLaTeX passes and produced compiler-reported 2-page PDFs.
- Hans final log SHA-256: `F4C78F614B4395B2D0622ECCAB137A93339EDDD3C4AC5548E2834CD58E4758D7`.
- Hant final log SHA-256: `98A3A99433210D8A1BCEF43342FCA5C6BBDBB8CC30EBEA1C53CA7D1135E4D729`.
- Each final log has zero error/fatal/missing-dollar, package-warning, ordinary LaTeX-warning, overfull, underfull, and missing-character matches. Each records the unavailable italic CJK font shape and its summary occurrence.
- Source custody record SHA-256: `819F9077DCD2F7BF095ED5D76A882EE6488C21D9DEA55DEA6F895CA694246F8C`.
- Source segmentation record SHA-256: `896858043709B49C19CE3138D5BFF9F9FC7ABDF37979A7264BAA51D7E042C218`.
- Hans assembly record SHA-256: `E2D759B3049ECB0464EB5E55C9DCE7006810238888164E4C65C0714AA0B4D278`.
- Controlled-Hant OpenCC producer record SHA-256: `E4545BEA9028D74B9496994886ED3A6E5F31C28CD27B15E995DA07447483C1CF`.
- No PDF page was rendered to an image or viewed by this lane.

## Producer evidence for the checker

- `TRANSLATION_NOTES.md` — SHA-256 `540004659CDF4B572797528A36CA6F324F16993B660868F4E07306771C11DBB3`.
- `STATUS.md` — SHA-256 `BE18D289911646DE15E503CEE0847C0E808B056F7492D867B3F640286A45331B`.
- `evidence/TERMINOLOGY_LEDGER.csv` — SHA-256 `38D478E8E6D650787EDA73CFDC7AB27D4A79E13E32BB3C9B372E04CF38628FFA`.
- `evidence/ADVERSE_EVIDENCE_LEDGER.csv` — SHA-256 `58D258877D4C76949399384BC6F8D84E6E6FD5BA97BAD83890B3A5DEC9B92BAD`.
- `evidence/CJKV_CROSSWALK.csv` — SHA-256 `17BEAA43143FA3C399698DFD9DCEED2F70D157F81C0DF94F93776A678EA90AD1`.
- `evidence/CONCEPT_EVIDENCE_GRAPH.json` — SHA-256 `BF24C1E5FD32CF8B3B3EAA9DE542A4D439B29CFF9ABBEB74BF8EE557C834F57F`.

The three CSVs each contain 20 producer rows. The graph mechanically parses as 100 nodes and 100 edges. Entries are producer proposals with independent checking absent; trap-prone entries include sense windows, alternatives, qualitative Mandarin-Simplified dominance debt, and provisional lexical-attractor basin. Japanese and Korean were not consulted and are not Chinese authority.

## Independent checker requested

Please check Hans against the exact German interval; verify every title/byline/front note, bibliography detail, footnote, formula, symbol, table cell, theorem statement, enumeration, and segment boundary; render and visually inspect both PDFs; and separately assess the controlled-generic Hant derivative. Mandatory terminology attention includes:

- `Formensystem` / `Bildung` / `Bildungen` → `型系统` / title `构成` / `构成式`;
- historical `automorphe Form` → `自同构型`, distinct from modern analytic automorphic-form usage;
- source-defined `Ordnung` / `Grad` → `阶` / `次数` within their coefficient/variable dimension sense window;
- `Invariante` / `Kovariante` / `Kontravariante` → `不变式` / `协变式` / `逆变式`;
- `relativ vollständiges System` / `absolut vollständiges System` → `相对完备系统` / `绝对完备系统`;
- historical invariant-theory `Modul` → `模`, which collides with algebraic module and modulo senses;
- `Überschiebung` → `换位运算（Überschiebung／transvection）` on its first occurrence;
- `Faltungsprozeß` / `Faltung` / `Grundfaltung` → `缩并过程` / `缩并` / `基本缩并`;
- `Formenreihe` / `Reduzent` / `doppelte Reduktion` / `Faltung mit zerfallenden Formen` → `型列` / `化简子` / `双重化简` / `同分解型作缩并`;
- current-source formula `\nu(s)=(ss'u)^4\ldots`, which the producer preserved instead of importing a witness variant.

Please return corrections in a checker-owned append rather than silently rewriting producer history. The italic-shape substitutions require checker-owned visual handling.

No source defect was adjudicated or asserted by this lane. If a checking session identifies a precise possible Noether source defect, it must first deduplicate it and then ensure that `4 -nterslav` receives it under Floris's instruction; this producer lane must not self-adjudicate or duplicate-route it.

Lane log: `C:/Users/Floris/Documents/interlanguage/03_projects/language_management/cjk/00_lane_control/CHINESE_DECISION_LOGBOOK_20260718.md`, producer-freeze decision `ZH-D081`.

Scope remains Noether only. SGA is held until Floris explicitly confirms it.

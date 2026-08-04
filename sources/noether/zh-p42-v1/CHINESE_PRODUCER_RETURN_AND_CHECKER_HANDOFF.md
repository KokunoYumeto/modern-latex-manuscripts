# Noether Paper 42 — Chinese producer return and independent-checker handoff

Producer state: **complete Chinese translation and mechanical builds; independent check pending**.

This lane translated the supplied current German Paper 42 interval. It did not collate scans, check or adjudicate the source, validate translation/formulas/terminology, inspect rendered pages, localize regional Hant prose, approve, or certify the work.

## Authority and cursor

- Current German whole TeX SHA-256: `443EF950D7D45DC6D9E44A9B87501620C10DA873E50E5F2B253ECCAE6A946D27`.
- Exact local interval: `source/Noether_Paper42_CurrentGermanAuthority_interval.tex`.
- Interval SHA-256: `B6BB3A6267BA8495FC19914A72768351E4923B13374634701AF3CBDE659883CC`.
- Inherited Simplified-Chinese drafting-witness interval SHA-256: `6570BA44DE36A51B4C198B16F647FA5E57586B7734E91989D531AE015E1D2492`.
- `SOURCE_CUSTODY.md` SHA-256: `1E5B4F6500F9E3B11EC5EF1A969E6129626547FF72F63EE015D4F0B3940DE58E`.
- The stale shared R821 pointer was not used.

## Translation deliverables

- `zh-Hans-CN/Noether_Paper42_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex`
  - SHA-256: `B326FA4696A29D4B6393E85651FDF07EF072C452CAB3BDD93A9BB271285E6625`.
- `zh-Hans-CN/Noether_Paper42_Chinese_CurrentAuthority_zh-Hans-CN_v001.pdf`
  - SHA-256: `D27ABE145A7FCD5F3BF6BF80245E7560A2FB6CDDC5889D72D5F834BB9174A7BC`.
- `zh-Hant-controlled/Noether_Paper42_Chinese_CurrentAuthority_zh-Hant-controlled_v001.tex`
  - SHA-256: `8D8EE8B75EB83D90B03BD646E8453D6C0E0CBCF72B08452005185A482C131F57`.
- `zh-Hant-controlled/Noether_Paper42_Chinese_CurrentAuthority_zh-Hant-controlled_v001.pdf`
  - SHA-256: `1263EC5E734E700C3B63D301582BF97C2F5EB9B333FED0FC4DB63F08B9F54A12`.

The Hant deliverable is controlled generic only, not `zh-Hant-TW`, `zh-Hant-HK`, or `zh-Hant-MO` localization.

## Mechanical production

- `BUILD_REPORT.md` SHA-256: `DFBA6C0BB84B90289E55B908E35BF9EE8AA3DCCA4A9A7EF16C26C9C7DD27AD08`.
- Both targets completed two successful XeLaTeX passes and produced five-page PDFs.
- Each final compiler log contains one unavailable italic-shape warning plus the summary substitution warning; no fatal error or undefined control sequence.
- OpenCC producer record SHA-256: `36C8AC62CEDE3EE4D9C37A340B6A7DDC9BB22CAD78D77A564BE4A16AA351D70C`.
- No PDF page was rendered or viewed by this lane.

## Producer evidence for the checker

- `TRANSLATION_NOTES.md` — SHA-256 `647AE5B9799B5BB27DEA75A4DCDBA758B61E2D6B0027F503FB651C6AED4D0963`.
- `STATUS.md` — SHA-256 `FC33BF8145F1A39B2D03A0CC7023C779852B5233468295F1C376617FFFAA3BDF`.
- `PRODUCER_STRUCTURAL_INDEX.json` — SHA-256 `311AFA30C3DC03849CB2B22FD6E9A07E9E507DA125B6B2440361E0B5162F1499`.
- `evidence/PRODUCER_TERMINOLOGY_LEDGER.csv` — SHA-256 `44584AED35C2BA8E84FAD6ED3484357F2638B1869589A6506024C812AC6AB0D3`.
- `evidence/ADVERSE_SENSE_LEDGER.csv` — SHA-256 `561EFAC6C2D40AA18E5D501A7FCCE6C699CF6BD36A06F86E57238B6FE4123CE1`.
- `evidence/CJKV_CROSSWALK_P42_ZH.csv` — SHA-256 `17263CAADB580870585DD886B972D2EB385936AC051D8B32941DDF9EC6E81656`.
- `evidence/PRODUCER_CONCEPT_GRAPH.json` — SHA-256 `8FE7ACA2A3B6861523975072FF225E3A8920474AEB05F44F753B459314CFF0A5`.

Each CSV has 20 rectangular producer rows. The graph has 100 typed nodes, 100 edges, and `independent_check: absent`. Japanese and Korean were not used as Chinese authority. The artifacts document producer choices, sense windows, adverse readings, alternatives, lexical-attractor basins, and qualitative Mandarin-Simplified dominance debt; none is validation.

The evidence producer initially left one terminal blank record in each CSV. `qa/EVIDENCE_CSV_NEWLINE_RECORD.json`, SHA-256 `5E1AB2DB619FD2AA976A0FD85AD73436147D3049F81A25359543BC0017E4879F`, records removal of only those blank records.

## Independent checker requested

Please check Hans against the exact German interval; verify all formulas, notes, theorem statements, and terminology; evaluate the trap-prone forms including `区域/主区域`, `主阶`, `互补基`, `关于 p 的商环`, and technical `不同理想`; render and visually inspect both PDFs; and separately assess the nonregional Hant derivative. Return corrections in a checker-owned append rather than rewriting producer history silently.

No source defect was adjudicated or asserted by this lane. Any checker-discovered source issue belongs to the established duplicate-aware source-owner/`4 -nterslav` workflow.

Lane log: `C:/Users/Floris/Documents/interlanguage/03_projects/language_management/cjk/00_lane_control/CHINESE_DECISION_LOGBOOK_20260718.md`, latest production decision `ZH-D071`.

Scope remains Noether only. SGA is held until Floris explicitly confirms it.

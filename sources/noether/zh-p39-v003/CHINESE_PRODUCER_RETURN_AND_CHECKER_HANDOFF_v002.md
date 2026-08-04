# Noether Paper 39 — Chinese producer return and independent-checker handoff v002

Producer state: **exact current-authority binding and mechanical dual-target build complete; independent check required**.

## Authority

- Binder: `NOETH-DE-BINDER-P39-ZH-COMPLETE-20260804-001`.
- Receipt: `authority/CHINESE_P39_COMPLETE_BINDER_20260804.json`, 8,623 bytes / SHA-256 `39C97E6424B0ACCD8FFDFD218A422F59501BFC48456000BAB717F0CC15951E8C`.
- Pointer: `NOETH-DE-AUTH-v006-20260804`, snapshot 20,666 bytes / `DB99DD87100654674D7ED24B4ABBBBC3A9920CCF035740D276CE8A87A5313C18`.
- Default authority ED0001: 2,153,565 bytes / `D1F06B311F6CBD991DD247D745DD9A72DDE326A20396DF43CFE0C8EDB1593CDB`.
- Complete P39: lines 19051–19140; canon-owner raw span 18,814 bytes / `7B79F86BC2845F2F1A6BEF69664E4E91645C66F8E0C001C1FEF7AFE167551711`; retained LF unit 18,724 bytes / `4F6355189925F249DE27FE5FD25C22FB3A2226088EBB7CAF5CB486607A112B7C`.
- Canon-owner ruling: preserved German witness is LF-byte-identical; only 90 CR bytes differ; zero translation-visible source delta; no source defect claimed.

## Exact targets

- `zh-Hans-CN/Noether_Paper39_Chinese_CurrentAuthority_zh-Hans-CN_v002.tex` — 16,141 bytes — `101836C41985DEE9B1A8FCC74A76CD9DF082BE2D07E2A3D45E22BC4DE68C6FE6`.
- `zh-Hans-CN/Noether_Paper39_Chinese_CurrentAuthority_zh-Hans-CN_v002.pdf` — 261,533 bytes — `367061323E97D9D7431B883D48F190A214A224D62F3901C8E01DD1BCA7125BA1`.
- `zh-Hant-controlled/Noether_Paper39_Chinese_CurrentAuthority_zh-Hant-controlled_v002.tex` — 16,322 bytes — `DEF7DFDCF1545066447880698B1A1C109D4BBED2CEDC4B8409D786044FCEEE33`.
- `zh-Hant-controlled/Noether_Paper39_Chinese_CurrentAuthority_zh-Hant-controlled_v002.pdf` — 276,331 bytes — `EE22B4475DB19B48FDD7838A307C0069CE06682EBDC370AB4A9BBE46DEC431C5`.

Both v002 document bodies beginning at `\documentclass` are byte-identical to their v001 counterparts. The only Hans change is source-authority metadata before the document body; Hant was freshly regenerated from exact Hans and likewise retains its prior document body.

## Mechanical production

Hans and Hant each completed two serial XeLaTeX passes with exit code `0`. Each PDF has four pages by compiler transcript and `mutool info`. Logs have zero fatal/emergency/undefined-control and zero overfull/underfull boxes; known unavailable small-cap/italic font shapes fall back as recorded. The producer did not render or visually inspect either target PDF.

## Independent checker request

Please independently:

1. replay the binder, pointer, source, target, and frozen-manifest custody;
2. check Hans against the exact retained source, including formulas, footnotes, apparatus, terminology, and all producer sense-window/adverse-evidence choices;
3. verify that zero source-text delta legitimately permits the retained target body;
4. check controlled-generic Hant separately, including conversion-tool false spans and the explicit nonregional claim;
5. compile serially, extract both PDFs, render every page, and visually inspect all pages;
6. return corrections append-only with exact coordinates and hashes.

Do not mutate the producer root. A possible German issue requires the independent-checker-confirmed canon packet; no German defect is asserted here. Hant is generic only; `zh-Hans-SG` and regional Hant are absent. SGA remains held.

Lane decisions through source receipt: `ZH-D143`. The exact freeze manifest and external producer receipt are generated after this handoff document and will be supplied in the route message.

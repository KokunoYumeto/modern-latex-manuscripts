# Noether Paper 3 — Korean U01–U03 checker handoff

Date: 2026-08-04  
State: translation-producer drafts only; all units UNCHECKED

## Bound input

- Current pointer: NOETH-DE-AUTH-v003-20260804; SHA-256 932FEDC1735A41A9CF71D15A6C662A468A4CAD016AE8B3DECDF9A71E8BA7F197.
- German authority: NOETH-DE-ED-0001; supplied whole SHA-256 D1F06B311F6CBD991DD247D745DD9A72DDE326A20396DF43CFE0C8EDB1593CDB.
- Exact Paper 3 interval: whole lines 3573–3608; 8,277 LF UTF-8 bytes; SHA-256 E600FD2A19ACA22F43D54FB65C61B79172B12FE5AB09446A2C9C9B8CACD26E7D.

| Unit | Source lines | Source-slice SHA-256 | Target SHA-256 |
|---|---:|---|---|
| U01 | 3573–3584 | DF50EAD7065F663901F51ADFCA37A138921063362CA449665D37B855921B496C | 057D6EAECAAB02C4D19C6908276C11E32953748726BD36B628712AB5C5E78ECB |
| U02 | 3586–3594 | A7B7CA981F7B8D6B32171BF0709E27440A25B2754642BD095304E54A5A25D5C6 | A2A9F68B55C15EEFEAE178B4F24CB5D56222E563F6B5A126F46D1AA75BEA38B1 |
| U03 | 3596–3608 | 0D110465AEE20E18EE1427577D33D435FCF97D5CA99BEF3878EF52DC341F01A5 | 7942126177C707C89F67444BE020F90F2139C0C5036A153297C0A7F83119F4B4 |

Target root: ${PUBLIC_INTERLANGUAGE_ROOT}/03_projects/language_management/cjk/03_working_translations/noether_paper03_ko_translation_001_20260804/targets

Exact target names are Noether_P03_Korean_U01_UNCHECKED.tex through Noether_P03_Korean_U03_UNCHECKED.tex.

## Producer metadata

- SOURCE_CUSTODY.md: 2,433 bytes; SHA-256 0475B7BED3D5190C4A6C29D75F8E4FD7BB5E74DB4D943AB54E729E4696A252A5.
- TRANSLATION_CHOICES_U01_U03.md: 6,157 bytes; SHA-256 3299C07345D907C6FA387EBB2B18A7E656EF95A6181F4D38EC07EED402ED4AB3.
- STATUS.md: 2,955 bytes; SHA-256 AFC0DFA2EB79BCBDBEF04E7CB7E06C250E938CD70E171A50FAB0E54F6A19078D.

The choices file exposes the unresolved arity style, Reihe family, Matrizenprodukt sense, Faltung, kogredient/kontragredient, Reduzent, Zerlegungsidentität, Defekt, and Normalformen questions, plus Hangul/Hanja and ko-KP evidence debt.

## Independent-checker return requirements

1. State the independent checker task ID, role, date, and incoming pointer/source/target hashes.
2. Return a disposition for every unit: checked-pass, checked-with-changes, or held, with exact source and target locators.
3. Check Korean semantic fidelity, completeness, syntax, register, names, bibliographic prose, and cross-unit consistency.
4. Check every formula, symbol, range, display, TeX environment, citation, and footnote call independently; producer preservation is not a correctness claim.
5. Resolve or hold every terminology question with Korean-language evidence. Do not use Chinese or Japanese as Korean authority. Record Hangul/Hanja and ko-KR/ko-KP scope explicitly.
6. For changes, return editable TeX, exact before/after hashes, affected units, alternatives rejected, adverse evidence, and remaining uncertainty. Do not silently overwrite producer history.
7. If an independent checker confirms a German defect, route a precise finding packet to the sole German-canon task 019fca5c-0e73-7c72-92fb-5b507b710598. Do not patch German locally or promote a translator guess.
8. State everything not checked. Compilation, rendering, assembly, packaging, certification, approval, publication, archive work, and SGA remain outside this handoff unless separately routed.

Until a durable independent return exists, all three TeX files remain UNCHECKED.

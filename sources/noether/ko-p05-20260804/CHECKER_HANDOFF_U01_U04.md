# Noether Paper 5 Korean U01--U04 independent-checker handoff

Handoff state: UNCHECKED producer drafts. This document requests checking; it does not perform or claim checking.

## Authority and source bounds

- Pointer: NOETH-DE-AUTH-v003-20260804
- Pointer SHA-256: 932FEDC1735A41A9CF71D15A6C662A468A4CAD016AE8B3DECDF9A71E8BA7F197
- German authority: C:\Users\Floris\Documents\interlanguage\03_projects\noether\07_german_canon_control\candidates\NOETH-DE-ED-0001\Noether_German_NOETH-DE-ED-0001.tex
- Authority SHA-256: D1F06B311F6CBD991DD247D745DD9A72DDE326A20396DF43CFE0C8EDB1593CDB
- Paper 5 body: whole-source lines 4535--4573; 8,185 LF UTF-8 bytes; SHA-256 99BD68A8DBD9861EFF0CDBE26CB365C3306EDF15BD93A6C4C10B9F25419D5CAE
- Exclusion: whole-source line 4574 \clearpage.

## Target units

| Unit | Source lines | Source SHA-256 | Target | Target SHA-256 |
|---|---|---|---|---|
| U01 | 4535--4545 | 8AB438E098574B638EB932F7E002A8D894A97DE4872EBEEE7B96EEC52A1C072C | targets\Noether_P05_Korean_U01_UNCHECKED.tex | EEB39C3A693410823F66A75BCE7DBB9906F35637BFFF87A55CE4A7B873A6F203 |
| U02 | 4547--4557 | 3B6528941F0DC23909DEDAE5F9C4AA0598CADE04916DA12094F188BE4983EAB2 | targets\Noether_P05_Korean_U02_UNCHECKED.tex | 62D644153874FFE07C839102D5EF222BCED55F693C1BA6E8E9FF318A670F8DEA |
| U03 | 4559--4563 | 778D2BAE411E136A3760673A839EF0DB9BA79C83F0534F103CF851F5F7E4A698 | targets\Noether_P05_Korean_U03_UNCHECKED.tex | 2B7ADD81855DD9D06A1D2D17249F32F5D7BBDB458F7474E0BB7BC3F14A5FFA89 |
| U04 | 4565--4572 | FF5058094D557ECF29D2EA4A37762067EF5936EAD529E70AF5C5FA0E6B063230 | targets\Noether_P05_Korean_U04_UNCHECKED.tex | 8A50F7549C23A50A6A824C97763941535D12061EE08E32D2EC1D3F678FE4CA6B |

## Checks requested from an independent Korean checker

1. Check every Korean sentence against its exact German unit and record corrections without treating producer coverage as approval.
2. Check all formulas, TeX commands, note markers, bibliography data, quotation macros, names, and section order.
3. Resolve the sense windows in TRANSLATION_CHOICES_U01_U04.md, especially Zahlkörper, Gattungsbereich, affektlos, Integritätsbasis, ganze rationale Verbindung, relativ ganze Funktionen, and Resultante.
4. Supply Korean-local evidence for terminology. Do not infer Korean validity from Mandarin, Japanese, or Sino-xenic resemblance.
5. Decide Hangul-only versus first-use Hanja glosses and state the evidence.
6. State whether the checked target is ko-KR, ko-KP, or separately adapted variants. The producer draft is provisionally ko-KR and does not authorize ko-KP.
7. Check historical personal-name and title treatment without silently modernizing bibliography.
8. Report any suspected German defect as a checker finding with exact pointer, source lines/bytes/hash, proposed correction, alternatives, evidence, uncertainty, and checker identity. Do not patch German in this producer root.

## Known producer risks

- 라그랑주 종영역(Gattungsbereich) and 아펙트 없는(affektlos) 방정식 are explicit unresolved witness-preserving choices.
- 정수성 기저 and the gloss 정칙 유리결합, 곧 다항식적 결합 may conflate historical regular, polynomial, and integral senses.
- 수체 may be too narrow for the historical Zahlkörper window that explicitly allows all complex numbers.
- Korean spacing and Hanja policy remain unchecked.
- No source/scan check, Korean review, formula review, compilation, rendering, or visual QA occurred.

## CSV projection integrity note

- Report: C:\Users\Floris\Documents\interlanguage\03_projects\language_management\cjk\03_working_translations\noether_paper05_ko_translation_001_20260804\evidence\csv_artifact_validation\CSV_PROJECTIONS_ARTIFACT_TOOL_VALIDATION_REPORT.json
- Identity: 2,720 bytes; SHA-256 D968079EC46718F85F4BFC1EC325B8FFFEBECE152D110B1F57DF27BE3C5A40E2
- Result: PASS under `@oai/artifact-tool` import for the structural, difficulty, and visual CSV projections. The imported tables contained respectively 41, 6, and 0 data rows and 24, 20, and 24 columns; all were rectangular, had no blank or duplicate headers, and produced no formula-error match in the bounded inspected regions.
- Scope limit: this is metadata-table integrity evidence only. Rendering was deliberately skipped under the translation-only boundary. The result does not check Korean translation, German source fidelity, mathematical formulas, semantic accuracy, image evidence, or any checker decision. Under `CJK-KO-ARCH-001`, missing checks are archive metadata rather than a publication veto.

## Return requested

Return stable checker finding IDs, exact unit and source/target locators, target before/after hashes for any correction, local evidence, adverse evidence, unresolved items, ko-KR/ko-KP scope, and a clear checked or held state. Until that return exists, every target remains `UNCHECKED`. Under `CJK-KO-ARCH-001`, that state is not a release hold; archive maintenance may preserve and publish it with the label intact.

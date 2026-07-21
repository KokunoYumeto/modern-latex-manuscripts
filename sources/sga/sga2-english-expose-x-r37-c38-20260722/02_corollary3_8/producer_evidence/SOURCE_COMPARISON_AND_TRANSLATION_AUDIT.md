# SGA2 Exposé X — Corollary 3.8 statement and proof

Status: `producer_pass_pending_independent_review`. This is a bounded internal working unit, not a seal, publication payload, independent review, or archive handoff.

## Authority, scope, and locators

- Authority: corrected arXiv French TeX `smf_doc-math_4_01.tex`, 586,789 bytes, SHA-256 `C2F899E92A904E312B550C6452A117FF23D30AF984B2254A0961D2DF0DACD042`.
- Scope: French lines 3536–3540 inclusive; one complete corollary and its one-line proof; 218 Latin-1 LF bytes, SHA-256 `94D108BA11D32F382E082BC77136954852D98A5FCBD1DE545A67C4064F9F3E2D`.
- Boundary: lines 3534–3542; 326 bytes, SHA-256 `0773A5923A4656A65C3D9F2EB2444BFF1B35EDD2EDDAD2D6FAC05DC48206F5CE`.
- Original printed page 120; source-PDF physical page 104; recomposed running page 96.
- Remark 3.7 and blank line 3535 are excluded. Blank line 3541 is excluded and is exactly one LF byte, SHA-256 `01BA4719C80B6FE911B091A7C05124B64EEECE964E09C058EF8F9805DACA546B`.
- Transition line 3542 is excluded; its 90-byte no-EOL identity is `DF17A55BC0E31E17B96E03B83BF2108252101010433948276728DB4A0D519B84`.
- Raw continuation cursor: line 3541. Next substantive cursor: line 3542.
- French authority action: none; authority bytes remain unchanged.

The same-edition reader is 1,576,954 bytes, 216 pages, SHA-256 `41AD02C57321A8D2200FF32A929BC93ADBC3DE0D59DCD5A284D28D859FB87A90`. Its physical-page-104 render is manifestation and layout evidence only, not independent original-print corroboration. The source raster and extracted source page remain rights-gated internal evidence.

## Source-to-target comparison

| Control | French authority | English target | Producer finding |
|---|---|---|---|
| Kind and number | `corollaire`, label `X.3.8` | `Corollary 3.8.` | Preserved visibly |
| Ring | `A` a `anneau local noethérien` | `A` a noetherian local ring | Object and hypotheses preserved |
| Depth hypothesis | `\prof A\geq 2` | `\operatorname{depth} A\geq 2` | Mathematical value and inequality preserved; established Exposé X English operator normalization applied |
| Completion | `\hat A` | `\widehat A` | Completion, base symbol, and hat preserved typographically |
| Purity implication | purity of `\hat A` implies purity of `A` | same | Direction and both purity predicates preserved |
| Proof | follows from Lemmas 3.5 and 3.6 | same | Both references and order preserved |

The target uses “Assume that” and “If …, then …” instead of the French sequence “Supposons … Alors si …”; this is idiomatic English syntax with no change in logical strength. It supplies the standard structural label “Proof.” before the separately printed proof line and does not invent a QED symbol absent from the source.

The bounded source-defect scan found no grammatical, mathematical, numbering, reference, or symbol defect and no unresolved source ambiguity. In particular, both Lemma 3.5 and Lemma 3.6 exist in the admitted source and are the same references printed in the PDF. No silent French emendation occurs.

## Terminology and comparison lineage

Accepted English register:

- `anneau local noethérien` → “noetherian local ring”;
- `prof` → the established English operator “depth” while preserving the value and inequality;
- `pur` → “pure”;
- `Résulte de` → “This follows from.”

The current jcreinhold `e7a259f` Markdown is comparison-only, not authority or independent corroboration. Its whole-file SHA-256 is `2BDDBC3D15EECE7A47FDBDFBE31DAE735446BC14480A75113E704F63901C7BF5`; exact comparison lines 392–398 are 184 UTF-8 LF bytes, SHA-256 `D2D01AAE6DEFA0BA3A8F3D5A6E3BFC4FA03CED70498B1C541B9001D457B6673D`.

Accepted after French verification: complete coverage of the ring, depth bound, purity implication, and both proof references. Rejected or normalized choices:

- its visible heading is merely `Corollary.` with the number hidden in a comment; the target exposes source number 3.8;
- its literal `prof` is normalized to established mathematical English `depth`;
- its code-formatted completion glyph is typographically degraded; the target uses mathematical `\widehat A`;
- its “Then if” syntax is replaced by the clearer “If …, then …”;
- its proof line lacks an explicit structural label; the target adds “Proof.” but no unsourced QED mark.

## Build, render, and PDF gates

- Target TeX: 1,563 bytes, SHA-256 `856B396D68A41AD2F6EAFD17AB50C0B2167519D4361E378EFE1F758BFEF9146B`.
- Target PDF: 184,318 bytes, one A4 page, SHA-256 `109C9F32D3560C940D0EE27EAEFC0977E42279D20735195EBDB625B3EB709B97`.
- Three pdfLaTeX passes succeeded with no warnings, overfull/underfull boxes, or errors; the three console logs are byte-identical, 7,162 bytes each, SHA-256 `8EBA67279666BCD14D8A846087ECB6B78E55C65D323A7E89CB717964796F31DF`.
- Target extracted text: 1,030 bytes, SHA-256 `2D84488EFC1FA13497CBCA9E6A555D66E33A1B0AE2C24F22311F965A3F04A9B6`.
- Target font report: 1,235 bytes, SHA-256 `D039DF39FC595FCD67254A52BA4DDA802170589E0165B63406B49F396E58B65A`; 11/11 font rows are embedded, subsetted, and Unicode-mapped.
- Target 200-dpi render: 133,303 bytes, SHA-256 `601912F151D06316F8B18897D1CAF75DDECFD35363DC215DE8F1A670E3600094`.
- Fresh source physical-page-104 render: 392,630 bytes, SHA-256 `0CBF631AC8F698115683A90439E57C357549A2AC7F76CD3BC3AAA7CFEC0165EE`.

Original-detail inspection of both source and target renders confirms the number, depth inequality, completed-ring hat, implication direction, Lemma 3.5/3.6 references, and boundary. No clipping, overlap, missing glyph, black box, or formula ambiguity is visible. The internal PDF has no metadata stream and is untagged; it is not a publication artifact.

## Custody

All artifacts remain `internal_not_for_release`. Machine ledgers, Artifact Tool QA, privacy scanning, and the true-ordinal manifest accompany this audit. Independent review remains required. No shared decision-log edit, archive handoff, GitHub action, or Zenodo action is claimed.

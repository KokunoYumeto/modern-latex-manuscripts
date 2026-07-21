# SGA 2, Exposé X — Remark 3.7

## Producer disposition

The bounded English target for corrected French authority lines 3532–3534
passes the producer source, translation, formula/symbol, terminology, boundary,
locator, build, font, extraction, and visual checks described below. This is
`producer_pass_pending_independent_review`, not a seal or publication claim.

The French authority remains byte-identical. Lines 3522–3530 belong to the
preceding Lemma 3.6 proof and are excluded; blank line 3531 is excluded. Blank
line 3535 and the Corollary 3.8 opening on line 3536 are excluded. The raw
continuation cursor is 3535 and the next substantive cursor is 3536.

## Scope and locator separation

- Current-rescribe source lines: 3532–3534.
- Editable translation units: 1 complete remark.
- Original printed page: 120.
- Source-PDF physical page: 104.
- Recomposed running page: 96.
- Target: one editable TeX file and one one-page A4 PDF.

The fresh source-page render visibly shows running page 96, Remark 3.7, and
the later original-page marker 121 below Corollary 3.8. Thus the remark remains
on original printed page 120. These three locator systems are not conflated.

## Authority and source evidence

- Corrected French TeX: 586,789 B; SHA-256
  `C2F899E92A904E312B550C6452A117FF23D30AF984B2254A0961D2DF0DACD042`;
  ISO-8859-1, LF-only, unchanged.
- Exact lines 3532–3534: 218 B; SHA-256
  `7F0D9E686076D85702CAA5E3E9F5216AC73B0EF78E271E88ACA58573C73BB18D`.
- Boundary lines 3530–3536: 976 B; SHA-256
  `50EDDFB359B8CF97E35C23C05DAD9058F1EFA64AFD1F7D79B3B60373B282E04D`.
- Excluded preceding proof line 3530 without EOL: 722 B; SHA-256
  `63D2615167DCCFFBCBEE8E1AB86994C5D5FFC61A6D39A54F3A5A9214F7CED6C0`.
- Excluded blank line 3535 is exactly one LF byte; SHA-256
  `01BA4719C80B6FE911B091A7C05124B64EEECE964E09C058EF8F9805DACA546B`.
- Excluded Corollary 3.8 opening, line 3536 without EOL: 32 B; SHA-256
  `0C7A650AFCBC72EC15F50C0829C8E1788BB83948389C62AE3FD1F2345041335D`.
- Same-edition reader: 1,576,954 B, 216 pages; SHA-256
  `41AD02C57321A8D2200FF32A929BC93ADBC3DE0D59DCD5A284D28D859FB87A90`.
- Fresh physical-page-104 render at 200 dpi: 392,630 B; SHA-256
  `0CBF631AC8F698115683A90439E57C357549A2AC7F76CD3BC3AAA7CFEC0165EE`.

The same-edition reader and raster are manifestation/layout evidence only, not
independent original-print corroboration. The source renderer emitted the known
legacy display-font notices; the rendered text and mathematical symbols remain
clear. Source slices and the source raster are rights-gated evidence.

## Translation, formulas, and terminology

| Control | French authority | English target | Producer finding |
|---|---|---|---|
| Heading | `Remarque`, label `X.3.7` | `Remark 3.7.` | Kind and visible numbering preserved |
| Retrospective register | `On a prouvé chemin faisant` | “We proved along the way” | Proof status and idiom preserved |
| Hypothesis | `O_X→i_*O_U` is an isomorphism | same | Source, target, arrow, and assertion preserved |
| Connectedness | `X` connected iff `U` is connected | same | Biconditional and both objects preserved |
| Fundamental-group map | `π_1(U)→π_1(X)` | same | Domain, codomain, direction, and subscripts preserved |
| Conclusion | map is surjective | same | Consequence and strength preserved |

The target repeats “connected” after `U` rather than using an elliptical “is”;
this is an English clarity choice with no logical change. It retains the
inherited immersion symbol `i` without inventing a new definition. “Connected,”
“isomorphism,” “fundamental group,” and “surjective” follow the established
SGA2 English register.

The bounded source-defect scan found coherent French grammar, a well-typed
sheaf map, an unambiguous biconditional, and a correctly directed fundamental-
group map. There is no source defect or unresolved ambiguity and no silent
French emendation.

## External English comparison

The current jcreinhold `e7a259f` Markdown chapter is comparison-only, not
authority and not independent corroboration. Whole-file SHA-256:
`2BDDBC3D15EECE7A47FDBDFBE31DAE735446BC14480A75113E704F63901C7BF5`.
The frozen lines 383–390 slice is 257 B; SHA-256
`806B8F540EE1B7D3DA5016B05C11A6BBA4FB74AFD6F6C3F799D45B7332317EEC`.

Accepted only after checking against French: complete coverage of the
hypothesis, connectedness equivalence, map direction, and surjectivity.
Rejected or normalized choices:

- the candidate's unnumbered visible `Remark.` plus hidden label becomes the
  source-visible `Remark 3.7.`;
- “shown in passing” is normalized to the closer source-register rendering
  “proved along the way”;
- elliptical “if and only if U is” is expanded to “if and only if U is
  connected” for clarity;
- the candidate comment `original page 96` is rejected as a locator error:
  96 is the recomposed running page, while the original printed page is 120.

## Build and rendered QA

- Target TeX: 1,623 B; SHA-256
  `AF2A17669348B4B5B25C0F7DBC4476DAFBD5A1DD68A199C9AF97E16EA1314F0B`.
- Target PDF: 201,876 B; SHA-256
  `699745968DAEB371AC26F389976A61F15F63083DB2231C96D5D69C53162C6269`;
  one A4 page.
- Three pdfLaTeX passes succeeded. Pass 1 contains only the expected initial
  `rerunfilecheck` warning; passes 2 and 3 have no warnings or errors and their
  console logs are byte-identical.
- Font gate: 13/13 rows are embedded, subsetted, and Unicode-mapped.
- Extracted target text: 1,101 B; SHA-256
  `DE2D450407A5F029A23FC73DE8FC69E2FD59EF6FF2BBA1A9CC9E207F3D0DDE8A`.
- Target 200-dpi render: 149,450 B; SHA-256
  `CF375B491B7A3AE36DC2AA891535C43ED62985B3D038E193590BFEA599A6907C`.

Original-detail inspection shows a legible authority box and complete remark;
the sheaf map, biconditional, and fundamental-group map are clear. There is no
clipping, overlap, missing glyph, black box, or formula ambiguity. The internal
PDF has no XMP stream and is untagged; it is not a publication artifact.

## Next gate and custody

Machine CSV/JSONL, Artifact Tool, privacy/rights, and recursive-manifest gates
must accompany this audit. Every file remains `internal_not_for_release`.
Independent review is still required. No archive handoff, shared decision-log
write, GitHub action, or Zenodo action is claimed.

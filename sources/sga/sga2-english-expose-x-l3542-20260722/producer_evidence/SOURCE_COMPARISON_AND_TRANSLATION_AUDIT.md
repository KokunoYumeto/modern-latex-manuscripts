# SGA2 Expose X - transition to Lemma 3.9

Status: `producer_pass_pending_independent_review`. This is a
bounded internal unit, not a seal, public payload, or archive handoff.

## Authority, scope, and locators

- Authority: corrected arXiv French TeX `smf_doc-math_4_01.tex`, 586,789
  bytes, SHA-256
  `C2F899E92A904E312B550C6452A117FF23D30AF984B2254A0961D2DF0DACD042`.
- Scope: French line 3542 only, the transition sentence immediately before
  Lemma 3.9.
- Locators: original printed page 120; source-PDF physical page 104;
  recomposed running page 96.
- Excluded before: Corollary 3.8 and proof through line 3540, plus blank 3541.
- Excluded after: blank 3543 and Lemma 3.9 beginning line 3544.
- Raw continuation cursor: line 3543. Next substantive cursor: line 3544.
- The French authority remains byte-identical.

The same-edition 216-page reader is manifestation and layout evidence only,
not independent original-print corroboration. Its physical page 104 visibly
places the sentence between the proof of Corollary 3.8 and the heading of
Lemma 3.9.

## Translation and comparison

French: `Le lemme suivant est le point essentiel de la demonstration du
theoreme de purete:` (accents encoded by TeX commands).

English target: `The following lemma is the essential point in the proof of
the purity theorem:`.

The translation preserves the forward deictic reference, `lemma`, the
importance qualifier `essential`, the proof relationship, the named purity
theorem, and the terminal colon. `demonstration` is rendered as the standard
mathematical English `proof`. No formula, reference number, footnote, or
source emendation occurs in the bounded sentence.

The current jcreinhold `e7a259f` Markdown is comparison-only. Its line 400
uses the same sentence. This agreement is useful for register comparison but
is not independent corroboration because it is one LLM-generated candidate
lineage. Rejected alternatives include `key step`, which is idiomatic but
less literal, and `demonstration`, which is nonstandard here in English.

## Gate

The producer froze exact source and comparison slices, ran three clean
pdfLaTeX passes, inspected target and source renders, validated stable-ID CSV
and JSONL evidence, and ran Artifact Tool tabular QA. The target TeX is 1,356
bytes, SHA-256
`5B188F1951434DCCF7809CCFFEF0CCD0728231D1B8FD2B145F35471627771A89`;
the deterministic one-page PDF is 136,849 bytes, SHA-256
`DD4610237E4FE8D0CA8AD026BD24DD2228FCB87317AA4C7716779712BD0C664A`.
All three build logs are byte-identical at 6,354 bytes, SHA-256
`94804C60F9E06C7AA53E02BDB5FC99ACFC9C79E70777F52790284D804052A102`,
with no TeX errors, warnings, overfull boxes, or underfull boxes.

The target render is 115,437 bytes, SHA-256
`21EF987175F8751B42FCEBD8A3B3E2C7AA9F4C806720E7DD1026D87DD18743FF`;
the source-page render is 392,630 bytes, SHA-256
`0CBF631AC8F698115683A90439E57C357549A2AC7F76CD3BC3AAA7CFEC0165EE`.
Original-detail inspection found no clipping, overlap, missing glyph, black
box, or punctuation loss. The five Artifact Tool panels cover all 26 columns
and 25 data rows; their receipt reports zero formula errors or formula-safety
triggers and unique nonempty IDs.

A fresh independent review remains required before any seal or
archive-maintenance handoff.

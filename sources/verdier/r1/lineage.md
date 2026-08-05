# Authority and comparison lineage

Status: controlling  
Scope: complete Astérisque 239 only

## Controlling authority

`verdier:numdam:asterisque239`

- Path:
  `C:\Users\Floris\Documents\Papors\OS\AST_1996__239__R1_0.pdf`
- Bytes: 19,188,423
- Physical pages: 270
- SHA-256:
  `6214C252BACEBA5584E3C4AEB564C129851941C1A9250BABAB45B79A3939B0AE`
- Admissibility: controlling textual, mathematical, typographical, page, and
  visual authority for the complete issue.
- Rule: every admitted unit records this hash and exact physical/printed or
  unnumbered coordinate. Extraction and inherited text cannot substitute.

Physical page 1 is the NUMDAM access wrapper. Physical page 2 begins issue
content. The hard stop is physical page 270. The authority contains front
matter, Luc Illusie's preface, Georges Maltsiniotis's editor material, Verdier's
historically unfinished thesis body, indexes, bibliography, and contents. Those
roles are mapped separately; their presence in one PDF does not merge their
authorship.

## Comparison witness 1

`verdier:comparison:djvu`

- Path:
  `C:\Users\Floris\Documents\Papors\OS\Des categories derivees des categories abeliennes (Verdier J.-L.).djvu`
- Bytes: 1,330,094
- SHA-256:
  `7D20F3E0F62E58E8CE27DB038BCAD6D8821CDEA7D0E49D27EEBB8EC1225F7F63`
- Admissibility: comparison only. It may clarify a damaged or unreadable
  primary image after an explicit page-level decision.
- Prohibition: it may not silently decide diplomatic text, fill a missing
  passage, or displace the NUMDAM/SMF authority.

## Comparison witness 2

`verdier:comparison:pdf`

- Path:
  `C:\Users\Floris\Documents\Papors\OS\Des categories derivees des categories abeliennes (Verdier J.-L..pdf`
- Bytes: 8,705,514
- SHA-256:
  `9F93C0BB3131F720B9C736E7C2E7834E76500A62B3C68155FCFE62301C5DA4EB`
- Admissibility: comparison only under the same page-level rule.
- Prohibition: no authority promotion from convenience, extractability, OCR,
  apparent cleanliness, or agreement with an inherited translation.

The unusual filename is reproduced literally. It is not silently normalized,
because the exact path is part of custody.

## Other witness classes

The following are never controlling authority:

- existing OCR or PDF text extraction;
- reconstructed or inherited TeX;
- earlier French or English transcriptions;
- later translations or scholarly expositions;
- Stacks Project material;
- other Verdier works; and
- memory, model preference, or mathematical plausibility.

They may locate a page, propose a reading, identify a possible correction, or
support a separately attributed external comparison. The direct authority
still decides the source layer. Later mathematical material may never complete
the historically unfinished thesis body.

## Comparison-use record

Every use of a comparison witness must append a stable decision containing:

- local unit and layer;
- controlling authority SHA and exact page;
- comparison witness ID, hash, and corresponding page;
- defect or ambiguity in the controlling image;
- both visible readings;
- adopted diplomatic reading and confidence;
- effect, if any, on corrected French or English;
- rejected alternative;
- reviewer and review method;
- exact inverse and supersession fields; and
- recurrence test for other pages with the same image defect.

If the primary image is sufficient, no comparison witness is needed. If the
primary and comparison witnesses conflict and direct authority remains
ambiguous, the reading stays unresolved; plausibility cannot convert it into a
fact.

## Identity gate

`SOURCE_AUTHORITY.csv` is the machine-readable projection of this lineage. A
restart or cumulative source seal fails if:

- the controlling PDF bytes, page count, or hash differ;
- a comparison file is missing when cited by an active decision;
- an authority ID resolves to more than one path;
- a source unit lacks the controlling hash and coordinate;
- a comparison-only witness is typed as controlling; or
- an external work enters the admitted Astérisque 239 page range.

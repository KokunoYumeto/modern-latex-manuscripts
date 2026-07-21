# SGA2 Exposé X Remark 3.7 — fresh independent visual QA

Status: **PASS**.

The reviewer inspected the fresh 200 dpi source and target renders at original
detail on 22 July 2026.

## Source witness

`rendered_qa/SOURCE_PHYSICAL104_200DPI.png` is the independently rendered
physical page 104 of the 216-page same-edition reader. It is 392,630 bytes,
SHA-256
`0CBF631AC8F698115683A90439E57C357549A2AC7F76CD3BC3AAA7CFEC0165EE`.

The page visibly shows:

- recomposed running page 96;
- the complete French `Remarque 3.7`;
- the sheaf map `O_X -> i_* O_U`, the connectedness biconditional, and the map
  `pi_1(U) -> pi_1(X)` with its surjectivity conclusion;
- the opening of Corollary 3.8 below the remark; and
- the later original-print marker 121 below Lemma 3.9, so the preceding remark
  remains within original printed page 120.

The Poppler renderer reports the known legacy display-font notices for this
same-edition reader. Inspection shows no lost or substituted mathematical
symbol in the bounded remark. There is no clipping, overlap, black box,
missing line, or formula ambiguity. This PDF is manifestation/locator evidence
only, not independent original-print corroboration.

## English target

`rendered_qa/REBUILD_PAGE001_200DPI.png` is the independently rebuilt target
page. It is 149,450 bytes, SHA-256
`CF375B491B7A3AE36DC2AA891535C43ED62985B3D038E193590BFEA599A6907C`.

The authority box and the complete italicized Remark 3.7 are legible. The
visible number, subscripts, pushforward star, arrows, biconditional wording,
and surjectivity conclusion are intact. There is no clipping, overlap,
missing glyph, black box, bad line break, or ambiguous formula.

The independent rebuild render is byte-identical to the producer target
render. Their extracted text is also byte-identical. The comparison is a
rendering/reproducibility check, not a second translation witness.


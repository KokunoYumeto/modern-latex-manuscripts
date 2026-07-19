# Draft source audit

The target covers corrected French lines 2733--2750 only. It preserves the
opening proof strategy, the local-duality display, equations (2.2)--(2.4), the
editor's-note reference, and all definitions of `S_q`, `S'_q`, and `Z_q`.
Line 2751 begins the next equivalence argument and is excluded.

Formula controls checked directly against the corrected TeX and same-edition
compiled reader:

- `D H^{i-c(x)}` and `Ext^{d(x)-i}` retain both shifts and both local-ring
  arguments;
- (2.2) retains both definitions of `d(x)` and the ordered codimension pair;
- (2.3) retains sheaf Ext before taking the stalk at `x`;
- (2.4) retains the prime on `S'_q`, closes `S'_q` rather than `S_q`, and
  intersects that closure with `Y`;
- the note states vanishing in both directions and retains editor's note (4),
  page 54.

No source ambiguity or target emendation is recorded. The jcreinhold
`e7a259f` passage at lines 360--400 is close but remains one LLM-generated
comparison lineage and supplies no independent source agreement.

The corrected French `\SheafExt` macro renders underlined `Ext`; the target
uses the calligraphic sheaf-Ext typography established across the current SGA2
English units. This is an explicit recorded typography normalization, not a
claim of literal glyph identity; all degrees, bases, arguments, stalks, and
support operations remain source-controlled.

Likewise, the corrected French branch renders the sheaf symbol as plain `F`,
whereas the established SGA2 English units use calligraphic `\mathcal F`.
That target-register typography normalization is separately recorded; it does
not change the sheaf denoted.

Status: self-reviewed production draft; independent source/formula/build/render
review is still required before sealing or handing anything to the archive
owner.

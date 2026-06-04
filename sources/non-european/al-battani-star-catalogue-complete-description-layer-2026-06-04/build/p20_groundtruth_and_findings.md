# Page 20 — manual ground truth + findings (validation anchor for the OCR)

Hand-read from the full Nallino scan at 600–820 dpi. Used to (a) correct the draft and
(b) validate the abjad OCR classifier once trained. Confidence: deg/dir/mag high; minute
cells partly ambiguous (faded dots) — flagged `?`.

## FINDING: longitude convention shifts between sections
- **الحوت / Pisces (p20 top):** longitude is degrees WITHIN the sign of Pisces (0–30). Read
  cells: 11, 11, 13, 11, 6, 7, 8 — no hundreds-letter present.
- **السمكتين / the Two Fishes (p21):** longitude is ABSOLUTE ecliptic degrees (0–360): 334, 337,
  339, 341, 342, 347, 352, 355, 358.
- So one section measures within-sign and the next measures absolute. This must be reconciled in
  the edition (check Nallino's introduction for the table convention). Do NOT silently normalize.

## Pisces (al-Ḥūt), p20 top — confident cells
star | long°(in Pisces) | lat° | lat′ | dir | mag
1 marbaṭ al-kattān, N-leading | 11 | 1 | 25? | N | 5
2 middle of three in cord     | 11 | 5 | 25? | N | 3
3 N of two in mouth of Fish   | 13 | 21? | 45 | N | 5
4 N of three on tail tip      | 11 | 9 | 5  | N | 4
5 leading of three on spine   | 6  | 14 | 14? | N | 4
6 middle of them              | 7  | 13 | 5  | N | 3
7 hindmost of three           | 8  | 13? | ?  | N | 4

**OCR validation anchor (cells I am sure of):** longitude-degree column = [11,11,13,11,6,7,8];
direction column = all ش (N). When the classifier is trained, segment this column and check it
predicts those values on the real 1899 print (the true test of synthetic→print transfer).

## Cetus (Qīṭus), p20 bottom — direction all ج (S); longitudes 28,28,28,21,21,13 (within-sign?).
Already in star_catalogue.csv (flagged). Same convention question applies.

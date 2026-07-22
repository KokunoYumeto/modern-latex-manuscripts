# SGA 3 English Loop 1 — through Exposé II

This immutable bounded checkpoint contains the Editorial Notice, Introduction,
all of Exposé I, and all of Exposé II through its bibliography. The continuation
cursor is Exposé III, component-local page 1 / combined-reader page 111. This is
not a complete SGA 3 translation.

The controlling source is the 1,366-page Polo--Gille current complete reader,
SHA-256 `B0984B5BF322A88AB455709578E4E41EB43D6E1C91931282CFEE64F2C1F69BE2`.
OCR was used only as locator/drafting witness. Jacob C. Reinhold's
`jcreinhold/sga` lineage `e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e` was used
and credited as English comparison/drafting material; its author declares CC BY
4.0 for his translation contribution. It is not source authority or independent
mathematical corroboration. Underlying French rights and attribution remain
separate caveats.

The reader PDF has 117 A4 pages. It was produced by a two-pass `latexmk` build.
The build has no errors or overfull boxes and two harmless underfull-box
diagnostics inherited from the continuous reader. Fifteen pages spanning the
component joins and Exposé II ending were rendered and visually checked in
`../../qa/master_expose_II_checkpoint_20260722`.

Primary frozen identities:

- `SGA3_English_through_Expose_II.tex`: 4,455 bytes; SHA-256
  `76C94B53C7E7FAF6A1D4C75263B8ED26A16CDD1576C39E356B3B8BBC439A0AEF`.
- `build/SGA3_English_through_Expose_II.pdf`: 1,850,991 bytes; SHA-256
  `27D7AAAB91BE2FFA343FE1DC3D6A84A8F14789F10430E9399CB8C3F7CF721908`.
- `build/SGA3_English_through_Expose_II.log`: 60,319 bytes; SHA-256
  `F08D1DC1A02019B6ECDC756F335351EDFA0BE047BF951CEDD1FA10C13E8DDEFB`.

The wrapper depends on `tex/sga3_loop1_macros.tex`, numbered components 00--14,
and the Exposé I/II PNG diagrams under `figures/exp1` and `figures/exp2` in the
working root. `SHA256SUMS.csv` binds the complete checkpoint dependency and QA
closure.

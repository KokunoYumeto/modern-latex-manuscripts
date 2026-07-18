# Source check

## Authority and extent

- Sealed German authority: `cum_de_Local_20260718_P31.tex`, SHA-256 `A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F`.
- Complete Paper 27 extent: cumulative lines 14192-14200, from the section heading through the following `\clearpage`; Paper 28 begins at line 14201.
- Journal extent: `J. Ber. d. DMV 34 (1925), S. 101`.
- The later compiled working candidate has SHA-256 `C243961810AD2EE10E866007620BBCDAFE2EF5305A1CAD040B5EA7E6ADDC2C39`. Direct extraction found its Paper 27 span byte-for-byte identical to the sealed head; it was not promoted to sealed authority.
- The standalone German control expands only cumulative macros and preserves the complete notice.

The shared project pointer at `03_projects/noether/00_current_german_authority` remains stale at R821. It was not used as current authority; the pending pointer refresh is recorded under `CJK-D012`.

## Printed-source check

The full-resolution GDZ image `P27_GDZ_printed101_canvas000358_full.jpg`, SHA-256 `B00824115997D651F5EAB48420D05E6E0E6D7DF0AAC2CCD69E0836B033BFD8EC`, was inspected at original resolution. The German TeX agrees with the printed page on:

- paper number, title, citation, leading dash, author attribution, and complete one-page extent;
- the quoted `charakteristischen Funktion` label and the Hilbert/Macaulay/Ostrowski sequence;
- primary ideal `q`, associated prime ideal `p`, and the residue-field reference;
- `q, q/p, q/p^2, ...` and the composition-series interval from `q/p^i` to `q/p^{i-1}`;
- the finite-order example and the final equivalence claim.

OCR and inherited translations were not used as source authority.

## Korean fidelity check

An independent internal Korean read-through compared the complete Korean TeX with the German control. It found one substantive issue in the draft: `das Äquivalent für` had been weakened to a generic “corresponding object.” The accepted text now reads `표현에 상응하는 대체물을 이룬다`, preserving the source's equivalent/substitute relation. No other substantive fidelity defect was found.

Formula identifiers, exponent indices, sequence order, proper names, and bibliographic apparatus are retained. Held Korean terms keep visible German or English controls where needed.

## Result and limit

Source check: **pass for internal production and handoff**. This is an internal source/fidelity finding, not external Korean domain certification.

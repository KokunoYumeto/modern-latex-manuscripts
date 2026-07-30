# Noether Paper 4 Sections 4-5 source adjudication and QA

## Result

The independent print-versus-R823 collation found four editorial deltas and one genuine downstream formula regression.

The four editorial deltas remain unchanged in the reader bodies:

1. Printed p. 132 repeats `tau >= sigma` in cases 3 and 4. R823 uses `tau > sigma` in case 3 and `tau >= sigma` in case 4, making the partition disjoint.
2. Printed p. 135 equation (35) uses `alpha`, no terminal `-lambda`, and `alpha`; R823 uses a coordinated `lambda`, terminal `-lambda`, and `lambda` emendation.
3. Printed p. 137 says `Defekt alpha`; R823 says `Defekt rho`, coherently with relation (38)'s exponent and range.
4. Printed p. 137 uses an identity/congruence sign in the linear-form condition; R823 uses ordinary equality.

The real target-lineage regression was inside the retained R823 form of equation (35): all four active bodies had lost the subscript on `rho_1`, producing

```tex
R_{\rho+\sigma_1-\alpha-\lambda}
```

instead of R823's

```tex
R_{\rho_1+\sigma_1-\alpha-\lambda}.
```

That unsupported `rho_1` to `rho` change is now repaired in Latin Interslavic, Cyrillic Interslavic, Russian, and Ukrainian.

## Evidence opened directly

- Original Paper 4 PDF SHA-256: `D7F7CE6D4B311FFD968ED47DC9C1478CFFCF9F446A86BF90263E0C9D1B41C9EF`.
- R823 TeX SHA-256: `EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21`.
- Printed p. 132 600-dpi case crop SHA-256: `7360CE6F2A331E7AD5A8C157658757BF69A360A4397ABE855BEE4A59E72A0C3F`.
- Printed p. 135 equation-(35) crop SHA-256: `661A6006C42E6D3035D228A0492E0E7A0FA6F3AD54ED4D0B8FD798C5CD7AA3A8`.
- Printed p. 137 focused crop SHA-256: `46271D1E96FA96A71B3CF1425441FBD724F2DE03C8C1C6FDED0DB3F4925506D7`.

The canonical equation-(35) alert is the expanded 4,668-byte receipt with SHA-256 `575858ED2D73BD9AC5D97A923B8200CF8014C26E357E56AD3440747D1E6BA0B5`. Its earlier hash `B577CE71E0D03E44CE6132E17FBF89E7845D73BF4BF330F3D592A62ADCBE2F92` is superseded and must not be used as the live receipt.

## Build and render QA

All four repaired Section 5 units compiled twice with XeLaTeX. They produced nine pages total: two Latin Interslavic, two Cyrillic Interslavic, three Russian, and two Ukrainian.

The compile scan found zero fatal errors, undefined controls, rerun warnings, or overfull boxes. It retained 16 underfull-box notices across three outputs; visual review found no clipping, overlap, missing glyph, blank page, or broken formula.

All nine rendered pages were inspected. Equation (35), including `rho_1`, was inspected in every language at full page scale and in a four-language focused contact sheet (SHA-256 `CCE1FDED343898BE9CA17CC333163326899A27E17231735B6492260DED984566`).

## Authority limit

This checkpoint repairs one four-language formula family and records four no-change print-to-R823 editorial deltas. It does not certify all of Sections 4-5 or adjudicate the mathematical rationale of every historical editorial emendation.

# Exposé XXIII native-diagram lead review — 5000 dpi

Date: 2026-07-28

## Scope

The complete Exposé XXIII TeX closure contains exactly one diagram:
the rank-one commutative square in §4.1.2, implemented natively in
`tex/components/09_expose_XXIII_fundamental_theorem.tex`. It contains
no raster inclusion and the complete TeX tree contains zero
`\includegraphics` calls.

Authority: `Exp23-13oct24.pdf`, physical page 26, 332,989 bytes,
SHA-256
`8C3F94D256B151C68EA8765EEC13812FE079E90B3A18C649B939B023E77DA12F`.

Delivered reader: `build/SGA3_Expose_XXIII_English.pdf`, physical page
27, 220,261 bytes, SHA-256
`22EB1CD2B5133D2E7567CAE086AFE920EA90AEA4FF17E4C07BC5BA5E42DBF7D5`.

The 600-dpi full-page renders were used only to locate the diagram
crop. They are legitimate context evidence but do not carry the
diagram-fidelity decision.

## Adverse first comparison

Direct 5000-dpi comparison found four label-side discrepancies in the
first native version:

1. the left vertical `q(\alpha)` was on the left rather than the right;
2. the central vertical `f_T` was on the right rather than the left;
3. the lower-left horizontal `\alpha'^*` was below rather than above;
4. the lower-right horizontal `\alpha'` was below rather than above.

The first delivered-detail evidence is
`page27_rank1_square_5000dpi.png`, 1,284,304 bytes, SHA-256
`C6B8CEA88D4FF248F6DE32E35E715BB2F099AD9CF847C9E570BF29860F75635E`.
It is preserved as adverse history.

## Repair and final comparison

The four placement controls were corrected in the native `tikzcd`
source without changing the objects, arrows, directions, or
mathematical labels. The corrected component is 11,703 bytes, SHA-256
`869F9CFAC409FC4F81DBC921DC5A94A3410E2BAF15904CB152866BE5E403096E`.

Authority 5000-dpi detail:
`authority_page26_rank1_square_5000dpi.png`, 2,002,230 bytes,
SHA-256
`9A727734B97B0FDD4519AC6086FBEC7806FC2E85D7884B6FE525AFD430290907`.

Corrected delivered 5000-dpi detail:
`page27_rank1_square_5000dpi_r2.png`, 1,258,753 bytes, SHA-256
`D686FF1C919CB493EE7F07AD6568F5AFA9AD072BE4DCF959163C260D14561CCF`.

Lead manual comparison PASS:

- all six objects match;
- all six arrows match in incidence and direction;
- all six arrow labels match;
- all label sides match the authority;
- no hook, tail, crossing, curvature, prime, star, subscript, or
  attachment-point ambiguity remains.

No agent or delegated reviewer made this visual judgment. The
top-level session lead inspected both 5000-dpi details directly.

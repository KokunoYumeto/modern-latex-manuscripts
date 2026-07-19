# Independent review

Final disposition: PASS after two target-only QA repairs; zero remaining
blockers.

The direct source review checked corrected French lines 2796--2805 and the
same-edition physical source-PDF page 82. The implication `(d) => (b)`, the
definition of `D(Z_q)`, the nonmembership `q+i`, corrected Proposition
VII.2.3, corrected calligraphic-F branch, outer Ext supports and degrees, inner
degrees, `E_2^{p,q}`, `p+q=i`, the `H_Y^*` abutment, and the conclusion all
pass. Calligraphic sheaf Ext is the established English typographic
normalization of the source's underlined Ext; no semantic object, support,
degree, or argument changed.

The literal source statement that only finitely many integer pairs satisfy
`p+q=i` omits the restriction to terms that can contribute. The target keeps
the source body literal and adds a visible `[S]` note. The stated interpretation
is supported by the finite-projective-dimension setup at French line 2733,
which bounds nonzero inner Ext degrees. The French authority is unchanged.

Page and boundary review passes: original printed page 93, physical source-PDF
page 82, recomposed running page 74; printed marker 93 precedes the unit at
line 2782 and marker 94 follows at line 2813. Blank line 2806 is excluded and
French line 2807 is the exact next substantive cursor. The jcreinhold
`e7a259f` witness remains comparison-only; its bullet abutment and genericized
notation are rejected.

The first independent visual pass caught an unwanted gap in the source-note
compound. The searchable-text gate then caught two U+0001 bytes created by
parenthesis-sizing commands. Both target-only defects were repaired without
changing mathematics. The final identities are:

- TeX: 2,329 bytes, SHA-256
  `4F339AD2E60C1620EB7F773B30025A1F2BA676EC80F8D46EB6FC03B7E64D44EE`.
- target PDF: 272,771 bytes, one A4 page, SHA-256
  `78E0B96D6A1EC4D1CC778155370BF8D6A4A2FB048F25D017F9CF5072023AAAC9`.
- extracted text: 1,863 bytes, SHA-256
  `0C127459BB45CDD2453B39C1BCE42D291CF38390CB1454CB203C98D6C6849ECA`.
- 300-dpi render: 321,927 bytes, SHA-256
  `EAF736E265E58AE5F077F375B659088B3B0C0CAAD1C94AD1C117FD128E38BA56`.

The fresh isolated PDF is 272,771 bytes with SHA-256
`0352A5749D260E7FDB038D6B95EEAF19B807710BDD78343B45B6F764916D75E7`.
Its extracted text and 300-dpi render are byte-identical to the target. Its
second pass has zero real warning, error, box, undefined-control, missing-glyph,
or fatal diagnostics; the first pass has only the expected rerun request.

This review seals the bounded unit only. It does not claim a complete Exposé
VIII, complete SGA2 volume, critical edition, publication, archive acceptance,
or remote readback.

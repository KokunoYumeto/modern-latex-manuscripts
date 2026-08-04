# Noether Paper 6 Korean producer status — T03 / §2

Current state: **complete producer-draft coverage of §2 in eight editable units; every T03 target remains UNCHECKED and unbuilt**.

- Source coverage: ED0001 lines 4692--4798; 5,856 LF bytes / SHA-256 `27A1D4E81287A3F2D4C4276CB3A1909611EDE4B1BB5A47F52F9F86E6DB27B681`.
- Target coverage: T03-U15--U22, eight files / 12,698 bytes. Together with T01 and T02, Paper 6 currently has twenty-two producer targets / 41,488 bytes through §2.
- Binding: `NOETH-DE-AUTH-v007-20260804`; 21,580 bytes / SHA-256 `A6A8FC8E5AC24ACAF49DFD55B4B58FA3DA882EF8C3FDD4D136220C8751045156`; ED0001 remains 2,153,565 raw bytes / `D1F06B311F6CBD991DD247D745DD9A72DDE326A20396DF43CFE0C8EDB1593CDB`.
- Cross-unit topology: U21 opens the `\srcfn{**)}{...` source footnote and U22 continues and closes it. They must remain ordered U21→U22 with no inserted prose.
- Next substantive cursor: line 4799, the §3 heading. It is outside T03.
- Language posture: provisional Hangul-first ko-KR producer prose. The Hanja disambiguator `階數` is unverified; no ko-KP evidence or localization exists, so ko-KP remains `unverified_do_not_claim`.
- Review state: no source/scan comparison; no independent Korean clause, lemma, proof, footnote, formula, notation, or terminology check; no Hanja or regional review; no independent human validation.
- Build state: not compiled, extracted, rendered, visually inspected, assembled, packaged, certified, approved, or published. Zero render or visual-inspection calls were made for T03.
- Authority state: no German defect is claimed and no German source or canon file was changed.

## Open holds

- The distinction between `Unbestimmte` as algebraic indeterminates (`미정원`) and `unbestimmt` as an indeterminate value or quotient (`부정형`, especially `0/0`) remains an explicit sense-window hold.
- `algebraischer Rang` and `Rang der Funktionalmatrix` are provisionally rendered with `계수(階數)`. The checker must prevent confusion with coefficient `계수` and consider `랭크` or another Korean mathematical term.
- `Spezialisierung`, `Substitution`, `sukzessiv`, and `Rang erhalten` are provisionally differentiated as `특수화`, `대입`, `잇따른/순차적`, and rank preservation; their historical and mathematical scopes remain unchecked.
- `teilbar/Teilbarkeit`, `gemeinsamer Nenner`, `irreduzible Gleichung`, `reduzierte Darstellung`, `teilerfremd`, `homogene Formen`, numerator/denominator language, and the 0/0 conclusion remain terminology holds.
- Every Jacobian-style derivative, exponent, index, equation number (1)--(6), divisibility claim, quotient colon, specialization bracket, and nonvanishing condition remains a formula/notation hold.
- The long source footnote in U19 and the cross-unit source footnote spanning U21→U22 remain unchecked in scope, wording, example, delimiters, and mathematical content.

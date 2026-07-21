# Source comparison: SGA2-X-COROLLARY2.4-PROOF

This bounded source-aligned producer unit is not an independent seal,
publication payload, archive handoff, or volume-completion claim.

## Authority and boundary

- Authority: corrected French arXiv TeX `smf_doc-math_4_01.tex`, 586,789
  bytes, SHA-256
  `C2F899E92A904E312B550C6452A117FF23D30AF984B2254A0961D2DF0DACD042`.
- Scope: French lines 3433--3437 inclusive, the complete proof of Corollary
  2.4. Blank 3438 is excluded; raw cursor 3438 and next substantive cursor
  3439 (Corollary 2.5).
- Source coordinates: original printed pp. 116--117, physical source-PDF
  p. 101, and recomposed running p. 93. The `\pageoriginale` marker within
  line 3433 occurs after “two” in “two nonzero rings” and advances the
  original printed page. The three locator systems are not conflated.
- LF/no-terminal-EOL slice: 299 bytes, SHA-256
  `F069959778F912FF793B77E65E76C8FD441EB8159CB460FC55950D2378C81951`.
- Retained terminal-LF slice: 300 bytes, SHA-256
  `3DB457DA2960EE068953F0B48D0CFA89DA0385EFE2B3321D1D62E5F13C5C107C`.
- CRLF/terminal-EOL slice: 305 bytes, SHA-256
  `0C239C0470067CE27DE15EE0A51088BAAF617B870D0A0624A9BDBF3E7FB1ABB5`.
- Same-edition physical-p. 101 render: 407,075 bytes, SHA-256
  `E59A5DADE48D40EA47B11A4747A72A21ABA090FA09F697F403FC5B4ACD0FB793`.

The five retained lines replay exactly against the authority. The PDF/render
is same-edition manifestation, formula, and layout evidence only, not
independent original-print corroboration. No source defect or unresolved
mathematical ambiguity was found, and French remains byte-identical.

## Translation and mathematical comparison

The target preserves the connectivity criterion for a locally ringed space:
`(X,O_X)` is connected if and only if `Gamma(X,O_X)` is not a direct product
of two nonzero rings. “Direct product” is used because the objects are rings;
“direct sum” was rejected.

The displayed isomorphism preserves both global-section domains, direct
images, hats, and subscripts:

`Gamma(U,r_*O_R) ~= Gamma(hat X,hat r_*O_hatR)`.

The attribution to `Lef(X,Y)` remains part of the proof. The source-page
transition is ledgered but does not interrupt or alter the English sentence.

## External comparison candidate

The current jcreinhold chapter
`ii/10-application-to-the-fundamental-group.md` is 31,425 bytes, SHA-256
`2BDDBC3D15EECE7A47FDBDFBE31DAE735446BC14480A75113E704F63901C7BF5`.
It is comparison-only, not authority or independent corroboration. Its
connectivity wording was useful as a register check, but the target and every
formula were derived from and replayed against the French authority.

## Build and rendered QA

Two pdfLaTeX passes completed. Pass 1 contains only the expected
`rerunfilecheck` request; pass 2 has zero matched LaTeX/package warnings,
overfull or underfull boxes, undefined controls, emergency stops, or fatal
errors. The target is one A4 page. All 13 font rows are embedded, subsetted,
and Unicode-mapped.

Original-detail inspection of the 150-dpi target and 200-dpi source renders
passes. The authority/page-marker note, connectivity criterion, both global
sections, all hats/subscripts, `Lef`, margins, and page number are legible;
there is no clipping, overlap, broken glyph, black box, or missing text.

- Target TeX: 1,696 bytes, SHA-256
  `8F867DE410B58747B336FD61EF9050DE2BB464DCE324FF8A001513B8E19BC052`.
- Target PDF: 199,476 bytes, SHA-256
  `963DDF70C59130B99D1C37BC0333AE8B87682A650796A8F43B8EB5992C2AC8EF`.
- Pass-1 log: 7,416 bytes, SHA-256
  `542FA7E274771E18449684F7881D62B34C3A3608696E9974843A56CE68E015AB`.
- Pass-2 log: 7,292 bytes, SHA-256
  `DCDC66181E79DB7B099C261842CB8D599F1406194D5654FF2FD37F40DBDF23D7`.
- Final engine log: 24,655 bytes, SHA-256
  `C9899FD2E4C0E46039ED324E6D7435C536DCDEECDB38642353FE4DA32EDF9B90`.
- Target render: 103,512 bytes, SHA-256
  `F952BFBC4E525F7BD478CECF42C5C269F55C694C04F8B278B87964FA469B88E2`.

The package remains `internal_not_for_release` until machine validation and
fresh independent review pass. Path-bearing logs must be sanitized or
excluded from any public payload. Continue at raw 3438 / substantive 3439.

# Source comparison: SGA2-X-COROLLARY2.5-STATEMENT

This is a bounded source-aligned producer unit. It is not an independent
seal, publication payload, archive handoff, or volume-completion claim.

## Authority and boundary

- Authority: corrected French arXiv TeX `smf_doc-math_4_01.tex`, 586,789
  bytes, SHA-256
  `C2F899E92A904E312B550C6452A117FF23D30AF984B2254A0961D2DF0DACD042`.
- Scope: French lines 3439--3444 inclusive, the complete statement of
  Corollary 2.5. Blank line 3445 is excluded; raw cursor 3445 and next
  substantive cursor 3446 (the counter and label for Corollary 2.6).
- Source coordinates: original printed p. 117, physical source-PDF p. 101,
  and recomposed running p. 93. These systems are not conflated, and no
  `\pageoriginale` marker occurs within the slice.
- LF/no-terminal-EOL slice: 332 bytes, SHA-256
  `98E3268632859DF9C0579B59A45A27DD8107764DEC31A5D80EB5A95E43D2C4A5`.
- Retained terminal-LF slice: 333 bytes, SHA-256
  `92F6573CE4524B6839658A73C9621D897422B8354F1577097179851E4B0EA86D`.
- CRLF/terminal-EOL slice: 339 bytes, SHA-256
  `21D285EEF73BF9F2C198E474D97267D41271214BC7049D550689C0F0B8FBC9F9`.
- Same-edition physical-p. 101 render: 407,075 bytes, SHA-256
  `E59A5DADE48D40EA47B11A4747A72A21ABA090FA09F697F403FC5B4ACD0FB793`.

The six retained lines replay exactly against authority lines 3439--3444.
The PDF/render establishes same-edition manifestation, formula, and layout
only; it is not independent original-print corroboration. No source defect or
unresolved mathematical ambiguity was found, and the French authority
remains byte-identical.

## Translation and mathematical comparison

The first sentence preserves the hypothesis `Lef(X,Y)`, universal
quantification over `U`, the direction and endpoints of the functor

`Et(U) -> Et(Y)`,

and its full faithfulness. Because Expose X fixes `U` as a variable open
neighborhood of `Y`, the bounded English target makes that standing convention
explicit as “for every open neighborhood U of Y.” This supplies no new
hypothesis.

The second sentence preserves the separate `Leff(X,Y)` hypothesis, the
universal etale covering `R` of `Y`, existential `U` and `R'`, the fiber
product base, and the isomorphism

`R' times_U Y ~= R`.

The French says `revetement etale R` but only `revetement R'` in the
conclusion. The target therefore says “etale covering R” and “a covering R'”
rather than silently inserting a second “etale.” This is a recorded literal
source distinction, not a proposed defect or an English mathematical
correction. The bold category symbol, primes, subscripts, arrow, fiber product,
and isomorphism were checked directly against both the TeX and page image.

The shared register “open neighborhood,” “covering,” “etale covering,” “fully
faithful,” and “isomorphism” is retained. Replacing “fully faithful” with
“one-to-one,” flattening the category notation, reversing the functor, adding
the omitted adjective to `R'`, and conflating the three page systems were
rejected.

## External comparison candidate

The current jcreinhold chapter
`ii/10-application-to-the-fundamental-group.md` is 31,425 bytes, SHA-256
`2BDDBC3D15EECE7A47FDBDFBE31DAE735446BC14480A75113E704F63901C7BF5`.
Its corresponding material is at lines 249--254. It is one LLM-generated
comparison lineage, not authority or independent corroboration. It usefully
confirms ordinary English register and likewise does not add “etale” before
`R'`; however, its source-derived wording was not reused without direct French
and formula replay.

## Build and rendered QA

Two pdfLaTeX passes completed. Pass 1 contains only the expected
`rerunfilecheck` request; pass 2 has zero matched LaTeX/package warnings,
overfull or underfull boxes, undefined controls, emergency stops, or fatal
errors. The target is one A4 page. All 12 font rows are embedded, subsetted,
and Unicode-mapped.

The 150-dpi target and 200-dpi source renders were inspected at original
detail. The authority box, corollary label, bold `Et`, arrow, both hypotheses,
prime, fiber product, isomorphism, margins, and page number are legible. There
is no clipping, overlap, broken glyph, black box, or missing text.

- Target TeX: 1,701 bytes, SHA-256
  `62855478F9EFA28BA875AE3A15BFF72D3572575249458DE90680A47B30AD92BD`.
- Target PDF: 196,847 bytes, SHA-256
  `135EDC77C71D6B2FD0D375B62268CCC8CEEBD870BA9C0CCAD29D7F73E31C20E3`.
- Pass-1 log: 7,206 bytes, SHA-256
  `68A79032BBD65D8CC14574DF63F12A0439B0CC660348491E84011F5ADBF1671F`.
- Pass-2 log: 7,086 bytes, SHA-256
  `52D0E050A7E74524A0FD45674EAE13DE6056051A2D0928FF4C0ABF2E886E6537`.
- Final engine log: 24,083 bytes, SHA-256
  `E637D901F2E31500A05FE57FA3F05C6AFE71782101D858151706F912B855841C`.
- Target render: 107,275 bytes, SHA-256
  `345A0FB54EF9FF36FA17849308C2A18DBED6198FA62FABE549287C6748C39F98`.

The package remains `internal_not_for_release` until machine validation and
fresh independent review pass. The build logs and final engine log contain
local runtime paths and must be sanitized or excluded from any public payload.
Continue at raw line 3445 / substantive line 3446.

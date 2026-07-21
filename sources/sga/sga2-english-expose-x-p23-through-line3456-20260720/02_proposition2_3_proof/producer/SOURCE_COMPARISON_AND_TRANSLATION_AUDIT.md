# Source comparison: SGA2-X-PROPOSITION2.3-PROOF

This is a bounded source-aligned producer unit. It is not an independent
seal, publication payload, archive handoff, or volume-completion claim.

## Authority and boundary

- Authority: corrected French arXiv TeX `smf_doc-math_4_01.tex`, 586,789
  bytes, SHA-256
  `C2F899E92A904E312B550C6452A117FF23D30AF984B2254A0961D2DF0DACD042`.
- Scope: French lines 3425--3427 inclusive, the complete proof of
  Proposition 2.3. Blank line 3428 is excluded. The raw cursor is 3428 and
  the next substantive cursor is 3429 (Corollary 2.4).
- Source coordinates: original printed p. 116, physical source-PDF p. 101,
  and recomposed running p. 93. These systems are not conflated. There is no
  `\pageoriginale` marker within the slice.
- LF/no-terminal-EOL slice: 424 bytes, SHA-256
  `0D5F4B5B729F784BCF1FB82FF53403E5B99178A20D0016963EA3FA2F2052D4F2`.
- Retained terminal-LF slice: 425 bytes, SHA-256
  `B12225CCCA08AD2432F5AF9C6330ABC31EDA8E1378FA96F3CECD8E2F91DE4231`.
- CRLF/terminal-EOL slice: 428 bytes, SHA-256
  `517C9A74985CA1C1505BD9F516CC849C2CE012646EE04F34971BAAB73EEBF71A`.
- Same-edition reader: 1,576,954 bytes, SHA-256
  `41AD02C57321A8D2200FF32A929BC93ADBC3DE0D59DCD5A284D28D859FB87A90`.
- Physical-p. 101 render: 407,075 bytes, SHA-256
  `E59A5DADE48D40EA47B11A4747A72A21ABA090FA09F697F403FC5B4ACD0FB793`.

The three retained source lines replay exactly against authority lines
3425--3427. The reader/render establishes same-edition manifestation,
formula, and layout only; it is not independent original-print
corroboration. No source defect or unresolved mathematical ambiguity was
found in this bounded proof, and the French authority was not changed.

## Translation and mathematical comparison

The target preserves the two proof parts and the dependency of item (ii) on
item (i) plus the `Leff` hypothesis. It retains the qualification “at least
for `L_U` and `P_U`,” which is essential because the rest of the proof treats
the etale case separately.

For an etale covering `R` of `hat X`, the target preserves:

1. an open neighborhood `U` of `Y` in `X`;
2. a finite flat covering `R'` of `U`;
3. the isomorphism `widehat(R') ~= R`;
4. the induced covering `R''` of `Y`;
5. its etaleness by Proposition 1.1; and
6. etaleness of the restriction of `R'` over some neighborhood `U'` of `Y`.

The final wording “the restriction of `R'` to some neighborhood `U'`” makes
explicit the source phrase that `R'` is etale in a neighborhood; it does not
alter the covering or the conclusion. “Part (i) has already been proved” is
the natural target rendering of the terse source `A ete vu`. The hats,
single/double primes, neighborhood variables, reference, and QED are all
preserved.

## External comparison candidate

The current jcreinhold chapter
`ii/10-application-to-the-fundamental-group.md` is 31,425 bytes, SHA-256
`2BDDBC3D15EECE7A47FDBDFBE31DAE735446BC14480A75113E704F63901C7BF5`.
It is one LLM-generated comparison lineage, not authority or independent
corroboration. Its proof is useful as a terminology check but retains the
literal “(i) Has been seen” and code-formats functor names. Those register
choices were rejected. The target was translated from the French authority
and checked against the same-edition page.

## Build and rendered QA

Two pdfLaTeX passes completed. Pass 1 contains only the expected
`rerunfilecheck` request; pass 2 has zero matched LaTeX/package warnings,
overfull or underfull boxes, undefined controls, emergency stops, or fatal
errors. The target is one A4 page. All 12 font rows are embedded, subsetted,
and Unicode-mapped.

The 150-dpi target render and 200-dpi source render were inspected at
original detail. The authority box, two proof parts, `L_U`/`P_U`, all hats
and primes, displayed isomorphism, Proposition 1.1 reference, QED square,
margins, and page number are legible. There is no clipping, overlap, broken
glyph, black box, or missing text.

- Target TeX: 1,680 bytes, SHA-256
  `96BFF50B8D9C982805A19F68766C1B23D0FCFB52AC7B0AD4D33C5770091BA004`.
- Target PDF: 184,261 bytes, SHA-256
  `F31CC1743790BA1115F9E964149EDE9D555E0BE1A233ADDEB4FC250B39F416A7`.
- Pass-1 log: 7,377 bytes, SHA-256
  `2E8AE016D0671DAEF0721CDAE1534F255E74EFB5EA1BD87DA9BD5B7F297BEFFB`.
- Pass-2 log: 7,257 bytes, SHA-256
  `C15E3AC3E6A91DB2A52C76D755588CC8541D0BADF41BDC339EE1211EAD54C7B2`.
- Final engine log: 24,412 bytes, SHA-256
  `D608522A6FC569B385836066A32500D0D0D5B406783F0A3F88F8055B4F6AD679`.
- Target render: 110,804 bytes, SHA-256
  `8ED65FBBD171532289F552F6B9CFC0F1CFA3DC733D6A4B885C4EBAAA5CCB562B`.

The package remains `internal_not_for_release` until machine validation and
fresh independent review pass. Build logs contain local TeX runtime paths
and must be sanitized or excluded from any public payload. Continue at raw
line 3428 / substantive line 3429.

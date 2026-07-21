# Independent final audit: SGA2-X-PROPOSITION2.3-PROOF

## Decision

**PASS for the bounded English target; internal evidence only.** The proof of
Proposition 2.3 is source-aligned, mathematically faithful, independently
build-reproducible, render-clean, and supported by valid machine evidence.
No producer file was changed. This review is not a publication payload,
archive handoff, French-source patch, or completion claim for Expose X or
SGA 2. The continuation boundary remains raw French line 3428 (the excluded
blank line) and substantive line 3429 (Corollary 2.4).

## Authority replay and source coordinates

The admitted corrected French TeX is 586,789 bytes, SHA-256
`C2F899E92A904E312B550C6452A117FF23D30AF984B2254A0961D2DF0DACD042`.
I independently re-extracted lines 3425--3427 with LF separators and one
terminal LF. The result is exactly 3 lines / 425 bytes / SHA-256
`B12225CCCA08AD2432F5AF9C6330ABC31EDA8E1378FA96F3CECD8E2F91DE4231`
and is byte-identical to `SOURCE_LINES_3425_3427.tex`. Line 3428 is blank;
line 3429 is `\begin{corollaire} \label{X.2.4}`.

The locator systems remain distinct: original printed p. 116, physical
same-edition reader p. 101, and recomposed running p. 93. The reader is
1,576,954 bytes, SHA-256
`41AD02C57321A8D2200FF32A929BC93ADBC3DE0D59DCD5A284D28D859FB87A90`.
An independent 200-dpi render of physical p. 101 is 407,075 bytes, SHA-256
`E59A5DADE48D40EA47B11A4747A72A21ABA090FA09F697F403FC5B4ACD0FB793`,
byte-identical to the producer source render. It visibly contains the entire
proof before Corollary 2.4. This is same-edition manifestation and layout
evidence only, not independent original-print corroboration.

No source defect or unresolved mathematical ambiguity was found in this
bounded proof, and the French authority remains byte-identical.

## Translation, formulas, and proof logic

The target preserves both proof parts. “Part (i) has already been proved” is
a natural formal rendering of the terse `A ete vu`; it neither adds a proof
nor changes the disposition.

Part (ii) retains the exact dependency on part (i) and the hypothesis, plus
the essential qualification “at least for $L_U$ and $P_U$.” The separate
etale case preserves the full chain:

1. an etale covering `R` of `hat X`;
2. an open neighborhood `U` of `Y` in `X`;
3. a finite flat covering `R'` of `U`;
4. the completion isomorphism `widehat(R') ~= R`;
5. the induced covering `R''` of `Y`;
6. etaleness of `R''` by X.1.1, rendered as Proposition 1.1; and
7. etaleness of the restriction of `R'` over a neighborhood `U'` of `Y`.

The wording “By restriction” and “the restriction of `R'` to some
neighborhood `U'`” makes explicit the source's induced-covering and
near-`Y` statements without changing an object, hypothesis, or conclusion.
All hats, single and double primes, covering types, neighborhood variables,
reference, and QED are present and correctly attached.

The current jcreinhold chapter independently re-hashes at 31,425 bytes,
SHA-256
`2BDDBC3D15EECE7A47FDBDFBE31DAE735446BC14480A75113E704F63901C7BF5`.
Its lines 221--226 are broadly aligned but use “Has been seen,” code-formatted
functor names, and an awkward hat/prime rendering. Those choices were
correctly rejected. This file remains one comparison-only LLM lineage, not
authority or independent corroboration.

## Independent build, PDF, fonts, text, and render

The copied review TeX is byte-identical to the producer target: 1,680 bytes,
SHA-256
`96BFF50B8D9C982805A19F68766C1B23D0FCFB52AC7B0AD4D33C5770091BA004`.
Two fresh pdfLaTeX passes exited zero. Pass 1 contains only the expected
`rerunfilecheck` request; pass 2 and the final engine log contain zero matched
LaTeX/package warnings, box diagnostics, undefined controls, emergency stops,
or fatal errors.

The independent PDF is one A4 page, 184,261 bytes, SHA-256
`25B5459673581A8A2743F6CA7C75289E18765E89BC2CED49787915DA9BB4F135`.
It differs from the producer PDF SHA-256
`F31CC1743790BA1115F9E964149EDE9D555E0BE1A233ADDEB4FC250B39F416A7`
because of rebuild metadata and job name. Its 150-dpi render is byte-identical
to the producer render: 110,804 bytes, SHA-256
`8ED65FBBD171532289F552F6B9CFC0F1CFA3DC733D6A4B885C4EBAAA5CCB562B`.
Its layout-preserving extracted text is also byte-identical to the producer
extraction: 1,520 bytes, SHA-256
`445860333DDFE95DF506F1D429773C97F0FEB8FBD1C4CC65958EB1D024C5DF59`.

All 12 font rows are embedded, subsetted, and Unicode-mapped. Original-detail
inspection of the independent target and source renders found both proof
parts, `L_U`/`P_U`, `R`/`R'`/`R''`, both hats, `U`/`U'`, the displayed
isomorphism, Proposition 1.1, and the QED square legible. There is no clipping,
overlap, broken glyph, black box, or missing content.

## Producer and independent machine evidence

The producer CSV independently validates at 8 data rows x 22 columns, 9 CRLF
line endings, zero bare LF, unique nonempty stable IDs, zero formula triggers,
and zero parent/revision/supersession-reference errors. Its SHA-256 is
`814ECF4AC513A61565A0331A5283D6D49F84C4D576C49C622A7D06C5FBBD92D1`.
The producer JSONL validates at 8 records with zero parse, duplicate-key,
duplicate-ID, hierarchy, or revision-reference errors; SHA-256
`BAE2151D3326FF06E80133CBBCC675CB687BE346966BE64A18DAE0A82A57ED3B`.
The producer's 24-row ordinal manifest is rectangular and resolves all 24
listed paths, byte counts, and hashes exactly; SHA-256
`DEED6B14B367109FD86F69882C1FE32C0CF27A2E90585782F534DF034F72E750`.

Artifact Tool 2.8.24 independently imported the producer's full `A1:V9`
range. Its receipt is 1,365 bytes, SHA-256
`2905F8DFAACD21902F91262DD1D442D134E72E87B3D255FE05989E4026CC1AA5`.
The three producer panels cover columns A--V, have zero formula-error or
formula-trigger values, and were inspected at original detail.

This independent review adds an append-only 11-row x 22-column CSV, 7,215
bytes, SHA-256
`1D879DB3E2C2C979869D595957A7A7445C556F323ED3DA5A751EE61F73AE4B17`,
and a matching 11-record JSONL, 4,749 bytes, SHA-256
`8086C56AB67633EBCA5F4E61E6A7F2919ACE612C869FD0CC90EF4AF3487BBD57`.
Their IDs, local hierarchy, and status/cursor/source bindings close exactly.
Artifact Tool imported the full independent `A1:V12` range, found zero
formula errors or triggers, and rendered three panels covering all 22
columns. The receipt is 1,395 bytes, SHA-256
`6E0BB4BD3602C19A8DAB554C66587A8E6BEB169796552E0729DB52365C4CCF6B`;
all three panels were inspected at original detail and are legible.

The first independent validation receipt is preserved as
`INDEPENDENT_REVIEW_VALIDATION_PRELIM_FAIL.json`: 4,651 bytes, SHA-256
`60EA443E11185243336461BEE6FA1348C5BAA84C019638365FFF94FC75941698`.
It failed only because its target-fragment check treated a TeX source line
break between “of” and `$Y$` as a semantic mismatch. The validator successor
normalizes whitespace before exact fragment comparison. This correction did
not change authority, target, build, render, CSV, JSONL, or Artifact Tool
bytes; the final validation receipt passes with `errors: []`.

## Privacy and release gate

Exactly three producer files and three independent-review files contain
reconstructable local TeX runtime paths: each layer's two captured build-pass
logs and final engine log. These files must be sanitized or excluded from any
public successor. The raw producer/review tree therefore remains
`internal_not_for_release` despite the bounded substantive PASS.

## Final disposition

The bounded proof may be treated upstream as independently passed at raw
cursor 3428 / substantive cursor 3429. Public seal or archive work requires a
separate privacy-clean successor and an explicit handoff by the owning task.

# Source comparison: SGA2-X-PROPOSITION2.3-STATEMENT

This is a bounded source-aligned producer unit. It is not an independent
seal, publication payload, archive handoff, or volume-completion claim.

## Authority and boundary

- Authority: corrected French arXiv TeX `smf_doc-math_4_01.tex`, 586,789
  bytes, SHA-256
  `C2F899E92A904E312B550C6452A117FF23D30AF984B2254A0961D2DF0DACD042`.
- Scope: French lines 3414--3423 inclusive, the complete statement of
  Proposition 2.3. Blank line 3424 is excluded. The raw cursor is 3424 and
  the next substantive cursor is 3425 (the proof).
- Source coordinates: original printed p. 116, physical source-PDF
  pp. 100--101, and recomposed running pp. 92--93. These systems are not
  conflated. There is no `\pageoriginale` marker within the bounded slice.
- LF/no-terminal-EOL slice: 923 bytes, SHA-256
  `E90055324DCF97F5097850CD96834A0C699968C7FB11886EDA6F8E82DCE4EEC4`.
- Retained terminal-LF slice: 924 bytes, SHA-256
  `0ADFF5B4A4FDD17DFF772AAF4AFA55FDFE23BC061351A440BC54CAD0ACC43B72`.
- CRLF/terminal-EOL slice: 934 bytes, SHA-256
  `ED6F60A507CB1445992D507605F5E3BBD356B1A64777BDBF41963418D439BD20`.
- Same-edition reader: 1,576,954 bytes, SHA-256
  `41AD02C57321A8D2200FF32A929BC93ADBC3DE0D59DCD5A284D28D859FB87A90`.
- Physical-p. 100 render: 417,901 bytes, SHA-256
  `38A02FFE373296E96091781F960D76E5272C12D447C15F272A5DEEE2D02E572E`.
- Physical-p. 101 render: 407,075 bytes, SHA-256
  `E59A5DADE48D40EA47B11A4747A72A21ABA090FA09F697F403FC5B4ACD0FB793`.

The ten retained source lines replay exactly against authority lines
3414--3423. The reader and renders establish same-edition manifestation,
formula, and layout only; they are not independent original-print
corroboration. No source defect or unresolved mathematical ambiguity was
found in this bounded statement, and the French authority was not changed.

## Translation and mathematical comparison

The target preserves the locally noetherian prescheme `X`, the closed subset
`Y`, the formal completion `hat X` along `Y`, and the requirement that every
open `U` under discussion contain `Y`. It keeps the three functors distinct:

- `L_U` for locally free coherent `O_U`-modules;
- `P_U` for finite flat coverings of `U`;
- `E_U` for etale coverings of `U`.

The target renders `image inverse` as “pullback” and preserves the morphism
`hat X -> X`. Item (i) retains the `Lef(X,Y)` hypothesis and full faithfulness
of all three functors for every open neighborhood `U` of `Y`.

In item (ii), the source writes the module case and abbreviates both covering
cases with three occurrences of `resp ...`. The target does not invent a new
hypothesis or object. It gives the module formula
`L_U(E) ~= mathcal E` and then spells out that the analogous assertions hold
for finite flat and etale coverings with `P_U` and `E_U`, respectively. This
is an explicit English rendering of the source's parallel-case ellipses, not
a source emendation. The `Leff(X,Y)` hypothesis and existential dependence of
`U` on the object are preserved.

The shared register uses “locally noetherian prescheme,” “closed subset,”
“formal completion,” “locally free coherent module,” “finite flat covering,”
“etale covering,” “pullback,” and “fully faithful.” Symbols, hats,
subscripts, functor names, and the two Roman items were checked against both
authority and the same-edition pages.

## External comparison candidate

The current jcreinhold chapter
`ii/10-application-to-the-fundamental-group.md` is 31,425 bytes, SHA-256
`2BDDBC3D15EECE7A47FDBDFBE31DAE735446BC14480A75113E704F63901C7BF5`.
It is one LLM-generated comparison lineage, not authority or independent
corroboration. It supplies useful ordinary-English phrasing, but its Markdown
renders both Roman items as `1.`, uses “inverse image by,” and retains literal
ellipses without explaining the parallel cases. Those choices were rejected.
Its renaming of the formal object as `E` and the algebraized object as a
tilded `E` is mathematically possible but was rejected so the target remains
aligned with the French `mathcal E`/`E` roles. The accepted target was
translated from the French authority and checked against the reader.

## Build and rendered QA

Two pdfLaTeX passes completed. Pass 1 contains only the expected
`rerunfilecheck` request; pass 2 has zero matched LaTeX/package warnings,
overfull or underfull boxes, undefined controls, emergency stops, or fatal
errors. The target is one A4 page. All 11 font rows are embedded, subsetted,
and Unicode-mapped.

The 150-dpi target render and both 200-dpi source renders were inspected at
original detail. The authority box, proposition label, functor subscripts,
hats, `Lef`/`Leff`, displayed isomorphism, parallel-case sentence, margins,
and page number are legible. There is no clipping, overlap, broken glyph,
black box, or missing text.

- Target TeX: 2,357 bytes, SHA-256
  `1EAE03E37C9D0602F5972E61BD8F328570C1C199530D35932F882D6E9F9E0133`.
- Target PDF: 178,612 bytes, SHA-256
  `083AE3363895379E1A690D0865FDBD150EC2A6F1596A0A675BE08D583AF39E2F`.
- Pass-1 log: 7,303 bytes, SHA-256
  `3FFA2DBF4EDEEE74538A3E6D32F9FD86D33FB6C5E82668647E17341B5706D99A`.
- Pass-2 log: 7,185 bytes, SHA-256
  `0A9D390F6F9EC0B685730010B9B279A1250BE55A0E0CEC56B9557E6CC199FECF`.
- Final engine log: 24,384 bytes, SHA-256
  `8840332D5A8DE880DD174303F2CBDB62A528C604C715A7F3CD40A33BBB096970`.
- Target render: 156,442 bytes, SHA-256
  `A6E67AC8D7CDBEA2052334900D98252462ADDF2304A6BD5AEDB5C79799601368`.

The machine-evidence and producer-validation gates pass; the unit remains
`internal_not_for_release` pending fresh independent review. Build logs
contain local TeX runtime paths and must
be sanitized or excluded from any public payload. Continue at raw line 3424 /
substantive line 3425.

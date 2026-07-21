# Independent final audit: SGA2-X-PROPOSITION2.3-STATEMENT

## Decision

**PASS, internal evidence only.** The bounded producer unit for Proposition
2.3 is source-aligned, mathematically faithful, build-reproducible, and
render-clean. Producer bytes were not changed. This review does not publish,
dispatch, or claim completion of Expose X or SGA 2. The continuation boundary
remains raw French line 3424 (the excluded blank line) and substantive line
3425 (the proof).

## Authority replay and source coordinates

The admitted corrected French TeX is 586,789 bytes, SHA-256
`C2F899E92A904E312B550C6452A117FF23D30AF984B2254A0961D2DF0DACD042`.
I independently sliced lines 3414--3423 with a retained terminal LF. The
result is exactly 10 lines / 924 bytes / SHA-256
`0ADFF5B4A4FDD17DFF772AAF4AFA55FDFE23BC061351A440BC54CAD0ACC43B72`
and is byte-identical to `SOURCE_LINES_3414_3423.tex`. Line 3424 is blank;
line 3425 begins the proof with `(i) A ete vu.` in TeX accent notation. No
`pageoriginale` marker occurs inside the bounded slice.

The locator systems remain distinct: original printed p. 116, physical
same-edition reader pp. 100--101, and recomposed running pp. 92--93. At
original render detail, physical p. 100 shows Proposition 2.3 beginning after
the printed-p. 116 marker and physical p. 101 shows item (ii) before the next
printed-p. 117 marker. The reader is same-edition manifestation and layout
evidence only, not independent original-print corroboration.

## Translation, symbols, and mathematical content

The target preserves all data and quantifiers:

- locally noetherian prescheme `X`, closed subset `Y`, and formal completion
  `hat X` of `X` along `Y`;
- every open `U` of `X` containing `Y`;
- `L_U`, `P_U`, and `E_U`, respectively for locally free coherent
  `O_U`-modules, finite flat coverings, and etale coverings;
- pullback along `hat X -> X`;
- item (i): `Lef(X,Y)` and full faithfulness of all three functors for every
  open neighborhood `U` of `Y`;
- item (ii): `Leff(X,Y)`, every locally free coherent `O_hatX`-module
  `mathcal E`, and an open neighborhood `U` with a locally free coherent
  `O_U`-module `E` satisfying `L_U(E) ~= mathcal E`.

The French source abbreviates the finite-flat and etale instances in item
(ii) through three parallel `resp. ...` occurrences. The English sentence
that the analogous assertions hold for finite flat and etale coverings, with
`P_U` and `E_U` respectively, states those two source-supplied parallel cases
explicitly. It adds no hypothesis, object class, or source correction and is
therefore faithful explication, not emendation.

The jcreinhold file was independently re-hashed at 31,425 bytes / SHA-256
`2BDDBC3D15EECE7A47FDBDFBE31DAE735446BC14480A75113E704F63901C7BF5`.
Its lines 203--220 confirm its comparison-only role and the producer's
recorded rejections: duplicated Markdown item numbering, `inverse image by`,
literal unexplained ellipses, and renamed module objects. It is not authority
or independent corroboration.

## Independent build and PDF review

The producer TeX was copied byte-for-byte as `INDEPENDENT_REBUILD.tex`
(2,357 bytes; SHA-256
`1EAE03E37C9D0602F5972E61BD8F328570C1C199530D35932F882D6E9F9E0133`)
and compiled in this append-only review directory. Both pdfLaTeX passes exited
zero. Pass 1 contains only the expected rerunfilecheck notice; pass 2 and the
final engine log contain zero matched LaTeX/package warnings, overfull or
underfull boxes, undefined controls, emergency stops, or fatal errors.

The independent PDF is one A4 page, 178,612 bytes, SHA-256
`4112A2172FFFEDFD3302684AD1C0437270FACC22E49A572AF7BB839D45CC1E56`.
It differs from the producer PDF at the PDF-byte level because the rebuild has
a new creation timestamp and job name, but its 150-dpi render is byte-identical
to the producer render: 156,442 bytes, SHA-256
`A6E67AC8D7CDBEA2052334900D98252462ADDF2304A6BD5AEDB5C79799601368`.
Its layout-preserving extracted text is likewise byte-identical to the
producer extraction: 1,805 bytes, SHA-256
`C32B45DC7ACE16BD6D179D17E4D5D0B9FA30877324F4763347DB5B309BD43FB0`.

All 11 font rows are embedded, subsetted, and Unicode-mapped. I inspected the
independent target render and both source-page renders at original detail.
The authority panel, proposition label, hats, functor subscripts, Roman item
labels, `Lef`/`Leff`, displayed isomorphism, and parallel-case sentence are
legible. No clipping, overlap, broken glyph, black box, or omitted text is
visible.

## Machine evidence and privacy

The producer CSV independently validates at 10 data rows x 22 columns, 11
CRLF line endings, zero bare LF, unique nonempty stable IDs, zero formula
triggers, and zero parent/revision-reference errors. The producer JSONL
validates at 10 records with zero parse, duplicate-ID, parent, or revision
reference errors. The ordinal producer manifest has 25 live identities and
zero byte/hash mismatches.

Artifact Tool 2.8.24 imported the producer CSV as the full range `A1:V11`.
Its receipt, three rendered column panels, region inspection, and formula-error
scan all re-hash to the producer identities. I independently inspected all
three panels at original detail: every column A--V is present, headers and
records are legible, and no formula-error or formula-trigger value is present.

Privacy remains fail-closed for direct public use. Exactly three producer
files and three independent-review files contain reconstructable local TeX
runtime paths: each layer's two captured build-pass logs and final engine log.
They must be sanitized or excluded from any public successor. The producer and
review packages therefore remain `internal_not_for_release` even though the
bounded substantive audit passes.

## Gate result

The statement may be treated upstream as independently passed at its bounded
source cursor. Any archive/public payload still requires a privacy-clean
successor and an explicit archive-maintenance handoff by the owning task.


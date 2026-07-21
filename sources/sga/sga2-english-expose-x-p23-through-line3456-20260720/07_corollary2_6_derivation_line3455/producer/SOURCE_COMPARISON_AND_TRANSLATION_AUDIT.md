# Source comparison: SGA2-X-COROLLARY2.6-DERIVATION

This is a bounded source-aligned producer unit. It is not an independent
seal, publication payload, archive handoff, or volume-completion claim.

## Authority and boundary

- Authority: corrected French arXiv TeX `smf_doc-math_4_01.tex`, 586,789
  bytes, SHA-256
  `C2F899E92A904E312B550C6452A117FF23D30AF984B2254A0961D2DF0DACD042`.
- Scope: French line 3455 only, the complete one-sentence derivation after
  Corollary 2.6.
- Blank line 3454 is excluded. The long editor's note at line 3456 is also
  excluded for its own bounded unit. The raw cursor and next substantive
  cursor are both line 3456.
- Source coordinates: original printed p. 117, physical source-PDF p. 101,
  and recomposed running p. 93. These systems are not conflated, and no
  `\pageoriginale` marker occurs in the one-line slice.
- LF/no-terminal-EOL slice: 92 bytes, SHA-256
  `82F16E97EF1FBE7ADB5E19DD48E1688EB6EC5EA5828AC193D34F1DDF14D7119F`.
- LF/terminal-EOL slice: 93 bytes, SHA-256
  `8FF4A86B4B0D2A4CE56FBB97964E24A83F583985CA15FD0C54BDDD0C5BEC8A2D`.
- CRLF/terminal-EOL slice: 94 bytes, SHA-256
  `90C30EEF78EDD678D7551B1CDC3B700E78B9A4C107F030A7B0A64CFD1E75E50C`.
- Same-edition physical-p. 101 render: 407,075 bytes, SHA-256
  `E59A5DADE48D40EA47B11A4747A72A21ABA090FA09F697F403FC5B4ACD0FB793`.

The retained line replays exactly against authority line 3455. The page
render establishes the printed manifestation, references, and layout only;
it is not independent original-print corroboration. No source defect or
unresolved ambiguity was found, and the French authority remains
byte-identical.

## Translation, references, and terminology

The target reads: “All of this follows immediately from Propositions 1.1
and 2.3.” It preserves the anaphoric scope of `Tout ceci`, the derivational
relation, and both proposition references. The singular source abbreviation
is repeated before each reference; normal English coordination uses the
plural “Propositions” once without changing either referent.

Both labels were resolved in the admitted authority. Label `X.1.1` is the
proposition asserting the categorical equivalence
`Et(hat X) -> Et(Y)`. Label `X.2.3` is the proposition governing the
fully faithful and, under `Leff`, algebraizing functors for locally free
modules, finite flat coverings, and etale coverings. Neither label is
missing, mistyped, or redirected.

The exact terminal-LF authority targets are retained separately:

- `REFERENCE_TARGET_X_1_1_LINES_3327_3329.tex`: 213 bytes, SHA-256
  `8D26CF3517241995FD7ABF24F94BC59E5D0BCEE195A494C5C81D21FADB9FF1C5`;
- `REFERENCE_TARGET_X_2_3_LINES_3414_3423.tex`: 924 bytes, SHA-256
  `0ADFF5B4A4FDD17DFF772AAF4AFA55FDFE23BC061351A440BC54CAD0ACC43B72`.

Both files replay byte-exactly against their declared authority ranges.

The established English lane register translates `résulte trivialement` as
“follows immediately.” The alternative “follows trivially” is semantically
possible but was rejected as an unnecessarily literal register choice, not
as a French source defect. Stable rejected-choice record
`SGA2-X-C26-DERIV-COMPARE-TRIVIALLY-REJECT-001@1` preserves this decision.

## External comparison candidate

The current jcreinhold chapter
`ii/10-application-to-the-fundamental-group.md` is 31,425 bytes, SHA-256
`2BDDBC3D15EECE7A47FDBDFBE31DAE735446BC14480A75113E704F63901C7BF5`.
Its matching sentence is line 270, preserved with terminal LF as
`JCREINHOLD_LINE_270.md`, 72 bytes, SHA-256
`DE70675A97363E141810E0658E2618A01CFA715A4A9CEDDB22111829B5A113B2`.
It preserves both proposition numbers and the ordinary sentence structure,
but uses “trivially.” It remains one LLM-generated comparison lineage, not
authority or independent corroboration. The target was translated from the
French and uses the established “immediately” register.

Rejected choices include omitting either proposition, changing either
number, treating the references as formulas, importing the line-3456
editor's note, replacing “immediately” by the candidate's “trivially,”
silently patching the French, or conflating printed, physical, and running
page systems.

## Build and rendered QA

Two pdfLaTeX passes completed. Pass 1 contains only the expected
`rerunfilecheck` request; pass 2 has zero matched LaTeX/package warnings,
overfull or underfull boxes, undefined controls, emergency stops, fatal
errors, or LaTeX errors. The target is one A4 page. All five font rows are
embedded, subsetted, and Unicode-mapped.

The target 150-dpi and source 200-dpi renders were inspected at original
detail. The authority box, both reference numbers, sentence punctuation,
margins, and page number are legible without clipping, overlap, broken
glyphs, black boxes, or missing text. The source page visibly prints the same
line immediately before editorial note (3).

- Target TeX: 1,209 bytes, SHA-256
  `6072C2E73CCD8A9063D9B4671E84059ED699ECF8EB2D480FBC2F9EBEF95CABAA`.
- Target PDF: 135,713 bytes, SHA-256
  `74E3B33F70C99399096DA0B020C94D7DDB828CE2AD49F1E2DBFD9DB681AFD837`.
- Pass-1 log: 5,553 bytes, SHA-256
  `32E37245E7D6EF7BE531A6ABA680E8588C6979A57762D69CF8D30E51B656CC71`.
- Pass-2 log: 5,434 bytes, SHA-256
  `576C05D31662007DA0C74CF24760F9A18F2F4DD67CE8E606FEB9A274425EF8A0`.
- Final engine log: 19,805 bytes, SHA-256
  `EF0546C513616778F7ADF7829D874D86CD12C0B5B0C923E3291403787A7E195C`.
- Target render: 72,848 bytes, SHA-256
  `77E62951DDBD7A6235DBAB8AF17E1BF461389D2105D5FB21A9E484F2765B0D21`.

The package remains `internal_not_for_release` pending machine validation
and fresh independent review. The two build logs and final engine log contain
local runtime paths and must be sanitized or excluded from any public
payload. Continue at raw/substantive line 3456.

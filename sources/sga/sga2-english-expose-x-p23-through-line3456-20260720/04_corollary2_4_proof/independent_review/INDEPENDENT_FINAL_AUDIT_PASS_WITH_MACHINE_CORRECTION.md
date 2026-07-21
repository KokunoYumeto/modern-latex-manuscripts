# Independent final audit: PASS with append-only machine-locator correction

## Disposition

The bounded SGA 2 Exposé X Corollary 2.4 proof passes independent source,
translation, formula, build, PDF, render, font, and machine-structure review.
The producer target TeX and PDF are unchanged. One comparison-only machine
locator was two lines early: the complete relevant jcreinhold proof occupies
chapter lines 236--243, not 234--241. Record
`SGA2-X-C24-PROOF-COMPARE@2` supersedes producer record
`SGA2-X-C24-PROOF-COMPARE@1` append-only. This correction changes neither the
French reading nor the English target.

The resulting review status is
`independent_review_pass_with_machine_locator_correction`. It is not a public
release, archive handoff, volume-completion claim, or permission to expose the
path-bearing logs.

## Frozen boundary and authority

- Authority: corrected French TeX `smf_doc-math_4_01.tex`, 586,789 bytes,
  SHA-256
  `C2F899E92A904E312B550C6452A117FF23D30AF984B2254A0961D2DF0DACD042`.
- Scope: authority lines 3433--3437 inclusive, the complete proof of
  Corollary 2.4.
- Locators: original printed pp. 116--117; physical same-edition PDF p. 101;
  recomposed running p. 93.
- Boundary: blank line 3438 is excluded. Raw cursor 3438; next substantive
  cursor 3439, Corollary 2.5.
- Exact retained terminal-LF slice: 300 bytes, SHA-256
  `3DB457DA2960EE068953F0B48D0CFA89DA0385EFE2B3321D1D62E5F13C5C107C`.

An independent direct extraction of authority lines 3433--3437 is byte-equal
to `SOURCE_LINES_3433_3437.tex`. The `\pageoriginale` token occurs within
line 3433 immediately after `deux` in `deux anneaux non nuls`; it advances the
printed locator from 116 to 117 without changing the sentence. Physical page
101 visibly contains running page 93 and the printed 117 transition. That PDF
is same-edition manifestation, typography, formula, and layout evidence only,
not independent original-print corroboration. French authority bytes remain
unchanged. No source defect or unresolved ambiguity was found in this unit.

## Translation, terminology, and formula review

The complete source sense is present. The target correctly states that a
locally ringed space `(X,O_X)` is connected if and only if its global-section
ring is not a direct product of two nonzero rings. “Direct product” is the
correct English choice for rings; “direct sum” was rejected. The conjunction
and proof logic of `En effet ... Or on a ... par Lef(X,Y)` are preserved.

The displayed formula independently replays as

`Gamma(U,r_*O_R) ≃ Gamma(hat X,hat r_*O_hat R)`

with both domains, direct images, hats, subscripts, the isomorphism, and the
`Lef(X,Y)` attribution intact. No symbol, exponent, index, or object was added,
lost, or silently normalized.

The jcreinhold chapter is 31,425 bytes, SHA-256
`2BDDBC3D15EECE7A47FDBDFBE31DAE735446BC14480A75113E704F63901C7BF5`.
Its proof occupies lines 236--243 and is comparison-only. It is one external
LLM lineage, not authority or independent corroboration. The producer CSV's
234--241 locator included two lines from the preceding statement and omitted
the closing attribution; the append-only successor corrects only that locator.

## Independent rebuild and PDF comparison

The producer target identities remain:

- TeX: 1,696 bytes, SHA-256
  `8F867DE410B58747B336FD61EF9050DE2BB464DCE324FF8A001513B8E19BC052`.
- PDF: 199,476 bytes, SHA-256
  `963DDF70C59130B99D1C37BC0333AE8B87682A650796A8F43B8EB5992C2AC8EF`.

Two fresh pdfLaTeX passes from the untouched producer TeX exited zero. Pass 1
has only the expected `rerunfilecheck` request; pass 2 has zero matched LaTeX
or package warnings, bad boxes, undefined controls, emergency stops, or fatal
errors.

- Independent pass-1 log: 8,212 bytes, SHA-256
  `5263CE07C58FA71E1360BF3EE6E292D1772D757A24A4EB9A8D51E14B83ACC938`.
- Independent pass-2 log: 8,788 bytes, SHA-256
  `B5BC4505F851918C239B9B640E457858F38B7D3187E917040FBC3ED6390AB67E`.
- Independent PDF: 199,476 bytes, SHA-256
  `18AEED328ED8F21DC7C122B4FDF6346EC030783F685CB64103E786CC882EBE33`.

The two PDF file hashes differ only at the file/metadata layer: creation and
modification dates changed from 01:46:40 to 02:01:40 local time. The decoded
page streams are byte-identical, both SHA-256
`76D51E4768054A595D80B8A86E6FE45255AD30839ADBE44635974570B02667A8`.
The extracted texts are byte-identical, both SHA-256
`A85C6CBB4CDA9096206063A7674EA2C062F6AFDD487813A69367268553A39803`.
The one-page A4 PDF is unencrypted, has no JavaScript, and has the expected
title/author metadata.

All 13 font rows are embedded, subsetted, and Unicode-mapped. The independent
font table is byte-identical to the producer table, SHA-256
`80E0A681A21F10A14E7F864D09D69DB00286329D8A03BC048EE5603E1158348E`.

## Rendered visual QA

The independent 150-dpi render is 103,512 bytes, SHA-256
`F952BFBC4E525F7BD478CECF42C5C269F55C694C04F8B278B87964FA469B88E2`,
pixel-identical to the producer render. Original-detail inspection of the
source physical-page render and the independent target render confirms:

- the three locator systems and mid-sentence printed-page transition are
  reported accurately;
- the connectivity criterion, `Gamma`, both direct images, hats, subscripts,
  isomorphism sign, and `Lef` attribution are legible;
- there is no clipping, overlap, broken glyph, black box, missing text, or
  margin collision.

## Machine evidence

Producer controls independently revalidate as follows:

- CSV: 7 data rows by 22 columns, 8 CRLF records including header, zero bare
  LF, unique nonempty IDs, zero formula-trigger cells, and zero parent errors;
  SHA-256
  `32401A2C18DDC31445DBCDEA9A82AAD883AA41C1826690F49CBF87ECF28BAF09`.
- JSONL: 7 parsed records, unique IDs, zero parent errors, and exact CSV ID-set
  equality; SHA-256
  `01CF2F3875CE8D29CF7FE9059A6CCE0B37F33D0494CD390F3EF9526984394FF3`.
- Producer manifest: 24 rows rehashed with zero identity errors; SHA-256
  `7B831A743ADB8ACA52A5980FC97439E2FA10504571C4DF15A56DA96A761EFC68`.
- All three producer Artifact Tool panels were inspected at original detail.

Independent controls contain 17 stable-ID records in both CSV and JSONL. The
CSV is 17 by 26, CRLF, rectangular, formula-safe, and hierarchy-closed. The
JSONL parses cleanly and has the same ID set. Revision and supersession fields
bind the comparison-locator correction to its producer predecessor. Current
identities are:

- Independent CSV: 12,542 bytes, SHA-256
  `7685A01C97CBAD1C7389A7BD51D94034E435085269E163B15FA16E7E7A65A3B2`.
- Independent JSONL: 10,166 bytes, SHA-256
  `DC03F163E14246AA5E70697A05827D87249A1662D3074475229D38B2982A139F`.
- Artifact Tool receipt: 1,619 bytes, SHA-256
  `A0BCFE930DC566E7BECFD5B70EFD76CC5D75D0334F5A8BE6E384225E14A28A0E`;
  status `pass`, 17 rows, 26 columns, zero formula errors/triggers, and four
  rendered panels covering A--Z. All four panels were inspected at original
  detail after the locator correction.

## Privacy and release gate

Exactly six internal text logs currently contain reconstructable local paths:

1. producer `BUILD_PASS1.log`;
2. producer `BUILD_PASS2.log`;
3. producer target engine `.log`;
4. review `rebuild/INDEPENDENT_BUILD_PASS1.log`;
5. review `rebuild/INDEPENDENT_BUILD_PASS2.log`;
6. review `rebuild/INDEPENDENT_REBUILD_C24_PROOF.log`.

They must be sanitized or excluded before any public custody package. This
review therefore remains `internal_not_for_release`. No archive or Zenodo
handoff was made. The source-checked continuation remains raw line 3438 /
substantive line 3439.

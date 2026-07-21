# SGA2 Exposé X Remark 3.7 — fresh independent final audit

## Disposition

**PASS** for the exact producer TeX and PDF identities reviewed here.

This closes the independent source-review gate for the bounded unit only. It
does not change the French authority, overwrite producer files, declare the
whole exposé or volume complete, authorize public release, or claim an archive
handoff.

## Exact bounded scope and cursors

- French authority lines: 3532–3534.
- Editable unit count: one complete Remark 3.7.
- Current-rescribe locator: lines 3532–3534.
- Original printed page: 120.
- Same-edition source-PDF physical page: 104.
- Recomposed running page: 96.
- Raw continuation cursor: line 3535, an excluded blank line.
- Next substantive cursor: line 3536, the excluded opening of Corollary 3.8.
- The preceding Lemma 3.6 proof, lines 3522–3530, and blank line 3531 are
  excluded and absent from the target body.

These locator systems and cursors remain distinct.

## Authority replay and source result

The reviewer reread the corrected arXiv French authority directly:
`smf_doc-math_4_01.tex`, 586,789 ISO-8859-1/LF bytes, SHA-256
`C2F899E92A904E312B550C6452A117FF23D30AF984B2254A0961D2DF0DACD042`.
Independent byte slicing reproduces lines 3532–3534 as 218 bytes, SHA-256
`7F0D9E686076D85702CAA5E3E9F5216AC73B0EF78E271E88ACA58573C73BB18D`,
and reproduces every producer boundary slice exactly. The authority remains
unchanged.

The bounded French is coherent. No source defect, type conflict, numbering
conflict, or unresolved ambiguity was found.

## Translation, symbols, and numbering

The producer target is faithful:

- `Remarque` with label `X.3.7` is visibly `Remark 3.7.`;
- `On a prouvé chemin faisant` is rendered as “We proved along the way,”
  preserving its retrospective proof register;
- `O_X -> i_* O_U` retains source, target, arrow direction, pushforward, and
  the assertion that the map is an isomorphism;
- connectedness of `X` if and only if connectedness of `U` remains a full
  biconditional;
- `pi_1(U) -> pi_1(X)` retains domain, codomain, subscripts, and direction;
- “is surjective” preserves the strength of `est surjectif`.

Repeating “connected” after `U` resolves the French ellipsis without changing
the statement. No material from the adjacent proof or corollary was imported.

The jcreinhold `e7a259f` chapter was checked only as one comparison lineage.
Its hypothesis, biconditional, map, and conclusion agree after French source
checking. Its unnumbered visible heading, “shown in passing,” ellipsis after
`U`, and `original page 96` comment are appropriately rejected or normalized.
Running page 96 is not original printed page 120. The candidate is neither
authority nor independent corroboration.

## Independent build and PDF comparison

- Exact producer TeX: 1,623 bytes, SHA-256
  `AF2A17669348B4B5B25C0F7DBC4476DAFBD5A1DD68A199C9AF97E16EA1314F0B`.
- Exact producer PDF: 201,876 bytes, SHA-256
  `699745968DAEB371AC26F389976A61F15F63083DB2231C96D5D69C53162C6269`.
- Fresh independent three-pass pdfLaTeX rebuild: 201,876 bytes, SHA-256
  `7641BB9C232ABF025E01A5252B425AB00D125FF26EA2065D8C9C7399C62C892B`.

All three compile passes exit zero. Pass 1 has only the expected initial
`rerunfilecheck` notice; passes 2 and 3 have no warning or error and their
console logs are byte-identical. The rebuild and producer binaries differ only
in creation/modification timestamps. Their one decoded page stream, extracted
text, A4 media box, 13-row embedded/subsetted/Unicode font inventory, and fresh
200 dpi raster are identical.

Original-detail inspection of the fresh source and target renders passes. The
source renderer's known legacy display-font notices do not obscure or alter
the bounded remark. No clipping, overlap, missing glyph, black box, line loss,
or formula ambiguity was found.

## Machine evidence and custody

The producer CSV and JSONL parse cleanly, have 38 unique stable IDs in matching
order, maintain rectangularity and local reference closure, and contain no
formula-injection trigger cell. The 59-row producer manifest resolves every
represented safe relative path to the declared byte count and SHA-256. The
excluded live Artifact Tool runtime junction is not treated as manifest
content.

This fresh review retains its own stable-ID CSV/JSONL, validation report,
reproducibility report, render evidence, build logs, and recursive checksum
manifest. The review package is `internal_not_for_release`: source slices and
source raster are rights-gated, while copied controls and logs may contain
private local paths. No shared manager STATUS/log edit, archive dispatch,
GitHub action, Zenodo action, or public-readback claim is made.


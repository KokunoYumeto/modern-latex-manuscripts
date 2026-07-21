# Producer final audit — PASS pending independent review

## Result

**`producer_pass_pending_independent_review`.** The complete English Remark 3.7
for corrected French authority lines 3532–3534 passes the producer source,
translation, formula/symbol, numbering, terminology, source-defect, boundary,
locator, build, font, text, render, machine-ledger, and Artifact Tool gates.

It is not independently reviewed, sealed, publication-ready, or authorized for
archive handoff.

## Exact scope

- Included: complete Remark 3.7, lines 3532–3534; one editable unit.
- Excluded and untouched: the preceding Lemma 3.6 proof, lines 3522–3530,
  and blank line 3531.
- Excluded: blank line 3535 and Corollary 3.8 opening line 3536.
- Raw cursor: 3535; next substantive cursor: 3536.
- Original printed page: 120; source-PDF physical page: 104; recomposed running
  page: 96.

## Source and translation result

The target preserves the exact hypothesis that
`O_X→i_*O_U` is an isomorphism, the biconditional between connectedness of
`X` and `U`, and the consequence that `π_1(U)→π_1(X)` is surjective. Domain,
codomain, arrow direction, subscripts, logical strength, and visible number
`Remark 3.7` are intact.

The bounded French source is coherent. No source defect, ambiguity, or silent
emendation was found. The French authority remains byte-identical at 586,789 B,
SHA-256 `C2F899E92A904E312B550C6452A117FF23D30AF984B2254A0961D2DF0DACD042`.

The jcreinhold `e7a259f` text was used only as one comparison lineage. Its
semantic coverage was accepted only after French checking. Its hidden rather
than visible numbering, elliptical connectedness wording, and “shown in
passing” register were normalized. Its `original page 96` comment was rejected:
96 is the recomposed running page; the original printed page is 120.

## Target and build identities

- TeX: 1,623 B; SHA-256
  `AF2A17669348B4B5B25C0F7DBC4476DAFBD5A1DD68A199C9AF97E16EA1314F0B`.
- PDF: 201,876 B; SHA-256
  `699745968DAEB371AC26F389976A61F15F63083DB2231C96D5D69C53162C6269`;
  one A4 page.
- Three pdfLaTeX passes exit zero. Pass 1 has only the expected initial rerun
  notice; passes 2 and 3 are clean and byte-identical as console logs.
- Thirteen of thirteen font rows are embedded, subsetted, and Unicode-mapped.
- Extracted text: 1,101 B; SHA-256
  `DE2D450407A5F029A23FC73DE8FC69E2FD59EF6FF2BBA1A9CC9E207F3D0DDE8A`.
- Target render: 149,450 B; SHA-256
  `CF375B491B7A3AE36DC2AA891535C43ED62985B3D038E193590BFEA599A6907C`.
- Source physical-page-104 render: 392,630 B; SHA-256
  `0CBF631AC8F698115683A90439E57C357549A2AC7F76CD3BC3AAA7CFEC0165EE`.

Both source and target render inspections pass at original detail, with no
clipping, overlap, missing glyph, black box, or formula ambiguity.

## Machine evidence

- CSV: 38 rows × 22 columns; SHA-256
  `3DC582CA12EF675D4A81191DD6D28C4EF45929188596AE85F4658D42ADF98488`.
- JSONL: 38 records; SHA-256
  `0E9D63857F8C873D79EE30DBDB6B33E2577A70C411692342505C469CDD5ADA7A`.
- Ledger validation: PASS with failures `[]`; SHA-256
  `DAE57ED07335A62E573C700E4B4995C3F26BC768F3CB03BC886570818EA0C1A5`.
- Artifact Tool receipt: 38 rows × 22 columns, unique nonempty IDs, zero formula
  errors/triggers, three panels; SHA-256
  `479A7185B7BA05E17B2DB48B70F6862946658E5E87C2F770B2F272A86962E8D7`.
- All three panels passed producer original-detail visual inspection.

Stable IDs, source/target locators, hierarchy, difficulty, revision state,
parent/child/revision reference closure, cursor state, evidence hashes, and
release holds are present.

## Custody

The full working tree is `internal_not_for_release`. French source slices and
the source raster are rights-gated. The jcreinhold slice is comparison-only.
Internal scripts, logs, and receipts may expose private local paths and must be
excluded or sanitized before any future public payload.

No independent review, seal, archive handoff, shared-log edit, GitHub action,
or Zenodo action is claimed. The next gate is a fresh independent PASS on these
exact target and evidence identities.

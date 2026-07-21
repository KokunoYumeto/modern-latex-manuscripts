# Independent final audit PASS -- SGA2 Expose X, Corollary 2.6 editor's note (3)

Decision: PASS. The producer unit is source-aligned at the reviewed boundary.
No source defect or unresolved source ambiguity was found. Producer bytes
were not modified. This review does not itself seal, publish, or hand off the
unit to an archive.

## Exact scope and authority

- Authority: `smf_doc-math_4_01.tex`, 586,789 bytes, SHA-256
  `C2F899E92A904E312B550C6452A117FF23D30AF984B2254A0961D2DF0DACD042`.
- Included: French line 3456 only, one complete `ndetext` editor's note.
- Exact no-EOL replay: 2,145 bytes, SHA-256
  `C5F8286F8A860C2BA1F892B9CBAEF882C810C72AADB23BFAA2667B86EF9A3581`.
- Exact CRLF replay: 2,147 bytes, SHA-256
  `694B4AE97FB45D030BE47C59D4DD1F28C359109855379B731DB8D379E1744A86`.
- Boundary: line 3454 blank; line 3455 is the prior derivation; line 3456 is
  the complete note; blank 3457 is excluded; line 3458 opens Section 3.
- Continuation: raw cursor 3457; substantive cursor 3458.
- Locators: printed 117-118; physical source-PDF 101-102; running 93-94.
  These locator systems remain distinct.

Both source pages were inspected at original detail. The note begins on
physical 101 and continues at the foot of physical 102 after the main Section
3 text begins. This is verified footnote layout, not an apparent omission or
reordering.

## Translation and mathematical audit

Every source sentence was compared with the target and the comparison-only
jcreinhold lineage.

- The relative Lefschetz derivation retains Proposition 3.3 and both
  cross-volume criteria XII.2.4 and XII.3.4.
- The projective-flat hypotheses, connected noetherian schemes, effective
  relatively ample relative Cartier divisor, and all quantifiers are intact.
- The depth-at-closed-points thresholds `>= 2` and `>= 3`, connectedness,
  purity, complete-intersection example, and conclusions are intact.
- Source and target each contain eight `pi_1` occurrences. Five distinct map
  checks pass: `i_U`, `i_X`, the geometric-surface surjection, the
  projection-induced arithmetic map, and its inverse induced by `P`.
- Nefness and positive self-intersection are retained.
- Bost and Ihara titles, venues, volumes, pages, theorem and corollary numbers,
  acute `Ec.`, and the Belyi diacritic are retained from the French authority.
- Lowercase `noetherian` is the established target register.
- `merely` correctly renders discourse-level `simplement` without the
  technical suggestion of simple connectedness.
- The projection map is accurately described as an isomorphism whose inverse
  is the oppositely directed map induced by `P`.

The four exact authority reference slices for X.3.3, X.3.4, XII.2.4, and
XII.3.4 were replayed byte-for-byte and resolve to the claimed proposition,
purity theorem, and two cross-volume corollaries.

## Comparison and decisions

The current jcreinhold Markdown is 31,425 bytes, SHA-256
`2BDDBC3D15EECE7A47FDBDFBE31DAE735446BC14480A75113E704F63901C7BF5`.
Its line 256 contains the footnote call and lines 541-559 contain the complete
deferred note. No omission adverse finding is warranted.

The independent review confirms these stable decisions:

- Accepted: `SGA2-X-L3456-AU-DESSUS-NORMALIZATION-001@1`; the corrected
  `sisi` branch selects `au-dessus`, rendered visibly as `over`.
- Rejected: `SGA2-X-L3456-JCREINHOLD-XII-PREFIX-REJECT-001@1`; the target
  retains both `XII` prefixes.
- Rejected: `SGA2-X-L3456-JCREINHOLD-SIMPLY-REJECT-001@1`; the target uses
  `merely`.
- Rejected: `SGA2-X-L3456-JCREINHOLD-INVERTIBLE-PHRASE-REJECT-001@1`; the
  target uses precise isomorphism/inverse phrasing while preserving both map
  directions.

## Build, render, and machine evidence

- Producer TeX: 3,730 bytes, SHA-256
  `9D0A5373889DB323F804DA0C21A22405E93988743E310D1328C0E31F6356EDD5`.
- Producer PDF: 275,147 bytes, SHA-256
  `33B82F41791672BA26C0237A25B2A8D9B8807AE38C9060B66943A021887D1B0C`.
- Fresh PDF: 275,147 bytes, SHA-256
  `32746F8A9E344844468205D3260CD3C034A295AD23C149551C5D2AE00C986706`.
- Three-pass rebuild: pass 1 has only the expected rerun warning; passes 2
  and 3 are clean and byte-identical.
- Producer/fresh extracted text: exact, SHA-256
  `080D6C1021C2EC081DCD3F09D4E50CD14A9E2AFCAED326637D086DBB41F5A663`.
- Producer/fresh raster: exact, SHA-256
  `BBC2E912CFA9BCC0B255FE4B6807978F8868D2EEF9A2C72E0790571E80BC5BB5`.
- Producer/fresh font table: exact, 14 good rows, SHA-256
  `2FCFC61208B42C0D8EEA48E94E1688FF116735FD0EF54B7FEBE897D89A347D18`.
- Non-time PDF metadata: exact.

Producer machine evidence independently validates at 32 CSV rows x 22
columns and 32 strict JSONL records. IDs are unique and nonempty; CSV is
rectangular and formula-safe; JSONL has closed hierarchy, difficulty,
revision, parent, and supersession references; CSV and JSONL ID sets match.
Producer manifest coverage is exact at 38 root payload rows with no byte or
hash mismatch. Validation and file timestamps are actual and non-future.

Independent evidence validates at 36 CSV rows x 28 columns and 36 strict
JSONL records. Artifact Tool 2.8.24 replayed both machine surfaces with zero
formula-error or trigger values, and all six rendered panels received direct
visual review.

## Release gate

The unit remains `internal_not_for_release`. Four producer build/engine logs
contain private local paths. Within the independent review, seven rebuild
logs and four reproducibility/validation scripts contain private local paths.
All eleven review files must be sanitized or excluded before publication.
The two source-page rasters are rights-gated internal evidence. No archive
handoff was made.

# Independent final audit - SGA2 Expose X Lemma 3.9 statement

Verdict: `PASS` for the bounded source-aligned unit. The owning SGA2 lane may
treat this unit as independently sealed, subject to its append-only status,
cumulative-integration, and archive-custody procedures. This review performs
no archive handoff, shared-log write, French-source mutation, or public
release.

## Scope and authority

- Sole editable authority: corrected arXiv French TeX
  `smf_doc-math_4_01.tex`, 586,789 bytes, SHA-256
  `C2F899E92A904E312B550C6452A117FF23D30AF984B2254A0961D2DF0DACD042`.
- Exact bounded source: lines 3544-3553, 827 Latin-1 LF bytes, SHA-256
  `1938246ACBCA9D6DBE4F16CDFD933184C8005562DACE517CBD982098629F0231`.
- Locators: original printed page 120; same-edition source-PDF physical page
  104; recomposed running page 96.
- Raw continuation cursor: blank line 3554. Next substantive cursor: proof
  line 3555.
- French authority and producer target remained byte-identical throughout
  review.

The same-edition 216-page reader is manifestation and locator evidence only,
not independent original-print corroboration. The jcreinhold e7a259f English
Markdown is one LLM-generated comparison lineage and was not used as
authority.

## Translation and source-defect disposition

The target preserves the lemma number, all ring hypotheses, `t`-adic
completeness, the regular-local-quotient condition and parenthetical example,
`B=A/tA`, both numbered items, both dimension/depth hypotheses, the two
opposite purity implications, and editor's note (5). The French operator
`prof` is rendered as standard mathematical English `depth`; formulas,
subscripts, inequalities, memberships, and logical directions are otherwise
unchanged.

Manager decision
`EG-SGA2-X-L3551-MISSING-EST-SOURCE-DEFECT-ADJUDICATION-20260722-0001`
is applied under final stable ID
`SGA2-X-L3551-MISSING-EST-SRCDEF-001`. French line 3551 lacks the finite
copula in `si A_p pur lorsque t notin p`; English correctly says that
`A_p is pure whenever t is not in p` and displays the stable-ID note
immediately in item (ii). Provisional candidate
`SGA2-X-L3551-MISSING-EST-SRCCAND-001@1` remains append-only and is explicitly
superseded. The later source `si` before the depth-three condition is present
and has not been duplicated or misdiagnosed.

## Independent build, render, and machine gates

The exact 3,041-byte producer TeX, SHA-256
`670B61898309661847F5EA53FA20399958DD5E627F9873ED9C29AB4B9551ACA9`,
was copied into an isolated build directory. Three fresh pdfLaTeX passes each
produced the same 277,302-byte, one-page A4 PDF, SHA-256
`DDE0C24DBE66647300B18804CD726D209FA56C7A498895B90481459281CE1625`,
byte-identical to the producer PDF. The engine logs contain no TeX error,
warning, overfull box, or underfull box. All 18 fonts are embedded, subset,
and Unicode-mapped. Fresh extracted text and target/source renders passed
original-detail inspection.

Producer machine evidence independently revalidated as 44 CSV rows x 26
columns and 44 JSONL records: rectangular/formula-safe CSV, unique stable IDs,
complete required schema, parent/revision/supersession/reference closure,
evidence-identity closure, exact three-coordinate locators, and distinct raw
3554/substantive 3555 cursors. The 66-row recursive producer manifest has
contiguous ordinals, unique path coverage, exact rehash closure, and no file
marked public. Artifact Tool independently replayed the full producer CSV,
found zero formula errors or formula-safety triggers, and rendered five
visually inspected panels.

Core independent validation completed 62 checks with zero errors. Rights
controls keep French slices/source imagery and comparison text gated; the
review package remains `internal_not_for_release`. The one-page PDF is
untagged and has no metadata stream, so it is not a standalone publication
payload even though the bounded translation gate passes.

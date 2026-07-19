# Source check and review - SGA 1 Exposé I section I.6

## Exact bounded source

- Sole textual authority: French arXiv `math/0206203v2` TeX.
- Authority archive SHA-256:
  `0A33C9C06908705A2525690FAAE02F6F07980A4AA069A8B6CFF9B1D9BC39ACD3`.
- French main-TeX SHA-256:
  `754E9FD6BC04BA52359D0CF4102AA01D2805A00B0E3E298CCD7396564CC7702D`.
- Included lines: 1168--1216 inclusive; 49 LF-normalized lines; 1,983
  UTF-8 bytes; slice SHA-256
  `7F9831D26582DB33861D2C9D48F6DD09C6956F639C566A92FAFA0514F08DDFCD`.
- First excluded line: 1217, the section I.7 heading.
- English fragment: 2,168 bytes; SHA-256
  `101CD6F1FC9C46E754E3AD31903863FCA2418DCF31A2E91D47637DF4815291EF`.

The original printing was used only as an audit witness at physical PDF page
26 / printed Exposé I page 9. External English witnesses were used only as
target-language comparison controls.

## Source and formula result

Seven source-comparison rows and seven formula/structure rows cover the
editorial opening, Theorem I.6.1, the fully-faithful bridge, Corollary I.6.2,
its unheaded reduction, the essential-surjectivity construction, and the
excluded I.7 cursor. Checked objects include the exact direction and category
of `R(B)=B tensor_A k`, the variance and arguments of the canonical Hom map,
the reduction through `A/m^n`, and the constructions `k[t]/F k[t]` and
`A[t]/F_1A[t]`.

The source hierarchy remains intact: no proof wrapper, QED, theorem, or
heading was added to the unheaded paragraphs. Plain `I.7` is used as a bounded
document locator rather than an unresolved TeX reference. No source-original
defect or unresolved source ambiguity was found. Two source-compressed
standard steps were recorded in the adverse ledger and not expanded in the
translated body.

## Evidence and independent review

- Promoted comparison input: 7 rows, 4,386 bytes, SHA-256
  `097D362D41D57143609DFBEC7DFA11FED3E3EB79381877AF3129CC4F97ABF1FB`.
- Promoted formula/structure input: 7 rows, 2,383 bytes, SHA-256
  `40B650EE723CA7723BD66EB2A7E469C7ED90A28963904E0B497D121F1559764B`.
- `ledgers/PUBLIC_SOURCE_COMPARISON_I_6.csv`: 7 public rows; the six
  promoted unit rows are projected as `closed_source_checked_independent_pass`
  and the cursor row remains `cursor_fixed_independent_pass`.
- `ledgers/PUBLIC_SOURCE_FORMULA_AND_STRUCTURE_CHECK_I_6.csv`: the same seven
  terminal public statuses.
- `ledgers/PUBLIC_SGA1_I6_EVIDENCE_GRAPH.jsonl`: 7 records; source input
  8,506 bytes, SHA-256
  `16A5E3A7E37C9130D6E5ACE366825A992649BBD834D237537461DDF0A0683CBC`.
- `ledgers/PUBLIC_SGA1_I6_DIFFICULTY_FAILURE_REVISION.jsonl`: 2 records.
- Sealed local machine-gate receipt: 17,181 bytes, SHA-256
  `AB341EFB62BC6DFAE98485864FDDD046B8CF8224F541EF060D5A91EA66A16492`;
  217 CSV rows, 77 JSONL records, zero failures.
- Continuation cursor: French line 1217, excluded.

Two independent automated read-only source audits compared the final fragment
against the exact French slice and original-print witness. Both returned PASS
with no remaining change request. This is not human scholarly peer review or
mathematical certification.

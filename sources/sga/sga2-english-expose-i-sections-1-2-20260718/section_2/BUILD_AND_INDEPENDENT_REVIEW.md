# Build and independent review: Exposé I, §2

Review date: 2026-07-18

## Build

Target source:

`SGA2_Expose_I_section_2_English_SourceAligned.tex`

Target PDF:

`SGA2_Expose_I_section_2_English_SourceAligned.pdf`

The target was compiled twice with `pdflatex` in nonstop, halt-on-error mode.
The retained final log is:

`evidence/build/SGA2_Expose_I_section_2_English_SourceAligned_final.log`

Final build results:

- exit status: PASS;
- PDF pages: 5;
- errors: 0;
- warnings: 0;
- overfull/underfull boxes: 0;
- unresolved references: 0;
- TeX SHA-256:
  `C532156CDE07F10D4419115FC91490DAF3A0C05020F1DCA31C0700776D255404`;
- PDF SHA-256:
  `7FB6C5346BEE69949C6A61E6BCB4FD52BBF0CCDBF9629C5D57BB7739C68AE513`.

A strict PDF parser also confirmed a readable five-page file.

## Independent source review

The corrected French TeX lines 280--503 were split into two independent
source-review ranges, 280--390 and 391--503. Review covered prose, every
statement, equations (19)--(32), bis labels, underlined sheaf functors,
restrictions, inverse-image stars, closure bars, primes, subscripts, arrows,
inequalities, printed-page markers, corrected `\sisi` branches, editorial
notes, and bibliography.

The first pass identified five presentation/traceability defects:

- singular “Remark” where the source heading is plural;
- an omitted reference to the preceding editorial note;
- one printed-page marker placed a word too early;
- a second original-to-corrected reference occurrence not covered by the
  consolidated editorial note; and
- quotation marks lost on the second historical occurrence of
  “sheafifying.”

All were corrected. Both source ranges then returned PASS with no remaining
translation defect.

A separate release audit found stale target/source locators in four ledger
rows and one stale singular heading in `UNIT_STATUS.md`. Those metadata
defects were corrected; the final metadata re-audit returned PASS, with all
CSV files parsing at uniform row widths.

## Explicit source decisions

The target transparently records four source emendations:

1. equation (25): restore the middle support subscript `Z`, required by
   equations (18), (24), and Proposition 1.8;
2. equation (28): restore the omitted argument `(F)`, supplied by the
   immediately following explanatory prose;
3. closing remark: use ambient `X` instead of source lowercase `x`; and
4. complete only the grammatical syntax forced by equation (30) for the
   normal orientation sheaf.

The French source reading and the basis for each decision remain visible in
the target notes and ledgers.

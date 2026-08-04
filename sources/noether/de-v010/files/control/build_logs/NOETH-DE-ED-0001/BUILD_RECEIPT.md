# NOETH-DE-ED-0001 build receipt

Build date: 2026-08-04 (Europe/Berlin)

## Input

- TeX bytes: `2,153,565`
- TeX SHA-256: `D1F06B311F6CBD991DD247D745DD9A72DDE326A20396DF43CFE0C8EDB1593CDB`
- Engine: XeTeX `3.141592653-2.6-0.999998`, MiKTeX 26.5
- Invocation: `xelatex -interaction=nonstopmode -halt-on-error -file-line-error`

## Serial passes

Pass 1 exited 0 and produced 466 pages. Its first-run unresolved-reference and
rerun notices are preserved in `Noether_German_NOETH-DE-ED-0001_pass1.log`.

- pass-1 log: 36,009 bytes; SHA-256 `1CD867AF92AB54D94F0685EF4A73693FA7BC41B25A7A5504404F68F94ECD2229`
- pass-1 PDF: 2,654,566 bytes; SHA-256 `B32E11BD3AC66417CA106A271A2E810CD7F91B6FFCEB9CE0D430072AEBB14229`

Pass 2 exited 0 and produced 466 pages. A selected scan found zero instances of
fatal error, emergency stop, undefined control sequence, unresolved
references, rerun request, overfull/underfull box, or missing character.

- pass-2 log: 35,688 bytes; SHA-256 `F01B10A5B7B25E448E60D344CDBBB7835A1BEF5EF518387F89A3CEFF2243DA1A`
- pass-2 PDF: 2,654,407 bytes; SHA-256 `7C24C60B3F691944D7F24FDCDDECDB50A78DB679177255A67F9D2683CAA8A710`

Font-substitution warnings remain inherited build-environment warnings; they
did not prevent output.

## Focused visual QA

Text extraction locates the changed sentence on output page 228. That page was
rendered at 180 dpi and visually reopened. The corrected lambda-indexed module
is present near the footnote continuation; no collision or clipping is visible.

- render: `qa/page_228.png`
- bytes: `365,396`
- SHA-256: `FB274049CCECE25C93EC744C6DBB1DCC3968DF07C3AA56653632D69BC9BEAE72`

This validates compilation and the changed locus. It is not a whole-document
human proofread or a critical-edition certification.

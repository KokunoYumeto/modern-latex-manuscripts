# Build validation

The final editable target is 3,579 bytes, SHA-256
`67DD636D18534E5AB372C7D38E13D98036DC821DF5C3D52FAB5D912395026252`.
A clean two-pass `pdflatex` build produced one A4 page, 284,712 bytes,
SHA-256
`C85E8FA13F035E68FFE98507E8E556952CFFFACEEE9F6F58C45853356C6F3BD8`.

- Sanitized pass 1 log: 6,592 bytes, SHA-256
  `80846B96EA8EEEC47233B32D2C154DB11084D064ED7D21FDB8C4F9E64DAF5F41`.
  Its expected `rerunfilecheck` outline warning is resolved by pass 2.
- Sanitized pass 2 log: 6,431 bytes, SHA-256
  `81C1C152A737D8E541E98DE8D2B87C6DF9018CF8310DC2831915374FB5E89BA7`.
  It contains no TeX/LaTeX error, undefined-reference, rerun, overfull-box, or
  underfull-box diagnostic.
- `PDFINFO.txt`: 710 bytes, SHA-256
  `D794DBD195A2F2516202A320D769623333100150B883A2125998D2625F35DA91`.
- `PDFFONTS.txt`: 2,090 bytes, SHA-256
  `0971A8038216A485903B77588F20C07A5106297667B439677DF09A7B190FC568`.
  All 20 listed fonts are embedded, subset, and Unicode-mapped.

The first draft's enlarged delimiters generated two U+0001 extraction bytes.
Only those delimiters were replaced by source-matching ordinary parentheses.
The final layout extraction is 3,381 bytes, SHA-256
`ECDB67ECCB1BCC24B8CC41C85FA71C49A5CBFCF80E1617D5867BC0F58ADA849A`,
with exactly one formfeed and zero forbidden control bytes.

Raw build transcripts remain internal because they contain local dependency
paths. The full sanitized transcripts retain package, warning, output, and
font-audit context and pass the private-path scan. This is production build
evidence only, not an independent seal.

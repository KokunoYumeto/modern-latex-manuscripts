# Build validation

The final editable target is 3,154 bytes, SHA-256
`1CBB3EF71309ED5C5AABEDA6DB5ED840E2C007B70DE112667A78A4AE5F9B207D`.
A clean two-pass `pdflatex` build produced one A4 page, 292,372 bytes,
SHA-256
`B2973258EE71F71D55CA4F167B74D41AE43388CB498A81B92E3E920F1ED6933D`.

- Sanitized pass 1 log: 3,779 bytes, SHA-256
  `A80A0F874CDBBD9E326C296B2444EE7BF71BBE6E4DFAFFC20027CE1092122167`.
- Sanitized pass 2 log: 3,779 bytes, same SHA-256 because this standalone
  target has no unresolved label state. It contains no TeX/LaTeX error,
  undefined-reference, rerun, overfull-box, or underfull-box diagnostic.
- `PDFINFO.txt`: 684 bytes, SHA-256
  `63674CCAC32C91EC2C02ED850B6C8AD13A9A60EC453BDEA8FEE288A8E80C227A`.
- `PDFFONTS.txt`: 1,995 bytes, SHA-256
  `447ABCCCDC182B2A16F0FA1D43378A0F6D5D564C804D5CCF25F8CCA30456DD3E`.
  All 19 listed fonts are embedded, subset, and Unicode-mapped.

The first visual build's enlarged delimiters generated two U+0001 extraction
bytes. Only those delimiters were replaced by source-matching ordinary
parentheses. The final layout extraction is 2,529 bytes, SHA-256
`E229FB8A83914F093EFB19006FBB60A92CB2330A6010314917900744712B7CAE`,
with exactly one formfeed and zero forbidden control bytes. Exact failed-state
artifact identities remain in the append-only difficulty ledger.

Raw build transcripts remain internal because they contain local dependency
paths. The first purportedly public sanitization left reconstructable wrapped
font-resource paths in both 5,681-byte logs; those failed identities remain in
the append-only difficulty ledger. The repaired sanitizer removes the entire
wrapped font-map/encoding/Type1 resource block and substitutes one public-safe
summary line. The repaired transcripts retain package and output context and
pass checks for user/profile fragments, directory fragments, drive-qualified
paths, and split-line continuations. This is production build evidence only,
not an independent seal.

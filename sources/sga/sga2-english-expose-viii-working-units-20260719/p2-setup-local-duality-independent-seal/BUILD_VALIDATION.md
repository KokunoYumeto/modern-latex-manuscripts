# Build validation

The bounded target builds with two `pdflatex` passes, zero errors, and no
LaTeX warning, overfull-box, or underfull-box hits. The result is one A4 page,
217,162 bytes.

- TeX SHA-256: `FDC13B7A721E456F8AFA5E0B7DB3DE88A5DD4ABE1604513FE3BC47161A31C595`
- PDF SHA-256: `F1F2E78AB82A011D57ABC3EB2E03D3BFB031E4E269434E3F791C8C0B8CF3CE64`
- pass-1 local log SHA-256: `B13AD491F47E75E1D71DE9BF6547F925C9C549B25BEE4AC5D4999E8F62987847`
- pass-2 local log SHA-256: `B13AD491F47E75E1D71DE9BF6547F925C9C549B25BEE4AC5D4999E8F62987847`
- pass-1 sanitized log SHA-256: `CBCF89ED5281D41CE1449D3FC5BB71F4533A840F7C8D9BFA9FB6139CD08E56AE`
- pass-2 sanitized log SHA-256: `CBCF89ED5281D41CE1449D3FC5BB71F4533A840F7C8D9BFA9FB6139CD08E56AE`
- PDF metadata report SHA-256: `03A397094B8E55ACD257F6201C2FBF56C500B5101E9893E936136C2FD2B39C68`
- extracted target text SHA-256: `2B521B55B03C70B5B4FFA08A93B13C894C32F232E2F8CD7D796AFF555628C743`

The first extraction emitted two U+0001 control bytes after `\bigl`/`\bigr`
groups in equations (2.2) and (2.3). Those sizing commands were replaced with
ordinary parentheses, the target was rebuilt twice, and the final extracted
text contains no forbidden non-layout control bytes. Its one form-feed byte is
the ordinary one-page extraction delimiter. The formulas are mathematically
unchanged.

An independent pre-handoff check then found two duplicate equation-anchor
warnings per pass that the earlier validation had missed. Adding
`hypertexnames=false` makes hyperlink destinations unique without changing the
mathematics. The rebuilt logs contain zero warning/error/box hits.

The raw TeX logs name a user-specific local MiKTeX installation and are
explicitly `LOCAL_ONLY`. The proposed public logs are sanitized, and both
contiguous and newline-elided private-path scans pass.

The renewed independent two-pass build also exits zero. Its 217,162-byte PDF
has SHA-256
`5C966BA019AFF03F117DB88045FAEE5664B588436F53FBF4ADEADA762981B336`;
its extracted text and 300-dpi render are byte-identical to the target. The
different PDF hash is limited to expected creation/modification timestamps.

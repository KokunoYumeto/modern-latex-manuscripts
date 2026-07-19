# Independent build validation - SGA2-VIII-C22

The frozen TeX was copied byte-for-byte to an isolated temporary build
directory. Its SHA-256 before the build was
`D8C03D02ADCFEE92D2CB507B02FDEDCC07FE425D201B32AE6F6685A224EB649B`,
equal to the frozen unit TeX.

Two fresh `pdflatex` passes completed successfully. Pass 1 contained only the
two expected first-run cross-reference/rerun warnings; pass 2 contained zero
warnings, errors, overfull boxes, underfull boxes, undefined references, or
missing-character diagnostics. Privacy-sanitized logs are preserved as
`INDEPENDENT_BUILD_PASS1_SANITIZED.log` and
`INDEPENDENT_BUILD_PASS2_SANITIZED.log`; raw logs remain local-only outside
the proposed checkpoint.

The isolated PDF is one unencrypted A4 page, 291362 bytes, SHA-256
`57732B6CF913FBF3F8E48E1E7DDE3D716ED76D105B6110E7E15B438AE4BC4C04`.
All 22 `pdffonts` rows report embedded=yes, subset=yes, and Unicode=yes. Named
destinations include `sourcecorollary.2.2`; the label resolves to 2.2. Extracted
text contains no forbidden C0 controls and includes the complete statement,
condition c), and editor's note.

The frozen checkpoint PDF remains the earlier clean build, 291362 bytes,
SHA-256
`83269A1189F997538B61F07D9DD7A15748BD105A35BBD86817E06F3E508D3B63`.
Its different hash is expected because PDF creation/modification metadata is
timestamped. Independent extraction is text-identical and independent target
renders are byte-identical at both 300 and 600 dpi.

Status: independent build, font, destination, and extraction pass.

# Independent build validation - SGA2-VIII-C23

The frozen TeX was copied byte-for-byte to a clean isolated build directory.
Its SHA-256 was
`45FE67183432E18ADC78B72962A997AB03BEFD4A227F4F873DE13306BB93940F`,
equal to the frozen unit TeX.

Two fresh `pdflatex` passes completed successfully. Pass 1 contained only the
expected first-run label and rerun-file warnings; pass 2 contained zero
warnings, errors, overfull boxes, underfull boxes, undefined references, or
missing-character diagnostics. Complete privacy-sanitized logs are retained as
`INDEPENDENT_BUILD_PASS1_SANITIZED.log` and
`INDEPENDENT_BUILD_PASS2_SANITIZED.log`; raw logs and
the isolated PDF remain local-only and are outside the checkpoint manifest.

The isolated PDF is one unencrypted A4 page, 279208 bytes, SHA-256
`D6403788100F8FCFB0F526BA878486005B303ECE180DF04BC479245FBF67E321`.
All 17 font rows report embedded=yes, subset=yes, and Unicode=yes. Named
destinations include `sourcecorollary.2.3`, all four Roman-item anchors, and
the note anchor. Extracted text contains zero forbidden C0 controls and is
byte-identical to the frozen checkpoint extraction, SHA-256
`366E27432CC949064B24103FCE651BC8F1FFBCE59756F683E0ED140D2B0029BF`.

The frozen checkpoint PDF remains the earlier clean build, 279208 bytes,
SHA-256
`9D53EFB7BFE7063F05E466BE618103FBCCAEA39DF5783A4D3F0CE53E405AF9BB`.
Its different hash is expected because PDF creation/modification metadata is
timestamped. Independent 300 and 600 dpi target renders are byte-identical to
the frozen target renders.

Status: independent build, extraction, font, destination, and reproducibility
pass.

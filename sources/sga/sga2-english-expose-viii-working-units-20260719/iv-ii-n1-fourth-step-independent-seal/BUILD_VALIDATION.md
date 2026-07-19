# Build validation

Target: SGA2_Expose_VIII_Fourth_Step_iv_Implies_ii_Induction_n1_English_SourceAligned.tex.

Two pdflatex nonstop and halt-on-error passes exited zero. Pass 1 contains
only the expected first-build cross-reference/rerun requests. Pass 2 contains
zero LaTeX warnings, package warnings, overfull boxes, underfull boxes,
undefined controls, or missing-character diagnostics. Raw logs remain
local-only. Both public logs replace whitespace-wrapped private user roots
and pass literal and whitespace-elided privacy scans.

- TeX: 3,329 bytes; SHA-256
  C3EE7A146335E9C685D5B0E1AB0264580E6BE61EDAC1A085065625CEE55811EB.
- PDF: 237,675 bytes; one A4 page; SHA-256
  74E7182A077EF8B8BE3B374BA9A02740818FED947665E40442E43D035B5A9543.
- Pass-1 sanitized log: 7,223 bytes; SHA-256
  18DCB5DCBB8D1B747B09397A1104F6A17E9E366F6A2649807A8093F6DF8E8DB7.
- Pass-2 sanitized log: 7,223 bytes; SHA-256
  18DCB5DCBB8D1B747B09397A1104F6A17E9E366F6A2649807A8093F6DF8E8DB7.
- Layout extraction: 3,152 bytes; SHA-256
  198C19CC484BFF826015E3182C6A7C45B6B4EEA39554C10389AED2D81C42525D.
- Target 300-dpi render: 413,329 bytes; SHA-256
  65C14CCD2B73E4021496A6B1256AC28893A14C86F1DDFF6DD83FE10377E2EEF9.

The first target build emitted four U+0001 bytes from four oversized
delimiter pairs. Independent review caught this before sealing. The four
pairs were replaced by source-matching ordinary parentheses; mathematical
grouping is unchanged and all affected evidence above was regenerated. The
repaired extraction contains one expected form-feed delimiter and zero
forbidden non-layout control bytes. It contains the complete n=1 contradiction,
equation numbers (2.7) and (2.8), the printed-page-95 marker, both fraction
identities, and the closing contradiction. Formula typography is assessed
from TeX and rendering because plain-text extraction cannot preserve
overlines and underlines reliably.

All 16 font records are embedded, subset, and Unicode-mapped. The PDF is
unencrypted and searchable. It has descriptive title/author metadata but no
XMP metadata stream and is untagged; those are bounded-review limitations.

An independent isolated two-pass rebuild also exited zero. Its 237,675-byte
PDF SHA-256 is
CBABECF596CC17B2C6522A48BF72BAC5E5435059124F695E8573685026E7BE87;
the difference from the frozen target is timestamp-only. Independent
extraction and 300-dpi rendering are byte-identical to the target. The
independent final TeX-log SHA-256 is
AEE0370DDC8E9E952FA6E7D44BE3183911E462CDE6E439413B6FFD428FFD2846.

Status: repaired production build, extraction, font, public-log privacy, and
independent reproducibility gates pass.

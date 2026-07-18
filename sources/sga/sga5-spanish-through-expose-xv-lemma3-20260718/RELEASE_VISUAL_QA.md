# Release visual QA

- Frozen reader: 304 pages.
- PDF SHA-256:
  `982B996654A1D4459CC6E6AD48D124465528F5E252C89364EE2B912B49C75C91`.
- Expanded target SHA-256:
  `1D7E49A4FFB6691C6D0A57B8D6BC938307373104B4F816500F42329849A7E6BB`.
- Build diagnostics: zero LaTeX/package/pdfTeX warnings, overfull boxes,
  underfull boxes, missing characters, undefined controls, and fatal errors.
- Exact changed/boundary pages inspected: 302--304 at 160 dpi.
- Render-set SHA-256:
  `4C2D8BCFC60950FC8697C3F5DFE6825940B935C54E0539FDA164133F23F245BA`.

The three pages were inspected individually at original render resolution.
The Lemma 1 tail, finite-map point decomposition, alternating exponents,
Leray convergence, excision alternatives, exact sequences, and proper-support
product were readable, unclipped, and free of overlaps or malformed arrows.
Sparse lower space on page 304 is intentional at the Lemma 3 boundary.

Earlier pages retain the bounded QA history recorded in
`evidence/VISUAL_QA_WORKING.csv`; this release does not claim a fresh
whole-volume independent visual certification.

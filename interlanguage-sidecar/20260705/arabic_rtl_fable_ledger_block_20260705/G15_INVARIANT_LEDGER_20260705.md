# G15 Invariant Ledger: Arabic RTL

Status: generated-draft / non-canonical / Arabic-only support.

This ledger implements the Fable G15 invariant table for the Arabic RTL sublane. It records what must survive script direction, register changes, source-use relabeling, and formula-neighboring layout before any Arabic form can move beyond draft support.

The invariant rows are in `G15_INVARIANT_LEDGER_20260705.csv`.

Current result:

- Source-use separation is satisfied for the current package.
- Arabic-only language boundary is satisfied for the current package.
- Eponym/prose split is preserved for the Artinian row.
- Codepoint/extraction QA now checks the six-row Arabic forms and formula-neighboring notes in `interlanguage-sidecar/20260705/arabic_rtl_codepoint_extraction_ledger_20260705/`; it found 8 RTL/LTR formula-boundary risk rows and no embedded bidi-control or Arabic presentation-form drift in the inspected Fable form fields.
- Formula-neighboring RTL layout now has a compiled/rendered probe under `interlanguage-sidecar/20260705/arabic_rtl_tex_pdf_probe_20260705/`; the safer variant is preferred for generated drafts, but `Im*` adjacency and heading layout remain review-sensitive.
- Arabic technical `.tex` source-body recovery and Arabic math-rendering `.dtx` source recovery partially improve the direct-source gap. Round 3 adds GitHub code/repository search evidence plus CTAN/TeX/Khatt provenance, but no direct algebra-specific Arabic TeX/source package was recovered; algebra-specific TeX/source-package and specialist invariant/covariant source-body gaps remain active.

No native review, accepted terminology, source certification, license clearance, gate promotion, final status, or translation completion is claimed.

# Diagram audit through SGA 6 source page 353

Audit scope: cumulative SGA 6 bilingual rebuild through source scan page 353, i.e. through Exposé V, source pages 331--353 as currently staged.

Method: rendered the original source scan cumulatively through source page 353, made page-contact passes over the full range, then spot-checked high-resolution original pages against the corresponding English and French TeX/PDF surfaces.  The TeX surfaces contain 88 `tikzcd`/TikZ diagram blocks in each language, plus aligned displayed formula blocks where the original has formula arrays rather than commutative diagrams.

Result: one diagram needed correction.  On original source scan page 99, Exposé I, Lemma 1.4.1 proof, the octahedron in `K(C_X)` had been rendered too schematically in the previous reader surface: it omitted the node `G'` from the octahedron display and suppressed several octahedral arrows.  The English and French cumulative TeX/PDFs now contain a faithful diagram with the six objects `E_X`, `E'`, `F_X`, `M[-n]`, `G_X`, `G'`, the distinguished-triangle arrows, the curved `+1` arrows, and the marked triangle `(*)`.

Correction artifacts included:

- `DiagramCorrection/SourceScan/SGA6_source_page_099_original.pdf`
- `DiagramCorrection/RenderChecks/Source_page_099_octahedron.png`
- `DiagramCorrection/English/SGA6_Expose_I_pages_092_110_English_diagram_audited.pdf`
- `DiagramCorrection/French/SGA6_Expose_I_pages_092_110_French_diagram_audited.pdf`
- corrected cumulative `English/SGA6_English_pages_001_353.pdf`
- corrected cumulative `French/SGA6_French_pages_001_353.pdf`

Other diagram-bearing or diagram-candidate pages checked in the original source included: 48, 81, 93, 94, 97, 98, 99, 100, 101, 104, 105, 106, 108, 110, 111, 114, 120, 121, 124, 126, 127, 130, 132, 138, 143, 144, 164, 177, 178, 183, 185, 204, 229, 231, 232, 233, 234, 235, 238, 240, 241, 244, 246, 250, 253, 254, 259, 264, 290, 297, 298, 301, 308, 309, 311, 314, 317, 321, 324, 328, 334, 336, 350, 351. No other missing diagram was found in this audit pass.

Continuation anchor remains: SGA 6 source scan page 354, Exposé V, Definition 6.2.

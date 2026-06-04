# N34 p3 ES/JA

Contents: Spanish and Japanese translations of Noether Paper 34 §§15--26, completing Paper 34.

Package structure is path-safe and strict: one root folder, then subfolders. Maximum internal path length including root at build time: 50 characters.

Subfolders:

- `00_doc`: audit, build, global, and continuation notes.
- `01_work`: standalone Spanish/Japanese TeX and PDFs for the current block.
- `02_cum`: cumulative Spanish/Japanese TeX and PDFs through Paper 34 complete.
- `03_meth`: cumulative methodology, glossary, special-character aids, and nested method handoff ZIP.
- `04_src`: German/English control TeX/PDF and scan witness.
- `05_logs`: build logs.
- `06_man`: manifests.
- `07_rend`: render checks.

Important audit point: §25 includes the source-visible product table in editable TeX, using the existing Paper 34 product-table patch. It is included in the Spanish/Japanese outputs and the patched German/English controls.

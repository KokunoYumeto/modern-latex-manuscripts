# Cayley Collected Mathematical Papers - Clean Per-Volume Build

Produced 2026-05-29 by a local repair pass in response to the Cayley repair
packet from Codex.

## What's here

For each available volume of Arthur Cayley's Collected Mathematical Papers,
this directory contains:

- `Cayley_Collected_Mathematical_Papers_<label>.pdf` -- single compiled PDF
- `Cayley_Collected_Mathematical_Papers_<label>.tex` -- single master LaTeX
  source (unified preamble + concatenated chunk bodies)
- `sources_tex_<label>/` -- raw per-chunk source TeX files (50-page chunks
  from source typesetting work, used as the source for the master)

Labels: `Front_Matter`, `Vol_I`, `Vol_II`, `Vol_III`, `Vol_IV`, `Vol_V`,
`Vol_VI`, `Vol_VII`, `Vol_IX`, `Vol_X`, `Vol_XI`, `Vol_XII`, `Vol_XIII`.

`MANIFEST.csv` and `MANIFEST.json` summarize all volumes, page counts,
byte sizes, and SHA-256 hashes.

## Status: 13 of 14 volumes clean and complete

All 13 produced PDFs pass the leak audit: **zero raw TeX commands leaking
into rendered prose/math** (the defect the repair packet was built to fix).
The previously-published "Modern LaTeX Draft" PDFs contained literal `\frac`,
`\partial`, `\delta`, etc. -- all eliminated here.

Total: 6,389 rendered pages, 22.8 MB.

## Missing material

- **Vol. VIII**: no available TeX source exists anywhere on disk; volume cannot
  be produced from current local material.
- **Vol. II, pages 105--156**: chunk missing from source set; the rest of
  Vol. II is present and clean. The master TeX has a `Repair TODO` section
  flagging the gap.
- **Vol. XII, pages 101--150**: same situation; rest of vol. is present.

## How the rebuild works

1. The source source-generated chunk TeX files are pulled from
   `local workspace\Documents\Papors\Chatnotes\CHat translates and clean\source system\source system 7\source system 7\latex_typesetting_CONTINUED_WORK\cayley\<volXX>\`
2. For each volume, a per-volume master TeX is built: a unified preamble
   (with fallback `\providecommand` definitions for the source system's non-standard
   commands like `\tome`, `\page`, `\canont`, `\Disc`, `\asterism`, etc.),
   followed by each chunk's body wrapped with `\clearpage`.
3. pdflatex is run once per master to produce the per-volume PDF.

If a chunk has a structural TeX defect (e.g., the missing `\]` in
vol06_pages_001_050), a patched copy is dropped into
`sources_tex_<label>/` and the build script prefers that local copy over
the source original.

## Why the old "Modern LaTeX Draft" PDFs were broken

The old PDFs were NOT produced by compiling these TeX chunks. They appear
to have been generated from extracted/converted text where LaTeX math
commands rendered as literal text instead of math. Recompiling the
underlying clean source system TeX yields clean output.

## Files for Codex pickup

The PDFs + master TeX files in this directory are ready for direct upload
to:
- GitHub `modern-latex-manuscripts` repo (one PDF + one TeX per volume)
- Zenodo Cayley satellite record (one PDF per volume; include the master
  TeX as supplementary)

The previously-broken "00 Cayley ... Volume IV Modern LaTeX Draft.pdf"-style
filenames should be REPLACED with the new clean per-volume PDFs.

## Build scripts

The `_*.py` scripts are reproducibility evidence -- not needed by Codex.

- `_build_inventory.py`: scans source files, picks canonical chunks
- `_build_master_tex.py`: writes per-volume master TeX with unified preamble
- `_compile_all.py`: runs pdflatex on each master
- `_check_leaks.py`: counts leaked `\command` text in rendered PDF
- `_audit_chunk_pdfs.py`: per-chunk leak inspection (historical)
- `_build_manifest.py`: writes MANIFEST.csv / MANIFEST.json
- `_inventory.json`, `_master_tex_summary.json`,
  `_compile_all_report.json`, `_chunk_leak_audit.json`: build artifacts

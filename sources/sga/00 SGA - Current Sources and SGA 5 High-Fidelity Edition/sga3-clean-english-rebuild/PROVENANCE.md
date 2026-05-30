# SGA 3 English clean rebuild provenance

This folder preserves the working material for the SGA 3 English clean rebuild.

Local toolchain used:

- Python 3.13 for the repair script and file packaging.
- MiKTeX XeLaTeX for two-pass compilation.
- PyMuPDF/fitz for page counts, text sweeps, and PDF validation from the organizing scripts.
- DejaVu Serif, DejaVu Sans, DejaVu Sans Mono, and Cambria Math as local font substitutions.

Repair scope:

- Rebuilt an existing English translation snapshot into a continuous PDF reader.
- Replaced syntax-highlight/code-style formula blocks with normal text-flow blocks.
- Neutralized color-token wrapper commands from the converted TeX source.
- Left full mathematical normalization of every inline formula for later work.

The top-level reader is useful for reading and continuation, but it is not a final proofread critical edition.

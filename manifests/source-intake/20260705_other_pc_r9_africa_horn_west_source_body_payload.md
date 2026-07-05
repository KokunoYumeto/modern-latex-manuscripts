# Other-PC R9 Africa/Horn/West Source-Body Payload

- Date: 2026-07-05
- Source branch commit: `origin/codex/noether-pc-20260629` at `7b3ed05b8`
- GitHub mirror: `interlanguage-sidecar/20260705/other_pc_r9_africa_horn_west_source_body_payload_20260705/`
- Zenodo-facing artifact: `publish_staging/interlanguage-methodology/20260705_other_pc_r9_africa_horn_west_source_body_payload/OtherPC_R9_Africa_Horn_West_SourceBodyPayload_20260705.zip`
- Bytes: 7,843,748
- SHA256: `A3601253C8C52493E79FBCAB0BD20C4F1826167AF7DDA050E549A931F248631D`
- ZIP entries: 27

## Contents

R9 Africa/Horn/West source-body/source-witness payload from the other PC.

Included bodies:

- Hausa (`ha`) source archive: `FazamMV23_HausaMath_4c35f0abeb88.zip`
- Hausa (`ha`) mathematical-prose PDF witness: `hawiki-Lissafi-20200722.pdf`
- Tigrinya (`tig`) arXiv source archive: `arxiv_2601_03403_tigrinya_number_verbalization_eprint.tar`
- Tigrinya (`tig`) GitHub source archive: `github_fgaim_tigrinya_numbers_main.zip`
- Extracted Tigrinya arXiv TeX/build files, including `main.tex`, `main.bbl`, `icml2025.sty`, `icml2025.bst`, and fonts.

## Archive-Maintenance Repair

The side-branch commit was useful, but had one packaging defect: its manifest tracked `main.bbl`, while the committed tree omitted it because `.bbl` is globally ignored. This main import recovered `main.bbl` from the included arXiv tar before packaging. `icml2025.bst` was also restored from the tar to preserve the manifest hash bytes after line-ending normalization.

## Classification

Source-canon/provenance support payload with actual bodies and logs.

## Caveat

Not native review, not accepted terminology, not translation completion, not source-fidelity certification, not publication readiness, not a critical edition, and not blanket license clearance.

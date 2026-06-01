# BATCH_REPORT — sensor_fusion_2506.19769

**Source**: arXiv:2506.19769 — Ruan et al., *A Survey of Multi-sensor Fusion Perception for Embodied AI: Background, Methods, Challenges and Prospects* (2025).
**License (per fetched_source_inventory.csv)**: arXiv source; CC-license to verify against arXiv listing.
**Translator**: auxiliary local run (Anthropic), lane lead: local project.
**Date**: 2026-06-01.
**Status**: Complete end-to-end translation of all 9 source sections.

## Output files
- `0_main.tex` — XeLaTeX + polyglossia (ukrainian) preamble, IEEEtran journal class preserved.
- `1_abstract.tex` … `9_Conclusion.tex` — section-by-section Ukrainian.
- `figure/` — figures copied verbatim from source (binary PDFs; captions translated in section files).
- `IEEEtran.cls`, `0_main.bbl` — copied from source for buildability.

## Build
```bash
cd sensor_fusion_2506.19769
xelatex -interaction=nonstopmode 0_main.tex
xelatex -interaction=nonstopmode 0_main.tex
```
(No bibtex run needed; bbl is provided. If you regenerate references you'll need the original `ref.bib`, which was not in the fetched chunk for this paper — only `0_main.bbl` was present.)

## Translation policy applied
- All equations, math symbols, labels, refs, `\cite{}` keys, figure includes preserved verbatim.
- Author block kept in original Latin (institutional affiliations untranslated).
- Section/subsection/caption text translated.
- IEEEkeywords translated.
- `\IEEEPARstart{I}{n}` adapted to `\IEEEPARstart{З}{а}` for the Ukrainian opening "За останні роки".

## Terminology decisions (extend the seed glossary)
Where the seed glossary did not cover a term, I made the following choices for consistency:
| EN | UK | Notes |
|---|---|---|
| multi-sensor fusion perception (MSFP) | багатосенсорне сприйняття на основі злиття даних (MSFP) | MSFP kept as Latin acronym at first use |
| embodied AI | втілений ШІ | "втілений" = embodied, anchors to corpus usage |
| LLM | LLM (велика мовна модель) | Latin acronym preserved; gloss at first use |
| MM-LLM | MM-LLM (мультимодальна LLM) | Same pattern |
| LiDAR | LiDAR | kept Latin |
| mmWave radar | радар міліметрового діапазону (mmWave) | |
| BEV (bird's-eye view) | BEV (вид з висоти пташиного польоту) | acronym dominates in literature |
| point cloud | хмара точок | |
| voxel | воксель | |
| bounding box | обмежувальна рамка | |
| 3D object detection | 3D-детектування об'єктів | |
| semantic segmentation | семантична сегментація | |
| occupancy prediction | передбачення зайнятості | |
| depth estimation | оцінювання глибини | |
| query (dense/sparse/hybrid) | запит (щільний/розріджений/гібридний) | |
| self-attention | самоувага | |
| cross-attention | перехресна увага | |
| deformable attention | деформівна увага | |
| modality / multi-modal | модальність / мультимодальний | |
| ego-motion | его-рух (also: власний рух) | first form is more compact, used throughout |
| ROI (region of interest) | область інтересу (ROI) | acronym at first use, then ROI |
| AIGC | AIGC | kept original; contextually glossed |
| RAG | RAG | kept original |
| transformer | трансформер | |
| Chain-of-Thought | ланцюгове міркування (Chain-of-Thought) | English at first use |
| handshake (communication) | "рукостискання" (handshake) | quoted at first use |
| zero-shot learning | zero-shot learning | technical term left in English |
| swarm robotics | роботи у складі рою / ройова робототехніка | both forms used contextually |
| frustum (PointNets) | зрізана піраміда (frustum) | |
| feature blurring | "розмиття ознак" | quoted on first use |
| range view | range view | left in English (technical projection name) |

## TODOs / `[[CHECK: ...]]` flags
- `[[CHECK: term-stability]]` — "оцінювання глибини" vs "оцінка глибини": I used "оцінювання" consistently (per seed glossary for "estimation"); native review for register would be good.
- `[[CHECK: term-stability]]` — "сприйняття зайнятості" — chose "передбачення зайнятості" for "occupancy prediction"; check against any preexisting Ukrainian robotics corpus.
- `[[CHECK: math]]` — Section 3.3 (background) "Depth Estimation" uses $\mathcal{R}^{M \times N}$, which in the source is a non-standard typesetting (should usually be $\mathbb{R}^{M\times N}$). Left as in source to preserve fidelity.
- The `ref.bib` was not included in the fetched arXiv chunk; only `0_main.bbl`. If a regenerated bibliography is needed, the .bib must be fetched separately from arXiv.

## Glossary additions proposed for `UKRAINIAN_TERMINOLOGY_GUIDE.md`
- `multi-sensor fusion perception (MSFP) → багатосенсорне сприйняття на основі злиття даних` — extend the "sensor fusion" entry
- `embodied AI → втілений ШІ`
- `point cloud → хмара точок`
- `voxel → воксель`
- `bird's-eye view (BEV) → вид з висоти пташиного польоту (BEV)`
- `occupancy prediction → передбачення зайнятості`
- `self-attention → самоувага`
- `cross-attention → перехресна увага`
- `bounding box → обмежувальна рамка`
- `ego-motion → его-рух`

## Coverage delta vs web model session
web model GPT-5.5 Pro session 02 lists this paper as **not in its pipeline**. This translation is wholly additive.


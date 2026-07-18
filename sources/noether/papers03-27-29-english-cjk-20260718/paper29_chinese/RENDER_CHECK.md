# Paper 29 rendered visual QA

Renderer: Poppler `pdftoppm`, PNG output at 150 dpi.

| Edition | Render directory | Pages | Individually inspected | Final result |
|---|---|---:|---:|---|
| sealed German control | `visual_inspection/de/` | 5 | 5 | pass |
| `zh-Hans-CN` | `visual_inspection/zh-Hans-CN/` | 4 | 4 | pass |
| controlled `zh-Hant` | `visual_inspection/zh-Hant-controlled/` | 4 | 4 | pass |

All 13 final pages were inspected at original render resolution. No clipping, overlap, blank/duplicate page, missing glyph, displaced formula, broken title/author block, or unreadable footnote was found in the frozen builds.

## Defects found and repaired during QA

1. OpenCC produced uncommon `一箇` in three controlled-Hant prose loci. These were normalized to controlled `一個` before the final build.
2. Footnote 6 initially rendered as though attached to the following `可推出`; its marker was moved into the exact displayed field inclusion in both scripts.
3. The Hilbert note was initially attached to the first displayed definition of `\mathfrak T`; it was moved to the source's post-derivation second definition.
4. The characteristic-`p` premise had one source emphasis locus split into two target loci, and `endliche` had been broadened to the whole module-generating-system phrase. Both were repaired; final emphasis counts are 22/22/22.

Every target affected by a correction was rebuilt twice and all of its pages were rerendered and reinspected. Contact sheets are retained for navigation, but the pass is based on the individual page images.

Visual inspection is internal production QA, not external/community validation.

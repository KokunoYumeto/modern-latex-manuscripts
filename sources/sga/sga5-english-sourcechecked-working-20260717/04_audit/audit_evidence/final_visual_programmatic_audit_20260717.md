# SGA 5 English final PDF: programmatic and visual QA audit

**Audit date:** 2026-07-17 (Europe/Berlin)  
**Scope:** read-only audit of the final English workpass PDF, its two final build logs, the 309 page renders, and the regenerated contact sheets.  
**Audited PDF:** `03_projects/language_management/english_germanic/03_working_translations/sga5_english_sync_workpass/SGA5_English_sync_workpass.pdf`

## Verdict

The audited 309-page PDF is render-complete and visually usable. No blank page, clipped formula, missing diagram, broken glyph, page-size anomaly, or fatal build diagnostic was found. The three objectively sparse pages are intentional end material: the Exposé III bibliography tail (PDF 88) and the two-page tail of the terminological index (PDF 308–309).

The initial contact-sheet audit found four all-white contact-sheet files even though the underlying page renders were populated. Those four files were subsequently regenerated, and all sixteen sheets were re-encoded as 8-bit RGB PNGs. The refreshed sheets were then rechecked both programmatically and visually. All sixteen are now populated; the visual-evidence defect is cleared.

This is a rendering/package audit, not an independent retranslation or a substitute for the source/formula ledgers. Publication freeze, payload upload, and Zenodo coordination remain with the parent English manager.

## Frozen content artifacts

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| `SGA5_English_sync_workpass.pdf` | 2,054,026 | `176759209CD284F1DD6D3E26D0C7600EC146AB01FAA637BF6F6BB97BFAA396A4` |
| `SGA5_English_sync_workpass.tex` | 796,755 | `3CC5204680B2A2CE92FDF09401AB1A4654F9E0A4B0ED932D110FC0B1B024720F` |
| `BUILD_FINAL_PASS1_20260717.log` | 49,352 | `4AEE7355405CCA10390DB2105F981F24E43DF9B02C0006DCADCA9DD16419F2C6` |
| `BUILD_FINAL_PASS2_20260717.log` | 49,352 | `4AEE7355405CCA10390DB2105F981F24E43DF9B02C0006DCADCA9DD16419F2C6` |
| `BUILD_FINAL_PASS1_20260717.console.txt` | 22,988 | `193023D40F6C77CDA92EEEC0ECDF708206B2DF1FAE5CCF921BBA727453E50BE6` |
| `BUILD_FINAL_PASS2_20260717.console.txt` | 22,988 | `193023D40F6C77CDA92EEEC0ECDF708206B2DF1FAE5CCF921BBA727453E50BE6` |

Both final passes produced the same 309-page, 2,054,026-byte PDF; their `.log` files are byte-identical and their console captures are byte-identical.

## PDF structure and metadata

- Page count: **309**.
- Encryption: **none**.
- Page geometry: all 309 MediaBoxes are exactly `(0, 0, 612, 792)` points (US Letter); no outlier geometry or rotation defect was found.
- Page-render inventory: exactly **309** PNGs, each **850 × 1100** pixels.
- Producer: `MiKTeX pdfTeX-1.40.29`.
- Creator: `LaTeX with hyperref`.
- Creation and modification date: `D:20260717223918+02'00'`.
- PTEX banner: `This is MiKTeX-pdfTeX 4.27.0 (1.40.29)`.
- Title, author, subject, and keyword metadata fields are empty. This does not affect content or rendering, but it is a discoverability/citation caveat for the publication manager to accept or correct before deposit.

## Blank and near-blank page audit

Method:

1. Extract text from every PDF page with `pypdf`, strip surrounding whitespace, and count characters.
2. Open every original 850 × 1100 page PNG with Pillow, convert to 8-bit grayscale, and count the share of pixels with value `<250` as a conservative ink proxy.
3. Treat a page as a near-blank candidate if extracted text is below 600 characters **or** ink is below 2%. Treat ink below 0.5% or zero extracted text as a blank-page alarm.
4. Inspect every candidate at original resolution.

Aggregate results:

| Measure | Minimum | Median | Maximum |
|---|---:|---:|---:|
| Extracted characters | 207 | 1,762 | 4,171 |
| Ink proxy | 0.615615% | 5.486096% | 12.844278% |

- Zero-text pages: **0**.
- Pages below 0.5% ink: **0**.
- Near-blank candidates: exactly **3**.

| PDF page | Extracted characters | Ink proxy | Visual explanation | Verdict |
|---:|---:|---:|---|---|
| 88 | 429 | 1.385241% | Intentional tail of the Exposé III bibliography/reference note; six bibliographic lines plus folio. | Pass; intentional sparse page. |
| 308 | 586 | 1.797112% | Terminological index continuation, with entries and cross-references in two columns. | Pass; intentional sparse index page. |
| 309 | 207 | 0.615615% | Final terminological-index tail, with the remaining entries and folio. | Pass; intentional sparse final page. |

PDF 307, the preceding index page, is also relatively open but does not meet the near-blank rule (817 characters; 2.439465% ink). The content sequence across 307–309 is coherent.

## Build-log diagnostics

Each final pass reports:

- Fatal TeX errors: **0**.
- Lines beginning with `!`: **0**.
- Undefined-reference, rerun-required, or missing-character diagnostics: **0**.
- Underfull boxes: **0**.
- LaTeX font warnings: **3**.
- Overfull boxes: **9**.
- Output: **309 pages, 2,054,026 bytes**.

The three font warnings are `Command \scriptsize invalid in math mode` at TeX input lines 3258, 3485, and 5740, mapping to PDF 63, 67, and 118. Each corresponding diagram/formula page was inspected at original resolution; labels are present, readable, and do not collide or clip.

The nine overfull diagnostics map to PDF 4, 45, 53, 73, 82, 85, 111, 115, and 266. The reported excesses are respectively 38.56181 pt, 10.81624 pt, 11.46852 pt, 23.09824 pt, 0.29135 pt, 11.65924 pt, 5.13628 pt, 8.09499 pt, and 15.1008 pt. Every affected page was visually inspected. Some lines extend into the available margin, but no text crosses the physical crop, disappears, overlaps another object, or becomes unreadable.

## High-risk page inspection

The companion CSV records page metrics and the same page-level verdicts. “Pass” below means the specified restored content is visibly present and the page has no clipping, overlap, missing glyph, malformed arrow, or unintended blank region.

### Global and diagnostic sample

| PDF page | Trigger | Visual finding |
|---:|---|---|
| 4 | Required sample; 38.56181 pt overfull | Dense Exposé I opening matter remains inside the physical page; underline and final paragraph are intact. Pass. |
| 45 | 10.81624 pt overfull | Künneth-formula paragraph is complete and readable. Pass. |
| 53 | 11.46852 pt overfull | Long displayed formula is complete; no right-edge loss. Pass. |
| 63 | `\scriptsize` warning | Large diagram (4.4.2) and all labels are fully rendered inside the page. Pass. |
| 67 | `\scriptsize` warning | Diagram (4.4.6) is complete and legible. Pass. |
| 73 | 23.09824 pt overfull | Long composition formula is readable with no crop loss. Pass. |
| 82 | 0.29135 pt overfull | No visible defect. Pass. |
| 85 | 11.65924 pt overfull | Residue formulas and adjacent prose are complete. Pass. |
| 111 | 5.13628 pt overfull | Extension-of-scalars display and diagram are complete. Pass. |
| 115 | 8.09499 pt overfull | Square `(*)`, displays (2)–(3), and dependent prose are complete. Pass. |
| 118 | Required sample; `\scriptsize` warning | Diagrams/formulas 5.12.2–5.12.5 and the start of §5.13 are present and clean. Pass. |
| 266 | 15.1008 pt overfull | Trace-formula material is within the physical page and readable. Pass. |

### Exposé I scan-backed anchors

| French/source printed page | PDF page | Restored structure checked | Visual finding |
|---:|---:|---|---|
| 38 | 23 | Cartesian square `U ← U′` with vertical `i` and `i′` arrows down to `X` and `X′`. | All four objects and arrows render in the intended orientation. Pass. |
| 48 | 28 | Two distinguished triangles with cyclic arrows and `+1` on the source edge. | Both triangles are complete; arrow cycles and labels are visible. Pass. |
| 71 | 41 | The `i′` arrow from `U` to `Y′`, oriented upward-right. | Arrow and label render correctly. Pass. |

### Exposé III B changed areas

| PDF page | Anchor checked | Visual finding |
|---:|---|---|
| 94 | §2.1 diagrams (1)–(4), with squares (1) and (4) and the square-(1) reference. | Complete and clean. Pass. |
| 111 | §5.9 extension-of-scalars formula and diagram. | Complete and clean. Pass. |
| 115 | §5.10.9 square `(*)`, displays (2)–(3), and dependent prose. | Complete and clean. Pass. |
| 118 | 5.12.2–5.12.5 diagrams and §5.13 transition. | Complete and clean. Pass. |
| 121 | Module categories and (6.2.3), including the second argument. | Complete and clean. Pass. |
| 124 | §6.6 tensor bases `A`, `Λ`, `A`, and the final `A` base. | Complete and clean. Pass. |
| 135 | Proposition 6.23: connected `(fc_1)^{-1}(V)` and inclusion `d_1^{-1}(V) ⊂ d_2^{-1}(V)`. | Complete and clean. Pass. |

### Exposé VII late repairs

| PDF page | Restored content checked | Visual finding |
|---:|---|---|
| 190 | Source p. 286 projective-bundle arrow `c: μ_S^{⊗-1}[-2] → Rp_*(A_P)`. | Complete and clean. Pass. |
| 197 | Formula (3.8.1), including `H^{2i}`. | Complete and clean. Pass. |
| 198 | Exponential sequence with `t ↦ 2iπt` and the mod-`ν` exponential. | Complete and clean. Pass. |
| 207 | `Q(S/T,L)` with `R^n`. | Complete and clean. Pass. |
| 214 | Corollary 7.4 checked cotangent bundle in (7.4.1) and (7.4.2). | Complete and clean. Pass. |
| 217 | Lemma 8.2(c) omitted-map display. | Restored display is present and clean. Pass. |
| 228 | (9.7.1) `c_d`, checked `E`, barred `ξ`; (9.7.4) `β_*`/`α_*`; and (9.8.1) `v_*`. | Complete and clean. Pass. |
| 229 | Full `β_*δ_*` derivation, D1 sentence, (9.8.5), (9.8.6), and adjacent diagram. | Complete and clean. Pass. |
| 230 | Continuation, D2-related diagram, and theorem. | Complete and clean. Pass. |

### Exposés X, XII, and XV

| Exposé | PDF page | Restored/high-risk content checked | Visual finding |
|---|---:|---|---|
| X | 248 | Proposition 3.2 K-theory bullets render as `K_•`, not an asterisk. | Pass. |
| X | 254 | `Sw_{y′}` proof and leading equalities (4.5.1)–(4.5.3). | Pass. |
| X | 260 | Reverse arrow in (7.6) and restored triangle (7.8). | Pass. |
| X | 261 | Coproduct `∐_{y∈Y} F_y`. | Pass. |
| X | 263 | Triangles (7.15), (7.16), and the Cartesian square. | Pass. |
| X/XII | 264 | End of Exposé X and Exposé XII title transition. | Transition is complete and clean. Pass. |
| XII | 266 | Trace-formula page and overfull-log site. | Complete, readable, and unclipped. Pass. |
| XII | 271 | Dense local calculation. | Complete and clean. Pass. |
| XII | 276 | §6.2 local terms. | Complete and clean. Pass. |
| XII/XV | 282 | Exposé XII tail and Exposé XV title transition. | Transition is complete and clean. Pass. |
| XV | 287 | Map type `π_{Spec(A)/S}: Spec(A)^{(p)} → Spec(A)`. | Complete and clean. Pass. |
| XV | 289–290 | Frobenius adjunction; explicit “with `g^*` left adjoint to `g_*`”; corrected `(Fr^*_{-/})^{-1}` context. | Complete and clean across both pages. Pass. |
| XV | 298 | Finite punctual reduction `X = Spec(F_{q′})`. | Complete and clean. Pass. |
| XV | 299 | First noetherian reduction `j = 1,…,r−1`. | Complete and clean. Pass. |
| XV | 300 | Dense Lefschetz calculation. | Complete and clean. Pass. |
| XV | 302 | System construction and lemma. | Complete and clean. Pass. |
| XV | 303 | Dense continuation page. | Complete and clean. Pass. |
| XV/index | 305 | Start of the terminological index after Exposé XV. | Transition is complete and clean. Pass. |

## Contact-sheet audit after regeneration

All files below are 8-bit `RGB` PNGs. Sheets 001–300 are 1008 × 1610; the nine-page final sheet is 1008 × 990. The ink proxy is computed on grayscale pixels `<250`, as for individual pages. The four sheets that were initially all white—141–160, 161–180, 201–220, and 301–309—were individually reopened at original resolution after regeneration and visibly contain their expected page thumbnails.

| Contact sheet | Bytes | Ink proxy | SHA-256 | Verdict |
|---|---:|---:|---|---|
| `contact-001-020.png` | 855,312 | 15.150781% | `0B3A25CFCE50EBC86A4FABA47A98436978E4394811F8F969DF19FD98E87DE0D5` | Populated; pass. |
| `contact-021-040.png` | 879,028 | 15.572069% | `10B2174EFCF3ABAAE745A9CEF4C717367D3B54E3C295B44DF986CB4E8662C9A6` | Populated; pass. |
| `contact-041-060.png` | 785,348 | 13.445480% | `85A24853F7F4C3A4F6FE8D0BD676D80D400F4AAB516CA37805A84B7D36AEE8F3` | Populated; pass. |
| `contact-061-080.png` | 831,895 | 14.284359% | `654DF6BE08793860148192691EA36A828C358FA720CAC2E0A56B421BA723215E` | Populated; pass. |
| `contact-081-100.png` | 862,185 | 15.290841% | `CD49B60EA5AE9EFD6E489F130BB1EB32ED71F3A1436E266000BEAAF7E485955E` | Populated; pass. |
| `contact-101-120.png` | 835,583 | 14.618949% | `56090B6B4C7F319FADAB2ECC72821C787136ECB7C1983125671A1074D718FFFA` | Populated; pass. |
| `contact-121-140.png` | 715,884 | 11.693841% | `CB9DB23A393E72F9D1D309799B02BC709459A47487B75F41FA98826CCFEB9633` | Populated; pass. |
| `contact-141-160.png` | 744,987 | 12.569321% | `2EE80D3B02330944F488D1ED4CCCA1C535C147271E051F585B599D6B00109A1D` | Regenerated; visibly populated; pass. |
| `contact-161-180.png` | 784,950 | 13.448622% | `DD4417D13BF668EFB10D6E2D88D506BC3D6634D5BA11FAE577D608147FE2A0B4` | Regenerated; visibly populated; pass. |
| `contact-181-200.png` | 730,532 | 12.182540% | `7B338117D079B507F3CE74D177616CE4B414A7E3FFA2CC48566414EB57B2DFB9` | Populated; pass. |
| `contact-201-220.png` | 771,966 | 12.916174% | `3BE929B3C43FB9F5FBBE20902C896DF5D157DA3B14E24766C92AF251A55DE4B0` | Regenerated; visibly populated; pass. |
| `contact-221-240.png` | 708,640 | 11.674492% | `A53EDB7E3BEF7980AFF1DBC53E3FE240501865FF7E6B5DF076AB415FC1EFDAD1` | Populated; pass. |
| `contact-241-260.png` | 776,838 | 13.196848% | `20A08B176F22A8772CA62E4EF68D9B09AFC0CADC3A17B76F51135D430A3E13E3` | Populated; pass. |
| `contact-261-280.png` | 689,112 | 10.882444% | `CA3701C30A648D491022D5F925BB5A6721AC4480B8C9300327E7CC30825B0582` | Populated; pass. |
| `contact-281-300.png` | 800,662 | 13.710133% | `531E91625835D17D74E745A77ED642FD3A8D435AABBF81BB4D10DDD0D37B5C9F` | Populated; pass. |
| `contact-301-309.png` | 308,471 | 8.588564% | `695F52BF0B33F8004AD6C8477F60F5E1871C4C3E4D60A254424F15438F95A2F2` | Regenerated; visibly populated, including sparse index tail; pass. |

## Residual caveats

1. Empty title/author/subject/keyword PDF metadata is a publication-quality caveat, not a content-render blocker.
2. The logged overfull boxes are real TeX diagnostics. Visual inspection shows no physical-page clipping or collision, so they do not block this PDF, but the exact log entries must remain in the publication evidence rather than being reported as a warning-free build.
3. This audit does not claim that visual cleanliness alone proves source-critical synchronization. That proof depends on the exposé/page/source-correction ledger, formula comparison, terminology/rejected-choice ledger, and scan-backed receipts maintained elsewhere in the task package.
4. No external upload, DOI minting, or Zenodo mutation was performed in this audit.

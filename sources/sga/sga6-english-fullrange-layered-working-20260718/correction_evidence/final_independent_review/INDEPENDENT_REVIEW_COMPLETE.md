# Independent review of the complete layered SGA 6 English reader

Review date: 2026-07-18  
Review scope: final complete-reader integration, build, coordinates, seam, macro state, selected repaired-prefix renders, and equivalence to the independently reviewed standalone tail. Production TeX/PDF and the French workpass were not edited by this reviewer.

## Verdict

**PASS for the frozen complete layered working-edition integration.** No blocking defect remains in the reviewed assembly, final clean-auxiliary build, source-coordinate closure, Exposé IX/X seam, tail macro reset, physical terminal, targeted repaired-prefix rendering, or sampled tail equivalence.

This verdict is deliberately narrower than publication certification. The prefix remains inherited and only partially source-synchronized outside the expressly adjudicated repair gates; idx663--702 and the unindexed terminal matter remain a scan-checked English draft pending Claude's French-workpass corrections. The reader must therefore retain its layered-authority and not-publication-ready labels.

## Frozen final artifacts

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| `SGA6_English_Complete_Layered_WorkingEdition.tex` | 3,917 | `7E731468367BBC27A37BC224BBBEE3FAB37A3852FC76BB541A1AF36EF76D50F3` |
| `SGA6_English_Complete_Layered_WorkingEdition.pdf` | 2,565,870 | `F8B1E15754BEB5C83CF2A47B261D6F9F907DE5B7E8A6ED4DF311C624E38C7B8E` |
| final prefix fragment | 812,912 | `3FE03C89BA0662A61607CDE80DDB24BC4683FA37C30C1DA580908CFAD186F68C` |
| tail macro-state reset | 3,943 | `7EB2EF408B4541FD6AE5CA295B00049601B44A789F8696D48FFEC9C4310F29F2` |
| synchronized tail body | 106,090 | `613006848EC8968D991FE2556AEC1B49AF29EB268FCA8C9C559DD61EF238C1A4` |
| independently reviewed standalone tail PDF | 1,028,065 | `7B1280140ADE4BC7FBA152F3BA9006EA6AA1E288FBADB9740D2980085098164E` |

The French workpass remained unchanged at 1,318,579 bytes, SHA-256 `77703F2D7E8FF9000C2C1E7320A903A48ADE00BF62C8F5F240FF88C42ED82703`.

## Prefix lineage and post-seal integration repair

The reviewed lineage is coherent and reproducible:

1. Frozen repair108 control: 1,085,092 bytes, SHA-256 `FFCE609E3F38124C801304F109767C60A94B9319637B0F926B9D797CCCDC74D8`.
2. Exact pre-Exposé-X extraction, repair108 lines 71--13575: 807,071 bytes / 13,502 lines, SHA-256 `EEEDD95BB9C042CCB1E4D9F5685248609E870DB3F0C270598FCE28B5B007DE2B`.
3. Documented intermediate after the early repair gate: 809,652 bytes, SHA-256 `FDEE28678288310DD9955AB2A65144BD67F1B213C40BCA1D32BD7E44C679A3F1`.
4. Jointly sealed source-repaired prefix: 812,825 bytes / 13,569 lines, SHA-256 `6A6878FCE68050F797E1E4256D363D038A7BE0B4C8A00430195E268887391194`. The exact witness is preserved in `controls/prefix_repairs_integration_postseal/`.
5. Final integrated prefix after TeX-only footnote plumbing: 812,912 bytes / 13,572 lines, SHA-256 `3FE03C89BA0662A61607CDE80DDB24BC4683FA37C30C1DA580908CFAD186F68C`.

The sealed-to-final diff contains only the two documented source-footnote sites on source-PDF pages 141--142. Exercise 5.7(b) uses a non-linked repeated superscript. Lemma 5.8.2 advances the counter once before the display, prints a non-mutating superscript in the display, and emits the matching optional-number `footnotetext` under `NoHyper` after the display. This avoids both the original dangling `Hfootnote` destination and amsmath's repeated evaluation of a mutating marker.

The final full-page render of complete physical page 81 shows marker **14**, footnote number **14**, and the complete final-object/constant-sheaf text. Complete physical page 80 likewise shows the source-faithful repeated marker **13** and full footnote **13**. No prose, formula, symbol, or source disposition changed in the post-seal repair.

Supporting receipts:

- `POST_SEAL_TECHNICAL_FIX.md`: SHA-256 `CFA9018E4533055E0C8F5B36434939BE2819E345E7F7500F896641FD4207A743`;
- `TECHNICAL_CHANGE_LEDGER.csv`: SHA-256 `64272C0CB9B0AC662BB553E5910CDF14941CA5DA7278A01DA4D43DFEC545BC23`;
- `SEALED_TO_FINAL_TECHNICAL.diff`: SHA-256 `02C056F33A07B662C7B75EF041D3059234BD0ED9A547AAE3B304FDC64BAB1979`;
- `COMPLETE_LAYER_EXTRACTION_LEDGER.csv`: SHA-256 `5E9349760792477B8FDEBF1D4040A69FFDB97F74FAA1048F1074D8ACDB8822EC`.

## Assembly seam and macro state

The production root contains exactly one `documentclass`, one `begin{document}`, and one `end{document}`; it inputs the prefix, macro reset, and tail body once each and has one deliberate `clearpage` at the seam.

The prefix ends with Exposé IX, Corollary 4.4 and its concluding proof sentence. The tail begins with the idx532 / printed-page-519 / source-PDF-page-526 marker, the Exposé X title and authorship, section 1, and subsection 1.1. In the final PDF:

- complete physical page 272 ends Exposé IX with Corollaries 4.3 and 4.4;
- complete physical page 273 starts Exposé X on a fresh page;
- there is no duplicate Exposé X, missing seam text, or intervening blank page.

All 55 tail namespace definitions in `SGA6_tail_macro_state.tex` match the standalone tail's effective definitions exactly. The seam file also restores `hbadness=1000`, `hfuzz=0.1pt`, and `allowdisplaybreaks` exactly once. This prevents inherited prefix definitions from silently changing the tail.

## Clean build and PDF inspection

The final reader was rebuilt from clean auxiliary state.

| Receipt | Bytes | SHA-256 | Finding |
|---|---:|---|---|
| pass 1 log | 45,924 | `25C87149FC9F3DDCF37235AD55A42B369FA993D14BCA2F1BF621208496AA2632` | zero errors, undefined references, box warnings, missing characters, or Hfootnote defects; one expected rerun-file notice because no prior auxiliary file existed |
| stabilized pass 2 log | 45,759 | `A9B1182E2E266B8A4A8A883D17B1E5F7812F83F7951EF67269C15A01D9FC6E1C` | zero errors, warnings, undefined references, overfull/underfull boxes, missing characters, or Hfootnote defects |
| validation JSON | 1,610 | `81B847D6CBEC053224114B28E393DCB269D8575BA2E2929D902DCD0764BEA8A1` | pass |

Independent PDF inspection found:

- 381 physical pages;
- exactly one MediaBox, `595.276 x 841.89 pt`;
- all 381 pages A4 and all 381 rotations zero;
- 41 font rows, all embedded; no Type 3 fonts;
- no encryption, form, JavaScript, or suspect flag.

## Coordinate closure and physical terminal

An independent line-level scan of the actual TeX closure found exactly 171 page-coordinate marker lines: one each for every current-rescribe index 532--702, with no duplicate and no omission. It also found exactly ten unindexed back-matter markers:

- printed pages 691--700;
- source-PDF pages 693--702.

The final source ends its notation-index longtable with `Z(x)`. Complete physical page 381 visibly ends with `Z(x)`, the bottom rule, and the intact footer. This is the volume's physical terminal, not idx702 alone.

## Tail pixel/text equivalence

Six complete-reader tail pages were independently re-rendered from the frozen final PDF at 120 dpi and compared with the standalone 109-page tail. A `993x1280+0+0` crop excluded only the generated footer region. Every pair had absolute error **0** and RMSE **0**:

- complete 273 / standalone 1;
- complete 343 / standalone 71;
- complete 351 / standalone 79;
- complete 364 / standalone 92;
- complete 366 / standalone 94;
- complete 381 / standalone 109.

For the first five pairs, normalized `pdftotext` alphanumeric token multisets also matched exactly. On the terminal pair, Poppler orders the visible `r^0_{\mathcal O}` glyph tokens as `ro` versus `ro0`; the rendered body is nevertheless pixel-identical and the visible terminal entries, including `Z(x)`, agree. Exact metrics and hashes are in `TAIL_EQUIVALENCE.csv`.

## Targeted rendered-prefix review

Twelve full-page 150-dpi renders from the frozen final PDF were inspected: complete physical pages 9, 80, 81, 152, 157, 191, 192, 206, 224, 272, 273, and 381. They cover the repaired source-PDF 14, 141--142, 277, 286, 347, 350, 377, and 431 gates, plus the Exposé IX/X seam and physical terminal.

All inspected pages are legible and free of clipping, overlap, broken diagrams, black replacement glyphs, or cut footnotes. Formula labels, restored triangles/derivations, the gamma correction, restored lemma sequence, seam titles, and terminal table are visually intact. Exact page-by-page findings are in `TARGETED_VISUAL_CHECK.csv`; the renders are in `target_pages_clean_final/`.

## Residual status, not review failures

- The prefix is not globally page-by-page source-certified merely because its known audit gates were repaired.
- idx663--702 and terminal back matter remain pending Claude/French-workpass synchronization.
- The source-faithful dangling `Cf.` note in the tail remains documented, not silently completed.
- This package remains a working/review edition. Publication and Zenodo decisions belong to the parent English manager.

Within those declared authority limits, the final complete layered reader passes this independent integration review.

# Cayley Current Duty Status

Generated: 2026-06-02

## Current Public State

Arthur Cayley, *Collected Mathematical Papers*, Volume I has a complete source-checked public reader in this repository:

`reader-pdfs/classical/Arthur Cayley - Collected Mathematical Papers, Volume I - Complete Source-Checked Modern LaTeX Reader.pdf`

That reader was rebuilt from validated slices plus six source-checked gap fills:

- pages 1-12
- pages 38-50
- pages 251-262
- pages 389-400
- pages 438-450
- pages 501-525

The full source/control packet is:

`sources/classical/cayley-volume-i-complete-source-checked-reader-2026-06-02/`

## Broader Cayley State

The repository also has volume-level slice readers for Volumes II-XIII under `reader-pdfs/classical/`, and a large extracted source scaffold under:

`sources/classical/cayley-current-slice-and-source-rebuild-2026-05-29/`

Those broader volume readers are useful public surfaces, but they should not be described as final source-faithful editions. The safer measured progress remains the validated slice/gap-fill layer described in `manifests/cayley_claude_progress_cost_inventory_20260531.md`.

Update, 2026-06-02: Volume VIII pages 17-66 have now been replaced in the public source tree by a 52-page source-checked TeX/PDF slice. A second local pass added source-checked pages 517-528, replaced the incorrect pages 569-570 text, and then filled pages 529-541 from source-checked TeX. A third pass replaced the defective pages 67-116 slice, whose old PDF rendered but whose TeX source was effectively empty, with a 45-page native source-checked TeX/PDF slice. A fourth pass replaced the unsafe pages 117-166 slice with a 42-page native source-checked TeX/PDF rebuild. A fifth pass replaced the TODO-heavy pages 317-366 slice with a 50-page source-checked semantic TeX/PDF rebuild, including the corrected pp. 353 paragraphs and native table material. A sixth pass replaced the former pages 167-216 and 367-416 public slices with source-checked semantic TeX/PDF rebuilds; both include native diagram/table reconstructions and no image/facsimile stand-ins. The public Volume VIII reader was rebuilt from the non-facsimile source PDFs and now renders as 541 pages; page-count shifts reflect denser repaired TeX rather than omitted source coverage. A seventh local pass replaced explicit diagram placeholders in pages 001-016, 217-241, 242-266, and 517-528 with native TikZ reconstructions while preserving the fuller public prose/math bodies. An eighth pass promoted full source-checked pages 417-441 and 442-466 rebuilds with native TikZ figures and no image stand-ins. A ninth pass promoted source-checked repairs for pages 267-291 and 304-316. A tenth pass promoted the pages 467-516 tail splice, keeping the existing repaired front half and replacing pages 501-516 with verified native TeX from the scan. The Volume VIII reader was rebuilt again and now remains 536 selectable-text pages with zero embedded images.

## New Local Cayley Handoff Packet

A local Cayley handoff packet was found at:

`C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Cayley\cayley_existing_workflow_packets_handoff_20260602\`

It contains workflow/example packets for Volume I visible pages 162-181, including:

- first-pass TeX/PDF transcriptions for pages 162-171 and 172-181;
- unified prose/math packets with formula, array, diagram, and witness crops;
- explicit TODO notes for uncertain formula details.

The packet README states that no fresh Cayley processing run was performed in that thread. These files are therefore useful as assist/workflow material, not as public promotion-grade Cayley reader replacements. They are also superseded as public reader material by the complete Volume I reader already mirrored in GitHub.

## Next Cayley Action

The next productive Cayley work is volume-by-volume continuation. Volume VIII is now much closer to clean public status, but it should still be audited for any remaining formula-level defects before a full-volume claim.

Specific Volume VIII targets after this pass:

- Remaining Volume VIII work before any full-volume clean claim: audit the promoted pp. 267-291, 304-316, and 467-516 repairs against the scan for formula-level slips; then inspect pp. 517-570 for smaller equation/alignment issues and confirm that excluded FACSIMILE helper PDFs are not needed by the public reader. The former pp. 467-516 high-risk tail is now represented by native TeX/PDF, not screenshots.

Local witness scan for Volume VIII:

`C:\Users\Floris\Documents\Papors\OS\Cayley\collmathpapers08caylrich.pdf`

Secondary explicit placeholder target:

- `sources_tex_Vol_IV/cayley_vol04_pages_401_425.tex`

Recommended repair loop:

1. Choose the next incomplete volume by validated-slice coverage and mathematical priority.
2. Identify missing ranges from the existing manifest and source scaffold.
3. For each range, use OCR/prose extraction plus GPU/crop-assisted math localization as a helper layer.
4. Promote only source-checked TeX/PDF slices, never screenshots or facsimile placeholders.
5. Rebuild the volume reader after enough verified slices/gap fills land.

This keeps the Cayley workflow bounded and auditable while still allowing parallel repair on dense mathematical pages.

Update, 2026-06-02: Volume X tail repair promoted. The legacy `cayley_vol10_pages_551_586` repair slice is now treated as a superseded source artifact for the public reader. The public Volume X reader was rebuilt from `551_565`, `566_575`, `576_585`, and `586_600` tail slices. Pages 566-600 are native source-checked TeX/PDF, with the p. 586 diagram reconstructed in TikZ and no screenshot/facsimile stand-ins. Verification: the rebuilt reader has 571 selectable-text pages, zero embedded raster images by `pdfimages`, and contains the previously missing Problems and Solutions tail names including A. B. Evans, Pellianus, and Artemas Martin. Follow-up polish: pp. 551-565 were then source-checked against printed pp. 550, 560, 563, and 564; the inherited formula placeholders were replaced with native TeX, including the p. 550 quartic, the p. 560 theta-product substitution, and the p. 563-564 differential/integration block.

Further Volume X update, 2026-06-02: Table No. 97 on printed p. 366 was repaired in `cayley_vol10_pages_376_400.tex`. The public TeX/PDF now contains native source-checked schedules for covariants `N`, `O`, and `P`, replacing summary placeholders that previously pointed readers back to the scan. The surrounding status prose was also tightened so the remaining unpromoted dense schedules on the following pages are clearly marked as next repair targets rather than hidden behind generic scan references. The rebuilt Volume X reader now has 572 selectable-text pages with zero embedded raster images.

Additional Volume X update, 2026-06-02: the invariant `Q` on printed p. 367 was promoted from a compact ellipsis formula to a native source-checked Table No. 97 column. A scratch candidate for the larger `R` and `S` tables exists locally, but those entries remain too ambiguous for direct public promotion without another scan-check pass.

Additional Volume X update, 2026-06-02: printed pp. 391-392 and p. 400 in `cayley_vol10_pages_401_425.tex` were source-checked against the Volume X scan. The malformed `AA4` half-value calculation was corrected, the `CH2` leading-coefficient calculation and its small segregate replacement table were replaced with native TeX from the scan, and the final derivative now reads `ch2 = 1/3 cy - 1/3 b^3 + 11/30 bh - 1/5 cg` instead of a placeholder-scale summary. The p. 400 `S_3` verification line was also corrected to the visible `b^6(-27c^5+101c^4-141c^3+87c^2-20c)`. The slice and public Volume X reader were rebuilt; the reader remains 572 selectable-text pages with no embedded raster-image bodies.

Additional Volume X update, 2026-06-02: printed pp. 393-396 in `cayley_vol10_pages_401_425.tex` were source-checked against the Volume X scan. Table No. 100 was promoted from noisy partial OCR to native TeX for the degree 3-6 schedules visible on pp. 393-394, including the concluded 6.8, 6.10, 6.12, and 6.14 blocks. The quartic, quintic, and sextic N.G.F. formulas on pp. 394-396 were also repaired, removing all literal `?` placeholders from the slice and restoring the long product denominators and Cayley's half-exponent sextic note. The repaired slice compiles to 21 pages, `pdfimages` reports no embedded raster images, and the public Volume X reader was rebuilt from the known-good non-overlapping slice list; it remains 572 selectable-text pages.

Additional Volume X/XII update, 2026-06-02: the Volume X Table No. 93 bis header in `cayley_vol10_pages_401_425.tex` was corrected from a degree-5/six-coefficient placeholder to the scan-visible cubic form `(S_0,S_1,S_2,S_3 \mid x,y)^3`; the full monomial lists remain deliberately unpromoted because the 600-dpi crops are still ambiguous in several lower-column entries. Volume XII repairs were also promoted in two slices. `cayley_vol12_pages_026_050.tex` now fixes the scan-readable `a_1b_1` and `a_1b_2-a_2b_1` terms and its preamble typo; the residual provisional table entries on lines 591-593 remain open. `cayley_vol12_pages_451_475.tex` now removes all literal `?` placeholders from the repaired slice, replacing the theta-function note (paper 861) and the fractional-power/indicial-equation examples in papers 862-863 with native source-checked TeX. The rebuilt public Volume XII reader has 439 selectable-text pages and zero embedded raster-image bodies; the one-page drop versus the previous reader is reflow from the repaired native TeX slice, not an intentional coverage loss.

Follow-up Volume XII `026_050` repair, 2026-06-02: the remaining literal `?` and dotfill placeholders in this slice were removed. Book p.14 now restores Cayley's reduced `\Psi` formula and `-3L^2\Omega` term; book p.15 now carries a native TeX sparse coefficient table for `\Box` instead of the earlier six-row placeholder; the reduction sentence below the table was restored from the scan; and book p.23 now restores the `\Lambda` recurrence `B=\Lambda A`, `C=\frac12\Lambda B`, `D=\frac13\Lambda C,\ldots`. The rebuilt slice is 25 pages with zero embedded raster images, and the public Volume XII reader remains 439 pages with zero embedded raster images.

Follow-up Volume X `526_550` repair, 2026-06-02: the previous sideways-table and characteristic-diagram placeholders were replaced with native TeX in `cayley_vol10_pages_526_550.tex`. The slice now carries Table No. 80 in single notation and double-theta notation, plus native characteristic tables for the upper and lower halves. No screenshots or `includegraphics` bodies were introduced. The repaired slice compiles to 20 pages and the rebuilt public Volume X reader is now 574 selectable-text pages with zero embedded raster images.

Follow-up Volume XIII `001_025` repair, 2026-06-02: Paper 889, "On a Differential Equation and the Construction of Milner's Lamp," was source-checked against the Volume XIII scan. The incorrect inherited half-coefficients and reversed integral limits were replaced by Cayley's scan-visible `\tfrac23` formulas, equations (3), (4), and (6) were restored to their differential-ratio forms, the concluding constants now read `b^3=-\tfrac43 a^3\cos^3\beta`, and the Milner lamp diagram was reconstructed as native line art. The repaired slice compiles to 18 pages and the rebuilt public Volume XIII reader is 453 selectable-text pages with zero embedded raster images.

Follow-up Volume IX `551_562` repair, 2026-06-02: Paper 619, "On an Algebraical Operation," was source-checked against the Volume IX scan on printed pp. 539-540. The inherited quadratic example was corrected from the spurious `1-x^{-4}` numerator family to Cayley's scan-visible `1-x^{-2}` formulas, including the `P,Q,R` partial fractions, the formerly question-marked Omega term, and the final `A(x)=1/((1-ax^2)(1-a^2))` result. The visible cubic setup on p. 540 was also restored through the first operated-on expression. The repaired slice compiles to 10 pages and the rebuilt public Volume IX reader is 374 selectable-text pages with zero embedded raster images.

Follow-up Volume XIII `301_325` repair, 2026-06-02: the damaged coefficient tables on printed pp. 283-284 were rebuilt in native TeX. The repaired tables now remove the literal `-?` entries in the `S\alpha^5\beta + S\alpha^4\beta^2 + S\alpha^3\beta^3` comparison and the `G-CE-D^2` comparison, including the `bcd`, `b^3d`, `b^2c^2`, and `b^4c` rows. The p. 284 displayed calculation was corrected to the scan-visible `+10f(b)+15g(-1)-5b(...)` form. Square-diagram placeholders remain explicitly marked as unresolved rather than promoted without a scan-faithful native layout. The repaired slice compiles to 15 pages and the rebuilt public Volume XIII reader remains 453 selectable-text pages with zero embedded raster images.

Follow-up Volume IV `301_325` repair, 2026-06-02: Papers 266-267 were source-checked against the Volume IV scan and the repaired slice no longer contains literal `?` placeholders. The promoted fixes include the pp. 280-286 cubic/quartic/quintic coefficient formulas, the `M e-\square`, `N e+M`, and `N+a^2e` tables, the p. 285 quintic coefficient header (`76125\,\square\sqrt{\square}` as printed), the pp. 290-291 symmetric-function array, and the pp. 299-303 determinant/reduced-function tables. The dense long coefficient table printed below the p. 285 header remains explicitly marked as pending full line-by-line collation. The repaired slice compiles to 27 pages and the rebuilt public Volume IV reader is 501 selectable-text pages with zero embedded raster images.

Follow-up Volume IV `526_545` repair, 2026-06-02: Paper 297, "On the Sextic Torse," was source-checked against the Volume IV scan. The inherited formulas now restore the missing leading `\Box` terms, correct the `af^2`, `bg^2`, and `ch^2` substitution terms in the cyclic expression, normalize the square-symbol notation, and restore the final cyclic-sum identity as a native TeX display. The repaired slice compiles to 20 pages with zero embedded raster images. The rebuilt public Volume IV reader remains 501 selectable-text pages and zero embedded raster-image bodies.

Follow-up Volume XIII `451_475` repair, 2026-06-02: the opening Pell-equation table in Paper 943 was checked arithmetically against the scan-readable relation `y^2 = ax^2 \pm 1`. Rows `a=1007` and `a=1010` through `a=1021` were repaired, including shifted entries and large integer values such as the `a=1017`, `a=1019`, and `a=1021` rows. The repaired slice compiles to 30 pages with zero embedded raster images. The rebuilt public Volume XIII reader remains 453 selectable-text pages and zero embedded raster-image bodies.


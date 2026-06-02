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

Update, 2026-06-02: Volume X tail repair promoted. The legacy `cayley_vol10_pages_551_586` repair slice is now treated as a superseded source artifact for the public reader. The public Volume X reader was rebuilt from `551_565`, `566_575`, `576_585`, and `586_600` tail slices. Pages 566-600 are native source-checked TeX/PDF, with the p. 586 diagram reconstructed in TikZ and no screenshot/facsimile stand-ins. Verification: the rebuilt reader has 571 selectable-text pages, zero embedded raster images by `pdfimages`, and contains the previously missing Problems and Solutions tail names including A. B. Evans, Pellianus, and Artemas Martin. Remaining Vol X cleanup target: pp. 551-565 still inherit a few older placeholder phrases from the previous repair layer and should be formula-polished next.


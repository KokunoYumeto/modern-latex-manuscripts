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

Update, 2026-06-02: Volume VIII pages 17-66 have now been replaced in the public source tree by a 52-page source-checked TeX/PDF slice. A second local pass added source-checked pages 517-528, replaced the incorrect pages 569-570 text, and then filled pages 529-541 from source-checked TeX. The public Volume VIII reader was rebuilt from the non-facsimile source PDFs and now renders as 559 pages.

## New Local Cayley Handoff Packet

A local Cayley handoff packet was found at:

`C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Cayley\cayley_existing_workflow_packets_handoff_20260602\`

It contains workflow/example packets for Volume I visible pages 162-181, including:

- first-pass TeX/PDF transcriptions for pages 162-171 and 172-181;
- unified prose/math packets with formula, array, diagram, and witness crops;
- explicit TODO notes for uncertain formula details.

The packet README states that no fresh Cayley processing run was performed in that thread. These files are therefore useful as assist/workflow material, not as public promotion-grade Cayley reader replacements. They are also superseded as public reader material by the complete Volume I reader already mirrored in GitHub.

## Next Cayley Action

The next productive Cayley work is volume-by-volume continuation. The immediate target should be Volume VIII, because it is public as a 495-page reader but still has source-folder facsimile ranges and TODO-heavy TeX.

Specific Volume VIII targets:

- `sources_tex_Vol_VIII/cayley_vol08_pages_067_116.tex` - obvious public-facing defect: the PDF renders 41 pages, but the TeX file is effectively empty. This is the current first-priority repair target.
- `sources_tex_Vol_VIII/cayley_vol08_pages_117_166.tex` - dense table/math TODO risk.
- `sources_tex_Vol_VIII/cayley_vol08_pages_167_216.tex` - dense table/math TODO risk.
- `sources_tex_Vol_VIII/cayley_vol08_pages_317_366.tex` - dense table/math TODO risk.

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

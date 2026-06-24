# Workflow Addendum 2026-06-24: Source Witnesses, Public Surfaces, and Audit Routing

This addendum records workflow lessons from the June 2026 archive-maintenance and source-audit lanes. It is a practical rule sheet for future local Codex / web Pro / other-agent collaboration.

## 1. Public Surface Rule

Do not let file names such as `complete`, `strict`, `source-checked`, `critical`, or `accepted` carry the public claim by themselves. Public records must state the actual status in human-facing prose.

Recommended labels:

- **OCR/source-witness aid**: OCR text, page images, crops, or locator files. Useful for checking, not authoritative.
- **Working draft**: TeX/PDF exists and is useful, but formulas, diagrams, tables, or prose may still contain source-faithfulness errors.
- **Source-witnessed tranche**: a bounded page/paper range has source scans and an audit ledger; this still does not certify the whole author or whole volume.
- **Source-closed locus**: a specific formula/table/diagram/prose locus was checked against stated source witnesses and needs no patch under that source-quality caveat.
- **Critical edition**: reserved until explicitly certified by Floris/human review; do not infer it from AI output.

## 2. OCR As Witness, Not Judge

GPU OCR / Surya-style OCR / Pix2Text / VLM outputs are useful mainly as **coverage witnesses**:

- They help detect missing prose, missing formulas, page-map gaps, duplicated pages, and suspicious compression.
- They are useful for making web sessions ask, “where did this paragraph/formula go?”
- They are not automatically correct transcription and must not override page images or source PDFs.
- OCR from a different copy or edition must not be used for page-precise claims without source identity, checksum, and page-map reconciliation.

The SGA5 audit lane showed the correct posture: OCR and indexes can locate dense loci, but source-page visual audit remains the authority. Current SGA5 workpass coverage has since advanced to source pages 1-60 plus the p103 diagram locus; this still proves the same workflow point: much more TeX can exist than has been source-page certified, and public records must state the narrower audited coverage.

## 3. High-Resolution Source Packets

For difficult mathematical scans, useful aid packets should include:

- source PDF or source page images at sufficient resolution;
- page map from source PDF page to printed/source page;
- per-page object inventory for diagrams, tables, displayed formulas, footnotes, and unusual symbols;
- crops with one or two surrounding text lines, not isolated symbol fragments only;
- render witnesses from the output PDF;
- stable object IDs and ledger verdicts.

High-DPI images are expensive for web-session context but often cheaper than repeated failed reasoning over bad scans. They are appropriate when diagrams, tables, dense formulas, or old typography are the bottleneck. For normal prose pages, OCR/text witnesses and lower-resolution renders may be enough.

## 4. Audit Bundles Versus Reader Versions

Do not dump every audit bundle into Zenodo as though it were a new reader edition. Route material by purpose:

- Reader PDFs/TeX: front them when they improve the actual reading surface.
- Source witnesses/high-resolution images: upload when they materially support verification or continuation.
- Audit/survival/no-patch ledgers: keep as compact provenance or pending support unless they close a public-facing uncertainty.
- Raw local project bricks: track with manifests first; upload only with clear source-witness wording.

Noether R122/R123/R123+P08 survival packages are examples of **anti-regression/source-closure support**, not full paper certification. Gordan and Steinitz project-upload bricks are examples of **source-witness/project-handoff sets**, not new completed editions.

## 5. Known Weak-Point Policy

Public descriptions should explicitly preserve known weak points:

- SGA5 is not complete while only bounded source pages have been audited; SGA6/SGA7 remain working drafts with compression and diagram risks unless a later packet closes a locus.
- Deligne diagram-heavy material can be genuinely useful while still requiring diagram/source review.
- Cayley drafts are not source-faithful enough to call complete or accurate without fresh page-level repair.
- Older `accepted` labels in Steinitz/Gordan/Cayley-like handoff lanes mean accepted by a production lineage, not independently line-certified.

## 6. Collaboration Loop

Best current loop:

1. Local machine collects public-domain source scans and high-resolution page witnesses.
2. Local OCR/CV tools produce locator text, formula/table/diagram crop inventories, and page maps.
3. Web/agent sessions produce or repair TeX/translation against those aids.
4. Local Codex sweeps downloads, extracts zips, classifies quality, updates pending manifests, and updates GitHub/Zenodo public surfaces.
5. Human-facing public records state what is done, what is only working draft, and where corrections can be suggested through GitHub issues or pull requests.

This workflow is AI-run, not merely AI-assisted, but its outputs must still be represented by source fidelity level rather than by agent confidence.
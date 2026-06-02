# Math-OCR Assist Lessons from Sylvester Volume I

Date: 2026-06-02

This note records what the Sylvester Volume I continuation thread found useful from local GPU/math-OCR assist packets.

## What Helped

- Witness crop images for formula, table, and diagram regions.
- Page manifests that map book page, source PDF page, crop filename, and region type.
- Accepted/rejected candidate lists as triage aids.
- Failure-mode lists showing where OCR or pix2tex-style outputs hallucinated, split formulas incorrectly, or confused prose/math boundaries.

## What Did Not Work as Direct Input

- Candidate TeX was not reliable enough for paste-in promotion without source comparison.
- Formula/prose boundary classification was too fragile to be trusted automatically.
- Assist packets for one page range do not help a non-overlapping range except as workflow calibration.

## Practical Rule

Use local/GPU extraction to localize and witness hard mathematical regions, not to replace the source-checking step.

Preferred assist packet shape:

1. One manifest row per crop with book page, source PDF page, region type, crop filename, and status.
2. Cropped witness PNGs keyed by page and region.
3. Candidate TeX in CSV with explicit `accepted`, `rejected`, or `uncertain` status.
4. A short failure-mode audit for the range.

Do not promote extracted TeX into public readers unless it has been compared against the source scan. For normal prose pages with short displayed equations, manual source reading plus targeted formula crops may be cheaper than adjudicating large candidate lists.

# Cayley Pro Source Staging Packet

Date: 2026-06-29

Local staging root:

`C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Cayley\Cayley_PRO_SOURCE_STAGING_20260629`

Companion upload manifest:

[`20260629_cayley_pro_source_staging_uploads.csv`](20260629_cayley_pro_source_staging_uploads.csv)

## Scope

This is a source-first upload packet for a ChatGPT Pro / continuation lane to repair Arthur Cayley's *Collected Mathematical Papers*. It is not a new reader edition, not a proof of transcription completeness, and not a promotion of any existing Cayley TeX/PDF range to source-faithful status.

The staging folder contains 33 files totaling 6,237,004,684 bytes. Its `UPLOAD_ORDER.csv` has 27 upload rows:

- 20 selected JP2 source master ZIPs/chunks covering Vol. 00/front/index and Vols. I-XIII.
- 3 generated witness/index ZIPs.
- 4 audit/status notes.

## Source Authority

Use the selected JP2 master zips/chunks in `01_best_source_masters/` as the source authority. Internet Archive derivative PDFs are explicitly excluded as authority when JP2 masters are available; the local source verdict found some derivative PDFs in this lane at only about 100-166 dpi, while the JP2 masters contain the actual page pixels.

Generated PNG witness packs are localization/render aids only. They can save time finding known hard regions, but they do not override the JP2 masters.

## Excluded Candidate Policy

The packet deliberately excludes ambiguous or lower-confidence candidates such as `sylv`/`sylvrich`-named duplicates unless they are needed only as local comparators. It also excludes derivative PDF files as source authority. The selected-source manifest and excluded-candidates CSV in the local packet record the exact choices.

## Public Quality Framing

Current Cayley public PDFs/TeX/unit indexes remain provenance, salvage, and repair material. They are not source-faithful transcriptions. Known failure modes include symbol drift, equations and tables flattened into prose, placeholders, stale screenshot/facsimile instructions, whitespace/layout failure, and mathematically wrong or non-source-faithful passages.

No Cayley range is presently promoted as source-faithful. Promote only a specific page/range after page-by-page glyph/source comparison against the selected source masters.

## Workflow Lesson

This packet captures the current best practice for large image-heavy repair projects: stage one source authority per volume, split only oversized masters into sub-500MB chunks, keep generated witness images separate from source authority, and put salvage TeX/PDF in a lower-confidence lane until exact ranges pass source comparison.

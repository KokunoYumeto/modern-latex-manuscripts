# Workflow Notes

The project workflow is deliberately redundant: raw source packets are preserved, while clean public records present the best current reader PDFs and organized artifacts.

## Typical Path

1. Identify public-domain or otherwise suitable source material.
2. Download scans or source PDFs.
3. Produce initial TeX with automated transcription.
4. Compile and repair into readable PDFs.
5. Review against source scans.
6. Translate where useful.
7. Publish reader PDFs and artifact ZIPs to Zenodo.
8. Track corrections and future work in GitHub.

## Public File Roles

Reader PDFs are the public browsing surface. They should be named by author, work, language when helpful, and draft status when the text is not final.

Artifact ZIPs are not meant to be pretty. They preserve TeX, source witnesses, OCR text, render checks, source packets, and provenance so the reader-facing PDF can be checked and rebuilt.

Manifest/status files explain what is included, what passed technical checks, and what still needs review. They should be short enough to read and precise enough to act on.

## Publication Rule

Availability and provenance matter, but the public surface should not look like a raw tool dump. When a source packet has internal run names, partial folders, or repair logs, keep those inside artifact ZIPs and give the Zenodo record a human title organized by author, work, corpus, or mathematical tradition.

Public-facing titles should name the author, work, language/status where needed, and role. Internal run names should stay inside raw provenance archives, not in Zenodo titles or top-level filenames.

## Current Review Loop

1. Run the public archive readability audit.
2. Run the public PDF surface audit.
3. Check the newest local drops against the current public summaries.
4. Promote only the clearer or more complete surface material.
5. Preserve older material in artifacts or version history when it is useful for provenance.
6. Update the archive guide, file catalog, known gaps, and current-status manifest.

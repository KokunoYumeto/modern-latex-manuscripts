# Release Checklist

Use this before publishing or replacing a Zenodo record.

## 1. Select The Public Surface

- Prefer author, work, or coherent corpus records over raw processing-run records.
- Keep the main landing record as the broad preservation surface.
- Put readable PDFs at the top level.
- Put TeX, source witnesses, OCR, page images, render logs, raw packets, and provenance inside artifact ZIPs.
- Keep older useful material in artifacts or version history unless it is actively misleading.

## 2. Naming

- Title records by author, work, corpus, or mathematical tradition.
- Name files by role, author/work, language, and draft status where needed.
- Avoid internal run names, local folders, temporary labels, and tool-centric names in public titles or top-level filenames.
- Use ordinary reader language: "English Translation Draft", "Modern LaTeX Draft", "French Reference PDF", "TeX Sources and Provenance".

## 3. Rights And Source Hygiene

- Preserve public-domain scans and source witnesses when useful for checking.
- Do not present modern publisher wrappers, editorial prefaces, or collected-volume apparatus as part of the original work unless they are clearly public-domain or licensed.
- If a collected source is used only as a witness, keep the mathematical work and remove obvious modern wrappers from front-facing reader PDFs where practical.
- Keep provenance in artifact ZIPs so corrections can be traced.

## 4. Technical Checks

- Confirm each top-level PDF opens with `pdfinfo`.
- Check page count and file size for obvious bad exports.
- Extract a text sample when possible; classify known image-based scan references explicitly.
- Compile TeX roots when a compiled reader PDF is expected.
- Check ZIP integrity before upload.
- Compare local file sizes and checksums with the published Zenodo files after upload.

## 5. Metadata

- Description should explain the project, not just the latest upload.
- Include current coverage/status, known incompleteness, provenance model, and file roles. Base those labels on the newest local/source audits available, not only on package filenames.
- Link related records in the metadata when a corpus is split across records.
- Use CC0 where possible and document exceptions or caution areas in plain language.

## 6. Post-Publication

- Run the public archive readability audit.
- Run the public PDF surface audit.
- Refresh the public file catalog and status manifests.
- Update the GitHub mirror docs: browse index, author/work index, project dashboard, known gaps, workflow, and contribution notes.
- Commit and push the checkpoint to its designated GitHub ref, then verify the remote commit and raw public bytes.
- If remote delivery is blocked, record the exact blocker and keep the checkpoint explicitly incomplete.
- Update project release notes with current record IDs, audit timestamps, and blockers.
- Preserve audit/logbook material when it explains the real reliability level or reusable workflow, especially for constructed-language, OCR, diagram/table, and source-witness lanes.

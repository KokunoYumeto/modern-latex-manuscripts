# Current Public Repair Queue

Generated: 2026-05-31

This is the working repair queue after the 2026-05-30 Brahmagupta reader-surface correction, Cayley verified-slice refresh, Gauss repair rebuild, EGA IV sections 1-21 publication, Noether/Weber author-page refreshes, and main landing surface curation.

## Current Public Audit Status

- Public PDF surface audit: 335 PDFs checked, 0 flagged.
- Public PDF process-note audit: 335 PDFs checked, 0 flagged.
- Public archive/readability audit: 15 current records checked, 0 flagged.
- Typography/layout heuristic audit: 335 PDFs checked, 123 PDFs warned. These warnings are quality triage, not proof that a file is unusable.

Audit outputs:

- `reports/public_pdf_surface_audit_20260530_102048.md`
- `reports/public_pdf_process_note_audit_20260530_102402.md`
- `reports/public_archive_readability_audit_20260530_102402.md`
- `reports/public_pdf_typography_audit_20260530_103711.csv`
- `reports/public_pdf_typography_audit_20260530_103711.json`

## Published State

- Main landing page: https://zenodo.org/record/20393488
- Main all-version DOI: https://zenodo.org/records/20393488
- EGA current version: https://zenodo.org/record/20414353
- EGA all-version DOI: https://zenodo.org/records/20414353
- Non-European current version: https://zenodo.org/record/20410957
- Non-European all-version DOI: https://zenodo.org/records/20410957
- Classical/Cayley current version: https://zenodo.org/record/20459215
- Classical/Cayley all-version DOI: https://zenodo.org/records/20414787
- Gauss current version: https://zenodo.org/record/20410934
- Gauss all-version DOI: https://zenodo.org/records/20410934
- Noether current version: https://zenodo.org/record/20412587
- Noether all-version DOI: https://zenodo.org/records/20412587
- Weber current version: https://zenodo.org/record/20412153
- Weber all-version DOI: https://zenodo.org/records/20412153
- GitHub mirror: https://github.com/KokunoYumeto/modern-latex-manuscripts

## Repairs Completed In This Pass

- Replaced the top-level Brahmagupta original-language reader in the non-European record with the compact text-layer working edition.
- Preserved the larger scan-backed Brahmagupta reader inside the non-European artifact ZIP for provenance and source checking.
- Refreshed the non-European public summary, public guide, Zenodo metadata, main landing metadata, and GitHub mirror.
- Updated audit scripts to target the new main/non-European versions and the current SGA record.
- Published the refreshed classical shelf with 127 promoted review system-validated Cayley slice PDFs represented in the artifact layer; the front-facing public surface is organized as Cayley volume-level source-checked slice readers rather than the older broad per-volume drafts.
- Published the refreshed Gauss author page with eight cumulative working readers totaling 3,061 pages.
- Published the refreshed EGA record with a 514-page standalone EGA IV sections 1-21 English working reader, the TeX/PDF supplement, and the updated full artifact ZIP.
- Published the refreshed Noether author page with paired German/English paper-level cumulative readers through Papers 1-21 complete.
- Published the refreshed Weber author page with paired German/English readers for the Volume I introduction opening, Volume II sections 176-202, and Volume III sections 1-100.
- Patched the non-European record with seven small work-level replacement PDFs from the latest changed-this-round pass.
- Published the curated main landing version 20393488: metadata was refreshed after the Noether/Weber/SGA/non-European updates; older broad Cayley/Weber direct-reader drafts remain demoted from the latest main file list while the full preservation ZIPs, prior Zenodo versions, and author/corpus records remain available.
- Added local OCR tooling report for repair agents at `reports/MATH_OCR_TOOLING_STATUS_FOR_REPAIR_AGENTS_20260530.md`; standard Docling/Surya is useful as a witness, local SmolDocling was weaker on EGA, pix2tex runs but is only a fallible formula-crop witness, and direct Surya 0.20 currently needs Docker/vLLM.
- Confirmed no current public PDFs are flagged for extraction failure, process notes, stale public records, or archive-level readability problems.

## Priority Queue

1. Non-European work-level typography and layout.
   Continue replacing older multilingual drafts with cleaner per-work editions when a new render is actually better. Highest-value targets are Yang Hui Chinese originals, al-Khwarizmi Arabic/original-language renderings, the project guide body-size issue, and any Sanskrit pages with empty first-page content or inconsistent Devanagari layout.

2. SGA 3 existing English translation rebuild.
   The current rebuild is a substantial improvement over the raw code-block version, but formulas inside many imported blocks still render as text-like expressions rather than fully converted math. Keep it top-level for readability, but queue formula-level conversion as future repair.

3. SGA 5 high-fidelity source-checked edition.
   Current source-checkable SGA 5 material is complete through printed page 484. Continue merging new source-checked batches only when paired source/translation material is present and the cumulative reader remains coherent.

4. EGA working translation.
   EGA IV sections 1 through 21 are now live as a 514-page standalone working reader. Continue incorporating new translated sections from the local EGA workspace after each clean build, and keep the standalone EGA IV reader plus source ZIP current.

5. Cayley front-facing policy.
   Keep validated/repaired slices as the public reader surface. Broad per-volume Cayley drafts remain artifact/source material until they are independently rendered and checked; do not promote broad volume drafts as clean top-level readers.

6. Gauss current working editions.
   Current known mathematical transcription defects reported by the local repair pass have been addressed and the refreshed author page is live. The bands still need continued proofread and scan comparison. New scan downloads for missing bands should be indexed and fed into future repair work.

7. Noether and Weber high-fidelity repair streams.
   Noether is live through Papers 1-21 complete in paired German/English paper-level cumulative readers. Weber is live through Volume I introduction through section 8, Volume II sections 176-202, and Volume III sections 1-100 in paired German/English readers. Replace older cumulative drafts only incrementally, preserving older drafts in artifacts until the paper-level or volume-level high-fidelity replacement is complete. Keep author pages organized by work/paper, not by source session.

8. al-Battani / Albategnius, Opus Astronomicum.
   Newly queued acquisition candidate: Carlo Alfonso Nallino's edition of al-Battani's astronomical work, including Arabic text, Latin translation, notes, and astronomical tables. Baseline source located at Internet Archive (`albattanisivealb00batt`), with PDF plus OCR text, word-level XML, and hOCR witnesses downloaded locally. Next pass should split the scan into Arabic/Latin/table-heavy sections and create a table-aware transcription packet before any public reader is promoted.

9. Author-cluster and older main-record drafts.
   Several older broad readers still trigger mixed-page-size or font-size heuristics. These are not urgent public-surface failures, but they should be split or replaced by author/work-level records as cleaner TeX becomes available.

## Typography Heuristic Summary

- 123 of 335 PDFs had at least one layout warning.
- Warning types: 107 inconsistent-page-font-size, 38 mixed-page-sizes, 5 wide-font-size-spread, 1 body-font-small, 1 body-font-large.
- Records with the most warnings: non-European consolidated record, main landing legacy readers, Chinese focused slice, classical/Cayley-Dedekind-Dirichlet shelf, EGA reference/original PDFs, Noether, SGA, Gauss, author cluster.
- Reference scans and historical PDFs can legitimately trigger mixed-page-size warnings; prioritize generated modern-LaTeX readers first.

## Rule For Future Uploads

Top-level PDFs should be reader-facing: coherent work-level or corpus-level PDFs that open, extract text where appropriate, and avoid visible process notes. ZIP artifacts should carry TeX sources, source scans, provenance, build logs, superseded drafts, and repair notes.





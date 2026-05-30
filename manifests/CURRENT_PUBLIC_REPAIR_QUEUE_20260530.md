# Current Public Repair Queue

Generated: 2026-05-30

This is the working repair queue after the 2026-05-30 Brahmagupta reader-surface correction and main landing refresh.

## Current Public Audit Status

- Public PDF surface audit: 337 PDFs checked, 0 flagged.
- Public PDF process-note audit: 337 PDFs checked, 0 flagged.
- Public archive/readability audit: 15 current records checked, 0 flagged.
- Typography/layout heuristic audit: 337 PDFs checked, 126 reader PDFs warned. These warnings are quality triage, not proof that a file is unusable.

Audit outputs live in the local project reports directory and are mirrored into source/provenance artifacts during release refreshes.

## Published State

- Main landing page: https://zenodo.org/record/20454056
- Main all-version DOI: https://zenodo.org/records/20393488
- Non-European current version: https://zenodo.org/record/20453848
- Non-European all-version DOI: https://zenodo.org/records/20410957
- GitHub mirror: https://github.com/KokunoYumeto/modern-latex-manuscripts

## Repairs Completed In This Pass

- Replaced the top-level Brahmagupta original-language reader in the non-European record with the compact text-layer working edition.
- Preserved the larger scan-backed Brahmagupta reader inside the non-European artifact ZIP for provenance and source checking.
- Refreshed the non-European public summary, public guide, Zenodo metadata, main landing metadata, and GitHub mirror.
- Updated audit scripts to target the new main/non-European versions and the current SGA record.
- Confirmed no current public PDFs are flagged for extraction failure, process notes, stale public records, or archive-level readability problems.

## Priority Queue

1. Non-European work-level typography and layout.
   Continue replacing older multilingual drafts with cleaner per-work editions when a new render is actually better. Highest-value targets are Yang Hui Chinese originals, al-Khwarizmi Arabic/original-language renderings, the project guide body-size issue, and any Sanskrit pages with empty first-page content or inconsistent Devanagari layout.

2. SGA 3 existing English translation rebuild.
   The current rebuild is a substantial improvement over the raw code-block version, but formulas inside many imported blocks still render as text-like expressions rather than fully converted math. Keep it top-level for readability, but queue formula-level conversion as future repair.

3. SGA 5 high-fidelity strict restart.
   Current strict source-checkable SGA 5 material is through complete Expose V. Continue merging new strict batches only when paired source/translation material is present and the cumulative reader remains coherent.

4. EGA working translation.
   Continue incorporating new translated sections from the local EGA workspace after each clean build. The active blocker reported by the EGA worker was a single extra brace in `ega4-21.tex` plus a possible remarks/env mismatch after a re-merge.

5. Cayley front-facing policy.
   Keep validated/repaired slices as the public reader surface. Broad per-volume Cayley drafts remain artifact/source material until they are independently rendered and checked; do not promote broad volume drafts as clean top-level readers.

6. Gauss current working editions.
   Current known mathematical transcription defects reported by the local repair pass have been addressed, but the bands still need continued proofread and scan comparison. New scan downloads for missing bands should be indexed and fed into future repair work.

7. Noether and Weber high-fidelity repair streams.
   Replace older cumulative drafts only incrementally, preserving older drafts in artifacts until the paper-level or volume-level high-fidelity replacement is complete. Keep author pages organized by work/paper, not by source session.

8. Author-cluster and older main-record drafts.
   Several older broad readers still trigger mixed-page-size or font-size heuristics. These are not urgent public-surface failures, but they should be split or replaced by author/work-level records as cleaner TeX becomes available.

## Typography Heuristic Summary

- 126 of 337 PDFs had at least one layout warning.
- Warning types: 109 inconsistent-page-font-size, 40 mixed-page-sizes, 5 wide-font-size-spread, 2 body-font-small, 1 body-font-large.
- Records with the most warnings: non-European consolidated record, main landing legacy readers, Chinese focused slice, classical/Cayley-Dedekind-Dirichlet shelf, EGA reference/original PDFs, Noether, SGA, Gauss, author cluster.
- Reference scans and historical PDFs can legitimately trigger mixed-page-size warnings; prioritize generated modern-LaTeX readers first.

## Rule For Future Uploads

Top-level PDFs should be reader-facing: coherent work-level or corpus-level PDFs that open, extract text where appropriate, and avoid visible process notes. ZIP artifacts should carry TeX sources, source scans, provenance, build logs, superseded drafts, and repair notes.

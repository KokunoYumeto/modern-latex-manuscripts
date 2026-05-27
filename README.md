# Modern LaTeX Manuscript Corpus

This repository is the working coordination surface for an ongoing project to produce modern, inspectable LaTeX editions of older mathematics and physics manuscripts. The citable archival releases live on Zenodo; this GitHub repository is for collaboration, issue tracking, manifests, scripts, and review workflow.

Current archive:

- Zenodo concept DOI: <https://doi.org/10.5281/zenodo.20393488>
- Current public record: <https://zenodo.org/records/20410262>
- Current version DOI: <https://doi.org/10.5281/zenodo.20410262>

## What This Project Is

The immediate goal is a clean original-language typesetting layer:

- readable generated PDFs,
- corresponding TeX/source files,
- source-witness scans or references,
- provenance and quality-control manifests,
- enough structure that editors and AI agents can check work against the original witnesses.

Translation is a later layer once the source-language editions are stable, though SGA translation handoff packets are already included because that work is active.

This is not a final critical edition. It is a working corpus: useful now, but still being proofread, repaired, split, and normalized.

## Repository Scope

GitHub is not the bulk storage location. Large PDFs, scans, and artifact ZIPs belong on Zenodo releases. This repository keeps:

- release metadata and manifests,
- audit results and known-bad/demoted lists,
- scripts used to build and validate releases,
- contribution workflow and issue templates,
- project status and roadmap.

Do not commit large PDFs or ZIP payloads directly here. Link to the Zenodo file, attach a small patch, or open an issue with enough detail to reproduce the fix.

## Current Status

The v23 public release surface contains:

- 58 top-level reader PDFs,
- 35 artifact ZIPs,
- 22 cleaned non-European top-level reader PDFs from the cleanup 9/KIMI5 batch,
- 1 partial Cayley current-incremental top-level reader PDF,
- SGA 1-7 handoff material including active SGA4 English translation batches through SGA4 Expose I sections 8.7-8.8,
- two Kimi 7 non-scan artifact ZIPs with audited generated PDFs and TeX/text source material,
- a full-repo ZIP on Zenodo for bulk download.

Important caveats: `00_pdf__gauss_werke.pdf` was demoted in v21, and `00_pdf__non_eu__karpinski_robert_of_chester_latin_translation_1915.pdf` was demoted in v22 after display QC. Both remain preserved in artifacts/history, but neither should be treated as a clean reader-facing PDF.

## How To Help

Useful contributions include:

- reporting unreadable or malformed PDFs,
- correcting TeX transcription errors,
- identifying missing source witnesses,
- splitting collected works into clean per-paper/per-work units,
- removing publisher apparatus while preserving the public-domain work,
- improving manifests and provenance,
- submitting translation batches with source alignment notes.

Open an issue using the templates in `.github/ISSUE_TEMPLATE/`. Small text corrections can be submitted as pull requests. For large generated artifacts, open an issue first and link the external package or Zenodo/GitHub release asset.

## Key Files

- `STATUS.md`: current release surface and known holds.
- `ROADMAP.md`: practical next steps.
- `data/zenodo/v23_public_check_summary.json`: machine-readable public Zenodo check for v23.
- `data/zenodo/v23_summary.json`: machine-readable v23 build summary.
- `data/manifests/zenodo_v23_upload_files.csv`: v23 upload file list.
- `data/audits/v21_demoted_top_level_reader_pdfs.csv`: reader-surface demotions.
- `data/manifests/v23_kimi7_added_artifacts.csv`: v23 Kimi 7 artifact additions.
- `data/manifests/kimi7_continue_nonscan_delta_summary.json`: current Kimi 7 continuation non-scan web handoff summary.
- `scripts/`: release and audit helpers.

## License

The project coordination material and scripts in this repository are released under CC0 1.0 unless otherwise noted. Historical works, scans, and upstream transcriptions may carry their own public-domain/source status. The Zenodo record currently uses CC BY 4.0 for the dataset metadata/release wrapper.

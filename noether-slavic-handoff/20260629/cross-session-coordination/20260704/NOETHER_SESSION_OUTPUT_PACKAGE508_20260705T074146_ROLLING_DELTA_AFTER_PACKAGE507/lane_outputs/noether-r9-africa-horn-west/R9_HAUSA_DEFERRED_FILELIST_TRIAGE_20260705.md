# R9 Hausa Deferred File-List Triage

Generated: 2026-07-05T05:41:42.924628+00:00 UTC

## Boundary

This artifact converts already-captured metadata for two deferred Hausa leads into file-level triage rows: the Internet Archive `hawiki-Lissafi-20200722.pdf` item file list and the GitHub `FazamMV23/HausaMath` recursive repository tree. It does not download IA file bodies, repository archives, GitHub blob bodies, PDFs, OCR text, rendered app content, or source text. License/access values are metadata signals only, not clearance. No translation, accepted term, native/community review, canonical approval, gate promotion, package action, staging, commit, or Git push is claimed.

## Summary

- Total file-list rows: 82
- Internet Archive file-list rows: 12
- GitHub recursive tree rows: 70
- Rows with `body_saved=false`: 82
- Rows with `source_text_saved=false`: 82
- Rows with `promotion_allowed=false`: 82

## Counts By Lead

| lead | count |
|---|---:|
| FazamMV23/HausaMath | 70 |
| hawiki-Lissafi-20200722.pdf | 12 |

## Counts By Metadata Source

| metadata source | count |
|---|---:|
| GitHub recursive git-tree metadata | 70 |
| Internet Archive metadata file list | 12 |

## Counts By File-List Role

| file-list role | count |
|---|---:|
| ia_derivative_ocr_or_image_file_metadata_only | 3 |
| ia_distribution_sidecar_only | 1 |
| ia_metadata_sidecar_only | 6 |
| ia_static_preview_metadata_only | 1 |
| license_file_metadata_only | 1 |
| public_wiki_pdf_file_metadata_only | 1 |
| repository_directory_metadata_only | 10 |
| repository_readme_metadata_only | 1 |
| static_asset_metadata_only | 43 |
| web_app_source_file_metadata_only | 15 |

## Counts By Decision

| source gate decision | count |
|---|---:|
| not_admitted_filelist_metadata_only | 82 |

## Lead Notes

| lead | current file-list signal | source-gate blocker |
|---|---|---|
| `hawiki-Lissafi-20200722.pdf` | IA metadata lists a small Hausa Wikipedia-derived item with PDF, OCR/derivative, preview, and metadata sidecar files. The item metadata includes `licenseurl=https://creativecommons.org/licenses/by-sa/3.0/`, `creator=Wikipedia`, `language=Hausa`, and `mediatype=texts`. | Public wiki/register metadata can guide discovery, but it is not admitted as target-language mathematical source-corpus evidence until body capture, file hash verification, attribution-chain review, source-owner/reviewer gates, and math-source scope review are handled. |
| `FazamMV23/HausaMath` | GitHub metadata lists 70 recursive tree entries for a small web-app repository, including HTML/CSS/JS files, static assets, README, and `LICENSE`; repo metadata reports MIT license and default branch `main`. | Repository file-list and license metadata can guide controlled capture, but no blob bodies, repository archive, rendered app content, license text body, target-language math fit, or source-owner/reviewer gates were reviewed here. |

CSV: `C:\Users\memo_\Documents\Codex\2026-07-04\noether-r9-africa-horn-west\outputs\R9_HAUSA_DEFERRED_FILELIST_TRIAGE_20260705.csv`

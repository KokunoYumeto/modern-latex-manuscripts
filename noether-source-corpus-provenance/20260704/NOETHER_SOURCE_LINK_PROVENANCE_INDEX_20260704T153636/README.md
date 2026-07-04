# Noether Source Corpus Provenance Link Index

Generated UTC run id: `20260704T153636`

This is the first published source-corpus/provenance foundation for the Noether/interlanguage translation workflow.

It indexes local source-corpus candidate files, extracted URLs/arXiv IDs/DOIs, license-evidence files, redacted secret-scan blockers, and the provided interlanguage transfer zip entries, including GLORD/table-style broad language-analysis grounding material. It also includes split LaTeX payload zips for source-level TeX/LaTeX candidates that passed the blocker scan and path gating.

This is source/provenance infrastructure, not a translation completion claim. It does not claim native review, canonical approval, or full license clearance for every indexed candidate. Generated translations and downstream render/package products are kept out of the source-corpus payload bucket.

Key files:

- `SUMMARY.json` - machine-readable run summary and policy notes.
- `manifests/SOURCE_CORPUS_CANDIDATE_FILE_INDEX.csv` - all indexed source/provenance candidates.
- `manifests/SOURCE_CORPUS_PROVENANCE_LINKS.csv` - extracted URL/arXiv/DOI evidence with credential-like query values redacted.
- `manifests/SOURCE_CORPUS_LATEX_PAYLOAD_MANIFEST.csv` - file-level manifest for LaTeX payload members.
- `manifests/SOURCE_CORPUS_LATEX_PAYLOAD_ZIPS.csv` - hashes and sizes for the split LaTeX payload zips.
- `manifests/CURRENT_20260704_NOETHER_LANE_OUTPUT_INDEX.csv` - current output-file index across the active Noether lane folders.
- `SOURCE_CORPUS_COMPLETION_AUDIT_20260704.md` - requirement-by-requirement completion audit and next publication gaps.
- `payload_zips/` - source-level TeX/LaTeX payload archives.

Three-step publication plan:

1. Upload all source links and provenance indices.
2. Download or retain the open source-level corpus assets referenced by those links.
3. Publish split corpus/provenance zips with manifests and keep generated translations out of the source bucket.

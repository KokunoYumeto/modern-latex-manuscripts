# Arabic RTL Source Bodies Package

Status: local transfer package; draft/source-provenance only.

This package collects the Arabic sublane source bodies and supporting provenance already present on disk in this workspace. It is scoped to Arabic (`ar`) technical or mathematical prose only. It does not claim coverage for Persian, Persianate-neighbor, or Tajik rows.

## Contents

- `source-bodies/pdf/`: 27 downloaded PDF witnesses.
- `source-bodies/doc/`: 1 downloaded DOC witness.
- `source-bodies/native-text/`: 15 raw MediaWiki/Wikibooks text witnesses.
- `source-bodies/native-html/`: 1 native HTML source-body witness.
- `extracted-ocr-witnesses/`: 26 extracted text, first-page, string, or OCR-style check files. These are not treated as native source bodies.
- `provenance/`: 65 HTML metadata pages, HTTP headers, source-archive search results, download probes, blockers, and related access evidence.
- `MANIFEST.csv`: package-level manifest with byte sizes, SHA-256 hashes, and exact source-use labels.
- `manifest.csv` and `manifest.json`: source-witness inventory generated during the first package pass, retained as audit support.
- `SOURCE_USE_LABELS.csv`: package source-use label table.
- `generated-draft/non-canonical/`: scoped non-canonical Arabic active-row draft support for covered rows, kept separate from source bodies.
- `bucket-summary.csv`: count and byte summary by bucket and witness class.
- `EXTENSION_COUNTS.csv`: package file counts by extension, byte totals, and role summary.
- `SHA256SUMS.txt`: whole-package checksum ledger generated after package assembly.
- `LOGBOOK.md`: build decisions, boundaries, and remaining gaps.
- `logs/LOGBOOK_EXCERPT_20260705.md`: logbook excerpt for transfer packaging.

## Boundary Notes

- Native/literal source bodies are separated from OCR/extraction/runtime witnesses.
- Generated Arabic translation drafts, reviewer packets, and gate ledgers are not included.
- Generated non-canonical active-row support is included only under `generated-draft/non-canonical/` and labeled `generated-draft`.
- Existing Arabic evidence tables were used only to annotate manifest rows; this package is not a source-canon approval table by itself.
- No native review, accepted terminology, license clearance, gate promotion, reviewer-packet population, or translation-completion claim is made.
- No Arabic TeX/LaTeX/arXiv/e-print source archive was present in the local Arabic shelf at package time. Search/API probes remain in `provenance/search-results/` as gap evidence.

## Body Counts

The package includes 27 PDF source-body witnesses, 1 DOC source-body witness, 15 raw wiki-text source-body witnesses, 1 native HTML source-body witness, 26 extracted/OCR-style witnesses, 65 provenance/search/blocker witnesses, and 2 generated/non-canonical active-row draft support files. See `EXTENSION_COUNTS.csv`, `SOURCE_USE_LABELS.csv`, and `MANIFEST.csv` for authoritative file-level labels.

## Transfer Note

The current workspace is not a Git repository, so no branch change or Git push was performed. This directory is ready for the transfer/GitHub uploader to review and stage under the shared Noether packaging process.

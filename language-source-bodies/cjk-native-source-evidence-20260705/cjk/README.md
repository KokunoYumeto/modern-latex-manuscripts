# CJK Language Source Bodies

Generated: 2026-07-05T19:04:28+02:00

This directory is a dedicated source-body corpus for CJK mathematical/technical prose used as interlanguage and translation-style baseline evidence. It keeps external/native source bodies separate from generated draft support.

## Required Files

- `MANIFEST.csv`: package manifest with byte counts, SHA-256 hashes, and source-use labels.
- `SHA256SUMS.txt`: checksum replay file for package contents except the checksum file itself.
- `SOURCE_BODIES.csv` / `SOURCE_BODIES.json`: detailed provenance for downloaded source bodies.
- `source-files/`: selected literal source files downloaded from recorded GitHub source-path witnesses.
- `generated-draft/`: non-canonical draft renderings/source-evidence notes/scaffolds for covered rows.
- `logs/LOGBOOK_EXCERPT_20260705.md`: logbook excerpt; full log remains in `logbook.csv/json/md`.

## Counts

- Package files listed: 79
- Native source body rows: 66
- Pointer-only zero-byte rows retained: 3
- Generated draft scaffold rows: 81
- Source language buckets: {'japanese': 28, 'simplified_chinese': 27, 'korean_addendum': 14}
- Source-use label counts: {'generated-draft': 3, 'audit-ledger': 4, 'method-note': 1, 'native-source-body': 66, 'pointer-only': 3, 'manifest': 2}
- Extension counts: {'.csv': 3, '.json': 3, '.md': 12, '.tex': 58, '.cls': 2, '.sty': 1}

## Source-Use Labels

- `native-source-body`: non-empty external source body from a recorded source repository/path.
- `pointer-only`: zero-byte recorded source path retained for audit visibility, not body evidence.
- `generated-draft`: model/project-generated draft scaffold support, non-canonical.
- `manifest`: manifest/checksum/provenance support.
- `audit-ledger`: logbook or audit support.
- `method-note`: README/caveat.

## Boundaries

- This package does not claim native review, canonical approval, accepted terminology, license clearance, gate promotion, source-canon completion, or translation completion.
- Japanese source bodies are target-language mathematical source witnesses only; generated Japanese Noether output is not treated as native CJK evidence.
- Korean material is retained as source-body/addendum evidence when present, not as Korean-school or native-edition authority.
- Generated drafts are explicitly `generated-draft` / `non-canonical` support only.
- License/access fields are recorded as signals for later review; they are not legal clearance.
- No credentials, OCR/runtime caches, `.traineddata`, or `main` branch work are included.

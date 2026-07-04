# Noether Source Witness Acquisition Template

Generated UTC: 2026-07-04T16:40:40Z

Status: reusable source-canon acquisition and publication template. This template records source provenance only. It does not approve terms, translations, bridges, community consent, native review, pilots, or canonical editions.

## Header

```text
Artifact:
Generated UTC:
Lane owner:
Route IDs:
Language / standard / script / stream:
Source-canon priority ID:
Prepared by:
Publication state:
  - source_canon_draft
  - source_canon_captured_not_reviewed
  - source_canon_gap_only
  - source_canon_rejected_candidates_only
```

## Source Witness Table

```text
| witness_id | language_or_standard | script | topic_tags | witness_rank | source_type | original_url_or_archive_locator | local_path | sha256 | license_signal | publication_or_version_date | retrieval_or_archive_date | page_section_theorem_anchor | extraction_or_render_state | source_gap | allowed_use | forbidden_use |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| W001 |  |  |  | editable_source_preferred | TeX/LaTeX/arXiv_source/eprint_source/repository_source/PDF/DOCX/HTML/text/OCR/scan/metadata_only |  |  |  | known/unknown/restricted/public_domain/open_license/custom_license/no_redistribution_signal |  |  |  | not_extracted/text_extracted/OCR_risk/encoding_risk/render_verified/render_failed |  | source provenance only | term approval, bridge approval, community consent, native review, pilot readiness, canonical translation |
```

Witness rank values:

- `rank_1_editable_source`: TeX, LaTeX, repository source, arXiv source bundle, e-print source archive, or equivalent editable source package.
- `rank_2_source_archive`: publisher, project, institutional, or author source archive with version and license signal.
- `rank_3_pdf_provenance`: PDF with stable provenance, page anchors, extraction state, and local hash.
- `rank_4_fallback_text`: DOCX, HTML, text, OCR text, scan, or manual transcription when better source is unavailable.
- `rank_5_metadata_gap`: metadata-only or failed search, recorded only as a source gap.

## Rejected Candidate Table

```text
| candidate_id | candidate_url_or_path | source_type_claimed | reason_rejected | preserved_for_audit | replacement_needed |
| --- | --- | --- | --- | --- | --- |
| R001 |  |  |  | yes/no |  |
```

## Gap Table

```text
| gap_id | route_id | language_or_standard | missing_field | why_it_matters | next_acquisition_action | blocker |
| --- | --- | --- | --- | --- | --- | --- |
| G001 |  |  | source_url/license/hash/local_path/topic_tags/page_anchor/source_file |  |  |  |
```

## Hash Procedure

For every captured local file, compute SHA-256 and record the exact path:

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath '<absolute local path>'
```

If a URL is cited but no file is captured, mark `local_path` and `sha256` as `explicit_gap`, not blank.

## Publication Checklist

- Source manifest exists in `.md` and `.json`.
- Every cited witness has URL or archival locator.
- Every captured file has absolute local path and SHA-256.
- License signal is recorded or marked as explicit gap.
- Topic tags are copied or derived from source metadata, title, abstract, theorem label, or section heading.
- Page, theorem, or section anchor is present when a claim depends on location.
- OCR, encoding, script, and render risks are marked.
- Rejected candidates are preserved.
- Any missing source TeX/LaTeX/arXiv/e-print/source archive is stated as a gap.
- No row claims native/community/project consent, external review, term approval, bridge approval, pilot readiness, canonical translation, or canonical edition.

## Boundary Statement

This artifact may support source provenance, source capture, reproducibility, and gap triage. It may not support acceptance of terminology, bridge surfaces, native/community authority, project consent, reviewer completion, learner-facing pilot readiness, or canonical publication.

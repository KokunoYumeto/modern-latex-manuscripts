# Workflow Addendum 2026-06-24: Archive Scope Guardrail

This addendum records a publication-scope correction for the AI-run manuscript archive workflow. The local sweep process is allowed to inspect many folders, but publication is limited to the transcription/translation/source-audit project unless Floris explicitly requests a named non-project upload.

## Rule

A file being mathematical, interesting, recently downloaded, or technically publishable is not enough. The file must belong to one of the existing project lanes: source scans, source witnesses, TeX transcriptions, translations, audit ledgers, repair packages, workflow/methodology notes, or author/corpus public-surface metadata for the manuscript project.

Unrelated third-party TeX, new research drafts, Reddit downloads, personal/novel math files, and loose Lean experiments stay out of Zenodo and out of the GitHub mirror unless explicitly named by Floris as an external upload. Coherent buildable Lean 4 / mathlib-style packets can be routed as a clearly labelled Lean/library-candidate companion lane, but not as proof, certification, source audit, or correctness evidence for the historical archive.

## Sweep Classifications

- project_candidate: eligible for routing/staging only after inspection and caveat assignment.
- downloads_review_do_not_upload_by_default: can be read for context, but not staged or uploaded by default.
- OUT_OF_SCOPE_unless_explicitly_requested: quarantine from publication unless Floris explicitly names that file or record.
- review: ambiguous project-management material; use only if it improves workflow/status accuracy.

## DOI Hygiene

Use existing author, corpus, workflow, or raw/provenance DOI lanes whenever possible. Do not create new DOI records just because a package exists. A new DOI is justified only when a coherent author/work/corpus surface has enough reader-facing value or when Floris explicitly asks for it.

## Public Claims

Publication metadata must distinguish reader-facing editions, source-witness/support packages, OCR locator layers, survival/audit bundles, superseded provenance holds, and actual source-closed loci. Internal labels such as complete, accepted, or source-checked are not public proof.

## Current Sweep Result

The 2026-06-24 scoped sweep found recent project packages that needed Noether staging and many unrelated Downloads/new-math-style files that must remain out of scope. After staging the legitimate Noether packages, the recent project-ZIP comparison against the GitHub mirror returned zero unstaged project ZIPs by filename. Internal PDFs inside support ZIPs were not promoted separately.

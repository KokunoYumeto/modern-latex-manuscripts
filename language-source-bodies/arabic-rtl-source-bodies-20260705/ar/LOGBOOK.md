# Arabic Source Bodies Logbook

## 2026-07-05

- Goal set verbatim from the coordinator instruction for Session 06, Arabic / Persianate / RTL Source Bodies, Arabic sublane.
- Checked the current workspace and confirmed it is not a Git repository. No Git push or branch operation was performed.
- Read the local Arabic source shelf under `sources/non_slavic_reference_corpus/`.
- Built `language-source-bodies/rtl-persianate-arabic/ar/` as a local transfer package.
- Copied 135 existing Arabic-lane witness files:
  - 27 PDF source-body witnesses.
  - 1 DOC source-body witness.
  - 15 raw MediaWiki/Wikibooks text witnesses.
  - 1 native HTML source-body witness.
  - 26 extracted/OCR-style text witnesses, kept outside source-body buckets.
  - 65 provenance, search-result, download-probe, blocker, header, and metadata witnesses.
- Generated `manifest.csv`, `manifest.json`, and `bucket-summary.csv` from copied package files.
- Manifest rows include original local paths, package-relative paths, file sizes, SHA-256 hashes, witness class, Arabic-only language boundary, and non-claim boundary.
- Existing Arabic source-canon CSVs in `outputs/` were used to enrich manifest rows with matched URLs, license/access signals, topic tags, RTL/script notes, and status/gap notes where local-path matching was possible.
- Generated `SHA256SUMS.txt` and replayed the ledger: 140 entries checked with 0 mismatches before this logbook update.
- Ran a filename boundary scan for draft/corpus/translation/reviewer/packet/gate terms. The only hit was `researchgate_invariant_theory_sections_probe.html`, a provenance page whose provider name contains `gate`; it is not a gate ledger or reviewer artifact.
- Read remote side-branch directive files at commit `2d72c779f8bb8e46ee3ce0ba76731eb9cf4a2914`: `00_SET_EVERY_ASSIGNED_GOAL_VERBATIM_NOW_20260705.md`, `00_DISPATCH_ALL_IDLE_SESSIONS_NOW_20260705.md`, and `SET_THIS_AS_YOUR_GOAL_VERBATIM_20260705.md`.
- Reset the pursued goal verbatim for Session 06-Arabic-Split.
- Added `generated-draft/non-canonical/` with Arabic active-row draft support copied from the current Arabic row workup, labeled as generated/non-canonical support and kept separate from source bodies.
- Added package-shape support for `MANIFEST.csv`, source-use labels, extension counts, and logbook excerpt.

## Explicit Boundaries

- Arabic source evidence here does not authorize Persian, Persianate, or Tajik rows.
- OCR/extraction/textcheck files are not native source bodies and are separated under `extracted-ocr-witnesses/`.
- HTML article pages and metadata pages are mostly provenance only unless explicitly bucketed as `source-bodies/native-html/`.
- Search/API result files are provenance for the source-archive gap, not source bodies.
- Generated translation drafts and reviewer-facing approval packets are excluded.
- No native-review, accepted-terminology, license-clearance, gate-promotion, reviewer-packet, or translation-completion claim is made.

## Open Gaps

- Direct Arabic TeX/LaTeX/arXiv/e-print source packages remain absent from the local shelf.
- Specialist invariant/covariant Arabic source-body coverage remains provenance/gap-heavy and should not be treated as closed.
- License/access signals are recorded as evidence only. They are not reuse clearance.
- RTL/PDF rendering QA is still required before any source-body-derived Arabic examples are promoted into reviewer or canonical contexts.

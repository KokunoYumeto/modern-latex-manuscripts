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
- Fixed Windows case-preservation issue by moving the package manifest through an intermediate path so the required file name is `MANIFEST.csv`.
- Restored the first-pass source-witness inventory as `SOURCE_WITNESS_MANIFEST.csv`; `manifest.json` remains as the JSON form of that inventory.
- Current source-use label counts before final reseal: 44 `native-source-body`, 26 `OCR-witness`, 2 `generated-draft`, 56 `pointer-only`, 9 `rejected`, 2 `manifest`, 3 `audit-ledger`, and 4 `method-note` rows in `MANIFEST.csv`.

## 2026-07-05T20:35Z

- Ran a focused Fable/source-canon recovery probe for Arabic TeX/source-package and invariant-theory gaps.
- Added one Arabic technical `.tex` source body from the GitHub-hosted Arabic LaTeX book source into `source-bodies/native-tex/`.
- Added invariant-theory provenance and Internet Archive dictionary OCR/text evidence into separated provenance/OCR buckets.
- Updated `MANIFEST.csv`, `SOURCE_USE_LABELS.csv`, `EXTENSION_COUNTS.csv`, and `SHA256SUMS.txt`.
- Source-use label counts after this pass: 45 `native-source-body`, 27 `OCR-witness`, 2 `generated-draft`, 69 `pointer-only`, 9 `rejected`, 2 `manifest`, 3 `audit-ledger`, and 4 `method-note` rows.
- Boundary: the recovered `.tex` source is Arabic technical/LaTeX prose, not algebra-term approval and not Persianate evidence. Algebra-specific Arabic TeX/source-package and specialist invariant/covariant source-body gaps remain active.

## 2026-07-05T21:45+02:00

- Ran Arabic source-canon recovery round 2 and added the package ledger `ROUND2_SOURCE_CANON_LEDGER_20260705.csv` plus the readable note `ROUND2_SOURCE_CANON_LEDGER_20260705.md`.
- Added three Arabic PDF source bodies into `source-bodies/pdf/20260705T213000Z_arabic_source_canon_round2/`: a Tiaret linear-algebra course, the HIAST/Kouba algebra volume 2 PDF, and the Arab Academy mathematics terminology dictionary.
- Added `nagwa_arabic_math.dtx` into `source-bodies/native-tex/20260705T213000Z_arabic_source_canon_round2/`; the file header signals CC0 and supports Arabic mathematical notation in LuaTeX, so it is useful for RTL/formula-rendering provenance.
- Kept the Shamra finite-field page, HTTP headers, GitHub pointer files, curl progress logs, and license/pointer files in provenance buckets rather than native source-body buckets.
- Extracted first-eight-page text from the three PDFs for string/topic checks and kept those files under `extracted-ocr-witnesses/`; extraction logs and summaries were moved to provenance.
- Resealed package metadata: 194 `MANIFEST.csv` rows and 195 `SHA256SUMS.txt` entries; checksum replay checked 195 files with 0 missing or mismatched entries; `SHA256SUMS.txt` hash `3AEAD14E9D5750C1E99776AD2DEAE05892E31E8F0A6B9AF727FB981268C9154F`.
- Current source-use label counts after round 2: 49 `native-source-body`, 30 `OCR-witness`, 3 `generated-draft`, 95 `pointer-only`, 7 `rejected`, 3 `manifest`, 3 `audit-ledger`, and 4 `method-note` rows.
- Boundary: the new PDF bodies improve Arabic algebra/linear-algebra/terminology coverage, and the `.dtx` improves Arabic math-rendering source coverage. They do not establish native review, accepted terms, license clearance, source certification, Persianate coverage, or translation completion.

## 2026-07-05T23:55+02:00

- Ran Arabic algebra-specific TeX/source-package recovery round 3 and added `ROUND3_ARABIC_ALGEBRA_TEX_SOURCE_RECOVERY_LEDGER_20260705.csv` plus `.md`.
- GitHub code searches for Arabic algebra terms with `.tex` constraints returned zero direct hits for the searched strings.
- GitHub repository searches for Arabic algebra/math/LaTeX combinations returned zero repository hits for the searched strings after correcting the JSON field query.
- Downloaded CTAN/TeX/Khatt provenance pages for ArabTeX, ArabLuaTeX, CTAN Arabic topic, Arabic mathematical symbols in LaTeX, and Khatt Arabic mathematical notation. These are provenance/pointer files, not native algebra source bodies.
- Inventoried the local Arabic TeX-like source bodies: the Arabic LaTeX book `.tex` and `nagwa_arabic_math.dtx` remain useful partial RTL/TeX support, but they do not close the algebra-specific Arabic TeX/LaTeX/arXiv/e-print source-package gap.
- Copied round-3 search results and downloaded provenance into `provenance/source-recovery-round3/20260705T235000Z_arabic_algebra_tex_source_recovery_round3/`.
- Boundary: round 3 is blocker/recovery evidence only. It does not add a native algebra TeX source body, does not certify sources or licenses, and does not approve terminology.

## Explicit Boundaries

- Arabic source evidence here does not authorize Persian, Persianate, or Tajik rows.
- OCR/extraction/textcheck files are not native source bodies and are separated under `extracted-ocr-witnesses/`.
- HTML article pages and metadata pages are mostly provenance only unless explicitly bucketed as `source-bodies/native-html/`.
- Search/API result files are provenance for the source-archive gap, not source bodies.
- Generated translation drafts and reviewer-facing approval packets are excluded.
- No native-review, accepted-terminology, license-clearance, gate-promotion, reviewer-packet, or translation-completion claim is made.

## Open Gaps

- Algebra-specific Arabic TeX/LaTeX/arXiv/e-print source packages remain absent from the local shelf; current TeX coverage is Arabic technical/LaTeX prose and Arabic math-rendering/tooling source, not algebra-source-package closure.
- Specialist invariant/covariant Arabic source-body coverage remains provenance/gap-heavy and should not be treated as closed.
- License/access signals are recorded as evidence only. They are not reuse clearance.
- RTL/PDF rendering QA is still required before any source-body-derived Arabic examples are promoted into reviewer or canonical contexts.

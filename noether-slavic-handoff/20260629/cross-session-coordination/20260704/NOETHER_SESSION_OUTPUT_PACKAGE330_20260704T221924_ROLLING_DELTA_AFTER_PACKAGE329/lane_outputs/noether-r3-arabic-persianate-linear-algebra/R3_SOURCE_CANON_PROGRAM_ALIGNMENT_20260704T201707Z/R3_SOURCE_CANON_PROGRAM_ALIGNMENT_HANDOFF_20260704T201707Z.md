# R3 Source-Canon Program Alignment Handoff

Created UTC: 20260704T201707Z

Status: source-canon/provenance alignment only. This artifact does not create translation output, glossary expansion, bridge promotion, native-review claims, canonical approvals, license-clearance claims, gate-promotion claims, completion claims, package claims, or Git pushes.

## What This Adds

- Normalized the current R3 source-canon witness ledger into the parent-required witness table shape:
  - `lane`
  - `target_language_or_access_target`
  - `source_title`
  - `source_author_or_owner`
  - `topic_tags`
  - `evidence_tier`
  - `source_type`
  - `source_url`
  - `local_path`
  - `license_or_access_signal`
  - `sha256_or_other_hash`
  - `source_language`
  - `is_target_language_witness`
  - `is_source_level_tex_or_archive`
  - `is_pdf_docx_or_text_fallback`
  - `gap_or_blocker_note`
  - `non_claim_boundary`
- Recorded source-canon instruction rechecks from `AGENTS.md` and `.github/copilot-instructions.md` on `origin/codex/noether-pc-20260629` at commit `6f756fcf3ab0528ab6286c4ee53f69ff956bf82a`.
- Rechecked parent ledger, source-canon steering record, B3 steward log, Arabic RTL witness table, Persianate/Tajik witness table, R2 Pan-Turkic register, and interlanguage source-canon priority ledger.
- Added row-level external witness pointers from the Arabic RTL and Persianate/Tajik source-canon tables so their URLs, hashes, license/access signals, language tags, and blocker boundaries are findable without importing authority claims.
- Emitted unpacked sidecars only. B3 remains the package/push owner.

## Current Counts

- Normalized R3 rows: 22
- Cross-lane recheck rows: 10
- External lane witness pointer rows: 25
- Source-level TeX/archive/package rows: 3
- PDF/text/catalog fallback rows: 16
- Explicit gap rows: 3
- Fetch-failed rows: 1

## Routing Boundaries

- Arabic rows route only to the Arabic RTL source-canon lane as controlled Arabic evidence. The Arabic RTL table has stronger direct algebra/ring PDFs; R3 Arabic rows remain adjacent linear-algebra or invariant-context provenance.
- Persian/Farsi rows route only to the fa_IR side of the Persianate/Tajik lane. R3 does not let fa_IR evidence authorize Dari, Tajik, Urdu, Hindustani, or Pan-Turkic rows.
- Dari/Afghan Persian rows route only to the prs_AF separate gate; failed PDF/candidate rows remain blockers.
- Tajik Cyrillic rows route only to the tg_Cyrl_TJ separate gate and remain adjacent linear-algebra provenance.
- Pan-Turkic material remains separate under R2; no R3 Arabic/Persianate evidence is inherited by Pan-Turkic rows.

## Files

- Required-shape witness table CSV: `C:\Users\memo_\Documents\Codex\2026-07-04\noether-r3-arabic-persianate-linear-algebra\outputs\R3_SOURCE_CANON_PROGRAM_ALIGNMENT_20260704T201707Z\R3_SOURCE_CANON_REQUIRED_SHAPE_WITNESS_TABLE_20260704T201707Z.csv`
- Required-shape witness table JSON: `C:\Users\memo_\Documents\Codex\2026-07-04\noether-r3-arabic-persianate-linear-algebra\outputs\R3_SOURCE_CANON_PROGRAM_ALIGNMENT_20260704T201707Z\R3_SOURCE_CANON_REQUIRED_SHAPE_WITNESS_TABLE_20260704T201707Z.json`
- Cross-lane recheck CSV: `C:\Users\memo_\Documents\Codex\2026-07-04\noether-r3-arabic-persianate-linear-algebra\outputs\R3_SOURCE_CANON_PROGRAM_ALIGNMENT_20260704T201707Z\R3_SOURCE_CANON_CROSS_LANE_RECHECK_20260704T201707Z.csv`
- Cross-lane recheck JSON: `C:\Users\memo_\Documents\Codex\2026-07-04\noether-r3-arabic-persianate-linear-algebra\outputs\R3_SOURCE_CANON_PROGRAM_ALIGNMENT_20260704T201707Z\R3_SOURCE_CANON_CROSS_LANE_RECHECK_20260704T201707Z.json`
- External lane witness pointers CSV: `C:\Users\memo_\Documents\Codex\2026-07-04\noether-r3-arabic-persianate-linear-algebra\outputs\R3_SOURCE_CANON_PROGRAM_ALIGNMENT_20260704T201707Z\R3_SOURCE_CANON_EXTERNAL_LANE_WITNESS_POINTERS_20260704T201707Z.csv`
- External lane witness pointers JSON: `C:\Users\memo_\Documents\Codex\2026-07-04\noether-r3-arabic-persianate-linear-algebra\outputs\R3_SOURCE_CANON_PROGRAM_ALIGNMENT_20260704T201707Z\R3_SOURCE_CANON_EXTERNAL_LANE_WITNESS_POINTERS_20260704T201707Z.json`
- Validation JSON: `C:\Users\memo_\Documents\Codex\2026-07-04\noether-r3-arabic-persianate-linear-algebra\outputs\R3_SOURCE_CANON_PROGRAM_ALIGNMENT_20260704T201707Z\R3_SOURCE_CANON_PROGRAM_ALIGNMENT_VALIDATION_20260704T201707Z.json`
- Manifest JSON: `C:\Users\memo_\Documents\Codex\2026-07-04\noether-r3-arabic-persianate-linear-algebra\outputs\R3_SOURCE_CANON_PROGRAM_ALIGNMENT_20260704T201707Z\R3_SOURCE_CANON_PROGRAM_ALIGNMENT_MANIFEST_20260704T201707Z.json`

# Noether Source-Corpus Completion Audit

Generated: 2026-07-04

This audit records what the current source-corpus/provenance publication proves, what it only partially proves, and what still remains before any translation lane can claim source-grounded completion. It is intentionally separate from native review, canonical approval, and translation promotion.

## Objective Requirements

1. Publish source links and provenance indices across useful local corpus lanes.
2. Retain, organize, and make discoverable open-source source-level mathematical corpus assets.
3. Include TeX/LaTeX plus source archives, PDF/DOCX/text evidence, manifests, URLs, license signals, and GLORD/table-style broad language-analysis grounding material.
4. Publish usable GitHub artifacts as searchable manifests and zip payloads.
5. Keep generated translations separate from source corpus material.
6. Preserve draft/non-canonical/support labels.
7. Avoid credentials and raw unverified dumps.
8. Avoid native-review, canonical-approval, and license-clearance claims not proven by evidence.

## Evidence Now Published

- Publication root:
  `noether-source-corpus-provenance/20260704/NOETHER_SOURCE_LINK_PROVENANCE_INDEX_20260704T153636`.
- Candidate source/provenance files indexed: 22,437.
- Provenance links extracted: 101,742.
- License-evidence files indexed: 157.
- Transfer zip entries indexed: 2,103.
- Source-level TeX/LaTeX candidates indexed: 10,870.
- LaTeX payload manifest rows: 10,517.
- Unique LaTeX payload files zipped: 3,495.
- Current 2026-07-04 lane output artifacts indexed: 866 files across 15 Noether lanes.
- Current lane-output index:
  `manifests/CURRENT_20260704_NOETHER_LANE_OUTPUT_INDEX.csv`,
  SHA-256 `8FE1A1A461B2EFC79A90431D3883E55E3C9FD16040A4553ACF973FB4A0AA50C8`.

## Requirement Status

| Requirement | Status | Evidence |
| --- | --- | --- |
| Source links/provenance indices | Partial but published | `SOURCE_CORPUS_PROVENANCE_LINKS.csv`, `SOURCE_CORPUS_CANDIDATE_FILE_INDEX.csv`, `CURRENT_20260704_NOETHER_LANE_OUTPUT_INDEX.csv` |
| Open source-level mathematical assets | Partial | LaTeX payload zips are published; PDF/DOCX/source archives remain manifest-only pending license/source gating |
| TeX/LaTeX payload | Published | `SOURCE_CORPUS_LATEX_PAYLOAD_MANIFEST.csv` and two `payload_zips/NOETHER_SOURCE_CORPUS_LATEX_PAYLOAD_*.zip` archives |
| PDF/DOCX/text/source-archive evidence | Manifest-only | Candidate and lane-output manifests classify these assets, but payload publication is not yet complete |
| License/provenance signals | Partial | `SOURCE_CORPUS_LICENSE_EVIDENCE_FILES.csv`; individual assets are not globally license-cleared |
| GLORD/table-style grounding | Indexed | `INTERLANGUAGE_TRANSFER_ZIP_ENTRY_INDEX.csv` flags transfer-zip GLORD/table/language-analysis candidates |
| Generated translations separated | Published policy and manifest categories | `SOURCE_PUBLICATION_POLICY.md`, `README.md`, and generated/downstream manifest-only categories |
| No credential leakage | Passed current gates | 55 blocker rows are redacted path/reason records; 60 credential-like link values redacted; final scans found no publish-blocking patterns |
| No native-review/canonical approval claim | Passed current gates | README and policy state this is source/provenance infrastructure only |

## Current Gaps

- The publication does not prove that every indexed candidate is open-source or redistributable.
- The PDF/DOCX/source-archive payloads are not yet zipped for GitHub; they are present as searchable provenance/candidate records until license/source gating is complete.
- The current LaTeX payload excludes blocker-scan paths and generated/downstream paths; those excluded files require manual review before any future payload inclusion.
- Current lane outputs are indexed for discovery, but only source/provenance assets should be promoted into corpus payloads.
- Translation lanes still need to be rated against these source witnesses before any renewed translation or interlanguage approval claim.

## Next Publication Steps

1. Use `CURRENT_20260704_NOETHER_LANE_OUTPUT_INDEX.csv` to identify lane-local source evidence not already covered by the primary source roots.
2. For each PDF/DOCX/source archive candidate, verify source URL, license/redistribution signal, and whether the file is source evidence or generated downstream work.
3. Publish additional payload zips only for assets that pass the license/source gate.
4. Keep all translation outputs draft/non-canonical until they have been checked against the published source witnesses and any new native review evidence.

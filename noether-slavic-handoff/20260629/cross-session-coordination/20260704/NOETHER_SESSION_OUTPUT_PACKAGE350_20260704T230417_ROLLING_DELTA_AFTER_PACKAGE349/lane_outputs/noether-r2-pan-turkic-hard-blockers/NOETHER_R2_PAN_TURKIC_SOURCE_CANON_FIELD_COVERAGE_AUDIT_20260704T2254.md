# R2 Pan-Turkic Source-Canon Field Coverage Audit

Prepared: 2026-07-04T22:54+02:00

Scope: source-canon/provenance field-coverage audit for the R2 Pan-Turkic normalized register. This checks required witness-table fields, explicit hard-blocker gap rows, local file existence, and local SHA-256 matches. It does not add translation output or promote any term, bridge, review, approval, license, gate, Zenodo, or Git state.

## Control And Git State

- AGENTS.md SHA-256: EE41CF302952ADC624160B9A94CC5AE4CD3EB61B309115F61D1316D0EF039548.
- .github/copilot-instructions.md SHA-256: CBF1788357F102CE372EF35606FD931AE8A79F782C1B495C96B78351A93AE34A.
- Parent ledger SHA-256: F7D49B47107E8F33151E93B0C48EED3CCD5AFDEBCE124FD3D1FABA1A0271EE3F.
- Source-canon steering SHA-256: 531B9E358E52BDE20F613E75B8DE33558C05301CA971639E727DD584B34205C4.
- B3 steward log SHA-256: D90B72C21DB212355FBACEFB51C9A965C4DC0145E869FAB54B39C77F533E7C0D.
- Git HEAD observed: c7588b53d5d37d71081c5c143b5d2636aad5d262.
- Git upstream observed: c7588b53d5d37d71081c5c143b5d2636aad5d262.
- Git status observed: ## codex/noether-pc-20260629...origin/codex/noether-pc-20260629.

## Register Counts

- Total rows: 61.
- Row kinds: exact_candidate_witness=7; explicit_hard_blocker_gap=8; ocr_source_witness=2; source_witness=44.
- Language/access-target counts: Kyrgyz=13; Tatar=14; Tatar-region lead=1; Turkmen=13; Uyghur=20.
- Evidence tiers: explicit_gap_or_blocker=8; html_or_web_fallback=29; pdf_or_text_fallback=24.
- Source-level TeX/LaTeX/arXiv/e-print/source-archive rows in R2: 0.
- Explicit hard-blocker gap rows: 8.

## Field Coverage

All shared required fields are present across 61 rows; non-gap source/candidate/OCR rows have URL/path/hash/license/topic/language/upload-policy fields present; gap rows have explicit blocker notes.

Local file/hash audit:

- Non-gap source/candidate/OCR rows checked: 53.
- Local path/hash failures: 0.
- Grouped status: False, not_applicable_gap_or_no_local_file=8; True, match=53.

Target-language witness flag audit:

- Target-language witness rows: 52.
- Explicit non-target/gap-labeled rows: 9.
- Non-target/gap-labeled IDs: SCW-TT-003; EHR-TT-NR-001; EHR-TT-PR-001; EHR-KY-NR-001; EHR-KY-PR-001; EHR-TK-NR-001; EHR-TK-PR-001; EHR-UG-NR-001; EHR-UG-PR-001.

## Machine Files

- outputs/NOETHER_R2_PAN_TURKIC_SOURCE_CANON_FIELD_COVERAGE_AUDIT_20260704T2254.csv
- outputs/NOETHER_R2_PAN_TURKIC_SOURCE_CANON_FIELD_COVERAGE_AUDIT_20260704T2254.json
- outputs/NOETHER_R2_PAN_TURKIC_SOURCE_CANON_FIELD_COVERAGE_ROW_AUDIT_20260704T2254.csv
- outputs/NOETHER_R2_PAN_TURKIC_SOURCE_CANON_FIELD_COVERAGE_ROW_AUDIT_20260704T2254.json

## Boundary

No translation output, glossary/term promotion, Pan-Turkic bridge, pilot, native/community-review claim, canonical approval claim, accepted terminology claim, license-clearance claim, gate promotion, Zenodo action, canonical source edit, Git stage, Git commit, or Git push is made here.

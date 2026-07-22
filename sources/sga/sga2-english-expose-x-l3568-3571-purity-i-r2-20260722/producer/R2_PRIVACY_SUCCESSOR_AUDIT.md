# R2 privacy successor audit

Status: `PRODUCER_R2_PASS_PENDING_FRESH_INDEPENDENT_REVIEW`.

## Scope preserved

This is a no-overwrite evidence/privacy successor to the original producer package. The target translation is not revised. Its admitted French scope remains lines 3568–3571 inclusive, with raw cursor 3572 and substantive cursor 3573. Original printed pp. 121–122, source-PDF physical p. 105, and recomposed running p. 97 remain distinct.

The predecessor directory remains unchanged. This successor must reproduce its target TeX and PDF byte-for-byte while replacing the privacy-defective build-log and dependent validation surface.

## Independent failure bound

Confirmed finding `IR-SGA2-X-PURITYI-PRIVACY-001` identifies 12 line-dewrapped private-user occurrences: four in each predecessor `BUILD_PASS1.log`, `BUILD_PASS2.log`, and `BUILD_PASS3.log`. Their raw predecessor bytes are not copied here. Only their exact identities and the independent finding controls are retained as restricted predecessor bindings.

Bound independent controls:

- `INDEPENDENT_FINAL_AUDIT.md`: 4,574 B, SHA-256 `6FCB5DA35D1646D5252873AE9990823A11D8835AD0E50AB77226E92A558D5C4C`;
- `INDEPENDENT_VALIDATION.json`: 8,319 B, SHA-256 `84C65379946A92DE959E70C277874C5324BB049861E405B2836618861F74A866`;
- `INDEPENDENT_FINDINGS.csv`: 541 B, SHA-256 `0ED5B973C0C2C9C1097A487D627329CBCFEFAFC636C9224142B6281D0E9C0B23`;
- `INDEPENDENT_PRIVACY_HIT_EVIDENCE.json`: 1,719 B, SHA-256 `9D249259F0B7769310BB40FE445A7C89849DD745C1F88D32021FB777FA35E9C8`.

## R2 remediation policy

R2 builds from the unchanged TeX in an isolated temporary directory with relative input names. Raw subprocess output is held only in memory long enough to hash and sanitize it. The package retains sanitized build logs and a machine ledger binding raw bytes/hashes, replacement counts, and sanitized bytes/hashes. No raw R2 build log is retained.

Sanitization recognizes private roots even when line wrapping occurs inside any character sequence. The successor privacy gate scans literal text, line-dewrapped text, whitespace-compacted text, slash-normalized variants, and percent-decoded variants. Ephemeral regression fixtures cover forward slashes, backslashes, and mid-token line wrapping; the fixtures themselves are never written into the package.

## Revision and release state

The R2 machine ledger carries predecessor and successor records together. Every revised record has `revision_of` and `supersedes` links to its predecessor; every predecessor has a reciprocal `superseded_by` link. The independent finding and the R1 privacy false-pass are separately bound.

All R2 artifacts remain `internal_not_for_release`. Fresh independent review is required. No seal, cumulative integration, manager/shared-log write, archive handoff, GitHub action, or Zenodo action is claimed.

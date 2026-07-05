# Noether CJK Source License/Access Boundary Audit

Generated: 2026-07-05T03:41:03+02:00

Purpose: normalize upload/reuse boundaries for CJK source-canon GitHub/source-archive witnesses. This audit keeps source evidence findable while preventing rolling-package raw-source or archive payload leakage.

## Summary

- Rows audited: 21.
- Access classes: {'manifest_only_raw_payload_blocked_pending_license_access_review': 13, 'manifest_only_payload_requires_dedicated_b3_license_review': 4, 'gap_or_nonpayload_row': 4}.

| Target/access | Repository/title | License/access signal | Access class | Upload policy |
| --- | --- | --- | --- | --- |
| Japanese | homuralove/linear-algebra | No GitHub license detected in repository metadata; manual license/access review required | manifest_only_raw_payload_blocked_pending_license_access_review | manifest_only |
| Japanese | HideakiHosaka/2015_linear_algebra | No GitHub license detected in repository metadata; manual license/access review required | manifest_only_raw_payload_blocked_pending_license_access_review | manifest_only |
| Japanese | t-higashida/linear_algebra | No GitHub license detected in repository metadata; manual license/access review required | manifest_only_raw_payload_blocked_pending_license_access_review | manifest_only |
| Japanese | rsato64/relativisticQM | No GitHub license detected in repository metadata; manual license/access review required | manifest_only_raw_payload_blocked_pending_license_access_review | manifest_only |
| Simplified Chinese | zhcosin/algebra-notes | No GitHub license detected in repository metadata; manual license/access review required | manifest_only_raw_payload_blocked_pending_license_access_review | manifest_only |
| Simplified Chinese | Kfj2006/Algebra_notes | No GitHub license detected in repository metadata; manual license/access review required | manifest_only_raw_payload_blocked_pending_license_access_review | manifest_only |
| Simplified Chinese | ayhe123/algebra-lecturenote | GitHub license signal: CC-BY-4.0 (Creative Commons Attribution 4.0 International); not legal clearance | manifest_only_payload_requires_dedicated_b3_license_review | manifest_only |
| Simplified Chinese | GooduckZ/Linear-Algebra-for-ZJUCKC | GitHub license signal: NOASSERTION; manual review required | manifest_only_raw_payload_blocked_pending_license_access_review | manifest_only |
| Simplified Chinese | yhwu-is/Linear-Algebra-Left-Undone | GitHub license signal: NOASSERTION; manual review required | manifest_only_raw_payload_blocked_pending_license_access_review | manifest_only |
| Simplified Chinese | DolveKD/Advanced-Algebra-Notes | No GitHub license detected in repository metadata; manual license/access review required | manifest_only_raw_payload_blocked_pending_license_access_review | manifest_only |
| Simplified Chinese | arshtyi/Advanced-Algebra | GitHub license signal: MIT (MIT License); not legal clearance | manifest_only_payload_requires_dedicated_b3_license_review | manifest_only |
| Korean addendum/source routing | gshstexsociety/examples | No GitHub license detected in repository metadata; manual license/access review required | manifest_only_raw_payload_blocked_pending_license_access_review | manifest_only |
| Korean addendum/source routing | alstn2468/category-theory-for-programmers | GitHub license signal: MIT (MIT License); not legal clearance | manifest_only_payload_requires_dedicated_b3_license_review | manifest_only |
| Korean addendum/source routing | Korean modern/abstract algebra source-level TeX recheck | not applicable; no exact source-level repository witness accepted from this query | gap_or_nonpayload_row | gap_row_only |
| Japanese | Japanese exact abstract/modern algebra source-level TeX recheck | not applicable; no exact source-level repository witness accepted from this query | gap_or_nonpayload_row | gap_row_only |
| Japanese | imamuray/algebraic-systems | No GitHub license detected in repository search result; manual license/access review required | manifest_only_raw_payload_blocked_pending_license_access_review | manifest_only |
| Japanese | t-higashida/commutative_ring_and_field | No GitHub license detected in repository search result; manual license/access review required | manifest_only_raw_payload_blocked_pending_license_access_review | manifest_only |
| Japanese | Seasawher/matsumura | GitHub search license signal: GPL-3.0; not legal clearance | manifest_only_payload_requires_dedicated_b3_license_review | manifest_only |
| Korean addendum/source routing | calofmijuck/algebra | No GitHub license detected in repository search result; manual license/access review required | manifest_only_raw_payload_blocked_pending_license_access_review | manifest_only |
| Japanese | Japanese algebra source coverage residual | not applicable; coverage residual row | gap_or_nonpayload_row | gap_row_only |
| Korean addendum/source routing | Korean algebra source coverage residual | not applicable; coverage residual row | gap_or_nonpayload_row | gap_row_only |

## Boundary Rules Applied

- Repositories with no detected license, `NOASSERTION`, or manual-review signals stay manifest-only.
- Repositories with apparent MIT/GPL/CC-BY signals still stay manifest-only in this lane; payload requires dedicated B3/license review.
- Gap rows remain gap/provenance rows with no source payload.
- Archive URLs are recorded for findability, not as permission to package archive files.
- No translation, glossary promotion, native/public signoff, canonical approval, license clearance, Korean-school claim, pan-CJK claim, gate promotion, or completion claim is made.

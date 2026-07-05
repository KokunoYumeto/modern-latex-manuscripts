# Noether CJK Explicit Bytecount and Upload-Policy Normalization

Generated: 2026-07-05T13:27:09+02:00

Purpose: make the CJK source-canon findability index machine-checkable for the downstream requirement that witness rows expose explicit `byte_count` and `upload_policy` fields, or exact gap values. Byte counts are parsed only from existing source-path evidence; no raw source body or archive is fetched or packaged.

## Summary

- Rows normalized: 21.
- Upload policy counts: {'manifest_only': 17, 'gap_row_only': 4}.
- Byte count status counts: {'explicit_source_path_byte_count_present': 13, 'exact_gap_row_no_source_payload_byte_count': 4, 'source_metadata_without_exact_payload_byte_count': 4}.
- Target/access counts: {'Japanese': 9, 'Simplified Chinese': 7, 'Korean addendum/source routing': 5}.

| ID | Target/access | Repository/title | Upload policy | Byte count status | Byte count total |
| --- | --- | --- | --- | --- | ---: |
| CJK-BYTE-UPLOAD-20260705-001 | Japanese | homuralove/linear-algebra | manifest_only | explicit_source_path_byte_count_present | 106732 |
| CJK-BYTE-UPLOAD-20260705-002 | Japanese | HideakiHosaka/2015_linear_algebra | manifest_only | explicit_source_path_byte_count_present | 130199 |
| CJK-BYTE-UPLOAD-20260705-003 | Japanese | t-higashida/linear_algebra | manifest_only | explicit_source_path_byte_count_present | 20436 |
| CJK-BYTE-UPLOAD-20260705-004 | Japanese | rsato64/relativisticQM | manifest_only | explicit_source_path_byte_count_present | 19698 |
| CJK-BYTE-UPLOAD-20260705-005 | Simplified Chinese | zhcosin/algebra-notes | manifest_only | explicit_source_path_byte_count_present | 24571 |
| CJK-BYTE-UPLOAD-20260705-006 | Simplified Chinese | Kfj2006/Algebra_notes | manifest_only | explicit_source_path_byte_count_present | 93489 |
| CJK-BYTE-UPLOAD-20260705-007 | Simplified Chinese | ayhe123/algebra-lecturenote | manifest_only | explicit_source_path_byte_count_present | 344379 |
| CJK-BYTE-UPLOAD-20260705-008 | Simplified Chinese | GooduckZ/Linear-Algebra-for-ZJUCKC | manifest_only | explicit_source_path_byte_count_present | 16231 |
| CJK-BYTE-UPLOAD-20260705-009 | Simplified Chinese | yhwu-is/Linear-Algebra-Left-Undone | manifest_only | explicit_source_path_byte_count_present | 158557 |
| CJK-BYTE-UPLOAD-20260705-010 | Simplified Chinese | DolveKD/Advanced-Algebra-Notes | manifest_only | explicit_source_path_byte_count_present | 61552 |
| CJK-BYTE-UPLOAD-20260705-011 | Simplified Chinese | arshtyi/Advanced-Algebra | manifest_only | explicit_source_path_byte_count_present | 37692 |
| CJK-BYTE-UPLOAD-20260705-012 | Korean addendum/source routing | gshstexsociety/examples | manifest_only | explicit_source_path_byte_count_present | 65665 |
| CJK-BYTE-UPLOAD-20260705-013 | Korean addendum/source routing | alstn2468/category-theory-for-programmers | manifest_only | explicit_source_path_byte_count_present | 15371 |
| CJK-BYTE-UPLOAD-20260705-014 | Korean addendum/source routing | Korean modern/abstract algebra source-level TeX recheck | gap_row_only | exact_gap_row_no_source_payload_byte_count |  |
| CJK-BYTE-UPLOAD-20260705-015 | Japanese | Japanese exact abstract/modern algebra source-level TeX recheck | gap_row_only | exact_gap_row_no_source_payload_byte_count |  |
| CJK-BYTE-UPLOAD-20260705-016 | Japanese | imamuray/algebraic-systems | manifest_only | source_metadata_without_exact_payload_byte_count |  |
| CJK-BYTE-UPLOAD-20260705-017 | Japanese | t-higashida/commutative_ring_and_field | manifest_only | source_metadata_without_exact_payload_byte_count |  |
| CJK-BYTE-UPLOAD-20260705-018 | Japanese | Seasawher/matsumura | manifest_only | source_metadata_without_exact_payload_byte_count |  |
| CJK-BYTE-UPLOAD-20260705-019 | Korean addendum/source routing | calofmijuck/algebra | manifest_only | source_metadata_without_exact_payload_byte_count |  |
| CJK-BYTE-UPLOAD-20260705-020 | Japanese | Japanese algebra source coverage residual | gap_row_only | exact_gap_row_no_source_payload_byte_count |  |
| CJK-BYTE-UPLOAD-20260705-021 | Korean addendum/source routing | Korean algebra source coverage residual | gap_row_only | exact_gap_row_no_source_payload_byte_count |  |

## Boundaries

- This sidecar normalizes fields only; it does not make an AGENTS-complete witness, native-review, public-review, canonical-approval, license-clearance, gate-promotion, or completion claim.
- Rows with `source_metadata_without_exact_payload_byte_count` or `exact_gap_row_no_source_payload_byte_count` remain explicit gaps for owner/B3 handling.
- Korean rows remain addendum/source-routing rows, not Korean native-edition authority.
- No raw source bodies, source archives, temporary probes, translation text, or glossary promotion are included.

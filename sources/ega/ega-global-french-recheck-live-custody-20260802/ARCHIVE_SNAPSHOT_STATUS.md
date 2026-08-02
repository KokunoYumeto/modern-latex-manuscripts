# EGA global French-recheck live production custody snapshot

Date: 2026-08-02

Status: exact byte custody of a live sequential capture; not a production completion or validation claim.

## Capture boundary

- Capture window: `2026-08-02T15:16:57+02:00` through `2026-08-02T15:22:29+02:00`.
- Component capture boundaries: `{"ega_french_canon_original": {"bytes": 1887431437, "captured_through": "2026-08-02T15:22:29+02:00", "files": 1318}, "ega_successor_original": {"bytes": 7565951, "captured_through": "2026-08-02T15:17:09+02:00", "files": 154}, "fac_original": {"bytes": 356931436, "captured_through": "2026-08-02T15:17:09+02:00", "files": 851}}`.
- Capture mode: `sequential_copy_composite_byte_snapshot`. Because files were copied sequentially, the tree is a composite byte snapshot, not an asserted filesystem-atomic or semantic checkpoint.
- Exact captured files: 1,472; exact captured bytes: 1,894,997,388; original manifest SHA-256: `F54CA1EA87E2678113DFFF907C580F6A42A27E3AC7993E2B6A4802FFFAF63BEA`.
- Producer trees were not modified. Every captured byte is retained in the private exact-custody ZIP.

## Generation/status caveat

```json
{
  "claim": "captured bytes are not certified as coherent R9, complete, rebuilt, reference-replayed, or publication-ready",
  "classification": "LIVE_COMPOSITE_BYTE_CUSTODY_WITH_R9_CONTROL_CONTENT_LAG",
  "french_canon_custody": {
    "all_controls_public_projected_and_dual_doi_bound": true,
    "all_qa_files_private_custody_only_pending_rights_clearance": true,
    "all_source_files_public_projected_with_license_not_specified_caveat": true,
    "bytes": 1887431437,
    "controls_bytes": 405885,
    "controls_files": 96,
    "files": 1318,
    "normalization_revision_policy": {
      "bytes": 6628,
      "relative_path": "french_canon/controls/ENGLISH_NORMALIZATION_DECISION_AND_REVISION_POLICY_20260802.md",
      "sha256": "AE09C581B4EC6B0DFF647EBD367A2FA455C0895CCE43CC54D8A4315185677EE5"
    },
    "strict_r2_r9_provenance_bytes": 89822,
    "strict_r2_r9_provenance_files": 23,
    "strict_r2_r9_provenance_paths": [
      "french_canon/controls/EGA1_PRINTED69_SECTION742_745_DIRECT_AUTHORITY_IMAGES.json",
      "french_canon/controls/EGA1_PRINTED69_70_SECTION751_753_DIRECT_AUTHORITY_IMAGES.json",
      "french_canon/controls/EGA1_PRINTED70_71_PROP754_DIRECT_AUTHORITY_IMAGES.json",
      "french_canon/controls/EGA1_PRINTED71_72_PROP755_763_DIRECT_AUTHORITY_IMAGES.json",
      "french_canon/controls/EGA1_PRINTED73_PROP764_7610_DIRECT_AUTHORITY_IMAGES.json",
      "french_canon/controls/EGA1_PRINTED74_PROP7611_7614_DIRECT_AUTHORITY_IMAGES.json",
      "french_canon/controls/EGA1_PRINTED74_75_SECTION7615_7618_DIRECT_AUTHORITY_IMAGES.json",
      "french_canon/controls/ENGLISH_CORRECTION_RECHECK_APPEND_20260802.jsonl",
      "french_canon/controls/ENGLISH_CORRECTION_RECHECK_APPEND_P70_20260802.jsonl",
      "french_canon/controls/ENGLISH_CORRECTION_RECHECK_APPEND_P71_20260802.jsonl",
      "french_canon/controls/ENGLISH_CORRECTION_RECHECK_APPEND_P71_P72_20260802.jsonl",
      "french_canon/controls/ENGLISH_CORRECTION_RECHECK_APPEND_P73_20260802.jsonl",
      "french_canon/controls/ENGLISH_CORRECTION_RECHECK_APPEND_P74_20260802.jsonl",
      "french_canon/controls/ENGLISH_CORRECTION_RECHECK_APPEND_P75_20260802.jsonl",
      "french_canon/controls/ENGLISH_CORRECTION_REPAIR_APPLICATION_20260802.jsonl",
      "french_canon/controls/ENGLISH_CORRECTION_REPAIR_APPLICATION_P70_20260802.jsonl",
      "french_canon/controls/ENGLISH_CORRECTION_REPAIR_APPLICATION_P71_20260802.jsonl",
      "french_canon/controls/ENGLISH_CORRECTION_REPAIR_APPLICATION_P71_P72_20260802.jsonl",
      "french_canon/controls/ENGLISH_CORRECTION_REPAIR_APPLICATION_P73_20260802.jsonl",
      "french_canon/controls/ENGLISH_CORRECTION_REPAIR_APPLICATION_P74_20260802.jsonl",
      "french_canon/controls/ENGLISH_CORRECTION_REPAIR_APPLICATION_P75_20260802.jsonl",
      "french_canon/controls/ENGLISH_REPAIR_VALIDATION_SUPERSESSION_P70_20260802.jsonl",
      "french_canon/controls/ENGLISH_REPAIR_VALIDATION_SUPERSESSION_P71_20260802.jsonl"
    ]
  },
  "r9_control_content_match": false,
  "r9_control_content_mismatch_count": 1,
  "r9_control_content_mismatches": [
    {
      "captured_bytes": 75620,
      "captured_sha256": "29008BF15E3674F9B84BACDC8168B38E3C2B4B25497B153B2F96C744629749D8",
      "r9_bytes": 75432,
      "r9_sha256": "81196521B4A963CFD614452C63C1669482B4C58A6A2E250DD593B1B11159F036",
      "reason": "captured_content_differs_from_r9_control",
      "relative_path": "successor/source/ega0/ega0-7.tex"
    }
  ],
  "r9_diff_control_errors": [],
  "r9_diff_control_status": "PASS_SOURCE_SUCCESSOR_DIFF_CURRENT",
  "r9_manifest": {
    "bytes": 24485,
    "declared_bytes": 7280020,
    "declared_files": 127,
    "declared_tree_sha256": "B20246760E9A19F7050C457EC91697105B6CB255FBBDDEFF15DD0718716698AE",
    "relative_path": "successor/controls/SOURCE_INPUT_SHA256_R9.json",
    "sha256": "203A7E34F3BC5683E4612DA4300358B4A5DD295EA2781454811EB2C15A38B05D"
  }
}
```

The identities above are preserved as disagreeing evidence. This archive does not repair, reinterpret, or certify production decisions.

## Public projection

- Public-projected producer files: 257.
- Text files mechanically redacted: 93; total redaction actions: 1,433.
- Rights-withheld files: 1,215; rights-withheld bytes: 1,886,478,790.
- Every withheld file remains listed by exact path, bytes, and SHA-256 in `ORIGINAL_PUBLIC_MANIFEST.csv` with disposition `RIGHTS_UNCLEARED_PRIVATE_CUSTODY_ONLY`.
- Public redaction changes only machine-local absolute roots, user-home prefixes, or detected secret values. All other bytes are preserved.
- Project-authored provenance/control surfaces in the dual-DOI payload are marked CC0-1.0. Corpus source and build artifacts remain `License Not Specified`; packaging does not manufacture a rights grant.

## Dual-DOI provenance route

The exact provenance ZIP under `dual_doi/` is intended for both methodology DOI `10.5281/zenodo.21124403` and replication DOI `10.5281/zenodo.20461174`. Packaging does not itself assert that either DOI has been updated.

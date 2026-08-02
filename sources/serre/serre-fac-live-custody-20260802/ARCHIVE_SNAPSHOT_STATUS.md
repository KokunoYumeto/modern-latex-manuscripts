# Serre FAC live production custody snapshot

Date: 2026-08-02

Status: exact byte custody of a live sequential capture; not a production completion or validation claim.

## Capture boundary

- Capture window: `2026-08-02T15:16:57+02:00` through `2026-08-02T15:22:29+02:00`.
- Component capture boundaries: `{"ega_french_canon_original": {"bytes": 1887431437, "captured_through": "2026-08-02T15:22:29+02:00", "files": 1318}, "ega_successor_original": {"bytes": 7565951, "captured_through": "2026-08-02T15:17:09+02:00", "files": 154}, "fac_original": {"bytes": 356931436, "captured_through": "2026-08-02T15:17:09+02:00", "files": 851}}`.
- Capture mode: `sequential_copy_composite_byte_snapshot`. Because files were copied sequentially, the tree is a composite byte snapshot, not an asserted filesystem-atomic or semantic checkpoint.
- Exact captured files: 851; exact captured bytes: 356,931,436; original manifest SHA-256: `1F0DEA1F0129A19EED4AE4FD04379A150EC865DD3AC894723258F41D8EF6BA2C`.
- Producer trees were not modified. Every captured byte is retained in the private exact-custody ZIP.

## Generation/status caveat

```json
{
  "captured_highest_component": "U0041",
  "checkpoint_identities_bound_by_validator": {
    "bytes": 8868,
    "sha256": "709E959BA8F275D7204F87727E28532C5C4B5D997E5C3C173075D2EBC6D0CA51"
  },
  "checkpoint_identities_current": {
    "bytes": 9713,
    "sha256": "F8E4FB717D586819D694E665DBBC25DE85A96568B530E5BE259D9732D2E3D324"
  },
  "claim": "no completion, publication readiness, semantic coherence, or QA certification inferred",
  "classification": "LIVE_COMPOSITE_BYTE_CUSTODY_NOT_SEMANTIC_CHECKPOINT",
  "status_component_lag": false,
  "status_declared_highest_unit": "U0041",
  "validator_bound_highest_unit": "U0036",
  "validator_manifest_matches_captured_identity": false,
  "validator_overall_work_status": "ACTIVE_NOT_COMPLETE_NOT_PUBLICATION_READY",
  "validator_status": "PASS_BOUNDED_INTERNAL_CHECKPOINT",
  "validator_status_lag": true
}
```

The identities above are preserved as disagreeing evidence. This archive does not repair, reinterpret, or certify production decisions.

## Public projection

- Public-projected producer files: 795.
- Text files mechanically redacted: 342; total redaction actions: 53,386.
- Rights-withheld files: 56; rights-withheld bytes: 205,112,648.
- Every withheld file remains listed by exact path, bytes, and SHA-256 in `ORIGINAL_PUBLIC_MANIFEST.csv` with disposition `RIGHTS_UNCLEARED_PRIVATE_CUSTODY_ONLY`.
- Public redaction changes only machine-local absolute roots, user-home prefixes, or detected secret values. All other bytes are preserved.
- Project-authored provenance/control surfaces in the dual-DOI payload are marked CC0-1.0. Corpus source and build artifacts remain `License Not Specified`; packaging does not manufacture a rights grant.

## Dual-DOI provenance route

The exact provenance ZIP under `dual_doi/` is intended for both methodology DOI `10.5281/zenodo.21124403` and replication DOI `10.5281/zenodo.20461174`. Packaging does not itself assert that either DOI has been updated.

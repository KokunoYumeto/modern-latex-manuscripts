# Nöther Spanish/French production-ledger ↔ Romance WordWeb crosswalk v10

This successor binds the current 101-row Spanish and 93-row French production terminology ledgers to the immutable v9 WordWeb without inventing attestations. The first 60 Spanish rows are the pinned T01–T60 production sequence. Other rows map only when an existing German core source identity or target surface matches uniquely after deterministic normalization. Ambiguous, conflicting, and absent exact identities remain held or unmapped.

- Total production rows preserved: `194` (`101` Spanish + `93` French).
- Spanish mapping states: `{"mapped": 61, "unmapped_explicit": 40}`.
- French mapping states: `{"mapped": 9, "unmapped_explicit": 84}`.
- Every production row and evidence field is retained in the CSV/JSON; each source row has a canonical SHA-256.
- The crosswalk creates no attestation and uses no semantic nearest-neighbor inference.
- `attestation_effect`, `promotion_effect`, and `human_or_MII_effect` are uniformly `none`.
- Unmapped rows are an integration cursor, not negative evidence about the language or term.

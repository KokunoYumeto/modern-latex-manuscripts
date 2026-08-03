# English/Germanic decision-log privacy remediation v2

## Scope

Methodology record `21779952` and replication record `21779957` corrected the
earlier verbatim-log path disclosures, but an independent UUID-shape scan found
nine internal task identifiers still present across six historical finding
fields.  The v1 matcher required a leading word boundary; the missed UUIDs were
concatenated directly after prose such as `thread` or `task`.  Both v1 records,
and their earlier raw-log predecessors `21778949` and `21778962`, remain
immutable adverse history.

This successor preserves all 480 decision records in
their exact order and omits none.  It replaces only private path roots, private
state-directory segments, the private project email, and every complete
internal task-ID shape even when adjacent to prose.
Task IDs receive stable SHA-256-derived pseudonyms so repeated references remain
linkable without exposing the source identifiers.  The event ledger binds every
source token by length and SHA-256 without repeating the private token.

## Exact projection

- Private source custody: 480 records / 3209113 bytes /
  SHA-256 `374271E653FEA9472ACA461FA6E759F0F9E785D232715E1A6811ABF12D0D327F`; not redistributed on the current heads.
- Public projection: `00_ENGLISH_GERMANIC_DECISION_LOG_1_PUBLIC_PRIVACY_CLEAN_v2.jsonl` — 480 records /
  3151969 bytes / SHA-256 `4D789AD4A9E588CFCDDA4CFD39EB7810BED7EC39E37BD03D22D8F49F7AF5B641`.
- Transformation ledger: `00_ENGLISH_GERMANIC_DECISION_LOG_2_PRIVACY_TRANSFORMATIONS_v2_20260803.csv` — 2425 events /
  441869 bytes / SHA-256 `B4B34D51216E64EEF1ED9CEB2CAFCEA511DB78BC6503CB92A57DE5B54B3AF582`.
- Validation: `ENGLISH_GERMANIC_DECISION_LOG_PRIVACY_VALIDATION_v2_20260803.json` — PASS; records omitted 0; residual private
  tokens 0; reader/production content changes 0.
- Methodology successor record: `21780213`
  under existing concept `10.5281/zenodo.21124403`.
- Replication successor record: `21780218`
  under existing concept `10.5281/zenodo.20461174`.

The controlling 2,296-byte dual-DOI requirement remains byte-exact in the
provenance ZIP as an explicitly mandated three-identifier exception.  The v1
false residual-closure claim is preserved by predecessor identity and by the
new append-only remediation decision.  No SGA reader, TeX, translation,
mathematical statement, source decision, error, reversal, or continuation
record is changed or curated away.

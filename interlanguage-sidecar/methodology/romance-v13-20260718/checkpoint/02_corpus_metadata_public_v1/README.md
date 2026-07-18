# Romance corpus metadata checkpoint v1

This is a publication-safe, metadata-only projection of the internal Romance corpus v5 and branch-routing ledger v4. It contains **153 corpus records** and **61 explicit branch routes** (11 active, 50 zero-body). It does not redistribute source PDFs, extracted text, quotations, or quotation-bearing workbooks.

## What is included

- `ROMANCE_CORPUS_METADATA_v1.csv`: deduplicated source identities, language/variety/domain/register metadata, source and search-text SHA-256 values, license/status fields, public HTTP locators where available, and explicit eligibility/status flags.
- `ROMANCE_BRANCH_ROUTES_v1.csv`: 61 named standards/varieties, including explicit zero-body routes rather than dominant-language substitution.
- `ROMANCE_LANGUAGE_COVERAGE_v1.csv` and `ROMANCE_VARIETY_COVERAGE_v1.csv`: per-language and per-variety coverage.
- `ROMANCE_REJECTED_EVIDENCE_METADATA_v1.csv`: rejected searches, adverse evidence, and catalog-only records that do not count as corpus bodies.
- `SOURCE_BINDING_v1.json`: hashes of the internal inputs and exact projection boundary.

The eight initial standards—Spanish, French, Portuguese, Catalan, Italian, Galician, Romanian, and Romansh—each have at least one active reviewed mathematics body. Coverage is not equal: Romansh has seven active general-school bodies but **zero specialist-algebra bodies**; Surmiran and Sutsilvan remain explicit zero-body routes. The four 2025 branch-native Romansh documents total 60 pages but form one translation family and must not be treated as four independent exam designs.

## Rights and claim boundary

The source hash and license/status metadata are published for provenance. A source URL is not a reuse grant. Rights-unresolved bodies remain excluded from this payload. No corpus row is term-promotion eligible. This checkpoint contains zero human observations, zero native validation, zero empirical marginal-intelligibility results, and no lane-completion claim. Corpus occurrence is evidence requiring sense/register review, never canon.

Internal source checkpoint hashes are recorded in `SOURCE_BINDING_v1.json`. Run `python build_public_corpus_metadata_v1.py` inside the live lane, then `python validate_public_corpus_metadata_v1.py`, to reproduce and validate the projection.

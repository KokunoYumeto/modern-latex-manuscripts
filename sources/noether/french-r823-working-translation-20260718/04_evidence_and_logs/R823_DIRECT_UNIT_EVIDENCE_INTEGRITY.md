# R823 French direct-unit evidence integrity

Date: 17 July 2026

## Acceptance defect closed at the routing layer

The former evidence map sent P01--P43 to a nonexistent paper router and the 32 book units to a generic chapter router. It is preserved, but is not acceptance evidence, at `working/backups/R823_REVIEW_EVIDENCE_MAP_FR_router_pre_direct_20260717.csv` (SHA-256 `7E211A89019794260D80C660EFD359BFDE2F73E4EA4C1EB3F27EA0013B07C3FE`).

The production `evidence/R823_REVIEW_EVIDENCE_MAP_FR.csv` now contains 81 unique rows and the five fields `unit_id,evidence_path,evidence_record,review_scope,notes`. Every row points to `R823_UNIT_RECONCILIATION_EVIDENCE_FR.csv`, and every `evidence_record` is exactly the row's `unit_id`. There are no router paths and no blank scopes. Map SHA-256 at this architecture cut: `B76F4ED1A8A12E3063762349427F13C3549613F2A503A7715B358506B74C3223`.

## Hash-safe construction and promotion

- `tools/seed_unit_reconciliation_evidence.py` (SHA-256 `EA92C092C5FCCB07FDBA6E2D943F14144AAFF11F0A16BAA2857011A34D85A13D`) carries review content forward only when the source-unit, target-unit, and whole expanded-target hashes all remain exact; otherwise it resets the unit to pending.
- `tools/build_unit_reconciliation_evidence.py` (SHA-256 `80DA3CAAC432E0E69ADD1CC593635DAC8E901B62EACA0C45ABA5ABFBD9E44B82`) requires exactly 81 genuinely completed draft reviews, injects only the frozen v3 manifest hashes/line spans, rejects thin or duplicated narratives, resolves every cited artifact, and calculates its live SHA-256.
- `tools/promote_exact_parity_ledger.py` (SHA-256 `75432CED7061497C0473951F1AE97CDF8F410B9EC810B1F1F7707F13199E8EA6`) requires the evidence corpus to contain exactly the same 81 units as the seed, exact source/target/whole-document hashes, numeric source and target locators, substantive method/structure/formula/note/finding/provenance fields, unique narratives, and live matching artifact hashes before it writes `source-reconciled` parity.

## Deliberate refusal self-test

A disposable live snapshot expanded 130 TeX files, sliced all 81 units, and produced whole-target SHA-256 `562DC4828D33682E3615F5138BE9049069DEE609E7D0EF2FBEFDA7CBD6503D72`. The target manifest, parity seed, and pending review seed have SHA-256 values `34B8116F4C0FE7463ABD14AA6413170E218F646FFAF90D8D746857258F3AE606`, `D92FE84C5B7EDF272327EEDE5E8316C633E8DA4D9FDD35E0CC02BF97604C56CB`, and `EC0B941484F3AB587FFFBA3CD69193C157E4CF9988C70D14B436BB2185E536FB`. All 81 parity/review rows remained pending.

The promoter then refused before writing output:

```text
ValueError: P01: missing or empty review evidence ...\evidence\R823_UNIT_RECONCILIATION_EVIDENCE_FR.csv
```

`working/tmp/SHOULD_NOT_EXIST_PROMOTED.csv` was confirmed absent. These snapshot hashes are architecture-test evidence only; they must not be copied into the final unit corpus. Final evidence is generated only after all 130 dependencies are frozen and a new v3 manifest/seed is produced.

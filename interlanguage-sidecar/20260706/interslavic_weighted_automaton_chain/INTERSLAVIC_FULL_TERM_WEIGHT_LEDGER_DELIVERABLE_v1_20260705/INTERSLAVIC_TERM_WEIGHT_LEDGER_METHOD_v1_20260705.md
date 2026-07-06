# Interslavic full term weight ledger — v1

This deliverable is the requested full Interslavic term ledger with weights. It covers every row in the current retrofit ledger and adds the proof-register ledger as a separate table. It is a ledger, not a certification artifact: no form is promoted and no translated prose is changed.

## Row scope
- Technical/term rows: **1254**
- Proof/register rows: **532**

## Weight columns
- `witness_E/W/S/I/X`: current witness-vector axes. E/W/S are family branches; I is Interslavic/community/authority evidence; X is international/specialist evidence.
- `family_effective_branches_D1`: term-level Hill/Shannon effective branch count over E/W/S. 1 ≈ one-branch support; 3 ≈ balanced family support.
- `family_balance_weight`: `D1/3`, normalized to [0,1].
- `axis_support_weight`: capped weighted mass over E/W/S/I/X; used as an evidence-use diagnostic, not truth.
- `evidence_sufficiency_weight`: F10 flag prior: F10-0=0.85, F10-1=0.35, F10-2=0.45, F10-3=0.20, F10-4=0.50.
- `current_support_weight`: composite evidence/use weight, bounded [0,1].
- `review_priority_weight`: high means row needs review, backfill, or caution before external use.
- `candidate_*`: dry-run candidate vector/weight after v11 metadata candidates, not certified.

## Recommended action semantics
- `candidate_metadata_writeback_after_exact_row_check`: likely F10 metadata writeback candidate; still needs exact row context.
- `false_sense_filter_then_candidate_metadata_writeback`: usable only after false-sense/source filter.
- `competitor_channel_review_packet`: evidence exists but competitor/adverse channel prevents simple support.
- `authority_review_before_any_writeback`: dominance-sensitive row.
- `specialist_or_authority_review_needed`: constructed/specialist row.
- `backfill_non_east_witness_or_mark_gap`: missing non-East support.

## Corpus-level branch mass
- branch_mass_current: `{'E': 2396, 'W': 167, 'S': 169, 'I': 0, 'X': 192, 'D1_effective_branches_family_only': 1.581, 'distribution_family_only': {'E': 0.877, 'W': 0.0611, 'S': 0.0619}}`
- branch_mass_candidate_W1W2: `{'E': 2528, 'W': 311, 'S': 345, 'I': 0, 'X': 192, 'D1_effective_branches_family_only': 1.918, 'distribution_family_only': {'E': 0.794, 'W': 0.0977, 'S': 0.1084}}`

## Boundary
Weights are evidence/use weights. They do not certify target-language usage, do not promote bridge forms, and do not authorize text patches.
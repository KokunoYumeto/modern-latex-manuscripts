# Romance language manager

This is the single manager lane for Spanish, French, Portuguese, Italian,
Catalan, Galician, Romanian, Romansh, and additional Romance varieties when
evidence becomes available. It covers every mathematical work in the shared
archive. It is not divided into one task per work or language.

## Authority and evidence rules

1. Source scans and current source editions control mathematical content.
2. Existing translations are translation memory and comparison controls; they
   do not become source authority merely because they compile.
3. Native target-language mathematical bodies may witness target usage only
   after their exact row and sense have been checked.
4. Generated drafts cannot witness living target usage.
5. Support, candidate, competitor, adverse, veto, and absence evidence remain
   separate typed channels. No scalar score makes an automatic decision.
6. Branch breadth is interpreted only against the declared operational
   family/cohort tree. W0 is a projection, not observed access.
7. No artifact is described as community-certified or externally reviewed
   without actual external review evidence. Unified v6.2 readiness is rejected.

## Manager/cohort linkage

The manager identifier is `romance_manager`. Its canonical nine-reader-cohort
topology is `ROMANCE_FAMILY_COHORT_TREE_v2.json`, with the exact IDs
`C-ES-STD`, `C-FR-STD`, `C-PT-STD`, `C-GL-STD`, `C-CA-STD`,
`C-IT-STD`, `C-RO-STD`, `C-RM-RG`, and `C-RM-ID`. Rumantsch Grischun
and readers primarily literate in a Romansh regional idiom remain separate
evaluation cohorts; the five idioms remain separate source routes.

This topology has zero human observations. Its rows are protocol declarations,
not measured intelligibility. `ROMANCE_FAMILY_COHORT_TREE_v1.json` is retained
as superseded historical control evidence and is not the operative topology.

## French triple interlock

French has three distinct roles which must never be collapsed:

- SGA/EGA French: source-language authority or source control.
- Noether French: target-language translation memory and repair target.
- Independent native French mathematics: target-register witness after
  row-level and sense-level checking.

## Operative files

- `WORK_CORPUS_LOCATION_REGISTER_v1.csv`: exact disk locations and roles.
- `DISK_WORK_ROOT_INVENTORY_v1.csv`: 105 current top-level work/package roots
  across the public source shelf, public readers, Papors archive, and other-PC
  language-body shelf.
- `ROMANCE_FAMILY_COHORT_TREE_v2.json`: canonical nine-reader-cohort
  operational topology linked to manager `romance_manager`.
- `ROMANCE_FAMILY_COHORT_TREE_v1.json`: preserved superseded eight-row
  topology; never use it for current MII/access row counts.
- `ROMANCE_MANAGER_EVIDENCE_GRAPH_v1.json`: typed evidence graph seed and the
  first SGA6 Spanish routing decision.
- `validate_manager_control_v2.py`: reproducible semantic, linkage, path, and
  count validator plus SHA-manifest generator.
- `ROMANCE_MANAGER_CONTROL_VALIDATION_20260717.json` and
  `ROMANCE_MANAGER_CONTROL_SHA256SUMS.csv`: parse, path, count, and integrity
  checks for the manager-control layer. The SHA manifest excludes its own hash.
  The validation timestamp is the declared 2026-07-17 control-snapshot time,
  not the runtime wall clock, so repeated validation is byte-reproducible.
- `../04_sga6_spanish_20260717/SGA6_X_ES_T001/`: first bounded SGA6 Spanish
  source-checked working tranche.

The recovered Noether French and Spanish books have nominal Papers 1--43 but
remain incomplete drafts against R823. Their terminal scope and audit status
are recorded in `NOETHER_FR_ES_RECOVERY_AUDIT_20260717.md`; that work is not
duplicated here.

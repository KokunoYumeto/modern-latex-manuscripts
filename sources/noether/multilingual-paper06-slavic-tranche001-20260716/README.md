# Noether Paper 06 multilingual handoff

Start here. This is a portable continuation package for Paper 06, *Körper und Systeme rationaler Funktionen*.

## What changed

Fable Tranche 001 supplied a reviewed orthographic decision set for the Interslavic branch. The approved changes were applied TeX-aware to the sixteen Latin units and mirrored into their existing Cyrillic siblings without overwriting prior manual Cyrillic corrections. The exact 17 replacements, paths, hashes, and unified diff are in `audit/`.

Russian and Ukrainian were deliberately not edited. They are included as synchronized working controls so that a later source correction can be propagated across all four Slavic branches together.

## What is ready

- 16 Interslavic Latin TeX files and 16 compiled PDFs.
- 16 Interslavic Cyrillic TeX files and 16 compiled PDFs.
- 16 Russian TeX controls and 16 freshly compiled PDFs.
- 16 Ukrainian TeX controls and 16 freshly compiled PDFs.
- 16 translation-unit JSON records.
- German generation slice, English control slice, and source-scan PDF.
- Current R821-integrated German cumulative TeX and its public status note.
- Build ledgers, change ledger, hashes, diff, method specification, and render checks.

All 64 standalone TeX files compile. Across the four languages there are zero TeX errors and zero overfull boxes. Underfull warnings remain layout diagnostics, chiefly in Russian and Cyrillic Interslavic, and do not establish linguistic correctness.

## Scholarly status

This is a working multilingual translation corpus with a checked orthographic tranche. It is not a critical edition, and the compiled result is not proof of source or translation correctness. The German source remains authoritative. Before claiming Paper 06 source synchronization, compare the complete June generation slice against the Paper 06 span in the current R821-integrated cumulative source and propagate every substantive delta across all four languages.

## Folder guide

- `tex/`: editable language files.
- `pdf/`: compiled standalone readers.
- `sources/translation_generation_source/`: exact source/control material used by the earlier translation workflow.
- `sources/current_german_authority/`: newer German cumulative authority for reconciliation.
- `translation_units/`: unit coverage, terminology choices, and provenance.
- `audit/`: machine- and human-checkable evidence for this tranche.
- `methodology/`: governing production and Fable decision specifications.
- `scripts/`: deterministic application script.
- `render_checks/`: contact sheets inspected after compilation.

## Next action

Run a source-delta reconciliation for Paper 06, then continue the multilingual corpus from its actual next uncovered unit. Do not regenerate completed units from scratch and do not promote older controls over the current German authority.

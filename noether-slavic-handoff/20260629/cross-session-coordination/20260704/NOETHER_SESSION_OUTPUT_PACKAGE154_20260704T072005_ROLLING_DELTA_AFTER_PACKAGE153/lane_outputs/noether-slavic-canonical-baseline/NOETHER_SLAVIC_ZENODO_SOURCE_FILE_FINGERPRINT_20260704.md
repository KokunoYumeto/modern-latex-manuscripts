# Noether Slavic Zenodo Source File Fingerprint

Generated: 2026-07-04T07:11:xx+02:00

Live source record: `https://zenodo.org/api/records/20836874`

DOI: `10.5281/zenodo.20836874`

Purpose: make the source-baseline rebuild trigger executable by storing key, size, and checksum fingerprints for the Zenodo files whose names indicate German source, source witness, source audit, source repair, R124/P40 repair, or Slavic transfer/current-source relevance.

## Fingerprint Scope

Artifact:

- `NOETHER_SLAVIC_ZENODO_SOURCE_FILE_FINGERPRINT_20260704.csv`

Rows: `21`

CSV SHA256 at creation: `5E66DCE7E0088337365D0847A5A1F52AAF6CD4886FB3B90FFCD560B62E38C2D9`

Matched key pattern:

`(?i)(German|Source|source|Slavic|witness|repair|R124|P40|CurrentSources)`

This intentionally watches the source-bearing slice of the record rather than every English/non-Slavic reader PDF.

## Watcher Integration

`NOETHER_SLAVIC_BASELINE_WATCHER_20260704.ps1` now embeds the 21 watched key/size/checksum triples and emits an aggregate trigger check:

- `zenodo_source_file_fingerprints_match`

Latest test run after watcher hardening:

- Generated: `2026-07-04T07:12:42.9522713+02:00`
- Checks: `27`
- Source fingerprint pass: `true`
- Source fingerprint mismatches: `0`
- Rebuild trigger now: `false`

## Trigger Rule

A missing watched source file, changed watched source file size, or changed watched source file checksum is a source-baseline trigger. It requires human inspection before publication refresh and may require source inventory re-anchoring, affected TeX/PDF rebuild, manifest updates, and package hash regeneration.

This artifact does not alter Slavic canonical output and does not claim external/native review completion.

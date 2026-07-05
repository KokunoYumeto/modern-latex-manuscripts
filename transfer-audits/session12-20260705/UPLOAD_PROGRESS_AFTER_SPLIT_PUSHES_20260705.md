# Upload Progress After Split Pushes - 2026-07-05

Side branch: `codex/noether-pc-20260629`

Latest observed local/remote head before this audit note was staged: `739e63a1790fc119f9aa8c56b0b21677d20d2265`

This note supplements the generated transfer audit files in this directory. It records the split-upload state after large body packages were pushed in smaller commits so the branch could keep moving without touching `main`.

## Pushed Body Packages

- R7 Malay/SEA/Pacific source bodies: pushed at `201ebbdbf55b854f72eb4fbf1057fcfbe070db3a` after a package-local token-shaped-string redaction, SHA refresh, and tar listability check.
- R6 Indigenous/Creole/Sign source bodies: pushed in split commits from `55bac00994c1f7bbda458cf4e95d209113839943` through `a0cb73ba8b0ca715c30af0d84e6802ad872b223d`; the original all-in-one commit was too large for a reliable push and is preserved only as a local backup ref.
- R3 Arabic/Persianate full source-body package: pushed across split commits, with current tree containing metadata/OCR/minor bodies, Tajik Cyrillic bodies, Arabic bodies `0001-0099`, Persian source ZIP, remaining Persian source bodies, and the populated R3 CSV manifest from `739e63a1790fc119f9aa8c56b0b21677d20d2265`. The final Arabic chunk landed at `2c6bafc5776108557dbb64e97e13b4a67ee46385`.
- Earlier body packages already on branch include Fable/interlanguage heartbeat ledgers, OLP support bodies, package 636 repair, Arabic RTL, CJK draft/native, and Persianate/Tajik source bodies.

## Concurrent Branch Writes

While R3 was being uploaded, another uploader advanced the same side branch with Slavic source-body chunks and checksum repairs. This session did not overwrite those commits; it repeatedly fetched/reset to the remote head and replayed only still-missing R3 chunks.

Observed concurrent commits included:

- `a4539575` Add Slavic source body chunk 1
- `716c525c` Add Slavic source archives chunk
- `0bfc3d15` Add Sorbian source body chunk
- `cfe5fb67` Add Interslavic Slavic source body chunk
- `28093601` Repair Slavic source body checksums
- `739e63a1` Populate R3 source body CSV manifest

## Safety Gates

- R7: credential scan clean after redaction; 53 SHA entries verified; two tar archives listed; no files >= 50 MB.
- R6: credential scan clean; 194 SHA entries verified; no archive bodies; no files >= 50 MB; split because total package size was about 364 MB.
- R3: credential scan clean; 190 SHA entries verified; six zip-like archives listed; one file was about 86.8 MB and no file was >= 100 MB; split because total package size was about 341 MB.

No native-review, accepted-terminology, license-clearance, gate-promotion, source-fidelity, publication-readiness, or translation-completion claim is made by this note.

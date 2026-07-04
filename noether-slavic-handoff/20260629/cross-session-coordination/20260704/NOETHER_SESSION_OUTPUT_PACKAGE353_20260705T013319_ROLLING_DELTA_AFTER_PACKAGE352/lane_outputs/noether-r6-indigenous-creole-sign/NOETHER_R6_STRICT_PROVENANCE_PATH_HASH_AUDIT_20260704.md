# Noether R6 Strict Provenance Path/Hash Audit

Generated: 2026-07-04

Lane: Session I / R6 Indigenous, Creole, and Sign Access

Status: source-canon provenance integrity audit only. It records no source-authority, reviewer approval, community consent, canonical approval, license-clearance record, media-reuse permission, OCR reuse, accepted term/sign, translation, pilot, lane-completion claim, Git staging, commit, or push.

## Inputs

| Artifact | Rows | Role |
|---|---:|---|
| `NOETHER_R6_SOURCE_CANON_STRICT_PROVENANCE_WITNESS_TABLE_20260704.csv` | 82 | Strict exact-URL provenance rows requiring URL, local path, SHA-256 hash, license/access signal, and language/topic tags. |
| `NOETHER_R6_STRICT_PROVENANCE_PATH_HASH_AUDIT_20260704.csv` | 82 | Per-row disk existence and SHA-256 replay audit generated from the strict witness table. |

## Result

| Check | Count |
|---|---:|
| Strict provenance rows audited | 82 |
| Local paths found on disk | 82 |
| Recorded SHA-256 values matching disk files | 82 |
| Missing local paths | 0 |
| SHA-256 mismatches | 0 |

## Boundary

This audit verifies only that the strict provenance table points to local files that currently exist and match their recorded hashes. It does not verify legal reuse, source authority, reviewer approval, community consent, media clearance, sign authority, term acceptance, translation readiness, or reader completion.

The safe Git checkout was most recently rechecked read-only on branch `codex/noether-pc-20260629` at `45393348e2debe0c2fa347b5e4fa5346f6b12825` (`Add Noether package 352`) with B3-owned untracked source-canon upload drift at `noether-source-corpus-provenance/20260704/NOETHER_ALL_LOCAL_LATEX_SOURCE_CANON_UPLOAD_20260704T212224Z/`. That untracked path is B3-owned packaging/source-canon work and was not staged, modified, cleaned, committed, or pushed by R6.

## Maintenance Rule

If any future R6 source row changes URL, local path, hash, or local capture, regenerate this audit before B3 packaging consumes the row. If a path is missing or a hash mismatches, move the affected row to a blocker/gap state until provenance is repaired.

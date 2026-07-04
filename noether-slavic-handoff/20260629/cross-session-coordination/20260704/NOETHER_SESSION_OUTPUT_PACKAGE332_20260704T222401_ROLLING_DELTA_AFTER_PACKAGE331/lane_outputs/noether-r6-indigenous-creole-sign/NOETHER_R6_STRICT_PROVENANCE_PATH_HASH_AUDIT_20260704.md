# Noether R6 Strict Provenance Path/Hash Audit

Generated: 2026-07-04

Lane: Session I / R6 Indigenous, Creole, and Sign Access

Status: source-canon provenance integrity audit only. No source-authority, reviewer approval, community consent, canonical approval, license clearance, media reuse, OCR reuse, accepted term/sign, translation, pilot, lane-completion claim, Git staging, commit, or push is claimed.

## Inputs

| Artifact | Rows | Role |
|---|---:|---|
| `NOETHER_R6_SOURCE_CANON_STRICT_PROVENANCE_WITNESS_TABLE_20260704.csv` | 83 | Strict provenance rows requiring URL, local path, SHA-256 hash, license/access signal, and language/topic tags. |
| `NOETHER_R6_STRICT_PROVENANCE_PATH_HASH_AUDIT_20260704.csv` | 83 | Per-row disk existence and SHA-256 replay audit generated from the strict witness table. |

## Result

| Check | Count |
|---|---:|
| Strict provenance rows audited | 83 |
| Local paths found on disk | 83 |
| Recorded SHA-256 values matching disk files | 83 |
| Missing local paths | 0 |
| SHA-256 mismatches | 0 |

## Boundary

This audit verifies only that the strict provenance table points to local files that currently exist and match their recorded hashes. It does not verify legal reuse, source authority, reviewer approval, community consent, media clearance, sign authority, term acceptance, translation readiness, or reader completion.

The safe Git checkout was observed on branch `codex/noether-pc-20260629` at `2f472b0b6f2e5c90c52d9f908646348cbb3e001b` (`Add Noether package 329`) with moving untracked package drift under the handoff tree. That untracked package path is B3-owned packaging work and was not staged, modified, cleaned, committed, or pushed by R6.

## Maintenance Rule

If any future R6 source row changes URL, local path, hash, or local capture, regenerate this audit before B3 packaging consumes the row. If a path is missing or a hash mismatches, move the affected row to a blocker/gap state until provenance is repaired.

# Noether Romance Source-Canon Spanish Repository License Gap Deepening

Status: draft / non-canonical / provenance-only / not native reviewed / not approved.

Created: 2026-07-04.

Scope: source-canon maintenance for the Spanish TeX repository witness `ES-B-002` and its explicit gap row `ES-GAP-004`. This note records source/provenance and rights-signal evidence only. It does not clear licenses, approve terms, translate corpus prose, populate reviewer packets, promote gates, or authorize a Git push from this lane.

## Summary

- Updated base witness table: `NOETHER_ROMANCE_SOURCE_CANON_WITNESS_TABLE_20260704.csv`.
- Created row-deepening CSV: `NOETHER_ROMANCE_SOURCE_CANON_SPANISH_REPO_LICENSE_GAP_DEEPENING_20260704.csv`.
- Created linked-page probe CSV: `NOETHER_ROMANCE_SOURCE_CANON_SPANISH_REPO_LINKED_WEB_PROBES_20260704.csv`.
- Created classified text-hit CSV: `NOETHER_ROMANCE_SOURCE_CANON_SPANISH_REPO_LICENSE_TEXT_HITS_CLASSIFIED_20260704.csv`.
- Probe material is under `outputs/source_canon_repo_text_probe/`.

## Evidence Checked

| Evidence class | Result |
|---|---|
| Local archive | ZIP SHA256 `cb36231487863bc0af7225259dfb27f0951b583776427743cfc70b380c790629`; 882,100 bytes; 102 entries. |
| License-file scan | No `LICENSE`, `COPYING`, `licencia`, or equivalent explicit license file found. Only `README.md` matched the broad file-name probe. |
| Text-like archive scan | 64 text-like files scanned, totaling 2,022,298 bytes. |
| Rights-specific hit classification | 0 repository license-grant hits; 1 third-party bibliography-style copyright notice in `amsalpha-cust.bst`; 3 false positives from `licenciatura` / `GNU/Linux`. |
| GitHub API | Repository endpoint HTTP 200; `repo.license` is null; license endpoint returned HTTP 404. |
| Linked teaching pages | 6 `cadadr.org` teaching pages from the README checked; all returned HTTP 200; rights/license scan found 0 hits. |

## Row Decisions

| Row | Decision |
|---|---|
| ES-B-002 | Keep as a Spanish TeX/source witness for algebra/register evidence, but not as rights-clear publication proof. |
| ES-GAP-004 | Retain as an explicit repository license/source-canon review gap before any reuse beyond provenance. |

## Probe Files

- `outputs/source_canon_repo_text_probe/ES-B-002_notas-san-salvador_probe_summary.json`
- `outputs/source_canon_repo_text_probe/ES-B-002_notas-san-salvador_github_api/repo.json`
- `outputs/source_canon_repo_text_probe/ES-B-002_notas-san-salvador_github_api/license_endpoint.json`
- `outputs/source_canon_repo_text_probe/ES-B-002_notas-san-salvador_web/*.html`
- `outputs/NOETHER_ROMANCE_SOURCE_CANON_SPANISH_REPO_LICENSE_TEXT_HITS_20260704.csv`
- `outputs/NOETHER_ROMANCE_SOURCE_CANON_SPANISH_REPO_LICENSE_TEXT_HITS_CLASSIFIED_20260704.csv`
- `outputs/NOETHER_ROMANCE_SOURCE_CANON_SPANISH_REPO_LINKED_WEB_PROBES_20260704.csv`

## Boundary

This pass deepens an explicit source-canon gap. It does not change the witness table's non-claim boundary: all Romance source-canon outputs remain draft, non-canonical, not native reviewed, not approved, not license-cleared, not gate-promoted, and not pushed by this language lane.

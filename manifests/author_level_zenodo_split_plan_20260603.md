# Author-Level Zenodo Split Plan - 2026-06-03

This plan records which mixed shelves should be split into dedicated author records. It is intentionally separate from the raw/provenance lane: large working archives stay on the main landing/provenance record, while author records should remain reader-facing and comparatively lean.

## Existing Author Records

| Author / corpus | Current record | Action |
|---|---:|---|
| Emmy Noether | `20412587` | Update existing record. Current GitHub state has German/English numbered papers complete through Paper 43 and Spanish/Japanese cumulative readers through Paper 15. |
| Heinrich Weber | `20412153` | Update existing record after outsourced Weber cumulative package is accepted. |
| Carl Friedrich Gauss | `20410934` | Update existing record after next Gauss cumulative audit. |
| Bernhard Riemann | `20429778` | Keep existing author record; not urgent. |
| Arthur Cayley | `20520749` | Dedicated author record created 2026-06-03. |
| Richard Dedekind | `20520669` | Dedicated author record created 2026-06-03. |
| P. G. Lejeune Dirichlet | `20520679` | Dedicated author record created 2026-06-03. |
| James Joseph Sylvester | `20520692` | Dedicated author record created 2026-06-03. |

## New Author Records To Create

| Author | Staged metadata | First reader-facing payload | Source/provenance policy |
|---|---|---|---|
| Ernst Steinitz | `zenodo-metadata/metadata_author_steinitz_current.json` | Existing Steinitz reader from the author cluster; newer local bilingual packets still need mirroring/checking. | Do not create until the current local Steinitz packet is mirrored and checked. |

## Newly Created Author Records

| Author | Concept DOI | First version DOI | Payload |
|---|---|---|---|
| Arthur Cayley | `10.5281/zenodo.20520749` | `10.5281/zenodo.20520750` | Thirteen current volume readers plus `Cayley_source_and_manifest_20260603.zip`. |
| Richard Dedekind | `10.5281/zenodo.20520669` | `10.5281/zenodo.20520670` | Nine reader PDFs plus `Dedekind_source_and_manifest_20260603.zip`. |
| P. G. Lejeune Dirichlet | `10.5281/zenodo.20520679` | `10.5281/zenodo.20520680` | Original-language cumulative reader, English cumulative reader, and `Dirichlet_source_and_manifest_20260603.zip`. |
| James Joseph Sylvester | `10.5281/zenodo.20520692` | `10.5281/zenodo.20520693` | Volume I through book page 218 reader and `Sylvester_source_and_manifest_20260603.zip`. |

## Mixed Shelf Policy

- `20414787` (`Cayley, Dedekind, and Dirichlet`) should remain an interim classical shelf and preservation umbrella until the Cayley, Dedekind, and Dirichlet author records exist.
- `20411006` (additional author cluster) should remain an umbrella for less mature author starts. Mature lanes should migrate out of it into author records.
- Do not repeatedly upload raw multi-gigabyte provenance bundles to each author record. Link them to the main landing/provenance record, concept DOI `10.5281/zenodo.20393488`.

## Immediate Authenticated Publish Order

1. Update SGA existing record `20410947` with SGA 6 page-702 completion and SGA 7-I page-96 continuation.
2. Update Noether existing record `20412587` with Spanish/Japanese cumulative readers through Paper 15.
3. Create Sylvester author record. Done: concept DOI `10.5281/zenodo.20520692`.
4. Create Dedekind and Dirichlet author records. Done: concept DOIs `10.5281/zenodo.20520669` and `10.5281/zenodo.20520679`.
5. Create Cayley author record. Done: concept DOI `10.5281/zenodo.20520749`.
6. Hold Steinitz until the local bilingual packet is checked and mirrored.

## Same-Day Author Record Refreshes

| Author | Concept DOI | Refreshed version DOI | Payload |
|---|---|---|---|
| Arthur Cayley | `10.5281/zenodo.20520749` | `10.5281/zenodo.20521540` | Replaced repaired Volume VI, VII, VIII, XI, and XIII readers plus refreshed `Cayley_source_and_manifest_20260603.zip`. |
| Arthur Cayley | `10.5281/zenodo.20520749` | `10.5281/zenodo.20522228` | Replaced rebuilt Volume II reader plus refreshed `Cayley_source_and_manifest_20260603.zip` after Paper 109 determinant-array repair. |
| Arthur Cayley | `10.5281/zenodo.20520749` | `10.5281/zenodo.20522518` | Replaced reconciled 485-page Volume XIII reader plus refreshed `Cayley_source_and_manifest_20260603.zip` after Paper 932 native table repair. |

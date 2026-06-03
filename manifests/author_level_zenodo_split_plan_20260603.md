# Author-Level Zenodo Split Plan - 2026-06-03

This plan records which mixed shelves should be split into dedicated author records. It is intentionally separate from the raw/provenance lane: large working archives stay on the main landing/provenance record, while author records should remain reader-facing and comparatively lean.

## Existing Author Records

| Author / corpus | Current record | Action |
|---|---:|---|
| Emmy Noether | `20412587` | Update existing record. Current GitHub state has German/English numbered papers complete through Paper 43 and Spanish/Japanese cumulative readers through Paper 15. |
| Heinrich Weber | `20412153` | Update existing record after outsourced Weber cumulative package is accepted. |
| Carl Friedrich Gauss | `20410934` | Update existing record after next Gauss cumulative audit. |
| Bernhard Riemann | `20429778` | Keep existing author record; not urgent. |
| Richard Dedekind | `20520669` | Dedicated author record created 2026-06-03. |
| P. G. Lejeune Dirichlet | `20520679` | Dedicated author record created 2026-06-03. |
| James Joseph Sylvester | `20520692` | Dedicated author record created 2026-06-03. |

## New Author Records To Create

| Author | Staged metadata | First reader-facing payload | Source/provenance policy |
|---|---|---|---|
| Arthur Cayley | `zenodo-metadata/metadata_author_cayley_current.json` | Current Cayley volume readers from `reader-pdfs/classical/`, including complete Volume I and repaired slice readers. | Attach compact current TeX/manifests; keep large raw and broad repair dumps on main provenance DOI. |
| Ernst Steinitz | `zenodo-metadata/metadata_author_steinitz_current.json` | Existing Steinitz reader from the author cluster; newer local bilingual packets still need mirroring/checking. | Do not create until the current local Steinitz packet is mirrored and checked. |

## Newly Created Author Records

| Author | Concept DOI | First version DOI | Payload |
|---|---|---|---|
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
5. Create Cayley author record or, if the repair state is still too patchwork, update the classical shelf once more while marking it explicitly as an interim umbrella.
6. Hold Steinitz until the local bilingual packet is checked and mirrored.

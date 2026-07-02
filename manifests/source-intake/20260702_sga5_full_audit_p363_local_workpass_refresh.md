# SGA5 Local Workpass Refresh Through p363

Date: 2026-07-02

This manifest records a local SGA5 workpass/audit refresh found during the archive sweep. It is a metadata/provenance update only.

## Local Source

`C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\SGA continuation 2\_claude_aid\sga5_full_audit_20260623`

## Observed State

The local workpass TeX/PDF/log were rebuilt again after the earlier p360 checkpoint. The compile log reports:

`Output written on sga5_fr_workpass.pdf (307 pages, 2017325 bytes).`

The newest clearly inspectable `AGENT_SCORECARD.md` evidence reaches p363. It records:

- p360: Expose VIII section 5 on pseudo-coherent complexes opens; diagram D174 is verified.
- p361: diagrams D175 and D176 are verified. D176 includes an editor label addition (`f`) where the scan has an unlabeled bottom arrow; the label is kept and noted, not treated as a source error.
- p362: section 5 closes and sections 6/7 begin, with perfect complexes and the important ring case; no TeX fix and no diagram.
- p363: section 7 continues with `K_\bullet(A)=K(D^b(A)_\mathrm{coh})`, `K^\bullet(A)=K(D(A)_\mathrm{parf})`, and the noetherian-ring comparison; no TeX fix and no diagram.

Fresh p364 crops and patch-candidate material exist under `_work`, but p364 is not promoted by this manifest. The stale rerun patch JSON also records many failed agent returns; this supports keeping the public claim at live workpass/provenance level only.

## File Hashes

| File | Bytes | Modified Local | SHA256 |
|---|---:|---|---|
| `CERT_LOG.md` | 729493 | 2026-07-02T03:08:14 | `C7944C3CDAC0D49977CB739C7CDB88D4C3A9117C09F474027EDFD835B3FE8ADE` |
| `AGENT_SCORECARD.md` | 618798 | 2026-07-02T03:07:45 | `98CADACD9D23A196D92820F62CBA287A31BC80FD3234E90FCAD7D4E585C06D13` |
| `sga5_fr_workpass.tex` | 844619 | 2026-07-02T03:13:29 | `E3BA3ED39124D869D019198D46BC51999D318FBBEA13F6AF4377848CB513581E` |
| `sga5_fr_workpass.pdf` | 2017325 | 2026-07-02T03:14:01 | `FFB712E1C6B9FD47C4106833C9365E48BF5877C7DCB4C5C3E00EF8C8EC6A2DEA` |
| `sga5_fr_workpass.log` | 360411 | 2026-07-02T03:14:01 | `A5586D2276E18745E4376DCB055974FF2D69904FCB8CD6CE31FCDC45AC6A78A4` |
| `_work\swarm_results\patches_rerun.json` | 123100 | 2026-06-24T07:36:45 | `1A9E1C0336ACDC9067F41135538DF501AD81F37A520E85907453F85C93C5FB07` |

## Public Caveat

This is not a promoted compact SGA5 delta, not a reader release, not English synchronization, not SGA5 completion, not global source-faithfulness certification, and not critical-edition material. It is useful live workpass/provenance evidence. Local ledger phrases such as clean, certified, complete, or perfect must be read as page-local workpass claims unless and until a separate archive promotion package is built and reviewed.

# SGA5 Local Workpass Refresh Through p360

Date: 2026-07-02

This manifest records a local SGA5 workpass/audit refresh found during the archive sweep. It is a metadata/provenance update only.

## Local Source

`C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\SGA continuation 2\_claude_aid\sga5_full_audit_20260623`

## Observed State

The local workpass TeX/PDF/log hashes remain the same as the p355 refresh, but the running `CERT_LOG.md` and `AGENT_SCORECARD.md` have advanced. The compile log still reports:

`Output written on sga5_fr_workpass.pdf (307 pages, 2017325 bytes).`

The newest clearly inspectable AGENT_SCORECARD evidence reaches p360. It records:

- p351: Expose VIII starts, Grothendieck/Bucur, class groups of abelian and triangulated categories.
- p352: fix #33, reverting an editor/source-fidelity `\psi` tag back to source `\varphi`.
- p353-p354: diagrams D165-D170 checked in the Expose VIII triangulated-category section.
- p355: fix #34, correcting a copied source typo/type error in the K(F) formula from `cl_C(F(X,X'))` to `cl_{C''}(F(X,X'))`, plus diagram D171 checked.
- p356-p359: Proposition 3.1 and section 4 checked; p358 verifies diagrams D172-D173; section 4 closes with comparison between abelian and triangulated K-groups.
- p360: section 5 on pseudo-coherent complexes opens; diagram D174 is verified.

## File Hashes

| File | Bytes | SHA256 |
|---|---:|---|
| `CERT_LOG.md` | 722800 | `1D24241CC2BF64AA401C32675D7E9083CB2172CA33446BF4D551FC255D42C9D1` |
| `AGENT_SCORECARD.md` | 614654 | `C4CB043C358CADCC2CF78A91A35AC9B4FB278A90808D5FFE2029D257050A4EFB` |
| `sga5_fr_workpass.tex` | 844619 | `258CDD405EDC705ED26D5E607E1A74A1B17457CFE1B7DD207D9087FF92804497` |
| `sga5_fr_workpass.pdf` | 2017325 | `7AC1725BC322C70B98CC844E177AC0125D90D3344ED09506DB6D706F1A396747` |
| `sga5_fr_workpass.log` | 360411 | `F8AE4712F19E7BEB60B3EFCCCDC72F0E7AAB9958966A2593BD0E53A8FC853767` |

## Public Caveat

This is not a promoted compact SGA5 delta, not a reader release, not English synchronization, not SGA5 completion, not global source-faithfulness certification, and not critical-edition material. It is useful live workpass/provenance evidence. Local ledger phrases such as clean, certified, complete, or perfect must be read as page-local workpass claims unless and until a separate archive promotion package is built and reviewed.

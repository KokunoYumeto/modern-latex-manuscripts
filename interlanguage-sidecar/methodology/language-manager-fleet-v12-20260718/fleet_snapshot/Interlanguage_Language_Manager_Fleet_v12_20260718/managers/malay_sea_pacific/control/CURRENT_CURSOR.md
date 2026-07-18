# Current production cursor

## Completed immediately before this cursor

The complete Indonesian working translation of Noether Paper 36 is built and visually checked at:

`03_projects/language_management/malay_sea_pacific/03_working_translations/noether/paper36/tranche_001_id_20260717/`

## Active decision

Translate the same complete one-page Noether Paper 36, *Idealdifferentiation und Differente*, independently into Malaysian Malay (`ms-MY`). Do not derive it through mechanical substitution from Indonesian.

## Exact source unit

- Current cumulative authority: `03_projects/noether/03_translation_workspaces/romance_rebase_20260717/authority_r823/pkg_r823/Noether_R823_WebB_R822_P20p27_31_RunInDashRefine_20260717/1/01_cumulative/Noether_R823_cum_de.tex`, lines 18600–18610.
- Exact standalone R823 wrapper SHA-256: `49B95034B3873A1759991427B3665F0EA72DEE221E0E92672230702342EDE41E`.
- One-page scan SHA-256: `6E6D797671475455C982CE9A39A81B193406A34B4DA02446E81C6065715BA105`.
- Boundary: complete five-segment work `P36-S0001`–`P36-S0005`.
- Translate directly from German. Indonesian and CJK translations are comparison witnesses only.

## Target contract

- Language/standard: Malaysian Malay (`ms-MY`).
- Script: Latin for this tranche. Jawi is not inferred without a mathematical witness and a declared reader need.
- Register: formal university/research mathematical prose.
- Status: working, source-reconciled translation; no native-review or finality claim.

## Recovered candidate evidence

Primary extracted sources:

- University of Malaya English-to-Bahasa-Malaysia mathematical terms.
- University of Malaya Bahasa-Malaysia-to-English mathematical terms.
- UKM Malay mathematics course/register descriptions.
- UMT Malay mathematics programme descriptions.
- DBP/PRPM snapshots where the exact concept is present.

Current lexical/string candidates, not exact-sense decisions:

| Source concept | Recovered Malay candidate evidence | Open decision |
| --- | --- | --- |
| differentiation | `pembezaan` | compound `Idealdifferentiation` is not directly witnessed |
| ideal | `unggulan`, `unggul`; Malay course prose uses `Unggulan` | confirm algebraic-number-theory register; do not import Indonesian `ideal` automatically |
| field | `medan` | exact compound “algebraic number field” absent |
| algebraic number | `nombor algebra` | candidate compound `medan nombor algebra` requires exact-sense review |
| quotient | `hasil bahagi` | exact `Differentialquotient` phrase absent |
| differential | `pembezaan`, `terbitan`, and related forms | decide the correct head/compound for Noether's ideal-theoretic sense |
| interpolation formula | `rumus interpolasi` | Lagrange attribution is separately attested in course prose |
| Differente | no recovered Malay witness | retain the italicized German source term unless specialist evidence is found |

## Immediate work

1. Check the Malay source corpus for exact or near-exact algebraic-number-theory contexts for `medan nombor algebra`, differential quotient of an ideal, and *Differente*.
2. Record competitor and absence rows before choosing compounds.
3. Translate all five segments directly from German.
4. Build twice with XeLaTeX, extract text, render the one page, and inspect it.
5. Deliver a separate TeX/PDF/ledger/manifest/hash package parallel to—but not textually derived from—the Indonesian tranche.

## Later cursor

After Malaysian Malay Paper 36, return to the longer Indonesian Noether Paper 06 introduction. Vietnamese and Thai remain the strongest separate non-Malayic next-language candidates; Māori remains the strongest Pacific local-register candidate.


# Noether Romance French Institutional License Gap Addendum

Status: source-canon/provenance addendum; draft / non-canonical / not native reviewed / not approved / not license-cleared / not gate-promoted.

Created: 2026-07-04.

## Scope

This addendum deepens the two remaining French course-PDF rights/license gaps:

- `FR-C-007`: Mourougane, `ACGA-cours` 2024-2025.
- `FR-C-010`: Marche, `Theorie geometrique des invariants`, M2 notes.

It does not translate text, approve terms, claim native review, claim canonical approval, claim license clearance, promote gates, or push Git.

## Probe Artifacts

Machine-readable probe files:

- `outputs/NOETHER_ROMANCE_SOURCE_CANON_FRENCH_INSTITUTIONAL_LICENSE_PROBES_20260704.csv`
- `outputs/NOETHER_ROMANCE_SOURCE_CANON_FRENCH_INSTITUTIONAL_LICENSE_PROBES_CLASSIFIED_20260704.csv`

The probe records URL, HTTP status, content type, fetched byte count, SHA-256 where fetched, rights-term hit count, classification, source-canon effect, and non-claim boundary. Full page bodies were not saved in this addendum.

## Probe Results

| Row | Probe | URL | Result |
| --- | --- | --- | --- |
| `FR-C-007` | ACGA course page | `https://perso.univ-rennes1.fr/christophe.mourougane/enseignements/2024-25/ACGA/ACGA.html` | HTTP 200; page reachable; no reuse/license grant found. The detected `CC` string is a course-assessment false positive, not a license signal. |
| `FR-C-007` | ACGA direct PDF | `https://perso.univ-rennes1.fr/christophe.mourougane/enseignements/2024-25/ACGA/ACGA-cours.pdf` | HTTP 200; SHA-256 matches local PDF `c3c2588f0ab62edcb4a8dbf2014afe5dc5f8b8fc1d54c595a29fdc016aa93dd6`; binary-body rights hit ignored; prior `pdftotext`/`mutool` probe remains controlling and found no reuse grant. |
| `FR-C-007` | Author home | `https://perso.univ-rennes1.fr/christophe.mourougane/` | HTTP 200; no rights/reuse terms found. |
| `FR-C-007` | University of Rennes legal page | `https://www.univ-rennes.fr/mentions-legales` | HTTP 200; legal page contains intellectual-property and reproduction-reserved language. This deepens the rights boundary but is not a permissive license for the course PDF. |
| `FR-C-007` | University regulation PDF | `https://www.univ-rennes.fr/sites/www.univ-rennes.fr/files/medias/files/REGLEMENT_INTERIEUR_VOTE_PAR_CA_2025-06-26_Et_ses_ANNEXES.pdf` | HTTP 200; general copyright context only; no course-PDF reuse grant. |
| `FR-C-010` | M2 teaching page | `https://webusers.imj-prg.fr/~julien.marche/enseignement_M2.html` | HTTP 200; page links the GIT notes and separately marks some references as not to be diffused; no reuse/license grant for the GIT PDF found. |
| `FR-C-010` | GIT direct PDF | `https://webusers.imj-prg.fr/~julien.marche/M2/GIT.pdf` | HTTP 200; SHA-256 matches local PDF `8731e06f40b8354d58d6d938418d6e061a81af1efda2d4524dddaf1b6084c384`; binary-body rights hit ignored; prior `pdftotext`/`mutool` probe remains controlling and found no reuse grant. |
| `FR-C-010` | Author home | `https://webusers.imj-prg.fr/~julien.marche/` | HTTP 200; no rights/reuse terms found. |
| `FR-C-010` | IMJ-PRG legal page | `https://www.imj-prg.fr/mentions-legales` | HTTP 200; legal page contains conditions/intellectual-property language. This deepens the rights boundary but is not a permissive license for the course PDF. |
| `FR-C-010` | Alternate bare IMJ host | `https://imj-prg.fr/mentions-legales` | Connection refused; no change because canonical `www.imj-prg.fr` legal page was reachable. |

## Source-Canon Effect

- `FR-C-007` remains a French PDF/text fallback witness for Hilbert-basis theorem context.
- `FR-C-010` remains a French PDF fallback witness for geometric invariant theory register.
- Both rows now have deeper institutional rights/access evidence.
- Both rows retain explicit rights/license gaps: no TeX/source archive verified, no permissive reuse grant found, no license-clearance claim.

## Updated Tables

Updated machine-readable tables:

- `outputs/NOETHER_ROMANCE_SOURCE_CANON_WITNESS_TABLE_20260704.csv`
- `outputs/NOETHER_ROMANCE_SOURCE_CANON_WITNESS_TABLE_REQUIRED_SHAPE_20260704.csv`
- `outputs/NOETHER_ROMANCE_SOURCE_CANON_FIELD_COMPLETENESS_AUDIT_20260704.csv`

The update changes provenance language only. It does not change the number of Romance source-canon rows or close the weak/gap license status.

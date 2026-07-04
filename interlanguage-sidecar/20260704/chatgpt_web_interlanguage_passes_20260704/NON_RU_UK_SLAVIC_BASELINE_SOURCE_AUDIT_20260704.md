# Non-RU/UK Slavic baseline source audit — 2026-07-04

Boundary: native independent non-Russian/non-Ukrainian Slavic PDF source/reference shelf. This is eligible for `language_family_witness` work after context review. The term probes below are `pdftotext` form-hit counts, not automatic term promotion.

## Bundle inventory
- Downloaded PDF sources: **20**
- Languages: Bulgarian 2, Croatian 2, Czech 6, Polish 6, Serbian 1, Slovak 1, Slovenian 2
- Branch groups: South Slavic 7, West Slavic 13
- Manifest SHA-256 check: **all match**
- Known pages: **1147**; extracted text chars: **2,686,745**

## Source records
| id | branch | language | pages | chars | role |
|---|---:|---:|---:|---:|---|
| `czech_cuni_algebra_2021` | West Slavic | Czech | 120 | 412566 | broad algebra ring/body/field control |
| `czech_cuni_telesa_pole_note` | West Slavic | Czech | 3 | 6941 | explicit commutative field versus noncommutative body distinction |
| `czech_cuni_noncommutative_body_thesis` | West Slavic | Czech | 26 | 55168 | division-ring/body and Brauer-group control |
| `czech_karlin_commutative_rings_fields` | West Slavic | Czech | 118 | 79227 | Noetherian ring/module and field-theory control |
| `czech_karlin_galois_splitting_field` | West Slavic | Czech | 14 | 10052 | splitting-field register control |
| `czech_cuni_representation_idempotents` | West Slavic | Czech | 59 | 147306 | representation/idempotent/left-ideal control |
| `polish_impan_algebra_lecture3` | West Slavic | Polish | 10 | 8458 | Polish ring/field/homomorphism control |
| `polish_uwr_algebra2_rings` | West Slavic | Polish | 17 | 161610 | Polish ring terminology control |
| `polish_mimuw_noncommutative_body` | West Slavic | Polish | 66 | 172371 | noncommutative body/quaternion control |
| `polish_uj_algebra1_noetherian` | West Slavic | Polish | 65 | 315017 | Noetherian/splitting-field/ideal control |
| `polish_mimuw_algebra2_galois` | West Slavic | Polish | 48 | 85886 | Galois/splitting-field register control |
| `polish_mimuw_left_ideals_idempotents` | West Slavic | Polish | 23 | 12366 | left-ideal/idempotent associative-algebra control |
| `slovak_abstraktna_algebra` | West Slavic | Slovak | 70 | 176995 | Slovak okruh/teleso/grupa axis control |
| `slovenian_uvod_v_algebro` | South Slavic | Slovenian | 262 | 615045 | Slovenian kolobar/polje/algebra/homomorphism control |
| `slovenian_komutativna_algebra_noetherian` | South Slavic | Slovenian | 3 | 7110 | Noetherian kolobar/modul control |
| `serbian_belgrade_algebra_i_lecture9` | South Slavic | Serbian | 17 | 35404 | Serbian Cyrillic prsten/polje control |
| `croatian_mathhr_algebra_structures_2024` | South Slavic | Croatian | 116 | 298953 | Croatian prsten/polje/tijelo axis control |
| `croatian_pmf_split_prsteni` | South Slavic | Croatian | 101 | 67719 | Croatian ring/polynomial register control |
| `bulgarian_sofia_rings_lecture7` | South Slavic | Bulgarian | 4 | 5700 | Bulgarian ring/field Cyrillic register control |
| `bulgarian_sofia_noncommutative_body_problem` | South Slavic | Bulgarian | 5 | 12851 | Bulgarian noncommutative body/quaternion control |

## Concept probe summary
| concept | total hits | by branch | by evidence class |
|---|---:|---|---|
| `basis` | 140 | {'South Slavic': 21, 'West Slavic': 119} | {'support': 140} |
| `corollary` | 191 | {'South Slavic': 89, 'West Slavic': 102} | {'intl': 15, 'native': 176} |
| `determinant` | 66 | {'South Slavic': 30, 'West Slavic': 36} | {'intl': 45, 'west_native': 21} |
| `extension` | 902 | {'South Slavic': 129, 'West Slavic': 773} | {'generic': 902} |
| `field` | 1113 | {'South Slavic': 497, 'West Slavic': 616} | {'support_or_related': 1113} |
| `group` | 6443 | {'South Slavic': 3391, 'West Slavic': 3052} | {'support': 6443} |
| `homomorphism` | 659 | {'South Slavic': 259, 'West Slavic': 400} | {'support': 659} |
| `ideal` | 1614 | {'South Slavic': 1035, 'West Slavic': 579} | {'support': 1614} |
| `idempotent` | 304 | {'South Slavic': 44, 'West Slavic': 260} | {'support': 304} |
| `invariant` | 15 | {'West Slavic': 15} | {'support': 15} |
| `module` | 558 | {'South Slavic': 117, 'West Slavic': 441} | {'support': 558} |
| `polynomial` | 1363 | {'South Slavic': 859, 'West Slavic': 504} | {'intl': 885, 'west_native': 478} |
| `quotient_field` | 32 | {'South Slavic': 10, 'West Slavic': 22} | {'south_possible': 10, 'west_competitor': 22} |
| `ring` | 4338 | {'South Slavic': 2671, 'West Slavic': 1667} | {'south_competitor_cyr': 118, 'south_competitor_latin': 2553, 'west_competitor': 1667} |
| `splitting_field` | 52 | {'South Slavic': 32, 'West Slavic': 20} | {'generic': 52} |
| `theorem` | 1122 | {'South Slavic': 268, 'West Slavic': 854} | {'intl': 268, 'west_native': 854} |
| `trace` | 349 | {'South Slavic': 324, 'West Slavic': 25} | {'native': 349} |

## Immediate implications
- This ZIP is the missing broad non-East Slavic **source/reference** shelf, not a LaTeX translation feed. It should sit under `language_family_witness`, not `draft_translation_triangulation`.
- It materially strengthens the W/S shelf already used for `ring`, `quotient field`, F12 West-calque checks, and variant/doublet policy.
- Because the package contains PDFs, the next safe grind is context-window extraction for the review-priority rows (`ring`, `quotient_field`) and then C2 row fill. The sources should not be treated as reviewed until row-context snippets are checked.
- The manifest confirms no additional local non-RU/UK Slavic TeX/PDF files were found in the `extra_local_latex_or_pdf_found` scan; this is not the lost Slavic LaTeX translation corpus.
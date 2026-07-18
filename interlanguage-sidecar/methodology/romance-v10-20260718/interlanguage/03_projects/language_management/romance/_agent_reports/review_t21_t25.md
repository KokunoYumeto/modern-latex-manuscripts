# Internal occurrence review — T21–T25

Date: 2026-07-17  
Scope: fresh, bounded, read-only semantic review of every extracted occurrence for T21–T25 against the explicit v6 senses.  
Reviewer tier: Codex internal source-context review. No form promotion, human observation, intelligibility result, or license clearance is asserted.

## Frozen inputs

| Artifact | SHA-256 |
|---|---|
| 03_redo_ultra_20260717/wordweb/ROMANCE_TERM_OCCURRENCES_v1.csv | 6DF8FAD570D48369CA0A8FE06CD5A0EBC3C21275677E35BEDCF077208865DEE8 |
| 03_redo_ultra_20260717/wordweb/PAN_ROMANCE_WORDWEB_v6.json | 0D4B581A2CE3F6664B1A97A44AAD023ED1FDC6C023FED5ADE42677E445751AD4 |

I inspected the stored quote and adjacent source lines for all 58 rows. Each occurrence ID appears exactly once below as accepted with one modeled sense, rejected, or held. Acceptance means semantic fit only; it does not convert a mechanical context candidate into promoted evidence. Repeated navigation labels and translated/template families are identified separately and must not be counted as independent prose attestations.

## Exact outcome

| Term | Extracted | Accepted | Rejected | Hold | Modeled-sense result |
|---|---:|---:|---:|---:|---|
| T21 invariant | 6 | 4 | 2 | 0 | T21-S1: 3; T21-S2: 1 |
| T22 basis | 19 | 6 | 13 | 0 | T22-S1: 6; T22-S2: 0 |
| T23 rank | 12 | 6 | 5 | 1 | T23-S1: 1; T23-S2: 4; T23-S3: 1 |
| T24 center | 7 | 3 | 4 | 0 | T24-S1: 3 |
| T25 extension | 14 | 8 | 6 | 0 | T25-S1: 7; T25-S2: 0; T25-S3: 1 |
| **Total** | **58** | **27** | **30** | **1** | every extracted ID classified exactly once |

No term in T21–T25 has zero extracted rows. The following explicit modeled senses nevertheless remain zero-hit gaps: T22-S2 historical ideal basis and T25-S2 scalar extension. No row directly supports either sense.

## T21 — invariant

Accepted:

| Occurrence ID | Sense | Decision and reason |
|---|---|---|
| OCC-EF7497F66DAD5A8E | T21-S1 invariant_object | accepted / fixed_under_explicit_Q_action — a subset of Qgp is explicitly invariant under the action of Q |
| OCC-AE63A1F83183BC7C | T21-S1 invariant_object | accepted / mutation_class_invariant — the cluster algebra is an invariant of the mutation class |
| OCC-344E5A4568C7A286 | T21-S2 invariant_theory_form | accepted / classical_binary_form_invariant — the discriminant is identified as an invariant of a binary form in an explicit history of invariant theory |
| OCC-EF7D92B9CE0F9869 | T21-S1 invariant_object | accepted / preserved_by_symmetry_transformations — the property is preserved by the transformations constituting the symmetry group |

Rejected:

| Occurrence ID | Classification | Reason |
|---|---|---|
| OCC-CD8D29A71D8CCF87 | rejected_wrong_sense | invariant_basis_number_compound — names the invariant basis number property; it is neither an object fixed by a specified action nor an invariant polynomial/form |
| OCC-0656FC5309458378 | rejected_wrong_sense | invariant_basis_number_compound — Portuguese instance of the same unmodeled property |

The two invariant-basis-number rows are a translated module-article family. Both are adverse to treating bare invariant as sufficient evidence for T21 and are not independent support.

## T22 — basis

Accepted for T22-S1 linear_basis:

| Occurrence ID | Decision and reason |
|---|---|
| OCC-29043AFDCC8D2288 | accepted / canonical_vector_basis — standard coordinate vectors are explicitly called the canonical basis |
| OCC-F1B7B80E0A9674C2 | accepted / cluster_algebra_linear_basis — construction of a canonical basis of the cluster algebra |
| OCC-86B38FE76D068CCD | accepted / Lie_algebra_basis — a displayed family is explicitly a basis of sl2(S) as an S-Lie algebra |
| OCC-EC69DDB13A370D6F | accepted / vector_space_and_dual_bases — fixes a basis of M/M², its associated dual basis, and a basis of a Hom space |
| OCC-BAF4B149C822FB8B | accepted / free_module_basis — a free module is described as having a free basis and as a direct sum of copies of the scalar ring |
| OCC-9414F0167831A397 | accepted / vector_space_basis — vector-space passage explicitly lists existence of a basis and dimension |

Rejected:

| Occurrence ID | Classification | Reason |
|---|---|---|
| OCC-31A59543452E768B | rejected_wrong_sense | free_monoid_basis_unmodeled — S is a basis of a free commutative monoid, not a linear basis or historical ideal basis |
| OCC-7B8F73BF2BEF7D84 | rejected_wrong_sense | base_space_compound — topological base space in a fundamental-group passage |
| OCC-5CFD61B9462BBABB | rejected_adverse | ordinary_foundation — cyclic group is “at the base of” the Caesar cipher |
| OCC-0DDA66745C8B3089 | rejected_adverse | criterion_based_on — structures distinguished “com base no” number of operations |
| OCC-6D923BEA1FBAA10D | rejected_adverse | ordinary_foundation — axioms as a basis for future study and unification on a common set of concepts |
| OCC-9785ABD072D803F5 | rejected_adverse | premise_for_later_proof — proved proposition used as a basis for another proof |
| OCC-1A47F57D2230F4E4 | rejected_adverse | historical_foundation — integers served as the basis for formulating the ring concept |
| OCC-0069CA0483C13084 | rejected_adverse | based_on_common_concepts — ordinary foundation/conceptual-basis construction |
| OCC-468CE1233B81ADC4 | rejected_adverse | foundation_of_treatments — structure provides the basis of formal treatments of calculus |
| OCC-577C8F25268C0B21 | rejected_adverse | Italian_in_base_al — phrase means “according to the sign,” not a noun meaning mathematical basis |
| OCC-8D109F7F1BC76B47 | rejected_wrong_sense | induction_base_case — logical base case, not linear or ideal basis |
| OCC-1616C5C1C91BBEE9 | rejected_adverse | Romanian_basic_terms — bază functions adjectivally in “undefined basic terms” |
| OCC-6E9A5EE2D89EE690 | rejected_adverse | ordinary_foundation — Romanian “at the base of” the Caesar cipher |

OCC-5CFD61B9462BBABB and OCC-6E9A5EE2D89EE690 are a translated group-article/Caesar-cipher family and must not be counted independently. No occurrence supports T22-S2 historical_ideal_basis.

## T23 — rank

Accepted:

| Occurrence ID | Sense | Decision and reason |
|---|---|---|
| OCC-DFC1021A4322A1C0 | T23-S3 generic_module_rank | accepted / group_completion_generic_rank — rank of Qgp is the dimension obtained after scalar passage from the finitely generated abelian group, matching the generic-rank mechanism rather than matrix or free-group rank |
| OCC-13F47FD20DFD504F | T23-S2 free_module_rank | accepted / locally_free_module_rank — ΩX,x is explicitly free of rank equal to the Krull dimension |
| OCC-3697B5C4B986706F | T23-S2 free_module_rank | accepted / free_R_algebra_rank — Q is explicitly a free R-algebra of rank four with a displayed R-basis |
| OCC-C41FA996075D5CCB | T23-S2 free_module_rank | accepted / basis_cardinality_of_free_module — Portuguese module passage defines posto as the potentially nonunique number of elements in a free-module basis |
| OCC-0142541E093802D4 | T23-S1 matrix_rank | accepted / matrix_rank_section — Rango section immediately introduces matrix minors and the matrix-rank definition |
| OCC-BBAEC24D3E0B310B | T23-S2 free_module_rank | accepted / explicit_free_module_rank — Italian text directly calls n the rank of the free module |

Rejected:

| Occurrence ID | Classification | Reason |
|---|---|---|
| OCC-C2161805E1BA58F2 | rejected_wrong_sense | free_group_rank_unmodeled |
| OCC-6805F7E3EDF1C646 | rejected_wrong_sense | cluster_rank_cardinality — rank is the constant cardinality of a cluster, not a matrix or module rank |
| OCC-1FE515EA705A7824 | rejected_wrong_sense | free_group_rank_unmodeled |
| OCC-772BCF7D00AC8532 | rejected_wrong_sense | free_group_rank_unmodeled |
| OCC-37EA3F1AEB88678D | rejected_wrong_sense | free_group_rank_unmodeled |

Hold:

| Occurrence ID | Reason |
|---|---|
| OCC-A4959F10886D9D49 | hold / navigation_rank_ambiguous — bare French Rang occurs in a linear-algebra navigation list near vector families, bases, dimension, and subspaces, but the stored source window does not distinguish matrix rank from family/subspace rank; forcing T23-S1 or T23-S2 would invent specificity |

The Spanish, Portuguese, Catalan, and Romanian free-group-rank rows are the same Cayley-graph/group-article translation family. All four are wrong-sense evidence, not four independent rank attestations for the modeled senses.

## T24 — center

Accepted for T24-S1 center:

| Occurrence ID | Decision and reason |
|---|---|
| OCC-126BD7712C451B3A | accepted / ring_center — A is contained in Cen(B), explicitly glossed as the center of B |
| OCC-A0A0F3DB1D2C5356 | accepted / enveloping_algebra_center — the Casimir element generates the center of the enveloping algebra |
| OCC-6386FE7C67BC4B53 | accepted / ring_page_navigation_label — Galician Centro is a ring-page subsection beside subrings, ideals, and units; accepted only as a lexical navigation label, not as independent defining prose |

Rejected:

| Occurrence ID | Classification | Reason |
|---|---|---|
| OCC-F48A770A0C3617EA | rejected_adverse | institutional_center_in_commented_title — Centro de Investigación en Matemáticas |
| OCC-A77491067FA5A71E | rejected_wrong_sense | Lie_algebra_center_unmodeled — center of a reductive Lie algebra, whereas v6 T24-S1 explicitly defines the ring center |
| OCC-86B5899552CE69D4 | rejected_adverse | molecular_geometric_center — inversion through the center of a molecule |
| OCC-126C55E4C4C5ED0A | rejected_adverse | sphere_geometric_center — sphere centered at the origin |

The institutional and two geometric uses are direct adverse evidence against accepting bare centro/centre by surface form alone.

## T25 — extension

Accepted:

| Occurrence ID | Sense | Decision and reason |
|---|---|---|
| OCC-FCBFEE325B7A3D6F | T25-S1 structure_extension | accepted / finite_valuation_ring_extension — R→S explicitly described as a finite extension of valuation rings |
| OCC-9E96884D41998AFD | T25-S3 map_extension | accepted / linear_extension_of_map — group action on S is given by C-linear extension of a specified map |
| OCC-C15981A19E4EA15B | T25-S1 structure_extension | accepted / field_extensions — field theory explicitly studies extensions of fields |
| OCC-5FA0ACEE9D28FC78 | T25-S1 structure_extension | accepted / field_extension_navigation — Galician field-page subsection Extensión de corpos; lexical navigation evidence only |
| OCC-BFAC6A7ED7F7335B | T25-S1 structure_extension | accepted / finite_number_field_extension — a number field is a finite extension of the rationals and contains them as a subfield |
| OCC-4B9C35E9F26ECC7D | T25-S1 structure_extension | accepted / real_over_rational_field_extension — R is explicitly an extension of Q |
| OCC-17B08DBF84F80999 | T25-S1 structure_extension | accepted / field_extension_navigation — Italian field-page section and subsections on algebraic and transcendental extensions; navigation evidence only |
| OCC-06D859CA13430936 | T25-S1 structure_extension | accepted / ring_extension — construction of the smallest subring containing the starting ring and an adjoined subset is explicitly called an extension of rings |

Rejected:

| Occurrence ID | Classification | Reason |
|---|---|---|
| OCC-704C010B1BB3EFB7 | rejected_adverse | disciplinary_generalization — abstract algebra is said not to be a simple extension of arithmetic |
| OCC-83AF0FCC7D62D7C7 | rejected_wrong_sense | quiver_principal_extension_unmodeled — extends a quiver by adding vertices and arrows, not a ring/field, scalar, or map extension under v6 |
| OCC-4B4B206DAC50DDFC | rejected_wrong_language_and_sense | English extension_blocks inside an explicitly English abstract embedded in the French source; also a category/Ext-block sense not modeled here |
| OCC-A25441B791D4C29F | rejected_adverse | extension_of_theory — generalization of Galois theory to continuous symmetry groups |
| OCC-CB37413119DDA006 | rejected_adverse | extension_of_associativity — natural generalization of associativity to empty/infinite products |
| OCC-59E4EDC7A8EDEC4C | rejected_adverse | extension_of_theory — Catalan translation-family instance of extending Galois theory to continuous symmetry groups |

OCC-A25441B791D4C29F and OCC-59E4EDC7A8EDEC4C are a Portuguese/Catalan translation family and are adverse evidence, not independent structure-extension support. OCC-5FA0ACEE9D28FC78 and OCC-17B08DBF84F80999 are correct lexical section labels but not running-prose definitions. No occurrence supports T25-S2 scalar_extension.

## Exact machine-side ID lists

Accepted (27):

OCC-EF7497F66DAD5A8E, OCC-AE63A1F83183BC7C, OCC-344E5A4568C7A286, OCC-EF7D92B9CE0F9869, OCC-29043AFDCC8D2288, OCC-F1B7B80E0A9674C2, OCC-86B38FE76D068CCD, OCC-EC69DDB13A370D6F, OCC-BAF4B149C822FB8B, OCC-9414F0167831A397, OCC-DFC1021A4322A1C0, OCC-13F47FD20DFD504F, OCC-3697B5C4B986706F, OCC-C41FA996075D5CCB, OCC-0142541E093802D4, OCC-BBAEC24D3E0B310B, OCC-126BD7712C451B3A, OCC-A0A0F3DB1D2C5356, OCC-6386FE7C67BC4B53, OCC-FCBFEE325B7A3D6F, OCC-9E96884D41998AFD, OCC-C15981A19E4EA15B, OCC-5FA0ACEE9D28FC78, OCC-BFAC6A7ED7F7335B, OCC-4B9C35E9F26ECC7D, OCC-17B08DBF84F80999, OCC-06D859CA13430936.

Rejected (30):

OCC-CD8D29A71D8CCF87, OCC-0656FC5309458378, OCC-31A59543452E768B, OCC-7B8F73BF2BEF7D84, OCC-5CFD61B9462BBABB, OCC-0DDA66745C8B3089, OCC-6D923BEA1FBAA10D, OCC-9785ABD072D803F5, OCC-1A47F57D2230F4E4, OCC-0069CA0483C13084, OCC-468CE1233B81ADC4, OCC-577C8F25268C0B21, OCC-8D109F7F1BC76B47, OCC-1616C5C1C91BBEE9, OCC-6E9A5EE2D89EE690, OCC-C2161805E1BA58F2, OCC-6805F7E3EDF1C646, OCC-1FE515EA705A7824, OCC-772BCF7D00AC8532, OCC-37EA3F1AEB88678D, OCC-F48A770A0C3617EA, OCC-A77491067FA5A71E, OCC-86B5899552CE69D4, OCC-126C55E4C4C5ED0A, OCC-704C010B1BB3EFB7, OCC-83AF0FCC7D62D7C7, OCC-4B4B206DAC50DDFC, OCC-A25441B791D4C29F, OCC-CB37413119DDA006, OCC-59E4EDC7A8EDEC4C.

Hold (1):

OCC-A4959F10886D9D49.

## Integration constraints

1. Preserve every accepted row as internal semantic-review evidence only; no form, bridge, or cohort promotion follows from this review.
2. Keep translated/template families folded and do not sum them as independent support.
3. Do not infer T22-S2 from generic basis rows, T23 matrix/module rank from free-group or cluster rank, ring-center support from Lie/geometric center, or T25-S2 from generic uses of extension.
4. Preserve the English embedded-abstract row OCC-4B4B206DAC50DDFC as wrong-language/adverse evidence.
5. The inherited ES/FR core records remain quotation-free and unresolved; none of these extension-node contexts can be reported as core promotion.

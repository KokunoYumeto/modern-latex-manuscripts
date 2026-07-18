# Independent semantic occurrence review: T36–T40

Date: 2026-07-17  
Scope: every T36–T40 occurrence in the frozen v1 occurrence table, reviewed against WordWeb v7  
Reviewer status: Codex internal semantic review; not human attestation  
Production edits: none

## Frozen inputs

- `03_redo_ultra_20260717/wordweb/ROMANCE_TERM_OCCURRENCES_v1.csv`
  - SHA-256: `6DF8FAD570D48369CA0A8FE06CD5A0EBC3C21275677E35BEDCF077208865DEE8`
- `03_redo_ultra_20260717/wordweb/PAN_ROMANCE_WORDWEB_v7.json`
  - SHA-256: `A48BF8C89F252A0274D2FDE2FE8A2E6E6E3077AD81A4B60BFA0B5FFF44A1A366`

Every stored quote was inspected at its exact locator, with adjacent source lines opened for thin hits. “Accepted” means only a reviewed match to the explicit modeled sense shown below. It does not promote a form, count as human attestation, or establish intelligibility. Navigation labels, code comments, and derivational substring leaks are held rather than counted as independent body attestations. Clear mathematical but unmodeled senses are rejected as wrong-sense rows; an adverse target is named only when the occurrence is actually adverse to a modeled sense.

## Result

| Term | Raw rows | Accepted body matches | Rejected/wrong sense | Held | Independent body-attestation count |
|---|---:|---:|---:|---:|---:|
| T36 divisibility | 6 | 3 | 0 | 3 | 3 |
| T37 power | 12 | 7 | 2 | 3 | 7 |
| T38 matrix | 12 | 8 | 0 | 4 | 8 |
| T39 group | 21 | 19 | 0 | 2 | 19 |
| T40 subgroup | 19 | 19 | 0 | 0 | 19 |
| **Total** | **70** | **56** | **2** | **12** | **56** |

No term has zero raw rows. T37-S2 `ideal_power` has zero accepted support in this tranche. Accepted T37 evidence splits into T37-S1 element power = 5 and T37-S3 prime power = 2. All accepted rows for T36, T38, T39, and T40 map respectively to T36-S1, T38-S1, T39-S1, and T40-S1.

## Exact ID lists

### T36

Accepted:

`OCC-C55CA95961752173`, `OCC-9D99D9BCC82698B5`, `OCC-EB1B01CC7DF54531`

Rejected/adverse: none.

Held:

`OCC-4319C50EC2EE8199`, `OCC-9503AD323D4B9512`, `OCC-CD5BC44BDA9E07D3`

### T37

Accepted:

`OCC-A92E390B17EED1F1`, `OCC-EDF91E46E105A8B3`, `OCC-FDB2E97B03050EF6`, `OCC-A61F0DE29F1D4202`, `OCC-D74EDDF993896602`, `OCC-CB263D14B4AE7191`, `OCC-926BF3E5888415CB`

Rejected/wrong sense:

`OCC-083DCC1CFD7872A3`, `OCC-64840CB73A653DFB`

Held:

`OCC-2EACDF8D40BD2232`, `OCC-2C40AFE31C10C8AE`, `OCC-4D8A78A5A6AB0050`

### T38

Accepted:

`OCC-DA41691EE0C9F0FC`, `OCC-C0C897186C70BD7D`, `OCC-989783CEC84E7906`, `OCC-345605AFFF75651A`, `OCC-3BBA808D4CD2CBA5`, `OCC-7AAC0FE13BE66828`, `OCC-1BA8AABF8B078E00`, `OCC-B5514956D3EA968E`

Rejected/adverse: none.

Held:

`OCC-4B0BE8D09019A5AF`, `OCC-294DFB7F51C36D81`, `OCC-F52BB4F6D1E2A13F`, `OCC-77D0BE7622072E31`

### T39

Accepted:

`OCC-83048397D53C23F2`, `OCC-F97468AE08ED5864`, `OCC-366DC55C4C59E3F7`, `OCC-FB5B23582BE0301F`, `OCC-419DC2A2ECAFEF42`, `OCC-7794ADBE2C214D6B`, `OCC-DA020128B7CAE444`, `OCC-3DE23B6F04BF8FD8`, `OCC-6CF669324B7C705C`, `OCC-E3E4B2D2D52A46AB`, `OCC-55377C8E1AE83ABF`, `OCC-14CC72D19EE87BBD`, `OCC-83A014E16AE667C4`, `OCC-DB3D55741B058561`, `OCC-A8A9814618AE0147`, `OCC-37D89394364D5BE1`, `OCC-33731D1ACEF74ADB`, `OCC-B1FBCBA50A6E3598`, `OCC-FC9D6E83EC11CD01`

Rejected/adverse: none.

Held:

`OCC-07552FD5F9AB9323`, `OCC-52A474006C2DEF83`

### T40

Accepted:

`OCC-7B369963E48BE528`, `OCC-5AEA21F23E795D59`, `OCC-FC362E206F9784F2`, `OCC-0796F59803BE313C`, `OCC-1638DA12EBC948CE`, `OCC-32CC9C7A22E14C9D`, `OCC-888E5E66C022FCF0`, `OCC-3C68C3023CC49EBF`, `OCC-B72FADC5AAF4B878`, `OCC-04721CEC9366402E`, `OCC-70526DD139F8B519`, `OCC-3A4CA75E48732F90`, `OCC-E408ADF9479EF3A6`, `OCC-988C5347C5A1F8E6`, `OCC-E7D888F76BAE4729`, `OCC-75AC0070CBE5DD13`, `OCC-B081CBDC3A206737`, `OCC-A4689651E1B9EFDD`, `OCC-3A3FD82DD2011FD2`

Rejected/adverse: none.  
Held: none.

## Occurrence-by-occurrence decisions

### T36 — divisibility

| Occurrence ID | Lang | Decision | Sense/candidate | Adverse target | Reason code | Review note |
|---|---|---|---|---|---|---|
| OCC-C55CA95961752173 | es | accepted | T36-S1 | none | `INTEGER_POLYNOMIAL_DIVISIBILITY` | Ring-history body explicitly discusses divisibility of integers and polynomials. |
| OCC-9D99D9BCC82698B5 | fr | accepted | T36-S1 | none | `DIVISIBILITY_RELATION_NATURALS` | Natural numbers are explicitly equipped with the divisibility relation. |
| OCC-4319C50EC2EE8199 | ca | held | T36-S1 candidate | none | `IDEAL_DIVISIBILITY_DEFINITION_UNSTATED` | Related ring-theory body says `divisibilitat per ideals`, but does not state whether the modeled element relation or a distinct ideal-divisibility relation is intended. |
| OCC-9503AD323D4B9512 | it | held | T36-S1 candidate | none | `NAVIGATION_TEMPLATE_ONLY` | `Criteri di divisibilità` occurs only in an arithmetic navigation family. |
| OCC-EB1B01CC7DF54531 | it | accepted | T36-S1 | none | `INTEGRAL_DOMAIN_DIVISIBILITY_DEFINITION` | Body prose gives the modeled definition: one element divides another when the latter is its product with some element. |
| OCC-CD5BC44BDA9E07D3 | it | held | T36-S1 candidate | none | `DUPLICATE_NAVIGATION_TEMPLATE` | Exact duplicate `Criteri di divisibilità` template row in a second page; not a second body attestation. |

### T37 — power

| Occurrence ID | Lang | Decision | Sense/candidate | Adverse target | Reason code | Review note |
|---|---|---|---|---|---|---|
| OCC-A92E390B17EED1F1 | es | accepted | T37-S1 | none | `MONOID_ELEMENT_POWER` | A power of element `b` is used explicitly in a primary-ideal proof. |
| OCC-EDF91E46E105A8B3 | es | accepted | T37-S1 | none | `NILPOTENT_ELEMENT_POWER` | A power of `z` vanishes; surrounding formulas display iterated element powers. |
| OCC-FDB2E97B03050EF6 | es | accepted | T37-S1 | none | `POWER_ASSOCIATIVE_RECURSIVE_DEFINITION` | Body explicitly defines `x^(n+1)=x x^n`, matching iterated element product. |
| OCC-A61F0DE29F1D4202 | fr | accepted | T37-S1 | none | `COMMUTATIVE_RING_ELEMENT_POWER` | Elements divide powers of other elements in a commutative ring. |
| OCC-083DCC1CFD7872A3 | fr | rejected/wrong sense | none | none | `EXTERIOR_POWER_UNMODELED` | `Puissance extérieure` is the exterior-power construction, not element, ideal, or prime power; the hit is also navigation-only. |
| OCC-64840CB73A653DFB | pt | rejected/wrong sense | none | none | `CARTESIAN_POWER_UNMODELED` | Cartesian power of a set is a distinct modeled-missing sense, not an iterated algebraic product. |
| OCC-D74EDDF993896602 | gl | accepted | T37-S1 | none | `BINOMIAL_ELEMENT_POWER` | Running proof-history prose refers to the power of a binomial. |
| OCC-CB263D14B4AE7191 | gl | accepted | T37-S3 | none | `PRIME_POWER` | Finite-field order is explicitly a power of a prime. |
| OCC-926BF3E5888415CB | ca | accepted | T37-S3 | none | `PRIME_POWER` | Same explicit prime-power condition in Catalan finite-field prose. |
| OCC-2EACDF8D40BD2232 | it | held | T37-S1 candidate | none | `POWER_ASSOCIATIVITY_NAV_TEMPLATE` | `Associatività della potenza` is a navigation label, not body evidence. |
| OCC-2C40AFE31C10C8AE | it | held | T37-S1 candidate | none | `DUPLICATE_POWER_NAV_TEMPLATE` | Same navigation template in a second page. |
| OCC-4D8A78A5A6AB0050 | it | held | T37-S1 candidate | none | `DUPLICATE_POWER_NAV_TEMPLATE` | Same navigation template in a third page. |

T37-S2 ideal power remains unsupported. The two rejected rows are distinct mathematical senses, so they have no adverse target beyond being unsafe for automatic assignment to any current T37 sense.

### T38 — matrix

| Occurrence ID | Lang | Decision | Sense/candidate | Adverse target | Reason code | Review note |
|---|---|---|---|---|---|---|
| OCC-DA41691EE0C9F0FC | es | accepted | T38-S1 | none | `SQUARE_COEFFICIENT_MATRIX` | Explicit square `s × s` matrix with coefficients in a field. |
| OCC-C0C897186C70BD7D | es | accepted | T38-S1 | none | `OPERATOR_MATRIX_LINEAR_MAP` | Operator-entry matrix defines a module-linear map. |
| OCC-989783CEC84E7906 | es | accepted | T38-S1 | none | `MATRIX_RING_AND_MATRIX_UNIT` | Matrix ring and an explicit `n × n` matrix with prescribed entries. |
| OCC-345605AFFF75651A | fr | accepted | T38-S1 | none | `CARTAN_MATRIX` | Displayed Cartan matrix of a rank-two root system. |
| OCC-4B0BE8D09019A5AF | fr | held | T38-S1 candidate | none | `CODE_MACRO_COMMENT_ONLY` | `% matrice 2 x 2` comments a LaTeX macro declaration; no running-source assertion. |
| OCC-3BBA808D4CD2CBA5 | fr | accepted | T38-S1 | none | `LIE_AUTOMORPHISM_MATRIX` | A Lie-algebra automorphism is explicitly expressed by a displayed matrix in an ordered basis. |
| OCC-7AAC0FE13BE66828 | pt | accepted | T38-S1 | none | `RECTANGULAR_ARRAY_DEFINITION` | Running linear-algebra body defines matrices as rectangular arrays of values. |
| OCC-1BA8AABF8B078E00 | pt | accepted | T38-S1 | none | `MATRIX_RING_AND_MATRIX_UNIT` | Matrix ring context with a matrix having one specified unit entry. |
| OCC-B5514956D3EA968E | it | accepted | T38-S1 | none | `LINEAR_MAP_MATRIX_PRODUCT` | Matrices represent linear maps and composition is represented by matrix product. |
| OCC-294DFB7F51C36D81 | it | held | T38-S1 candidate | none | `NAVIGATION_TEMPLATE_ONLY` | Bare `Matrice` in a ring-theory navigation family. |
| OCC-F52BB4F6D1E2A13F | it | held | T38-S1 candidate | none | `DUPLICATE_NAVIGATION_TEMPLATE` | Same bare `Matrice` template row in a second page. |
| OCC-77D0BE7622072E31 | ro | held | T38-S1 candidate | none | `TOC_COMPOUND_ONLY` | `Grupuri de matrice` appears only as a contents entry for matrix groups at this locator. |

### T39 — group

| Occurrence ID | Lang | Decision | Sense/candidate | Adverse target | Reason code | Review note |
|---|---|---|---|---|---|---|
| OCC-83048397D53C23F2 | es | accepted | T39-S1 | none | `UNIT_GROUP` | Explicit unit group of an algebra. |
| OCC-F97468AE08ED5864 | es | accepted | T39-S1 | none | `GROUP_IS_MONOID` | Running definitions state every group is a monoid and contrast group/monoid theory. |
| OCC-366DC55C4C59E3F7 | es | accepted | T39-S1 | none | `FUNDAMENTAL_GROUP` | Fundamental group in a representation/monodromy context. |
| OCC-07552FD5F9AB9323 | fr | held | T39-S1 candidate | none | `SUBGROUP_DERIVATIONAL_SUBSTRING_LEAK` | Exact source expression is `sous-groupe`; this row is accepted under T40, but must not double-count as an independent T39 body occurrence. |
| OCC-FB5B23582BE0301F | fr | accepted | T39-S1 | none | `FINITE_PRODUCT_GROUP_ACTION` | Explicit group `Gamma = Z_2 × Z_2` acting on Lie algebras. |
| OCC-419DC2A2ECAFEF42 | fr | accepted | T39-S1 | none | `FINITE_AUTOMORPHISM_GROUP` | Finite group acting by automorphisms in running algebra prose. |
| OCC-7794ADBE2C214D6B | pt | accepted | T39-S1 | none | `RUBIK_GROUP` | Rubik-cube group in a group-theory body. |
| OCC-DA020128B7CAE444 | pt | accepted | T39-S1 | none | `ALGEBRAIC_STRUCTURE_GROUP` | Groups listed as algebraic structures distinguished by operations and axioms. |
| OCC-3DE23B6F04BF8FD8 | pt | accepted | T39-S1 | none | `GROUP_STRUCTURE_EXPLICIT` | Rubik permutations are said to have group structure. |
| OCC-52A474006C2DEF83 | gl | held | T39-S1 candidate | none | `TOC_COMPOUND_ONLY` | Transformation/automorphism group appears only in the contents block. |
| OCC-6CF669324B7C705C | gl | accepted | T39-S1 | none | `MULTIPLICATIVE_ABELIAN_GROUP` | Nonzero field elements form an abelian multiplicative group. |
| OCC-E3E4B2D2D52A46AB | gl | accepted | T39-S1 | none | `RING_ADDITIVE_GROUP` | Ring definition explicitly requires a commutative group under addition. |
| OCC-55377C8E1AE83ABF | ca | accepted | T39-S1 | none | `MODULE_UNDERLYING_ABELIAN_GROUP` | Module structure explicitly includes an abelian group. |
| OCC-14CC72D19EE87BBD | ca | accepted | T39-S1 | none | `RUBIK_PERMUTATION_GROUP` | Rubik permutations form a group in running abstract-algebra prose. |
| OCC-83A014E16AE667C4 | ca | accepted | T39-S1 | none | `RING_ADDITIVE_GROUP_AXIOMS` | Ring definition supplies additive-group identity, inverses, associativity, and commutativity. |
| OCC-DB3D55741B058561 | it | accepted | T39-S1 | none | `EXPLICIT_GROUP_DEFINITION` | A monoid is defined as a group when every element has a two-sided inverse. |
| OCC-A8A9814618AE0147 | it | accepted | T39-S1 | none | `ALGEBRAIC_GROUP_COMPOUND` | Algebraic-group use in field/Galois history; the added structure does not change the underlying group sense. |
| OCC-37D89394364D5BE1 | it | accepted | T39-S1 | none | `RING_ADDITIVE_ABELIAN_GROUP` | Ring definition explicitly requires an abelian additive group. |
| OCC-33731D1ACEF74ADB | ro | accepted | T39-S1 | none | `RING_ADDITIVE_ABELIAN_GROUP` | Same substantive ring axiom in Romanian. |
| OCC-B1FBCBA50A6E3598 | ro | accepted | T39-S1 | none | `GROUP_AS_CORE_ALGEBRAIC_STRUCTURE` | Running group-theory prose identifies groups as central algebraic structures. |
| OCC-FC9D6E83EC11CD01 | ro | accepted | T39-S1 | none | `RUBIK_PERMUTATION_GROUP` | Rubik permutations form a group in an abstract-algebra body. |

### T40 — subgroup

| Occurrence ID | Lang | Decision | Sense | Adverse target | Reason code | Review note |
|---|---|---|---|---|---|---|
| OCC-7B369963E48BE528 | es | accepted | T40-S1 | none | `ABELIAN_GROUP_CONGRUENCE_SUBGROUP` | Image of a congruence under a homomorphism is a subgroup; inverse-image correspondence is stated. |
| OCC-5AEA21F23E795D59 | es | accepted | T40-S1 | none | `FINITE_GROUP_PERMUTATION_SUBGROUP` | Every finite group is a subgroup of a permutation group. |
| OCC-FC362E206F9784F2 | es | accepted | T40-S1 | none | `PERMUTATION_SUBGROUP` | Any permutation group is a subgroup of the symmetric group. |
| OCC-0796F59803BE313C | fr | accepted | T40-S1 | none | `MAXIMAL_UNIPOTENT_SUBGROUP` | Explicit maximal unipotent subgroup in an algebraic-group setting. |
| OCC-1638DA12EBC948CE | fr | accepted | T40-S1 | none | `ROOT_SUBGROUP` | `Q=2Z` is explicitly the root subgroup in the additive group `P`. |
| OCC-32CC9C7A22E14C9D | fr | accepted | T40-S1 | none | `SUBMODULE_ADDITIVE_SUBGROUP` | Submodule definition requires `N` to be a subgroup of `(M,+)`. |
| OCC-888E5E66C022FCF0 | pt | accepted | T40-S1 | none | `PERMUTATION_SUBGROUP` | Permutation group as subgroup of a symmetric group. |
| OCC-3C68C3023CC49EBF | pt | accepted | T40-S1 | none | `FINITE_GROUP_PERMUTATION_SUBGROUP` | Historical theorem context with `G` a subgroup of `S_5`. |
| OCC-B72FADC5AAF4B878 | pt | accepted | T40-S1 | none | `SUBMODULE_ADDITIVE_SUBGROUP` | Submodule definition begins with an additive subgroup. |
| OCC-04721CEC9366402E | gl | accepted | T40-S1 | none | `PERMUTATION_SUBGROUP` | Permutation group as subgroup of a symmetric group. |
| OCC-70526DD139F8B519 | gl | accepted | T40-S1 | none | `FINITE_MULTIPLICATIVE_SUBGROUP` | Finite subgroup of a field’s multiplicative group. |
| OCC-3A4CA75E48732F90 | gl | accepted | T40-S1 | none | `SUBRING_ADDITIVE_SUBGROUP` | A subring is explicitly an additive subgroup. |
| OCC-E408ADF9479EF3A6 | ca | accepted | T40-S1 | none | `FINITE_GROUP_PERMUTATION_SUBGROUP` | Every finite group is a subgroup of a permutation group. |
| OCC-988C5347C5A1F8E6 | ca | accepted | T40-S1 | none | `PERMUTATION_SUBGROUP` | Group `G` is a subgroup of the symmetric group. |
| OCC-E7D888F76BAE4729 | ca | accepted | T40-S1 | none | `FINITE_MULTIPLICATIVE_SUBGROUP` | Finite subgroup of a field’s multiplicative group. |
| OCC-75AC0070CBE5DD13 | it | accepted | T40-S1 | none | `EXPLICIT_SUBGROUP_DEFINITION` | Immediate body definition: a subset of a group that is itself a group under the same operation. |
| OCC-B081CBDC3A206737 | it | accepted | T40-S1 | none | `FINITE_MULTIPLICATIVE_SUBGROUP` | Finite subgroup of a field’s multiplicative group. |
| OCC-A4689651E1B9EFDD | it | accepted | T40-S1 | none | `SUBRING_ADDITIVE_SUBGROUP` | A subring is explicitly an additive subgroup closed under multiplication. |
| OCC-3A3FD82DD2011FD2 | ro | accepted | T40-S1 | none | `PERMUTATION_SUBGROUP` | Permutation group as subgroup of a symmetric group. |

## Duplicate/template and integration cautions

1. T36 `OCC-9503AD323D4B9512` and `OCC-CD5BC44BDA9E07D3` are the same Italian `Criteri di divisibilità` navigation family. Neither is an independent body attestation.
2. T37 `OCC-2EACDF8D40BD2232`, `OCC-2C40AFE31C10C8AE`, and `OCC-4D8A78A5A6AB0050` are the same Italian `Associatività della potenza` navigation family.
3. T38 `OCC-294DFB7F51C36D81` and `OCC-F52BB4F6D1E2A13F` are the same Italian bare-`Matrice` navigation family. The French macro comment and Romanian contents label are also non-body evidence.
4. T39 `OCC-07552FD5F9AB9323` is the same physical source hit as the accepted T40 French `sous-groupe` occurrence. It must not be counted once for subgroup and again as an independent standalone-group attestation.
5. Identical quote hashes for bare `group/subgroup` strings across distinct running-language bodies do not by themselves establish a template duplicate. The T40 rows retained as accepted have substantive local propositions or definitions.
6. No row in this review promotes a form, supplies human attestation, changes a cohort score, or licenses a pilot/intelligibility claim.

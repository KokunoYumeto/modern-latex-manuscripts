# Internal occurrence review — T11–T15

Date: 2026-07-17  
Scope: read-only semantic review of every occurrence currently extracted for T11–T15.  
Reviewer tier: Codex internal context review; no form promotion, no human observation, and no intelligibility claim.

## Frozen inputs

| Artifact | SHA-256 |
|---|---|
| `03_redo_ultra_20260717/wordweb/ROMANCE_TERM_OCCURRENCES_v1.csv` | `6DF8FAD570D48369CA0A8FE06CD5A0EBC3C21275677E35BEDCF077208865DEE8` |
| `03_redo_ultra_20260717/wordweb/PAN_ROMANCE_WORDWEB_v5.json` | `4B2B92D18F2823B1173AF6A9AD7F06FD990813452451F553F7623C300DDFFC5B` |

The classifications below answer only whether a quoted occurrence matches one of the explicit v5 senses. `accepted` does not mean promoted, independently attested, license-cleared, or human-validated. I inspected the full stored quote and adjacent source lines for every nonempty term. Repeated navigation/template labels remain separate occurrence IDs but are not treated as independent running-prose quotations.

## Exact outcome

| Term | Extracted | Accepted | Rejected | Hold | Result |
|---|---:|---:|---:|---:|---|
| T11 relatively prime | 0 | 0 | 0 | 0 | explicit zero-hit gap for both modeled senses |
| T12 least common multiple | 1 | 1 | 0 | 0 | one clear T12-S1 match |
| T13 greatest common divisor | 4 | 4 | 0 | 0 | four T13-S1 matches; three are the same Italian navigation template |
| T14 product | 20 | 16 | 3 | 1 | 13 T14-S1, 3 T14-S3, no T14-S2 evidence |
| T15 factor | 13 | 12 | 1 | 0 | 7 T15-S1, 5 T15-S2, no T15-S3 evidence |
| **Total nonempty occurrences** | **38** | **33** | **4** | **1** | no wrong-language rows found |

## T11 — relatively prime

No current occurrence exists for T11. This is a corpus gap, not negative evidence. It leaves both explicit v5 senses without occurrence support:

- `T11-S1 relatively_prime_elements`: zero occurrence matches.
- `T11-S2 comaximal_generated_ideals`: zero occurrence matches.

The inherited ES/FR seed records do not cure this gap because they contain no quotations.

## T12 — least common multiple

Accepted for `T12-S1 least_common_multiple`:

- `OCC-D52C7C0632C0FD24` — `accepted / exact_term_in_UFD_statement`: Italian source says that every pair of elements in a unique-factorization domain has a greatest common divisor and a least common multiple. This is the modeled algebraic sense, not merely an initialism or bibliography label.

Rejected: none. Hold: none.

## T13 — greatest common divisor

Accepted for `T13-S1 greatest_common_divisor`:

- `OCC-9E2CC75E86A70EB9` — `accepted / math_navigation_label_MCD`: Italian `MCD`, surrounded by divisors, coprime integers, Bézout identity, `mcm`, and Euclidean algorithm.
- `OCC-2EAA99526AECE0C7` — `accepted / math_navigation_label_MCD`: same mathematically disambiguating navigation sequence on a second page.
- `OCC-6B588AE33943B89B` — `accepted / math_navigation_label_MCD`: same mathematically disambiguating navigation sequence on a third page.
- `OCC-513F9CB0A847D534` — `accepted / explicit_polynomial_gcd`: Romanian running text explicitly calls `r(x)` the greatest common divisor of two polynomials.

The three Italian `MCD` rows are semantically correct lexical labels, but they are one repeated navigation-template evidence family rather than three independent prose attestations. They must not be summed as three independent quotations for promotion.

Rejected: none. Hold: none.

## T14 — product

### Accepted for `T14-S1 multiplicative_product` (13)

- `OCC-131584C7675B48BF` — `accepted / algebra_multiplication`: a displayed multiplication induces a product on `G(R)` making it a graded algebra.
- `OCC-0E1702D0DFA7F04E` — `accepted / algebra_multiplication`: the product in `A` is explicitly identified with composition in `End_A(A)`.
- `OCC-8804B2F795FFC5CC` — `accepted / product_of_powers`: cluster monomial defined as a product of positive powers.
- `OCC-9FA2FC27D8AFB147` — `accepted / matrix_product`: explicit matrix product calculation.
- `OCC-B4AEC435302C4B75` — `accepted / Euler_product`: Euler product formula in an algebraic-number-theory passage.
- `OCC-67DA8C04582F72F3` — `accepted / matrix_product`: matrix product `AB`, followed by an explanation of multiplication of square matrices.
- `OCC-1AE2087FD4C69969` — `accepted / group_operation_product`: a group is closed under product and inverse.
- `OCC-58B7F85C42732507` — `accepted / field_multiplication`: nonzero elements are invertible with respect to the product operation.
- `OCC-866549268EF99357` — `accepted / module_action_product`: adjacent Catalan text states that the product belongs to the module in the module-action context; stripped formulas make the quote thin but the local sense is still multiplication.
- `OCC-964C6351AC8E7AE0` — `accepted / ring_operation_product`: ring definition names its second binary operation `producte`.
- `OCC-1E7337EA09D84541` — `accepted / extended_real_multiplication`: heading for the sum and product operations on the extended reals.
- `OCC-5027536F60E1521B` — `accepted / ring_operation_product`: internal operations explicitly named sum and product and compared with rational-number operations.
- `OCC-3C37DC0098E5DFB9` — `accepted / polynomial_product`: every polynomial described as a product of degree-one polynomials.

### Accepted for `T14-S3 direct_product` (3)

- `OCC-3FA6FDA62AE7A321` — `accepted / direct_product`: the direct sum of monoids is defined as a submonoid of `\prod_i M_i`; this is the direct/cartesian product construction.
- `OCC-7BE5570564DAFDAE` — `accepted / cartesian_power`: algebraic operation typed from a Cartesian power of a set.
- `OCC-536B5CF1BF2844F2` — `accepted / cartesian_product`: Italian section explicitly defines `prodotto cartesiano A × B`.

### Rejected (3)

- `OCC-3A624F791BE8AE0E` — `rejected_wrong_sense / tensor_product_unmodeled`: `produit tensoriel g \otimes S` is a named tensor-product construction; it is neither ambient multiplication, ideal product, nor the v5 direct/cartesian-product sense.
- `OCC-575DEDACE17E4844` — `rejected_adverse / ordinary_causal_result`: mathematical proof is described as a product of ancient Greek mathematicians; this is an ordinary causal/result sense.
- `OCC-A59BA5D3C0F196B5` — `rejected_adverse / ordinary_causal_result`: mathematics is described as a product of human thought; this is ordinary prose, not algebraic multiplication.

### Hold (1)

- `OCC-6A20983E3E964DEB` — `hold / exterior_product_compound`: a historical sentence says Grassmann introduced the exterior product. The phrase is mathematical, but the local passage does not establish whether this row should be attached to generic ambient multiplication or represented by a distinct compound/sense edge. Do not force it into T14-S1 from this quote alone.

No current occurrence supports `T14-S2 ideal_product`.

## T15 — factor

### Accepted for `T15-S1 multiplicative_factor` (7)

- `OCC-52402A5D8ADE6FFE` — `accepted / integer_multiplicative_factor`: an even integer expression has 2 as a factor. This is an integer factor, not an ideal or quotient.
- `OCC-BB4ABD5CB160116B` — `accepted / tensor_factors`: the first and second factors of `k_0 \otimes k_0` are the objects participating in that product.
- `OCC-6E78B1085F34FE13` — `accepted / integer_multiplicative_factor`: Galician proof says a sum has 2 as a factor.
- `OCC-6C85DC9B04FE051D` — `accepted / common_integer_factor`: Catalan irrationality-proof context specifies integers with no common factor.
- `OCC-37D3CE8C2CFF05E9` — `accepted / scalar_multiplier_factor`: determinant gives the multiplicative scaling factor for areas and volumes.
- `OCC-3B3359BB4DC21315` — `accepted / product_factor`: an irreducible element divides a product but neither factor.
- `OCC-4FE18012F439124D` — `accepted / irreducible_polynomial_factor`: an irreducible factor of a polynomial.

### Accepted for `T15-S2 quotient_or_factor_object` (5)

- `OCC-65A723BAEE193003` — `accepted / factor_algebra_quotient`: the associated graded ring is a factor of a polynomial algebra; the surrounding construction is quotient/factor-algebra usage, not a multiplicative factor.
- `OCC-065EDE76429D42E2` — `accepted / quotient_group`: Portuguese source explicitly pairs `grupo fator` with `grupo quociente` and writes `G/...`.
- `OCC-644086A8BC130A48` — `accepted / quotient_ring`: Galician source explicitly glosses `anel factor (ou cociente)` and writes a polynomial-ring quotient.
- `OCC-CFDDAAAD942F1CA1` — `accepted / quotient_ring`: Catalan `anell factor` followed by the polynomial-ring quotient notation.
- `OCC-53A6AD487706E58E` — `accepted / quotient_group`: Romanian `grup factor G/H`.

### Rejected (1)

- `OCC-152D76C3FA7BE9F4` — `rejected_wrong_sense / direct_factor_unmodeled_navigation`: French `Facteur direct` is a navigation-list label for a direct summand/factor of a module. It is not a multiplicative factor, factor-ring quotient, or factor-system occurrence under the explicit v5 senses.

Hold: none. No current occurrence supports `T15-S3 factor_system`.

## Exact ID lists for machine-side integration

Accepted (33):

`OCC-D52C7C0632C0FD24`, `OCC-9E2CC75E86A70EB9`, `OCC-2EAA99526AECE0C7`, `OCC-6B588AE33943B89B`, `OCC-513F9CB0A847D534`, `OCC-131584C7675B48BF`, `OCC-0E1702D0DFA7F04E`, `OCC-8804B2F795FFC5CC`, `OCC-9FA2FC27D8AFB147`, `OCC-B4AEC435302C4B75`, `OCC-67DA8C04582F72F3`, `OCC-1AE2087FD4C69969`, `OCC-58B7F85C42732507`, `OCC-866549268EF99357`, `OCC-964C6351AC8E7AE0`, `OCC-1E7337EA09D84541`, `OCC-5027536F60E1521B`, `OCC-3C37DC0098E5DFB9`, `OCC-3FA6FDA62AE7A321`, `OCC-7BE5570564DAFDAE`, `OCC-536B5CF1BF2844F2`, `OCC-52402A5D8ADE6FFE`, `OCC-BB4ABD5CB160116B`, `OCC-6E78B1085F34FE13`, `OCC-6C85DC9B04FE051D`, `OCC-37D3CE8C2CFF05E9`, `OCC-3B3359BB4DC21315`, `OCC-4FE18012F439124D`, `OCC-65A723BAEE193003`, `OCC-065EDE76429D42E2`, `OCC-644086A8BC130A48`, `OCC-CFDDAAAD942F1CA1`, `OCC-53A6AD487706E58E`.

Rejected (4):

`OCC-3A624F791BE8AE0E`, `OCC-575DEDACE17E4844`, `OCC-A59BA5D3C0F196B5`, `OCC-152D76C3FA7BE9F4`.

Hold (1):

`OCC-6A20983E3E964DEB`.

Zero-hit gap: `T11` (both `T11-S1` and `T11-S2`).

## Integration constraints

1. Keep `accepted` as internal semantic review only; every row remains `candidate_not_promoted` until the lane's provenance, license, independence, and cohort gates are satisfied.
2. Do not count the three Italian `MCD` template rows as three independent quotations.
3. Do not infer ideal-product support from generic product rows; `T14-S2` is still at zero.
4. Do not infer factor-system support from generic or quotient factors; `T15-S3` is still at zero.
5. Integer factors (`factor de 2`, `factor en comú`, irreducible polynomial factor) support T15-S1 only and must not be promoted as evidence for ideal factorization terminology.
6. The inherited ES/FR core seed records retain zero quotations and must remain distinct from these mechanically extracted, internally reviewed context rows.

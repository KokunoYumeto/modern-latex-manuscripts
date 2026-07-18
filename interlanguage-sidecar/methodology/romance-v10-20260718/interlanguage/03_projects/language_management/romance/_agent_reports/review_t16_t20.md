# Independent semantic occurrence review: T16–T20

Date: 2026-07-17  
Scope: every occurrence currently assigned to T16–T20 in the v1 occurrence table  
Reviewer status: Codex internal semantic review; not human validation  
Production edits: none

## Frozen inputs

- `03_redo_ultra_20260717/wordweb/ROMANCE_TERM_OCCURRENCES_v1.csv`
  - SHA-256: `6DF8FAD570D48369CA0A8FE06CD5A0EBC3C21275677E35BEDCF077208865DEE8`
- `03_redo_ultra_20260717/wordweb/PAN_ROMANCE_WORDWEB_v5.json`
  - SHA-256: `4B2B92D18F2823B1173AF6A9AD7F06FD990813452451F553F7623C300DDFFC5B`

I inspected the stored quotation and the adjacent source lines at every locator. “Accepted” means only that the occurrence is an internally reviewed lexical/sense match. It does **not** promote a form, supply a human intelligibility observation, or make a pilot claim. Navigation-only labels are held when the local body does not independently establish the sense. Wrong-language bibliography/code strings, explicit non-examples, material source errors, and adjacent mathematical senses outside the v5 definition are not treated as supporting evidence.

## Result

| Term | Occurrences | Accepted | Rejected/adverse | Hold |
|---|---:|---:|---:|---:|
| T16 decomposition | 14 | 11 | 1 | 2 |
| T17 representation | 14 | 8 | 3 | 3 |
| T18 homomorphism | 15 | 14 | 1 | 0 |
| T19 isomorphism | 20 | 17 | 1 | 2 |
| T20 automorphism | 10 | 7 | 0 | 3 |
| **Total** | **73** | **57** | **6** | **10** |

### Sense-level result

- T16-S1 `generic_decomposition`: 6 accepted; 1 wrong-language/code rejection.
- T16-S2 `direct_sum_decomposition`: 4 accepted.
- T16-S3 `primary_decomposition`: 1 accepted; 2 navigation-only holds.
- T17-S1 `direct_representation`: 8 accepted, including explicit group/ring/Lie representations and unambiguous representation-theory compounds; 2 wrong-language rejections; 3 navigation-only holds.
- T17-S2 `reciprocal_representation`: no supporting occurrence in this tranche.
- T17-S3 `representation_image`: no supporting occurrence in this tranche. One coordinate-matrix use is rejected as a different representation sense, not reassigned to S3.
- T18-S1 `homomorphism`: 14 accepted; 1 explicit crossed-homomorphism/non-homomorphism adverse record.
- T19-S1 `isomorphism`: 17 accepted; 1 source-error adverse record; 2 non-propositional holds.
- T20-S1 `automorphism`: 7 accepted; 2 navigation-only holds. One category-theoretic autoequivalence use is held because the broader sense is not represented in v5.

## Exact ID lists

### T16

Accepted:

`OCC-4FD456B68365596E`, `OCC-37D911D5F3BF3601`, `OCC-5E4605EAF4059DFD`, `OCC-4B0AF4AACA1CB8BD`, `OCC-0C684E9EDDA30134`, `OCC-F413CAACE1649037`, `OCC-D035BFEC124B070F`, `OCC-4CE594BED74B0DF0`, `OCC-6EE39C25B2B8CA1F`, `OCC-74C0C4E136747126`, `OCC-8DBE218A385B7A80`

Rejected/adverse:

`OCC-FD919D2A654E8276`

Hold:

`OCC-F5CFB29B5618B836`, `OCC-9D0B733A9E4C7DB9`

### T17

Accepted:

`OCC-855D9412D6D27E64`, `OCC-F1C5EFBC5CE14A4C`, `OCC-4F5A1C4DE08BB9C0`, `OCC-C3A8C52163E15CC2`, `OCC-FF38F968E23A33AD`, `OCC-6C9D18FB19B3793D`, `OCC-69D0BAF2C491C257`, `OCC-00AB352B7A5311F3`

Rejected/adverse:

`OCC-F4D3BF6D23492F3A`, `OCC-BE1E7350CD214AB5`, `OCC-47D17A78D3D65925`

Hold:

`OCC-18B9CAECB08871DC`, `OCC-310338F60B3D09A1`, `OCC-A794F6C6D498085E`

### T18

Accepted:

`OCC-0186A8073BD69F7A`, `OCC-98FD9E53A9E4943C`, `OCC-74AD623E3CAC4ECB`, `OCC-126EB43FE523C2AE`, `OCC-0EA46714BAEC564B`, `OCC-36606C586BE519AE`, `OCC-F4F55129362EE71D`, `OCC-F0893D305CBB55F6`, `OCC-3938B1FAFD350D08`, `OCC-5ABEAED9F770C54C`, `OCC-E6CE985F452E2607`, `OCC-B2670A8388E430FA`, `OCC-F002893BE948EA9A`, `OCC-00209D16575B5CE3`

Rejected/adverse:

`OCC-8FC255BA87A54893`

Hold: none.

### T19

Accepted:

`OCC-8787AED925CBE819`, `OCC-E217FF34500D3425`, `OCC-87AFBE7B36C87957`, `OCC-320847F8A031BF88`, `OCC-5EA8B2B9B26D2855`, `OCC-47BFDBF93BB7FCB1`, `OCC-AC96C2D81A417845`, `OCC-46032EF8074CE367`, `OCC-99A4BAD440782F01`, `OCC-E677297B9BAA3C38`, `OCC-EFC4AC63E3F2C411`, `OCC-CD5F6505DECDEF84`, `OCC-BC9C9D8513FB1722`, `OCC-F7A461FA2324B727`, `OCC-5581743365D1DC13`, `OCC-81EC860D331346B3`, `OCC-DC2BAE019EE5C968`

Rejected/adverse:

`OCC-A8FEE5299CCE3A40`

Hold:

`OCC-5E917BB01D56606D`, `OCC-76090F5CCE2C9E01`

### T20

Accepted:

`OCC-958D9B2A333E926B`, `OCC-B3C9F669A34EBA1B`, `OCC-21CA003B7FF8042B`, `OCC-BBD5DAA638D0A0DC`, `OCC-8C2B54D00C9E7DDE`, `OCC-1BBBAF23EDE00F6F`, `OCC-537655620D8C357B`

Rejected/adverse: none.

Hold:

`OCC-EC9D87555536A150`, `OCC-E3AD4842AA3687A3`, `OCC-D5BA86CC0588DC2F`

## Occurrence-by-occurrence decisions

### T16 — decomposition

| Occurrence ID | Lang | Decision | v5 sense | Reason code | Review note |
|---|---|---|---|---|---|
| OCC-4FD456B68365596E | es | accepted | T16-S3 | `PRIMARY_IDEAL_CONTEXT` | “descomposición primaria” occurs among primary ideals; exact primary-decomposition sense. |
| OCC-37D911D5F3BF3601 | es | accepted | T16-S1 | `PEIRCE_ALGEBRA_DECOMPOSITION` | Peirce decomposition in an associative-algebra history passage. |
| OCC-5E4605EAF4059DFD | es | accepted | T16-S2 | `DIRECT_SUM_EXPLICIT` | A graded module is given with an explicit direct-sum decomposition. |
| OCC-FD919D2A654E8276 | fr | rejected | T16-S1 candidate | `WRONG_LANGUAGE_CODE_LABEL` | English `Decomposition Theorem` occurs only in a LaTeX theorem-environment declaration inside a French body. |
| OCC-4B0AF4AACA1CB8BD | fr | accepted | T16-S2 | `BLOCK_DIRECT_SUM_EXPLICIT` | Category decomposition into blocks is immediately characterized by their direct sum. |
| OCC-0C684E9EDDA30134 | fr | accepted | T16-S1 | `ALGEBRAIC_ACTION_DECOMPOSITION` | Decomposition of a group action via Galois cohomology; unambiguously mathematical and constituent-based. |
| OCC-F413CAACE1649037 | pt | accepted | T16-S1 | `LU_MATRIX_DECOMPOSITION` | LU decomposition is a specified matrix decomposition in linear algebra. |
| OCC-D035BFEC124B070F | pt | accepted | T16-S1 | `PERMUTATION_CYCLE_DECOMPOSITION` | Decomposition of a permutation into cycles. |
| OCC-4CE594BED74B0DF0 | pt | accepted | T16-S2 | `DIRECT_SUM_EXPLICIT` | A graded ring module is supplied together with a direct-sum decomposition. |
| OCC-6EE39C25B2B8CA1F | gl | accepted | T16-S1 | `PERMUTATION_CYCLE_DECOMPOSITION` | Decomposition of a permutation as a product of cycles. |
| OCC-74C0C4E136747126 | ca | accepted | T16-S1 | `PEIRCE_ALGEBRA_DECOMPOSITION` | Peirce/Pierce decomposition in an associative-algebra history passage. |
| OCC-F5CFB29B5618B836 | it | hold | T16-S3 | `NAVIGATION_LABEL_ONLY` | Exact `Decomposizione primaria`, but only in a template/navigation list with no local proposition or definition. |
| OCC-9D0B733A9E4C7DB9 | it | hold | T16-S3 | `NAVIGATION_LABEL_ONLY` | Duplicate exact primary-decomposition label in another template/navigation instance. |
| OCC-8DBE218A385B7A80 | it | accepted | T16-S2 | `MODULE_DIRECT_SUM_DECOMPOSITION` | Krull–Schmidt context, with module addends and decomposition into indecomposable submodules; direct-sum sense is established. |

### T17 — representation

| Occurrence ID | Lang | Decision | v5 sense | Reason code | Review note |
|---|---|---|---|---|---|
| OCC-855D9412D6D27E64 | es | accepted | T17-S1 | `REGULAR_REPRESENTATION` | Regular representation of a monoid in active algebraic prose. |
| OCC-F1C5EFBC5CE14A4C | es | accepted | T17-S1 | `GROUP_REPRESENTATION_THEORY_COMPOUND` | Historical prose explicitly identifies representation theory of finite groups. |
| OCC-4F5A1C4DE08BB9C0 | es | accepted | T17-S1 | `GROUP_REPRESENTATION_THEORY_COMPOUND` | Running prose couples group theory with its representation theory and applications. |
| OCC-F4D3BF6D23492F3A | fr | rejected | T17-S1 candidate | `WRONG_LANGUAGE_BIBLIOGRAPHY` | English book/chapter title in a French bibliography; not French lexical attestation. |
| OCC-BE1E7350CD214AB5 | fr | rejected | T17-S1 candidate | `WRONG_LANGUAGE_ENGLISH_ABSTRACT` | Explicit `otherlanguage{english}` abstract in a French source. |
| OCC-C3A8C52163E15CC2 | fr | accepted | T17-S1 | `EXPLICIT_RHO_V_REPRESENTATION` | Explicit finite-dimensional irreducible representation `(rho,V)` of a Lie algebra. |
| OCC-18B9CAECB08871DC | pt | hold | T17-S1 | `TOC_LABEL_ONLY` | `Representação de grupos` occurs only as a local contents/navigation label. |
| OCC-47D17A78D3D65925 | pt | rejected | no exact v5 sense | `COORDINATE_REPRESENTATION_WRONG_SENSE` | A matrix as a coordinate representation of a linear transformation is neither the homomorphism sense S1 nor the R823 image-object sense S3. |
| OCC-FF38F968E23A33AD | pt | accepted | T17-S1 | `REPRESENTATION_THEORY_COMPOUND` | Running abstract-algebra prose characterizes representation theory as study of concrete realizations. |
| OCC-310338F60B3D09A1 | gl | hold | T17-S1 | `TOC_LABEL_ONLY` | `Representación de grupos` is only a contents/navigation label. |
| OCC-6C9D18FB19B3793D | gl | accepted | T17-S1 | `RING_TO_END_HOM_EXPLICIT` | Adjacent lines define the ring homomorphism `R -> End_Z(M)` and call it a representation. |
| OCC-69D0BAF2C491C257 | gl | accepted | T17-S1 | `GROUP_REPRESENTATION_THEORY_COMPOUND` | Historical prose explicitly discusses group representation theory. |
| OCC-00AB352B7A5311F3 | ca | accepted | T17-S1 | `REPRESENTATION_THEORY_COMPOUND` | Running abstract-algebra prose describes representation theory and its concrete realizations. |
| OCC-A794F6C6D498085E | ca | hold | T17-S1 | `TOC_LABEL_ONLY` | `Representació de grups` occurs only as a contents/navigation label. |

No T17 occurrence supports reciprocal representation (S2) or the historical representation-image object (S3).

### T18 — homomorphism

| Occurrence ID | Lang | Decision | v5 sense | Reason code | Review note |
|---|---|---|---|---|---|
| OCC-0186A8073BD69F7A | es | accepted | T18-S1 | `ORDERED_MONOID_HOM` | Explicit homomorphism between ordered monoids. |
| OCC-98FD9E53A9E4943C | es | accepted | T18-S1 | `MONOID_HOM_DEFINITION` | Full operation- and identity-preserving definition. |
| OCC-74AD623E3CAC4ECB | es | accepted | T18-S1 | `MODULE_HOM_DEFINITION` | Sheaf morphism required componentwise to be a module homomorphism. |
| OCC-126EB43FE523C2AE | fr | accepted | T18-S1 | `MODULE_HOM_SECTION` | A section is introduced as an L-module homomorphism in a split exact sequence. |
| OCC-8FC255BA87A54893 | fr | rejected/adverse | T18-S1 | `EXPLICIT_NONEXAMPLE_CROSSED_HOM` | The passage explicitly says a 1-cocycle is **not** a group homomorphism; “crossed homomorphism” is a distinct qualified notion. |
| OCC-0EA46714BAEC564B | fr | accepted | T18-S1 | `SURJECTIVE_MODULE_HOM` | Explicit surjective homomorphism of right modules. |
| OCC-36606C586BE519AE | pt | accepted | T18-S1 | `GROUP_HOM_IN_REP_CONTEXT` | The adjacent representation passage identifies the map into GL as a group homomorphism. |
| OCC-F4F55129362EE71D | pt | accepted | T18-S1 | `STRUCTURE_PRESERVING_MAP` | Homomorphisms are described as tools for comparing structural properties. |
| OCC-F0893D305CBB55F6 | pt | accepted | T18-S1 | `UNIVERSAL_ALGEBRA_HOM` | Running universal-algebra prose gives each algebraic class its homomorphism notion. |
| OCC-3938B1FAFD350D08 | gl | accepted | T18-S1 | `MODULE_HOM_DEFINITION` | Adjacent lines define an R-module homomorphism. |
| OCC-5ABEAED9F770C54C | ca | accepted | T18-S1 | `RING_HOM_DEFINITION` | Explicit ring-homomorphism equations, including unit preservation when rings are unital. |
| OCC-E6CE985F452E2607 | ca | accepted | T18-S1 | `GROUP_HOM_IN_REP_CONTEXT` | The adjacent group-representation passage identifies the map as a group homomorphism. |
| OCC-B2670A8388E430FA | it | accepted | T18-S1 | `RING_TO_END_HOM_EXPLICIT` | Italian prose explicitly glosses `omomorfismo` as a structure-preserving map into an endomorphism ring. |
| OCC-F002893BE948EA9A | it | accepted | T18-S1 | `FIELD_VALUED_HOM_KERNEL` | Nonzero homomorphism into a field, with kernel context. |
| OCC-00209D16575B5CE3 | it | accepted | T18-S1 | `RING_HOM_KERNEL` | Homomorphism between rings, with the kernel identified as a two-sided ideal. |

### T19 — isomorphism

| Occurrence ID | Lang | Decision | v5 sense | Reason code | Review note |
|---|---|---|---|---|---|
| OCC-8787AED925CBE819 | es | accepted | T19-S1 | `QUOTIENT_MONOID_ISOMORPHISM` | A specified natural map between quotient monoids is asserted to be an isomorphism. |
| OCC-E217FF34500D3425 | es | accepted | T19-S1 | `ALGEBRA_ISOMORPHISM_EXPLICIT` | Explicit algebra isomorphism `A -> End_A(A)`. |
| OCC-87AFBE7B36C87957 | es | accepted | T19-S1 | `BIJECTIVE_GROUP_HOM_DEFINITION` | Exact definition as a bijective group homomorphism. |
| OCC-320847F8A031BF88 | fr | accepted | T19-S1 | `QUIVER_UP_TO_ISOMORPHISM` | A quiver is characterized up to an isomorphism fixing vertices. |
| OCC-5EA8B2B9B26D2855 | fr | accepted | T19-S1 | `LIE_ALGEBRA_ISOMORPHISM` | Explicit isomorphism between S-Lie algebras. |
| OCC-47BFDBF93BB7FCB1 | fr | accepted | T19-S1 | `ISOMORPHISM_THEOREM_COMPOUND` | Algebraic running prose discusses standard isomorphism theorems and their module analogues. |
| OCC-AC96C2D81A417845 | pt | accepted | T19-S1 | `INVARIANT_UNDER_ISOMORPHISM` | Group properties are described as invariant under isomorphism. |
| OCC-46032EF8074CE367 | pt | accepted | T19-S1 | `SPECIAL_HOMOMORPHISM_GLOSS` | Isomorphisms are explicitly characterized as a special kind of homomorphism. |
| OCC-99A4BAD440782F01 | pt | accepted | T19-S1 | `HISTORICAL_TERM_USAGE` | Running history of group theory identifies the isomorphism notion. |
| OCC-E677297B9BAA3C38 | gl | accepted | T19-S1 | `INVARIANT_UNDER_ISOMORPHISM` | Group properties are described as invariant under isomorphism. |
| OCC-EFC4AC63E3F2C411 | gl | accepted | T19-S1 | `FINITE_FIELD_UP_TO_ISOMORPHISM` | Uniqueness of a finite field up to isomorphism. |
| OCC-CD5F6505DECDEF84 | gl | accepted | T19-S1 | `BIJECTIVE_MODULE_HOM_DEFINITION` | Exact definition as a bijective module homomorphism. |
| OCC-A8FEE5299CCE3A40 | ca | rejected/adverse | T19-S1 | `SOURCE_DEFECT_HOM_IMPLIES_ISO` | The sentence begins correctly but then falsely says that existence of any ring homomorphism makes the rings isomorphic; the whole quote is unsafe as supporting evidence. |
| OCC-BC9C9D8513FB1722 | ca | accepted | T19-S1 | `GROUP_ISOMORPHISM_PROBLEM` | Explicit group-isomorphism problem and example of isomorphic presentations. |
| OCC-F7A461FA2324B727 | ca | accepted | T19-S1 | `FINITE_FIELD_UP_TO_ISOMORPHISM` | Uniqueness of a finite field up to isomorphism. |
| OCC-5581743365D1DC13 | it | accepted | T19-S1 | `LINEAR_ISOMORPHISM_DEFINITION` | A linear isomorphism is explicitly defined as an invertible linear transformation. |
| OCC-81EC860D331346B3 | it | accepted | T19-S1 | `FIELD_ISO_TOPIC_WITH_BODY_CONTEXT` | The bare main-topic link is immediately followed by running prose about field isomorphisms and preserved structure. |
| OCC-5E917BB01D56606D | it | hold | T19-S1 | `NAVIGATION_LABEL_ONLY` | `Isomorfismo` appears only in a group-theory template list. |
| OCC-DC2BAE019EE5C968 | ro | accepted | T19-S1 | `EXTENSION_UP_TO_ISOMORPHISM` | Algebraic extensions are distinguished as unique up to isomorphism, not by a unique isomorphism. |
| OCC-76090F5CCE2C9E01 | ro | hold | T19-S1 | `VOCABULARY_LIST_ONLY` | `izomorfism` appears only in a list of coined mathematical terms, without a structural proposition or definition. |

### T20 — automorphism

| Occurrence ID | Lang | Decision | v5 sense | Reason code | Review note |
|---|---|---|---|---|---|
| OCC-958D9B2A333E926B | es | accepted | T20-S1 | `DOMAIN_AUTOMORPHISM_IN_SKEW_RING` | Sigma is explicitly an automorphism of the coefficient domain in a skew-polynomial-ring corollary. |
| OCC-B3C9F669A34EBA1B | es | accepted | T20-S1 | `MONOID_AUTOMORPHISM_EXPLICIT` | Automorphisms of a monoid act bijectively on its finite generating/irreducible set. |
| OCC-EC9D87555536A150 | fr | hold | no exact v5 sense | `CATEGORY_AUTOEQUIVALENCE_UNMODELED` | `S^-1 o Sigma^2` is called an automorphism acting on a derived category; this broader category-theoretic sense is not the v5 algebraic-structure sense. |
| OCC-21CA003B7FF8042B | fr | accepted | T20-S1 | `LIE_ALGEBRA_AUTOMORPHISM` | Explicit S-Lie-algebra automorphism represented by a matrix. |
| OCC-BBD5DAA638D0A0DC | fr | accepted | T20-S1 | `LIE_ALGEBRA_AUTOMORPHISM` | Each cocycle value is explicitly an S-linear automorphism of the Lie algebra. |
| OCC-8C2B54D00C9E7DDE | pt | accepted | T20-S1 | `VECTOR_SPACE_AUTOMORPHISM` | A group representation assigns an automorphism of the vector space to each group element. |
| OCC-1BBBAF23EDE00F6F | ca | accepted | T20-S1 | `VECTOR_SPACE_AUTOMORPHISM` | Same explicit group-representation construction in Catalan. |
| OCC-537655620D8C357B | it | accepted | T20-S1 | `FIELD_AUTOMORPHISM_DEFINITION` | The adjacent body states that an isomorphism whose domain and codomain coincide is an automorphism. |
| OCC-E3AD4842AA3687A3 | it | hold | T20-S1 | `NAVIGATION_LABEL_ONLY` | `Automorfismo interno` appears only in a group-theory template list. |
| OCC-D5BA86CC0588DC2F | it | hold | T20-S1 | `NAVIGATION_LABEL_ONLY` | Duplicate `Automorfismo interno` label in another template/navigation instance. |

## Integration cautions

1. These 57 accepted rows are source-context matches, not bridge-form promotions and not human evidence.
2. T17-S2 and T17-S3 remain completely unsupported by this occurrence tranche.
3. The T16 navigation labels must not be counted as reviewed S3 quotations unless a substantive Italian primary-decomposition body is acquired.
4. Preserve `OCC-8FC255BA87A54893` and `OCC-A8FEE5299CCE3A40` as adverse evidence; silently deleting them would erase useful semantic QA.
5. Do not force `OCC-EC9D87555536A150` into T20-S1. Either keep it held or add a separately defined category-automorphism/autoequivalence sense later.

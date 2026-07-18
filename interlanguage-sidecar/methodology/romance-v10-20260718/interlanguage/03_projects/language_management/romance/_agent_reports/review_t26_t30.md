# Independent semantic occurrence review: T26–T30

Date: 2026-07-17  
Scope: every T26–T30 row in the frozen v1 occurrence table, reviewed against WordWeb v6 senses  
Reviewer status: Codex internal semantic review; not human validation  
Production edits: none

## Frozen inputs

- `03_redo_ultra_20260717/wordweb/ROMANCE_TERM_OCCURRENCES_v1.csv`
  - SHA-256: `6DF8FAD570D48369CA0A8FE06CD5A0EBC3C21275677E35BEDCF077208865DEE8`
- `03_redo_ultra_20260717/wordweb/PAN_ROMANCE_WORDWEB_v6.json`
  - SHA-256: `0D4B581A2CE3F6664B1A97A44AAD023ED1FDC6C023FED5ADE42677E445751AD4`

Every stored quote was checked at its exact locator; thin hits were checked against adjacent source lines. “Accepted” means only an internally reviewed source-context match to the single modeled sense named below. It is not form promotion, human validation, or an intelligibility/pilot claim. A nearby valid phrase does not rescue an occurrence whose exact locator is a person name, bibliography string, or another sense.

## Result

| Term | Raw occurrences | Accepted | Rejected/adverse | Held |
|---|---:|---:|---:|---:|
| T26 Galois | 15 | 3 | 8 | 4 |
| T27 Noetherian | 14 | 6 | 8 | 0 |
| T28 Artinian | 10 | 1 | 8 | 1 |
| T29 finite | 18 | 15 | 1 | 2 |
| T30 unique | 16 | 12 | 3 | 1 |
| **Total** | **73** | **37** | **28** | **8** |

No term in T26–T30 has zero raw hits. Raw-hit presence is misleading, however:

- T26-S1 `galois_extension` has **zero accepted** body occurrences; both Italian extension labels are held template/navigation rows.
- T27-S1 has accepted adjective evidence only in Spanish and French. Portuguese/Catalan hits are people; Italian hits are an eponymous lemma template.
- T28-S1 has one accepted Spanish definition. The sole French adjective row is navigation-only; Portuguese, Catalan, and Italian rows are people, citations, or eponymous theorem names.
- T29 has accepted evidence for all three modeled senses: S1 finite cardinality 11, S2 finite generation 1, S3 finite degree/dimension/rank 3.
- T30-S1 has 12 accepted uses, including two explicitly qualified uniqueness claims whose “up to isomorphism” qualification must remain attached.

## Exact ID lists

### T26

Accepted:

`OCC-3A19D2A33EDDFEF3`, `OCC-DF16928988C1AAA3`, `OCC-BD1B95E04B302A6F`

Rejected/adverse:

`OCC-A9B028BB11406F55`, `OCC-41841642240535EC`, `OCC-E57E105753672989`, `OCC-5F051DE668516412`, `OCC-D3809D55C9006F7F`, `OCC-0C577AD3948F88E4`, `OCC-A5E04F51D9FEFF57`, `OCC-DA01A6C1063FA0AB`

Held:

`OCC-F39703B2A1EB5324`, `OCC-71C72B67D4F4FA67`, `OCC-288196D154FAFF31`, `OCC-9F80560BF6EABF06`

### T27

Accepted:

`OCC-4B05E84AABB9DFE1`, `OCC-2EC597EEA18CB68A`, `OCC-BC405B967CE43829`, `OCC-FF0299968A9430FC`, `OCC-8C06B9EB11A84E12`, `OCC-CCA5CDE6A03A9C30`

Rejected/adverse:

`OCC-1E9571F2B091EDB6`, `OCC-73A2C8B58C088E92`, `OCC-46F19BC8D5EB35A1`, `OCC-F235C744F70E3341`, `OCC-4B1CA861894D4261`, `OCC-BBFEA57CF0C913D3`, `OCC-86D25DC51D575FB4`, `OCC-0E71052B2884F1C9`

Held: none.

### T28

Accepted:

`OCC-1CF0679243E78BDE`

Rejected/adverse:

`OCC-2FC9B53BC3F89C5D`, `OCC-3AF8625664C123ED`, `OCC-9A9155BAB78984C5`, `OCC-D022D4434C064634`, `OCC-56759CC0E75E4507`, `OCC-DB7A7F5D18312085`, `OCC-3B604EBBF448BA2B`, `OCC-6E7017F042A1282E`

Held:

`OCC-2AD1E8E07F29F526`

### T29

Accepted:

`OCC-08538B1B5404B653`, `OCC-5714A4B96C145ABE`, `OCC-91DAFA96FC0CACB2`, `OCC-7FE81D62F411A8F4`, `OCC-743C61E0B4678C40`, `OCC-B8544C8BB4CB0EED`, `OCC-2986372BE5EE0B74`, `OCC-9637D6E5501F7E26`, `OCC-E30D8BD2D11F1EB4`, `OCC-FA39E156E77401BE`, `OCC-BDD530058D2419A5`, `OCC-C3EEA5E660B36D73`, `OCC-90FD9B572E3091E9`, `OCC-C9D392444B7909D1`, `OCC-88863A0FAD1186C7`

Rejected/adverse:

`OCC-8C857A77EA75FBFE`

Held:

`OCC-B2058005A498EC35`, `OCC-2ADAA09F9919B0B8`

### T30

Accepted:

`OCC-D06C1FDE05C87EB4`, `OCC-82F61810A32723B2`, `OCC-13BD95F97195A52B`, `OCC-0D79CF1D878A89A5`, `OCC-BECBF15B7F1A762A`, `OCC-E03B6AE921C7126E`, `OCC-A14E3064491800E2`, `OCC-531F3B2AC4188E00`, `OCC-CA0F4A63003FBCB5`, `OCC-3AF0C968CAA177E6`, `OCC-6531468290B481CA`, `OCC-5E15ECFC3C22E263`

Rejected/adverse:

`OCC-F28F17CB799CA8F0`, `OCC-08D27D44F9FEA019`, `OCC-0CF4778D8A778D34`

Held:

`OCC-120F88AE3E936109`

## Occurrence-by-occurrence decisions

### T26 — Galois

| Occurrence ID | Lang | Decision | Modeled sense | Reason code | Review note |
|---|---|---|---|---|---|
| OCC-A9B028BB11406F55 | es | rejected | T26-S2 candidate | `WRONG_LANGUAGE_CODE_COMMENT` | English `%the absolute galois group of K` in a LaTeX macro declaration; not Spanish running evidence. |
| OCC-3A19D2A33EDDFEF3 | es | accepted | T26-S2 | `GALOIS_GROUP_OF_POLYNOMIAL` | Running Spanish history explicitly names a polynomial’s Galois group. |
| OCC-41841642240535EC | es | rejected | none | `PROPER_NAME_HIT` | Exact locator is the person name `Galois`. The nearby separately tokenized `teoría de Galois` does not change this ID’s sense. |
| OCC-E57E105753672989 | fr | rejected | none | `PERSON_IN_ACKNOWLEDGMENTS` | Évariste Galois is the writer’s favorite mathematician/congress subject; no modeled mathematical sense. |
| OCC-5F051DE668516412 | fr | rejected | none | `PROPER_NAME_HIT` | Évariste Galois in historical person-name prose. |
| OCC-D3809D55C9006F7F | fr | rejected | none | `PROPER_NAME_LIST` | Évariste Galois in a list of mathematicians. |
| OCC-F39703B2A1EB5324 | pt | held | T26-S3 | `TOC_LABEL_ONLY` | Exact `Teoria de Galois`, but only a contents/navigation entry at this locator. |
| OCC-DF16928988C1AAA3 | pt | accepted | T26-S3 | `GALOIS_THEORY_RUNNING_PROSE` | Running algebra prose says Galois theory characterized polynomials solvable by radicals. |
| OCC-0C577AD3948F88E4 | pt | rejected | none | `PROPER_NAME_HIT` | Exact locator and quote are `Évariste Galois`; the passage is biographical. |
| OCC-BD1B95E04B302A6F | ca | accepted | T26-S2 | `GALOIS_GROUP_OF_POLYNOMIAL` | Running Catalan history explicitly names Galois groups of a polynomial. |
| OCC-A5E04F51D9FEFF57 | ca | rejected | T26-S3 candidate | `WRONG_LANGUAGE_BIBLIOGRAPHY` | English book title `Galois Theory and Its Algebraic Background` in a Catalan bibliography. |
| OCC-DA01A6C1063FA0AB | ca | rejected | none | `PROPER_NAME_HIT` | Exact hit is `Évariste Galois`; the next line contains a distinct theory phrase that this occurrence ID did not capture. |
| OCC-71C72B67D4F4FA67 | it | held | T26-S3 | `TOC_LABEL_ONLY` | `Teoria di Galois` appears in the page contents with subsections, not in a local definition/proposition. |
| OCC-288196D154FAFF31 | it | held | T26-S1 | `TEMPLATE_LABEL_ONLY` | `Estensione di Galois` is only a field-extension navigation/template label. |
| OCC-9F80560BF6EABF06 | it | held | T26-S1 | `DUPLICATE_TEMPLATE_LABEL` | Same `Estensione di Galois` template family reproduced in the module-theory page. |

Accepted sense counts: T26-S1 = 0, T26-S2 = 2, T26-S3 = 1.

### T27 — Noetherian

| Occurrence ID | Lang | Decision | Modeled sense | Reason code | Review note |
|---|---|---|---|---|---|
| OCC-4B05E84AABB9DFE1 | es | accepted | T27-S1 | `NOETHERIAN_RING` | Standard adjective applied to a ring in active algebraic prose. |
| OCC-2EC597EEA18CB68A | es | accepted | T27-S1 | `NOETHERIAN_M_SET_DEFINITION` | Explicit definition by finite generation of all relevant subobjects, an ACC-equivalent profile. |
| OCC-BC405B967CE43829 | es | accepted | T27-S1 | `NOETHERIAN_MODULE_ACC_DEFINITION` | Module definition explicitly gives finite generation of submodules and stabilization of ascending chains. |
| OCC-FF0299968A9430FC | fr | accepted | T27-S1 | `NOETHERIAN_RING_HILBERT_BASIS` | Noetherian ring/algebra statement with Hilbert-basis proof context. |
| OCC-8C06B9EB11A84E12 | fr | accepted | T27-S1 | `NOETHERIAN_RING` | Standard adjective applied to a coherent strongly discrete ring. |
| OCC-CCA5CDE6A03A9C30 | fr | accepted | T27-S1 | `NOETHERIAN_BASE_RING` | The noetherian condition on A supports finite-presentation consequences for modules. |
| OCC-1E9571F2B091EDB6 | pt | rejected | none | `EMMY_NOETHER_PERSON` | Proper name in a list of mathematicians, not a Noetherian adjective. |
| OCC-73A2C8B58C088E92 | pt | rejected | none | `EMMY_NOETHER_PERSON` | Biographical proper-name occurrence. |
| OCC-46F19BC8D5EB35A1 | ca | rejected/adverse | none | `M_NOETHER_DIFFERENT_PERSON` | Historical `M. Noether` refers to Max Noether and cannot attest the Noetherian adjective. |
| OCC-F235C744F70E3341 | ca | rejected | none | `EMMY_NOETHER_PERSON` | Section heading and prose about Emmy Noether. |
| OCC-4B1CA861894D4261 | ca | rejected | none | `EMMY_NOETHER_PERSON` | Proper name in a mathematician list. |
| OCC-BBFEA57CF0C913D3 | it | rejected | none | `EPONYMOUS_LEMMA_TEMPLATE` | `Lemma di normalizzazione di Noether` is an eponymous theorem label, not `noetheriano`. |
| OCC-86D25DC51D575FB4 | it | rejected | none | `DUPLICATE_EPONYM_TEMPLATE` | Same Noether-normalization template in a second page. |
| OCC-0E71052B2884F1C9 | it | rejected | none | `DUPLICATE_EPONYM_TEMPLATE` | Same Noether-normalization template in a third page. |

### T28 — Artinian

| Occurrence ID | Lang | Decision | Modeled sense | Reason code | Review note |
|---|---|---|---|---|---|
| OCC-1CF0679243E78BDE | es | accepted | T28-S1 | `ARTINIAN_MODULE_DCC_DEFINITION` | Explicit definition by stabilization of descending submodule chains. |
| OCC-2AD1E8E07F29F526 | fr | held | T28-S1 | `NAVIGATION_LABEL_ONLY` | Correct adjective in `Anneau artinien`, but only in a ring-class navigation list. |
| OCC-2FC9B53BC3F89C5D | pt | rejected | none | `EMIL_ARTIN_PERSON` | Proper name in mathematical history. |
| OCC-3AF8625664C123ED | pt | rejected | none | `EMIL_ARTIN_PERSON` | Biographical person-name occurrence. |
| OCC-9A9155BAB78984C5 | ca | rejected | none | `EPONYMOUS_THEOREM` | Artin–Wedderburn theorem name, not the Artinian adjective. |
| OCC-D022D4434C064634 | ca | rejected | none | `AUTHOR_CITATION` | `Artin` is an author/citation name. |
| OCC-56759CC0E75E4507 | ca | rejected | none | `EMIL_ARTIN_PERSON` | Proper name in a mathematician list. |
| OCC-DB7A7F5D18312085 | it | rejected | none | `EMIL_ARTIN_PERSON` | Biographical statement about Artin’s work on Galois theory. |
| OCC-3B604EBBF448BA2B | it | rejected | none | `MICHAEL_ARTIN_BIBLIOGRAPHY` | Author name in a bibliography. |
| OCC-6E7017F042A1282E | it | rejected | none | `EPONYMOUS_THEOREM_TEMPLATE` | Artin–Wedderburn navigation label, not `artiniano`. |

### T29 — finite

| Occurrence ID | Lang | Decision | Modeled sense | Reason code | Review note |
|---|---|---|---|---|---|
| OCC-08538B1B5404B653 | es | accepted | T29-S3 | `FINITE_DIMENSION_FILTRATION` | Multi-filtrations are explicitly finite-dimensional. |
| OCC-5714A4B96C145ABE | es | accepted | T29-S1 | `FINITE_SUPPORT_CARDINALITY` | Functions vanish outside a finite set/finite number of indices. |
| OCC-91DAFA96FC0CACB2 | es | accepted | T29-S3 | `FINITE_DIMENSION_REPRESENTATION` | Finite- versus infinite-dimensional representations. |
| OCC-7FE81D62F411A8F4 | fr | accepted | T29-S1 | `FINITE_SET_CARDINALITY` | The set of cluster variables may be finite or infinite. |
| OCC-743C61E0B4678C40 | fr | accepted | T29-S3 | `FINITE_DIMENSION_MODULE` | The exact hit is in `modules de dimension finie`; other finite compounds in the same long line are not folded into this ID. |
| OCC-B8544C8BB4CB0EED | fr | accepted | T29-S1 | `FINITE_GROUP_CARDINALITY` | The exact first hit is a finite group acting by automorphisms. |
| OCC-2986372BE5EE0B74 | pt | accepted | T29-S1 | `FINITE_GROUP_BODY_CONTEXT` | Main-article label is followed immediately by substantive finite-group theory prose. |
| OCC-9637D6E5501F7E26 | pt | accepted | T29-S1 | `FINITE_FIELD_CARDINALITY` | Running abstract-algebra prose names finite fields. |
| OCC-8C857A77EA75FBFE | pt | rejected/adverse | T29-S1 | `EXPLICIT_NEGATED_NONINSTANCE` | The passage says a group need not be finite; preserve as negative/adverse evidence, not supporting instance evidence. |
| OCC-B2058005A498EC35 | gl | held | T29-S1 | `FINITE_GEOMETRY_NAV_LABEL` | Bare `finita` occurs only as the modifier in a mathematics-navigation entry for finite geometry. |
| OCC-E30D8BD2D11F1EB4 | ca | accepted | T29-S1 | `FINITE_GROUP_CARDINALITY` | Running history repeatedly applies `finit` to groups. |
| OCC-FA39E156E77401BE | ca | accepted | T29-S1 | `FINITE_GROUP_DEFINITION` | A group is explicitly called finite iff its underlying set is finite. |
| OCC-BDD530058D2419A5 | ca | accepted | T29-S1 | `FINITE_NUMBER_OF_CASES` | Proof by exhaustion over a finite set/number of cases. |
| OCC-C3EEA5E660B36D73 | it | accepted | T29-S1 | `FINITE_AXIOM_SET` | An algebraic structure is described with a finite set of identities/axioms. |
| OCC-90FD9B572E3091E9 | it | accepted | T29-S1 | `FINITE_INTEGRAL_DOMAIN` | A finite integral domain is asserted to be a field. |
| OCC-C9D392444B7909D1 | it | accepted | T29-S2 | `FINITE_GENERATING_SET_DEFINITION` | A ring extension is explicitly finitely generated when its generating set is finite. |
| OCC-2ADAA09F9919B0B8 | ro | held | T29-S1 | `TOC_LABEL_ONLY` | `Teoria grupurilor finite` occurs only in the contents block at this locator. |
| OCC-88863A0FAD1186C7 | ro | accepted | T29-S1 | `FINITE_FIELD_CARDINALITY` | A finite field K is used in a substantive proof that no finite field is algebraically closed. |

Accepted sense counts: T29-S1 = 11, T29-S2 = 1, T29-S3 = 3.

### T30 — unique

| Occurrence ID | Lang | Decision | Modeled sense | Reason code | Review note |
|---|---|---|---|---|---|
| OCC-D06C1FDE05C87EB4 | es | accepted | T30-S1 | `UNIQUE_IDENTITY_ELEMENT` | Exact uniqueness claim for a monoid identity element. |
| OCC-82F61810A32723B2 | es | accepted | T30-S1 | `UNIQUE_MORPHISM_UNIVERSAL_PROPERTY` | Explicit existence of a unique morphism in an adjunction/sheafification universal property. |
| OCC-13BD95F97195A52B | es | accepted | T30-S1 | `UNIQUE_PRIME_IDEAL_FACTORIZATION` | Each nonzero ideal is a unique product of prime ideals; commutative ideal-product factorization context is explicit. |
| OCC-0D79CF1D878A89A5 | fr | accepted | T30-S1 | `UNIQUE_CLUSTER_GRAPH` | The underlying graph is asserted unique; the following clause also gives one unique variable for a stated root. |
| OCC-F28F17CB799CA8F0 | fr | rejected | none | `NONMATHEMATICAL_PERSONAL_WORDPLAY` | Acknowledgments/personal joke (`mon existante et unique projection`), not algebraic uniqueness evidence. |
| OCC-BECBF15B7F1A762A | fr | accepted | T30-S1 | `QUALIFIED_UNIQUE_UP_TO_ISOMORPHISM` | Decomposition is explicitly unique **up to isomorphisms**. Accept only with that qualifier preserved. |
| OCC-08D27D44F9FEA019 | pt | rejected | none | `SINGLE_PARTICULAR_OBJECT` | `um único grupo ... G` means one/single chosen p-adic analytic group, not a theorem that exactly one exists. |
| OCC-E03B6AE921C7126E | pt | accepted | T30-S1 | `UNIQUE_LINEAR_SYSTEM_SOLUTION` | The point is the unique solution satisfying both equations. |
| OCC-0CF4778D8A778D34 | pt | rejected | none | `UNIFIED_ARGUMENT_WRONG_SENSE` | `num único argumento` means one combined/unified argument, not uniqueness under an equality relation. |
| OCC-120F88AE3E936109 | ca | held | T30-S1 | `UNIQUENESS_QUALIFIER_OMITTED` | Wedderburn-style algebra decomposition is said simply to be unique, but the relevant isomorphism/permutation equivalence is not stated locally. Do not normalize away this gap. |
| OCC-A14E3064491800E2 | ca | accepted | T30-S1 | `ONLY_NONINVERTIBLE_ELEMENT` | Zero is asserted to be the unique noninvertible ring element. |
| OCC-531F3B2AC4188E00 | ca | accepted | T30-S1 | `QUALIFIED_UNIQUE_UP_TO_ISOMORPHISM` | A finite field is unique **up to isomorphism**; qualifier is explicit and must remain attached. |
| OCC-CA0F4A63003FBCB5 | it | accepted | T30-S1 | `EXISTS_UNIQUE_QUANTIFIER` | Direct gloss of the logical quantifier `exists!`. |
| OCC-3AF0C968CAA177E6 | it | accepted | T30-S1 | `UNIQUE_MINIMUM_MAXIMUM` | Minimum or maximum, when it exists, is unique. |
| OCC-6531468290B481CA | it | accepted | T30-S1 | `UNIQUE_CONTAINING_IDEAL` | The only ideal containing the given ideal is itself, in the maximal-ideal criterion. |
| OCC-5E15ECFC3C22E263 | ro | accepted | T30-S1 | `UNIQUE_PRIME_FACTORIZATION` | Every integer is stated to decompose uniquely into prime factors. |

## Duplicate/template families and integration cautions

1. `OCC-288196D154FAFF31` and `OCC-9F80560BF6EABF06` are the same Italian Galois-extension navigation family; neither is a body quotation.
2. `OCC-BBFEA57CF0C913D3`, `OCC-86D25DC51D575FB4`, and `OCC-0E71052B2884F1C9` are the same Italian Noether-normalization template family. They are three representations, not three Noetherian-adjective attestations.
3. Proper-name matches must not be folded into adjective/theory counts. In particular, `M. Noether` is Max Noether, and bare Artin/Galois names do not establish the modeled senses.
4. Preserve `OCC-8C857A77EA75FBFE` as explicit negative/adverse evidence.
5. Preserve the full qualifiers on `OCC-BECBF15B7F1A762A` and `OCC-531F3B2AC4188E00`; neither supports unqualified equality-uniqueness.
6. Keep `OCC-120F88AE3E936109` held until its actual equivalence relation is sourced. Do not infer a promotion from the unqualified wording.
7. None of the 37 accepted rows authorizes a bridge-form promotion, cohort score change, human-observation count, or pilot claim.

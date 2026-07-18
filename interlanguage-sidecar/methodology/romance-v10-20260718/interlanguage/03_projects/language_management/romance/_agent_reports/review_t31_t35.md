# Independent semantic occurrence review: T31–T35

Date: 2026-07-17  
Scope: every T31–T35 row in the frozen v1 occurrence table, reviewed against WordWeb v7 senses  
Reviewer status: Codex internal semantic review; not human attestation or validation  
Production edits: none

## Frozen inputs

| Artifact | SHA-256 |
|---|---|
| 03_redo_ultra_20260717/wordweb/ROMANCE_TERM_OCCURRENCES_v1.csv | 6DF8FAD570D48369CA0A8FE06CD5A0EBC3C21275677E35BEDCF077208865DEE8 |
| 03_redo_ultra_20260717/wordweb/PAN_ROMANCE_WORDWEB_v7.json | A48BF8C89F252A0274D2FDE2FE8A2E6E6E3077AD81A4B60BFA0B5FFF44A1A366 |

Every stored quote was checked at its exact locator, and adjacent source lines were inspected for all thin or potentially ambiguous hits. Accepted means only an internally reviewed source-context match to the one explicit v7 sense named below. It does not promote a form, establish an independent quotation family, supply human evidence, or support an intelligibility claim.

## Exact result

| Term | Raw occurrences | Accepted | Rejected/adverse | Held |
|---|---:|---:|---:|---:|
| T31 reduced | 5 | 1 | 4 | 0 |
| T32 associated prime | 3 | 3 | 0 | 0 |
| T33 complement | 4 | 2 | 2 | 0 |
| T34 unit ideal | 0 | 0 | 0 | 0 |
| T35 congruence | 1 | 1 | 0 | 0 |
| **Total** | **13** | **7** | **6** | **0** |

Every one of the 13 extracted occurrence IDs is classified exactly once. There are no held rows.

Sense-level outcome:

- T31-S1 reduced_ring: one accepted French navigation label and one Spanish adverse definition; T31-S2 reduced_norm and T31-S3 reduced_degree have zero occurrence support.
- T32-S1 associated_prime: three accepted Italian navigation occurrences, all belonging to one repeated template family.
- T33-S2 set_complement: two accepted running-text occurrences; T33-S1 direct_complement and T33-S3 orthogonal_complement have zero accepted support.
- T34-S1 unit_ideal: explicit zero-hit gap.
- T35-S2 algebraic_congruence_relation: one accepted definition; T35-S1 modular_congruence and T35-S3 geometric_congruence have zero occurrence support.

## Exact ID lists

### T31

Accepted:

OCC-E1E3164538F997B7 → T31-S1 reduced_ring.

Rejected/adverse:

OCC-C19FB1EB927EFB35, OCC-27EA2D245FC98E5A, OCC-B0A4B253AF8E3FBD, OCC-6C6FE57D6F455878.

Held: none.

### T32

Accepted:

OCC-025AEC5228CF20A3 → T32-S1 associated_prime.  
OCC-4E98383B66B7E594 → T32-S1 associated_prime.  
OCC-38A244D91A019BB8 → T32-S1 associated_prime.

Rejected/adverse: none. Held: none.

### T33

Accepted:

OCC-B1A727E2131F8229 → T33-S2 set_complement.  
OCC-CAF8B9176750BBC1 → T33-S2 set_complement.

Rejected/adverse:

OCC-945F069751ED6784, OCC-3B2790D9171F7137.

Held: none.

### T34

No extracted occurrence IDs. T34-S1 unit_ideal remains a zero-body-occurrence gap. The inherited ES/FR core seed records are quotation-free and do not cure this gap.

### T35

Accepted:

OCC-1351B5D65CB3CD74 → T35-S2 algebraic_congruence_relation.

Rejected/adverse: none. Held: none.

## Occurrence-by-occurrence decisions

### T31 — reduced

| Occurrence ID | Classification | Sense/adverse target | Evidence-based reason |
|---|---|---|---|
| OCC-C19FB1EB927EFB35 | rejected_adverse | adverse target T31-S1 reduced_ring | The Spanish source explicitly labels anillo reducido but defines it as having no nonzero idempotents. The v7 sense and standard definition require no nonzero nilpotents. In a nonzero unital ring, 1 itself is a nonzero idempotent, making the printed definition especially unusable. Preserve this as a source-definition error, not support. |
| OCC-27EA2D245FC98E5A | rejected_adverse | adverse target T31 surface candidate réduit; no modeled sense | French verbal usage: a theorem “reduces” the problem of comparing extension blocks. This is ordinary reduction of a problem, not a reduced ring, reduced norm, or reduced degree. |
| OCC-B0A4B253AF8E3FBD | rejected_adverse | adverse target T31 surface candidate réduit; no modeled sense | French phrase réduit au minimum means “reduced/minimized the appeal to logical notions.” It is ordinary verbal usage. |
| OCC-E1E3164538F997B7 | accepted | T31-S1 reduced_ring | French Anneau réduit occurs in an algebra navigation list among named ring classes and prime/primary ideals. It is a correct lexical ring-class label, but only navigation/template evidence, not defining prose. |
| OCC-6C6FE57D6F455878 | rejected_adverse | adverse target T31 surface candidate reduzida; no modeled sense | Portuguese generalidade é reduzida says that generality is reduced when structure is added. It is an ordinary predicative adjective, not any modeled algebraic sense. |

No occurrence supports T31-S2 or T31-S3. The erroneous Spanish definition must remain attached as adverse evidence whenever anillo reducido is considered for T31-S1.

### T32 — associated prime

| Occurrence ID | Classification | Sense | Evidence-based reason |
|---|---|---|---|
| OCC-025AEC5228CF20A3 | accepted | T32-S1 associated_prime | Italian Primo associato appears in a commutative-algebra navigation sequence beside Gorenstein ring, Gröbner basis, and tensor product. |
| OCC-4E98383B66B7E594 | accepted | T32-S1 associated_prime | Same disambiguating Italian navigation label on a second page. |
| OCC-38A244D91A019BB8 | accepted | T32-S1 associated_prime | Same disambiguating Italian navigation label on a third page. |

These three IDs reproduce the same navigation-template sequence. They are three mechanical locations but one lexical evidence family, with zero independent running-prose definitions. They must be folded rather than summed for promotion or coverage breadth.

### T33 — complement

| Occurrence ID | Classification | Sense/adverse target | Evidence-based reason |
|---|---|---|---|
| OCC-B1A727E2131F8229 | accepted | T33-S2 set_complement | Spanish text explicitly states that the complement of a monoid face is a prime ideal and displays M minus the relevant subset. |
| OCC-CAF8B9176750BBC1 | accepted | T33-S2 set_complement | French proof treats S as the complement paired with a prime ideal P and uses an element outside P union S. This is the ambient-set complement sense. |
| OCC-945F069751ED6784 | rejected_wrong_sense | adverse target T33 surface candidate complemento; unmodeled matrix cofactor | Italian complemento algebrico is the signed minor/cofactor of a matrix entry. It is neither direct, set, nor orthogonal complement. |
| OCC-3B2790D9171F7137 | rejected_wrong_sense | adverse target T33-S1 overextension; unmodeled group complement | Bare navigation title Complemento (teoria dei gruppi) refers to the group-theoretic complement/semidirect-product concept. V7 T33-S1 explicitly requires a subobject completing another to a direct sum; the navigation title does not establish that narrower sense. |

No occurrence supports T33-S1 or T33-S3.

### T34 — unit ideal

The extraction has zero T34 rows. T34-S1 therefore remains an explicit occurrence-level gap. No negative claim follows from absence, but no bridge or source-quotation status may be inferred from the inherited quotation-free core records.

### T35 — congruence

| Occurrence ID | Classification | Sense | Evidence-based reason |
|---|---|---|---|
| OCC-1351B5D65CB3CD74 | accepted | T35-S2 algebraic_congruence_relation | Spanish definition says that an equivalence relation on a monoid which is also a submonoid of P×P is a congruence relation, and the following lines construct the quotient monoid. This exactly supplies operation compatibility. |

This row is not evidence for T35-S1 modular congruence or T35-S3 geometric congruence.

## Machine-side aggregate lists

Accepted (7):

OCC-E1E3164538F997B7, OCC-025AEC5228CF20A3, OCC-4E98383B66B7E594, OCC-38A244D91A019BB8, OCC-B1A727E2131F8229, OCC-CAF8B9176750BBC1, OCC-1351B5D65CB3CD74.

Rejected/adverse (6):

OCC-C19FB1EB927EFB35, OCC-27EA2D245FC98E5A, OCC-B0A4B253AF8E3FBD, OCC-6C6FE57D6F455878, OCC-945F069751ED6784, OCC-3B2790D9171F7137.

Held (0): none.

Zero-hit term: T34. Zero-hit modeled senses within otherwise nonempty terms: T31-S2, T31-S3, T33-S1, T33-S3, T35-S1, and T35-S3.

## Integration constraints

1. Keep all accepted rows at internal semantic-review status; none is a promoted form or human attestation.
2. Fold the three T32 Italian rows into one repeated navigation-template evidence family.
3. Preserve OCC-C19FB1EB927EFB35 as adverse evidence against the erroneous idempotent-based definition of reduced ring.
4. Do not map matrix cofactor or group complement into the modeled T33 senses.
5. Do not convert T34 absence or quotation-free inherited ES/FR seed records into positive evidence.

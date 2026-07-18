# Occurrence context review protocol v1

The input is `ROMANCE_TERM_OCCURRENCES_v1.csv`, whose rows are mechanical
context candidates. Review v1 now covers every surviving occurrence
contiguously through T01–T40 after the Romansh false-result quarantine and
corpus topic review. The preserved earlier tranches contain 117 rows for
T01–T10, 111 rows for T11–T20, and 131 rows for T21–T30: 359 numbered-term
occurrence rows. The T31–T40 tranche adds exactly 83 rows—63 accepted sense
matches, 8 rejected/wrong or adverse rows, and 12 held rows—for 442 contiguous
numbered-term occurrence rows. The separate 2021 Rumantsch Grischun review
contributes two source occurrences and three sense judgments for T45/T57,
yielding 444 distinct reviewed occurrences without altering the contiguous
cursor. Every reviewed window was inspected for mathematical sense, source
language, ambient structure, and whether a bare line needed adjacent source
lines.

The occurrence table remains frozen at SHA-256
`6DF8FAD570D48369CA0A8FE06CD5A0EBC3C21275677E35BEDCF077208865DEE8`.
It predates and does not cover the newly acquired official 2024 Rumantsch
Grischun sources `CURATED-RM-RG-GRCH-AP1G-2024-M1` and
`CURATED-RM-RG-GRCH-AP1G-2024-M2`; those require a later extraction and
semantic-review tranche.

An accepted row proves only that the cited source context uses the surface in
the target mathematical sense. It does not by itself establish a canonical
lemma, a bridge-form decision, cross-branch comprehensibility, or human
marginal intelligibility. Accepted navigation labels are lexical evidence,
not body attestation; repeated template locations remain one evidence family.
All accepted rows therefore remain
`bridge_form_promotion_eligible=false`.

Rejected rows are retained as adverse evidence. The review distinguishes ordinary homographs, field-of-study uses, modulo arithmetic/equivalence, wrong-language bibliography strings, monoid ideals versus the target ring-ideal senses, irreducible polynomials/elements versus irreducible ideals, and coprime integers versus coprime ideals. Folded spellings share a normalization group and are never summed as independent witnesses.

Held rows are neither supporting nor adverse until their ambiguity is
resolved. Duplicate/template, code-comment, table-of-contents,
subgroup-substring, and semantic-ambiguity holds remain typed rather than being
counted as body support. Explicit zero-hit or zero-accepted-sense gaps stay
visible rather than being filled by a dominant standard or by a
template/navigation label. Current zero-hit terms include T11 and T34. Earlier
zero-accepted gaps T22-S2, T25-S2, and T26-S1 remain; the T31–T40 gaps are
T31-S2, T31-S3, T33-S1, T33-S3, T34-S1, T35-S1, T35-S3, and T37-S2. Narrow
accepted-language coverage for T27-S1 and T28-S1 is recorded without
extrapolation.

This is internal model-assisted semantic curation, explicitly not human
validation. Human-observation count, form-promotion count, and pilot-claim
count are all zero. Review coverage advances in numbered contiguous tranches;
the next contiguous cursor is T41.

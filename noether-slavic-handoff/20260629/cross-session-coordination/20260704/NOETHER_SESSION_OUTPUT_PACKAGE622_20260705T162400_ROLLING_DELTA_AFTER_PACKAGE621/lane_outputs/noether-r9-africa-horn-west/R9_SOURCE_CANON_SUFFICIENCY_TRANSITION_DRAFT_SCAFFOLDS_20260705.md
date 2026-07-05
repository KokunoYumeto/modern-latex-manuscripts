# R9 Source-Canon Sufficiency Transition Draft Scaffolds - 2026-07-05

Created UTC: `2026-07-05T14:23:35+00:00`

This artifact applies the B3 source-canon sufficiency transition rule to the R9 Africa/Horn/West Africa lane. Source canon remains first. Rows with enough baseline source support receive scoped draft or reviewer-facing scaffolds; uncovered rows stay in source acquisition, OCR/Unicode repair, licensing/access, or reviewer-return status.

Boundary: every row is `DRAFT_NON_CANONICAL_NOT_NATIVE_REVIEWED_NOT_ACCEPTED`, `promotion_allowed=false`, `source_text_saved=false`, `translation_completion_claimed=false`, and no native/community review, accepted term, license clearance, gate promotion, package upload, commit, or Git push is claimed.

## Counts

- CSV rows: `49`
- Source-backed school-math draft scaffold rows: `18`
- Reviewer-facing candidate scaffold rows, not translations: `16`
- Gap/source-context/blocker rows: `15`

Status counts:
- `context_provenance_only_no_translation`: `1`
- `draft_scaffold_source_backed_for_school_math_scope`: `18`
- `hard_noether_terms_blocked_uncovered`: `1`
- `reviewer_facing_candidate_scaffold_not_translation`: `16`
- `reviewer_prompt_source_gap_no_target_rendering`: `1`
- `source_acquisition_gap_no_translation`: `3`
- `source_archive_and_public_register_candidate_not_translation_ready`: `1`
- `source_body_baseline_present_target_rendering_blocked`: `1`
- `source_gap_do_not_use_no_translation`: `7`

## Transition Decisions

- Somali, Oromo, and Tigrigna/Tigrinya have source-backed school-math/formula-neighboring rows from the prior R9 support CSV plus local source-body/access ledgers. Those rows now receive narrow draft scaffolds only for arithmetic, fraction, set, and elementary algebra context.
- Fulfulde/Fulani, Mandinka/Manding, Akan/Twi, Wolof, and Yoruba glossary/dictionary rows receive reviewer-facing candidate scaffolds only where a candidate string already existed. They are not promoted to translations because variety, register, source prose, license/access, and reviewer gates remain open.
- Amharic has source-body and current-access baseline support, but target renderings are not responsibly extracted here because OCR/font-map repair remains open.
- Hausa has a captured GitHub source-archive candidate and a captured IA public-register PDF body, but neither is admitted as translation support. They remain source-package/public-register review candidates.
- Igbo, Afar/Qafar, AF05, and AF06 remain source-acquisition or transcript/body gaps.
- Hard Noether anchors across all R9 languages remain blocked: ring, field, module, ideal, invariant, Noetherian ring, theorem/proof prose, and invariant-theory register require higher-math source witnesses or reviewer returns.

## Covered Draft Scaffold Rows

| ID | Language | Anchor | Draft target | Formula-neighboring note |
|---|---|---|---|---|
| `R9-TRANS-20260705-001` | Somali | mathematics / Mathematik | xisaab | Use only as a topic/subject label around formula-bearing school-math prose; no Noether prose frame inferred. |
| `R9-TRANS-20260705-002` | Somali | addition / Addition | isugeynta | Formula neighbor: a + b = c. Draft only for operation labels/sentences already near source math examples. |
| `R9-TRANS-20260705-003` | Somali | subtraction / Subtraktion | kalagoynta | Formula neighbor: a - b = c. Draft only after reviewer confirms noun/verb sentence behavior. |
| `R9-TRANS-20260705-004` | Somali | multiplication / Multiplikation | iskudhufashada | Formula neighbor: a * b = c or a x b = c. Confirm spacing and local symbol prose before use. |
| `R9-TRANS-20260705-005` | Somali | division / Division | isuqaybinta | Formula neighbor: a / b or a ÷ b. Confirm equation prose and fraction/division distinction. |
| `R9-TRANS-20260705-006` | Somali | fraction / Bruch | jajab | Formula neighbor: a/b or numerator-over-denominator examples. Confirm singular/plural and algebraic fraction transfer. |
| `R9-TRANS-20260705-007` | Somali | variable / Variable | doorsoomeyaasha | Formula neighbor: x, y, or x + 1 = 3. Confirm singular/plural and equation-prose behavior. |
| `R9-TRANS-20260705-009` | Oromo | mathematics / Mathematik | herrega; barnoota herregaa | Use only as a topic/subject label around formula-bearing school-math prose; no Noether prose frame inferred. |
| `R9-TRANS-20260705-010` | Oromo | addition / Addition | ida'uu | Formula neighbor: a + b = c. Draft only for operation labels/sentences already near source math examples. |
| `R9-TRANS-20260705-011` | Oromo | subtraction / Subtraktion | hir'isuu | Formula neighbor: a - b = c. Draft only after reviewer confirms noun/verb sentence behavior. |
| `R9-TRANS-20260705-012` | Oromo | multiplication / Multiplikation | baay'isuu | Formula neighbor: a * b = c or a x b = c. Confirm spacing and local symbol prose before use. |
| `R9-TRANS-20260705-013` | Oromo | fraction / Bruch | firaakshinoota | Formula neighbor: a/b or numerator-over-denominator examples. Confirm singular/plural and algebraic fraction transfer. |
| `R9-TRANS-20260705-014` | Oromo | variable / Variable | jijjiiramaa; jijjiiramoota | Formula neighbor: x, y, or x + 1 = 3. Confirm singular/plural and equation-prose behavior. |
| `R9-TRANS-20260705-016` | Tigrigna_Tigrinya | mathematics / Mathematik | ሒሳብ | Use only as a topic/subject label around formula-bearing school-math prose; no Noether prose frame inferred. |
| `R9-TRANS-20260705-017` | Tigrigna_Tigrinya | addition / Addition | ምድማር | Formula neighbor: a + b = c. Draft only for operation labels/sentences already near source math examples. |
| `R9-TRANS-20260705-018` | Tigrigna_Tigrinya | subtraction / Subtraktion | ምጉዳል | Formula neighbor: a - b = c. Draft only after reviewer confirms noun/verb sentence behavior. |
| `R9-TRANS-20260705-019` | Tigrigna_Tigrinya | fraction / Bruch | ጉዚ; ጉዚታት | Formula neighbor: a/b or numerator-over-denominator examples. Confirm singular/plural and algebraic fraction transfer. |
| `R9-TRANS-20260705-020` | Tigrigna_Tigrinya | set / Menge | እኩብ; እኩባት | Formula neighbor: set A, membership, or braces {a,b}; later algebra transfer requires reviewer/source confirmation. |

## Reviewer-Facing Candidate Rows

These rows expose source-attested candidate strings or glossary variants for reviewer comparison only. They are not accepted renderings and should not be used as translation evidence without source-owner/reviewer closure.

| ID | Language | Anchor | Candidate status | Next return |
|---|---|---|---|---|
| `R9-TRANS-20260705-015` | Oromo | theorem marker / Satz- / Lehrsatz-Marker | FOR_REVIEW_ONLY_NOT_TRANSLATION: tiyooramii; tiyooramoota | Confirm whether marker supports theorem headings and whether proof prose needs a different frame. |
| `R9-TRANS-20260705-021` | Tigrigna_Tigrinya | definition / Definition | FOR_REVIEW_ONLY_NOT_TRANSLATION: ትርጉም | Confirm whether chemistry definition marker transfers to math definitions. |
| `R9-TRANS-20260705-023` | Fulfulde_Fulani | algebra / Algebra | FOR_REVIEW_ONLY_NOT_TRANSLATION: aljabar; Aljabar | Identify variety label and decide whether loan form is acceptable in the target community. |
| `R9-TRANS-20260705-024` | Fulfulde_Fulani | equation / Gleichung | FOR_REVIEW_ONLY_NOT_TRANSLATION: fotuki; ko andaaka; nannduɗum; fottida | Choose among competing variants; do not flatten Fulfulde/Fulani/Fula/Pulaar rows. |
| `R9-TRANS-20260705-025` | Fulfulde_Fulani | variable / Variable | FOR_REVIEW_ONLY_NOT_TRANSLATION: fergere; baylatoongel; mamre | Review variety, register, and higher-math suitability. |
| `R9-TRANS-20260705-027` | Mandinka_Manding | algebra / Algebra | FOR_REVIEW_ONLY_NOT_TRANSLATION: algébro | Confirm Mandinka-specific form; do not widen to Manding without review. |
| `R9-TRANS-20260705-028` | Mandinka_Manding | equation / Gleichung | FOR_REVIEW_ONLY_NOT_TRANSLATION: équatiyon | Check loan form and prose use before draft translation. |
| `R9-TRANS-20260705-029` | Mandinka_Manding | theorem / Satz / Lehrsatz | FOR_REVIEW_ONLY_NOT_TRANSLATION: théorémo | Confirm theorem/proof/definition heading strategy before any Noether prose. |
| `R9-TRANS-20260705-031` | Akan_Twi | algebra / Algebra | FOR_REVIEW_ONLY_NOT_TRANSLATION: akontaabu a wɔde agyiraehyɛde di dwuma; nkonta a wɔde agyiraehyɛde di dwuma | Confirm compact register and whether phrase is usable beyond glossary context. |
| `R9-TRANS-20260705-032` | Akan_Twi | equation / Gleichung | FOR_REVIEW_ONLY_NOT_TRANSLATION: nsɛm abien a pɛyɛ gyiraehyɛde da ntam; afa abien akontaabu nsɛm a ɛyɛ pɛ | Review source split and mathematical sentence behavior. |
| `R9-TRANS-20260705-033` | Akan_Twi | proof / Beweis | FOR_REVIEW_ONLY_NOT_TRANSLATION: adanse | Confirm whether this supports formal proof prose. |
| `R9-TRANS-20260705-035` | Wolof | algebra / Algebra | FOR_REVIEW_ONLY_NOT_TRANSLATION: alseebar; alseebur; Joxe ndigël | Choose among variants and check subject-specific register. |
| `R9-TRANS-20260705-036` | Wolof | equation / Gleichung | FOR_REVIEW_ONLY_NOT_TRANSLATION: tolloole; Ikuwaason; ikuwaason | Review orthography/register variants before draft prose. |
| `R9-TRANS-20260705-037` | Wolof | proof / Beweis | FOR_REVIEW_ONLY_NOT_TRANSLATION: Ki sampp; Përëw | Confirm formal proof frame and avoid translating Noether prose before review. |
| `R9-TRANS-20260705-039` | Yoruba | algebra / Algebra | FOR_REVIEW_ONLY_NOT_TRANSLATION: Ìṣirò Àlámìn | Confirm dictionary form against school/STEM prose source. |
| `R9-TRANS-20260705-040` | Yoruba | equation / Gleichung | FOR_REVIEW_ONLY_NOT_TRANSLATION: ọmì | Check extraction damage and whether this is correct for equation. |

## Gap and Source-Context Rows

| ID | Language | Status | Blocker / next return |
|---|---|---|---|
| `R9-TRANS-20260705-008` | Somali | `reviewer_prompt_source_gap_no_target_rendering` | Reviewer/source-owner/license/OCR gates remain open; hard Noether prose remains blocked unless the row is explicitly source-backed for school-math scope. |
| `R9-TRANS-20260705-022` | Tigrigna_Tigrinya | `source_gap_do_not_use_no_translation` | Reviewer/source-owner/license/OCR gates remain open; hard Noether prose remains blocked unless the row is explicitly source-backed for school-math scope. |
| `R9-TRANS-20260705-026` | Fulfulde_Fulani | `source_gap_do_not_use_no_translation` | Reviewer/source-owner/license/OCR gates remain open; hard Noether prose remains blocked unless the row is explicitly source-backed for school-math scope. |
| `R9-TRANS-20260705-030` | Mandinka_Manding | `source_gap_do_not_use_no_translation` | Reviewer/source-owner/license/OCR gates remain open; hard Noether prose remains blocked unless the row is explicitly source-backed for school-math scope. |
| `R9-TRANS-20260705-034` | Akan_Twi | `source_gap_do_not_use_no_translation` | Reviewer/source-owner/license/OCR gates remain open; hard Noether prose remains blocked unless the row is explicitly source-backed for school-math scope. |
| `R9-TRANS-20260705-038` | Wolof | `source_gap_do_not_use_no_translation` | Reviewer/source-owner/license/OCR gates remain open; hard Noether prose remains blocked unless the row is explicitly source-backed for school-math scope. |
| `R9-TRANS-20260705-041` | Yoruba | `source_gap_do_not_use_no_translation` | Reviewer/source-owner/license/OCR gates remain open; hard Noether prose remains blocked unless the row is explicitly source-backed for school-math scope. |
| `R9-TRANS-20260705-042` | Yoruba | `source_gap_do_not_use_no_translation` | Reviewer/source-owner/license/OCR gates remain open; hard Noether prose remains blocked unless the row is explicitly source-backed for school-math scope. |
| `R9-TRANS-20260705-043` | Amharic | `source_body_baseline_present_target_rendering_blocked` | Perform page-render/font-map comparison and reviewer/source-owner/license return before target rendering. |
| `R9-TRANS-20260705-044` | Hausa | `source_archive_and_public_register_candidate_not_translation_ready` | File-body/rendered app language-domain review, license-file/attribution review, source-owner/reviewer return. |
| `R9-TRANS-20260705-045` | Igbo | `source_acquisition_gap_no_translation` | Exact source acquisition or reviewer/source-owner return. |
| `R9-TRANS-20260705-046` | Afar_Qafar | `context_provenance_only_no_translation` | Target-language math source body or transcript required. |
| `R9-TRANS-20260705-047` | R9_ALL_LANGUAGES | `hard_noether_terms_blocked_uncovered` | Higher-math source-canon acquisition or reviewer-ledger return required. |
| `R9-TRANS-20260705-048` | AF05_South_Sudan | `source_acquisition_gap_no_translation` | Exact language/source-owner acquisition required. |
| `R9-TRANS-20260705-049` | AF06_Omotic_Southern_Non_Bantu | `source_acquisition_gap_no_translation` | Exact target-language math source acquisition required. |

## Supporting Source-Canon Artifacts

- `R9_NONCANONICAL_CORPUS_TRANSLATION_SUPPORT_ROWS_20260704.csv`
- `R9_LOCAL_SOURCE_BODY_PROVENANCE_SPINE_20260705.csv`
- `R9_P0_FULL_SOURCE_URL_ACCESS_SIGNAL_SWEEP_20260705.csv`
- `R9_P0_TIMEOUT_RETRY_TIGRIGNA_TEACHER_GUIDE_20260705.csv`
- `R9_HAUSA_GITHUB_SOURCE_ARCHIVE_CAPTURE_20260705.csv`
- `R9_HAUSA_IA_PDF_BODY_CAPTURE_20260705.csv`
- `R9_IGBO_REFINED_SOURCE_WITNESS_RESWEEP_20260705.csv`
- `R9_SOURCE_GATE_MINIMUM_EVIDENCE_MATRIX_20260704.csv`

## Machine-Readable Companion

- `R9_SOURCE_CANON_SUFFICIENCY_TRANSITION_DRAFT_SCAFFOLDS_20260705.csv` contains one row per scaffold/status decision with source context, formula-neighboring notes, reviewer questions, source-canon artifacts, and non-claim flags.


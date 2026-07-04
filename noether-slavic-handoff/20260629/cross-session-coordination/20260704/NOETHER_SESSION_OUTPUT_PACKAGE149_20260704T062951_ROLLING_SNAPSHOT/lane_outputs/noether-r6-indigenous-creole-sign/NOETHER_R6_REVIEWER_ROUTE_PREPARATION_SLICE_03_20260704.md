# Noether R6 Reviewer Route Preparation Slice 03

Generated: 2026-07-04

Status: reviewer-route preparation only. This slice does not contact reviewers, fill returns, accept authority, clear reuse, promote terms/signs/crosswalks, select excerpts, translate, construct surfaces, or open pilots.

## Purpose

Slice 03 prepares durable return-ledger shells for the rows that already have evidence-backed request routes. It exists so future work can ingest real reviewer/source-owner returns without mixing them into support notes or term work.

## Return Ledger Shells To Create Only When A Direct Route Is Verified

| Ledger shell | Parent rows | Recipient profile | Required fields | Still blocked |
|---|---|---|---|---|
| Kreyol MIT-Ayiti return ledger | R6-KR-SAR-001..004 | Source owner, MIT-Ayiti maintainer, Kreyol math educator, or qualified Kreyol STEM reviewer. | Return party, role, authority basis, date, row IDs, source-authority decision, reuse decision, attribution text, scope notes, do-not-use notes. | No terms, excerpts, copied prose/media, adaptation, translation, pilot. |
| Peru Quechua/Aymara EIB return ledger | R6-QA-SAR-001..003 | Peru EIB source-context reviewer, Quechua/Aymara educator, language-standard reviewer, or qualified Andean math-education reviewer. | Named standard, source authority, reuse mode, attribution, crosswalk limits, rejected scopes, next route. | No macrostandard, crosswalk, terms, excerpts, translation, pilot. |
| ASL video-first return/media ledger | R6-ASL-SAR-001..003 | Source owner, ASL STEM lexicon maintainer, Deaf/ASL STEM educator, or qualified ASL reviewer. | Video-route decision, sign/variant decision, media/reuse mode, attribution, context limits, variant/disagreement notes. | No accepted signs, copied media/stills, cross-sign transfer, translation, pilot. |
| LSQ source/media return ledger | LSQ-SAR-001..003; LSQ-CAT-001..011; LSQ-CON-001..014 | LSQ source owner, LSQ school/STEM reviewer, media/license contact, or qualified LSQ access reviewer. | Source authority, category priority, media/reuse status, grade/variant scope, rejected rows, next route. | No accepted signs, visual inventory, copied media/stills, translation, pilot. |
| DGS source/media/SWU return ledger | DGS-SAR-001..008; DGS-CAT-001..008; DGS-CON-001..012; DGS-GOE-V-001..002 | Sign2MINT/source owner, DGS STEM reviewer, media/license contact, Goettingen route owner where relevant. | Source authority, category priority, concept priority, SWU/variant treatment, media/reuse mode, comparator limits. | No accepted signs/SWU, copied media/stills, translation, pilot. |
| Bolivia Quechua candidate-source ledger | R6-IA-P3-003 | Bolivia Quechua/EIB reviewer or source owner. | Source identity, curriculum/context scope, reuse mode, attribution, whether row is source authority, context only, rejected, or needs narrower review. | No terms, algebra authority, crosswalk, excerpts, translation, pilot. |
| Mauritius MIE candidate-source ledger | candidate-00DER-3; candidate-00DER-5 | MIE source owner, Kreol Morisien/Kreol Rodrige education reviewer, or qualified Indian Ocean creole STEM reviewer. | Source identity, language/scope classification, source authority, reuse mode, attribution, whether row is exact source or context. | No terms, translation, cross-creole register, excerpts, pilot. |

## Return State Vocabulary

Use these states consistently:

| State | Meaning | Gate effect |
|---|---|---|
| `route_accepted_link_only` | Source can be linked or named as a route only. | Keeps term/sign/excerpt gates closed. |
| `source_context_accepted_no_reuse` | Source can guide context questions but cannot be quoted/adapted. | Keeps excerpt/reuse gates closed. |
| `short_quote_allowed_with_attribution` | Short quotation is allowed under stated terms. | Opens only exact quoted-use path, not term/sign acceptance. |
| `adaptation_or_translation_allowed_with_terms` | Adaptation or translation is allowed under stated terms. | Requires separate target-lane review before any output. |
| `candidate_video_route_accepted_for_review` | Signed-language video route can be reviewed, but sign is not accepted. | Keeps sign/media gates closed until next return. |
| `sign_variant_accepted_with_scope` | Qualified reviewer accepts a sign/variant with scope. | Still requires media/reuse clearance before copied use. |
| `media_reuse_cleared_for_named_mode` | Source owner/license clears a specific media use. | Does not imply lexical authority. |
| `crosswalk_candidate_requires_separate_ledger` | Comparison may be explored but needs a crosswalk artifact. | Keeps crosswalk acceptance closed. |
| `rejected_or_out_of_scope` | Row should not be used for the proposed support packet. | Preserve rejection in ledger. |
| `needs_more_context` | Reviewer/source owner asks for narrower scope. | No gate opens. |

## Minimum Return Evidence

A return is not ingestible unless it has:

- Dated response.
- Row IDs covered.
- Role or authority basis.
- Source-authority decision.
- Reuse/media decision where relevant.
- Scope limits and do-not-use notes.
- Variant or disagreement notes where relevant.

## Durable Warning

Do not turn a future return into a translation. A return first creates a return-ledger entry. Only a later artifact may decide whether any local term, sign, crosswalk, excerpt, adaptation, or translation-support work is allowed.


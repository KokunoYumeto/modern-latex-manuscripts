# Reviewer-facing glossary table templates - 2026-06-29

This artifact defines reviewer-facing glossary table templates for the Noether multilingual canonical-edition workflow.

It is not a glossary and not a review result. It does not approve any term. It gives future review packets a common table shape so that source anchors, proposed terms, reviewer decisions, and accepted-correction ledger entries can be linked without ambiguity.

Companion machine-readable file: `REVIEWER_FACING_GLOSSARY_TABLE_TEMPLATES_20260629.json`

## Common Reviewer Glossary Columns

| Column | Purpose |
| --- | --- |
| `term_id` | Stable term identifier from `TERM_ID_REGISTRY_SEED_20260629.json`. |
| `language_lane` | Language lane or family. |
| `sublane_or_script` | Register/script where relevant, such as `fa_IR`, `prs_AF`, `tg_Cyrl_TJ`, Latin, Cyrillic, or RTL. |
| `english_concept` | English mathematical concept used as review anchor. |
| `mathematical_domain` | Algebra, invariant theory, module theory, ring theory, finiteness, document logic, or metadata. |
| `observed_source_term` | Native/source term as seen in the source shelf. |
| `source_witness_id` | Source witness identifier. |
| `source_page_refs` | Page or location references from the term-anchor seed. |
| `source_context_status` | `automated_anchor`, `page_inspected`, `ocr_uncertain`, or `needs_source_recheck`. |
| `project_proposed_term` | Term proposed for this Noether translation lane. |
| `alternatives` | Legitimate variants, regional forms, or rejected candidates. |
| `usage_scope` | Section/document/register scope for the proposed use. |
| `current_decision_state` | Term-governance state before review. |
| `review_question` | Short question asked of reviewer. |
| `reviewer_decision` | Accept, revise, reject, variant, unclear, or needs source. |
| `reviewer_recommended_term` | Reviewer replacement or preferred variant. |
| `reviewer_rationale` | Short reason or source pointer. |
| `correction_id` | Accepted-correction ledger ID once ingested. |
| `follow_up_action` | Page inspection, edit, rebuild, sidecar validation, source reinforcement, or no action. |

## Lane Template Requirements

| Lane | Template status | Required extra columns or checks |
| --- | --- | --- |
| Simplified Chinese | `reviewer_glossary_template_ready_not_populated` | CJK render check, mainland/other usage note, formula spacing note. |
| French | `reviewer_glossary_template_ready_not_populated` | Calque risk, regional/institutional variant note, Romance-experiment separation flag. |
| Spanish | `reviewer_glossary_template_ready_not_populated` | Regional variant note, article/preposition check, learner-facing clarity note. |
| Japanese | `reviewer_glossary_template_ready_not_populated` | Kanji/kana balance, imported-term naturalness, line-break/render note. |
| `fa_IR` | `reviewer_glossary_template_ready_not_populated` | RTL render check, Persian-script punctuation/numeral note, sublane isolation flag. |
| `prs_AF` | `needs_more_sources_before_full_glossary` | Dari/Afghan Persian source-reinforcement flag and sublane isolation flag. |
| `tg_Cyrl_TJ` | `unresolved_no_current_term_rows` | Tajik Cyrillic source-discovery flag before table population. |
| Arabic | `needs_more_sources_before_full_glossary` | RTL render check, OCR/provenance flag, module/representation reinforcement flag. |
| Interslavic/Panslavic | `template_ready_for_sidecar_review_when_terms_available` | Latin/Cyrillic sidecar equivalence, community/project authority, term-origin classification. |

## Review Questions by Lane

### Simplified Chinese

- Is this term standard for the mathematical concept in mainland mathematical writing?
- Is the phrase natural inside theorem/proof prose?
- Does the rendered term remain visually attached to the relevant formula or label?

### French

- Is the proposed term standard French mathematical usage rather than an English calque?
- Is a regional or institutional variant acceptable, and should it be recorded?
- Is the term appropriate for a canonical edition rather than only a glossary note?

### Spanish

- Is the proposed term standard for a broad Spanish mathematical audience?
- Is a regional variant legitimate and should it be labeled?
- Does the surrounding noun phrase require article/preposition revision?

### Japanese

- Is the kanji/kana/imported-term balance natural for mathematical prose?
- Does the term work in theorem/proof context, not just in isolation?
- Does line breaking or formula placement affect readability?

### Persian-Family Registers

- Is this decision valid only for `fa_IR`, `prs_AF`, or `tg_Cyrl_TJ`?
- Should a visually similar Persian-script term be treated as a separate register decision?
- Does directionality, punctuation, or numeral style affect the term in rendered context?

### Arabic

- Is this modern standard mathematical Arabic, a regional teaching form, or an OCR artifact?
- Is the source page reliable enough for term promotion?
- Does RTL rendering preserve formula association and reading order?

### Interlanguage / Constructed Pilot

- Is the term inherited from an existing community resource, selected by design, proposed by this project, or machine-generated?
- Does a language-community or project-authority reviewer accept this usage?
- Should the term remain research-only even if it is internally consistent?

## Population Rules

- Populate rows from term-anchor seeds only after assigning `term_id` values from `TERM_ID_REGISTRY_SEED_20260629.json`.
- Keep source anchors and project-proposed terms in separate columns.
- Mark all current rows as unapproved until review returns are ingested.
- Do not copy terms across sublanes without explicit reviewer authority.
- Do not promote OCR-uncertain rows without source-page inspection.
- Connect every accepted term to an accepted-correction ledger entry and artifact hash.

## Immediate Next Gates

- Generate populated draft glossary tables from the existing term-anchor seeds without claiming approval.
- Add page-inspection status fields as human inspection proceeds.
- Use reviewer decisions to create accepted-correction ledger entries only within reviewed scope.

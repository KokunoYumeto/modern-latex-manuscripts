# Multilingual review packet templates - 2026-06-29

This artifact provides reusable reviewer packet templates for the Noether multilingual canonical-edition workflow. It is intended to convert the current evidence shelves, terminology seeds, TeX/PDF artifacts, and manifest discipline into concrete external-review packets.

It is not a review result and does not imply acceptance by any native, technical, educational, or language-community reviewer.

Companion machine-readable file: `MULTILINGUAL_REVIEW_PACKET_TEMPLATES_20260629.json`

## Common Packet Structure

Every review packet should contain:

- Scope: language lane, document or section range, script/register, and reviewer role.
- Artifact list: TeX, PDF, cumulative reader, glossary, rationale log, visual inspection note, manifest, and any sidecars.
- Source evidence: native-register source shelf entries and page anchors used for terminology or style.
- Term table: observed source anchors, proposed project term, confidence, alternatives, and reviewer decision.
- Questions: small, answerable items that separate mathematical correctness, language idiom, pedagogy, and typography.
- Review return format: accepted correction, rejected correction, question, source suggestion, or blocking concern.
- Ledger fields: reviewer, date, artifact hash reviewed, decision, rationale, file/line/page reference, and follow-up action.
- Boundary statement: mechanical validation is complete or incomplete separately from native/external authority.

## Slavic Lane Packet

Applies to Ukrainian, Russian, and Interslavic/Panslavic Latin+Cyrillic sidecars.

Required reviewer roles:

- Ukrainian mathematical reviewer.
- Russian mathematical reviewer.
- Interslavic/Panslavic language-community or linguistics reviewer.
- Script-sidecar reviewer for Latin/Cyrillic consistency.

Priority checks:

- Confirm that ring, field, ideal, module, homomorphism, representation, invariant, and Noetherian terminology matches the intended register.
- Confirm that Latin and Cyrillic sidecars preserve content, punctuation, formula references, and section anchors.
- Identify any terms that look like private invention rather than accepted or intelligible technical usage.
- Confirm that review-return ingestion preserves accepted corrections in both script directions where applicable.

Blocking concerns:

- Sidecar divergence that changes mathematical meaning.
- Reviewer rejection of a core term without a recorded alternative.
- Script conversion errors that affect formulas, citations, labels, or glossary keys.

## Simplified Chinese Packet

Current checkpoint context includes Simplified Chinese Paper34 through Section 18 and seeded terminology anchors from six source witnesses.

Required reviewer roles:

- Native Simplified Chinese mathematical reviewer.
- TeX/PDF visual reviewer for Chinese line breaking, punctuation, and formula spacing.
- Optional educator reviewer for undergraduate readability.

Priority checks:

- Confirm algebra terms for ring, field, ideal, module, homomorphism, representation, invariant, Noetherian, finite generation, and quotient.
- Mark whether terms are standard mainland usage, acceptable but stylistically marked, or incorrect.
- Inspect section headings and theorem/proof transitions for natural mathematical prose.
- Check that formulas and labels are not visually separated from surrounding Chinese text in the rendered PDF.

Blocking concerns:

- Term choice that changes mathematical scope.
- OCR-derived or source-anchor ambiguity promoted into the glossary without page inspection.
- PDF layout issue that makes Chinese text or formulas hard to read.

## French Packet

Required reviewer roles:

- Native or near-native French mathematical reviewer.
- Optional undergraduate educator reviewer for pedagogical tone.

Priority checks:

- Confirm algebra and invariant-theory terminology for anneau/ring, corps/field, ideal, module, representation, invariant, homomorphism, Noetherian, quotient, and finitely generated.
- Distinguish French mathematical convention from literal English calque.
- Inspect theorem/proof prose for idiomatic register.
- Identify where regional or institutional style differs but does not block publication.

Blocking concerns:

- Literal calques that are mathematically understandable but not standard French.
- Failure to distinguish natural-language French lane from any later Pan-Romance or Neolatino research experiment.

## Spanish Packet

Required reviewer roles:

- Native or near-native Spanish mathematical reviewer.
- Optional educator reviewer familiar with undergraduate algebra or physics materials.

Priority checks:

- Confirm algebra and invariant-theory terminology for ring, field, ideal, module, representation, invariant, homomorphism, Noetherian, quotient, and finitely generated.
- Record regional variants when they are legitimate rather than errors.
- Inspect article/preposition choices in mathematical noun phrases.
- Identify places where a learner-facing Spanish edition should prefer clarity over compact specialist style.

Blocking concerns:

- Term choices that are regional but unlabeled where a wider Spanish readership is intended.
- Mixing Spanish natural-language evidence with Romance interlanguage proposals.

## Japanese Packet

Required reviewer roles:

- Native Japanese mathematical reviewer.
- TeX/PDF reviewer for line breaking, script mix, punctuation, and formula spacing.

Priority checks:

- Confirm standard terms for ring, field, ideal, module, homomorphism, representation, invariant, Noetherian, finite generation, and quotient.
- Inspect kanji/kana balance and whether imported technical terms are natural in context.
- Check theorem/proof discourse markers and sentence endings for mathematical prose.
- Confirm that line breaks do not isolate particles, labels, or formula punctuation in an awkward way.

Blocking concerns:

- Incorrect script/term mix that makes a standard mathematical word look nonstandard.
- Rendered PDF layout that breaks Japanese mathematical prose around formulas.

## Persian-Family Packet

Applies to separate sublanes unless external review justifies a cross-register bridge: `fa_IR`, `prs_AF`, and `tg_Cyrl_TJ`.

Required reviewer roles:

- Iranian Persian mathematical reviewer for `fa_IR`.
- Dari/Afghan Persian educator or technical reviewer for `prs_AF`.
- Tajik Cyrillic reviewer for `tg_Cyrl_TJ`.
- RTL/script reviewer where Persian-script artifacts are rendered.

Priority checks:

- Keep sublane decisions separate; do not transfer Persian terms across registers without explicit review.
- Confirm algebra terminology for ring, field, ideal, module, representation, invariant, homomorphism, Noetherian, quotient, and finite generation.
- Identify where source coverage is broad educational rather than advanced algebra.
- Track script, directionality, numeral style, punctuation, and formula alignment separately from lexical correctness.

Blocking concerns:

- Treating `fa_IR`, `prs_AF`, and `tg_Cyrl_TJ` as one lane without external rationale.
- Tajik Cyrillic terms missing from the evidence shelf.
- RTL rendering problems that affect formulas, citations, or glossary alignment.

## Arabic Packet

Required reviewer roles:

- Native Arabic mathematical reviewer.
- RTL/TeX/PDF reviewer.
- Optional educator reviewer for undergraduate register.

Priority checks:

- Confirm algebra terminology for ring, field, ideal, module, homomorphism, representation, invariant, Noetherian, quotient, and finite generation.
- Distinguish modern standard mathematical Arabic from regional pedagogy preferences.
- Inspect whether OCR/text-extraction artifacts contaminated any source anchor.
- Check RTL rendering, punctuation, formula embedding, labels, and glossary ordering.

Blocking concerns:

- OCR-derived term evidence used without page inspection.
- Missing module/representation source reinforcement.
- RTL layout issues that change reading order or formula association.

## Interlanguage / Constructed Pilot Packet

Applies to Interslavic/Panslavic work and any later semi-constructed or constructed-language research pilot.

Required reviewer roles:

- Language-community or project-authority reviewer where an existing interlanguage community exists.
- Linguist/interlinguistics reviewer.
- Mathematical-register reviewer.
- Script/tooling reviewer when sidecars or transliteration are part of the claim.

Priority checks:

- Identify whether each term is inherited, selected from community resources, newly proposed, or machine-generated.
- Check that design changes are logged as proposals and not silently represented as community usage.
- Confirm that examples are framed as research or pilot material unless external review supports learner-facing use.
- Ensure that open-source handoff is not described as community consent or adoption.

Blocking concerns:

- Canonical-edition claim before language-community and mathematical review.
- Missing distinction between constructed pilot, zonal/interlanguage project, and computational pivot.
- Script sidecar failure where the language community treats script as accessibility or authority.

## Review Return Schema

Each reviewer response should be ingestible into a correction ledger with these fields:

- `review_packet_id`
- `reviewer_role`
- `review_date`
- `artifact_hash_reviewed`
- `location`
- `issue_type`
- `severity`
- `current_text_or_term`
- `recommended_change`
- `source_or_reason`
- `decision`
- `accepted_correction_id`
- `follow_up_owner`

## Immediate Packaging Next Steps

- Convert these templates into per-lane packet files when a lane is ready for external review.
- Add reviewer-facing glossary tables for each language from the current term-anchor seeds.
- Add one accepted-correction ledger template shared across lanes.
- Record reviewer packet IDs in the status manifest once packets are emitted.

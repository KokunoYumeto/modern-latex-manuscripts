# Interlanguage reviewer authority and decision framework - 2026-06-29

This artifact extends the Noether research/publication lane for AI-assisted technical-register construction, semi-constructed/interlanguage methodology, educational translation, open-source handoff, and authority boundaries.

It is not a canonical-edition approval for any constructed or zonal language. It is a review and decision framework for deciding when work remains a research artifact, when it can become an educational pilot, and when it can even be considered as a candidate translation lane.

Companion machine-readable file: `INTERLANGUAGE_REVIEWER_AUTHORITY_DECISION_FRAMEWORK_20260629.json`

## Scholarly and Policy Anchors

| Source | URL | Use in this project |
| --- | --- | --- |
| Centre for Research and Documentation on World Language Problems (CED) | https://interlingvistiko.net/en/home/ | Establishes interlinguistics, language policy, and linguistic justice as an existing research ecosystem rather than an invented framing for this project. |
| CED description of Language Problems and Language Planning | https://interlingvistiko.net/en/language-problems-and-language-planning/ | Journal witness for multilingual scholarship on language problems, planning, and policy. |
| Federico Gobbo, Introduction to Interlinguistics | https://pure.uva.nl/ws/files/45013583/Gobbo2020_Introduction_to_Interlinguistics_FINAL_DRAFT.pdf | Book-length scholarly orientation for interlinguistics and Esperanto/planned-language study, tied to the University of Amsterdam special chair. |
| Haugen / language standardization overview | https://link.springer.com/article/10.1007/s10993-020-09549-x | Anchor for separating selection, codification, elaboration/function, implementation/diffusion, and acceptance questions. |
| Robert L. Cooper, Language Planning and Social Change | https://books.google.com/books/about/Language_Planning_and_Social_Change.html?id=-cOBzspgFNcC | Anchor for status, corpus, and acquisition planning and for the point that language planning serves social goals beyond linguistic form. |
| Bernard Spolsky, Language Policy | https://www.cambridge.org/core/books/language-policy/ECEC8D0753B37847BF04AF29D44D0BE8 | Anchor for distinguishing practices, beliefs/ideologies, and management decisions in language policy. |
| Grant Goodall, Constructed Languages | https://par.nsf.gov/servlets/purl/10478617 | Recent scholarly overview treating constructed languages as legitimate linguistic research objects. |
| Nathan Sanders, Constructed languages in the classroom | https://works.swarthmore.edu/fac-linguistics/188/ | Pedagogy anchor for constructed languages as classroom tools, while keeping pedagogy distinct from community or canonical authority. |
| Language Invention in Linguistics Pedagogy | https://global.oup.com/academic/product/language-invention-in-linguistics-pedagogy-9780198829881 | Book-level witness for invented languages as a university pedagogy practice. |
| UNESCO languages in education | https://www.unesco.org/en/languages-education | Education-policy anchor for mother-language and multilingual education, inclusion, and learner comprehension. |
| UNESCO multilingual education article | https://www.unesco.org/en/articles/multilingual-education-key-quality-and-inclusive-learning | Policy anchor for multilingual education as a quality and inclusion issue. |
| UN Declaration on the Rights of Indigenous Peoples | https://social.desa.un.org/issues/indigenous-peoples/united-nations-declaration-on-the-rights-of-indigenous-peoples | Rights anchor for language, culture, education, self-determination, and community authority. |
| UN declaration on minority rights | https://legal.un.org/avl/ha/ga_47-135/ga_47-135.html | Rights anchor for linguistic minorities and language use without discrimination. |
| UNESCO OER Recommendation | https://www.unesco.org/en/legal-affairs/recommendation-open-educational-resources-oer | Open-education anchor for licensing, localization, capacity-building, and reusable educational materials. |
| CARE Principles | https://www.gida-global.org/careprinciples | Governance anchor for collective benefit, authority to control, responsibility, and ethics. |
| TRUST Code | https://www.globalcodeofconduct.org/trust-code/ | Ethics anchor for avoiding extractive research partnerships and one-way authority claims. |
| FAIR Principles | https://www.go-fair.org/fair-principles/ | Mechanical stewardship anchor for findability, accessibility, interoperability, and reusability. |
| Open Source Definition | https://opensource.org/osd | Handoff anchor for redistribution, modification, non-discrimination, and license freedoms. |

## Review Authority Checklist

### Natural-Language Translation Lane

- Source shelf covers native-register mathematical writing in the target language, not only bilingual dictionaries or machine translations.
- Terminology glossary separates observed native anchors from proposed project usage.
- TeX/PDF renders are checked visually and mechanically.
- Native or near-native technical reviewer has authority over idiom, register, and local mathematical convention.
- Machine-readable manifest records source coverage, files, hashes, known gaps, and review state.
- Local validation may certify reproducibility and consistency; it may not certify native acceptability.

### Multi-Standard or Multi-Register Family Lane

- Each standard or register is tracked as its own sublane until a cross-register rationale exists.
- Shared terms and divergent terms are listed separately.
- Script, orthography, and transliteration choices are treated as governance decisions, not typography alone.
- Review requires authority for each affected standard/register.
- A family bridge may be publishable as research before it is appropriate as a learner-facing translation.

### Zonal or Interlanguage Lane

- Existing project authority is identified: institution, community, maintainers, dictionaries, grammars, corpora, active speakers/users, and software.
- Design changes are logged as proposals, not silently folded into the language.
- Latin/Cyrillic or other script sidecars are validated when the language community treats script as part of accessibility.
- Reviewer packet includes language-community review, linguist review, and mathematical-register review as separate gates.
- The lane stays research/pilot until external review supports learner-facing use.

### Constructed-Language Pilot

- The pilot has an explicit research question and does not claim to represent a community.
- Grammar, morphology, script, lexicon, and mathematical register are versioned and testable.
- Translation samples are marked as demonstrations, not canonical editions.
- Educational deployment requires opt-in users, teacher review, and a rollback/rejection path.
- Publication framing emphasizes method, auditability, and limits rather than adoption.

### Low-Resource or Under-Served Educational Lane

- The project identifies local educational needs without claiming to speak for local users.
- Open licensing, local editability, and handoff paths are recorded.
- CARE/TRUST-style authority review is required when the language/community is minoritized or politically sensitive.
- Teacher/community feedback is tracked separately from mechanical validation.
- The default posture is inspectable handoff; downstream users retain authority to reject, fork, adapt, or own the materials.

### Computational Interlingua or MT Pivot

- Corpus alignment, tokenization, model versions, and evaluation metrics are reproducible.
- Any user-facing text generated from the pivot receives human language review.
- A computational pivot is not a language standard and cannot substitute for speaker/community authority.
- Publication claims are limited to tooling, alignment, or evaluation unless reviewed human outputs exist.

## Decision Framework

1. Identify the object.
   - If it is an established natural language, route to a translation lane.
   - If it is a regional standard, dialect, register, or script variant, route to a sublane and require local authority.
   - If it is a zonal/interlanguage project with existing community resources, route to the interlanguage research lane first.
   - If it is newly designed by this project, route to a constructed-language pilot only.
   - If it is an MT/corpus pivot, route to computational methodology only.

2. Identify the authority claim.
   - Mechanical claim: files build, scripts validate, hashes match, terminology is internally consistent.
   - Evidential claim: native-register sources exist and the project cites them accurately.
   - Pedagogical claim: the material can help learners in a defined setting.
   - Community claim: users or speakers accept, prefer, or own the language/register.
   - Canonical-edition claim: the language lane is suitable for canonical Noether publication.

3. Match evidence to claim.
   - Mechanical claims can be handled locally.
   - Evidential claims require source shelves and page inspection.
   - Pedagogical claims require educator/learner review.
   - Community claims require community authority.
   - Canonical-edition claims require external native/technical review plus complete render/package validation.

4. Choose the publication state.
   - Research note: method, risks, source shelves, and examples only.
   - Educational pilot: limited learner-facing material, explicit opt-in context, review packet, no canonical claim.
   - Candidate translation lane: complete source shelf, glossary, TeX/PDF, manifests, and external review plan.
   - Review-ready edition: full artifact set, accepted-correction ledger, visual inspection, reproducible build status, and reviewer signoff.

5. Record the boundary.
   - Every artifact must say what it proves and what it does not prove.
   - Term anchors are not term approvals.
   - Open source is not community consent.
   - A successful build is not a successful translation.
   - A constructed language can be a valid research object without being a valid canonical edition.

## Publication Note

For an article or project report, this PC branch should frame semi-constructed and interlanguage work as methodological research under the translation header:

- It asks how AI-assisted workflows can make technical-register construction auditable.
- It uses source shelves, term anchors, render manifests, and correction ledgers to separate machine-checkable claims from authority claims.
- It treats interlanguage projects as existing communities and governance structures, not blank design spaces.
- It treats low-resource educational translation through open-source handoff, not intervention.
- It pairs FAIR-style reproducibility with CARE/TRUST-style authority and ethics.
- It names native/external review as a requirement, not an optional polish step.

## Immediate Next Gates

- Add per-lane reviewer packet templates for Chinese, French, Spanish, Japanese, Persian-family registers, Arabic, and Interslavic/Panslavic sidecars.
- Build a publication-outline artifact for AI-assisted technical-register construction and interlanguage authority.
- Add a terminology-governance matrix for natural-language, zonal/interlanguage, and constructed-pilot terms.
- Keep all new work on `codex/noether-pc-20260629` and preserve the distinction between local PC progress and project-level completion.

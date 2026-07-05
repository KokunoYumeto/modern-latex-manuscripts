# Source Use Policy
2026-07-04. Formalizes what each corpus stratum may and may not feed (post-Fable steer Task C). The categories are exclusive per use: a file can serve several categories, but each USE must declare which category it exercises.

## Categories

**1. canonical_source_authority** — the historical source text itself.
Holders: Noether German corpus (source witnesses, `$germanOut\sources\paperNN`), SGA certified .tex (French), Weber/Cayley source shelves.
May feed: German term normalization, concept IDs and glosses, source-context snippets, paper/section anchors, historical-vs-modern concept warnings, source-side disambiguation.
May NOT feed: witness status for ANY target language; promotion of any bridge form. The source proves what the author wrote, not what any community calls it today.

**2. language_family_witness** — native, independent, target-language sources.
Holders: uk/ru canonical corpora; the 20-source W/S triangulation shelf (cs/pl/sk/sl/hr/sr/bg university/institute texts); Pan-Romance native shelves (es/fr tier-0 + pt/gl/ca/it/ro/rm files); controlled-Arabic native register shelf; Malay-Indonesian institutional sources.
May feed: witnessed_for_branch status, attestation counts, branch balance statistics, competitor evidence (a witness for a different lexeme is adverse evidence against family-centrality of the current form).
Provenance levels within this category stay explicit: concept_shelf (shelf attests the concept's branch form) < row_verified (this term's form checked in context) < reviewed (human/community return).

**3. draft_translation_triangulation** — AI-era translation drafts.
Holders: Chatnotes Stratum-D tree (827K files incl. per-author bilinguals, Kimi drops, ES/JA zip), dump translations/ working drafts.
May feed: candidate-form proposals, register comparison, consistency checks, error mining, concept-coverage discovery.
May NOT feed: witness status (any branch, any level), attestation counts, promotion arguments. Status ceiling: linked/unreviewed. Compaction-era caveat applies always.

**4. candidate_form_source** — places surface candidates may legitimately come from.
Holders: categories 1–3 above (via their allowed uses), community dictionaries/portals (Interslavic dictionary, project grammars), comparator corpora (Interlingua/Esperanto/etc — evidence floor + warning comparators, never authority), lane rejection matrices (as negative candidates).
Rule: every candidate carries its origin tag; candidates from category 3 are flagged draft-origin and require a category-2 witness before any promotion argument.

**5. adverse_evidence_source** — where typed negative relations come from.
Holders: false-friend lists (community + lane), DO_NOT_USE ledger, Persianate rejection matrices, warning-comparator statuses, collision discoveries (Ränderung-class), competitor attestations from category 2.
Rule: adverse evidence is never folded into positive counts; veto relations bind regardless of support volume.

**6. external_authority_review** — community/human returns.
Holders: external-review role packets (prepared), van Steenbergen contact (planned), any future accepted returns.
Only this category can move a row to reviewed_for_bridge_use, certify a term, or close a pilot gate. Zero returns exist as of 2026-07-04; every artifact says so.

## Cross-cutting rules
- Linkage ≠ witness ≠ review (three-status discipline) — restated here because every misuse in the program's history blurred one of these lines.
- Freeze-then-fix: repairs are new artifacts; pre-repair states stay in `frozen/`.
- The stop-and-ask list (post-Fable steer §6) binds all automated work: no term promotion/renaming, no GitHub/Zenodo push, no external contact, no draft-as-witness, no GPU/embedding runs, no new packages beyond cap — without Floris.

# D031 final independent cold content review

Date: 2026-08-31. Decision: PASS WITH SCOPE LIMITATIONS. No remaining high-confidence content or rendered-layout defect was found within the scope below. This decision applies only to the six exact normalized files identified here. It is not acceptance of the immutable returned input or of an inherited salvage conclusion.

## Reviewed identities

All paths below are relative to D031/normalized. SHA256 and byte counts were independently recomputed from the files, not accepted from the producer's manifest.

| File | Bytes | SHA256 |
|---|---:|---|
| french_diplomatic.md | 172603 | F759118CD71B8CF239A174F5A1EE674F2878EBAE42BE08EEA0361BD318364C5F |
| french_diplomatic.pdf | 624217 | 097E041027B187A3E77846C43C394E694317A6A48ED14699B9C7AAC131B53ED7 |
| english_translation.md | 166695 | 93652E0368424AB9D70D6F05CAC5DE42639A0FD622A11AF6F3FE7689A3E555B2 |
| english_translation.pdf | 617180 | AE249736213AB6C581A9C36173D48157328225BA43DC80EEEBAF1195F9251C17 |
| apparatus.md | 43173 | 7AE648DD23F3AEE612968C5E5D80210B8B1932A12229E399FFD05905E020826C |
| apparatus.pdf | 252394 | 691A5D29ADBE0F25F6C647B54D3F11FF7CB3EEAB481D4AEFD16D5EBB105194DE |

Controlling authority is the exact IAS43-page PDF, SHA256 `591EE837C4C87E5263B76427B393742E111D615C6E098C940F132519A0861922`, 2735096 bytes. Its43 physical pages correspond to printed247-289. The header's247-290 claim does not supply a missing290 leaf. Comparison-only collected43-page PDF SHA256 `5A8B592C4A1BF21CBA5403B4CE8584D772CD7E907DD8B6EC7FCF9FE8E03605AC`,1331405 bytes, never superseded controlling pixels. Both source identities and the initial French, English and apparatus identities were rehashed unchanged after the repair builds.

## Independent work performed

The initial audit, documented in `content_audit.md`, examined every authority page1-43 at legible180dpi or original-size rendering, including page-owned text boundaries, headings/results, numbered displays, native diagram incidence and labels, copy matter and terminal bibliography/address. The four mandated fault sites were inspected directly from authority pixels. All cross-language mathematical spans were compared mechanically, and every emitted difference was reviewed in context. No inherited audit or salvage acceptance supplied the decision.

The first normalized freeze was superseded during review for the English page14 qualifier. The second received a complete sequential rendered pass1-43 in both readers, direct high-resolution examination of1,3,11,15,16,20,31,37,38,41,43 in both languages, English9/14, and a300dpi page16 equality crop. It was NOT accepted because table15 contained label collisions, reported as R01. This failure led to N012.

The final N012 freeze was independently hashed, freshly text-extracted, and checked again from physical1 through43 in both PDFs using the newly generated whole-page contact renders. The new final table15 was separately rendered directly from each actual PDF at180dpi and inspected against authority15. The final PDFs remain43pages each, with sequential printed folios247-289 and no page290. All final Markdown page-record bodies were compared with the immutable originals; only the documented repair and typesetting-normalization sites differ.

Before this terminal receipt, the producer independently noticed an orphaned A092 apparatus heading at the bottom of the prior apparatus PDF page8. An apparatus-only keep-with-next correction then superseded that PDF; both reader PDFs and all three Markdown files remained hash-identical. This reviewer independently rehashed the final apparatus PDF to the identity above, freshly text-extracted it, re-inspected all12 new apparatus pages, and directly rendered and inspected page9 at160dpi. A092 now stays with its body, the surrounding notes remain present, and no further orphaned note heading was observed. N001-N012 and corrected A088/A097 were read; no source or mathematical wording was changed by this last presentation repair.

To bind detailed prior visual observations to the final bytes, final pages1,3,11,16,20,31,37,38,41,43 in both languages were freshly rendered at160dpi and compared by SHA256 with the already inspected second-freeze renders. All20 image pairs are byte-identical. Page15 is deliberately different and was freshly inspected at180dpi. Thus the final review does not infer formula agreement merely from abstract mathematical equivalence or rely on a stale PDF image.

`final_mechanical_alignment.json` records the full final cross-language comparison:43 paired source-page records,3201 French and3192 English math spans,108 French and111 English display delimiters,23 TikZ-CD diagrams and7 TikZ pictures in each language,36 ordinary explicit tag commands plus the separately represented special tag. The differing display count is inline/display regrouping, not three missing source equations. Every emitted final cross-language difference was rechecked; the differences are translated prose inside mathematics, prose/mathematics regrouping, word-order changes, contextual repeated-symbol omissions, and explicit grouping parentheses. No new translation-only formula defect was found. English page14 now preserves the qualified equivalence to Satake's problem, as documented by N011.

`frozen_delta_audit.json` records exact final per-page bodies, tags, diagram counts, hashes and deltas, plus fresh PDF folio extraction. It shows French changed pages1,3,11,15,20,31,37,41 and English those pages plus14. Table of contents conversion on1, French ordinal typesetting on15, and N012 label offsets are presentation changes. Other body deltas are the precise source repairs below.

## Repair closure and mandatory checks

| Initial finding | Final result |
|---|---|
| C01,3/249 introductory diagram | Quotient is in the middle-right; both quotient arrows oblique; downward norm arrow and label retained. |
| C02,41/287,2.7.11 | Exactly three complex-base subscripts restored; source-unscripted neighboring terms unchanged. |
| C03,11/257,1.2.3 | Source-literal missing group before `(C)` retained; apparent mathematical incompleteness disclosed in N003. |
| C04,15/261 | Source-local pairing variable z and prose root r both retained, not unified; French singular racine restored and discrepancy disclosed. |
| C05-C06,20/266 | Source prose superscript plus and A-without-f restored only at the identified occurrences; displayed subscript-plus and adjacent finite-adele terms retained. |
| C07,31/277,(2.4.8.1) | Both downward injection hooks present; separate archimedean diagram unchanged. |
| C08,37/283 | Added lower-middle-to-right arrow removed only in the first unnumbered diagram; numbered diagrams retain their source arrows. |
| C09, apparatus A088/A097 | False scanner-border/sliver statements replaced by actual tight single-page crop descriptions; running heads and folios still recorded. |
| R01, rendered15 | E6 central2 and E7 central3 clear the vertical branch; D_H right label clears its circled vertex; all seven diagrams' numerical values, node associations, circles, underlines and bond directions retained. N012 discloses the offsets. |

All four mandatory sites pass in the final normalized readers: page3 norm diagram as above; page16 condition2.0.1(a) has r(phi(gamma)) with no extra g; page38's right-action sign convention has r_{G,X}(sigma) with no inverse, while the distinct legitimate inverse in Theorem2.6.3 remains; page43 bibliography item5 is Expose389. The13 bibliography entries, SGA line, terminal address and printed289 endpoint are retained. The table of contents retains its source section/page mappings.

## Scope limitations

- This is a complete page-topology review, a focused source-symbol/diagram review, a complete mechanical cross-language mathematical comparison with manual difference review, and a final rendered-layout review. It is NOT a glyph-by-glyph certification of every character or all roughly3200 mathematical spans against the scanned source.
- Mathematical equivalence alone was not treated as source agreement. The known source-local omissions and inconsistent variables are intentionally reproduced and documented. This is not a certification that those source expressions are mathematically correct.
- The final whole-page pass checks page topology and visible layout; high-resolution direct examination is concentrated at the mandatory, repaired and additionally suspicious sites described above. No unperformed exhaustive high-resolution character audit is claimed.
- No proof verification or external historical-bibliographical verification was attempted. The exact supplied authority pixels control textual readings. The comparison PDF supports select observations but does not replace authority.
- This reviewer did not modify input_state or normalized files, did not build the deliverable PDFs, and did not assess any publication transaction. Only QA scripts, renders and reports under qa_content were written. Parent structural/replay checks are separate evidence, not a substitute for this review.

Remaining observed defects within this scope: none. No further repair is requested by this reviewer. A later change to any identified normalized file invalidates this byte-specific decision and requires an appropriately scoped new review.

# D005 parallel bilingual layout correction logbook

## 2026-08-02 — adverse sequential composition reopened

- The predecessor's final French and English PDFs were copied byte-identically into `inputs/`; its source-alignment and native-diagram decisions remain controlling.
- The predecessor bilingual wrapper concatenated 26 English pages and 27 French pages sequentially. Floris clarified that terminal bilingual readers must be genuinely side by side.
- Blind ordinal pairing is not admissible because the page counts differ.
- Page-text and section-boundary replay shows the extra French page accumulates before Section 3: English Section 4 begins on output page 16, while French Section 4 begins on output page 17.
- The first trial inserted `\clearpage` immediately before English Section 3. Section 3 already began at a natural page boundary, so the trial remained 26 pages and did not alter alignment. No trial PDF is admitted.
- The second trial moved Corollary (2.7) to a fresh page, but subsequent content reflow still compressed the complete reader to 26 pages. It is retained in the active-source history but is not by itself an admitted final layout.
- The third trial bounded Corollary (2.7) by page breaks and produced 27 pages, but it shifted English Section 3 to page 15 while French Section 3 starts on page 14; English Section 4 aligned on page 17, and English Section 5 drifted to page 23 against French page 22. It is rejected as a semantic-layout mapping despite its clean build.
- Boundary replay of the unmodified readers establishes a simpler invariant: French Sections 2–5 each begin exactly one page later than their English counterparts.
- The fourth English trial starts Theorem (1.11) on a fresh page. It aligns Sections 2, 3, and 5, but English Section 4 still begins on page 16 against French page 17 and the total remains 26 pages. It is therefore rejected as the final mapping.
- The current hypothesis leaves the final English PDF byte-identical and reflows only a copy of the French TeX by changing the vertical margins from 0.82 inch to 0.62 inch while preserving the 0.82-inch horizontal measure. This increases vertical text capacity by about four percent, matching the observed 27-to-26-page difference without changing source content, font size, line measure, formulas, or diagrams.
- This is an active hypothesis until the new English page count, section starts, all 27 rendered spreads, and terminal bibliography pair are personally checked.
- Terminal provenance is governed by `PROJECT_LOGBOOK_METHODOLOGY_REPLICATION_DOI_REQUIREMENT_20260802.md` (2,296 bytes; SHA-256 `BFA1E3A3EDA94E8C3425BAE50C842610A47D508FB260BF761BA3206883012679`).

## 2026-08-02 — page-pairing trials superseded by source-level synchronization

- The French-margin reflow hypothesis was built and inspected but rejected. It changed pagination without furnishing a stable semantic correspondence between the two independently reflowing page streams. A matching page count is not sufficient evidence that corresponding mathematical units are paired.
- The same objection applies to every earlier `\clearpage` trial: page boundaries are layout accidents, not durable bilingual alignment anchors. All such trial TeX/PDF states are adverse history and are excluded from the final source surface.
- Direct comparison of the two closed TeX bodies revealed the stronger invariant: after their preambles, each contains exactly 265 blank-line paragraph blocks in the same semantic order.
- Two apparent block boundaries are internal to a single LaTeX environment in both languages: source blocks 33–34 share one `center`/`tabular` unit, and source blocks 143–144 share one `enumerate` unit. Splitting either environment would be invalid TeX and would distort semantic grouping. Each pair is therefore merged symmetrically, yielding 263 logical bilingual units.
- `tools\GENERATE_PARALLEL_SOURCE.ps1` asserts both 265-block counts, performs only those two symmetric merges, emits French on the left and English on the right, and synchronizes the `paracol` streams after every logical block.
- Separate saved footnote counters are necessary because each language has its own footnote stream. Reusing one shared counter would create numbering drift merely from column switching. The generator therefore restores and saves French and English counters independently around every paired block.
- A3 landscape was selected because each side retains a normal mathematical text measure. Portrait two-column composition made dense formulas and diagrams unnecessarily narrow; sequential full-page composition failed Floris's side-by-side requirement.
- The generated source replay is deterministic and byte-exact: 265 French blocks, 265 English blocks, 263 logical pairs, 339,600 bytes, SHA-256 `F273BE3D523BE6A6A597F3BF4604167A85DD55475D99C9DA2738081AEA769E58`.
- The generator introduces composition commands and logical-block comments but does not alter any French or English source block. The two inputs remain byte-identical to the closed predecessor.

## 2026-08-02 — final personal spread review and closure

- The final source-synchronized reader builds in three XeLaTeX passes to 23 A3 landscape spreads. The final log has zero fatal errors, undefined control sequences, multiply-defined labels, duplicate destinations, missing characters, overfull boxes, or rerun requests.
- I rendered every spread at 600 dpi in five small serialized batches to avoid CPU spikes and inspected all 23 personally. This review was not delegated.
- Review criteria were: both languages present; corresponding unit visible on the same spread; intact formulas and native diagrams; synchronized headings, notes, footnotes, bibliography, and received date; no clipping, overlap, column intrusion, unintended blank, or broken glyph.
- All 23 spreads pass. Dense diagram pages 9, 12–14, and 17–22 remain readable and paired; the terminal bibliography spans 22–23 in both languages and ends with the same received date.
- The 600-dpi evidence is strictly output-layout evidence. It does not replace the predecessor's direct 5,000/9,000-dpi authority evidence for source readings and diagram semantics.
- No new transcription, translation, normalization, source correction, or diagram repair was made in this successor. Therefore no global textual repair was triggered. The only admitted functional change is the source-synchronized bilingual composition described above.
- If a later audit finds a source or translation defect, it must be logged append-only against the predecessor decision ledger, repaired in both standalone language sources and this generated bilingual successor, and replayed across every affected downstream reader before the defect can be considered closed.

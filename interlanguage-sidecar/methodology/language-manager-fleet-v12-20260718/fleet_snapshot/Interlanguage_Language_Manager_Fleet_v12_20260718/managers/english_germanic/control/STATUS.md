# English / Germanic status — 2026-07-18

## Noether

- English coverage exists for all 43 papers: one complete RA10 cumulative TeX
  and PDF, 43 editable per-paper TeX files, and 43 standalone PDFs.
- RA10 is complete as an older English translation, not current against the
  German authority. The current German source-control witness is R823.
- Paper-level normalized source-drift triage found no unchanged paper slices:
  35 large deltas, 7 moderate deltas, and 1 small delta. These scalar results
  route review effort only; they do not decide correctness or publication.
- Papers 5, 7, 10, 18, 20, 25, 26, 27, 28, 29, 36, and 37 now have
  source-synchronized, compiled, visually inspected R823 English component
  packages with exact manifests. Thirty-one paper dispositions remain before
  the cumulative rebase can be treated as complete.
- This is synchronization debt, not missing English coverage. Each German
  change must be classified as prose/math/footnote/editorial/macro-only before
  it is propagated into English.

## SGA 5

- A complete legacy English cumulative TeX and reader PDF were recovered. It
  covers all ten curated exposés through printed page 484.
- Against the current French workpass, all ten exposés carry synchronization
  debt: 5 large deltas and 5 moderate deltas.
- The ongoing synchronization return has classified 432 source-delta
  candidates, including 170 safe exact propagations; individual adjudication
  continues for the remaining cases.
- Exposé III B contained a substantive omission. Its §§5.0--5.8 repair,
  including 43 numbered formulas, the missing footnote, and diagram 5.8.4, is
  currently being inserted and structurally validated. It is not yet an
  accepted publication payload.

## SGA 6

- Two complete inherited English controls (including a repair108 variant) were
  recovered, but neither is synchronized to the source-checked French work.
- The current French source-rescribe is checked through idx646 (printed page
  633); its next source cursor is idx647.
- The last sealed cumulative source-checked English workpass covers idx532--607,
  printed pages 519--594, and declared source-PDF pages 526--597 where
  present. It completes Expose X: Sections 1--6, Appendix §§7.1--7.18, and
  the bibliography.
- This cumulative uses the archive-maintainer-corrected idx543 base (`inside
  Z`) and adds sixty-four source-checked indices in eight sealed cumulative
  extensions. It includes independent scan, workpass, final-TeX, and
  inherited-witness audits and
  explicitly records every printed-source emendation rather than silently
  attributing a corrected reading to the scan.
- The accepted continuation cursor is **idx608**, printed page 595,
  source-PDF page 598, beginning Expose XII. The remaining source-controlled
  gap is idx608--646 inclusive (39 indices).
- The declared 702-page scan omits idx593 and idx595--597. The French
  source-control workpass was checked against a separately documented
  720-page, 360-dpi Internet Archive witness that contains those pages. Future
  idx532--607 package records those declared-scan coordinates as `ABSENT` and
  cites the high-resolution witness explicitly. All ten idx598--607
  declared-scan pages were also checked against that complete witness.
- Clear French-workpass defects and source-carried mathematical caveats at
  idx598, idx604, and idx606 are durably flagged both in the English package
  and in a note beside Claude's French workpass; the French TeX was not
  silently edited.
- The inherited full English remains a control only.

## SGA 1--4 controls

- English PDFs for SGA 1--4 and editable SGA 3 TeX were recovered.
- SGA 1--3 strongly support US `fiber` and `neighborhood`; SGA 4 is mixed.
  These controls support consistency decisions but do not override the source.

## Active production order

1. Continue the Noether paper-by-paper R823 rebase with per-paper evidence,
   correction, build, visual-QA, and publication ledgers.
2. Accept the SGA 5 worker return only after the repaired cumulative source,
   compile, rendered pages, terminology ledger, and exact manifest pass the
   lane hard gates.
3. Accept SGA 6 extensions only at sealed source cursors with the same hard
   gates; do not treat an in-review extension as accepted coverage.
4. Keep SGA 5 and SGA 6 German editions in the Germanic target-expansion
   queue. Begin target production only after the corresponding source-aligned
   English edition is stable, and route it through the same manager session,
   source graph, cohort tree, terminology ledger, and hard gates.

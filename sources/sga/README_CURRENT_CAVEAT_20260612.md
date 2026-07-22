# SGA Source Tree Caveat, 2026-06-12

This source tree preserves earlier SGA working packets, validation files, and
repair artifacts. Some folder names and older internal manifests use words such
as `strict`, `complete`, `validated`, or `source-checked`. Those words should be
read in their original packet-local context, not as current global certification.

Current public interpretation:

- SGA 5 French is carried through repair016, with a post-repair rescan reporting
  no new concrete defects in tested lanes. This is not an every-symbol global
  certification.
- SGA 5 English is an unsynchronized carry-forward branch unless a later packet
  explicitly states synchronization.
- SGA 6 repair003 restores Expose VI source pp. 372-387 in French, but later
  dense-region and diagram worklists remain open, especially around pp. 388-460
  and pp. 571-680.
- SGA 7-I material is working-draft material unless a specific later packet
  declares source-checked coverage for a named range.
- The SGA 1 and SGA 2 full-volume convenience readers in
  `sga1-sga2-full-volume-convenience-readers-reinhold-e7a259f-20260722` render
  Jacob Reinhold's LLM-generated English translation at pinned snapshot
  `e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e`. They are not French-source
  authority or source-audited translations; separately named audited/aligned
  checkpoints take precedence for the ranges they cover.
- Witness-aid ZIPs, OCR, crops, and worklists are locator/check layers; they are
  not replacement text or source authority by themselves.

For the live reader-facing status, use the SGA Zenodo record page and
`docs/records/sga.md`.

# SGA3 VII and SGA6 post-token-cutoff custody snapshot

Observed: `2026-07-27T14:46:53.7940911+02:00`

This privacy-clean archive-control snapshot recovers work that continued after
the archive-maintenance task lost its weekly-token context. It records exact
live boundaries so later publication cannot silently skip them. It is not a
body transport, publication authorization, or Zenodo mutation request.

## Public head

- Existing SGA concept: `10.5281/zenodo.20410947`.
- Current SGA version:
  [`10.5281/zenodo.21623401`](https://doi.org/10.5281/zenodo.21623401).
- GitHub `main`:
  `f7f3c2441e76cf16fa5969d98b3a0c01d0a0d804`.
- The current record already contains the complete bounded SGA3 Expose VIII
  checkpoint. This snapshot does not reopen or duplicate that publication.

## SGA3 Expose VII closeout

Local root name: `sga3_exposeVII_english_reconstruction_20260724`.

The textual endpoint has been integrated through VIIB Section 5.5 and the
bibliography. The final master currently includes 97 inputs.

- Master: `tex/SGA3_Expose_VII_English_Loop1.tex`, 8,587 bytes, SHA-256
  `0818906CA1A00AB44DBB8E167FFCFB500F0CAB966012657571920CA8C623C07C`.
- Final Section 5.5 component:
  `tex/components/94_expose_VIIB_section55_complements_en.tex`, 5,573 bytes,
  SHA-256
  `07A2D69E58384FFF45238BB625CFDBBD3DA8B3D562E69FF0C3B4089CFC09D267`.
- Final bibliography component:
  `tex/components/95_expose_VIIB_bibliography_en.tex`, 6,013 bytes, SHA-256
  `06A1551B40A5F5E20B5002DC5852E03C0BCE86AC98CBF7189E52F1064AF267F5`.
- Fresh complete reader:
  `build_exposeVII_complete_r1/SGA3_Expose_VII_English_Loop1.pdf`,
  211 pages / 1,707,365 bytes, SHA-256
  `FA8FC1FDC19130E69763BD4BEE7D8A42710BC41DD0A571E4B61703B789202225`.
- Build-log replay found zero TeX errors, undefined references,
  multiply-defined labels, duplicate destinations, overfull boxes, or rerun
  requests. One underfull diagnostic remains.
- PDF replay found 1,164 named destinations and 311 internal GoTo actions.
  All 311 resolve. The earlier visible editor-note `0` defect was repaired at
  its VII source while preserving the visible note number.
- Final visual review is active and includes physical page 74 plus terminal
  pages 204-211.

This is now a coherent complete-body build, but no immutable privacy-clean
release projection, manifest, independent release seal, or archive handoff
exists at this observation boundary. The producer tree remains live. Body
publication therefore waits for the promised sealed boundary.

## Claude SGA6 cold source audit

Local root name: `sga6_full_audit_20260703`.

The recovered audit has advanced to `CERT_LOG.md` entry `#1334`, cold
re-verification of `idx582`, with `idx583` next.

- French workpass TeX: 1,320,450 bytes, SHA-256
  `7330A42E74AD3AAA53A69CE142FE34B5589ED6DB903586BA58D0450F1109D42C`.
- Current reader: 373 pages / 2,871,619 bytes, SHA-256
  `EA3E57440D05182D32DC290FFBC6BC80BBBB04D17C8DAC4443472519D4A14035`.
- `CERT_LOG.md`: 10,811,643 bytes, SHA-256
  `9BA317F1657E930236BF60C1BA815E378F40805CD422C4BDE063F863F874D2C5`.
- Entry `#1333` / `idx581` records a real source-backed correction in the
  Section 7.10 prism: terminal punctuation was changed from a comma to the
  source period.
- Entry `#1334` / `idx582` records a clean page after decisive diagram zoom
  review. It confirms the inverse-image square and leaves the TeX/PDF baseline
  unchanged.
- The next page, `idx583`, contains two further diagrams and the opening of
  Section 7.11.

The audit is live and intentionally page-by-page. It has no current release
handoff or sealed crop selection. The post-cutoff work is queued for the next
privacy-clean source-rescribe or rights-curated crop successor; live mutable
files are not mirrored as if frozen.

## Disposition

- GitHub action: publish this metadata-only custody snapshot and logbook entry.
- Zenodo action: none.
- SGA3 VII: publish only after its immutable release controls and independent
  seal exist.
- SGA6: preserve the `idx582` recovery cursor and include all later sealed
  Claude output in the next same-concept successor.
- No duplicate concept, second successor, or competing draft is authorized.

This snapshot does not certify complete SGA3, whole-SGA6 source fidelity,
mathematical correctness, underlying-work rights, accessibility, or critical
edition status.

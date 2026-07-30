# SGA 7 I high-detail source-audit visual evidence

This package preserves the recent high-detail source crops that were actually
opened during the SGA 7 Tome I transcription and diagram review. It does not
publish page screenshots of a zoomable PDF.

## Public image archive

`10x_SGA7I_SourceAudit_Opened_Targeted_Crops_20260730.zip` contains 12
deduplicated targeted crops / 1,339,226 image bytes from six parent pages.
They cover Exposes I, VI, and IX and include diagram edges, arrow labels,
exact-sequence rows, and ambiguous symbol details. The recovered generation
scales range from 5,200 to 9,000. Every crop was opened after the generation
time of its current bytes.

The archive does not include whole-page or near-whole-page renders. Fourteen
opened page-like images, together with routine bands and generated-but-unread
images, are metadata-only.

## Metadata archive

`10y_SGA7I_SourceAudit_Visual_Provenance_RightsBlocked_Metadata_20260730.zip`
describes the complete selected scratch surface:

- 14,896 image instances / 946,591,632 bytes;
- 14,744 unique images / 865,700,946 bytes;
- 152 duplicate aliases / 80,890,686 avoidable duplicate bytes;
- 32 current-byte images with exact session read events;
- 12 opened targeted crops selected for the public image archive;
- 14,732 unique images whose pixels remain withheld.

The full index records image hashes and dimensions, parent-scan identity,
page and folio mappings, parent scan dimensions and effective DPI, linked TeX
identities, generator identities, read-event status, and publication
disposition. The 12 public crops additionally have exact command-backed page,
fractional bounding-box, and render-scale provenance.

## Parent and mapping

The controlling 540-page source reader is not bundled:

- bytes: 20,827,344;
- SHA-256: `9CD40FF06EB1E488AF385A56899D4F492492A06A1E2E3C0ED6876B82E3E3603F`.

For the main body, book folio is parent PDF index minus 11. Expose starts in
the parent are I=12, II=36, VI=43, VII=144, VIII=229, and IX=324. Physical
PDF page is the zero-based parent index plus one.

The superseded low-resolution 528-page scan, SHA-256
`17286B0F0BEC451068E0A5FA2C39E93DE28E7C1ECEE6739487CFAC11C03C8DAB`,
contributes no pixel to either public archive.

## Claim boundary

This is sparse provenance and QA evidence, not a replacement source scan,
translation release, transcription certification, mathematical certification,
complete SGA 7 reader, or critical edition. Expose IX was still a working
transcription at the inventory boundary. Computational enlargement does not
create optical detail absent from the parent scan.

See `RIGHTS_AND_PROVENANCE.md` and
`SGA7I_VISUAL_EVIDENCE_VALIDATION.json` before reuse.

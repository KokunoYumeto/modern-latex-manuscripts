# Concurrent Labels And OCR Handoff Snapshots

Date: 2026-06-28

This addendum records two workflow lessons from the Noether maintenance sweep around WebR252, CurrentR259, and parallel OCR/support handoffs.

## Release Labels Belong To Their Producing Lane

When multiple agents or web sessions work on the same author, bare release labels such as `R250`, `R252`, or `R259` must not be reused by local support packages unless those packages are actually the owning session's release.

Use names that encode both provenance and check target:

```text
Noether_LocalCodex_after_WebR252_<scope>_on_CurrentR259_YYYYMMDD.zip
```

This prevents three common failures:

- local support packets being mistaken for web releases;
- stale or superseded packages appearing current because their number is high;
- downstream indexers losing the relation between a support packet, the web drop it follows, and the cumulative branch it was checked against.

Legacy local files with misleading bare `R###` names should be quarantined or explicitly marked historical/do-not-upload. Public metadata should prefer corrected descriptive names and should not imply that every support package is a reader-facing release.

## Upload-Set Indexes Are Control Material

A small "current upload set" index can be more valuable than a large pile of ZIPs. It should record:

- the current base TeX or cumulative branch;
- corrected current package names;
- SHA256 checksums;
- whether each package applies a TeX patch or is no-patch support;
- legacy/do-not-use names;
- caveats such as low-DPI source witnesses, source conflicts, optional non-promoted variants, and stale queue traps.

Do not front every support package on Zenodo. Use the index to decide which packages belong in the next deliberate author rollup or replacement set.

## OCR Handoffs Are Locator Evidence

OCR or Marker-style handoff snapshots can be useful even when incomplete. They can provide:

- searchable page-batch text;
- heading or paper-start candidates;
- rough citation or boundary signals;
- source PDFs and scripts used to rebuild the snapshot.

But unless a page-specific source comparison promotes the text, such handoffs are not transcriptions, not translations, not reader editions, and not critical-edition evidence. They should be labelled as OCR/source-locator support.

For OCR handoffs, include:

- source PDF identity and page range;
- OCR engine/tool where known;
- whether page or paper boundaries are candidates or verified;
- coverage percentage or last processed page;
- scripts needed to rebuild the snapshot;
- explicit warning that OCR text cannot be pasted into the edition as authority.

## Source-Authority Conflicts

When two source witnesses disagree, a package should be allowed to promote no patch. For example, an original-publication witness and a collected-volume witness may differ in title-page order, author line, or editorial apparatus. The correct output is a source-policy decision, not an automatic "fix".

A good conflict package includes:

- both witness routes;
- the current branch disposition;
- an optional non-promoted variant, if useful;
- a clear statement that no TeX patch was promoted;
- the decision needed before later promotion.

## Public Wording

Use conservative labels:

- "current upload-set index";
- "source-route audit";
- "source-authority conflict";
- "OCR/source-locator handoff";
- "no promoted TeX patch";
- "support/provenance, not reader-facing edition".

Avoid:

- "complete";
- "critical";
- "certified";
- "source-closed";
- "finished translation";

unless a later human-reviewed source audit explicitly justifies those words.

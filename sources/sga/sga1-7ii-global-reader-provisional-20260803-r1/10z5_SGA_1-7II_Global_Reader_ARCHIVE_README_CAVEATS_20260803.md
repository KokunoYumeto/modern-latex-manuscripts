# SGA 1--7 II global reader: provisional archive checkpoint

## Archive identity

- Release identity: `SGA-GLOBAL-READER-PROVISIONAL-20260803-R1`
- Producer handoff identity: `SGA-GLOBAL-READER-PROVISIONAL-ARCHIVE-HANDOFF-20260803-R1`
- Transport acceptance: exact received byte state accepted into private archive custody; one separately derived privacy-clean public logbook projection was made.
- Received handoff control: 4,135 bytes, SHA-256 `6EB5B9256C24B77DAA9DDDA6B39C5294CBBF5C26F4883CAFEF2C82A75465E422`.
- Intended lineage: the existing SGA concept DOI `10.5281/zenodo.20410947`; no new concept is authorized.
- Status: **PROVISIONAL working checkpoint**, not a terminal reference-complete release.

Transport acceptance, Zenodo publication, and anonymous public readback are separate archive events. This file records transport acceptance and the public projection boundary; a publication receipt records the later record/DOI and readback identities.

## Exact scope

The reader concatenates the English reading order SGA 1, SGA 2, SGA 3, SGA 4, SGA 4½, SGA 5, SGA 6, SGA 7 I, and SGA 7 II:

- 9 immutable input readers;
- 4,185 PDF pages;
- 33,337 named destinations;
- 27,059 link annotations, consisting of 27,057 internal `GoTo` actions and 2 non-`GoTo` actions;
- 832 outline items, all resolving;
- zero missing destinations, destination-route mismatches, broken named actions, malformed internal actions, invalid outline destinations, or missing volume roots.

The supplied validation reports `PASS` with `errors: []`. The build evidence and input inventory agree on all nine input path/page pairs, and the nine input page counts sum to 4,185.

## Public byte projection and privacy transformation

The received PDF, validation JSON, build-evidence JSON, and input CSV are published byte-for-byte unchanged. Their exact received identities are in the adjacent self-excluding public manifest.

The received `LOGBOOK.md` is preserved unchanged in private custody at 19,948 bytes with SHA-256 `774DE83D1C70DF5BEB55AD7F98E5200D48CAF0F341E9D08C698C2E27DFC0622D`. Its public derivative is 19,992 bytes with SHA-256 `F17A35E2A7B828D23C16D058890EDB94215AFAAE5B4A8ABF5C1FD3484A31B806`. The sole transformation was four case-sensitive replacements of the project owner's personal name at received lines 5, 15, 70, and 128 with `the project owner` or the grammatically required possessive form. No decision, error, reversal, rationale, continuation instruction, or superseded generation was omitted or summarized.

Bounded privacy replay over the four text/data controls found:

- strict UTF-8 decoding: 4/4 pass;
- absolute local paths: 0;
- user-directory paths: 0;
- Codex-private/task identifiers: 0;
- emails: 0;
- credential markers: 0;
- CSV formula-like cells: 0.

The PDF was not rendered, OCRed, rebuilt, or recompiled. A byte and decoded-stream scan covered 5,919 streams and 91,446,070 decoded bytes, with zero user-directory paths, real multi-segment filesystem paths, Codex-private identifiers, task UUIDs, personal-name strings, emails, or credential patterns. A raw compressed-byte `sk-` coincidence was inspected at its exact offset and was non-text compressed data, not a credential. Independent PDF parsing found 4,185 pages, no encryption, and metadata limited to `/Producer: pypdf`.

## Mandatory caveats

- This is not an exhaustive terminal reference-v2 release.
- SGA 7 I and SGA 7 II do not yet have source-level exhaustive internal-reference graphs.
- SGA 6 R10 retains 1,492 destinations, while its visible-content/action delta against R6 remains under reconciliation.
- Cross-volume semantic links are not exhaustive.
- A reproducible cumulative TeX/source package remains open.
- Canonical French, FAC, and GAGA work are separate ongoing obligations.
- This checkpoint makes no mathematical certification, editorial certification, peer-review, critical-edition, accessibility-certification, or project-completion claim.

## Rights

This archive update grants no new license over the underlying French editions or scans. No French scans are included. The package preserves the English working reader, navigation evidence, input identities, and decision history under the existing record's `notspecified` license state. Rights in underlying source editions remain with their respective holders.

## Supersession

This checkpoint supersedes only the unpublished cumulative `build_baseline` reader and unpublished `build_navigation_r2` reader identified by the producer. It does not supersede any standalone reader, any previously published SGA record, or the separately continuing source/reference work. The complete predecessor lineage remains preserved through Zenodo versioning.

## Provenance-logbook control

The privacy-clean logbook is a first-class direct public file, not merely a ZIP member. The standing archive control requires this exact public logbook state to be carried on both the methodology DOI `10.5281/zenodo.21124403` and replication DOI `10.5281/zenodo.20461174`. This handoff authorizes the existing SGA concept only, so this SGA publication does not itself discharge that separate dual-DOI obligation; the exact 19,992-byte/SHA-256 identity above remains queued for the next authorized dual-DOI provenance successor.

## Package organization

Seven files are public directly: the reader, validation, build evidence, input inventory, privacy-clean logbook, this archive README, and the self-excluding public manifest. The companion ZIP contains those same seven exact public bytes for one-file transport. Distinct content is not deduplicated away; the ZIP is an additional transport container.

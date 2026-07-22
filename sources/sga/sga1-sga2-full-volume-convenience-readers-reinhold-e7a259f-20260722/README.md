# SGA 1 and SGA 2 full-volume convenience readers

This package supplies the conspicuous full-volume PDF reading surfaces that
were missing from the SGA Zenodo record. It renders every SGA 1 and SGA 2
Markdown chapter in Jacob Reinhold's public `jcreinhold/sga` repository at the
exact snapshot below.

"Full-volume" here describes the extent of the pinned upstream Markdown. It
does not certify completeness against the French source or promote these PDFs
to source authority.

## Readers

| Reader | Upstream extent | Pages | Bytes | SHA-256 |
| --- | --- | ---: | ---: | --- |
| `00_SGA1_English_FullVolume_ConvenienceReader_Reinhold_e7a259f_20260722.pdf` | SGA 1 Exposes I-XIII and index of notation | 286 | 1,311,405 | `BDFB3D8F869617B5F50890E067E4B80BA4ED6946C8655B38B1D83506EF843536` |
| `00_SGA2_English_FullVolume_ConvenienceReader_Reinhold_e7a259f_20260722.pdf` | SGA 2 Exposes I-XIV, glossary, and indexes | 200 | 864,526 | `ADBCFBA39C42088545E7AEE7D61787841221B2315D7ADE69727093AA11E8CBE3` |

The first page of each PDF is a reader notice stating the source, attribution,
license, and claim limits. The generated TeX files are included as the durable
editable reading surface.

## Status and precedence

These are convenience renderings of an LLM-generated English translation.
They are not:

- corrected French source authority;
- independently source-audited translations;
- mathematical certification or human peer review;
- critical editions; or
- a determination of rights in the underlying French text.

The archive's separately named source-audited or source-aligned SGA 1 and SGA
2 checkpoints take precedence for every range they cover. Those checkpoints
remain preserved alongside these readers.

## Attribution and rights

English translation contribution:

- Jacob Reinhold, *SGA - English translation*
- upstream: <https://github.com/jcreinhold/sga>
- exact snapshot: `e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e`
- license for Reinhold's English translation contribution: CC BY 4.0

The exact upstream `LICENSE` and a complete tracked-file snapshot are in
`provenance/`. The underlying French material remains subject to its own
rights. Interlanguage generated the PDF presentation and pagination; it does
not claim authorship of Reinhold's English wording.

## Package map

- `00_*.pdf`: immediately readable full-volume convenience readers.
- `source/`: generated editable TeX used for the PDFs.
- `provenance/`: exact upstream license and commit-pinned source snapshot.
- `qa/`: reviewed representative-page contact sheets and the repaired SGA 2
  diagram page.
- `SGA1_READER_NOTICE.md`, `SGA2_READER_NOTICE.md`: notice text embedded in
  the PDFs.
- `BUILD_AND_QA.md`: build, static inspection, text, privacy, and visual QA.
- `SHA256SUMS.csv`: exact self-excluding inventory of this directory.

## Accessibility

Both PDFs are searchable and use embedded, subset, Unicode-mapped fonts, but
they are untagged and have no XMP metadata stream. The generated TeX is the
durable accessible text source. PDF text extractors may render some ligatures
imperfectly even when the visible page is correct.

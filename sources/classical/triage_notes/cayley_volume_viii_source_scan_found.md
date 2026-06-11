# Cayley Volume VIII Source Scan Located

A local public source scan for Arthur Cayley's collected papers, Volume VIII, has been located and preserved here. The modern LaTeX reader for Volume VIII is still pending.

- Pages: 640
- Bytes: 45622978
- SHA-256: 57a89fb28684fe60870316578fe76e41958aeb5369e8f0490632a5db5dbdf97c

Use this scan as the source witness for the next Cayley Volume VIII TeX pass.

## Follow-up Triage Note

# Follow-up findings: Vol VIII, Landau, Sylvester

## Cayley Vol VIII — scan source IS local, just not typeset

`<local-user-home>\Documents\Papors\OS\Cayley\collmathpapers08caylrich.pdf`
**640 pages, 45 MB**, Internet Archive scan, English (standard Cayley
title page confirmed).

The Cayley source-scan folder uses two naming conventions:
- `collectedmathema00..11cayluoft.pdf` (vols 0, 1, 2, 4, 5, 6, 7, 9, 10, 11)
- `collmathpapers03..13caylrich.pdf` (vols 3, 8, 12, 13)

Both sets together cover **all 14 volumes**, including 8. My earlier
search missed the `caylrich` naming convention. Updated finding:

**The scan PDFs are complete; only the machine-assisted transcription LaTeX typesetting work
skipped Vol VIII.** Action options:

1. **Quick (recommended now):** ship the Vol VIII scan PDF as
   `Cayley_Collected_Mathematical_Papers_Vol_VIII_source_scan.pdf` on
   GitHub/Zenodo so the volume "exists" in the corpus, with a note
   that modern-LaTeX typesetting is pending.
2. **Slow:** queue Vol VIII for the next machine-assisted transcription typesetting batch.
3. **Both:** ship the scan now, replace with clean TeX-built version
   when machine-assisted transcription catches up.

## Landau — answer is "translated, not native English"

Edmund Landau wrote in German. **But** the famous "Elementare
Zahlentheorie" (1927) was translated to English by Jacob E. Goodman
(with exercises by Bateman & Kohlbecker, Chelsea, 1958/1966) as
**"Elementary Number Theory"**.

A clean 255-page typeset PDF of that English translation exists locally:
`...\archives_extracted\depth_0\A00010_..._machine-assisted transcription_batch_processed_salvage.zip--.../machine-assisted transcription_batch_processed_salvage/03_combined_corpus_pdfs/03-landau-elementary-nt_FULL.pdf`

- 255 pages, 1.8 MB
- 0 leaks (clean render)
- Body text is in English
- **Not yet in the GitHub mirror or Zenodo**

There are already 9 Landau PDFs in the Zenodo main-landing cache —
`Lectures on Number Theory I/II/III`, `Distribution of Prime Numbers
I/II`, `Algebraic Numbers and Ideals`, `Analytic and Geometric Number
Theory` — but **all of those have German body content despite English
titles** (same pattern as the Riemann "Selected Papers"). Render-wise
they're clean (0 leaks), but they're not English-language content.

So for the "English-language Landau" lane:
- Add `Landau - Elementary Number Theory (Goodman trans.)` from the
  salvage corpus → instant 255-page English reader.
- (Optional) Retitle the 9 German-body PDFs to flag them as
  German-original so the shelf doesn't mislead.

## Sylvester — English-native, scan PDFs exist, not yet processed

`<local-user-home>\Documents\Papors\OS\J. J. Sylvester, collected papers\collectedmathem01sylvrich.pdf`
**676 pages, 43 MB** scan of "The Collected Mathematical Papers of
James Joseph Sylvester, Volume I" (Cambridge Univ Press). Plus
`<local-user-home>\Documents\Papors\OS\collectedmathema04sylvuoft.pdf`
(Vol IV scan).

Sylvester wrote in English. Same setup as Cayley:
- Scan PDFs are local for at least vols 1 and 4
- No machine-assisted transcription LaTeX typesetting work has been done for him
- He's not currently in the GitHub mirror at all

For now: at minimum, drop the scan PDFs into the classical shelf as
`Sylvester - Collected Mathematical Papers, Volume I (source scan)`.
Add LaTeX typesetting to the machine-assisted transcription queue.

## Other English-native candidates spotted in OS folder

Not exhaustive, but quick wins seen:
- "Grassmann - A New Branch of Mathematics: The Ausdehnungslehre of
  1844, and Other Works" (English translation collection)
- Various Deligne collected papers (mostly French/English mix)
- Kummer's "Collected Papers Volume 1, Contributions to Number Theory"
  (Weil ed., English)

## Suggested actions for local archive tooling

1. Drop Cayley Vol VIII scan PDF into the classical shelf upload
   alongside the 13 clean per-volume PDFs from earlier.
2. Drop the Landau Goodman translation PDF into the classical shelf as
   the first true English-language Landau.
3. Drop Sylvester Vol I and Vol IV scan PDFs into the classical shelf
   as the first Sylvester entries. Mark as "source scan; modern LaTeX
   typesetting pending."

All three additions are zero-leak, ready files.

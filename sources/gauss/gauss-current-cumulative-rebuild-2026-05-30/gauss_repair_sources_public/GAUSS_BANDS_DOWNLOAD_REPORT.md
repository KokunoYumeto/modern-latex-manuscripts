# Gauss Werke band download report

Date: 2026-05-29

## Found and downloaded from Internet Archive

| Band | IA identifier | Local file | Pages | Bytes |
|---|---|---|---|---|
| **VIII** (1900, Algebra/Arithmetic/Analysis Nachlass) | `werkecarlf08gauscfga` | `werkecarlf08gauscfga.pdf` | 460 | 14 MB |
| **X.2.1** (Bachmann — Über Gauss' Zahlentheoretische Arbeiten, Heft 1, 1911) | `s2p1werkehrsgvon10gausuoft` | `s2p1werkehrsgvon10gausuoft.pdf` | 182 | 9 MB |
| **X.2.4** (Stäckel — Gauss als Geometer, Heft 5, 1917) | `s2p4werkehrsgvon10gausuoft` | `s2p4werkehrsgvon10gausuoft.pdf` | 136 | 7 MB |

## Not on Internet Archive

The following Bände are NOT on IA based on systematic probing of identifier patterns (`werkecarlf*gausrich`, `werkehrsgvonderg*gausuoft`, `s2p*werkehrsgvon10gausuoft`, `p1werkehrsgvon*gausuoft`, etc.):

- **Band IX** (Geodesy, 1903)
- **Band X parts 2, 3, 5, 6, 7** (biographical essays Hefte by Brendel, Galle, Schlesinger, etc.)
- **Band X Abteilung 2** (supplementary volume)
- **Band XI Part II** (supplementary essays — have Part I locally already)
- **Band XII** (1929, final Nachlass)

## Alternative sources to try (not attempted in this run)

- **Göttinger Digitalisierungszentrum**: `https://gdz.sub.uni-goettingen.de/` — has the complete Gauss-Werke including all Bände. May require manual navigation.
- **HathiTrust**: `https://catalog.hathitrust.org/Search/Home?lookfor=Gauss+Werke&type=all` — some Bände may be available
- **BSB Munich (Bayerische Staatsbibliothek)**: `https://www.bsb-muenchen.de/` — German collected works often available
- **Wikisource**: German Wikisource has some Gauss texts

These alternatives are recommended for any future fetch attempts.

## Status

Source-scan coverage for Gauss is now:
- ✅ Bands I, II, III, IV, V, VI, VII, VIII, XI Part I, two essays from X
- ❌ Band IX, Band X (most parts), Band XI Part II, Band XII

For corpus completeness, the cumulative Gauss work in `gauss_cumulative_for_codex/` operates on Bands I-VII, VIII (new), XI Pt I — all the published earlier source draft-typeset bands plus the v2 fixes. The missing scans listed above are not currently needed for fix work because no earlier source draft-typeset versions of those bands exist either.

---

## Update 2026-05-30: missing bands acquired from GDZ Göttingen

The Göttinger Digitalisierungszentrum hosts the full Gesammelte mathematische Werke (parent PPN23569441X). Per-band PPN identifiers were located via Wikisource's Carl Friedrich Gauß page; the GDZ direct-PDF URL pattern is

```
https://gdz.sub.uni-goettingen.de/download/pdf/<PPN>/<PPN>.pdf
```

All six missing bands were fetched with `curl -L` (server returns `Content-Type: application/pdf`; verified with `file` and `pdfinfo`) and stored in `gauss_v2_fixes/scans/`.

| Band | Title (GDZ) | Year | PPN | Local file | Pages | Bytes |
|---|---|---|---|---|---|---|
| **IX** | Geodäsie. Fortsetzung von Band 4 | 1903 | PPN23601515X | `scans/gauss_werke_band_ix.pdf` | 537 | 26,325,973 |
| **X Abt. 1** | Nachtraege zur reinen Mathematik | 1917 | PPN236018647 | `scans/gauss_werke_band_x_abt_1.pdf` | 617 | 31,251,025 |
| **X Abt. 2** | Abhandlungen ueber Gauss' wissenschaftliche Taetigkeit auf den Gebieten der reinen Mathematik und Mechanik | 1922–1933 | PPN236019856 | `scans/gauss_werke_band_x_abt_2.pdf` | 701 | 61,177,226 |
| **XI Abt. 1** | Nachtraege zur Physik, Chronologie und Astronomie | 1927 | PPN236020595 | `scans/gauss_werke_band_xi_abt_1.pdf` | 524 | 30,787,008 |
| **XI Abt. 2** | Abhandlungen ueber Gauss' wissenschaftliche Taetigkeit auf den Gebieten der Geodaesie, Physik und Astronomie | 1924–1929 | PPN236059505 | `scans/gauss_werke_band_xi_abt_2.pdf` | 660 | 60,654,915 |
| **XII** | Varia. Atlas des Erdmagnetismus | 1929 | PPN236060120 | `scans/gauss_werke_band_xii.pdf` | 450 | 39,877,326 |

Total: 6 bands, ~3,489 pages, ~250 MB. All bands now have a true source-scan PDF on local disk; this completes the source-scan coverage of all 12 Bände (the 1863 Werke I–VIII via Internet Archive, the post-1900 Werke IX–XII via GDZ Göttingen).

Note on naming: the earlier `band_xi_pt_i_RECOVERED.pdf` in the parent directory is a 5-page LaTeX retypeset of three recovered passages, NOT the source scan. `scans/gauss_werke_band_xi_abt_1.pdf` is the new full 524-page source scan for Band XI Abt. 1.

### Method notes (so the next agent can repeat this)

1. Locate the PPN for each Band on `https://de.wikisource.org/wiki/Carl_Friedrich_Gauß` (Wikisource lists the GDZ TOC links for every Band).
2. For the full-volume PDF, use `https://gdz.sub.uni-goettingen.de/download/pdf/<PPN>/<PPN>.pdf`. For individual chapters/Hefte, the alternate pattern is `https://gdz.sub.uni-goettingen.de/download/pdf/<PPN>/LOG_<NNNN>.pdf` (LOG IDs come from the METS XML at `https://gdz.sub.uni-goettingen.de/mets/<PPN>.xml`).
3. The naive pattern `https://gdz.sub.uni-goettingen.de/download/pdf/<PPN>.pdf` 301-redirects into a 500; do not use it.
4. The web viewer at `https://gdz.sub.uni-goettingen.de/id/<PPN>` is the TIFY single-page JS viewer; scraping it for PDF links yields nothing useful. Skip directly to the `/download/pdf/` endpoint.

# Carl Friedrich Gauss, Works, Volume VIII

## Supplements to Volumes I–IV · English edition

The English reader contains the historical title pages and portrait, all nine divisions, the volume remarks, errata, contents, and publisher’s advertisement. The divisions cover arithmetic and algebra, analysis and the theory of functions, numerical calculation, probability, foundations of geometry, Geometria Situs, elementary geometry, complex quantities in geometry, and the theory of curved surfaces. The supplements to Volume IV cover its non-geodetic material.

The editable source includes the text, formulas, tables, and drawings in LaTeX, together with the portrait image. The drawings use editable paths and labels. The contents and textual references retain the historical page numbers. The reader’s own folios run continuously, with bookmarks and named destinations for the source leaves. The historical errata appear separately from the original statements.

## Sources and credits

Carl Friedrich Gauss, *Werke. Achter Band*, edited by the Royal Society of Sciences at Göttingen and distributed on commission by B. G. Teubner in Leipzig, 1900. The Göttingen colophon credits the Dieterichschen Univ.-Buchdruckerei (W. Fr. Kaestner). The primary digitization and portrait are from the Niedersächsische Staats- und Universitätsbibliothek Göttingen. [Göttingen digitization and portrait](https://gdz.sub.uni-goettingen.de/id/PPN236010751)

F. Klein’s signed notice credits Fricke with arithmetic, algebra, and analysis, Börsch and Krüger with numerical calculation and probability, Stäckel with geometry, Weingarten with the note on developing surfaces, and Brendel with general editing. Schering left preparatory work, chiefly copies of Gauss’s papers and correspondence.

The Göttingen scan cuts off the right-hand portion of historical page 95 (source leaf 102). The alternative photograph on Kyushu canvas 52 supplies the missing text, formulas, and Fricke signature. The physical relationship of the photographed copies remains unestablished. The Kyushu manifest marks its digitized item **Public Domain** and gives the attribution **Kyushu University Library Collections**. [Kyushu catalogue](https://hdl.handle.net/2324/410995) · [Canvas 52](https://catalog.lib.kyushu-u.ac.jp/image/410995/canvas/p52) · [Rights and attribution](https://catalog.lib.kyushu-u.ac.jp/image/manifest/1/820/410995.json)

OpenAI GPT-6 Astra (Ultra) produced the underlying AI transcription and editable drawings in 2026. OpenAI GPT-6.1 Sol (Ultra) AI-translated the English edition in 2026. The source transcription is `Gauss_Werke_Band_VIII_LaTeX.zip`, SHA-256 `308f50749cdbf971f447662cb6a3ea41f8db2e1c7cac16673ab148a5eaeb2ef0`.

## Build the reader

Use Python 3.10 or later, XeLaTeX, and the LaTeX packages `amsmath`, `amssymb`, `babel` with English support, `booktabs`, `calc`, `fontspec`, `geometry`, `graphicx`, `hyperref`, `microtype`, `multirow`, `needspace`, and TikZ/PGF. Install the Latin Modern OpenType fonts, including `lmromancaps10-regular.otf`, through your TeX distribution. The Cyrillic font declarations require a local installation of Times New Roman visible to XeLaTeX. Install the fonts separately.

Run these commands in the extracted source directory.

```sh
python -m pip install PyMuPDF fonttools
python build_volume.py --output build/Gauss_Werke_VIII_English.pdf
```

The script follows `volume.json`, runs XeLaTeX twice per component, and assembles the reader with continuous folios. It then applies the PDF text mapping for mathematical delimiter characters. Use `--xelatex` if the executable has a different location. The component PDFs and logs are written beside the finished reader in a separate build directory.

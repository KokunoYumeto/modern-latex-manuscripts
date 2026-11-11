# Carl Friedrich Gauss, Werke, Band VIII

## Nachträge zu den Bänden I–IV · Deutsche Ausgabe

Die deutsche Ausgabe enthält die historischen Titelblätter und das Porträt, alle neun Abteilungen, die Bemerkungen zum Band, die Berichtigungen, das Inhaltsverzeichnis und die Verlagsanzeige. Die Abteilungen umfassen Arithmetik und Algebra, Analysis und Funktionentheorie, numerisches Rechnen, Wahrscheinlichkeitsrechnung, Grundlagen der Geometrie, Geometria Situs, elementare Geometrie, komplexe Größen in der Geometrie und die Theorie der krummen Flächen. Die Nachträge zum vierten Band betreffen dessen nichtgeodätischen Teil.

Das LaTeX-Paket enthält den bearbeitbaren Text, die Formeln, Tabellen und Zeichnungen sowie das Porträt. Die Zeichnungen bestehen aus bearbeitbaren Pfaden und Beschriftungen. Das Inhaltsverzeichnis und die Verweise im Text behalten die historischen Seitenzahlen. Der neu gesetzte Lesetext hat eine fortlaufende Seitenzählung, Lesezeichen und Sprungziele für die Vorlagenblätter. Die historischen Berichtigungen stehen gesondert von den ursprünglichen Aussagen.

## Quellen und Mitwirkende

Carl Friedrich Gauss, *Werke. Achter Band*, herausgegeben von der Königlichen Gesellschaft der Wissenschaften zu Göttingen, 1900, in Kommission bei B. G. Teubner in Leipzig. Der Göttinger Druckvermerk nennt die Dieterichsche Univ.-Buchdruckerei (W. Fr. Kaestner). Die historische Ausgabe folgt dem Exemplar der Niedersächsischen Staats- und Universitätsbibliothek Göttingen. [Göttinger Digitalisat](https://gdz.sub.uni-goettingen.de/id/PPN236010751)

Die Titelvignette zeigt dasselbe historische Motiv nach dem [zweiten Abdruck der Werke I von 1870](https://commons.wikimedia.org/w/index.php?oldid=1179960952), digitalisiert nach dem Exemplar der University of California Libraries. [Public Domain Mark 1.0](https://creativecommons.org/publicdomain/mark/1.0/).

Die von F. Klein unterzeichneten Bemerkungen nennen Fricke für Arithmetik, Algebra und Analysis, Börsch und Krüger für numerisches Rechnen und Wahrscheinlichkeitsrechnung, Stäckel für die geometrischen Abteilungen, Weingarten für die Notiz zur Abwicklung der Flächen und Brendel für die allgemeine Redaktion. Schering hinterließ Vorarbeiten, hauptsächlich Abschriften aus dem Nachlass und dem Briefwechsel.

Im Göttinger Scan fehlt der rechte Teil der historischen Seite 95 (Vorlagenblatt 102). Die alternative Aufnahme auf Blatt 52 im Kyushu-Digitalisat liefert den fehlenden Text, die Formeln und Frickes Unterschrift. Das Verhältnis der fotografierten Exemplare zueinander ist ungeklärt. Das Kyushu-Manifest kennzeichnet das eigene Digitalisat als **Public Domain** und nennt **Kyushu University Library Collections** als Quellenangabe. [Kyushu-Katalog](https://hdl.handle.net/2324/410995) · [Aufnahme auf Blatt 52](https://catalog.lib.kyushu-u.ac.jp/image/410995/canvas/p52) · [Rechteangabe und Quellenvermerk](https://catalog.lib.kyushu-u.ac.jp/image/manifest/1/820/410995.json)

Die zugrunde liegende LaTeX-Transkription und die bearbeitbaren Zeichnungen wurden 2026 mit OpenAI GPT-6 Astra (Ultra) von KI erstellt. Die deutsche Fassung wurde 2026 mit OpenAI GPT-6.1 Sol (Ultra) KI-übersetzt und sprachlich modernisiert. Grundlage ist `Gauss_Werke_Band_VIII_LaTeX.zip` mit der SHA-256-Prüfsumme `308f50749cdbf971f447662cb6a3ea41f8db2e1c7cac16673ab148a5eaeb2ef0`.

## Lesetext setzen

Erforderlich sind Python ab Version 3.10, XeLaTeX und die LaTeX-Pakete `amsmath`, `amssymb`, `babel` mit deutschen Sprachdaten (`ngerman`), `booktabs`, `calc`, `fontspec`, `geometry`, `graphicx`, `hyperref`, `microtype`, `multirow`, `needspace` und TikZ/PGF. Die OpenType-Schriften von Latin Modern einschließlich `lmromancaps10-regular.otf` lassen sich über die TeX-Distribution installieren. Die kyrillischen Schriftdefinitionen benötigen eine lokale, für XeLaTeX erkennbare Installation von Liberation Serif (SIL Open Font License 1.1). Installieren Sie die Schriften separat.

Führen Sie im entpackten Quellverzeichnis diese Befehle aus.

```sh
python -m pip install PyMuPDF fonttools
python build_volume.py --output build/Gauss_Werke_VIII_Deutsch.pdf
```

Das Skript folgt der Reihenfolge in `volume.json`, führt für jeden Teil zwei XeLaTeX-Durchläufe aus und setzt den Lesetext mit fortlaufender Seitenzählung zusammen. Anschließend ergänzt es die PDF-Textzuordnung für mathematische Klammerzeichen. Mit `--xelatex` lässt sich der Pfad zum Programm angeben. Die Teil-PDFs und Protokolle stehen in einem eigenen Arbeitsverzeichnis neben dem fertigen Lesetext.

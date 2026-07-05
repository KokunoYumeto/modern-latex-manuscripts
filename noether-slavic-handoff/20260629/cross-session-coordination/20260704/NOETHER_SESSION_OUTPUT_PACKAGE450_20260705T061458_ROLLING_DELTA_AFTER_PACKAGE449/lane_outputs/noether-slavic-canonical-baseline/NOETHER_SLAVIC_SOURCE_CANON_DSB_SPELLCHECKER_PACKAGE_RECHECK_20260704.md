# Noether Slavic Source-Canon Lower Sorbian Spellchecker Package Recheck - 2026-07-04

Scope: source-canon-first Lower Sorbian recheck for public source-package/lexicon evidence. This pass caches the Sorbian Institute spelling-dictionary page plus the 20241212 Hunspell OXT/ZIP packages and extracted metadata.

Boundary: source-package provenance only. The package strengthens Lower Sorbian lexicon/body evidence and includes mathematics-terminology provenance, but it is not the WITAJ mathematics terminology booklet, not a mathematical publication, and not a qualified review.

## Summary

* Rows: 1
* Package owner signal: Sorbian Institute publisher metadata in `description.xml`.
* Mathematics signal: public page states the 2018 version incorporated WITAJ 2016 mathematics terminology.
* License signal: OXT package contains GPLv3 `license.txt`; no blanket license clearance is claimed.
* Rebuild trigger: none.

| row_id | page_sha256 | oxt_sha256 | zip_sha256 | sample_rows | decision |
|---|---|---|---|---:|---|
| dsb_sorbian_institute_hunspell_math_lexicon_package_20241212 | 20E1628FD66B1BC8AD5C5459277F2F14F0978A5E1E2D959767CC9B9A18BFCC25 | EFC1E3D3C9BF405F7D1036F4A78971A58DD06B4AD65AD0E9A1648BE8CA95E614 | 9DFF2A52BE8C17012AF42E70C4CFFCFDA82ED3FB43563E8E7CD1819B6CDEB0E2 | 55 | source_package_provenance_strengthened_no_reader_or_translation_promotion |

## Evidence Lines

- Mathematics-source inclusion: `line 15: <P>Die erste Version der Rechtschreibkontrolle (veröffentlicht am 06.04.2016) basierte im Wesentlichen auf den Sprachdaten des Deutsch-Niedersorbischen Wörterbuchs (M. Starosta, E. Hannusch, H. Bartels, 2003-2018). Die zweite Version (22.03.2018) wurde um das Material des Niedersorbisch-deutschen Wörterbuchs (M. Starosta, 1999) und zusätzlich um die Terminologie im Fach Mathematik (WITAJ Sprachzentrum, 2016) erweitert. Die dritte Version (17.09.2018) wurde mit Eigennamen ergänzt; hauptsächlich aus dem Wörterbuch der nieder-wendischen Sprache und ihrer Dialekte (E. Mucke, 1911-1928), zusätzlich auch aus weiteren alten Wörterbüchern (B. Šwjela, 1961 und J. G. Zwahr, 1847) sowie aus anderen Quellen (T. Meškank, Serbske pśedmjena; Material von der Niedersorbischen/Wendischen Sprachkommission). Seit 20.02.2019 werden die neuen Regeln zur Schreibung des Buchstabens »ŕ« berücksichtigt. Die vierte Version (09.12.2019) umfasst zusätzlich neues, bisher nicht veröffentlichtes Material des Deutsch-Niedersorbischen Wörterbuchs (M. Starosta, E. Hannusch, H. Bartels, 2003-2019). Die fünfte Version (24.02.2021) wurde um den im Rahmen des <A href="https://www.serbski-institut.de/de/Staendiges-Monitoring-des-obersorbischen-und-niedersorbischen-Schrifttums/">Monitorings des niedersorbischen Schrifttums</A> 2019 bearbeiteten Wortschatz, als auch um bisher nicht enthaltene Wörter aus den von der Arbeitsstelle für sorbische/wendische Bildungsentwicklung bzw. vom Sprachzentrum WITAJ herausgegebenen Fachterminologien (für die Fächer: Computer und Internet 2004, Ethik-Religionskunde 2014, Zeichnen 2009, Musik 2006, Sachkunde 2011, Sport 2003, Geschichte 2010) erweitert. Sowohl die Datenbasis als auch der Funktionsumfang sollen in Zukunft erweitert werden. Die sechste Version (17.01.2022) wurde mit den noch fehlenden niedersorbischen Exonymen aus Sachsen ergänzt. Die aktuelle Version (12.12.2024) erkennt die reduzierten adjektivischen Endungen an. Sowohl die Datenbasis als auch der Funktionsumfang sollen in Zukunft erweitert werden.</P>`
- Hunspell/open-format statement: `line 76: <P>Laden Sie die <A href="/media/ortografija/dict-dsb-de-20241212.zip">ZIP-Datei</A> herunter und entpacken Sie das hunspell-Wörterbuch (die Dateien dsb-DE.aff und dsb-DE.dic) nach den Ordner Library/Spelling/ in Ihrem Home-Ordner. (Für die Lösung bedanken wir uns bei Martin Ballaschk.)</P>`
- License signal: `line 1: GNU GENERAL PUBLIC LICENSE`

## Decision

The Lower Sorbian row is strengthened from catalog-only evidence to catalog plus public Sorbian Institute Hunspell source-package/lexicon evidence. The open blocker remains because this is not the WITAJ mathematics terminology booklet, does not provide definitions or reviewer authority, and does not by itself authorize translation or reader changes.

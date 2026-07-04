# Noether Slavic Underrepresented Branch Extension Scan

Scan time: 2026-07-04T06:29:26.5326683+02:00

Scope: Belarusian, Macedonian, and Sorbian extension coverage for the Slavic canonical baseline support lane.

Boundary: this scan does not alter Ukrainian, Russian, Interslavic Latin, or Interslavic Cyrillic canonical output. It shelves optional broad-Slavic support sources and does not claim external/native review completion.

## Decision

The previous `belarusian_macedonian_sorbian_math_controls` gap can be narrowed.

- Belarusian: candidate mathematical terminology controls were found and source-shelfed.
- Macedonian: candidate university textbook/lexicon controls were found and source-shelfed.
- Sorbian: institutional lexical and specialist-routing infrastructure was found, a math-specific Upper Sorbian terminology booklet was found bibliographically, and a 1996 math terminology booklet was found in the Sorbian Institute Upper Sorbian text-corpus source list; booklet/corpus content was not locally inspected.

New status: shelfed extension with Sorbian content-inspection residual. No rebuild trigger.

## Belarusian

Primary useful sources:

- `https://slounik.org/bnt01/`
- `https://knihi-online.com/russko-bielorusskij-matiematicieskij-slovar.html?page=2`
- `https://knihi-online.com/russko-bielorusskij-matiematicieskij-slovar.html?page=10`

Motivation:

The Slounik BNT page identifies a 1922 Belarusian mathematical terminology source prepared through the Mathematical Section of the Belarusian Scientific-Terminological Commission and the Institute of Belarusian Culture. It covers arithmetic, algebra, geometry, trigonometry, analytic geometry, and higher analysis.

The 1993 Russo-Belarusian mathematical dictionary gives modern-ish Belarusian mathematical dictionary context. Page 2 includes algebra families; page 10 includes ring-family vocabulary, including division ring, commutative ring, topological ring, and endomorphism ring. The host warns that the online text is OCR-generated and may be imperfect, so any accepted terminology mutation would require scan-level verification.

Lane role:

Use as optional Belarusian register context only. It can inform broad Slavic legibility review but cannot certify Noether terminology or trigger a rebuild by itself.

## Macedonian

Primary useful sources:

- `https://im-pmf.weebly.com/10591095107710731085108010941080.html`
- `https://www.ukim.edu.mk/dokumenti_m/567_E-kniga%20AnS%20final.pdf`
- `https://drive.google.com/file/d/1Brf89ljd87hw2KLl07--5F8j5z5w_OA3/view`

Motivation:

The Institute of Mathematics PMF/UKIM textbook catalog lists Macedonian algebra and mathematical reference works, including algebra problem collections, algebraic n-ary structures, linear algebra, and a 2021 mathematical lexicon. This is a stronger Macedonian routing anchor than the previous arXiv-only indirect coverage.

Lane role:

Use as optional Macedonian register context and reviewer-routing support. PDF access/inspection is required before using these as evidence for any accepted terminology mutation.

## Sorbian

Primary useful sources:

- `https://hornjoserbsce.de/dow/?r%C4%9Bc=de`
- `https://www.serbski-institut.de/digitales-woerterbuch-soblex-und-obersorbische-rechtschreibkontrolle-erweitert/`
- `https://www.domowina.de/en/resources/translators/`
- `https://domowina-verlag.de/assets/pdf/34_LND_Lieferbare-Literatur_2022.pdf`
- `https://www.serbski-institut.de/wp-content/uploads/2022/02/Z%CC%8Co%CC%81rla-hornjoserbskeho-tekstoweho-korpusa.pdf`
- `https://slavistik-portal.de/en/datenpool/sorbib-db.html?autor=Ku%C5%A1kec%2C+Lucija`

Motivation:

The Sorbian Institute DOW-online page documents an institutional Upper Sorbian dictionary resource. The Sorbian Institute soblex page documents current dictionary/spell-check infrastructure and vocabulary expansion. Domowina lists Upper/Lower Sorbian dictionaries, translation tools, and qualified translator contacts.

The Domowina-Verlag literature list records Katja Magerowa, `Terminologija za predmjet matematika` / `Terminologie fuer das Fach Mathematik`, Deutsch-Obersorbisch and Obersorbisch-Deutsch, 2008, 106 pages, ISBN `978-3-7420-1359-0`.

The Sorbian Institute Upper Sorbian text-corpus source list includes `Termmat` and records Lucija Kuscec, `Terminologija za predmjet matematika`, German-Upper Sorbian and Upper Sorbian-German, for elementary school, Budysin 1996.

The SorBib bibliography independently records the Lucija Kuskec 1996 `Terminologija za predmjet matematika` title as a 96-page Budysin publication.

Lane role:

This is now a math-specific Sorbian source-list/bibliographic control, plus useful infrastructure for finding vocabulary and reviewers if the Interslavic/Panslavic lane ever needs Sorbian-specific validation. The residual is content access/inspection: do not use these booklets for any accepted terminology mutation until the actual text is obtained, corpus access is available, or a qualified reviewer confirms the relevant terms.

Follow-on access audit:

- `NOETHER_SLAVIC_SORBIAN_MATH_SOURCE_ACCESS_AUDIT_20260704.md`
- `NOETHER_SLAVIC_SORBIAN_MATH_SOURCE_ACCESS_AUDIT_20260704.csv`

## Rebuild Boundary

No source in this scan is a rebuild trigger. A rebuild would require the existing canonical triggers: source inventory or Zenodo/source change, accepted reviewer correction, accepted terminology mutation, targeted render defect, or validation failure.

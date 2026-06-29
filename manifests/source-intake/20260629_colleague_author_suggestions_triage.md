# Colleague Author Suggestions - Source Intake Triage

Date: 2026-06-29

Purpose: quick triage of suggested authors/works for possible transcription, translation, source-audit, or reference packets. This is not a final bibliography. It records rough corpus size, translation saturation, source/reference availability, and project priority.

## Publication-Law Frame

The colleague asking is in the United States, so the practical publication triage here uses a US-first public-domain screen rather than an EU life-plus-70 screen. As of 2026, works registered or first published in the United States before 1931 are generally in the US public domain. For foreign works, this is not the whole story: the URAA restored US copyright in some foreign works that had previously fallen into the US public domain but were still protected in their source country on the restoration date, usually 1996. For this project, the practical rule is:

- **Clean public archive candidates:** pre-1931 US publications; clearly public-domain foreign editions; author/source cases where source-country and US status both look clear; or openly licensed source scans/texts.
- **Source/reference candidates:** modern or legally ambiguous works that are useful for deciding what to transcribe, translating terminology, or building Lean/formalization targets, but should not be mirrored as full text on Zenodo/GitHub without a separate decision.
- **Private workflow candidates:** copyright-heavy modern authors where the intellectual value is high but the public deliverable should be a bibliography, source map, commentary, formalization stub, or rights-cleared excerpt rather than a full scan/text republication.

This is a triage layer, not legal advice. It is meant to keep public-facing repository claims clean while still letting the project identify important mathematical gaps.

## Summary Table

| Author/work | Rough corpus size | Translation / transcription situation | Source/reference spine | Triage |
|---|---:|---|---|---|
| Sophus Lie | Large: collected papers planned as six paper volumes plus a seventh supplement; HathiTrust records 1922-1960 German/French collected edition. | Partial English translations exist for selected key papers/books, but the collected-paper corpus is not broadly available as modern English/TeX. | `Gesammelte Abhandlungen` on IA/Hathi; major books such as `Theorie der Transformationsgruppen`. | High value, large. Best as staged source-audit/translation packets by theme: transformation groups, contact transformations, differential equations. |
| W. K. Clifford | Small/medium: `Mathematical Papers` 1882, roughly 650 pp including appendix. | Already English. Translation not needed; modern TeX transcription would be the main value. | IA and University of Michigan Historical Math Collection. | Useful but lower priority unless doing Clifford algebra/geometric algebra, graph fragments, or English TeX benchmark. |
| Carl Friedrich Gauss | Huge: `Werke` 12 vols plus related/commentary material; many manuscripts/Nachlass items. | Some famous works translated, but much of the Werke/Nachlass is not easily available in English. | Göttingen, HathiTrust, IA; local Gauss lane already exists. | High priority already in project. Needs source-complete spine, paper-level queue, and targeted translation rather than whole-corpus brute force. |
| Leonhard Euler | Enormous: Euler Archive indexes 866 works; Opera Omnia is 81 vols in four series. | Many translations exist and Euler Archive tracks them, but far from universal. | Euler Archive / Opera Omnia / original scans. | Too large for one lane. Best use: targeted untranslated works, benchmark/reference links, and avoid duplicating Euler Archive work. |
| Apollonius | Medium but source-complex: `Conics` books I-IV Greek, V-VII Arabic transmission, VIII lost. | English I-IV exists in modern Green Lion/Taliaferro/Fried; I-VII translations exist but rights/status vary. Public-domain Heath is more commentary/treatise than full modern edition. | Heiberg-style Greek/Arabic editions, IA scans, modern secondary references. | High historical value, but diagram/source-language hard. Good future classical geometry packet, not first easy win. |
| Archimedes | Small/medium: compact ancient corpus; Heath 1897 covers most works, 1912 supplement covers `Method`. | Already public-domain English via Heath; modern Netz translation exists but copyrighted. | IA, Gutenberg/Heath, NYU Archimedes page, Heiberg source tradition. | Good clean TeX/diagram project; less translation novelty, more source/diagram benchmark value. |
| Takagi? | Ambiguous item from speech text `Tatami`; likely Teiji Takagi. Collected papers about 376 pp. | Copyright-heavy: Takagi died 1960; collected papers are modern Springer. | Springer/Cambridge references; Japanese/German original publication routes may exist but rights need caution. | Mathematically high-value for Noether/class-field context, but not public-domain-safe in EU until 2031. Treat as private reference/source-search only unless permissions/public-domain status is clear. |
| Alfred Tarski | Large modern corpus: collected papers 4 vols, over 2500 pp; also monographs. | Many key English translations exist, but Polish/German originals and geometry material remain interesting. | Birkhäuser collected papers, selected translations, geometry references. | Not main public archive target: modern copyright and author died 1983. Useful for Lean/formalization/reference, not open Zenodo transcription without rights. |
| Evariste Galois | Small: 1897 `Oeuvres mathematiques` is compact. | Peter Neumann gives systematic English translation, copyrighted; older French editions public domain. | IA 1897 Oeuvres, later critical editions, EMS/Neumann. | Very feasible and compact, but less novel because good modern English exists. Could make source-audited French TeX + pointer to existing translation. |
| Girard Desargues | Tiny/small but hard: `Brouillon project` and related perspective/conic texts. | Modern scholarly editions/translations exist but may be copyrighted; original old French is hard. | Original/old editions, Cambridge `Oeuvres de Desargues`, Hogendijk work, projective-geometry secondary literature. | High historical value and likely high novelty if source-audited. Good small but difficult classical geometry packet. |
| Jakob Steiner | Medium: `Gesammelte Werke` 2 vols, 1881-82. | German corpus; English translation coverage appears sparse. | IA/Google/Cambridge reprint; MacTutor references. | Strong candidate: manageable size, important synthetic geometry, public-domain source, diagram-heavy but not enormous. |
| Joseph Fourier | Medium: `Oeuvres de Fourier` 2 vols; `Theorie analytique de la chaleur` core work. | `Analytical Theory of Heat` has 1878 English translation; many shorter works less visible. | IA French Oeuvres, IA/Freeman 1878 English translation, Cambridge reprint references. | Good applied/math-physics target. Avoid duplicating the main Heat translation; target lesser papers or produce source-audited TeX. |
| Laplace | Huge: `Oeuvres completes` 14 vols. | Some classics translated, e.g. probability essay and parts of celestial mechanics; much remains French. | IA/Hathi/Barcelona/Gallica-style scans. | High value but very large. Better as themed packets: probability, celestial mechanics, analysis, not whole-corpus first. |
| Lagrange | Huge: `Oeuvres de Lagrange` 14 vols. | Some major works have translations; many memoirs remain French/Latin/Italian/German context. | IA, Hathi, EuDML tome access. | High value, large. Similar to Laplace: staged by theme, especially mechanics, calculus of variations, number theory. |
| Karl Weierstrass | Medium/large: `Mathematische Werke` 7 vols, 1894-1927. | German; English translation coverage limited. | IA, University of Michigan, JHU lecture references. | Strong candidate after Noether/Gauss: foundations of analysis, compact enough compared with Cauchy/Euler, likely useful. |
| Augustin-Louis Cauchy | Very huge: `Oeuvres completes`, 2 series, 27 vols. | Some famous works translated (`Cours d'analyse` etc.), but most papers are French and not TeXed/translated. | IA/Hathi/Gallica-style scans. | Important but enormous. Good long-term lane; start only with high-value subcorpora and strict source maps. |
| A. F. Möbius | Medium: `Gesammelte Werke` 4 vols, 1885-87. | German; scattered modern discussion, but not broadly translated as a corpus. | IA/Hathi/MDZ scans for `Gesammelte Werke`; astronomy/mechanics/geometric papers. | Strong candidate. Manageable public-domain corpus, historically important geometry/topology/mechanics, likely under-translated. |
| Gotthold Eisenstein | Small/medium: `Mathematische Werke` in 2 vols, late 19th-century collected edition. | German/Latin/French-adjacent number theory; not broadly available in modern English/TeX. | IA/Hathi/Google scans of `Mathematische Werke`; Crelle originals. | Very strong candidate. Compact, high-value number theory, and natural beside Gauss/Dirichlet. |
| Georg Cantor | Medium: `Gesammelte Abhandlungen` one major 1932 volume plus scattered original papers. | Some key English translations exist, especially set-theory classics; complete modern translation apparatus is not trivial and some editions are copyrighted. | IA/Hathi scans of original papers and collected works; Ewald/Dauben-style modern secondary references. | Useful but handle paper-by-paper. Good source-audited German TeX target; translation novelty varies by paper. |
| Kurt Gödel | Modern/copyright-heavy: `Collected Works` are late-20th-century Oxford volumes; originals include 1930s-1970s papers. | Many canonical English/German editions/translations exist in copyrighted collected works. | Oxford collected works; selected original journal scans where legal access exists. | Not an open-publication transcription lane by default. Good for Lean/formalization/reference thinking, but avoid Zenodo transcription/translation without rights clearance. |
| David Hilbert | Medium/large: `Gesammelte Abhandlungen` 3 vols, originally 1932, 1933, 1935; plus books/lectures. | Some classics translated, especially `Foundations of Geometry`; broad collected-paper TeX/translation coverage is not trivial. | IA/Gutenberg for `Grundlagen`/`Foundations`; collected works via IA/Hathi/Chelsea reprints/EuDML portions. | Strong candidate. Public-domain in EU; useful for geometry, foundations, invariant theory, number theory, physics. Start with `Grundlagen`/Hilbert problems/source apparatus or selected papers. |
| Benoit Mandelbrot | Modern/copyright-heavy: major books from 1970s-1980s; Stanford archival papers circa 1932-2010. | English works already exist but are copyrighted; archive contains drafts/correspondence/data. | Stanford/OAC finding aid; IA controlled digital lending for books; publisher copies. | Not an open transcription lane. Useful as modern reference/computational-visualization inspiration, but do not publish text without rights/open source. |

## Immediate Priority Candidates

1. **Steiner** - manageable, public-domain, important, likely under-translated; good geometry/diagram pipeline test.
2. **Weierstrass** - important and medium-sized, with strong value for analysis/history and less duplication than Euler.
3. **Desargues** - small and historically important; difficult old French/geometry but a good source-audit showcase.
4. **Fourier lesser works** - applied/math-physics value; avoid redoing the already translated main heat treatise unless producing TeX/source apparatus.
5. **Sophus Lie thematic packets** - high value but large; split into coherent source/translation packages.
6. **Möbius** - manageable four-volume source corpus and likely good geometry/mechanics value.
7. **Eisenstein** - compact high-value number-theory corpus, especially natural alongside Gauss/Dirichlet.
8. **Hilbert** - public-domain, central, and broad; best handled by selected works or themed packets rather than a whole-corpus first pass.

## Already Active / Do Not Duplicate Blindly

- **Gauss** is already an active lane; add source-completeness work and themed translation queues rather than starting a separate Gauss DOI.
- **Euler** has the Euler Archive; use it as the canonical reference and choose gaps, not duplicate the whole archive.
- **Archimedes** already has public-domain English Heath; value is clean TeX/diagram/source apparatus, not first translation.
- **Cantor** needs paper-by-paper translation-gap triage because some key works already have good English translations.

## Copyright / Publication Caution

- **Tarski** and likely **Takagi** are modern enough that open Zenodo transcription/translation is not automatically safe under a US-first publication screen either. Keep as private reference, Lean/formalization inspiration, or permissioned/open-license work unless a specific source is independently publication-safe.
- **Gödel** is also not a default open Zenodo transcription lane. Treat as reference/formalization/source-search only unless a specific original source is public-domain/open-licensed and publication-safe.
- **Mandelbrot** is a reference/permissioned lane only. The Stanford archive and modern books are valuable, but the core text corpus is not open-publication material by default.
- For older non-US authors, do not blindly use a death-date screen. Check publication year, place/language, possible US simultaneous publication, and URAA restoration risk where relevant. Most 19th-century corpus candidates are likely much cleaner than 20th-century ones; 20th-century foreign works after 1930 need work-level checks.

## References Checked

- Euler Archive: https://eulerarchive.maa.org/
- Euler works/translation note: https://scholarlycommons.pacific.edu/euler-works/
- Gauss Werke IA/Hathi/Göttingen route: https://archive.org/details/werkecarlf06gausrich and https://catalog.hathitrust.org/Record/008856128
- Lie collected papers: https://archive.org/details/gesamabhansup03lierich and https://catalog.hathitrust.org/Record/006198696
- Clifford papers: https://archive.org/details/mathematicalpap00smitgoog and https://quod.lib.umich.edu/u/umhistmath/AAS8031.0001.001?view=toc
- Galois Oeuvres: https://archive.org/details/uvresmathmatiqu00frangoog
- Archimedes Heath: https://math.nyu.edu/Archimedes/Books/ArchimedesInternet.html and https://archive.org/details/worksofarchimede029517mbp
- Apollonius/Conics: https://archive.org/details/treatiseonconics00apolrich and https://www.greenlion.com/books/ApolloniusConics.html
- Tarski collected-papers review/source notes: https://philarchive.org/archive/CORROQ
- Desargues/Hogendijk: https://www.jphogendijk.nl/publ/Desargues2.pdf
- Steiner: https://archive.org/details/jacobsteinersge01steigoog and https://mathshistory.st-andrews.ac.uk/Biographies/Steiner/
- Fourier: https://archive.org/details/uvresdefourier00natigoog and https://archive.org/details/analyticaltheory00fourrich
- Laplace: https://archive.org/details/oeuvrescomplte01lapluoft
- Lagrange: https://archive.org/details/oeuvresdelagrang07lagr and https://eudml.org/doc/203101
- Weierstrass: https://archive.org/details/mathematischewer01weieuoft and https://quod.lib.umich.edu/u/umhistmath/AAN8481.0007.001?view=toc
- Cauchy: https://archive.org/details/oeuvresdaugusti203caucrich
- Möbius: https://archive.org/details/gesammeltewerk03mb and https://catalog.hathitrust.org/Record/008897460
- Eisenstein: https://archive.org/details/mathematischewer01eise and https://catalog.hathitrust.org/Record/008897451
- Cantor: https://archive.org/details/georgcantorgesam00cant and https://archive.org/details/beitrgezurbegr00cant
- Gödel collected works/caution reference: https://global.oup.com/academic/product/kurt-gdel-collected-works-volume-i-9780195147209
- Hilbert collected works/source references: https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/gesammelte-abhandlungen-by-david-hilbert-3-volumes-originally-published-by-j-springer-verlag-berlin-1932-1933-1935-unaltered-reprint-by-chelsea-publishing-co-new-york-1965/82F40AF4617230E251BACE80BC14DE2C, https://archive.org/details/grundlagendergeo00hilb, https://www.gutenberg.org/ebooks/17384
- Mandelbrot caution/reference sources: https://oac.cdlib.org/findaid/ark:/13030/c8sf2zgr/, https://archives.stanford.edu/findingaid/ark:/22236/s1bf3cb219-466e-4763-9f9a-f229ba308bf1, https://archive.org/details/fractalgeometryo00beno
- US public-domain/current-term references: https://www.copyright.gov/circs/circ15a.pdf, https://guides.library.cornell.edu/copyright/publicdomain, https://www.copyright.gov/circs/circ38b.pdf

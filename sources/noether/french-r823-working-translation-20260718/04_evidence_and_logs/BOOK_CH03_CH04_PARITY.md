# R823 French book, Chapters III--IV: source-parity and QA evidence

Date: 2026-07-17  
Scope: the complete direct-R823 French translation of true sections 14--21, from the heading `Kapitel III. Abelsche Gruppen` through the last paragraph of section 21, stopping immediately before `Kapitel V. Faktorensysteme`.

## Authority and produced artifact

- Authority file: `C:\Users\Floris\Documents\interlanguage\03_projects\noether\03_translation_workspaces\fr_r823_20260717\authority\R823\pkg_r823\Noether_R823_WebB_R822_P20p27_31_RunInDashRefine_20260717\1\01_cumulative\Noether_R823_cum_de.tex`
- Authority-file SHA-256: `EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21`
- Exact authority range: lines 21544--22342 inclusive (799 physical source lines).
- Normalized range SHA-256: `4C8E881398EC45E8E709B3251DF3F042D2B1B4480C8F915D12078920488F6ACF`. This hash is over precisely lines 21544--22342, joined with LF and encoded as UTF-8 without BOM.
- Stop-boundary witness: line 22343 is `\section*{Kapitel V. Faktorensysteme}` and is not included.
- Produced TeX: `C:\Users\Floris\Documents\interlanguage\03_projects\noether\03_translation_workspaces\fr_r823_20260717\working\r823_fr\post43\book_ch03_ch04_fr.tex`
- Produced-TeX SHA-256: `7278DEF4B8F82FA527A824E9E8AC7525AF7D872B4DA6C98D07E2A3AED5A086AD`
- Produced size: 52,713 bytes; 813 physical lines.

The recovered `translation_memory/post44_french/part01_opening_chapters_I_VI.tex` and `part02_chapter_IV_continued_satz11.tex` were consulted only as translation memory. They are structurally incompatible with R823: the former compresses or replaces most of the actual sections, changes headings and numbering, and omits extensive arguments. No passage was accepted as authority.

## Boundary and section ledger

| R823 line | German structure | French structure |
|---:|---|---|
| 21544 | Kapitel III. Abelsche Gruppen | Chapitre III. Groupes abéliens |
| 21546 | § 14. Der Gruppenring | `\S{} 14. L'anneau de groupe` |
| 21592 | § 15. Die Gruppenringe Abelscher Gruppen | `\S{} 15. Les anneaux de groupe des groupes abéliens` |
| 21640 | § 16. Die Charakterenrelationen | `\S{} 16. Les relations entre caractères` |
| 21668 | § 17. Die Galoissche Theorie Abelscher Gruppen | `\S{} 17. La théorie de Galois des groupes abéliens` |
| 21790 | Kapitel IV. Zweiseitig einfache Ringe | Chapitre IV. Anneaux simples bilatères |
| 21792 | § 18. Ein Hilfssatz | `\S{} 18. Un lemme` |
| 21939 | § 19. Darstellungen ... | `\S{} 19. Représentations des systèmes hypercomplexes simples bilatères dans des corps non commutatifs étendant leurs corps de coefficients` |
| 22089 | § 20. Nichtkommutative Körper | `\S{} 20. Corps non commutatifs` |
| 22258 | § 21. Die Galoissche Theorie der nichtkommutativen Körper | `\S{} 21. La théorie de Galois des corps non commutatifs` |
| 22343 | Kapitel V. Faktorensysteme | excluded; next fragment boundary |

Section count delivered: **8**, namely true sections **14--21**, under exactly **2** chapter headings.

## Structural parity audit

The authority range and target were parsed as TeX text. Counts below are source/target.

| Structure | R823 | French | Result |
|---|---:|---:|---|
| `\section*` | 2 | 2 | pass |
| `\subsection*` | 8 | 8 | pass |
| Display blocks `\[ ... \]` | 93 | 93 | pass |
| `\srcfn` footnotes | 2 | 2 | pass |
| `enumerate` environments | 3 | 3 | pass |
| `\item` entries, including `3'` and `3.` | 9 | 9 | pass |
| `aligned` environments | 4 | 4 | pass |
| `array` environments | 6 | 6 | pass |
| `gathered` environments | 1 | 1 | pass |
| `center` environments | 1 | 1 | pass |
| numbered theorem statements | 14 | 14 | pass |
| bold numbered theorem statements | 13 | 13 | pass; R823 §19 theorem 1 is deliberately plain, not bold |
| blank-line-delimited content blocks | 234 | 234 | pass; the target's one additional raw block is its two-line provenance comment |
| literal Unicode section signs | n/a | 0 | pass; headings use `\S{}` |
| literal guillemet characters | n/a | 0 | pass |

For formula parity, the 93 display blocks were paired in order. Whitespace, punctuation used only as sentence punctuation, spacing commands, and the translated contents of `\text{...}` were ignored; all remaining TeX/math tokens were compared. Mismatches: **0 of 93**. Thus every displayed formula is present in the same order with the same mathematical notation. The two footnotes remain attached to R823 theorem 3/definition 4 material and theorem 6 respectively.

The theorem ledger is also complete:

- section 14: the centered complete-reducibility criterion;
- section 15: the unnumbered statement giving the `h` distinct irreducible representations;
- section 17: the principal subgroup/invariance correspondence;
- section 18: the unnumbered descent lemma for stable submodules;
- section 19: theorems 1--3;
- section 20: theorems 1--10, including Wedderburn's theorem;
- section 21: theorem 11, the principal theorem of the noncommutative Galois theory, with the full extension lemma and conclusion.

No summary, placeholder, ellipsis standing for omitted prose, or Chapter V material occurs in the produced file. The `\cdots` and explicit `+\cdots` lines in formulas are those of R823 itself.

## Terminology and register decisions

The following sense-specific choices are intentional and should be carried into the cumulative terminology ledger:

| German | Canonical French in this fragment | Decision |
|---|---|---|
| Gruppenring | anneau de groupe | Fixed project term. |
| abelsche Gruppe | groupe abélien | Standard French, never Pan-Romance. |
| zweiseitig einfacher Ring | anneau simple bilatère | Retains Noether's bilateral emphasis. |
| nichtkommutativer Körper / contextually noncommutative Körper | corps gauche | Canonical French prose term. In §18, the inner-automorphism and centre context makes \(K\) noncommutative even where R823 abbreviates it to *Körper*; the historical §19 title alone retains « corps non commutatifs ». |
| galoissche Theorie | théorie de Galois | Standard capitalization and register. |
| reziproke Darstellung | représentation réciproque | Retained as Noether's historical representation label. |
| reziprok isomorph / reziproker Isomorphismus | anti-isomorphe / anti-isomorphisme | The map reverses multiplication; the modern map terminology is explicit. |
| vollreduzibel | complètement réductible | Standard representation-theoretic French. |
| Zerfällungskörper | corps de décomposition | Standard French in the algebra/representation context. |
| Automorphismenkörper eines einfachen Ideals | corps des endomorphismes d'un idéal simple | Modern mathematically exact sense: the division ring includes the zero endomorphism, so literal `corps des automorphismes` would be misleading. |
| Invariantengruppe | groupe d'invariance | Used for the subgroup fixing the relevant object. |
| Invariantenbereich | domaine des invariants | Kept distinct from `corps des invariants` in the group/module arguments. |
| Invariantenkörper | corps des invariants | Standard Galois-theoretic term. |
| Hauptcharakter / Hauptdarstellung | caractère principal / représentation principale | Canonical French. |
| operatorisomorph | isomorphe comme module à opérateurs | Preserves the historical operator-module sense without inventing a new object. |

The root QA instruction concerning `reziprok` is obeyed: `représentation réciproque` remains the historical class name, while actual order-reversing maps and bijections are called `anti-isomorphismes`. No order-reversing map is mislabeled as an ordinary isomorphism.

## Source repairs and ambiguities

These are editorially resolved but recorded for auditability:

1. R823's typographical line-break fragments `Zerfällungs-` / `körper` (lines 22173--22175) and `Iso-` / `morphismus` (lines 22225--22227) were rejoined as ordinary French words; no content was removed.
2. The shorthand displayed sums such as `\mathfrak K_Z=y_1\xi_1\mathsf P+\cdots+y_m\xi_n\mathsf P`, the repeated `+\cdots` rows in the long section-19 calculation, and the source's distributive-law formula `S(m+m')=Sm+Sm'` were retained rather than silently algebraically emended.
3. `Automorphismenkörper` is semantically the endomorphism division ring of a simple ideal. `corps des endomorphismes` was selected for canonical French accuracy; this is a terminology clarification, not a change in the object.
4. In section 21, `reziprok isomorph` is read in its explicitly multiplication-reversing sense and rendered `anti-isomorphe`; `représentation réciproque` is retained only for the historical representation label.
5. The source's proof of theorem 10 ends at the contradiction and contains no explicit `w.z.b.w.` before section 21. The French likewise does not add a new concluding sentence.
6. Page-number references (pages 9, 10, 13, 15, 16, 20, and 22) are historical references internal to the R823 book and are retained verbatim for later cumulative pagination reconciliation.
7. In §18, R823 l. 21794, 21796 and 21798 calls \(K\) a *Körper*, but the conjugations \(\tau^{-1}\alpha\tau\), the group of inner automorphisms, and its invariant field as the centre force the division-ring sense. Accordingly `book_ch03_ch04_fr.tex:256,258,260` uses « corps gauche », while \(P\), the invariant field/centre, remains « corps »/« sous-corps ». The same sense is explicit in the noncommutative §19 heading (R823 l. 21939), and the hypothesis at l. 21945 is rendered « \(K\) un corps gauche dont le centre est \(P\) » (`book_ch03_ch04_fr.tex:412`).

No unresolved mathematical ambiguity remains in the fragment. The historical phrase `corps des endomorphismes` should be checked for global consistency when the cumulative terminology ledger is merged, but it denotes an unambiguous object here.

## Standalone smoke build

A temporary wrapper was compiled with LuaLaTeX. The wrapper used `article` at 11 pt, `amsmath`, `amssymb`, French `babel`, T1 font encoding, and the local test definition `\newcommand{\srcfn}[2]{\footnote{#2}}`; it then input only `book_ch03_ch04_fr.tex`.

- Command class: `lualatex -interaction=nonstopmode -halt-on-error -file-line-error -jobname=book_ch03_ch04_smoke <inline wrapper>`
- Temporary QA directory: `C:\Users\Floris\AppData\Local\Temp\fr_r823_ch34_11ba56ed32fe4fff9406009f440f26db`
- Exit status: **0**
- Output: **22 pages**, 398,683 bytes
- Smoke-PDF SHA-256: `54C4DC5EFDE3AD81080726DB211CB7F18FA0874B4BAB2D9CE5B1AC51736E4437`
- TeX error lines beginning `!`: **0**
- Undefined-control-sequence errors: **0**
- Underfull boxes: **0**
- Overfull boxes: **5** in the deliberately narrow standalone `article` geometry. Four are 0.91--9.20 pt prose boxes; one is the inherited long `aligned` calculation (62.57 pt). Visual inspection confirms that it is not clipped. The integrated cumulative's wider project geometry may reflow these differently.

## Visual QA

The smoke PDF was rasterized at 110 dpi and inspected on pages **1, 7, 11, 12, 17, and 22**:

- page 1: Chapter III and section 14 opening, centered theorem, radical calculation;
- page 7: section 17 terminal character relation and the Chapter IV/section 18 transition;
- page 11: section 19 module construction and formula sequence;
- page 12: the complete long `aligned` calculation, including its right-hand explanatory annotation;
- page 17: theorem 6, the second source footnote, theorem 7, and anti-isomorphism terminology;
- page 22: terminal section-21 representation-separation argument and final conclusion.

Observed result: no clipping, overlap, malformed display, missing glyph, mojibake, accent loss, bad section-sign encoding, or footnote collision. The long page-12 display extends beyond the normal prose measure in the test geometry but remains wholly visible and legible. This is fragment-level smoke QA; the integrated cumulative still requires its own changed-page and representative-spread visual inspection after final pagination.

## Integration cursor

- Input this file immediately after the section-13/Chapter-II fragment and immediately before the Chapter-V fragment.
- The fragment has no preamble and does not reset counters.
- Required cumulative macro/package support already expected by R823: `amsmath`-class display environments and `\srcfn`.
- First content token: `\section*{Chapitre III. Groupes abéliens}`.
- Last content sentence: the proof of theorem 11 concludes `\(\mathfrak T=\mathfrak S\), c.q.f.d.`.
- Next authority cursor: R823 line **22343**, `Kapitel V. Faktorensysteme` / true section 22.

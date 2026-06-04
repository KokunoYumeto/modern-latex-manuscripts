# Cumulative translation method: Spanish/Japanese Noether lane

Superseding scope note: translations are cumulative through Paper 30 complete. German source remains governing, English control secondary, with no summary substitution.

# Cumulative translation method: Spanish/Japanese Noether lane

Scope through this packet: Spanish and Japanese translations through Paper 29 complete.

1. Base source and control. German TeX/source is treated as the governing text. English control TeX is used as a secondary witness only for sense checking and to stabilize long technical sentences. Where source/control anomalies appear, preserve the source reading and record the anomaly rather than silently normalizing.

2. Output standard. Deliver editable TeX and compiled PDF. Do not use screenshots as substitutes for tables, formulas, or difficult notation. Mathematical displays remain editable TeX.

3. Translation register. German `Körper` is translated as Spanish `cuerpo`, Japanese `体`; `System` as `sistema` / `系`; `lineare Schar` as `familia lineal` / `線形族`; `Integritätsbereich` as `dominio íntegro` / `整域`; `relativ-ganzer Bereich` as `dominio relativamente entero` / `相対的整領域`; `ganze rationale Funktion` as `función racional entera` / `整有理関数`; `ganz rational` as `racional entero` / `整有理`; `Polarprozess` as `proceso polar` / `極化過程`; `Grundform` as `forma fundamental` / `基本形式`; `vollständiges System` as `sistema completo` / `完全系`.

4. Special-character policy. Preserve mathematical Greek, fraktur letters, primes, German names with diacritics, and formula punctuation. For Japanese, keep Latin technical names (Lüroth, Castelnuovo, Enriques, Hilbert, Kronecker, Galois, Mertens, Capelli, Deruyts, Clebsch--Gordan, Fischer, Zermelo) in Latin script unless an established Japanese rendering would materially improve clarity.

5. Build policy. Spanish is built with pdfLaTeX under UTF-8/T1. Japanese had previously used LuaLaTeX and jlreq/luatexja. In this packet the Japanese chunk and cumulative PDF are built with XeLaTeX + xeCJK + Noto Serif CJK JP because the local LuaHBTeX/luaotfload run did not complete reliably; the text body remains ordinary UTF-8 TeX and can be adapted back to jlreq/luatexja by local Codex if desired.

6. Packaging. One ZIP contains one root folder and only subfolders beneath that root.


## Paper 09 continuation note
Paper 09 complete was translated as a full-paper unit in Spanish and Japanese. Fidelity checks matched formula tag counts against the English control. No tables or diagrams occur in this paper; formulas were kept as editable TeX.


## Paper 12 continuation note
Paper 12, `Invarianten beliebiger Differentialausdrücke`, was translated as a complete-paper unit in Spanish and Japanese. The scan-corrected paper-level German edition was used as the source authority over the broader OCR component file, because the latter misread formula-sensitive notation such as `\delta x` and formula (7). Mathematical displays remain editable TeX; no diagrams or tables occur in this paper.

Paper 14: preserve the paper's survey-comparison architecture. Translate concepts rather than modernizing them silently; record historical terms such as Polygon/divisor, residual correspondence, conductor, different, absolute Riemann surface, singular primary numbers, and power-residue reciprocity in the glossary delta.


## Paper 15 continuation note
Paper 15, `Die Endlichkeit des Systems der ganzzahligen Invarianten binärer Formen`, was translated as a complete-paper unit in Spanish and Japanese. Preserve the distinction among integral invariants, rational-integer coefficients, and algebraic-integer coefficients. The local Fraktur macros `\frH`, `\frK`, `\frM`, `\frN`, `\frG`, `\frS` and the determinant shorthand `(ik)` are recorded in the methodology aids.

## Paper 16 continuation note
Paper 16, `Zur Reihenentwicklung in der Formentheorie`, was translated as a complete-paper unit in Spanish and Japanese. The paper is short but formula-dense: numbered formulas `(1)`--`(10)`, including `(2a)`, Fischer's operators `S=AB`, polar operators, `\Omega`, `\Delta`, the module congruence notation `\modu{M}`, and the final corrections section must remain editable TeX. Treat the source scan and paper-level German excerpt as the authority for formula punctuation and historical wording.

---

# Paper 17 §§10-12 and Paper 18 method and special-character note

Scope: Paper 17 §§10-12 complete and Paper 18 complete in Spanish and Japanese. This completes the Spanish/Japanese cumulative translation through Paper 18.

Source basis: the Batch26 German source/control TeX and PDF, the corresponding English control, and the scan slice `Noether_Paper17_sections10_12_and_Paper18_SOURCE_SCAN_collected_pdf_pages354-367_printed_pp340-353.pdf`. The German source remains controlling; the English control is used only as a sense witness and a guard against omissions.

Retroactive title standardization: the new cumulative Spanish/Japanese outputs update Paper 17's displayed title to include both `Differential- und Differenzenausdrücke`. Spanish now reads `expresiones diferenciales y de diferencias`; Japanese now reads `微分式および差分式`. This follows the Batch26 title and is clearer for the full paper. It does not change formulas or theorem content.

Paper 17 §§10-12: preserve the noncommutative module language from §§1-9. `Restgruppe` remains `grupo residual` / `剰余群`; `vollständig reduzibel` remains `completamente reducible` / `完全可約`; and `von gleicher Art` remains `del mismo tipo` / `同種`. The sequence of Theorems VIII-XII is retained, and formulas (31)--(44) remain editable TeX.

Paper 18: use `forma resultante` / `終結式形式` for `Resultantenform`. The abstract ideal-theory terms are translated as `ideal primario` / `準素イデアル` and `factor primario` / `準素因子`; avoid Japanese `一次イデアル` here, because the intended algebraic term is primary, not linear. Preserve the bracket decomposition `[\mathfrak Q,\mathfrak Q_1,\ldots,\mathfrak Q_r]=[\mathfrak Q,\mathfrak L]` as editable TeX.

No tables or diagrams occur in this scope. No formulas were converted to images, and no source-visible footnotes were omitted.

## Paper 19 introduction--§5 addendum

Use compact path names in packages. For Paper 19, keep `Ringbereich` as `dominio de anillos` / `環領域`, and treat German source formulas as governing over English-control defects.


---

# Translation-aid update: Paper 20-21

Spanish/Japanese terms added in this block concentrate on absolute irreducibility, reducibility forms, prime ideals and residue classes, and the formal variational calculus of differential invariants.

For Paper 20, keep `absolutamente irreducible` / `絶対既約` stable. For Paper 21, keep `cálculo variacional formal` / `形式的変分計算`, `invariantes diferenciales` / `微分不変量`, and the tensorial pair `contragrediente` / `反変`, `cogrediente` / `共変`.

Use the finite-parameter interpretation of `endliche Gruppe` in Paper 21. This avoids the false reading of a finite group in the modern abstract-algebra sense.


---

# Paper 22 methodology note

Scope: Paper 22 complete, `Bearbeitung von K. Hentzelt: Zur Theorie der Polynomideale und Resultanten`, in Spanish and Japanese. The continuation uses both source batches: the introduction through §3/Satz VI and §§4--7 complete. The German source is controlling; the English translation is a sense witness and omission guard.

Title optimization: to avoid the ambiguity that Hentzelt authored the revision, the Spanish title is `Reelaboración de un trabajo de K. Hentzelt`, and the Japanese title is `K. Hentzelt の論文の改作`. This is a wording optimization only; the German title and bibliographic meaning are unchanged.

Terminology: `Polynomideal` is `ideal de polinomios` / `多項式イデアル`; `Resultantenform` is `forma resultante` / `終結式形式`; `Grundmodul` is `módulo fundamental` / `基本加群`; `Grundideal` is `ideal fundamental` / `基本イデアル`; `Elementarteiler` is `divisor elemental` / `初等因子`. `Divisor` is kept in the algebraic divisibility sense, not the geometric-divisor sense.

Formula policy: formulas (1)--(36), all named definitions and theorems I--XIII, the Dedekind quotient of modules, the norm notation `N(G|A)`, the explicit decomposition of `ar R^{(i)}(z,x)`, and all source footnotes are preserved as editable TeX. No formula was converted to an image.

Global optimization check: this packet adds Paper 22 terminology and symbol policies to the cumulative methodology aids, but does not alter earlier translated paper text except through normal cumulative appending. Internal package paths remain short for Windows/Codex path safety.


---

# Paper 23 translation method note

No summary substitution was used. The Spanish and Japanese texts follow the German mathematical structure with the English control as secondary witness. The paper is expository rather than theorem-proof dense, so the main fidelity risk is terminology drift across invariant theory, ideal theory, and differential geometry.

Global standardization in cumulative output:
- `Integritätsbereich`: `dominio íntegro` / `整域`.
- `Integritätsbasis`: `base íntegra` / `整基底`.
- `ganze rationale Funktion`: remains `función racional entera` / `整有理関数`; it is not normalized to a rational quotient.
- `ganzzahlig`: remains integer-coefficient language where it appears.

The reduction theorem passage was kept deliberately modern-readable without changing source meaning: Weyl--Schouten `Übertragung` is treated as connection-language, but the literal “transmission/伝達” cue is kept in parentheses for auditability.

---

# Translation-method note - Paper 24 p1

Spanish/Japanese terms were chosen to keep the algebraic-ideal-theory lane coherent with Papers 19, 22, and 23. In particular, `Integritätsbereich` remains `dominio íntegro` / `整域`, and `Elementarteilerform` is fixed as `forma de divisores elementales` / `初等因子形式`.

`Dimension schlechthin` is rendered literally but idiomatically as `dimensión sin más` / `単にいう次元`, preserving Noether's contrast with `Höchstdimension`.

Japanese uses `体` for field/body contexts and keeps `Galois 体` where the historical body language is central; Spanish keeps `cuerpo` consistently in residue-class/zero/Galois-body contexts.


---

# Paper 24 complete translation-method note

Scope: Paper 24, `Eliminationstheorie und allgemeine Idealtheorie`, is now complete in Spanish and Japanese. The present continuation covers §§4--7 and is joined with the already delivered title/introduction--§3 block in the full Paper 24 and cumulative outputs.

Source basis: Batch34 German/control for title--§3, Batch35 German/control for §§4--7, and the merged scan witness for printed pp. 444--476. The German source is controlling; the English control is a sense and omission witness.

Coherence policy: terminology is kept aligned with Papers 19, 22, and 23 for later Takagi/Weber-adjacent integration. `Integritätsbereich` remains `dominio íntegro` / `整域`; `Elementarteilerform` remains `forma de divisores elementales` / `初等因子形式`; `Restklassenkörper` remains `cuerpo de clases residuales` / `剰余類体`; `Primärideal` remains `ideal primario` / `準素イデアル`; and `eigentliches Primärideal` remains `ideal primario propio` / `真の準素イデアル`.

Paper 24 §§4--7: preserve the chain definition of dimension by prime ideals, the classification of fundamental ideals by isolated components, the distinction between necessary and sufficient criteria for prime/proper-primary ideals, the imperfect-field characteristic-$p$ examples, and the absolute-prime theorem with Ostrowski reduction. Theorems V--XVII, Lemmas VI--VIII, all displayed norm/elementary-divisor formulae, and all source-visible footnotes are kept as editable TeX.

Path policy: the root and internal package paths were shortened to reduce Windows/Codex path-length risk.


---

# Papers 25--29 translation-method note

Scope: Papers 25--29 were translated as a contiguous short-paper block. The cumulative branch begins from the corrected Paper 24-complete cumulative outputs and now runs through Paper 29 complete.

Source basis: Batch36 German source/control TeX/PDF, Batch36 English control TeX/PDF, and the scan witness for collected pages 491--506 / printed pp. 477--492. German remains controlling; English is a secondary sense and omission witness.

Global terminology carried forward: `Eliminationstheorie` is kept as `teoría de la eliminación` / `消去理論`; `Restklassenkörper` as `cuerpo de clases residuales` / `剰余類体`; `Nullstellenkörper` as `cuerpo de ceros` / `零点体`; `Primärideal` as `ideal primario` / `準素イデアル`; `zugehöriges Primideal` as `ideal primo asociado` / `付随素イデアル`; `Integritätsbasis` as `base íntegra` / `整基底`.

Paper-specific decisions: Paper 25 mirrors Paper 24's elimination/ideal-theory vocabulary. Paper 26 uses finite-order language for `endliche Ordnung`. Paper 27 keeps `números hilbertianos` / `Hilbert 数`. Paper 28 treats Frobenius character theory as ideal theory of the group ring and preserves one-sided/two-sided distinctions. Paper 29 uses finite abstract linear group language, unlike Paper 21's finite-parameter Lie-group context.

Formula policy: all displayed formulas, norm decompositions, Galois resolvent formulas, and source-visible footnotes remain editable TeX. No tables or diagrams occur in this block.


# Translation method - Paper 30

German source/control TeX is governing for terminology and formulas; English control is used as a secondary witness only. Where macro support was added in source/control TeX, the patch is mechanical preamble support for symbols visible in the German/English body, not a source-content normalization.

The Paper 30 translation keeps Noether's abstract ideal-theoretic wording rather than recasting the paper in later textbook terminology. Where modern terminology is unavoidable for clarity, it is limited to stable equivalents already established in earlier cumulative methodology files.

No diagrams or tables occur in Paper 30. All displayed formulas, chains, quotient expressions, and the final Jordan--Hölder comparison are preserved as editable TeX.

---

# Paper 31 translation-method note

Spanish: prefer `el discriminante` and `teorema del discriminante`; retain `orden` for algebraic orders. Use `anillo de clases residuales`, `cuerpo residual`, `anillo de extensión`, `anillo de cocientes`, `ideal discriminante`, and `anillo de multiplicación` consistently.

Japanese: use `判別式定理`, `オーダー`, `主オーダー`, `剰余類環`, `剰余体`, `拡大環`, `商環`, `判別イデアル`, and `乗法環`. For `erste/zweite Art`, use `第一種` / `第二種` rather than importing a different taxonomy.

Layout: the Japanese build uses XeLaTeX/xeCJK. The only warnings are normal font substitutions for small math/CJK italic shapes; no overfull/underfull hbox reports appear in the current translation logs.


---

# Papers 32--33 continuation note

# Method note - Papers 32--33 ES/JA

Scope: Papers 32 and 33 were translated as a contiguous Brauer/Noether representation-theory block. German source/control TeX remains governing; English control is used as secondary witness for sentence structure and omission checks.

Paper 32 distinction: `Zerfällungskörper kleinsten Grades` is rendered as `cuerpo de descomposición de grado mínimo` / `最小次数の分解体`, while `minimaler Zerfällungskörper` is rendered as `cuerpo de descomposición minimal` / `極小分解体`. This preserves Noether--Brauer's distinction between smallest degree and minimality under inclusion.

Noncommutative-field policy: historical `nichtkommutativer Körper` is kept as Spanish `cuerpo no conmutativo`, with first occurrence clarified by `(anillo de división)`, and Japanese `非可換体`, with first occurrence clarified by `（斜体）`. This is intended to remain compatible with later Brauer/Schur/central-simple-algebra integration.

Paper 33 operator language: `Gruppe mit Operatorenbereich`, `operatorisomorph`, `Automorphismenkörper`, `Doppelkettensatz`, and one-sided/two-sided ideal language were translated literally enough to preserve the historical operator-group framework, rather than modernizing directly to module-category terminology.

Formula policy: all displayed formulas, quaternion matrix arrays, relative-norm identities, footnotes, and the two Paper 33 block-matrix reductions remain editable TeX. No tables or diagrams occur in this block.


## Translation policy through Paper 34 §4

Noether’s `Gruppen mit Operatoren` is kept as group-with-operators terminology, not modernized into module categories. `Operatorhomomorphismus` is translated literally but idiomatically: Spanish uses `homomorfismo por operadores` in prose and `operador-homomorfo` in compact theorem statements; Japanese uses `作用素準同型`. The cumulative branch applies a wording-only retroactive refinement to Paper 33: `Automorphismenkörper` is now division-ring language, not a commutative field assertion.

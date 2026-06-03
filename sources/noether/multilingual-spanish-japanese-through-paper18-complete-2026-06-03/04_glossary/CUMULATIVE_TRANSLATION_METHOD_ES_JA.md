# Cumulative translation method: Spanish/Japanese Noether lane

Scope through this packet: Spanish and Japanese translations through Paper 16 complete. This file is cumulative and should travel with later packets.

1. Base source and control. German TeX/source is treated as the governing text. English control TeX is used as a secondary witness only for sense checking and to stabilize long technical sentences. Where source/control anomalies appear, preserve the source reading and record the anomaly rather than silently normalizing.

2. Output standard. Deliver editable TeX and compiled PDF. Do not use screenshots as substitutes for tables, formulas, or difficult notation. Mathematical displays remain editable TeX.

3. Translation register. German `Körper` is translated as Spanish `cuerpo`, Japanese `体`; `System` as `sistema` / `系`; `lineare Schar` as `familia lineal` / `線形族`; `Integritätsbereich` as `dominio de integridad` / `整性領域`; `relativ-ganzer Bereich` as `dominio relativamente entero` / `相対的整領域`; `ganze rationale Funktion` as `función racional entera` / `整有理関数`; `ganz rational` as `racional entero` / `整有理`; `Polarprozess` as `proceso polar` / `極化過程`; `Grundform` as `forma fundamental` / `基本形式`; `vollständiges System` as `sistema completo` / `完全系`.

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


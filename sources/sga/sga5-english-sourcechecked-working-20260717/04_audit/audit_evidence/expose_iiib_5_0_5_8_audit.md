# SGA 5 Exposé III B §§5.0--5.8 — translation and insertion audit

## Status

The omitted block was translated in full. While this audit was being completed, the parent integrated it into the active cumulative. The production block is byte-for-byte equal to the prepared tranche; this audit agent made no production edit. The durable standalone witness is `expose_iiib_5_0_5_8_insertion.tex`; it includes the missing Part II and no.~5 headings, §§5.0 through 5.8, the sole footnote, every displayed formula, and the square 5.8.4.

## Authority and exact scope

- Current French authority: `03_projects/language_management/english_germanic/02_native_examples/sga5_current_french_workpass/sga5_fr_workpass.tex`, SHA-256 `791F4EFFC5E02832D5D77ED03518C8156D6F07E4C8238B03545DB93D883FBB28`.
- Exact translated span: French lines **4928--5178 inclusive**. Lines 4928--4932 supply the missing `II. Correspondances équivariantes` and `5. Traces non commutatives` headings and the governing conventions; §5.0 starts at line 4934; the final sentence of §5.8 is line 5178. Line 5180 begins §5.9 and is excluded.
- Original scan: `C:\Users\Floris\Documents\Papors\OS\SGA5 (1).pdf`, SHA-256 `B256EBD072A8C68209518412A263C9289C6F1854A346733D86F885930D5FE6CA`. Printed pp.162--171 are PDF pages 174--183 (one-based).
- The older packet `sga_current_cumulative_packet_035/01_cumulative_clean/SGA5_clean_cumulative_translation_current.tex`, SHA-256 `E74DC0A56584EE9921B726D49E8305C74C816CF59A66520C5DED7B1670ADBFF6`, was consulted only as a negative/terminology witness. Its version is abridged, collapses distinct subsections, omits proofs and hypotheses, and replaces $A_\natural$ by the incorrect $A_K$; none of those departures was inherited.

## Exact integration and insertion anchors

At the observed active-workpass state SHA-256 `43982FFCB6D453492F758CDF7EED0124240C9FEAE8E5DE16FAEBECF4741F25F4` (15,247 lines), insert the tranche between these two exact strings:

1. Preceding anchor, active line 5132:

   `is zero. Therefore (*) is zero, which completes the proof of 4.2, hence of 2.5 and 1.2.`

2. Following anchor, active line 5134:

   `\subsubsection*{5.9. Traces and extension of scalars}`

The cumulative then changed concurrently. At the integrated state SHA-256 `8AD8C551BBB79FAFD07F2F6094CEA7041B33F6DBA1D8D01E34608B9CF2D4A460` (15,499 lines), the exact tranche occupies active lines **5134--5384**, §5.0 begins at active line 5140, and §5.9 begins at active line 5386. The 251-line active block and standalone tranche content have the identical LF-normalized UTF-8 SHA-256 `8D17CC58DB096F6F5CCC1713F1A65E94C1C73AE465B13FEC95BF6E3300084431`.

The strings and block hash, not transient whole-file line numbers, are controlling. The production cumulative now contains `\section*{II. Equivariant correspondences}` and `\subsection*{5. Non-commutative traces}` exactly once; do not reinsert the tranche or add duplicate headings.

After further concurrent edits changed the whole-workpass hash to `2A0B341893FF1996C04DAC49DF7F753A232D00A1C29AFA38A88E1A6A36926B40`, the same lines 5134--5384 were rehashed and still matched `8D17CC58...0084431` exactly. The integrated tranche is therefore stable across the later cumulative edits observed in this audit.

## Section and line coverage

| Unit | French authority lines | Printed pages | English tranche lines |
|---|---:|---:|---:|
| Part II / no.~5 headings and conventions | 4928--4932 | 162 | 6--10 |
| 5.0 Introduction | 4934--4981 | 162--164 | 12--59 |
| 5.1 Notation | 4983--4991 | 164 | 61--69 |
| 5.2 | 4993--5011 | 165 | 71--89 |
| 5.3 | 5013--5043 | 165--166 | 91--121 |
| 5.4 | 5045--5066 | 166--167 | 123--144 |
| 5.5 | 5068--5070 | 167 | 146--148 |
| 5.6 | 5072--5097 | 167--168 | 150--175 |
| 5.7 | 5099--5137 | 168--170 | 177--215 |
| 5.8 | 5139--5178 | 170--171 | 217--256 |

There are no theorem/proposition/proof environments in this source span. Its paragraph boundaries, lettered parts (a), (b), single footnote, subsection boundaries, and transition into 5.9 are all preserved.

## Formula and diagram parity

The task brief's inherited count of “43 numbered formulas plus diagram 5.8.4” does **not** match either the current French authority or the scan. The authoritative block contains:

- **38 tagged items total**, namely 37 non-diagram formulas and the tagged commutative square 5.8.4;
- 32 `equation` environments, 3 `align` environments (six tagged rows), and 11 unnumbered displays;
- **46 display blocks total** when each `equation`, `align`, or `\[...\]` block is counted once.

The formula-comparison script found 46 French display blocks and 46 English display blocks, with **zero differences after whitespace normalization**. `expose_iiib_5_0_5_8_formula_comparison.csv` enumerates every one of the 38 tags with exact French and English line anchors. No labels are absent in 5.1 or 5.5; those subsections contain no numbered formulas in the source. The count 43 should therefore be treated as an inventory error, not filled by inventing five labels.

## Scan-controlled and editorial decisions

| Site | Evidence and decision |
|---|---|
| 5.6.1, printed p.167 | The unusual printed/current-authority notation is `\Tr_A=\uRHom_A(...)\longrightarrow...`, not a colon. It is preserved exactly; silently regularizing it to `\Tr_A:` was rejected. |
| 5.7.5 lead-in, printed p.170 | Both scan and French workpass say the complex homomorphism targets `$A$`, although 5.6.3 targets `$A_\natural$`. The wording is preserved and the semantic tension is recorded rather than silently emended. |
| 5.8.1 prose, printed p.170 | The scan prints `$a,b\in K$`; the quotient relation `$axb\otimes y-x\otimes bya$` requires `$a,b\in A$`, and the source-checked French workpass already makes that correction. The English follows the authority: `$a,b\in A$`. |
| 5.8.4, printed p.171 | The four objects, horizontal arrows (1), trace arrows, and downward arrow (2) were visually checked against the scan. The `tikzcd` is formula-identical to the French authority. |
| Parenthesis after 5.8.4 | The scan closes the explanatory parenthesis after the two evaluation arrows; the French TeX drops that closing mark. A literal close after a display rendered as an orphan. The English preserves the complete thought as two sentences without changing either formula. |

## Terminology and rejected choices

| Adopted English | Rejected alternative | Control / reason |
|---|---|---|
| non-commutative | noncommutative | The active Exposé III B introduction and contents use the hyphenated form. |
| locally a direct factor | locally a direct summand | The active §§5.10 and 6.5 and recovered SGA 3 controls use “direct factor” for `facteur direct`. |
| punctual topos | point topos | The active Exposé III B introduction and SGA 4 English baseline use “punctual topos”. |
| $A_\natural$, $E_\natural$, $G_\natural$ | $A_K$, $E_A$ | Exact French/scan notation; the older abridged packet's substitutions destroy the coinvariant notation. |
| arrow | map (as default) | Matches the active §5.9--5.13 translation and keeps `flèche` distinct from a generic prose map. |
| external tensor product | exterior tensor product | Matches the active SGA 5 cumulative's terminology. |
| terms of a complex | components | Standard English homological usage for `composantes`; avoids confusion with connected components. |
| finite perfect amplitude; finite tor-dimension | finite Tor-amplitude | Tracks the source's two distinct phrases and the active cumulative's house style. |
| strictly perfect | strongly perfect | Standard SGA terminology and the SGA 1--4 control vocabulary. |
| extension of scalars / restriction of scalars | base change / forgetting scalars | Matches the already-present §5.9 and §5.10 headings and prose. |

## Compile and visual QA

- A temporary copy of the integrated active state `8AD8C551...D4A460` was made under `tmp/sga5_audits/`. No production file was modified by this audit agent.
- Two consecutive `pdflatex -halt-on-error` passes completed with exit code 0. The complete test PDF has 308 pages; a focused seven-page extract is `expose_iiib_5_0_5_8_compiled_extract.pdf`.
- The integrated block produces no overfull or underfull boxes. The full cumulative retains its existing repeated hyperref warnings for manually tagged equations; these are document-wide and not a tranche syntax failure.
- Exact full-size rendered-QA paths:
  - `C:\Users\Floris\Documents\interlanguage\tmp\sga5_audits\expose_iiib_5_0_5_8_rendered\page-105.png`
  - `C:\Users\Floris\Documents\interlanguage\tmp\sga5_audits\expose_iiib_5_0_5_8_rendered\page-106.png`
  - `C:\Users\Floris\Documents\interlanguage\tmp\sga5_audits\expose_iiib_5_0_5_8_rendered\page-107.png`
  - `C:\Users\Floris\Documents\interlanguage\tmp\sga5_audits\expose_iiib_5_0_5_8_rendered\page-108.png`
  - `C:\Users\Floris\Documents\interlanguage\tmp\sga5_audits\expose_iiib_5_0_5_8_rendered\page-109.png`
  - `C:\Users\Floris\Documents\interlanguage\tmp\sga5_audits\expose_iiib_5_0_5_8_rendered\page-110.png`
  - `C:\Users\Floris\Documents\interlanguage\tmp\sga5_audits\expose_iiib_5_0_5_8_rendered\page-111.png`
  - contact sheet: `C:\Users\Floris\Documents\interlanguage\tmp\sga5_audits\expose_iiib_5_0_5_8_rendered\visual_qa_contact.png`
- Visual verdict: **no layout defects** on PDF pages 105--111. There is no clipping, collision, broken glyph, margin overflow, blank page, or orphan punctuation. The single footnote is complete on page 106; formulas 5.6.1--5.6.6 fit on page 109; 5.8.1 and 5.8.2 remain within the measure on page 110; the complete 5.8.4 square and the transition into §5.9 are clear on page 111.

## Handoff

Retain the currently integrated block; do **not** apply the tranche a second time. Update the parent source/formula, terminology, continuation, and publication ledgers with the block hash and QA paths above. The translation itself has no unresolved source ambiguity. The three recorded source/editorial anomalies (5.6.1, the 5.7.5 target, and printed 5.8.1 `$a,b\in K$`) must remain visible in the editorial ledger after promotion.

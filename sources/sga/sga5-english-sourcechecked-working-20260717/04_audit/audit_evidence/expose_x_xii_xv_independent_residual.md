# SGA 5 independent residual synchronization — Exposés X, XII, XV

Audit and application date: 2026-07-17 (Europe/Berlin)

## Scope and gate

This is the independent, source-critical second pass over Exposés X, XII, and XV in the active English cumulative. The ordered displays, every diagram topology, and source-correction prose anchors were checked against the current French workpass; ambiguous readings were checked against the original LNM 589 scan. Only unambiguous residuals were applied. This pass did not compile because other editors were active in the shared cumulative; the parent manager owns the frozen build gate.

The pass found and applied new residual debt in Exposés X and XV. It found no additional unambiguous residual in Exposé XII. This is a bounded tranche receipt, not a claim that the complete SGA 5 volume is publication-ready.

## Frozen provenance and moving-workpass hashes

- English active workpass: `03_projects/language_management/english_germanic/03_working_translations/sga5_english_sync_workpass/SGA5_English_sync_workpass.tex`
  - observed at assignment: `A21FA26600D6DA671FBBEA6EF18BDDA6BAA0074456399AE823D2881610E19823`
  - immediately before this tranche: `237ACFB99BBD51A83495662F9D56260768DB7CFB4F22AE132583B2A3D71EF978`
  - immediately after this tranche: `CC9C46D6CE32039AA607670BD78E14E02347C03AAE284AD249EB6635F51D49B7`
  - moving shared head when this report closed: `313435A40E17DF53DC9C86D271548EFCE1C27520662D609D05C4FB373211E4F2`
- French source-checked authority: `03_projects/language_management/english_germanic/02_native_examples/sga5_current_french_workpass/sga5_fr_workpass.tex`
  - SHA-256: `791F4EFFC5E02832D5D77ED03518C8156D6F07E4C8238B03545DB93D883FBB28`
- Original LNM 589 scan: `C:/Users/Floris/Documents/Papors/OS/SGA5 (1).pdf`
  - SHA-256: `B256EBD072A8C68209518412A263C9289C6F1854A346733D86F885930D5FE6CA`

The difference between the immediate post-tranche hash and the closing moving-head hash is from concurrent work in the shared cumulative. The semantic anchors below, rather than volatile global line numbers, are the durable receipt.

## Applied correction ledger

| Exposé | Printed page | English semantic anchor | Exact source-critical correction | Authority / scan evidence | Disposition |
|---|---:|---|---|---|---|
| X | 387 | proof after Proposition 4.4 | `Sw_y\simeq\check{Sw}_y` → `Sw_{y'}\simeq\check{Sw}_{y'}` | French authority 12648; local valuation calculation is at `y'` | applied |
| X | 387 | (4.5.1), (4.5.2), (4.5.3) | restored the leading equalities `\sigma^{*}_{y'}=\sigma^{*}_{y''}=\sigma_y`, `\sigma^{\prime*}_{y'}=\sigma^{\prime*}_{y''}=\sigma'_y`, and `a^{*}_{y'}=a^{*}_{y''}=a_y` | French 12653–12670; scan render `p387.png` | applied |
| X | 383, 389–390, 396 | literal K-theory symbols in Proposition 3.2, reduction/trace maps, and examples (a)–(c) | replaced residual `K^*` with `K^{\bullet}` and residual `K_0` with `K_\bullet` at all literal sites in Exposé X | French 12361–12362, 12714–12715, 12748–12749, 12921–12925; scan renders `p389.png`, `p396.png` | applied |
| X | 392 | distinguished triangle in the trace calculation | restored the missing `\arrow[dl]` from `\RG_{Y'}`; the top object now has both diagonal arrows | French diagram at 12794; scan `p392.png` | applied |
| X | 395 | (6.1.1) | `F_{\bar\eta}=F'_{\bar\eta'}=M` → `F_{\bar\eta}\simeq F'_{\bar\eta'}=M` | French 12859–12862 | applied |
| X | 398 | (7.6) | changed the second link from an undirected `\simeq` token to the source reverse arrow `\xleftarrow{\sim}` | French 12996–13002; arrow direction is mathematically part of the displayed Künneth morphism | applied |
| X | 399 | distinguished triangle (7.8) | restored `\RG_Y(F|Y)\arrow[dl]` and `\RG_C(F)\arrow[ul]` | French 13019–13023; scan `p399.png` | applied |
| X | 399 | formula immediately after (7.8) | `\sum_{y\in Y}F_y` → `\coprod_{y\in Y}F_y` | French 13026–13027; scan `p399.png` | applied |
| X | 404 | distinguished triangle (7.16) | restored `\RG_Z(Q^\bullet|Z)\arrow[dl]` and `\RG_V(F)\arrow[ul]` | French 13176–13180; scan `p404.png` | applied |
| X | 404 | cartesian square following (7.16) | restored hook topology on both horizontal immersions: `\arrow[r,hook,"j"]` and `\arrow[r,hook]` | French 13183–13187; scan `p404.png` | applied |
| XV | 449 | affine/projective relative-Frobenius paragraph | restored the omitted map type `\pi_{\Spec(\mathcal A)/S}:\Spec(\mathcal A)^{(p)}\to\Spec(\mathcal A)` | French 14452; scan `p449.png` | applied |
| XV | 455 | sentence following the Hom-bijection display | restored the omitted parenthetical `(with $g^*$ left adjoint to $g_*$)` | French 14639–14645; scan `p455.png` | applied |
| XV | 456 | proof of Proposition 4(c) | `$(\Fr^*)^{-1}$` → `$(\Fr^*_{/})^{-1}$` | French 14670; scan `p455.png`/`p456.png` | applied |
| XV | 466 | finite punctual reduction | `X=\Spec(\mathbb F_q)` → `X=\Spec(\mathbb F_{q'})` | French 15010–15016; scan render `p466.png` visibly distinguishes `q'` from the preceding `q` | applied |
| XV | 468 | first noetherian reduction | malformed inherited `j=1,\\ldots,r` → `j=1,\ldots,r` | source line on scan `p468.png` | already applied by parent during this audit; verified present, not reapplied |

## Post-application structural receipt

The independent comparison script was rerun after the tranche.

| Exposé | Display math FR/EN | Inline math FR/EN | All math FR/EN | Diagrams FR/EN | Diagram topology result |
|---|---:|---:|---:|---:|---|
| X | 142/142 | 753/753 | 895/895 | 7/7 | all 7 topology-equivalent |
| XII | 137/146 | 456/444 | 593/590 | 4/4 | all 4 topology-equivalent |
| XV | 164/165 | 1217/1217 | 1381/1382 | 5/5 | all 5 topology-equivalent |

The XII and XV raw math-count deltas are representational: English display splitting/combining and a complete expanded proof create different TeX segmentation. Ordered comparison and direct review found no further unambiguous omitted or altered formula in XII. In XV the remaining one-item delta includes source-equivalent formatting/variable representation, not a missing French mathematical assertion.

Evidence files:

- `tmp/sga5_audits/x_xii_xv_independent_receipt/ORDERED_MATH_ALIGNMENT.csv`
  - SHA-256: `E71B85FFA596F205E141FAFE4BC772D52132489BE238910EEEDAFF4EE09C99F2`
- `tmp/sga5_audits/x_xii_xv_independent_receipt/DIAGRAM_TOPOLOGY.csv`
  - SHA-256: `7989EAB902ED20F1FC9CC75AF250D88484A349187224378E13B0232FE220757E`
- scan renders: `tmp/pdfs/sga5_x_xii_xv_scan/` (notably pp. 387, 389, 392, 396, 399, 404, 449, 455–456, 466, and 468)

## Authority hazards and rejected changes

1. The current French workpass has a `% FIX #52` comment embedded on its line 14737. In TeX this comments out the rest of that French source line, although the printed scan contains the omitted continuation. The English already preserves the scan content; no deletion was made to imitate the comment hazard.
2. The global English macro `\clKstar` expands to `K^*`, whereas the French workpass macro expands to `K^{\bullet}`. This bounded pass corrected every residual literal X site but did not change the global macro because that would alter all exposés. The parent manager must adjudicate it at the frozen whole-volume gate.
3. The Exposé XV proof consistently uses `\psi` where the French uses `\varphi`. This is coherent alpha-renaming throughout the argument, so no patch was made.
4. Existing scan-adjudicated readings were retained: X `(Lemma 5.1)`, the asymmetric point/source notation, XV bare `F`, bare `K'`, and the printed index references to Exposé XIV. No prior rejected choice was silently reopened.
5. The scan's typewritten K-theory glyph can resemble an asterisk. The current source-checked French authority and the existing exact-candidate ledger distinguish homological `K_\bullet` from cohomological `K^{\bullet}`; the applied literal corrections follow that controlled reading.

## Continuation cursor

The independent residual cursor for Exposés X, XII, and XV is closed at the semantic anchor after Exposé XV's first noetherian reduction (printed p. 468). All 16 diagrams in these three exposés are topology-equivalent after application. The next action is the parent's frozen whole-cumulative compile, rendered visual QA, formula/source comparison consolidation, and manifest refresh. No compile or publication action was taken in this bounded pass.

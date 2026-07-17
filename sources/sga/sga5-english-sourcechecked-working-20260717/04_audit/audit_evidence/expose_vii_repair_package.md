# SGA 5 Exposé VII — production repair package

Date: 2026-07-17  
Scope: Exposé VII only  
Production status: **not edited by this package author**  
Gate result: **repair package ready for application; Exposé VII is not synchronized until it is applied and the full cumulative is rebuilt and visually checked**

## Controlling witnesses

- Active English workpass snapshot at the final literal-anchor validation: `SGA5_English_sync_workpass.tex`, SHA-256 `8B30D84552E2A9EB04502A28935B4DE15466A171CE7C21136D9A47CE57B2FF82`.
- Final French authority: `sga5_fr_workpass.tex`, SHA-256 `791F4EFFC5E02832D5D77ED03518C8156D6F07E4C8238B03545DB93D883FBB28`.
- Original LNM 589 scan: `C:\Users\Floris\Documents\Papors\OS\SGA5 (1).pdf`, SHA-256 `B256EBD072A8C68209518412A263C9289C6F1854A346733D86F885930D5FE6CA`.
- Printed/source page mapping used here: printed page = PDF page minus 12.

## Deliverables

- `expose_vii_repair_map.json`: exact, machine-readable old→new anchors for all 24 actionable receipt IDs, plus the `(Q)` tag, p.333 arrow-label, and p.346 proof-tail repairs.
- `expose_vii_p346_replacement.tex`: insertion-ready English replacement for French authority lines 11419–11434 (printed pp.346–347).
- `expose_vii_p346_compile.tex`, `.pdf`, and `.log`: isolated integration harness and build evidence for the large replacement.
- `expose_vii_p346_render/expose_vii_p346_compile-1.png`: rendered visual-QA evidence.
- `expose_vii_scan_p346/lnm589_p346-358.png` and `lnm589_p347-359.png`: scan evidence for the Hironaka citation, both diagrams, and the final pushforward identity.
- `expose_vii_repair_sha256_manifest.csv`: hashes for the package and its evidence.

## Exact receipt coverage

All requested receipt IDs are present exactly once in `expose_vii_repair_map.json`:

`0038 0042 0048 0052 0055 0056 0197 0200 0206 0219 0220 0223 0224 0226 0227 0237 0247 0248 0250 0252 0255 0256 0259 0265`

Literal-anchor validation against the recorded production snapshot found every one of the 24 receipt anchors exactly once. The two bounded structural anchors also occur exactly once. This avoids unsafe global substitutions; receipt 0237, for example, targets only the first of two superficially similar formulas by including its preceding and following prose in the old string.

The most consequential bounded repairs are:

- 0048 restores the omitted sentence introducing the projection formula.
- 0206 removes the spurious compact-support subscript from Lemma 7.1.1(a), while leaving part (b) unchanged.
- 0237 restores `f^*f_*f^*=j_*\gamma f^*+f^*` in the first calculation only.
- 0250 restores the complete omitted display with `c_d(\check E)` and the transition “in other words”.
- 0255 corrects injectivity from `\gamma` to `\gamma_*` and identifies the retracted morphism correctly.
- 0265 is subsumed by the complete p.346 proof-tail replacement.

## Structural repairs

### Tag `(Q)`

French authority lines 10035–10039 use a tagged display. The active English had an untagged display. The map restores the authority representation `\[ ... \tag{Q} ... \]`.

### Printed p.333 arrow label

In Proposition 8.6.3(a), the left vertical arrow must be labelled `(8.6.1)`. The right vertical arrow remains `\cup`. The active English incorrectly labels both vertical arrows `\cup`.

### Printed pp.346–347 proof tail

The current English collapses the proof tail after (9.8.8) into one paragraph, omits both source diagrams and the Hironaka citation, changes `v''_*` to `v_*` too early, and concludes from the wrong/circular identity.

`expose_vii_p346_replacement.tex` restores:

1. Hironaka, *Smoothing of algebraic cycles*, Amer. Journal of Math. (1968), Lemma 4.1.
2. The cartesian diagram involving `H`, `H\times\mathbb P^1`, `X'\times\mathbb P^1=Z'_1`, and their maps to `Y`, `Y\times\mathbb P^1`, and `X\times\mathbb P^1`.
3. The canonical commutative diagram involving `X'`, `Z''`, `H`, and `X'\times\mathbb P^1`.
4. The correct target assertion that `v''_*` is injective.
5. The reduction via `(D_2)` to injectivity of `v_*` when `Y` has codimension one in `X`.
6. The final source identity `(f_1)_*\circ v_*=u_*\circ f_*` and the correct argument: `f_*` is an isomorphism and `u_*` is a direct monomorphism because `u` admits a retraction.

The two restored diagrams close the known Exposé VII diagram deficit (13 English versus 15 French before repair).

## Source-critical editorial decisions

- **Receipt 0248:** the scan and French authority say, literally, “Denote the locally free module defined by …” without naming it in the prose, although the following exact sequence begins `0\to E`. A literal English omission would be ungrammatical. The recommended English is “Denote by `E` the locally free … module defined by …”; it preserves the unique mathematical referent and normalizes the inherited prose without inventing content.
- **Receipt 0259:** the scan glyph after `Z` denotes set difference; the French workpass transcribes it as `\doteq`. The English repair uses `Z\setminus Y`, the geometrically correct complement over which the inverse image is taken.
- The Hironaka title remains in its published English form and the journal citation follows the scan.

## Compile and visual QA

The isolated harness compiled with pdfTeX/MiKTeX using `-interaction=nonstopmode -halt-on-error -file-line-error`.

- Output: one page, 153,415 bytes.
- Fatal errors: none.
- LaTeX/package warnings: none.
- Overfull/underfull boxes: none reported.
- Visual inspection at 180 dpi: both diagrams are legible and centered; arrowheads and labels are present; no clipping, overlap, or margin collision; the final identity and transition to Theorem 9.9 are readable.
- Scan comparison: rendered printed pp.346 and 347 directly confirms the citation, diagram topology, labels, target `v''_*`, and final identity.

## Safe production application order

1. Revalidate every `old_tex` count in `expose_vii_repair_map.json` against the then-current workpass. The recorded SHA-256 is a snapshot guard, not a claim that later concurrent edits are invalid.
2. Apply the 24 receipt replacements, except that 0265 is automatically covered by the full p.346 replacement.
3. Apply `SGA5-VII-TAG-Q` and `SGA5-VII-P333-ARROW-LABEL`.
4. Replace the exact p.346 tail bounded by `old_start` and `old_end` with `expose_vii_p346_replacement.tex`, preserving the following sentence “We now state the theorem corresponding to (8.5 b).”
5. Build the complete cumulative, rerun structural parity, and require Exposé VII to show 15/15 diagrams and the restored source tag.
6. Render all changed production pages, especially printed pp.283, 289, 294, 300, 303, 306, 309, 314, 319, 323–325, 331, 333, 337–342, and 346–347.
7. Only then promote the tranche and update the cumulative correction, terminology/rejected-choice, continuation, and SHA-256 ledgers.

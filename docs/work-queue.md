# Work Queue

The [adoption board](adopt.md) is the current operational queue. Its
[complete index](adopt-index.md) lists every Board ID, author, work, language,
coverage class, readiness state, owner, allowed workflow, and continuation
cursor. This page is a short human entry point, not a second source of truth.

At the current board generation there are 78 bounded rows: 9 current, 64 ready
for adoption, and 5 future/source-discovery scopes. An unclaimed row is open for
independent adoption. A current row may still welcome declared parallel review.
Neither state implies scholarly certification.

Before beginning work:

1. Open the row's coverage map and inspect the represented bytes.
2. Use the exact Board ID in an [adoption issue](https://github.com/KokunoYumeto/modern-latex-manuscripts/issues/new?template=adopt.yml).
3. Preserve the supplied source identities and declare any overlap.
4. Return an inspectable result with exact files, checks, failures, reversals,
   and a continuation cursor through the
   [handback form](https://github.com/KokunoYumeto/modern-latex-manuscripts/issues/new?template=handback.yml).

## Current Work

| Board ID | Author / work | Current public starting point | Useful parallel contribution |
|---|---|---|---|
| `noether-de-auth` | Emmy Noether — canonical German authority | [Noether map](noether-map.md) | Verify one exact correction or cross-language finding against its authority coordinate. |
| `ega-i-p143-control` | Grothendieck–Dieudonné — EGA I | [EGA map](ega-map.md) | Replay the sealed p.143 checkpoint or independently review a bounded range before p.144 continuation. |
| `fga-foundements` | Grothendieck and collaborators — FGA | [FGA map](fga-map.md) | Review one Exposé, *Commentaires* range, erratum, or graph residual. |
| `verdier-thesis` | Jean-Louis Verdier — thesis | [Verdier map](verdier-map.md) | Review admitted pp.2–9 or continue from physical p.10. |
| `tohoku-paper` | Alexander Grothendieck — Tôhoku paper | [Tôhoku map](tohoku-map.md) | Reconcile the preserved p.119 versus pp.119–121 cursor evidence. |
| `illusie-cotangent-i-ii` | Luc Illusie — *Complexe cotangent et déformations* I–II | [Illusie map](illusie-map.md) | Review LNM 239 pp.1–23 or continue at physical p.24 / printed p.6. |
| `deligne-papers-letters` | Pierre Deligne — papers and correspondence | [Deligne map](deligne-map.md) | Select one mapped paper, letter, correction generation, or source-review target. |
| `weber-algebra` | Heinrich Weber — *Lehrbuch der Algebra* | [Weber map](weber-map.md) | Reconcile the Volume II §143 GitHub frontier with the separately reported §176 generation before continuing at source p.643. |
| `stacks-commons-layer` | Stacks Project / Mathematics Commons overlay | [Stacks architecture](stacks.md) | Propose the first provenance-complete Commons overlay entry in a declared namespace. |

## High-Value Ready Work

The complete list is in the [adoption index](adopt-index.md). Especially useful
bounded starts include:

- Review existing complete Noether English, Spanish, French, Russian,
  Ukrainian, Interslavic, Korean, Chinese, Japanese, Indonesian, or Vietnamese
  work instead of retranslating it. Use the exact language/work row in the
  [Noether map](noether-map.md).
- Continue Korean Noether Paper 9 at authority line 7330
  (`noether-ko-p09`).
- Continue Arabic or Iranian Persian Noether Paper 6 at `P06-S0006`
  (`noether-ar-p06`, `noether-fa-p06`).
- Independently replay the represented English EGA 0–IV assembly
  (`ega-0-iv-en-global`).
- Recover the exact Gauss *Werke* II packet before continuing at printed p.305
  (`gauss-werke-ii`).
- Review or repair exact Dedekind, Dirichlet, Riemann, Cayley, Hecke, Killing,
  Maxwell, Gibbs, Sylvester, Gordan, and non-European work rows from their
  linked maps.

## Highest-Value Typesetting And Source-Check Work

| Board ID | Work | Exact next step | Map |
|---|---|---|---|
| `maxwell-treatise-v1` | Maxwell, *A Treatise on Electricity and Magnetism*, Vol. I | Continue at printed p.80 / IA leaf 118. | [Adoption index](adopt-index.md) |
| `gibbs-papers-v1-p3` | Gibbs, *Scientific Papers*, Vol. I, Paper 3 | Continue at printed p.135. | [Adoption index](adopt-index.md) |
| `gauss-werke-ii` | Gauss, *Werke*, Band II | Recover and hash-replay the exact nine-ZIP packet, then continue at printed p.305. | [Gauss map](gauss-map.md) |
| `dedekind-gmw-i` | Dedekind, *Gesammelte mathematische Werke*, Band I | Continue with item V at printed p.40. | [Dedekind map](dedekind-map.md) |
| `dedekind-stetigkeit` | Dedekind, *Stetigkeit und irrationale Zahlen* | Continue section 5 after printed p.328. | [Dedekind map](dedekind-map.md) |
| `dirichlet-werke-ii-xxv` | Dirichlet, *Werke* II, item XXV | Repair printed pp.263–302 at full formula and line level. | [Dirichlet map](dirichlet-map.md) |
| `dirichlet-werke-ii-xxvii` | Dirichlet, *Werke* II, item XXVII | Produce a typed German source track for printed pp.309–356. | [Dirichlet map](dirichlet-map.md) |
| `riemann-werke-sync` | Riemann, broader *Werke* draft | Recover or produce an exact post-trim source/control package for the 511-page reader. | [Riemann map](riemann-map.md) |
| `cayley-repair` | Cayley, *Collected Mathematical Papers* | Declare and repair one bounded page range. | [Cayley map](cayley-map.md) |

## Source-Only And Assembly Work

Several tracked languages already have editable text without a matching direct
reader. These are assembly or review tasks, not new-translation invitations.
Examples include the Arabic layers for *Nine Chapters* and *Sunzi Suanjing*, Li
Ye English layers, and Qin Jiushao modern-Chinese layers. Use the
[non-European map](non-european-map.md) and the exact Board ID before assigning
work.

## Historical Notes

Earlier staging and package notes remain preserved in Git history and in their
linked manifests. They are provenance, not the current queue. Use the adoption
board and coverage maps for present work so obsolete filenames, upload plans,
or superseded branches do not trigger duplicate effort.

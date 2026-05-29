# Deligne translation pass 3 - first completed body translations

## Scope

This pass translates selected available TeX sources from the pass-2 cleaned workspace. It does not attempt recasting, modernization of proofs, or repair of paper 76. The objective here is a direct English reading layer while preserving mathematical notation and LaTeX structure.

## Completed in this pass

| Paper | English title | Output |
|---:|---|---|
| 61 | What are motives for? | TeX + compiled PDF |
| 70 | Some Main Ideas in the Work of A. Grothendieck | TeX + compiled PDF |
| 81 | Extended Euler congruence | English-normalized TeX + compiled PDF; source was already English |

## Compile/render validation

- `61_What_are_motives_for_EN.tex`: compiles under XeLaTeX. One minor overfull hbox remains; render inspection found no clipped display after fixing the long equivalence in subsection 2.2.
- `70_Main_Ideas_in_Grothendieck_Work_EN.tex`: compiles under XeLaTeX with no LaTeX errors and no overfull hboxes reported.
- `81_Extended_Euler_congruence_EN.tex`: compiles under XeLaTeX with no LaTeX errors and no overfull hboxes reported after a second pass for cross-references.

## Translation policy used here

- Preserve displayed mathematics, labels, numbering, and bibliographic references as far as possible.
- Translate prose into direct modern mathematical English without expanding arguments.
- Do not recast proofs or replace terminology by a more speculative modern framework.
- Keep source-level anomalies visible unless they are clear transcription errors that would obstruct reading.

## Notable source correction

Paper 61, equation (3.12.1), read in the uploaded TeX as `\Ext^1(\mathbf{1}, \Q(1)) = K_{2j-1}(F) \otimes \Q`. I corrected this in the English translation to `\Ext^1(\mathbf{1}, \Q(j)) = K_{2j-1}(F) \otimes \Q`, which is the mathematically coherent form.

## Remaining work

The rest of papers 30-90 remain queued for body translation. Paper 76 remains deferred for structural TeX repair, as requested.

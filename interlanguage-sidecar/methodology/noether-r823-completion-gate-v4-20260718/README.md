# Noether R823 translation completion gate

This GitHub directory is the compact, inspectable mirror. The complete release
package, including all 473 render PNGs, is preserved on Zenodo at
<https://doi.org/10.5281/zenodo.21422899>; see `ZENODO_RELEASE.md` for exact
hashes and the post-publication download-back receipt.

This package freezes the executable v4 completion gate used on 18 July 2026
for the Spanish Noether R823 working translation. It supplements the actual
translation bodies and reader published on the Noether concept DOI:

- Noether concept DOI: `10.5281/zenodo.20412587`
- Candidate release tested here: `10.5281/zenodo.21422620`

## Contents

- `spec/`: the human-readable gate contract.
- `scripts/`: the exact gate, adversarial replay, manifest builders,
  structural audits, parity tools, and synchronization helper.
- `evidence/SPANISH_R823_COMPLETION_GATE_PIXEL_BOUND.json`: the passing
  35-check v4 result.
- `evidence/SPANISH_R823_GATE_ADVERSARIAL_SELFTEST.log`: the passing attack
  replay.
- `evidence/SPANISH_R823_FINAL_SOURCE_AUDIT_20260718.md`: the readable audit
  bound into all 81 unit records.
- `evidence/SPANISH_R823_VISUAL_REVIEW_RECORD_20260718.json`: the structured
  all-page review decision.
- `evidence/*120DPI.csv`: complete manifests for the candidate-derived
  473-page render baseline. The PNG bodies are in the full Zenodo ZIP rather
  than duplicated in ordinary Git history.
- `evidence/SPANISH_R823_TERMINOLOGY_LOCATOR_AUDIT.csv`: the 101-row evidence
  classification. Sixty-eight independent native Spanish TeX line witnesses
  pass file, SHA-256, and line-range verification; 33 target-only decisions
  remain visible but are excluded from the independent-source minimum.
- `FULL_ZENODO_PACKAGE_SHA256.csv`: the 501-file manifest for the complete
  Zenodo ZIP, including render PNGs that are intentionally absent here.

## What a pass means

The gate verifies the declared 81-unit scope, exact R823 authority hash,
expanded target hashes, byte-exact parity promotion, direct evidence and
support-file bindings, terminology-source minimum, structural tripwires,
current build artifacts, final-audit hashes, complete PDF derivation, stored
render pixels, visual-review record, and end-of-run snapshot stability.

It deliberately rejects a target-only terminology citation, a stale or
hand-edited parity ledger, arbitrary rehashed images, a review record bound to
another render, or a final audit that merely sits beside the unit evidence.

## What a pass does not mean

This is not a linguistic-quality oracle, native-speaker certification, peer
review, mathematical proof check, or critical-edition certification. The
Spanish reader remains a source-reconciled working translation. Users should
retain the limitations recorded on the Noether Zenodo page and compare
important passages with the German authority and source scans.

## Reuse

Run the gate separately for Spanish or French and supply the live authority,
expanded target, PDF/build files, parity evidence, terminology ledger, visual
ledger, structured review record, and final audit. The adversarial self-test
must pass first. Absolute paths in production evidence are provenance records,
not portable defaults; a relocated corpus should regenerate manifests and
parity output from its new root instead of editing a passing JSON result.

Corrections and improvements can be proposed through
<https://github.com/KokunoYumeto/modern-latex-manuscripts>.

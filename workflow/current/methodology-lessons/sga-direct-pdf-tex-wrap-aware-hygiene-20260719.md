# Direct PDF/TeX Surfaces and Wrap-Aware Hygiene

## What worked

- Keep the public SGA record reader-first while it remains comfortably below
  the repository file ceiling.
- Publish the current bounded PDF and cumulative TeX as direct files. Group
  source ledgers, build evidence, render QA, and reproducibility controls into
  coherent support packages.
- Preserve producer freezes unchanged and create a separately receipted public
  projection when audience wording, privacy, or single-file compilation needs
  adjustment.
- Verify every new direct file by streamed SHA-256 readback and every inherited
  file by exact byte count plus remote checksum.

## Failure and repair

- Evidence logs described as sanitized can still leak a local path when the
  path is split across wrapped lines. Literal whole-line searches are therefore
  insufficient.
- Public-package privacy gates should scan raw bytes, decoded text, slash and
  whitespace-normalized text, and reconstructed wrap joins before publication.
- A hygiene repair that changes only evidence wording must still regenerate all
  dependent manifests and receive an independent delta audit.

## Public-surface rule

- Current record `10.5281/zenodo.21435547` pairs all eight reader PDFs with
  direct TeX downloads: SGA1 English; SGA2 Exposes V and VI English; SGA5
  French and English; and SGA6 French, English, and the bounded Spanish tranche.
- When a canonical source is modular, publish a mechanically flattened direct
  companion only after confirming that it has no unresolved dependencies and
  reproduces the retained reader's page count and extracted text.
- Supporting ledgers and render images stay grouped, but their machine-readable
  indices remain mirrored on GitHub.
- This download convenience does not expand the scholarly claim. SGA1 and SGA2
  are bounded and incomplete; SGA5 is selected rather than complete; SGA6 has
  explicit mixed authority layers. None is a critical edition, peer review,
  proof certification, independent human review, or rights clearance.

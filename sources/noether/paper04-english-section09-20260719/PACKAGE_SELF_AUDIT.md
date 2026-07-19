# Package self-audit

The candidate was assembled as an additive Section 9 exact set. The following
gates were executed against the package-local artifacts and public
projections:

- exact TeX, locked PDF, extracted text, and render hashes;
- isolated three-pass build from the packaged TeX only;
- byte-identical isolated extraction and two-of-two page renders;
- two-page PDF metadata, font embedding, Unicode maps, and restricted action
  surface;
- five rectangular, formula-safe current-only CSV ledgers;
- four duplicate-key-free current-only JSONL ledgers;
- 122 globally unique stable IDs, evidence-reference closure, graph
  acyclicity, and structural parent-child reciprocity;
- exact 22-line source partition, twelve source-defect classes, seventeen
  adverse physical losses, and three zero-count ambiguity controls;
- source-body, source-image, inherited-body, raw-log, archive, traversal,
  symlink, and unexpected-executable exclusion;
- generic absolute-path and UUID scans plus separate configured-private-string
  and binary scans;
- exact manifest, size, SHA-256, and file-set reconciliation.

The final portable validator result is PASS with zero failures after the
manifest controls were generated. The separate raw-byte, multi-encoding,
whitespace-recomposition, PDF-object, and PNG-trailing-data audit also passed
with zero findings. This self-audit is operational evidence only,
not human peer review, mathematical certification, rights clearance, archive
acceptance, publication, or remote readback.

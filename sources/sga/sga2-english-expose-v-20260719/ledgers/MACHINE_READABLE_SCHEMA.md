# Machine-readable evidence schema -- SGA2 Expose V cumulative checkpoint

All CSV files are UTF-8, RFC-4180-style rectangular tables with one header row. Primary IDs are stable within this checkpoint, record_revision is numeric, supersedes is blank unless a prior record is replaced, and spreadsheet-formula trigger cells are apostrophe-protected.

STRUCTURAL_INDEX.jsonl forms a closed root-to-component hierarchy and carries an explicit root revision from assembly self-gate to independent-package-audit state. DIFFICULTY_REVISION_LEDGER.jsonl uses event_id, stable_id, record_revision, supersedes, and closed_by; every closed revision pair is reciprocal. Its publication-state revision records that independent package audit is closed while public archive curator rights/license/release decisions remain open.

INDEPENDENT_PACKAGE_REVIEW.csv records the independent audit checks with stable review IDs, source and target locators, exact status, evidence counts, and the assembly self-gate evidence each check reviews or supersedes. MACHINE_READABLE_VALIDATION.json is the current independent-package-audit validation receipt; ASSEMBLY_SELF_GATE_MACHINE_VALIDATION_20260718.json preserves the earlier self-gate receipt unchanged.

Source locators distinguish corrected French TeX lines, printed-volume pages, one-based physical source-PDF pages, and recomposed running pages. The body maps to physical pages 55-63 / running pages 47-55; physical pages 52-54 / running pages 44-46 are predecessor context only. Target locators identify cumulative TeX line spans. The corrected French TeX remains authority; the external English candidate is comparison-only.

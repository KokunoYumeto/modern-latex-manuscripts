# Workflow Addendum 2026-06-12: Object-Level Diagram And Table Audit

This addendum records a practical promotion rule learned from diagram-heavy and
table-heavy repair lanes, including Seki, Klein-Fricke, Poincare, Kneser,
Gordan, Picard, Mikami, SGA, and Deligne work packets.

## Core Rule

Page-level render checks are not enough for pages that contain diagrams, large
tables, determinant displays, dense formula clusters, or special-symbol regions.
Promotion should happen at the object level.

A promoted object should have:

- a stable object ID;
- a source page or source crop witness;
- one or more current-output render witnesses;
- the TeX or reader anchor where the object appears;
- an explicit verdict such as `accepted`, `needs_repair`, `image_backed`,
  `candidate_only`, or `not_present`;
- a note explaining any remaining limitation.

## What Counts As Evidence

Full-page screenshots and contact sheets are useful for orientation, but they
are not authority by themselves. The actionable unit is a source object witness
plus the corresponding output object or render, tied together in a ledger row.

This distinction matters because a page can look broadly plausible while still
having a wrong arrow, missing determinant row, flattened commutative diagram,
wrong table rule, missing label, or altered special symbol.

## Screenshot Substitution Rule

Source crops or screenshots must not silently replace TeX. If a public package
uses an image because faithful TeX reconstruction is not yet available, the
package should say so explicitly and mark the object as image-backed or open.
Do not describe such a range as fully reconstructed TeX.

## Separate Quality Axes

Diagram presence, diagram fidelity, language fidelity, and mathematical source
fidelity are separate status axes. A package can have all diagrams present but
still fail final promotion because the prose or mathematical wording has not
been checked. Conversely, a clean translation can still need object-level repair
for diagrams or tables.

## Minimal Ledger Shape

For compact handoffs and public audit support, use a CSV or JSONL ledger with
fields similar to:

```csv
author_package,object_id,object_type,source_witness,outputs_checked,verdict,notes
Seki p001-p009,seki_p009_cube_diagram,diagram,src-2.png,out1-2.png; out2-3.png,needs_repair,diagram present but cube geometry needs direct source comparison
Klein-Fricke V1 p029-p042,kf_p034_table_1,table,src-06.png,out1-06.png; out2-06.png,accepted,table visible in source and output render
```

The exact field names can vary by project, but the source witness, output
witness, object type, verdict, and note should not be omitted.

## Publication Guidance

Do not upload large raw audit bricks just because they exist. Distill them into:

- a short policy note;
- a compact object ledger;
- a few representative source/output witness crops if needed;
- a package-level status note that says which objects are accepted, open, or
  image-backed.

This keeps the public archive readable while preserving the audit trail needed
for future repair.

# Root independent audit — SGA5 exhaustive reference retrofit R9

Status: **PASS**

Final root:
`[local frozen R9 delivery root; absolute host path withheld]`

This public copy removes only that host-local locator. The frozen private
receipt is 2,593 bytes with SHA-256
`79C2D5EA56511F443D468B7A3140CC51784FD56FC48A7F6E85EB9BB7DB3CF31C`.

Frozen reader:

- TeX SHA-256: `765067892F2F208015235BF548F2F8FA03E56DA63D4ED470CF5B67F08CA1CE2F`
- PDF SHA-256: `EF93294085E06FFCF1F95DD8D2DEBB14DAD22FED44D967E09D3BAB24F5C78F6E`
- 309 pages
- 1,101 stable targets
- 1,578 cumulative edges, including 720 new R9 edges
- 1,460 candidate dispositions
- 1,614 compiled GoTo annotations
- zero unresolved, unwrapped, or unadjudicated internal reference candidates

Root checks:

1. Replayed the final manifest validation: 27 self-excluding rows, all exact.
2. Confirmed the three build passes converge in AUX, OUT, and decoded page content.
3. Confirmed R8-to-R9 flow and layout extraction are byte-identical.
4. Randomly inspected residual classifications, including typography/layout values and unavailable same-work targets; the sampled rows were positively supported rather than generic fallbacks.
5. Inspected all five 150-dpi visual contact sheets. Link color is the only intended visual change; diagrams, index columns, formulas, spacing, glyphs, and terminal pages are intact.
6. Confirmed the independent read-only audit closes the exact target, edge, candidate, TeX-wrapper, AUX, PDF-destination, PDF-annotation, font, residual, and visible-source multisets.

Controlling receipts:

- `machine_readable_references/R9_FINAL_REFERENCE_SUMMARY.json` — SHA-256 `8CD86A80AC6B29FFB098B33DD7A27A389E321649559F92BA53F149964B60BFA5`
- `machine_readable_references/R9_INDEPENDENT_REFERENCE_AUDIT.md` — SHA-256 `99D45263438BD30972E4458F3B18005E678031C57595A1A1954EE420E771F355`
- `machine_readable_references/R9_COMPILED_REFERENCE_VALIDATION.json` — SHA-256 `F453C2231F83F02BA8CEF090916EC472B43BFDB71A88D1AE40AD9C37BADFE4CF`
- `machine_readable_references/R9_VISUAL_QA.json` — SHA-256 `BABA5EC88F0EAF6CD630E26E287F68708B66BA3FC71AC26DF9DA7262D218CC3A`
- `machine_readable_references/R9_DELIVERY_MANIFEST.csv` — SHA-256 `5A262FD81A4638D321047D84A3ED2D4B904C74172B127FCABAED1F518C83AB9B`
- `machine_readable_references/R9_DELIVERY_MANIFEST_VALIDATION.json` — SHA-256 `C14904D2AC5810BDA8479229B84B30A4E0667772F8EBF45DA4A01E805767DB2F`
- convention v2 — SHA-256 `F5BDC71164EDA34128E584E4F117993D31EE07698E329986CF5013519E5CA8CC`

This receipt is stored outside the frozen R9 root and therefore does not alter its self-excluding manifest.

# Dedicated FAC quality-assessment DOI process logbook

## FAC-DOI-LOG-0001 — placement decision

- Date: 2026-08-03.
- Decision: create a dedicated, small FAC quality-assessment DOI rather than relying on the existing 5 GB methodology omnibus record.
- Rationale: the user asked that the accidental blind comparison be front-and-center and understandable to a mathematician without inspecting a large heterogeneous record. The current methodology head contains the earlier FAC evidence among 99 files and does not front it. Three of its nineteen FAC projections also differ from the final immutable evidence package.
- Relationship: the dedicated record will cite the broad methodology concept DOI `10.5281/zenodo.21124403` and later Serre/GAGA translation record. It does not erase the earlier broad-record projections.

## FAC-DOI-LOG-0002 — archive coordination and adverse predecessor state

- The replacement archive task confirmed that it created no FAC draft and performed no mutation after the dedicated-DOI correction.
- Pre-existing methodology record `10.5281/zenodo.21778949` and replication record `10.5281/zenodo.21778962` each contain nineteen FAC-named files but reproduce only 16/19 final R1 evidence bytes.
- Divergent predecessor files: the privacy-clean self-correction ledger, project-logbook snapshot, and evidence manifest. They are retained as adverse prior projections; this dedicated record uses the immutable R1 bytes.

## FAC-DOI-LOG-0003 — payload composition

- Front the human-readable chronology, claim boundary, quality-assessment report, and exact model/process provenance.
- Include both the 74-page chronology-bound no. 79 reader and the 78-page complete reader; label nos. 80--81 comparator-aware and exclude them from blind claims.
- Include unit/finding CSVs and complete project decision/self-correction logs directly.
- Include the full nineteen-file comparator evidence package as an exact ZIP.
- Include buildable English, diplomatic French, and corrected French TeX in one source ZIP; exclude build scratch, authority scan, third-party comparator files, and French compiled readers.

## FAC-DOI-LOG-0004 — operational adverse event: PowerShell result pipeline

- A read-only row-count command attempted to pipe directly after a `foreach` statement and failed at parse time with `An empty pipe element is not allowed`.
- Impact: none; no statement executed and no file changed.
- Correction: collect results into an explicit array and pipe only after the loop. The corrected query returned 79 unit rows, 138 finding rows, 219 self-correction rows, and 10 source/comparator identity rows.

## FAC-DOI-LOG-0005 — operational adverse event: literal wildcard copy

- The first source-staging command passed wildcard paths to PowerShell `Copy-Item -LiteralPath`; the wildcard could not expand. Direct reader/evidence copies and non-wildcard source files succeeded, but component/manual wildcard copies failed.
- Impact: the new no-overwrite source staging directory was temporarily incomplete; no source or immutable input was modified.
- Correction: enumerate the exact bounded component/manual directories with `Get-ChildItem -Filter '*.tex' -File`, then copy each resolved literal path. Final stage: 109 files / 1,125,913 bytes before adding its README and manifest.

## Continuation requirement

Any revision of this record must append a new entry recording the exact predecessor DOI/version, changed bytes, reason, evidence, and public readback result. No entry may be silently rewritten after publication.

## FAC-DOI-LOG-0006 — R1 privacy preflight rejection and R2 successor

- The first dedicated-DOI candidate inherited one internal archive-task identifier in `09_FAC_Project_Logbook.md`. The same byte was also embedded in the copied nineteen-file R1 evidence ZIP.
- The preflight scan found exactly one matching line before upload. No Zenodo file or metadata had been created from the candidate.
- R1 is retained locally as rejected preflight history. R2 removes the two task UUIDs from the public logbook sentence while preserving the substantive archive-role decision, states that identifiers were removed, and omits the contaminated R1 evidence ZIP.
- R2 exposes the complete 79-row inventory, 95-row input-identity layer, and all-unit validation directly. It retains the source ZIP, which independently passed a zero-hit scan of its 110 source/control files.
- This is a privacy/control-layer correction only. English and French TeX, both English reader PDFs, the 79 unit reviews, 138 findings, and mathematical decisions are unchanged.

## FAC-DOI-LOG-0007 — first R2 validator false PASS

- The first R2 package validator invoked the `pdfinfo.cmd` override on Windows. That wrapper could not resolve its bundled path, returned no metadata, and the page parser then tried to cast an empty/object-array result to an integer.
- The command emitted two conversion errors but continued. Because the validator did not make non-null page counts a mandatory condition, it wrote a false PASS with both reader `pages` fields null.
- The exact false-PASS JSON is preserved as `18_PACKAGE_VALIDATION_SUPERSEDED_R1_FALSE_PASS.json`, 3,933 bytes, SHA-256 `948C5389713F96618EC3C357751ADA5E5F46BCC312EEA10A6061437F5D01D21D`.
- Correction: select the exact native Poppler executable under the bundled runtime, require one and only one integer `Pages:` result for each PDF, require the expected 74/78 page pair, and regenerate the manifest and validation. Reader bytes and all substantive evidence remain unchanged.

## FAC-DOI-LOG-0008 — repeated read-only PowerShell pipeline parse error

- The first bounded native-`pdfinfo` test repeated the earlier PowerShell mistake of piping directly from a `foreach` statement and failed at parse time with `An empty pipe element is not allowed`.
- Impact: none; the command did not execute and no file changed.
- Correction: collect the two result objects in an explicit array and pipe after the loop. The corrected test returned native exit code 0, exactly one page line per file, and the expected counts 74 and 78.
- Recurrence lesson: all further multi-item PowerShell reports in this package use an explicit results array; the prior correction is not treated as closed merely because it appeared once in a ledger.

## FAC-DOI-LOG-0009 — corrected-validator parse failure

- The first corrected-validator invocation omitted a closing parenthesis in two nested `foreach ($m in $matches)` clauses and failed at parse time with `Unexpected token '{'`.
- Impact: none; PowerShell parsed no statement, so the payload manifest and validation were not regenerated and no publication file changed.
- Correction: restore the closing parentheses, rerun the complete validation from the immutable candidate files, and admit no PASS unless the validator reaches its final summary with errors empty and explicit 74/78 page counts.

## FAC-DOI-LOG-0010 — validator used a nonexistent unit-ID column

- The first successfully executing self-contained validator checked uniqueness through `$unitRows.unit_id`, but the 79-row review schema names its stable key `review_id` and uses `comparator_id` for the matched unit.
- PowerShell returned 79 null values as one unique value, so the validator correctly held the package but reported the misleading error `duplicate_unit_ids`.
- The exact FAIL is preserved as `19_PACKAGE_VALIDATION_SUPERSEDED_R2_BAD_ID_COLUMN.json`, 4,265 bytes, SHA-256 `DD0417B92259302C2F07CC90E78074FF3F2DA255BF33324BEB2A7F83C5E834C7`.
- Correction: validate `review_id` uniqueness explicitly and report the field as `review_ids_unique`. No CSV row or substantive artifact changed.

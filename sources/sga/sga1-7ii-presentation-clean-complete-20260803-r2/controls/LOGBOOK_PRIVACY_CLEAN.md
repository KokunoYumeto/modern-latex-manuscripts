# Production logbook — presentation-clean SGA checkpoint

This logbook records functional choices and reversals for the bounded clean
checkpoint.  It is external to every reader PDF.

## 2026-08-03 — reader-surface policy

Selected policy: reader PDFs contain only bibliographic matter, translated
mathematics, and genuine source-era/published-editor material.  Production
status, scan comparison, source ambiguity rationale, automation, certification,
and archive workflow belong in external ledgers.  This avoids making editorial
process commentary look like part of the historical mathematical work.

## SGA 1

Two project-added proof notes were removed from the visible reader and retained
in the external removal history.  The attested mathematical readings themselves
were not altered.  Two links that existed only inside removed commentary ceased
to be active reader edges.  The complete mathematical source scope and page
content otherwise remain unchanged.

## SGA 5

Two project-added source-comparison footnotes were removed from the visible
reader and retained in the external removal history.  The printed formula chain
and the selected French-control formula were preserved.  Workflow-bearing PDF
metadata was replaced by neutral bibliographic metadata.  No mathematical
reading was changed by this presentation repair.

## SGA 4½

The Calligra suffix letters in the sheaf-operator names were replaced by
mathrsfs initials plus Latin Modern suffix letters.  This is a font-layer
normalization only: operator spelling, mathematical role, formulas, pagination,
reference graph, and navigation remain unchanged.  The reason is exact and
testable: the predecessor emitted one embedded Type 3 font resource; the chosen
form emits embedded Type 1 fonts.  Workflow-bearing author metadata was also
replaced by the contributor list visible on the title page.

## SGA 2 and SGA 3 input refresh

The cumulative input was refreshed from the older local SGA 2/3 reader bytes to
the current public R10 and R29 reader bytes.  Both replacements were rescanned
for presentation prose.  The fifteen resulting matches are edition-intrinsic
editor notes, not producer or AI explanatory matter, and were retained with
row-level adjudications.  The input refresh changed no other volume.

## Cumulative construction

The cumulative builder clones each standalone reader in order and prefixes all
named destinations and named GoTo actions with a stable volume identifier.  It
imports each volume's outline beneath a volume-level bookmark.  Page streams and
geometry are not re-typeset.  An exact replay proves 4,177/4,177 pages equal to
their input pages and proves zero broken or misrouted named actions.

## Font-evidence reversals

The first long-path `pdffonts` invocation timed out and left an empty evidence
file.  The initial validator lacked a nonempty-inventory guard and therefore
reported a false PASS.  That PASS is rejected and preserved as adverse history.
The validator was amended to require at least one parsed font row.

A short-path, hash-identical copy allowed `pdffonts` to enumerate the reader, but
the first capture/parser combination collapsed the one-space terminal columns;
the tightened validator correctly failed that evidence as an empty parsed
inventory.  That second failure is also preserved.  The parser was then changed
to recognize the exact fixed-width `pdffonts` format.  The final R3 validation
parses 379 rows and passes with zero Type 3 and zero unembedded fonts.

## Visual review

The lead inspected cumulative pages 1, 260, 261, 438, 439, 1908, 1909, and
4177.  These cover the first page, the SGA1→2, SGA2→3, and SGA3→4 seams, and the
terminal page.  All eight surfaces are legible, correctly ordered, unclipped,
and free of workflow/status prose.

## Packaging choices

Only active editable source closures are placed in per-volume source ZIPs.
Generated PDFs, auxiliary files, logs, and accidental scratch directories are
excluded.  Existing current SGA 2 and SGA 3 public source ZIPs are preserved
byte-for-byte.  The cumulative source is honestly delivered as its PDF assembly
builder plus the exact input manifest and validators; no fictitious monolithic
TeX driver is asserted.

The first assembled package root was rejected before manifest freeze.  Its
privacy scanner found four retained control files whose field names or detector
source contained the bare internal workspace marker, and its CSV checker treated
three terminal empty records as zero-width data rows.  No reader PDF or editable
mathematical source failed.  The rejected root is preserved unchanged as R1.
The R2 successor sanitizes those control-only marker strings and makes the CSV
checker ignore wholly empty records while retaining every actual data row.

## Continuation

Archive maintenance owns publication and raw readback under the existing SGA
concept.  The producer owns any later standalone/cross-volume semantic-reference
successor and the broader diplomatic-French/FAC/GAGA program.  This checkpoint
must not be rewritten in place; corrections require an append-only successor.

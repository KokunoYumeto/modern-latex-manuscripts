# Project logbook

## 2026-08-04T01:26:45.3252505Z - intake and ownership

Created the prescribed no-overwrite root only after the full control read,
precedent rehash, handoff replay, local-witness rehash, and live ownership
inspection. `INTAKE_AND_OWNERSHIP.md` is the first production-root record. Live
result: no second Tohoku owner and no overlap with FGA, Verdier, Illusie,
SGA/FAC/GAGA, EGA, Deligne, Noether, CJK, or archive tasks.

## 2026-08-04T01:28Z - official authority snapshot

Downloaded the two exact J-STAGE PDFs once into `authority_snapshot`. Part I is
65 pages / 7,305,283 bytes / SHA-256
`5A8E5720BC2EF8905BF85F7919C65AC4A87A31CFC854BD77E6B5084C0D2DEBEF`.
Part II is 37 pages / 3,984,260 bytes / SHA-256
`8D632A04EE0FA987B40B721BEE6E64BB3E641D6A1CE02335556213F1564C9A53`.
The files are frozen read-only witnesses; no authority or predecessor file was
mutated.

## 2026-08-04T01:33Z - first image comparator, adverse classifier result

The first no-OCR image comparator produced strong SIFT/RANSAC correspondences
on all 102 paired pages but used an over-conservative fixed ratio threshold.
It labelled 1 MATCH and 101 HOLD. The exact adverse output is preserved as
`controls/AUTHORITY_IMAGE_COMPARISON.json`; it was not rewritten to make the
result look successful.

## 2026-08-04T01:44Z - calibrated image replay and resource-protocol event

Replayed every expected page pairing against an adjacent-page negative control.
Result: 102/102 MATCH, zero holds; minimum expected inliers 149; maximum
negative-control inliers 48; minimum expected/control margin 5.729167. The
exact successor output is `controls/AUTHORITY_IMAGE_COMPARISON_R2.json`.

Adverse execution note: asynchronous command yielding obscured two background
session identifiers, so duplicate R2 calibrations were unintentionally started
before the first completion became visible. All processes completed; a process
audit found none remaining. No-overwrite output protection retained only the
first complete R2 JSON and forced duplicates to fail at the existing target.
No authority, TeX, or decision file was altered. Future heavy commands must
capture and poll the returned session identifier before any retry.

## 2026-08-04T01:46:51.6811510Z - direct boundary review and first text unit

At 1,200-dpi-equivalent band detail, lead review confirmed the local physical
p.66 is completely blank. Official Part II begins at printed p.185 with
Chapter IV, no.4.1; its last page is printed p.221 and closes the bibliography.
Official Part I p.1 is printed p.119 and begins with the paper title. Admitted
the complete p.119 text through the open phrase `de sorte` into diplomatic
French, a separately instantiated corrected-French layer with no correction,
and source-aligned English. No OCR was generated or used.


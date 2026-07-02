# Noether R569/R570/R571 Source-Control Chain Update

Date: 2026-07-02

Scope: local Noether German/source-control tail sweep after R570.

## Current Status

- Current packaged local TeX-changing German source-control head: **R571**.
- Latest packaged no-patch source-audit checkpoint before R571: **R570**.
- Prior substantive repair head: **R569**.
- R571 cumulative TeX differs from R570 by one source-certain line: `Bd. III.2` -> `Bd.III.2` in the Leopold Kronecker Werke Bd.III.2 review line.
- R569, R570, and R571 compile with two XeLaTeX passes to 468-page cumulative German PDFs.
- These packages are queued for the next curated Noether rollup under the Zenodo 100-file ceiling.
- They are source-control/support material only: not reader releases, not Noether closure, not whole-corpus certification, not multilingual synchronization, and not critical editions.

## R571

Package: `Noether_R571_LocalCodex_R570_Tail_p773_778_SourceFixAudit_20260702.zip`

- Bytes: `17137860`
- SHA256: `1B49E6A2B9A268D815615A3781A540BE45F2DFFA11EB898C22B4007180D4BE52`
- Cumulative TeX SHA256: `F518B9F1CCD9AA97905F2ECE0CCCF7C590032F1EF390E1988AEB7C00FC14337D`
- Cumulative PDF SHA256: `96E4998648A7F533A408328D667C165B0AAB491DB0824944A4C4DBDB5FE31035`

Confirmed source repair:

- Collected p776 / cumulative output p466: `Bd. III.2` -> `Bd.III.2`.

Evidence:

- Full source pages p773-p778 at 650dpi.
- p776 Kronecker Werke Bd.III.2 targeted crop at 650dpi.
- Source PDF slice.
- Output renders pp462-468.
- Exact diff `audit/diff_R570_to_R571.diff`.

## Public Routing

The public-facing status should say:

> R571 is the latest packaged local TeX-changing German source-control head. It applies one source-certain tail typography repair over R570: collected p776 / cumulative output p466 changes `Bd. III.2` to source-visible `Bd.III.2` in the Leopold Kronecker Werke Bd.III.2 review line. R569 remains the prior substantive p761/p764 repair head; R570 remains the no-patch checkpoint over pp767-772. R569/R570/R571 are queued for curated rollup rather than uploaded loose under the Noether 100-file ceiling. This is source-control/support material only, not a reader release, Noether closure, whole-corpus certification, multilingual synchronization, or a critical edition.

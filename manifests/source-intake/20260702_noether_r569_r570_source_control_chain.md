# Noether R569/R570 Source-Control Chain Update

Date: 2026-07-02

Scope: local Noether German/source-control tail sweep after R568.

## Current Status

- Current packaged local TeX-changing German source-control head: **R569**.
- Latest packaged no-patch source-audit checkpoint after R569: **R570**.
- R570 cumulative TeX is content-identical to R569; `audit/diff_R569_to_R570.diff` is intentionally empty.
- Both R569 and R570 compile with two XeLaTeX passes to 468-page cumulative German PDFs.
- These packages are queued for the next curated Noether rollup under the Zenodo 100-file ceiling.
- They are source-control/support material only: not reader releases, not Noether closure, not whole-corpus certification, not multilingual synchronization, and not critical editions.

## R569

Package: `Noether_R569_LocalCodex_R568_Tail_p761_766_SourceFixAudit_20260702.zip`

- Bytes: `24858162`
- SHA256: `D28566542AFCB16821BCB17B02FBAE250D2C7798220F0F5AD2F2AEB7ADE89CCE`
- Cumulative TeX SHA256: `3A1DF482D9872FFF3EE0E8B6603EF6E5BF84B0C444D143CA20963E57D64DB4F3`
- Cumulative PDF SHA256: `32D1F6877475977F7251362ACCB80C67886DD5DBB4B7AEFDC17A662DC08F3D5E`

Confirmed source repairs:

- Collected p761 / cumulative output p457: `a^S=a` -> `a^{S^r}=a`.
- Collected p764 / cumulative output p459: `(Mit einem Zusatz, gemeinsam mit E. Noether in Goettingen.)` -> `(Mit einem Zusatz, gemeinsam mit E. Noether)`.

Evidence:

- Full source pages p761-p766 at 650dpi.
- p761 small-superscript crop at 1000dpi.
- Source PDF slice.
- Before/after output renders for pp457-459.
- Exact diff `audit/diff_R568_to_R569.diff`.

## R570

Package: `Noether_R570_LocalCodex_R569_Tail_p767_772_NoPatchAudit_20260702.zip`

- Bytes: `22368803`
- SHA256: `AAE81998A028FA37E6E1BA9A87AD109201ED353FF27F4608B19D2DD0A72F2D3C`
- Cumulative TeX SHA256: `3A1DF482D9872FFF3EE0E8B6603EF6E5BF84B0C444D143CA20963E57D64DB4F3`
- Cumulative PDF SHA256: `A2C42083696B9747CEDDCFB3887486E7CDE669C69E45D2A01D07A99AE0D8311C`

No TeX patch promoted. Checked loci:

- Formula (2), equation system (3), and Hilfssatz II conditions.
- Zusatz I/II and Satz III statement.
- Derivative display and Noether Zusatz heading.
- Satz IV and relation displays (4), (5), and (6).
- Bemerkung II end, including the `y^{(K)}` / `y^\lambda` distinction.

No-fix traps:

- Collected p770: tiny subscript in `d_i(y)` line looked visually soft at 650dpi; no source-certain correction promoted.
- Collected p772: Bemerkung II contains both `y^{(K)}` and `y^\lambda`; current TeX preserves that distinction and should not be normalized away.

## Public Routing

The public-facing status should say:

> R569 is the current packaged local TeX-changing German source-control head; R570 is the latest packaged no-patch audit checkpoint. R569/R570 are queued for curated rollup rather than uploaded loose under the Noether 100-file ceiling.
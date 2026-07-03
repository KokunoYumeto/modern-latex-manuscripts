# Noether R687 P40 Source-Fix Promotion

Date: 2026-07-03

Local path:

`C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Noether Multilingual\Noether_R687_P40_DirectArticleSourceAudit_work\Noether_R687_LocalCodex_P40_DirectArticleSourceAudit_SourceFix_20260703`

## Scope

Paper 40, `Nichtkommutative Algebra`, Math. Z. 37 (1933), printed pp. 514-541.

Source authority: clean GDZ article-level PDF `PPN266833020_0037/LOG_0050.pdf`, rendered locally at 650dpi for checking.

## Promoted Fix

One source-backed TeX repair was promoted:

- Printed p537 / cumulative line 19668 / output PDF p384: the displayed direct-sum formula begins with source `Z_\Omega`, not plain `Z`.
- Old TeX: `Z=r^{(1)}+\cdots+r^{(n)}`
- New TeX: `Z_\Omega=r^{(1)}+\cdots+r^{(n)}`

## Build / Evidence

- XeLaTeX passed twice.
- Repaired cumulative German PDF: 466 pages.
- Rendered QA pages: output p384 and p385.
- Included locally: exact R686-to-R687 diff, confirmed-fix ledger, P40 page-disposition ledger, source-quality ledger, 29 source page renders at 650dpi, compile logs, and provenance hashes.

## Hashes

- `cum_de_R687.tex`: SHA256 `44F125D39AD31A2D9B3A81F4EADA313C2DCC7A248FFEAB7343AF8EADBE6E8DBF`
- `cum_de_R687.pdf`: SHA256 `B0F8C9674CD39D6E649F77890B7E307B4CCF9F6F95B881D75EF28EC292B23A9E`
- `README_R687.md`: SHA256 `E8D5A243A7F0423AAFD3727B5BF12DF4D92B70C3AAC87A95292469A56BCF77E0`

## Public Handling

R687 is a narrow source-control repair, not a reader release, not Paper 40 closure, not Noether closure, not whole-corpus page-by-page certification, not multilingual synchronization, and not a critical edition.

Because the Noether record is at the 100-file ceiling, R687 should be folded into a curated Noether rollup with R685/R686 rather than uploaded as loose micro-files.

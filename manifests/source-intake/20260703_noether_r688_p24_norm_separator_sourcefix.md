# Noether R688 P24 Norm-Separator Source Fix

Local path:

`C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Noether Multilingual\Noether_R688_P24_NormSeparator_Audit_work\Noether_R688_LocalCodex_P24_NormSeparator_SourceFix_20260703`

## Status

R688 is a narrow TeX-changing source-control repair on top of R687. It resolves one Paper 24 norm-separator locus from the earlier R632-R636 open-item trail. It is not a reader release, not Paper 24 closure, not Noether closure, not whole-corpus page-by-page certification, not multilingual synchronization, and not a critical edition.

Because the Noether Zenodo record is already at the 100-file ceiling, R688 should be folded into the next curated Noether rollup with R685/R686/R687/R688 rather than uploaded as loose micro-files.

## Promoted Fix

Paper 24, printed p. 234 / source PDF page 239 / R687 cumulative line 13755 / output PDF page 249:

- Previous TeX: `N(\frakG_{i-1}\mid\frakM_{i-1})`
- Repaired TeX: `N(\frakG_{i-1},\frakM_{i-1})`

The neighboring ideal norm `N(\frakg_{i-1}\mid\frakg_i)` remains unchanged. Later ideal-norm occurrences checked in this narrow pass remain vertical bars.

## Evidence

- Full Paper 24 source context rendered from `PPN235181684_0090.pdf` at 650 dpi for source PDF pp.234-266.
- Targeted printed p.234 source evidence rendered/cropped at 1000 dpi.
- R687-to-R688 exact diff included locally as `1/03_audit/diff_R687_to_R688.diff`.
- CSV ledgers included locally: confirmed fixes, source quality, norm-separator audit, visual dispositions.
- Output render checks included locally for the changed area: output pages 249-250.

## Build

XeLaTeX pass 1 and pass 2 both exited 0. The cumulative German PDF remains 466 pages.

## Direct Hashes

- `cum_de_R688.tex`: SHA256 `EDF2F7DDBF3661AD28AB1E1EF11936ECAAA64924E0D9D0E419AFFE80A2BCC3E0`
- `cum_de_R688.pdf`: SHA256 `165C4DC9BACC1865C52E729F00529378328BEA4D57B2595EBE3615DAA9C4A919`
- `cum_de_R688_pdfinfo.txt`: SHA256 `D5779CEF249238786425A0BF4A0390C47B976B0AFE15DE73CA5B1518CABE0C9B`
- `PPN235181684_0090_host_source.pdf`: SHA256 `B64F8EA34E61637632620EED57374F73F9D981DC17DAE6AF7E0527357DE185EA`

## Public Wording

Treat R688 as the current latest inspected Noether source-control/support addition in the R685/R686/R687/R688 chain: R685/R686 remain no-patch source-support layers, R687 remains the narrow P40 `Z_\Omega` source fix, and R688 adds one narrow P24 norm-separator source fix. None of these packages should be represented as a critical edition or whole-corpus certification.

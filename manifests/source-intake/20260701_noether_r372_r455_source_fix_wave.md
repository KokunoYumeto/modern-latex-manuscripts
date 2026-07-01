# Noether R372-R455 source-fix/source-audit wave intake - 2026-07-01

This intake records the local Noether source-fix/support wave found after R371.

- Local root: `C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Noether Multilingual`
- Inventory CSV: `20260701_noether_r372_r455_source_fix_wave_inventory.csv`
- Inventory JSON: `20260701_noether_r372_r455_source_fix_wave_inventory.json`
- Artifact count: 86 ZIPs
- Total size: 2,757,241,222 bytes
- Current local candidate: `Noether_R455_LocalCodex_R454_P15p140_SourceInlineFormulaFix_20260701.zip`
- Current candidate size/hash: 53,589,469 bytes; SHA256 `CF0ED3C8B19984A4DED998FA1D23D3CE2A1AB26B4832EB2764B6891A280ACCC7`; 97 entries
- Web rollup checked and subsumed: `Noether_R280_Complete_P14_p182_191_SourceFix_20260701.zip`

## Scope

The wave covers localized Noether German-source audit/fix/support packets from R372 through R455, with a separate Web R280 Paper 14 pp.182-191 rollup. The active local branch is R455. R454 records that Web R280 needed no new local TeX patch because its Paper 14 pp.182-191 fixes were already present in local R454, which was already ahead through p.201. R455 then starts Paper 15 source checking and applies one source-layout fix on printed p.140.

## Human-Facing Disposition

Do not present this wave as a critical edition, Noether closure, multilingual synchronization, or complete page-by-page certification. It is a source-fix/source-audit provenance wave. The reader-facing archive should front compact current readers and coherent rollups, not every intermediate local ZIP. The full inventory remains useful for provenance, audit replay, and deciding which support packets should be compacted into a later public Noether repair/source-audit release.

## Current Candidate Caveat

R455 compiles with XeLaTeX in two passes and reports a 473-page cumulative German PDF. Its source witnesses for Paper 15 printed pp.138-140 are GDZ 400ppi, usable for the recorded inline-formula layout correction, but dense or ambiguous mathematics in later Paper 15 work should receive zoomed crops or better-source search before promotion.


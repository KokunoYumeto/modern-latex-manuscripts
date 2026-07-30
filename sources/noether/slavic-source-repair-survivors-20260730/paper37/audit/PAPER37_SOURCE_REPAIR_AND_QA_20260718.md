# Noether Paper 37 Slavic source repair and QA

## Scope

This checkpoint repairs three source-visible readings that were already correct in the current German authority but still missing or wrong in the four active downstream Paper 37 bodies: Latin Interslavic, Cyrillic Interslavic, Russian, and Ukrainian.

It is a bounded source-critical repair. It does not certify every Paper 37 sentence, formula, or translation choice.

## Source adjudication

The best staged GDZ witnesses were opened directly.

- Printed p. 147 visibly contains `Von Emmy Noether in Gottingen.` beneath the citation.
- Printed p. 150 visibly gives the basis as `v_1,...,v_t`, not `v_1,...,v_l`.
- Printed p. 151 visibly contains `[vgl. 2a)]`.

The original 1932 print is correct at all three loci. These are inherited transcription or abridgement defects, not errors by Noether. The broader RA08 audit is retained to prevent the same historical restoration from being counted again as new work.

## Applied repairs

Each active body received exactly three one-occurrence changes:

1. Restore the German author line as bibliographic source text.
2. Replace `v_l` with source `v_t` in the Galois-module basis.
3. Restore the cross-reference to 2a), with the abbreviation localized per language.

Exact post-repair TeX hashes:

| Language | SHA-256 |
| --- | --- |
| Latin Interslavic | `077AEEC28B65B8410CE09F4350B71F90E4A355771B63838BBA8BB8F4FC313167` |
| Cyrillic Interslavic | `3F63F9C6C581BBC7140A64107113CDB54C08A50D1C2590A6632E43A5BCC0A35A` |
| Russian | `5A71A3021C7D0B3A5D592C8023E9647024DBEAC0678B1A9BED0DE434D5A5D9BA` |
| Ukrainian | `B44905D156A03D6B61035EBA174A77D952F88166E8DBB8A5144CADA097233C45` |

## Build and visual QA

All four TeX units compiled twice with XeLaTeX. Each produced a five-page PDF. The compile scan found zero fatal errors, undefined controls, rerun warnings, overfull boxes, or underfull boxes.

All twenty output pages were rendered at 240 dpi and visually inspected. The author line, `v_t`, and localized 2a) reference were also inspected in focused output crops for each language. No blank page, clipping, overlap, missing glyph, or broken display was observed.

The four-language locus contact has SHA-256 `93E1F79A5D3AB08E606D8368E07F2719FD6A2C2B48A4ABE901D61609F8E1AAE7`.

## Reproducibility issue found

The live structural index still named older Paper 37 hashes and therefore was not a valid immediate preimage ledger. The exact immediate pre-edit bodies were reconstructed by reversing only the three unique changes and are retained under `07_prechange/`. The stale-index hashes, reconstructed preimages, and post-repair hashes are compared in `PAPER37_PRE_POST_HASH_MANIFEST_20260718.csv`.

The first compile invocation also repeated the known output-directory interpolation failure and wrote to literal `$out` directories. Those outputs were not accepted or moved. The accidental directories were removed after verification, and all four units were rebuilt twice into their exact intended directories.

## Remaining caveat

The current German article already contains these three restorations and was not changed. This package closes downstream propagation of these loci only. A later cumulative rebase must preserve the repaired readings and consult both the positive repair ledger and the negative-control ledger.

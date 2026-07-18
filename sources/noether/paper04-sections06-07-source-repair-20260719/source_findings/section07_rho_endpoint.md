# Noether Paper 4 §7 — confirmed R823 rho-endpoint source defect

Alert ID: `N04-S07-SOURCE-DEFECT-RHO-ENDPOINT-005`  
Recorded: 2026-07-18  
Status: confirmed against the original print and the surrounding R823 argument; downstream source-control propagation required  
Classification: R823 mathematical endpoint/quantifier transcription defect, not a target-language preference

## Exact locus

- Work: Emmy Noether, Paper 4, §7, series-expansion setup before formula (47).
- R823 locator: line 4121.
- Original locator: printed page 142; physical source-PDF page 25.

R823 line 4121 reads:

```tex
... eine Reihenentwicklung f"ur Formen mit $\rho$ ($\rho<n$)
kogredienten Reihen $\xi$; ...
```

The original print unambiguously has the inclusive endpoint
`\rho\le n`, printed as `\rho (\rho <= n)` in the same paragraph. The
source-audited English must therefore restore `\rho\le n` and disclose the
R823 defect immediately. The current pre-audit English draft repeated
`\rho<n`; that downstream contamination is being repaired and is not evidence
for the German reading.

## Internal mathematical corroboration

The inclusive printed endpoint is also required by the later R823 argument:

- formula (54), R823 lines 4198--4202, explicitly states
  `\qquad(\rho\le n)`;
- R823 line 4213 explicitly treats `\rho=n` in the first step of process (55);
- R823 line 4220 again begins the case `\rho=n`.

Thus R823 line 4121 is both print-divergent and internally inconsistent. This
alert establishes the transcription delta and its local coherence; it does not
claim specialist certification of the whole argument.

## Authority and evidence

- R823 cumulative editable German:
  `private-source/Noether_R823_cum_de.tex`
  - 2,125,031 bytes
  - SHA-256: `EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21`
  - complete §7 slice, lines 4112--4268: 13,024 bytes; SHA-256
    `6A693F9E3936CDD0EC07DE8B66C925839CA989FC5D80932D5D8916E5B1AD5CFA`
    (UTF-8 lines joined with CRLF plus terminal CRLF; no source-body slice file
    was created).
- Dedicated original 38-page journal scan:
  `private-source/paper_04_crelle139_pp118_154_ORIGINAL.pdf`
  - 72,444,867 bytes
  - SHA-256: `D7F7CE6D4B311FFD968ED47DC9C1478CFFCF9F446A86BF90263E0C9D1B41C9EF`
- Durable complete 300-dpi physical-page-25 / printed-page-142 render:
  `private-source/physical-25.png`
  - 1,382,597 bytes; 1944 × 2825 pixels; 300 dpi
  - SHA-256: `DB9F523FBA3533D1371C1B5F5499DE19349BDB9800CDDCFA5C3AD405D57F2699`
- Temporary audit-only zoom crop:
  `private-source/physical25_rho_crop2.png`
  - 568,641 bytes; 3200 × 900 pixels
  - SHA-256: `A62B791CD1459E12B9BF83ECCB2245435FEEAAADEE870481C8DF2D441ECE1FFF`
  - This temporary crop is a locator aid, not durable public evidence.

## Propagation rule

1. Record R823 line 4121 as an editable-German mathematical source defect,
   distinct from the four dotted-symbol defects later in §7.
2. Correct the German authority only through its owning source-governance
   workflow, preserving append-only before/after hashes and decision IDs.
3. Restore `\rho\le n` in every downstream Paper 4 §7 target; record any
   inherited or newly produced `\rho<n` as a target regression, not
   corroboration.
4. Link formula (54) and the two explicit `\rho=n` passages as internal
   cross-reference evidence in the typed graph.
5. Return the corrected German/source-control hash and downstream disposition
   IDs after the authority owner acts.

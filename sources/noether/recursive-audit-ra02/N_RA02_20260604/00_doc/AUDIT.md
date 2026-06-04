# RA02 audit note

## Audit rule

Order of authority for recursive repair:

1. German source against scan.
2. Correct German TeX if the scan shows a source-level mismatch.
3. Propagate the same mathematical/source correction into English, Spanish, and Japanese.
4. Rebuild cumulative PDFs and record diffs/renders.

The working instruction remains: no summary substitution, no screenshot substitution, and no silent omission of hard tables/diagrams.

## Papers covered in this packet

### Paper 01

Carried forward from RA01. The RA01 check found no immediate Paper 01 cumulative rewrite requirement. The RA01 Paper 01 audit note and German TeX are included under `09_back/p01/` for continuity.

### Paper 02

Paper 02 was checked against the scan witness pages 45--113, with formula-sensitive attention to the previously preserved anomalies and the two tables. One real source-to-TeX mismatch was found and corrected.

#### Correction applied: scan page 51, formula (10), derivation block

In the derivation of formula (10), the scan shows hatted nu factors, `\widehat{\nu}x^2`, not plain `\nu x^2`, and not the malformed literal `u x^2`. This affects ten occurrences in the derivation block: a), b), b'), and c).

Corrected in:

- German cumulative TeX/PDF.
- English cumulative TeX/PDF.
- Spanish cumulative TeX/PDF.
- Japanese cumulative TeX/PDF.

The unified diffs are in `02_diff/`, and the corrected formula snippets are in `08_snip/`.

#### Confirmed source anomaly retained: scan page 69

The line `Formen H_j^2, H_j^2` is scan-visible and was not normalized. The duplicate remains source-faithful in the cumulative branches.

#### Tables

The earlier repair of the two Paper 02 table pages is retained in all four cumulative PDFs. The tables remain standard A4 portrait pages, with editable TeX table bodies. No table-cell rewrite was made in this RA02 pass.

## Next recursive target

Start RA03 at Paper 03 and proceed forward: German-to-scan audit first, then English/German/Spanish/Japanese cumulative propagation. Particular attention should be paid to formula labels, hatted symbols, omitted footnote material, and old OCR-derived plain-letter substitutions inside math.

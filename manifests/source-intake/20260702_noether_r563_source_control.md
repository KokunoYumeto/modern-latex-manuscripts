# Noether R563 Local Source-Control Receipt

Date: 2026-07-02

Local artifact:

`C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Noether Multilingual\Noether_R563_LocalCodex_R562_Tail_p725_730_SourceFixAudit_20260702`

Role: current local TeX-changing German source-control head, with a very small tail repair over R562. This is not a reader release and not a critical-edition claim.

## Scope

R563 is a one-locus tail source-style repair on top of R562. The direct TeX diff against R562 changes:

```tex
\emph{Beweis.} 1.
```

to:

```tex
\emph{Beweis} 1.
```

in the tail printed p725-p730 source-audit span. R562 remains the richer ledged Paper 40 pp.530-535 source-control package underneath R563.

## Evidence Present

- Cumulative German TeX: `cum\cum_de_R563_tail_p725_730_sourcefix.tex`
- Cumulative German PDF: `cum\cum_de_R563_tail_p725_730_sourcefix.pdf`
- Local package README: `README_R563.md`
- Build logs: `cum\xelatex_R563_pass1.log`, `cum\xelatex_R563_pass2.log`, and full log
- Source witness PDF: `source_witnesses\Tail_R101_actual_slice_starts_collected_p711.pdf`
- Source witness PNGs: collected p725-p730 renders plus p729 1000dpi zoom
- Audit/provenance: confirmed fixes CSV, visual dispositions CSV, source-quality CSV, source mapping, exact R562-to-R563 diff, full post-R563 German source-audit logbook snapshot, and SHA256 file list
- Local ZIP now created for the next curated rollup: `Noether_R563_LocalCodex_R562_Tail_p725_730_SourceFixAudit_20260702.zip`

No standalone JSON manifest was observed inside the local R563 package folder at intake time; this repository receipt supplies that machine-readable manifest.

## Verification

- R562-to-R563 TeX diff: 1 insertion / 1 deletion
- PDF page count: 468 pages
- Pass-2 log scan: no fatal, runaway, missing-dollar, or unresolved-reference hits; only font-substitution warnings were found
- Cumulative TeX SHA256: `25DA49C074DA9768A87021EBAF99F2631CA285E1F7473C80F123C876A2031F54`
- Cumulative PDF SHA256: `F367726894134BAFB754C8396ADC1F94D7DC50F2A6AD907E9EDDF64EE385B3A5`
- Source witness PDF SHA256: `F98C16E6529BC4C24F8D1CDC087B48825FD71173EB18F0C1A25D0D1508B8F9B0`
- Local ZIP SHA256: `CDAF9FB0F73B05E1C323A339F49EA75A6B0C1E667F258C0BD21D194E5161F7CC`

## Public Caveat

R563 may be described as the latest local TeX-changing German source-control head, but only as a very small tail source-style repair over R562. It should be queued for a curated Noether rollup rather than uploaded loose while the Noether Zenodo record remains at the file ceiling. It is not Noether closure, whole-corpus certification, multilingual synchronization, a reader release, or a critical edition.

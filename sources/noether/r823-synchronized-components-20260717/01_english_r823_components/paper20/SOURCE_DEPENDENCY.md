# Noether Paper 20 English synchronization: source dependency

Date: 2026-07-17

## Translation lineage

The English working file is a revision of the previously audited English
control slice, not a fresh untracked translation. The baseline and source
controls copied into this package are:

- `source/Noether_Paper20_English_FINAL_AUDITED_control_slice_20260614.tex`
  - SHA-256: `AD2197BD392E947FF33A6E71009EA93CE0797730BC3A59E9275AF7716CA16912`
- `source/Noether_Paper20_German_FINAL_AUDITED_control_slice_20260614.tex`
  - SHA-256: `7C65D1DD57456036B4A05BAAB6A16B260F6A3366AE103CE1C5D51414AA7B53F4`

## Current German authority

The current cumulative authority is the R823 German TeX:

`C:\Users\Floris\Documents\interlanguage\03_projects\noether\03_translation_workspaces\romance_rebase_20260717\authority_r823\pkg_r823\Noether_R823_WebB_R822_P20p27_31_RunInDashRefine_20260717\1\01_cumulative\Noether_R823_cum_de.tex`

- SHA-256: `EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21`
- Paper 20 exact extraction in this package:
  `source/Noether_Paper20_German_R823_authority.tex`
- Extraction SHA-256:
  `44A8343BD50B9178737D4AAB6A70BDD17E92B0BACB0172294F443E1F1DB33E10`
- Extraction method: `scripts/noether_extract_paper.py --paper 20`.

## Primary facsimile evidence

The primary scanned article used to adjudicate R823 notation and layout is:

`C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Noether Multilingual\Noether_LocalCodex_after_WebR270_P20_FullVisual_SourceAudit_20260629\02_source_witnesses\P20_GDZ_article_LOG_0010_absolute_irreduzibilitaet.pdf`

- SHA-256: `CA9E177E60C0A12720C3B5BECAB9356D9A4105430BD187C89CF58E01CEFF2B60`

The 600-ppi images used for the final notation check are:

- printed p. 32, sequence 007:
  `raw_fullres_gdz/P20_seq007_printed32_canvas00000042_full.jpg`
  - SHA-256: `F03EE733FEC221280024EC32BBC69FE9A22D12A107B580E07298BC80A1EA28D6`
- printed p. 33, sequence 008:
  `raw_fullres_gdz/P20_seq008_printed33_canvas00000043_full.jpg`
  - SHA-256: `09DDDE86AB987301A6F6B991AA2AD667592004C0528FFD34D8F21F1F3F309A56`

## Authority decisions

The scan proves the following readings used in the English revision:

- section 5 factorization notation is barred: `\bar H`, `\bar h`,
  `\bar F`, and `\bar G`;
- section 6 deliberately keeps unbarred `E(x)` when naming the degree and
  reducibility form, but uses barred `\bar E(x)` and `\bar E(x,y)` as the
  factorization targets;
- section 7 uses `\mathfrak K`, not `\Omega`;
- the common denominator is `\Delta`, not `\Lambda`;
- the final replacement is `\bar E(x)` by `\Delta\cdot\bar E(x)`;
- the two consecutive displays printed as equation `(12)` are a source
  duplication and are retained, not silently regularized to `(12')`.

Two non-mathematical R823 deviations from the facsimile were recorded rather
than copied into English: R823 has `solcher speziellen` where the scan has
`solcher spezieller`, and R823 extends section 6 opening italics beyond the
phrase italicized in the scan.

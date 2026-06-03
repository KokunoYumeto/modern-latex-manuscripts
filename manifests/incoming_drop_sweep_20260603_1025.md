# Incoming Drop Sweep - 2026-06-03 10:25

This note records the newest local ZIP drops found under
`C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean`.
It is an intake queue, not a claim that every item has already been mirrored or
published.

## Already handled during this sweep

- Cayley Zenodo same-concept patch published as `10.5281/zenodo.20523305`.
  This replaces the Volume IV and Volume X readers and refreshes
  `Cayley_source_and_manifest_20260603.zip`.
- Local Cayley patch helper advanced from record `20522518` to `20523305`.

## Highest-priority public-facing deltas

| Lane | Newest local package | Why it matters | Current action |
|---|---|---|---|
| Sylvester | `Sylvester_Volume_I_Cumulative_bookpp001_283_with_scans_20260603.zip` | Author record is public only through book p. 218; this extends Volume I to book p. 283 with scans and TeX/PDF. | Mirror and patch Sylvester author record next. |
| Noether multilingual | `Noether_Paper17_complete_Paper18_complete_ES_JA_20260603.zip` | Public/mirror state is ES/JA through Paper 15; this advances Spanish/Japanese through Papers 17 and 18, with methodology/glossary deltas. | Mirror after checking cumulative PDFs compile/render; then patch Noether record. |
| SGA | `SGA7_I_pages_097_120_original_source_cumulative.zip` | Public/mirror state is SGA7-I through source p. 96; this extends to source p. 120 with English/French/source cumulative readers. | Mirror and patch SGA record after quick render/source check. |
| Weber | `Weber_Cumulative_ThreeVolumes_Batch68_Vol2_Sections63_66_REFINED_SIZE_CONTROLLED_20260603.zip` | Public Weber is much older; this has Volume I complete, Volume II through §§1-66, Volume III retained. | Keep as accepted cumulative candidate, but Weber aid is outsourced and lower than Cayley/Sylvester/Noether. |
| Ukrainian applied math | `ua_eskf_lie_next_20260603.zip` and `ukrainian_applied_mathematics_eskf_lie_source_translation_continuation_20260603.zip` | Extends the applied mathematics/state-estimation lane after the current Zenodo update. | Queue a compact same-concept update once several small modules have accumulated. |

## Additional recent deltas

| Lane | Package | Note |
|---|---|---|
| Steinitz | `Steinitz_10_corpus_shortpaths.zip` | New 1899 module packet; Steinitz author record should wait until current bilingual packets are mirrored and checked. |
| Dirichlet | `Dirichlet Round 14 - Jacobi Memorial Clean Cumulative 20260603.zip` | Band II cumulative now includes Paper XXII/Jacobi memorial material; compare against current author record before patch. |
| Deligne | `Deligne_010_Theorie_de_Hodge_II_p031_040_with_cumulative.zip`; `Deligne_Papers_090_Down_Cumulative_New_Paper087_Opening.zip` | Deligne remains curation-gated because previous drops varied in fidelity. |
| Old physics | `Gibbs_Vol1_Representation_by_Surfaces_p033_042_with_cumulative.zip` | New Gibbs lane; needs its own author/physics shelf policy before public promotion. |
| Dedekind | `Dedekind_Round12_Clean_LXVI_LXVII_pp483_504_20260603.zip` | Dedicated Dedekind record exists; queue after checking whether this is cumulative over the current record. |
| Gauss | `gauss_summatio_articles09_20_pp020_032_round17_20260603.zip` | Gauss round 17; current Gauss record is behind recent local work and needs a later cumulative audit. |
| Non-European / al-Battani | `non_eu_albattani_current_head_and_audit_20260603.zip` plus round 32-49 handoff ZIPs | Claude has started a separate CUDA/VLM table-cell reader lane; do not replace the public al-Battani record until table completeness is audited. |

## Side-lane tool note

Claude's al-Battani workspace reports a working RTX 4080 SUPER CUDA install with
Torch 2.6.0+cu124 and a VLM cell-reader test in progress. Treat that as a
reusable workflow experiment for table-heavy historical mathematics. If it
becomes reliable, record the exact dependencies and table-cell protocol in the
workflow DOI rather than burying it in an author-specific packet.

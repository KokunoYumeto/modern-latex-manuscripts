# Work pass 2026-07-05 — source-body intake, C2 fill probes, normalization queue

This pass continues the measurable interlanguage map without treating any generated or draft material as certification. It uses the new source-body packages as source-body probes and converts the F13 normalization evidence into a review queue.

## 1. Source-body package intake
- **romance_es_fr**: 1526 files; 1414 scanned text-like files; languages {'fr': 266, 'es': 1258, 'romance_unknown': 2}; use categories {'language_family_witness_candidate': 1524, 'source_body_uncertain': 2}.
- **slavic_support**: 1194 files; 1194 scanned text-like files; languages {'isv': 528, 'slavic_support_unknown': 18, 'de': 54, 'en': 50, 'ru': 272, 'uk': 272}; use categories {'interslavic_community_reference_candidate': 4, 'generated_or_review_support_internal_consistency': 1188, 'source_body_uncertain': 2}.
- **cjk_zh_ja**: 196 files; 164 scanned text-like files; languages {'zh': 194, 'cjk_unknown': 2}; use categories {'language_family_witness_candidate': 194, 'source_body_uncertain': 2}.
- **rtl_persian_arabic**: 1253 files; 1240 scanned text-like files; languages {'fa': 1247, 'ar': 4, 'rtl_unknown': 2}; use categories {'language_family_witness_candidate': 1226, 'source_body_uncertain': 13, 'draft_or_review_packet_not_witness': 14}.
- **pkg344_345**: 104 files; 98 scanned text-like files; languages {'unknown': 104}; use categories {'source_body_uncertain': 104}.

## 2. Pan-Romance C2 source-body probe
- The curated ES/FR source-body probe now gives witness-candidate hits for **33/39** Pan-Romance C2 missing rows; the six remaining gaps are specialized Noether terms requiring more focused historical/specialist source intake.
  - gap: `absolutely complete system` (noether_corpus)
  - gap: `biquadratic form` (noether_corpus)
  - gap: `form system` (noether_corpus)
  - gap: `relatively complete system` (noether_corpus)
  - gap: `ternary form` (noether_corpus)
  - gap: `transvection` (noether_corpus)

## 3. CJK and RTL probes
- RTL/Persian-Arabic C2 probe rows: 32; status counts {'gap_after_current_sourcebody_probe': 22, 'witness_candidate': 4, 'non_witness_or_uncertain_hits_only': 6}.
- CJK seed probes: 32 concepts with Chinese/Japanese source-body hits. These are source-body markers only, not a CJK bridge proposal.

## 4. Normalization queue
- Normalization rows: 67; action bands {'R2_pan_anchor_with_aliases': 20, 'R1_review_doublet_required': 21, 'R3_orthographic_or_unclassified': 20, 'R0_homograph_or_four_way_review': 3, 'R1_branch_specific_unbalanced': 3}.
- High-leverage review class: W/S doublet rows and homograph/four-way rows; no text patch or single-standard normalization is made in this pass.

## Boundary
- `language_family_witness_candidate` means “eligible for row-context review,” not “certified witness.”
- `generated_or_review_support_internal_consistency` and `draft_or_review_packet_not_witness` are discovery/consistency layers only.
- Normalization action bands are decision support only.
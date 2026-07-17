# Source dependency: Noether Paper 5

Date: 2026-07-17

## Authority and routing order

1. The four original JDMV/GDZ pages govern the title punctuation and note,
   byline, prose, page-local source notes, formulas, mathematical wording, and
   the contribution boundary above the rule on printed page 319.
2. The max-source-probe package routes the correct four GDZ canvases and
   records their dimensions, printed-page mapping, full-page visual audit,
   source-quality limit, and no-import boundary. It is an audit descendant of
   those pages, not an independent German witness.
3. The current R823 German block is the source-control transcription. The
   package extraction is byte-identical, with LF line endings, to cumulative
   source lines 4509--4546.
4. The RA10 cumulative English and the exact package extraction are one
   inherited translation cohort. They supply candidate prose continuity but
   cannot override the German pages or establish independent English use.
5. Other synchronized Noether translations, especially Paper 6, are
   same-project register controls for the three basis terms and the historical
   `Lagrange genus domain` wording only. They are not independent target
   witnesses.
6. Compile, text extraction, page rendering, and spreadsheet checks validate
   the promoted output only; they do not supply source or target wording.

## Typed evidence nodes and edges

| Node | Type | Channel | Permitted role |
|---|---|---|---|
| `source:p05-gdz-316-319` | primary printed source | source-content | Wording, apparatus, formula, layout, boundary |
| `audit:p05-max-source-probe` | dependent source audit | source-content | Canvas routing, source-quality limit, page map, no-import check |
| `source:p05-r823` | source-control transcription | source-content | Current German normalization |
| `candidate:p05-ra10-en` | inherited translation | target-text | Candidate discovery and continuity |
| `control:p05-p06-en` | same-project translation | target-register | Internal field-theory register consistency only |
| `adverse:p05-modern-number-field` | rejected target sense | adverse-target | Prevents modern finite-number-field narrowing of `Zahlkörper` |
| `adverse:p05-integral-rational` | rejected target wording | adverse-target | Prevents obscuring polynomiality in `ganze rationale Verbindung` |
| `adverse:p05-haentzschel-import` | rejected source boundary | adverse-source | Prevents importing the following article from page 319 |
| `qa:p05-compile-render` | deterministic validation | output-QA | Build, extraction, spreadsheet, and visual validation only |

Typed edges are: the GDZ pages `audited_by` the max-source probe and
`transcribed_as` R823; the source audit `confirms_current_span` and
`confirms_boundary`; RA10 `supplies_prior_candidate`; Paper 6
`routes_same_project_consistency`; the source pages
`reject_modern_number_field_narrowing`, `reject_integral_rational_calque`, and
`reject_following_article_import`; and the promoted English artifact is
`validated_by` compile/render/spreadsheet QA. No scalar score selects a
translation.

## Declared dependence tree

```text
Noether Paper 5 evidence families
├── original JDMV/GDZ article, printed pp. 316--319
│   ├── GDZ article PDF and IIIF page files (same German root witness)
│   ├── max-source-probe page map and visual audit (dependent audit)
│   └── R823 German transcription and package extraction (dependent descendants)
└── project translation family
    ├── RA10 cumulative English (inherited candidate)
    │   └── package Paper 5 extraction (exact dependent extraction)
    └── synchronized Paper 6 English (same-project register sibling)
```

The article PDF, four page JPEGs, audit ledgers, and R823 block are dependent
members of one German-source family. The RA10 cumulative and package
extraction are one English candidate cohort, not two translations. No
independent native-English target-domain witness is asserted for this
component; project-register terms therefore remain controlled candidates
pending external review.

## Exact witnesses and hashes

Current R823 cumulative German authority:

`C:\Users\Floris\Documents\interlanguage\03_projects\noether\03_translation_workspaces\romance_rebase_20260717\authority_r823\pkg_r823\Noether_R823_WebB_R822_P20p27_31_RunInDashRefine_20260717\1\01_cumulative\Noether_R823_cum_de.tex`

- full SHA-256:
  `EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21`;
- Paper 5 spans source lines 4509--4546;
- package extraction:
  `source/Noether_Paper05_German_R823_authority.tex`;
- exact extraction SHA-256:
  `1787B8C3FB7C501C8559D2F120A136C4C71F45A033613F8A5562257411C3E5AE`.

Original printed pages and source audit:

`C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Noether Multilingual\Noether_LocalCodex_after_WebR252_P05_GDZ600_MaxSourceProbe_NoPatch_on_PromotedBase_20260628`

- article PDF SHA-256:
  `12B98431ADE022866CE8234610B634604D2AD06094287A083A71587446C565AD`;
- printed page 316 / canvas 325 SHA-256:
  `5389B4408B128E4BE86898CAB23905ABDD36C52411464C342877C9DB21FD230F`;
- printed page 317 / canvas 326 SHA-256:
  `AFD68BAD6E62C3628BC4A9706CB16096E0462C5FA507CA8964C801D01BD0A62C`;
- printed page 318 / canvas 327 SHA-256:
  `61D0A311323DEB09E4520E4C2C00E3E6C064EC6A9F8CDA8675B748D3B627264C`;
- printed page 319 / canvas 328 SHA-256:
  `A01B272DB14176ED2368B9CF3A9E5A56A7A2C44E3C22A210A6EB4238ACFD4F67`;
- all four pages are 3248 x 5223 pixels at 600 ppi;
- audit README SHA-256:
  `B5ABEF347542AFDE709BEE31E7794DCBD84DC4606F93604749518EAA04E468BD`;
- full-page disposition ledger SHA-256:
  `76C8AD29E50EBAA71316687F74446CE0F0EDC16A2C454929ED23305D5758D0CA`;
- max-source disposition SHA-256:
  `9C15544B90E470EEBEBFD9A1AC1558F8F5FAC96CD871150C9EF77B4B96D02978`.

Prior English control:

`C:\Users\Floris\Documents\interlanguage\03_projects\language_management\english_germanic\01_recovered_witnesses\noether_ra10_complete_english\Noether_RA10_cumulative_English.tex`

- full RA10 cumulative SHA-256:
  `2BDB5EAB5DB6D7A46CF10EC8C99F720320A956EF866B473DAE4C28F8F49BF6C9`;
- exact package extraction, cumulative lines 4252--4287, SHA-256:
  `35A753F21E351B9358C9FB7558090BF5DBFC476139FEE4D1FAEB74E46E5DA8AA`.

All four complete source pages, the current R823 block, inherited English
control, extracted final PDF text, and both complete final renders were
inspected. This is an internal source-fidelity result; external review and
human-comprehension testing remain pending.

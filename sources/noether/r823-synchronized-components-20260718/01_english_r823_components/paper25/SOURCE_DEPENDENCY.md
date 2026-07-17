# Source dependency: Noether Paper 25

Date: 2026-07-17

## Authority order

1. The original JDMV/GDZ journal scan governs printed content, notation,
   apparatus, and the article boundary.
2. The current R823 German source is the source-control transcription and must
   agree with that scan at every disputed locus.
3. The complete RA10 and editable standalone English files are translation
   controls. They are prior candidates, not independent source witnesses.
4. Paper 24 is a sibling English terminology control for recurring technical
   terms; it is not independent evidence for Paper 25's German content.
5. The later collected-edition facsimile is adverse evidence at the opening
   apparatus and barred-field loci and does not govern those readings.

## Typed evidence nodes

| Node | Type | Channel | Role |
|---|---|---|---|
| `source:p25-jdmv-original` | primary printed source | source-content | Governs title, lecture/byline/note, congruence, barred field, and boundary |
| `source:p25-r823-extract` | current source-control transcription | source-content | Propagates the printed readings into the current German authority |
| `candidate:p25-ra10-english` | inherited translation candidate | target-text | Supplies the complete English body for adjudication |
| `candidate:p25-standalone-english` | editable inherited candidate | target-text | Supplies the compilable standalone base |
| `control:p24-english-terminology` | declared sibling terminology control | target-register | Routes greatest-primary and fundamental-ideal wording |
| `adverse:p25-collected-facsimile` | later dependent reproduction | adverse-source | Records omitted apparatus and omitted overbar; rejected where it conflicts |
| `qa:p25-compile-render` | deterministic technical validation | output-QA | Validates the promoted TeX/PDF, not linguistic community acceptance |

Routing edges are typed and channel-separated: the original scan
`supports_decision` for source readings; R823 `transcribes` the scan; each
English control `supplies_prior_candidate`; Paper 24 `routes_terminology`; the
collected facsimile `records_adverse_variant`; and the final candidate
`validated_by` compile/render QA. No scalar score selects a reading.

## Declared dependence tree

```text
Noether Paper 25 source family
├── original JDMV/GDZ journal issue (independent root witness)
│   ├── R823 German transcription (dependent source-control descendant)
│   ├── 1000 dpi opening crop (dependent diagnostic crop)
│   └── native600 p.119 crop (dependent diagnostic crop)
├── later collected-edition facsimile (dependent reproduction; adverse loci)
└── English translation family
    ├── complete RA10 cumulative translation (inherited candidate)
    ├── editable standalone extraction (dependent packaging descendant)
    └── Paper 24 English (sibling terminology cohort only)
```

The crop count does not create independent source breadth, and the two English
files do not create two independent translations.

## Exact witnesses and hashes

Current R823 cumulative German authority:

`C:\Users\Floris\Documents\interlanguage\03_projects\noether\03_translation_workspaces\slavic_r823_book_reconciliation_20260717\authority\Noether_R823_cum_de.tex`

- full SHA-256:
  `EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21`
- exact package extraction:
  `source/Noether_Paper25_German_R823_authority.tex`
- extraction SHA-256:
  `60F3335CA5AB41A5D660E54983261ADAA0506334ABBD81A61D15A53B8F3B7258`

English controls:

- `source/Noether_Paper25_English_standalone_control.tex`
  - SHA-256:
    `5CF60297F40C3CBD88B4DC6AED68EB9B675BBAC604CA9C8B0F1B89CD0083BFDD`
- `source/Noether_Paper25_English_RA10_control.tex`
  - SHA-256:
    `6999C9C189E07F2D8F3431188A6AAF9862E8AD32D2535731DA0F8EEDF76CAE39`
- full RA10 cumulative SHA-256:
  `2BDB5EAB5DB6D7A46CF10EC8C99F720320A956EF866B473DAE4C28F8F49BF6C9`

Original journal scan:

`C:\Users\Floris\Documents\Codex\2026-06-01\we-are-currently-doing-a-massive\Noether_R124plus_P25_p119_GaloisFieldOverbarFix_WebDrop_20260625\source\Noether_P25_GDZ_JDMV33_1924_LOG_0016_pp116_120.pdf`

- SHA-256:
  `0C5FE4E6735636A34C8DD34D16969C5A1E1659523F8840A9B8428F1A70D8E219`
- PDF page 1 is the GDZ cover; printed pp. 116--120 are PDF pages 2--6.

Diagnostic crops:

- opening/header 1000 dpi SHA-256:
  `57D6B20A5699799CA66CF033FB6D52180EAB98F02D176FDB95F98602DFCE87C7`
- p. 119 barred-field native600 SHA-256:
  `33054F6C18F25F14E79859A382B6CBD6B71A0C8CCEB89505F448FCDEA68E8E90`

Adverse later facsimile:

`C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Noether Multilingual\Noether_Source_Files_Addendum_20260616\_stage_unique_files\files\pdf\b867546021b1edb3_Noether_Paper25_SOURCE_SCAN_pages491-495_Eliminationstheorie_und_Idealtheorie.pdf`

- SHA-256:
  `B867546021B1EDB34F39CA2B7BFEF43575199D5DD563939045B687CDF2FBADB8`
- adverse disposition: it omits the original lecture/byline apparatus and the
  p. 119 overbar, so it cannot govern those disputed loci.

All five printed source pages and the two targeted diagnostic crops were
visually reviewed. This proves source fidelity for the adjudicated loci; it is
not external review or community certification of the English translation.

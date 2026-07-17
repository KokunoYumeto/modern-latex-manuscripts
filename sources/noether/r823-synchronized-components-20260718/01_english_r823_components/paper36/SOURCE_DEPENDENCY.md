# Source dependency: Noether Paper 36

Date: 2026-07-17

## Authority and routing order

1. The original JDMV/GDZ page governs the printed item number, wording,
   emphasis, author styling, and notice boundary.
2. The current R823 German block is the source-control transcription. It is a
   dependent descendant of the printed page, not a second independent source.
3. The RA10 cumulative English and its editable standalone are inherited
   translation candidates. They may supply English prose and consistency but
   cannot override the German source or establish independent target use.
4. Andrew V. Sutherland's MIT 18.785 lecture notes are an independent English
   target-domain witness for the technical noun `the different`. They do not
   witness Noether's German text or this historical notice's apparatus.
5. Paper 43 English and the CJK Paper 36 decision records are same-project
   concept and consistency controls only.

## Typed evidence nodes and edges

| Node | Type | Channel | Permitted role |
|---|---|---|---|
| `source:p36-gdz-p17` | primary printed source | source-content | Source wording, item number, emphasis, styling, boundary |
| `source:p36-r823` | source-control transcription | source-content | Current German normalization |
| `candidate:p36-ra10-en` | inherited translation | target-text | Candidate discovery and continuity |
| `witness:mit-different` | native independent English source | target-register | English technical usage of `the different` |
| `control:p43-en` | same-project translation control | target-register | Internal terminology consistency only |
| `adverse:p36-difference` | rejected false-friend form | adverse-target | Prevents ordinary `difference` at the number-theory locus |
| `qa:p36-compile-render` | deterministic validation | output-QA | Build and visual validation only |

Typed edges are: the GDZ page `transcribed_as` R823; R823
`normalizes_source_concept`; RA10 `supplies_prior_candidate`; the MIT witness
`supports_target_form`; Paper 43 `routes_same_project_consistency`; the source
sense and MIT witness `reject_false_friend`; and the promoted English artifact
is `validated_by` compile/render QA. No scalar score selects the form.

## Declared dependence tree

```text
Noether Paper 36 evidence families
├── original JDMV/GDZ page (independent German root witness; 600 ppi)
│   ├── R823 German transcription (dependent source-control descendant)
│   ├── focused diagnostic crop (dependent image derivative)
│   └── 2026-06-25 disposition ledgers (dependent audit records)
├── English target-domain sources
│   └── MIT 18.785 Lecture 12 (independent English usage witness)
└── project translation family
    ├── RA10 cumulative English (inherited candidate)
    │   └── editable Paper 36 standalone (dependent extraction)
    ├── Paper 43 English (same-project terminology sibling)
    └── CJK Paper 36 records (cross-lane concept controls; not English evidence)
```

The crop does not add source breadth, and the cumulative plus standalone do
not count as two English translations.

## Exact witnesses and hashes

Current R823 cumulative German authority:

`C:\Users\Floris\Documents\interlanguage\03_projects\noether\03_translation_workspaces\romance_rebase_20260717\authority_r823\pkg_r823\Noether_R823_WebB_R822_P20p27_31_RunInDashRefine_20260717\1\01_cumulative\Noether_R823_cum_de.tex`

- full SHA-256:
  `EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21`
- Paper 36 starts at source line 18600;
- package extraction:
  `source/Noether_Paper36_German_R823_authority.tex`
- extraction SHA-256:
  `8D098B22C5126EB3B18A9D67E541B7D9569D43DFC3DF9A3D4A0D7F423035870E`

Original printed page:

`C:\Users\Floris\Documents\Codex\2026-06-01\we-are-currently-doing-a-massive\Noether_GeneralSourceLibrary_v1_20260626\part07_P31_P43_upperband_source_witnesses\Noether_R127_LocalCodex_P36_GDZ600_SourceDisposition_NoNewPatch_WebDrop_20260625\source\P36_JDMV39_p017_GDZ_canvas0312_600ppi.jpg`

- SHA-256:
  `767E7207921548D60400C1113C7A76947C5CF5C63A937932B66EDCF4691C966F`
- native dimensions and metadata: 3280 x 5046 at 600 ppi;
- status: best staged original-page witness, below the project 650 ppi
  preference; legible for this complete notice but not strict high-resolution
  certification.

Focused diagnostic crop:

- SHA-256:
  `FE022B6AE5E8B4AC3950C88438943BBD888EFAB0BB51129FABA9497381F65C2F`
- dependent on the GDZ page; used only for inspection.

Prior English controls:

- full RA10 cumulative SHA-256:
  `2BDB5EAB5DB6D7A46CF10EC8C99F720320A956EF866B473DAE4C28F8F49BF6C9`
- package RA10 extract SHA-256:
  `918B4B2084883231F03E542DFE6EFB5193F6098B36BBFF9FB6DE5D17AD7AAD34`
- editable standalone SHA-256:
  `D8D98DC54A2EA064E9F94856FF8532E9099361B233AAC15BEEA3C27E3660B89D`

Independent English target-domain witness:

- Andrew V. Sutherland, *18.785 Number Theory I*, Lecture 12, section 12.1,
  “The different”:
  `https://math.mit.edu/classes/18.785/2021fa/LectureNotes12.pdf`
- permitted use: target-language term support for `the different` only.

The complete printed notice, focused crop, R823 block, and promoted English
render were visually inspected. This is an internal source-fidelity result;
external review and human-comprehension testing remain pending.

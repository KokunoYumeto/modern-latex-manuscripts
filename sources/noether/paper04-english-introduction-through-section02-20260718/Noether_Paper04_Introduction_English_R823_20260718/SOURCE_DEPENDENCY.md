# Source dependency: Noether Paper 4 Introduction

## Authority order

1. The dedicated original 1911 journal scan governs printed framing, byline,
   page-local note marks, emphasis, formula references, ambiguous glyphs, and
   the article boundary.
2. R823 German TeX routes the editable German wording and mathematical
   notation.
3. The searchable collected-work reproduction is a locator and comparison
   witness only. It changes the title framing.
4. The inherited English is one dependent target-language comparison lineage
   and cannot override either German source.
5. Editorial terminology, build, metadata, extraction, and rendering controls
   validate the promoted English artifact only within their declared roles.

## Typed evidence graph

| Node | Type | Permitted role |
|---|---|---|
| `source:p04-original-1911` | primary printed witness | framing, notes, emphasis, ambiguous glyphs, boundary |
| `source:p04-r823` | dependent editable German transcription | source-content routing and notation |
| `witness:p04-collected` | later searchable reproduction | text location and comparison, not original framing |
| `candidate:p04-inherited-en` | inherited target-language descendant | wording discovery and adverse comparison |
| `control:p03-p04-register` | project target-register control | terminology continuity subject to source context |
| `qa:p04-build-render` | deterministic output validation | build, metadata, extraction, and complete visual review |

The original pages are `transcribed_as` R823. The collected reproduction is
`derived_from` the printed work but `changes_framing`. R823 and the inherited
English `supply_controls_for` the revised English. The original
`overrides_framing`, `restores_note_identity`, and `bounds_scope`. Output is
`validated_by` build and render QA. No scalar score or candidate agreement
certifies fidelity.

## Declared dependence tree

    Noether Paper 4 evidence families
    ├── original 1911 Crelle/JRAM scan
    │   ├── physical pages 1–37: Paper 4, printed pp. 118–154
    │   ├── physical page 38: next article, excluded
    │   └── R823 editable German transcription (dependent descendant)
    ├── later collected-work reproduction
    │   └── searchable text and collected pagination 104–140
    └── project English family
        ├── inherited cumulative English candidate
        └── current source-synchronized bounded revision

Exact hashes, scope, and redistribution status are recorded in
`SOURCE_CONTROL_HASHES.csv`. Source scans, German source bodies, and inherited
English comparison bodies are not included in this package.

The dedicated original scan has 38 physical pages. Its first 37 pages contain
Paper 4, printed pages 118–154; physical page 38 begins the next article and is
excluded. The bounded current unit is R823 lines 3559–3589. Section 1 begins at
line 3591, while the full Paper 4 ends at line 4500.

This dependency record does not constitute external scholarly review,
community certification, a critical edition, or a rights determination.

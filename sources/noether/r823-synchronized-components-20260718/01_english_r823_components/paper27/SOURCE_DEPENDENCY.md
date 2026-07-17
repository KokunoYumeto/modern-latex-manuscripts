# Source dependency: Noether Paper 27

Date: 2026-07-17

## Authority and routing order

1. The original JDMV/GDZ page governs the printed wording, opening dash,
   author styling, ideal-letter glyph family, formula direction, and notice
   boundary.
2. The R639 source audit routes the correct duplicate-label canvas and checks
   the complete one-page notice. It is an audit descendant of the original
   page, not an independent German witness.
3. The current R823 German block is the source-control transcription. Its
   normalized Paper 27 span is byte-identical to the R639-audited span.
4. The RA10 cumulative English and editable standalone are inherited
   translation candidates. They supply prose continuity but cannot override
   the German source or establish independent English use.
5. F. S. Macaulay's original English article title is an independent
   historical mathematical-English witness for `Hilbert Numbers`. It does not
   witness Noether's German wording, apparatus, or boundary.
6. Synchronized English Papers 24, 25, and 30 are same-project register
   controls for `residue-class field` only.

## Typed evidence nodes and edges

| Node | Type | Channel | Permitted role |
|---|---|---|---|
| `source:p27-gdz-p101` | primary printed source | source-content | Wording, dash, glyphs, formula direction, boundary |
| `audit:p27-r639` | dependent source audit | source-content | Correct canvas routing and complete-page line check |
| `source:p27-r823` | source-control transcription | source-content | Current German normalization |
| `candidate:p27-ra10-en` | inherited translation | target-text | Candidate discovery and continuity |
| `witness:macaulay-1913-hilbert-numbers` | native independent English source | target-register | Historical English form `Hilbert Numbers` |
| `control:p24-p25-p30-en` | same-project translations | target-register | Internal `residue-class field` consistency only |
| `adverse:p27-fraktur-qp` | rejected inherited notation | adverse-source | Prevents over-frakturization |
| `adverse:p27-hilbert-function-collapse` | rejected English form | adverse-target | Keeps distinct counts distinct from Hilbert's function |
| `qa:p27-compile-render` | deterministic validation | output-QA | Build and visual validation only |

Typed edges are: the GDZ page `audited_by` R639 and `transcribed_as` R823;
R639 `confirms_current_span` R823; RA10 `supplies_prior_candidate`; Macaulay's
article `supports_target_form`; the project siblings
`route_same_project_consistency`; the source page `rejects_frakturization`;
the source distinction between functions and further counts
`rejects_concept_collapse`; and the promoted English artifact is
`validated_by` compile/render QA. No scalar score selects the form.

## Declared dependence tree

```text
Noether Paper 27 evidence families
├── original JDMV/GDZ page (independent German root witness; 600 ppi)
│   ├── R300 opening-dash audit (dependent audit record)
│   ├── R639 complete-page audit and labelled crop (dependent derivatives)
│   └── R823 German transcription and package extract (dependent descendants)
├── English target-domain sources
│   └── Macaulay 1913 article (independent historical English root witness)
└── project translation family
    ├── RA10 cumulative English (inherited candidate)
    │   └── editable Paper 27 standalone (dependent extraction)
    └── synchronized Papers 24, 25, and 30 (same-project register siblings)
```

The labelled crop does not add source breadth. The RA10 cumulative and
standalone do not count as two English translations. The Macaulay title
supports the target term only; it is independent of the Noether page for that
limited purpose.

## Exact witnesses and hashes

Current R823 cumulative German authority:

`C:\Users\Floris\Documents\interlanguage\03_projects\noether\03_translation_workspaces\romance_rebase_20260717\authority_r823\pkg_r823\Noether_R823_WebB_R822_P20p27_31_RunInDashRefine_20260717\1\01_cumulative\Noether_R823_cum_de.tex`

- full SHA-256:
  `EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21`;
- Paper 27 spans source lines 14192--14200; Paper 28 begins at line 14201;
- package extraction:
  `source/Noether_Paper27_German_R823_authority.tex`;
- extraction SHA-256:
  `4197C0DA2E8D27214813B1F29C081256F3B3A2C7E3D093A938783ED21B8617C3`.

Original printed page:

`C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Noether Multilingual\Noether_R639_LocalCodex_P27P28_SourceAudit_NoPatch_20260703\1\02_source\P27_P28_GDZ_JDMV34_1925\P27_correct_source_p101_canvas000358_fullres_600ppi.jpg`

- SHA-256:
  `B00824115997D651F5EAB48420D05E6E0E6D7DF0AAC2CCD69E0836B033BFD8EC`;
- native dimensions and metadata: 3120 x 4733 at 600 ppi;
- status: best staged full-resolution source, not downsampled, but below the
  project's 650 ppi preference;
- duplicate-label trap: use canvas `00000358`; reject non-Noether canvas
  `00000110`.

R639 source audit:

`C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Noether Multilingual\Noether_R639_LocalCodex_P27P28_SourceAudit_NoPatch_20260703`

- README SHA-256:
  `E78235F331556F0080357BC47E56068D0CC5CAF2A1454BFFB9EBD784080147B8`;
- source-quality ledger SHA-256:
  `68256E8FBF5BF0E05396ADAB5BFE9997C90512F1DD669E5C56DEDEEBC0187481`;
- routing ledger SHA-256:
  `F83D2C20275A95FC6D4EFE7FB956B043F77D6D109CFC4CC100B083660E27C7A2`;
- line-check ledger SHA-256:
  `C97FA6B41E30C0B186B663A992752645803E75D96DEDB98F16B231207E40EB02`;
- no-patch-traps ledger SHA-256:
  `7902D8730DEC02ED714D58A7E28F0B29F8859DD055BDAA7813D2BB32AE8B9210`;
- result: `checked_no_patch`, including plain italic `q,p`, the full quotient
  chain, the composition-series direction, and the complete notice boundary.

R300 opening-dash audit:

`C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Noether Multilingual\Noether_R300_LocalCodex_R299_P27Dash_SourceRegressionFix_20260630`

- exact dash diff SHA-256:
  `72B7E4D8260E4F7A3A7BC10CCA70A1513D530558FB556F54015E6B2E989B8542`;
- confirmed-fixes ledger SHA-256:
  `02779BCAF0117F653920F31BCD8BC18FA3B416C96A66DCDB5A15EADC5672A511`.

Prior English controls:

- full RA10 cumulative SHA-256:
  `2BDB5EAB5DB6D7A46CF10EC8C99F720320A956EF866B473DAE4C28F8F49BF6C9`;
- package RA10 extract SHA-256:
  `4F1586D1F71AD24B7C31754EB9EE7F695633069FE014FB7BF923D331DB1F0B36`;
- editable standalone SHA-256:
  `D0D15E2380A45555275A65FBB8B12C4338F55815023450E9A5AEAC105389A889`.

Independent English target-domain witness:

- F. S. Macaulay, *On the Resolution of a given Modular System into Primary
  Systems including some Properties of Hilbert Numbers*, *Mathematische
  Annalen* 74 (1913), 66--121;
- DOI: `10.1007/BF01455345`;
- bibliographic record and GDZ full-article route:
  `https://eudml.org/doc/158622`;
- permitted use: historical English term support for `Hilbert numbers` only.

The complete source page, current R823 block, inherited English control,
extracted final PDF text, and complete final render were inspected. This is an
internal source-fidelity result; external review and human-comprehension
testing remain pending.

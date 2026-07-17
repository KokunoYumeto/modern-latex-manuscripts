# Source dependency: Noether Paper 18

Date: 2026-07-17

## Authority and routing order

1. The original JDMV/GDZ page governs the printed session and talk headings,
   prose, emphasis, formula glyphs and indices, inline primary decomposition,
   and contribution boundary.
2. The R366 package routes the correct printed-page canvas and records the
   full-page visual audit, source-quality limit, current-span identity, and
   no-patch regression traps. It is an audit descendant of the original page,
   not an independent German witness.
3. The current R823 German block is the source-control transcription. Its
   Paper 18 span descends unchanged from the R366-audited source lineage.
4. The RA10 cumulative English and its package extraction are inherited
   translation candidates. They supply prose continuity but cannot override
   the German source or establish independent English use.
5. Synchronized project translations, especially Paper 22, are same-project
   register controls for `fundamental module`, `resultant form`, and related
   ideal-theory language only. They are not independent target witnesses.
6. Compile, text extraction, render inspection, and spreadsheet checks
   validate the promoted output only; they do not supply source or target
   wording.

## Typed evidence nodes and edges

| Node | Type | Channel | Permitted role |
|---|---|---|---|
| `source:p18-gdz-p101` | primary printed source | source-content | Wording, apparatus, formula, layout, boundary |
| `audit:p18-r366` | dependent source audit | source-content | Correct canvas routing, source-quality limit, full-page and regression checks |
| `source:p18-r823` | source-control transcription | source-content | Current German normalization |
| `candidate:p18-ra10-en` | inherited translation | target-text | Candidate discovery and continuity |
| `control:p18-p22-en` | same-project translation | target-register | Internal ideal-theory register consistency only |
| `adverse:p18-resultant-endpoint` | rejected inherited notation | adverse-source | Prevents `R^(m)(x_n)=0(M)` regression |
| `adverse:p18-redaction-calque` | rejected English form | adverse-target | Prevents false-friend `free redaction` |
| `qa:p18-compile-render` | deterministic validation | output-QA | Build, extraction, and visual validation only |

Typed edges are: the GDZ page `audited_by` R366 and `transcribed_as` R823;
R366 `confirms_current_span` R823; RA10 `supplies_prior_candidate`; Paper 22
`routes_same_project_consistency`; the source page
`rejects_resultant_endpoint_regression`; editorial target review
`rejects_false_friend`; and the promoted English artifact is `validated_by`
compile/render QA. No scalar score selects a translation.

## Declared dependence tree

```text
Noether Paper 18 evidence families
├── original JDMV/GDZ page (independent German root witness; 600 ppi)
│   ├── RA51 congruence correction (dependent source audit)
│   ├── R347/R366 full-page audit and regression ledgers (dependent audits)
│   └── R823 German transcription and package extraction (dependent descendants)
└── project translation family
    ├── RA10 cumulative English (inherited candidate)
    │   └── package Paper 18 extraction (dependent extraction)
    └── synchronized Paper 22 English (same-project register sibling)
```

The PDF wrapper around the GDZ raster does not add source breadth. The R366
full-page audit, normalized extracts, and R823 block are dependent members of
one German-source family. The RA10 cumulative and package extraction are one
English candidate cohort, not two translations. No independent native-English
target-domain witness is asserted for this component; project-register forms
therefore remain controlled candidates pending external review.

## Exact witnesses and hashes

Current R823 cumulative German authority:

`C:\Users\Floris\Documents\interlanguage\03_projects\noether\03_translation_workspaces\romance_rebase_20260717\authority_r823\pkg_r823\Noether_R823_WebB_R822_P20p27_31_RunInDashRefine_20260717\1\01_cumulative\Noether_R823_cum_de.tex`

- full SHA-256:
  `EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21`;
- Paper 18 spans source lines 11191--11213;
- package extraction:
  `source/Noether_Paper18_German_R823_authority.tex`;
- extraction SHA-256:
  `0D2B1824A9B5EBEE5FF893C40B1DDC3F5D3F67B7DF66A01BF2E325AF6DA5F49F`.

Original printed page:

`C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Noether Multilingual\Noether_R366_LocalCodex_R347_P18_GDZ600_FullPageAuditSurvival_NoPatch_20260630\source_witness\P18_GDZ_JDMV30_p101_canvas00000301_600ppi_raw.jpg`

- SHA-256:
  `19713BEE033F0B1FBE3697E0C8BF7A12C653E35D9920BC9E73BB21429DAE3844`;
- native dimensions and metadata: 3224 x 5157 at 600 ppi;
- status: verified correct printed-page canvas `00000301` and best staged
  full-resolution source, but below the project's 650 ppi preference;
- the PDF wrapper has SHA-256
  `468277D529BEE28DF5C65A4CCE53BADD985D6A081E1C28DAC46E099D34C3CC43`
  and is a derivative wrapper, not another witness.

R366 source audit:

`C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Noether Multilingual\Noether_R366_LocalCodex_R347_P18_GDZ600_FullPageAuditSurvival_NoPatch_20260630`

- README SHA-256:
  `A02C6180F0FDB766CE6E35D4E82C47C9C4CE22DAECBE82DA0658CACB2A284EC4`;
- no-patch/regression-trap ledger SHA-256:
  `936A08336A58479326FDBE62659A065044D893DB4C48E1F22187D045DAFACE7C`;
- current-span check SHA-256:
  `8C10213DB2F41DBDF38E7B04C7A76F5F9AEA2AEB959CED9F38926DE6B2524321`;
- source-quality ledger SHA-256:
  `4F8386FF6B690395DA77E8454B785B412086CB0BBF8C916E91AE7582A088E776`;
- RA51 applied-fixes ledger SHA-256:
  `C82D10771C2A7942CB513DD814A8E6C4DB75F3ABA812A1EEC04040C7E6080D16`;
- result: the audited normalized source span is unchanged in the later
  promoted lineage, and the endpoint must remain
  `R^(n)(x_n) congruent to 0(M)`.

Prior English control:

- full RA10 cumulative SHA-256:
  `2BDB5EAB5DB6D7A46CF10EC8C99F720320A956EF866B473DAE4C28F8F49BF6C9`;
- package RA10 extraction SHA-256:
  `6FD57CC7CD338DC4D74ACC5786C77A70D94ED9477A35DC3636814CB2B39DAEAD`;
- inherited formula errors `R^(m)(x_n)` and `=0(M)` are rejected by the
  original page and the dependent source audits.

The complete source page, current R823 block, inherited English control,
extracted final PDF text, and complete final render were inspected. This is an
internal source-fidelity result; external review and human-comprehension
testing remain pending.

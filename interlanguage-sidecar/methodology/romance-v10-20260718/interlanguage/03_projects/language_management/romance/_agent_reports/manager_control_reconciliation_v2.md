# Romance manager-control reconciliation to cohort topology v2

Date: 2026-07-17  
Scope: manager control plane only. No file under 03_redo_ultra_20260717 was touched.

## Outcome

The manager declaration now names ROMANCE_FAMILY_COHORT_TREE_v2.json as the canonical topology for manager romance_manager. It declares all nine exact reader-cohort IDs, keeps Rumantsch Grischun and regional-idiom readers separate, states that there are zero human observations, and retains ROMANCE_FAMILY_COHORT_TREE_v1.json as superseded historical control evidence rather than deleting it.

A reproducible validator, validate_manager_control_v2.py, now generates both the validation JSON and the SHA-256 manifest. Its final run passed:

- 19/19 semantic checks;
- 6/6 structural checks;
- declared cohort count 9 and actual reader-cohort count 9;
- exact cohort-ID set and unique root-leaf set;
- root manager linkage romance_manager;
- exact C-RM-RG / C-RM-ID split;
- v2 supersedes v1 while v1 remains present and parseable;
- current human observations 0;
- 29 location-register rows with 0 missing paths;
- 105 inventory rows with the existing 15/15/55/20 class counts;
- automatic scalar decision false; and
- community-certification claim false.

The SHA manifest now covers nine artifacts: every artifact in the earlier control-manifest design, the preserved v1 tree, the canonical v2 tree, and the new validator. The manifest intentionally excludes ROMANCE_MANAGER_CONTROL_SHA256SUMS.csv itself because a stable self-hash is impossible. Its own resulting hash is recorded below for handoff.

## Resulting control hashes

| Artifact | SHA-256 | Bytes | Note |
|---|---|---:|---|
| ROMANCE_MANAGER_README_20260717.md | BAF606026528D967724BD504A94A8A4A247765A07115CB22DA089B7C3FCC50B9 | 3562 | updated v2/9-cohort declaration |
| ROMANCE_FAMILY_COHORT_TREE_v1.json | 1D54C111FB98D11932802A151E56F4F0E907A6289F3245C280828C8E73EBD756 | 1336 | preserved unchanged, superseded |
| ROMANCE_FAMILY_COHORT_TREE_v2.json | 9EBDEF5BE13B9BDBB0F1F2B718C2EE6583CF59F723C200E78668FC9CD9AD332C | 3309 | canonical topology, unchanged |
| validate_manager_control_v2.py | 67E274EF182DA9F6C8C506F4EC602C6B81F85853EE17BDD0EFC8AF26D4FDE51A | 8744 | reproducible validator/generator |
| ROMANCE_MANAGER_CONTROL_VALIDATION_20260717.json | 69536BDCE53F6A33654A69CBD09BCD23DC456C76D671433739279378EB14498F | 3030 | schema 2.0, pass true |
| ROMANCE_MANAGER_CONTROL_SHA256SUMS.csv | C9A24CB76FD501E80662D7101CFDBF525484BA46D487F01AB0737DC2A74EDCD8 | 994 | nine verified rows; self excluded |

## Independent verification

After generation, all nine manifest rows were independently recomputed from disk. Hash mismatches: 0. Byte-count mismatches: 0. The validation artifact was reparsed and all 25 recorded checks were true.

Continuation for the root gate: consume ROMANCE_MANAGER_CONTROL_VALIDATION_20260717.json only if pass remains true and the manifest recomputes cleanly; use v2 cohort IDs for current 106×9 access rows, while retaining v1 solely as superseded provenance.

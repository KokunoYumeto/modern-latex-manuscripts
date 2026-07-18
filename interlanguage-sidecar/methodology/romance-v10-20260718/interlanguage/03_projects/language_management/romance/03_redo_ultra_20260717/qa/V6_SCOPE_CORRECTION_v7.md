# V6 scope correction carried into v7

`ROMANCE_ACCEPTANCE_GATE_v6.json` and its independent bounded audit are preserved as historical evidence for the files they actually checked. They are not the current lane-wide gate and are not a four-stage completion certificate.

The omitted dependency was the manager control plane: v6 hashed `ROMANCE_FAMILY_COHORT_TREE_v2.json` directly, but did not hash or semantically validate the manager README, manager validation JSON, or manager SHA manifest. At that snapshot, the manager README and manager manifest still named/bound the superseded eight-cohort v1 tree. Consequently, v6 could pass its bounded 86-file checks while the wider lane exposed conflicting cohort topologies.

The manager plane has since been reconciled by `00_lane_control/validate_manager_control_v2.py`: v2 is canonical, its nine cohort IDs and root leaves are checked exactly, v1 is retained only as superseded evidence, human observations remain zero, and all manager-manifest rows are recomputed. The v7 successor gate hashes and independently checks the manager README, validator, validation JSON, SHA manifest, v1 tree, and v2 tree.

V7 also supersedes v6 operationally because the T002 validator and validation JSON changed after the v6 hash snapshot. V7 binds the repaired live T002 controls and independently compares every embedded control/output hash against the current file. V6 must therefore be described only as a preserved bounded snapshot.

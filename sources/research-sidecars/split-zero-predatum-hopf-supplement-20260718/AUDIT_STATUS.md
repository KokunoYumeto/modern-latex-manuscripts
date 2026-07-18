# Audit Status

- Scope: bounded N16-N18 predatum/K4/Hopf working-note sequence.
- Local rerun date: 2026-07-18.
- `verify_k4_sphere_note16.py`: 12/12 exact checks passed.
- `verify_cowlick_ladder_note16b.py`: 17/17 exact checks passed.
- `verify_n16b_errata.py`: 10/10 exact checks passed.
- `verify_hopf_predatum_note18.py`: 12/12 exact checks passed when Python was
  run in UTF-8 mode. A default Windows code-page run can fail while printing
  the parallel symbol; that is an output-encoding failure, not a failed check.
- Two invalid-escape `SyntaxWarning` messages remain in the N18 script. They
  do not change its executed expressions or pass count.
- The N18 script does not machine-check the Kripke-Joyal, torsor
  classification, paracompactness, or recorded numerical Gauss-linking steps.
- The cumulative TeX ledger is included as received and was not promoted as a
  newly typeset paper.
- Public classification: working notes and executable checks, provisional and
  not independently certified.


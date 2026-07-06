# F10 East-Slavic Skew Audit — v1 (mechanical triage)
2026-07-04. Data: [F10_EAST_SLAVIC_SKEW_AUDIT_20260704.json](F10_EAST_SLAVIC_SKEW_AUDIT_20260704.json) (1254 rows), companion ledger [INTERSLAVIC_LEDGER_RETROFIT_20260704.json](INTERSLAVIC_LEDGER_RETROFIT_20260704.json) + [.csv](INTERSLAVIC_LEDGER_RETROFIT_20260704.csv). Inputs hash-pinned in the run manifest. Flags are review triage, not verdicts; no wording was changed.

## Headline numbers (1254 term-level rows, deduped from 1310 glossary records + 222 logbook decisions)

| Flag | Meaning | Count | Share |
| --- | --- | ---: | ---: |
| F10-0 | clean — W/S-shelf, Interslavic-authority, or international rationale present | 210 | 16.7% |
| F10-1 | missing witness — no non-East evidence recorded (choice may still be fine) | 963 | 76.8% |
| F10-2 | East-heavy — broad-Slavic claim on East-only evidence | 20 | 1.6% |
| F10-3 | dominance-risk — `kolco`-family rows; review before external contact | 42 | 3.3% |
| F10-4 | authority-needed — coinages/specialist terms (reducent, transvekcija, …) | 19 | 1.5% |

safe_to_show_external: yes 210 · yes_with_definition 16 · review 966 · no_fix_first 62.

## Reading

1. **The lane is not "wrong" — it is under-witnessed.** Three quarters of terms carry no recorded non-East evidence either way. The 20-source W/S shelf (2026-06-24) exists precisely to close this; the backfill was never run. This is the pre-van-Steenbergen work list, now enumerated row-by-row.
2. **The dominance question is concentrated and inherited.** All 42 F10-3 rows are the ring-term family: `kolco` and its compounds. One decision (kolco vs okruh/prsten/kolobar) resolves or re-justifies all 42 rows at once. This is the cheapest high-impact review item in the lane.
3. **F10-2 (broad claim, East evidence) is small (20)** — the lane rarely overclaimed; it mostly under-recorded. Good news for the review packet.
4. **Archaeology preserved:** this audit + the frozen pre-retrofit spine ([frozen/](frozen/)) lock the "AI with East-Slavic sources only" state as a historical stratum. After backfill, the diff (how many choices shift when W/S witnesses are added) is a measured result for the paper (CLM-DOM-001).

## Limits
- Mechanical keyword/field triage; a rationale phrased unusually can be misfiled. The F10-0 set errs conservative (requires positive evidence), so 210 is a floor, not a ceiling.
- Substring matching for flagship/dominance terms means inflected/compound forms are caught, but an unrelated term containing a flagged fragment would be a false positive — spot-check during backfill.
- No human or community judgment is encoded here; F10-* flags queue review, they do not assess Interslavic quality.

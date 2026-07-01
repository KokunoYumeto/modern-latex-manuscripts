# SGA5 Full-Audit Workpass p343 Live Ledger Update

Local folder:
`C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\SGA continuation 2\_claude_aid\sga5_full_audit_20260623`

This registers the current local SGA5 hand-audit/workpass ledger as of the
p343 checkpoint.

- Completed `CERT_LOG.md` rows: `343`
- Maximum completed page row: `p343`
- Next live cursor: `p344`
- Workpass PDF pages: `307`

Measured files:

| File | Bytes | SHA256 |
|---|---:|---|
| `CERT_LOG.md` | 675,411 | `D79956EDF0F1A9A9B3A7386D8CC62ACD948728DDF7C0B97770E8FC39E22E42AD` |
| `AGENT_SCORECARD.md` | 578,547 | `5373B480846C25F0A5B0B5C25DB28CF01005725DCA829760C98D6599CA8A8294` |
| `sga5_fr_workpass.pdf` | 2,017,343 | `176B2E8F1B15E518548E3C98FAEFBD6276CEA489A762EA53471E3C68147F53F3` |
| `sga5_fr_workpass.tex` | 844,611 | `CA51824BC9D212811015C7549F6E4C98EB7CE554CA4CF12BD5C37C6C01AE39EE` |

Recent p340-p343 scope:

- p340: Expose VII section 9, end of Lemma 9.3 proof and beginning of key Lemma 9.4; the ledger flags a source-visible checked-E/plain-E inconsistency and keeps the TeX source-faithful rather than silently normalizing it.
- p341: Lemma 9.4 proof continues through equations (9.4.2)-(9.4.9), including the reduction toward `b_0=0`; no TeX fix promoted.
- p342: Lemma 9.4 is proved and section 9.5 proves Theorem 9.2, the Mumford self-intersection formula in the Chow ring; no diagram and no TeX fix promoted.
- p343: Proposition 9.6, the key Chow analogue of Lemma 8.4.3, is stated; diagram D161, the cartesian square `Y' / X' / Y / X`, is checked edge-by-edge; Lemma 9.7 is stated. p344 is next.

Quality caveat: this is active local ledger/provenance evidence only. It is not
a promoted compact delta, not a new SGA5 public release, not SGA5 completion,
not English synchronization, not global source-faithfulness certification, and
not critical-edition material. The latest compact promoted SGA5 delta remains
p260-p265; p266+ are live local workpass/cursor evidence unless a later compact
package is built. Staged images or cursor material for later pages, including
p455-p484 source witnesses, are not audit claims from this checkpoint.

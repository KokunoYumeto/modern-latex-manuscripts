# Noether R521 - Paper 24 p257 R-prime Source Fix and Tail Audit

Local ZIP:
`C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Noether Multilingual\Noether_R521_LocalCodex_R520_P24p257_Rprime_SourceFix_TailAudit_20260702.zip`

ZIP metrics:

| Field | Value |
|---|---:|
| Bytes | 91,480,992 |
| Entries | 74 |
| SHA256 | `2CE208056C938129CEB85FCA07B2C8CB7677F180DF61689B81B00DE8EE37B009` |

R521 is a clean packaged TeX-changing source-control candidate on top of R520.
The ZIP includes current cumulative TeX/PDF, previous R518/R519/R520 audit
materials, source witnesses, diff, render checks, visual dispositions, and
XeLaTeX logs.

Repair promoted from `confirmed_fixes_R521.csv`:

| Paper | Printed page | Current PDF page | Previous reading | New reading | Rationale |
|---|---:|---:|---|---|---|
| P24 | 257 | 262 | `der Körper (\mathcal R)=...` | `der Körper (\mathcal R')=...` | The source distinguishes the rest-class field `\mathcal R` from the isomorphic subfield `\mathcal R'`; the active TeX collapsed them. |

No-patch visual audit:

- P24 printed pp251-256 and pp258-261 were checked with no TeX patch promoted.
- The dispositions are recorded in `audit/visual_dispositions_R521.csv`.

Build and scope:

- Base: R520 local cumulative.
- Cumulative PDF pages: 471.
- Changed output page: 262.
- Repairs: 1.
- Checked page span: P24 printed pp251-261.
- Compile: XeLaTeX passed twice.

Second-web intake refresh:

- Fronted ZIP: `39_R521_P24P257_RPRIME_SOURCEFIX_TAILAUDIT.zip`.
- Top-level files: 40.
- ZIP payloads: 35.
- ZIP bytes: 4,303,613,881.
- Total top-level bytes: 4,303,636,192.

Source-quality caveat: P24 pp251-261 authority is IA raw JP2 at about 400 dpi;
renders/crops are enlarged for readability only. Treat R521 as one inspected
source-control repair plus no-patch visual audit support only. It is not a
reader release, not Paper 24 certification, not Noether closure, not
whole-corpus certification, not multilingual synchronization, and not
critical-edition material.

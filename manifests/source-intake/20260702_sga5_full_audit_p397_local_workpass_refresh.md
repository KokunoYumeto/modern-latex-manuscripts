# SGA5 full-audit local workpass refresh through p397 (2026-07-02)

Source lane: `C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\SGA continuation 2\_claude_aid\sga5_full_audit_20260623`.

This manifest records a live local SGA5 French workpass/audit cursor. It supersedes the p391 refresh for current-public wording, but it is still live ledger/provenance only. The latest compact promoted SGA5 delta remains `SGA5_FullAudit_WebDrop_p260_p265_workpass_delta_20260626`; p266-p397 are not a compact promoted delta unless later packaged deliberately.

Important ledger caveat: `CERT_LOG.md` currently has an older p125 row physically appended after p397. The public cursor is therefore the highest forward SGA5 audit row, p397, not the final physical line in the file.

Evidence at this checkpoint:

- `CERT_LOG.md`: 835,616 bytes, last modified 2026-07-02T08:19:55, SHA256 `B544A586F4A0AA941576CA64A27800F6634512A1C8DA46EAF2E244C46ED7D90C`.
- `AGENT_SCORECARD.md`: 711,934 bytes, last modified 2026-07-02T08:24:03, SHA256 `2C265884517CB517686B6818B8C97403CAF7B22922735F7E7B38DE59B48314C6`.
- `sga5_fr_workpass.tex`: 845,081 bytes, last modified 2026-07-02T08:16:50, SHA256 `9E58CD97CB8C511DC12F2943B9E8125BA2AA824B933A6C8AD2774763AB5CCCB6`.
- `sga5_fr_workpass.pdf`: 2,017,718 bytes, last modified 2026-07-02T08:17:22, SHA256 `0F24B8F20255B80B30677251E366845012447107FC881B661A4D4FE2B4C7F8C2`.
- `sga5_fr_workpass.log`: 360,411 bytes, last modified 2026-07-02T08:17:22, SHA256 `06EBC74324A1760F494B4D89111822AC68A3E20C4C216F5670627B8460D6C91E`.

Build evidence:

- `sga5_fr_workpass.log` reports: `Output written on sga5_fr_workpass.pdf (307 pages, 2017718 bytes).`
- No fatal LaTeX error, undefined control sequence, or LaTeX Error line was observed in the targeted compile-status scan.

Current ledger cursor:

- Highest forward SGA5 audit row: p397.
- p392 verifies the distinguished-triangle diagram D179 and fixes a dropped verbal phrase, an incomplete SGA 4 IX reference, and an `H^*` vs `H^1` source-faithfulness error.
- p393 completes the proof of Proposition 5.1 / the Weil formula via Hurwitz and opens §6 on local terms `\varepsilon_x^\Delta(F)`.
- p394-p395 identify and fix the systematic A-vs-Lambda transcription error in `Hom`/`Sw` terms, restoring `Hom` over `\Lambda[G]` and `Sw^\Lambda` where the source glyph and mathematics require it.
- p396 completes §6 examples and states Theorem 7.1, while flagging the source slip "conditions of 7.1" where the referent is §6.1.
- p397 verifies the Euler-Poincare formula (7.2), checks proof steps a/b and formulae (7.3)/(7.4), and fixes a dropped prime `C` to `C'` in the equivalence of categories.
- Fixes are recorded through #44; diagrams are tracked through D179.
- p398 is the next queued page, with explicit watch for `RHom` and A-vs-Lambda checks in formula (7.7) and nearby `D(A[G])` / `\RHom_{A[G]}` lines.

Public-facing caveat:

Treat this as live local French workpass/source-audit provenance only. It is not a promoted reader package, not SGA5 completion, not English synchronization, not global source-faithfulness certification, and not critical-edition material. Local words such as clean/certified/complete/strict/source-checked are page-local workpass terms only.

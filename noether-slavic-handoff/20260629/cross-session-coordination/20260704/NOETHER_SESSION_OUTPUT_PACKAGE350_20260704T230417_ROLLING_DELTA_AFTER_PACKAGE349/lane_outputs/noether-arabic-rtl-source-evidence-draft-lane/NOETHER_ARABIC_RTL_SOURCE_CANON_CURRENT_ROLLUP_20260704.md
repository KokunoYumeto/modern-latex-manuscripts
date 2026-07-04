# Noether Arabic RTL Source-Canon Current Rollup

Created: 2026-07-04

Status: draft source-canon/provenance control layer only. This is non-canonical, not native reviewed, not approved, and not a license-clearance claim. It does not extend translations, approve terms, populate reviewer packets, promote gates, claim completion, or push Git changes.

## Current Instruction Boundary

The Arabic RTL lane is aligned to the repository-visible source-canon-first rule in `AGENTS.md` and `.github/copilot-instructions.md`: source witnesses and explicit gaps come before translation. Local lane work must keep URLs, hashes, license/access signals, language/topic tags, upload policy, and blockers visible. GitHub/package publication remains B3-owned.

## Easy-Find Current Artifacts

| Layer | Rows | SHA-256 | Path / status |
| --- | ---: | --- | --- |
| Arabic normalized witness table | 26 | `C70D17AFC7CA804738EDD376A86E432AD26B9336810142EB8AA62D6143505A4B` | `outputs/NOETHER_ARABIC_RTL_SOURCE_CANON_WITNESS_TABLE_NORMALIZED_20260704.csv` |
| Arabic GitHub/source-archive probe | 15 | `E7DBEE58048F5F2187D67B6DB51A5E956FE9654891013D5BEBAA8011971AFDDA` | `outputs/NOETHER_ARABIC_RTL_GITHUB_SOURCE_ARCHIVE_PROBE_20260704.csv` |
| Arabic R3 gap-refresh intake | 5 | `ACAE953C0A1F957493474D00FA0B500E92C4325E6EC75A384C2C82229D024F08` | `outputs/NOETHER_ARABIC_RTL_R3_GAP_REFRESH_INTAKE_20260704.csv`; based on the earlier R3 refresh and superseded for current R3 pointers by the rows below |
| R3 current gap-refresh required-shape table | 12 | `8239C25B3B440CE862F8E9C15950C51155D077DD5050E8003EBBAF9B712D1AA6` | `C:\Users\memo_\Documents\Codex\2026-07-04\noether-r3-arabic-persianate-linear-algebra\outputs\R3_SOURCE_CANON_GAP_REFRESH_20260704T202708Z\R3_SOURCE_CANON_GAP_REFRESH_REQUIRED_SHAPE_20260704T202708Z.csv` |
| R3 master source-canon index | 70 | `465FA3023D0B175E128D0CEC1713C32E3169E68D6B742CCDABAC4C95547295FC` | `R3_SOURCE_CANON_MASTER_INDEX_20260704T204214Z`; includes the R3 GitHub/source-archive probe |
| R3 GitHub/source-archive probe | 11 | `C1E9F2E256436D47EA94D929C83A1766C029C0BA01CB94E628E41ADBE6FC852C` | `R3_SOURCE_CANON_GITHUB_ARCHIVE_PROBE_20260704T203912Z`; Arabic rows are support/tooling or explicit gap, not mathematical source text |
| Arabic R3 policy/payload sync intake | 8 | pending rehash after edit | `outputs/NOETHER_ARABIC_RTL_R3_POLICY_PAYLOAD_SYNC_INTAKE_20260704.csv`; absorbs R3 policy-sync `20260704T205752Z` and external-pointer payload probe `20260704T205627Z` |

## Current Arabic Evidence State

- Direct Arabic TeX/LaTeX/arXiv/source-package witnesses found for Noether-style algebra or invariant theory: `0`.
- Arabic PDF/HTML/text fallback witnesses: present and hashed; they support provenance only.
- Arabic GitHub/source-archive hits from R3: `3` support/tooling/script-render rows, `0` Arabic mathematical source-text rows, and `1` explicit Arabic mathematical source-archive gap.
- Strongest Arabic algebra/ring source witnesses remain the local normalized table plus the R3 addenda below.
- Arabic invariant-theory source package remains open: weak phrase/metadata evidence exists, but no direct Arabic specialist TeX/source archive has been located.
- Persianate, Dari/Tajik, Urdu/Hindustani, and other Arabic-script neighbor materials do not authorize Arabic rows.

## R3 Current Arabic Addenda

| Witness | Type | URL | Hash | Current use |
| --- | --- | --- | --- | --- |
| Prüfer ring and Arithmetical ring / حلقة برفير والحلقة الحسابية | PDF publication fallback | `https://journal.damascusuniversity.edu.sy/index.php/basj/ar/article/view/3694/1220` | `8957E428CACBADA148C65E9894FCF73C0931BDA5722C8CC8A842F23150BE69C4` | Strengthens Arabic Noetherian/ring provenance; no invariant-theory source-package closure. |
| Cayley-Hamilton application and matrix algebraic structure Arabic article | PDF publication fallback | `https://journal.damascusuniversity.edu.sy/index.php/basj/ar/article/view/1133/844` | `01E37F125A62322451388F068E71BBF7E28F0448F1A112F62252E821E65EC6D4` | Adjacent Arabic matrix/ring witness; no bridge-term authorization. |
| Comparative study of Kronecker and Hadamard product effects on matrix algebraic structure | PDF publication fallback | `https://fezzanu.edu.ly/fusj/index.php/FUAJ/article/download/343/189/326` | `971692613BFD9312B364BD0740F8401BB6372635CF3BF092F7B3DCBE601D2A15` | Adjacent matrix/ring/Artinian/Noetherian provenance; not specialist invariant theory. |
| اللاتغيرية ونظرية النظم: الجوانب الجبرية والهندسية | Weak HTML metadata/summary | `https://shamra-academia.com/show/f0597758b3ef43` | `1C96766B86AD1336829B8A387B1E1E2626298E59B7A6B3AA8F2C17C45ABB0C2F` | Phrase evidence only; not an Arabic specialist publication/source package. |
| Arabic invariant-theory TeX/arXiv/source archive | Explicit gap | no source located | no hash | Keep open; Arabic PDF and weak phrase evidence do not close it. |

## Source-Archive Probe Result

The Arabic GitHub/source-archive probe records 15 rows. It found zero usable Arabic TeX/LaTeX/source-package rows for the treated algebra/invariant-theory topics. It records zero-hit queries, false-positive clusters, and one access/rate-limit-style search blocker. This remains evidence for an open acquisition task, not evidence of source closure.

## R3 GitHub / Source-Archive Intake

R3's newer GitHub/source-archive probe records three Arabic support rows and one Arabic explicit gap. `OmarIthawi/arabic-mathjax`, `Mohamed1984/ArabicMath`, and `latex3/babel` `lua-arabic.tex` are useful RTL/math-rendering or equation-tooling source evidence, but they are not Arabic algebra/invariant-theory mathematical source witnesses. R3 also carries Persian/Farsi SireJeff linear-algebra TeX/source rows; those remain Persianate-only and do not authorize Arabic.

## R3 Policy / Payload Sync Intake

R3 policy-sync `20260704T205752Z` adds normalized upload-policy and access/license classes for 70 current R3 master rows. Arabic receives 26 consumer rows: 17 `manifest_hash_url_only_no_payload_until_B3_license_review`, 5 `conditional_payload_requires_B3_attribution_and_license_review`, 1 `manifest_only_source_archive_until_B3_license_review`, and 3 `gap_only_no_payload` rows. The split-lane sync sees this Arabic rollup present at pre-intake hash `CB3A0B369F87CA577E9FFA166D7C311DB77E11796C0601B296A526E86F5083B0` with no stale R3 master pointer detected.

R3 external-pointer payload probe `20260704T205627Z` fetched 13 Arabic external-pointer payloads: 9 matched expected hashes, 4 are live-drift/hash mismatch candidates, and 0 failed to fetch. The mismatch rows are `INV-009`, `INV-010`, `REP-011`, and rejected false-positive `REJECT-013`; these remain blocker rows and do not replace owner-lane hashes without B3 or owner-lane review.

## Package Boundary

During this pass the B3 package frontier moved quickly. The Arabic lane observed packages advancing through package 345 and later package 346 drift while this source-canon work was being refreshed; a later recheck observed package 349 locally in the checkout and the branch ahead of origin by one package commit. These are point-in-time package observations, not a lane publication action. This Arabic lane did not stage, commit, push, clean, or alter package directories.

## RTL / TeX / PDF Notes

No new translation or TeX reader was created in this pass. Future Arabic rendering still needs an Arabic-capable XeLaTeX/LuaLaTeX stack, explicit bidi controls around inline formula neighbors, and visual QA for Arabic punctuation next to math. Source-canon rows here are manifest/hash/URL records only; raw PDFs or HTML bodies are not copied into this lane output.

## Open Arabic Gaps

- Direct Arabic TeX/LaTeX/arXiv/source packages for algebra/invariant-theory topics.
- Direct Arabic GitHub mathematical source archive for invariant theory / Noetherian-ring topics.
- Direct specialist Arabic invariant-theory source witness.
- Arabic covariant/binary-forms source witness.
- Direct Arabic source authority for Artinian/minimal-condition terms beyond adjacent ring PDFs.
- Direct Arabic ring homomorphism/isomorphism contexts beyond adjacent algebra/ring witnesses.
- License/reuse closure for all Arabic witness bodies.

These are blocker/acquisition rows, not reasons to invent terminology or resume translation churn.

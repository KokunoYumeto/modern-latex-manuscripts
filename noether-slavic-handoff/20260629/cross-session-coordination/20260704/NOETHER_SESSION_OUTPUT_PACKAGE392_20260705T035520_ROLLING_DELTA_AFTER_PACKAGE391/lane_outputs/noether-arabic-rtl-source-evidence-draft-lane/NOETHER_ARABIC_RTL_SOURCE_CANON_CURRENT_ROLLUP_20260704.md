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
| Arabic R3 policy/payload sync intake | 8 | `C4B6DBCA804C1DA115F1AAB566D47F3D61FE5126976682D587E5B2596C9D52CC` | `outputs/NOETHER_ARABIC_RTL_R3_POLICY_PAYLOAD_SYNC_INTAKE_20260704.csv`; absorbs R3 policy-sync `20260704T205752Z` and external-pointer payload probe `20260704T205627Z` |
| Arabic R3 current pointer refresh | 5 | `87757752B09DBB2468A2153ACB17D6A29F728BC80173367E73FBAE8B474498EF` | `outputs/NOETHER_ARABIC_RTL_R3_CURRENT_POINTER_REFRESH_20260704.csv`; absorbs R3 policy-sync `20260704T210315Z`, payload probe `20260704T210216Z`, and source-body omit manifest `20260704T210917Z` |
| Arabic R3 cross-lane sync intake | 6 | `C72D72F99DFB6FC0E82909677A08BCF1A6FD40530AD3A500EF973F2D6DB6FD0A` | `outputs/NOETHER_ARABIC_RTL_R3_CROSS_LANE_SYNC_INTAKE_20260704.csv`; absorbs R3 cross-lane sync `20260704T212016Z` |
| Arabic source-canon heartbeat probe | 8 | `5EF9D10A6D46848EEB219CA7BA9F4F4B9FF075922BE8E7DA7C10BE1056FA52B5` | `outputs/NOETHER_ARABIC_RTL_SOURCE_CANON_HEARTBEAT_PROBE_20260705.csv`; adds OMU `الجبر الحديث` PDF fallback witness and refreshes source-package gaps |
| Arabic MediaWiki raw source-text probe | 10 | `DB80BD30AC4B38EE6ADFEDE2B2C54929FBB41B8D9A6DCE96FB6B4AFB91737943` | `outputs/NOETHER_ARABIC_RTL_MEDIAWIKI_SOURCE_TEXT_PROBE_20260705.csv`; adds revision-pinned raw Arabic wikitext fallback witnesses for ring/group/field/module/abstract algebra/group theory |
| Arabic Wikibooks raw source-text probe | 10 | `59CD07B8C51732A7DD2548D92297F25D2BA49A167AA2C4538AB8ADD722E370A5` | `outputs/NOETHER_ARABIC_RTL_WIKIBOOKS_SOURCE_TEXT_PROBE_20260705.csv`; adds revision-pinned Arabic Wikibooks raw text for algebra/abstract algebra/rings/linear algebra/vector spaces |
| Arabic official PDF source probe | 8 | `7D0FC1F76DD78E485F56BFE1AF4B114A4F7CE8ABC9CA006DD1D4ADF8EF7925D7` | `outputs/NOETHER_ARABIC_RTL_OFFICIAL_PDF_SOURCE_PROBE_20260705.csv`; adds official university-hosted ring/group PDF fallback witnesses |

## Current Arabic Evidence State

- Direct Arabic TeX/LaTeX/arXiv/source-package witnesses found for Noether-style algebra or invariant theory: `0`.
- Arabic PDF/HTML/text fallback witnesses: present and hashed; they support provenance only.
- 2026-07-05 heartbeat addendum: one new Arabic PDF fallback witness from Omar Al-Mukhtar University Press (`الجبر الحديث`, hash `E60FD267AED80573F506683C47E9E2F6ED9C36DDE8809446C137DD5D1FC7188E`), plus one existing Milne group-theory PDF revalidation.
- Arabic GitHub/source-archive hits from R3: `3` support/tooling/script-render rows, `0` Arabic mathematical source-text rows, and `1` explicit Arabic mathematical source-archive gap.
- Strongest Arabic algebra/ring source witnesses remain the local normalized table plus the R3 addenda below.
- Arabic invariant-theory source package remains open: weak phrase/metadata evidence exists, but no direct Arabic specialist TeX/source archive has been located.
- Persianate, Dari/Tajik, Urdu/Hindustani, and other Arabic-script neighbor materials do not authorize Arabic rows.

## 20260705 Heartbeat Source-Canon Addendum

The 2026-07-05 source-canon heartbeat probe adds `NOETHER_ARABIC_RTL_SOURCE_CANON_HEARTBEAT_PROBE_20260705.*`. It caches and hashes Omar Al-Mukhtar University Press `الجبر الحديث` as a new Arabic PDF fallback witness for broad modern-algebra provenance. The metadata page declares Arabic language metadata, ISBN `978-9959-79-074-3`, and a CC BY-NC-ND 4.0 signal; the downloaded PDF hash is `E60FD267AED80573F506683C47E9E2F6ED9C36DDE8809446C137DD5D1FC7188E`. A local first-80-page `pdftotext` extract is kept as a derived verification artifact only.

The same pass revalidates the existing Milne Arabic group-theory PDF hash as `77B97DF62856083FF960790EA6CEA27E5AD6927241D5F87751B376C8F644A904`, records eight exact Arabic GitHub `extension:tex` code-search zero hits, and records a ResearchGate multi-linear algebra PDF candidate as HTTP `403 Forbidden` with no payload/hash. This addendum strengthens Arabic PDF fallback provenance for algebra/rings/modules/groups/linear-algebra-adjacent topics, but it does not close direct Arabic TeX/LaTeX/arXiv/source-package gaps or specialist invariant-theory/Artinian/manual-review gaps.

## 20260705 MediaWiki Source-Text Addendum

The 2026-07-05 MediaWiki probe adds `NOETHER_ARABIC_RTL_MEDIAWIKI_SOURCE_TEXT_PROBE_20260705.*`. It pins Arabic Wikipedia raw wikitext by revision ID for `حلقة (رياضيات)`, `زمرة (رياضيات)`, `حقل (رياضيات)`, `حلقية (رياضيات)`, `جبر مجرد`, and `نظرية الزمر`, and revalidates `جبر خطي`. These are hashable Arabic source-text fallback witnesses with Wikimedia license signals, not TeX/source packages and not reader-layout artifacts.

The same pass records a cautioned `شباه` raw-text row as homomorphism-adjacent but not a direct ring-homomorphism/isomorphism authority. A refreshed GitHub TeX probe found no target Arabic mathematical source package: one query returned a false-positive i18n QA corpus and one query hit HTTP `403` code-search access limiting. The direct Arabic TeX/LaTeX/arXiv/e-print/source-package gap therefore remains open.

## 20260705 Wikibooks Source-Text Addendum

The 2026-07-05 Wikibooks probe adds `NOETHER_ARABIC_RTL_WIKIBOOKS_SOURCE_TEXT_PROBE_20260705.*`. It pins Arabic Wikibooks raw wikitext by revision ID for `جبر`, `جبر/جبر تجريدي`, `جبر/جبر تجريدي/حلقات`, `جبر/جبر خطي`, and `جبر/جبر خطي/فضاءات شعاعية`, and revalidates the already-used `جبر/جبر خطي/جملة المعادلات الخطية` and `جبر/جبر خطي/المصفوفات` raw-text hashes.

The same pass ran another bounded GitHub `extension:tex` probe across module, group, field, algebraic-structure, linear-map, vector-space, commutative-ring, and homomorphism phrases. No Arabic mathematical TeX/source-package witness was admitted, and the final query hit HTTP `403` code-search access limiting. Wikibooks adds source-text fallback provenance only; it does not close TeX/source-package or specialist invariant-theory/Artinian/ring-homomorphism gaps.

## 20260705 Official PDF Source Addendum

The 2026-07-05 official-PDF probe adds `NOETHER_ARABIC_RTL_OFFICIAL_PDF_SOURCE_PROBE_20260705.*`. It caches and hashes official university-hosted Arabic PDF/metadata witnesses: Damascus University `البنى الجبرية 2 - نظرية الحلقات` (`B24697BD24D75073246E781402C6316104372F445D1EEE6E54E675A08AF2C1F2`), Tal Afar University `محاضرات نظرية الزمر` (`C3A2DCC3FB6267E4A7E61D7AC7624616E49FC547C9A3F362BA8C529E413F65C6`), and King Saud University `نظرية الزمر` course specification (`BE0DC74FE8F16AD62C1C5505A4C7B8A5DFD03CD19DE931DCD8AF817C49DCC29C`).

All three bodies have valid `%PDF` signatures and local first-page text extracts for topic verification. These official PDFs strengthen fallback provenance for ring theory, group theory, and homomorphism/isomorphism-adjacent course context, but they are not TeX/source packages, not license clearance, and not approval of any Arabic term.

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

## R3 Current Pointer Refresh

R3 current pointers advanced again after the earlier policy/payload intake. The current policy-sync audit is `20260704T210315Z`, with 70 policy rows and the same Arabic routing counts: 26 Arabic consumer rows, 3 Arabic gap rows, and upload-policy counts of 17 manifest/hash/URL-only, 5 conditional attribution/license-review, 1 manifest-only source archive, and 3 gap-only rows.

The current Arabic external-pointer payload probe is `20260704T210216Z`, with 13 fetched payloads, 9 expected-hash matches, 4 live-drift/hash mismatch rows, and 0 fetch failures. The four mismatch rows remain `INV-009`, `INV-010`, `REP-011`, and rejected `REJECT-013`; the `INV-010` current probe hash is now `E8CFF35F018A69200B17D0E1BEE7B3FBAAFF543D40A66338423AE110EDFB9AD7`. Expected hashes must not be replaced without B3 or owner-lane review.

R3 also added source-body omit manifest `20260704T210917Z`. It indexes 57 raw source bodies/cache payloads for package omission, including 33 Arabic-targeted rows. Of those Arabic rows, 26 are under current pointer/cache roots and 7 are superseded/historical duplicates. Arabic payload kinds include PDFs, HTML snapshots, text/wikitext bodies, support zip archives, TeX bodies, and one non-Arabic arXiv tar source body that remains non-authorizing for Arabic wording.

## R3 Cross-Lane Sync Intake

R3 cross-lane sync `20260704T212016Z` records 16 cross-lane rows, 33 open gap/action rows, and 70 durable row-log append rows. Arabic-relevant rows include a whole-program instruction/provenance recheck, R3 current artifact pointers, Arabic owner-lane state rows, direct Arabic source-package gaps, and four Arabic external-pointer drift blockers.

The cross-lane sync marks the older Arabic policy/payload intake as needing current-pointer refresh because it cites older R3 policy/probe artifacts. The Arabic lane preserves that older intake as historical and uses `NOETHER_ARABIC_RTL_R3_CURRENT_POINTER_REFRESH_20260704.*` as the current response, covering policy `20260704T210315Z`, probe `20260704T210216Z`, and omit manifest `20260704T210917Z`.

The cross-lane sync also observes GitHub-visible source-canon shelves under `noether-slavic-source-canon/20260704`. Those shelves are useful evidence-shape comparison only; they are not Arabic target-language authority and must not be imported into Arabic gap closure.

## Package Boundary

During this pass the B3 package frontier moved quickly. The Arabic lane observed packages advancing through package 345 and later package 346 drift while this source-canon work was being refreshed; later rechecks observed package 349, then package 352 as the current visible package frontier. These are point-in-time package observations, not a lane publication action. This Arabic lane did not stage, commit, push, clean, or alter package directories.

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

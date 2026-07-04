# Noether Romance Unrepresented Local Source Candidate Audit

Status: source-canon/provenance candidate audit; draft / non-canonical / not native reviewed / not approved / not license-cleared / not gate-promoted.

Created: 2026-07-04.

## Scope

This audit checks local French and Spanish source-level shelves for source packages that are not represented in the current Romance witness table. It is a candidate index only. It does not add rows to the main witness table, approve terms, translate text, claim native review, claim canonical approval, claim license clearance, promote gates, or push Git.

Current main witness table remains:

- `outputs/NOETHER_ROMANCE_SOURCE_CANON_WITNESS_TABLE_20260704.csv`
- `outputs/NOETHER_ROMANCE_SOURCE_CANON_WITNESS_TABLE_REQUIRED_SHAPE_20260704.csv`

Candidate source-package sidecars:

| Artifact | Rows | SHA-256 | Purpose |
| --- | ---: | --- | --- |
| `NOETHER_ROMANCE_SOURCE_CANON_UNREPRESENTED_LOCAL_SOURCE_CANDIDATES_20260704.csv` | 40 | `CF71D94BBA4DBC3E149F28ED69631AC9E294E9AF89580FB6F5B447596281A925` | Broad local candidate audit; 39 French rows and 1 Spanish row; 22 rows have quick topic-term hits. |
| `NOETHER_ROMANCE_SOURCE_CANON_SPANISH_UNREPRESENTED_LOCAL_SOURCE_CANDIDATES_20260704.csv` | 10 | `C3B0E1C369D1F0768AD9C5AFD0BEA04EAB52D31C6762B5E0DCFF6B5B266C4E84` | Spanish-focused supplement so Spanish source packages are visible even when the quick term scan finds few high-signal hits. |

## Candidate Method

Local shelves scanned:

- `C:\Users\memo_\Documents\Codex\2026-06-09\could-you-look-online-for-me\work\noether-slavic-canonical\sources\non_slavic_reference_corpus\20260628_french_spanish_native_math_register\downloaded_source_packages_expanded`
- `C:\Users\memo_\Documents\Codex\2026-06-09\could-you-look-online-for-me\work\noether-slavic-canonical\sources\non_slavic_reference_corpus\20260628_french_spanish_native_math_register\downloaded_source_packages`
- `C:\Users\memo_\Documents\Codex\2026-06-09\could-you-look-online-for-me\work\noether-slavic-canonical\sources\non_slavic_reference_corpus\20260628_french_spanish_native_math_register\added_sources`
- Existing context snippets under `20260630T065920Z_french_spanish_invariant_hardterm_evidence\local_corpus_contexts`

Rows were excluded from the candidate list when their local path or SHA-256 already appeared in the current main Romance witness table. Remaining candidates record local path, byte count, SHA-256, quick topic-term hits, context/source hit path where found, license/access placeholder, and a non-claim boundary.

## High-Signal Broad Candidates

The broad audit found 22 candidate rows with quick source/context hits for terms such as `Noether`, `Hilbert`, `anneau`, `module`, `corps`, `invariant`, or the Spanish `anillo`.

Representative candidate IDs:

| Language | Candidate IDs with topic hits | Source-canon status |
| --- | --- | --- |
| French | `0910.2557v1`, `1104.1507v4`, `1104.3350v3`, `1205.6530v1`, `1305.1672v1`, `1405.2056v2`, `1407.3941v1`, `1509.07817v1`, `1510.05382v1`, `1605.01289v1`, `1709.00597v2`, `1801.01463v2`, `1905.13138v3`, `2001.10515v4`, `2112.07476v2`, `2501.13300v2`, `2504.20230v1`, `2505.05443v1`, `2506.03851v1`, `math_0107137v2`, `math_0303168v2` | Candidate only. Needs live title/URL/license/API/language-topic verification before any main-table row. |
| Spanish | `1312.6798v1` | Candidate only. Has quick `Noether`, `Hilbert`, and `anillo` hits, but still needs live title/URL/license/API/language-topic verification. |

## Spanish Supplement

The Spanish-focused candidate supplement records 10 local unrepresented Spanish `.source` packages:

`1312.6798v1`, `1309.7609v1`, `1311.1146v1`, `2206.09700v1`, `2209.02110v1`, `2401.04069v4`, `2410.00616v1`, `math_0212002v2`, `math_9412207v1`, and `physics_0503102v1`.

Important caveat: `2209.02110v1` is listed as an unrepresented local source package because the main table uses the current v2 source witness downloaded in this lane. The v1 package should be treated as version-history context only unless a future source-canon pass has a reason to record it separately.

## Next Actions

- Prefer live arXiv/API/title/license checks for high-signal French candidates before promoting any candidate to the main witness table.
- For Spanish, verify whether `1312.6798v1` is genuinely Spanish-language mathematical source support for the Noether/Hilbert/anillo register and whether its live arXiv/license metadata is usable.
- Keep candidates separate from approved witness rows until title, URL, language evidence, topic relevance, license/access signal, and non-claim boundaries are verified.
- Do not upload raw source bodies from this audit through rolling packages; only manifests/provenance rows belong here unless B3 creates a dedicated gated source-canon payload.

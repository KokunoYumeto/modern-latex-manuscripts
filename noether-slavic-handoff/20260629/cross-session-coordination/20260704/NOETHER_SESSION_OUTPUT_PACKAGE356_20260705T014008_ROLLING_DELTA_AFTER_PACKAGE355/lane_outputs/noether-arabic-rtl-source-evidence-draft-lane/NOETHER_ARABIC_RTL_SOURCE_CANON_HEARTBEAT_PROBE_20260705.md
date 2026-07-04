# Noether Arabic RTL Source-Canon Heartbeat Probe

Created: 2026-07-05

Status: draft source-canon/provenance bookkeeping only. Non-canonical, not native reviewed, not approved, not license-cleared, not a translation artifact, not a package, and not a completion claim.

## Purpose

This heartbeat pass follows the source-canon-first steering for the Arabic RTL lane. It adds or revalidates Arabic target-language mathematical source witnesses for algebra, ring, module, group, and linear-algebra topics, while keeping TeX/source-package gaps explicit.

## New Or Revalidated Witnesses

| Row | Status | Evidence | Hash |
| --- | --- | --- | --- |
| `AR-HB-20260705-001` | New metadata witness | Omar Al-Mukhtar University Press page for `الجبر الحديث`; Arabic language metadata, ISBN `978-9959-79-074-3`, CC BY-NC-ND 4.0 signal, and topic summary including modern algebra, matrices over fields, module theory, lattices, and inner-product spaces. | `230538B261E8FC3DA2E83A137D6686E6A3AB478C067D1375D8A669415015584D` |
| `AR-HB-20260705-002` | New PDF fallback witness | Omar Al-Mukhtar University Press PDF for `الجبر الحديث`; broad Arabic modern-algebra coverage. | `E60FD267AED80573F506683C47E9E2F6ED9C36DDE8809446C137DD5D1FC7188E` |
| `AR-HB-20260705-003` | Derived verification artifact | First 80 pages extracted with `pdftotext`; supports TOC/topic verification only, not layout authority. | `2FCBFB414E46229A8742FE869C228FEF9EA5AD6D4357E3100108F24261387497` |
| `AR-HB-20260705-004` | Existing witness revalidated | Milne Arabic `Group Theory` PDF re-fetched; hash matches the existing Arabic witness table row. | `77B97DF62856083FF960790EA6CEA27E5AD6927241D5F87751B376C8F644A904` |

## Source-Package Probe

Eight GitHub code-search queries for exact Arabic phrases plus `extension:tex` returned no code hits:

- `"الجبر الحديث" extension:tex`
- `"نظرية الموديولات" extension:tex`
- `"الموديولات" "الجبر" extension:tex`
- `"الهومومورفزمات" extension:tex`
- `"غمر الحلقات" extension:tex`
- `"نظرية الزمر" extension:tex`
- `"الحلقات والحقول" extension:tex`
- `"جبر خطي" extension:tex`

Rate-limit snapshot after the probe: `code_search` limit `10`, remaining `2`, used `8`; `core` remaining `5000`; `search` remaining `30`.

## Blocked Candidate

The ResearchGate multi-linear algebra Arabic PDF candidate returned HTTP `403 Forbidden` during the direct PDF probe. No body was fetched, no hash was possible, and no license/access signal was established. It remains a blocked candidate, not a witness.

## Current Source-Canon Effect

- Adds one new Arabic PDF fallback witness for broad modern algebra, including group, ring, module, and linear-algebra-adjacent coverage.
- Revalidates the existing Milne Arabic group-theory PDF witness.
- Does not find any Arabic TeX/LaTeX/arXiv/e-print/source archive.
- Does not close specialist invariant-theory, Artinian, homomorphism/isomorphism, or source-package gaps.

## RTL / Layout Notes

The OMU PDF is Arabic RTL and its extracted text preserves enough content for source-topic checks, but the extraction is not typography-safe. Any future reader or TeX/PDF use still requires Arabic-capable XeLaTeX/LuaLaTeX or equivalent RTL-aware tooling, explicit bidi handling around formula neighbors, and visual QA. This artifact publishes metadata, URLs, hashes, local paths, and blockers only.

## Boundary

No raw source bodies are placed in `outputs`. Local downloaded/cache files stay under `sources/...` for provenance hashing. This pass makes no translation, glossary, term approval, bridge promotion, native-review, canonical-approval, license-clearance, gate-promotion, reviewer-packet, package, Git staging, commit, or push claim.

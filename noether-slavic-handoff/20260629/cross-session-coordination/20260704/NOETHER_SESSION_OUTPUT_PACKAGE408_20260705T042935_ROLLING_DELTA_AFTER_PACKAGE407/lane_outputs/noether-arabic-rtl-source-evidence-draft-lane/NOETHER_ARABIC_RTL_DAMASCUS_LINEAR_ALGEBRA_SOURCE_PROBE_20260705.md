# Noether Arabic RTL Damascus Linear-Algebra Source Probe

Created: 2026-07-05

Status: draft source-canon/provenance bookkeeping only. Non-canonical, not native reviewed, not approved, not license-cleared, not a translation artifact, not a package, and not a completion claim.

## Purpose

This heartbeat continuation looked for stronger official Arabic linear-algebra fallback witnesses after the earlier official-PDF pass left the Archive.org/Baath-style candidates for later review. It admits Damascus University repository metadata, PDFs, and one associated nonexclusive distribution-license text as provenance records only.

## Official Witnesses

| Row | Source | Hash | Use |
| --- | --- | --- | --- |
| `AR-DLA-20260705-002` | Damascus University repository metadata for `الجبر الخطي 1` | `9E4CEE7A7DCAEECD8556FC41B6BB3C584081DDCE1407DD7FE23601D7813755FB` | Metadata/source locator. |
| `AR-DLA-20260705-003` | Damascus University PDF `الجبر الخطي 1` | `5519520D7B8273F4133D35C9B5CDD121F5C2203883BB98A6582669B0E0974261` | Linear-algebra fallback witness. |
| `AR-DLA-20260705-004` | Damascus University full metadata for `الجبر الخطي و مبادئ الإحصاء و الاحتمالات` | `1B3DD3765F2ABC971A2937AA825604181D3917DA86AC7FD2CBEEFAF400392A5A` | Metadata/source locator. |
| `AR-DLA-20260705-005` | Damascus University PDF `الجبر الخطي و مبادئ الإحصاء و الاحتمالات` | `49921D1D0872656B7DBE361D5312E0FAED4ECF61EC8F2DD087F2860398055FBD` | Linear-algebra fallback witness, with statistics/probability adjacency. |
| `AR-DLA-20260705-006` | Associated Damascus University nonexclusive distribution-license text | `9053761570B66FDC880129181338795DFDF560771751D35ABF624AA96C107748` | Access/license signal only; not reuse clearance. |

## Verification Notes

Both downloaded PDF bodies have valid `%PDF` signatures:

- `الجبر الخطي 1`: `%PDF-1.6`, byte count `23372340`.
- `الجبر الخطي و مبادئ الإحصاء و الاحتمالات`: `%PDF-1.7`, byte count `7383146`.

The direct download `HEAD` responses reported `text/html; charset=UTF-8`, but the saved response bodies are valid PDFs. That mismatch is recorded as an access/provenance caveat, not a blocker.

## Extraction Caveat

Local first-5-page `pdftotext` extracts were generated for both PDFs, but each extract is only 5 bytes and has hash `2E9FAEBBD47A57F8D00D2F73A2E412BBF5353A95A112F2278B24F69EE5D14B62`. These extracts are therefore recorded as poor/empty extraction artifacts. They must not be used as Arabic content evidence, typography evidence, or formula-neighboring layout evidence. Topic evidence rests on the repository metadata titles and valid PDF bodies.

## License / Access Signal

The second Damascus repository item exposes a text file titled `رخصة التوزيع غير الحصرية - جامعة دمشق`, hash `9053761570B66FDC880129181338795DFDF560771751D35ABF624AA96C107748`. This is recorded only as a repository license/access signal. It is not a blanket license clearance or permission to republish source bodies.

## Current Source-Canon Effect

- Adds two official Damascus University Arabic PDF fallback witnesses for linear algebra.
- Adds two official repository metadata witnesses.
- Adds one associated nonexclusive distribution-license/access signal.
- Does not find or admit any Arabic TeX/LaTeX/arXiv/e-print/source package.
- Does not close specialist invariant-theory, Artinian, direct ring-homomorphism, or direct isomorphism authority gaps.
- Does not authorize terminology, bridge promotion, translation expansion, or reviewer packets.

## RTL / Layout Notes

These are Arabic RTL PDFs, but this pass did not create a TeX reader or perform visual PDF QA. Because `pdftotext` extraction is effectively empty, no claim is made about Arabic punctuation, bidi ordering, formula-neighboring layout, or extractable mathematical notation. Future reader work still needs an Arabic-capable XeLaTeX/LuaLaTeX stack and visual checks around inline formulas.

## Boundary

No raw source bodies are placed in `outputs`. Local downloaded/cache files stay under `sources/...` for provenance hashing. This pass makes no translation, glossary, term approval, bridge promotion, native-review, canonical-approval, license-clearance, gate-promotion, reviewer-packet, package, Git staging, commit, or push claim.

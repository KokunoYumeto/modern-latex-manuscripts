# Noether Arabic RTL Official PDF Source Probe

Created: 2026-07-05

Status: draft source-canon/provenance bookkeeping only. Non-canonical, not native reviewed, not approved, not license-cleared, not a translation artifact, not a package, and not a completion claim.

## Purpose

This heartbeat continuation looked for stronger non-Wikimedia fallback witnesses after repeated Arabic TeX/source-package misses. It admits only official university-hosted Arabic PDF/metadata witnesses and records weaker mirrors or blocked candidates as excluded.

## Official Witnesses

| Row | Source | Hash | Use |
| --- | --- | --- | --- |
| `AR-PDF-20260705-002` | Damascus University repository metadata for `البنى الجبرية 2 نظرية الحلقات` | `7F6B635DD179B309B32D0771399FD517570F9DA17BEB3CC6010C58CE74AB5887` | Metadata/source locator. |
| `AR-PDF-20260705-003` | Damascus University PDF `البنى الجبرية 2 - نظرية الحلقات` | `B24697BD24D75073246E781402C6316104372F445D1EEE6E54E675A08AF2C1F2` | Ring-theory fallback witness. |
| `AR-PDF-20260705-004` | Tal Afar University PDF `محاضرات نظرية الزمر` | `C3A2DCC3FB6267E4A7E61D7AC7624616E49FC547C9A3F362BA8C529E413F65C6` | Group-theory fallback witness. |
| `AR-PDF-20260705-005` | King Saud University course spec `نظرية الزمر` | `BE0DC74FE8F16AD62C1C5505A4C7B8A5DFD03CD19DE931DCD8AF817C49DCC29C` | Group/homomorphism/isomorphism-adjacent course-register witness. |

## Verification Extracts

All three downloaded bodies have valid `%PDF` signatures. Local first-5-page `pdftotext` extracts were generated for topic checks only:

- Damascus ring-theory extract: `FA3D4BE433AF17BD5AA5B8BB09C39C3554B9C1EE58BE15E60396A726F62535BC`
- Tal Afar group-theory extract: `09E160B4B1B6E9F9DE763883B3E94530811E1DDD8FD8B3F630C01E457479C880`
- KSU group-theory course-spec extract: `D21790756752C4B87495924A46104A66DDF7F97D692953B59A4218E5C47403A1`

These extracts are derived verification artifacts, not source bodies for publication.

## Exclusions

Scribd, Facebook/social mirrors, and blocked ResearchGate-style candidates were not admitted. An Archive.org linear-algebra PDF was left for a future source-authority/access pass because the current pass already found official university-hosted PDF witnesses.

## Current Source-Canon Effect

- Adds one official Arabic ring-theory PDF fallback witness.
- Adds one official Arabic group-theory lecture PDF fallback witness.
- Adds one official Arabic group-theory course specification with homomorphism/isomorphism-adjacent course terms.
- Does not find or admit any Arabic TeX/LaTeX/arXiv/e-print/source package.
- Leaves specialist invariant-theory, Artinian, and direct ring-homomorphism/isomorphism manual-review authority gaps open.

## RTL / Layout Notes

These are Arabic RTL PDFs. First-page text extraction is adequate for topic verification, but not typography-safe. They do not resolve formula-neighboring bidi layout, Arabic punctuation near formulas, or TeX/PDF reader QA.

## Boundary

No raw source bodies are placed in `outputs`. Local downloaded/cache files stay under `sources/...` for provenance hashing. This pass makes no translation, glossary, term approval, bridge promotion, native-review, canonical-approval, license-clearance, gate-promotion, reviewer-packet, package, Git staging, commit, or push claim.

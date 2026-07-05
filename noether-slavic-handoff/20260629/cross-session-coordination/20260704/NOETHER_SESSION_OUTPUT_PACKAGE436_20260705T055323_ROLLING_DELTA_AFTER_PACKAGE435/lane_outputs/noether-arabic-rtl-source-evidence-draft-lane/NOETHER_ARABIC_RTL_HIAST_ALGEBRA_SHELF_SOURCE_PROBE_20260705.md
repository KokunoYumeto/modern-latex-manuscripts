# Noether Arabic RTL HIAST Algebra Shelf Source Probe

Created: 2026-07-05

Status: draft source-canon/provenance bookkeeping only. Non-canonical, not native reviewed, not approved, not license-cleared, not a translation artifact, not a package, and not a completion claim.

## Purpose

This heartbeat continuation checks the official HIAST shelf for Omran Kouba's Arabic algebra volumes after the previous pass admitted a Mustansiriyah-hosted mirror of Algebra I. The goal is provenance tightening: prefer official pages and direct HIAST PDFs over mirrors, and keep TeX/source-package gaps open.

## Official HIAST Witnesses

| Row | Source | Hash | Use |
| --- | --- | --- | --- |
| `AR-HIAST-20260705-003` | HIAST metadata `الجبر - الجزء الأول` | `B6BC54182842C6D160DCC565AF45AA93C667A1FD20384BB03C7C2D6A4355D4E8` | Official metadata/source locator for abstract algebra. |
| `AR-HIAST-20260705-004` | HIAST PDF `الجبر 1 مبادئ الجبر المجرد` | `FAA47DEBCB0157EBB28B4A0D0FAECDC7C52950802CE51C66A4F92DA2446F97E0` | Official-origin upgrade for the existing broad algebra fallback witness. |
| `AR-HIAST-20260705-005` | HIAST metadata `الجبر - الجزء الثاني (الجبر الخطي)` | `CFE49D3DA82F40815DFDC2D43163BCCBC372CDE8FB5C1F937FEB5085DD95E02A` | Official metadata/source locator for linear algebra. |
| `AR-HIAST-20260705-006` | HIAST PDF `الجبر 2 الجبر الخطي` | `9E1A2EC4E2CD27889748DF75DCB9F631734F105A2E19BF542AD52F26470DB06F` | Strong official Arabic linear-algebra fallback witness. |

## Verification Extracts

Both downloaded PDF bodies have valid `%PDF` signatures:

- Algebra I: `%PDF-1.7`, byte count `5456693`, first-5-page extract `CFFBC20B9532025078477284CABF30AFCBAC757F738ECC5718690B8334C304FA`.
- Algebra II: `%PDF-1.6`, byte count `9490179`, first-5-page extract `1BD1052005F5E209C342492A07546FEE9AA048810DA9275FA980C2BB80B573A4`.

The Algebra I official HIAST PDF is byte-identical to the earlier Mustansiriyah-hosted `الجبر 1` witness, so this pass upgrades origin provenance rather than adding a distinct text body. Algebra II is a new official HIAST linear-algebra PDF witness for vector spaces, linear maps, matrices, determinants, systems of linear equations, reductions of linear maps, and inner-product spaces.

## License / Access Signals

The HIAST metadata pages and the PDFs carry CC-BY-ND 4.0 signals. The HIAST pages returned `200 text/html`; the direct PDFs returned `200 application/pdf`, with content lengths `5456693` and `9490179`. These are license/access signals only. This lane does not claim license clearance, payload upload permission, or reviewer-packet eligibility.

## Source-Package Status

The official HIAST pages expose PDF and Google Drive download links, not TeX, LaTeX, arXiv source, e-print source, or other source-package archives. The direct Arabic source-package gap therefore remains open.

## Current Source-Canon Effect

- Upgrades Algebra I from mirror-only fallback to official HIAST-origin provenance.
- Adds a strong official Arabic linear-algebra PDF fallback witness.
- Keeps raw bodies under `sources/...` and puts only metadata/hash/path evidence in `outputs`.
- Does not close specialist invariant-theory, Artinian, direct ring-homomorphism, or direct isomorphism authority gaps.
- Does not authorize terminology, bridge promotion, translation expansion, or reviewer packets.

## RTL / Layout Notes

These are Arabic RTL PDFs with non-empty extracted text. The extracts include bidi controls and formula-neighboring fragments. This pass did not create a TeX reader, perform visual PDF QA, or validate Arabic punctuation next to mathematical notation.

## Boundary

No raw source bodies are placed in `outputs`. Local downloaded/cache files stay under `sources/...` for provenance hashing. This pass makes no translation, glossary, term approval, bridge promotion, native-review, canonical-approval, license-clearance, gate-promotion, reviewer-packet, package, Git staging, commit, or push claim.

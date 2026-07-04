# Noether R7 JQMA Malaysian Malay Ring-Theory Candidate Normalization

Generated: 2026-07-04

Mode: `source_canon_candidate_normalization_manifest_only`

Primary row table:

- `NOETHER_R7_JQMA_MALAY_RING_THEORY_CANDIDATE_NORMALIZATION_ROWS_20260704.csv`

This pass tightens the follow-up JQMA Malaysian Malay ring-theory candidate before any later master-table ingestion. It records article metadata, stable document hashes, policy/license signals, source-package search gaps, and access blockers while keeping all evidence manifest-only.

It does not translate, approve terms, claim native review, claim canonical approval, clear licenses, promote gates, claim completion, or push Git.

## Candidate

Article:

- English title: `Perfect Codes in Graph Theory: A Ring-Theoretic Perspective`
- Malay parallel title: `Kod-kod Sempurna dalam Teori Graf: Perspektif Teori Gelanggang`
- Authors: Nurhidayah Zaid, Nor Haniza Sarmin, Sanhan Muhammad Salih Khasraw, and Ibrahim Gambo.
- Journal: `Journal of Quality Measurement and Analysis` (`JQMA`) 21(2), 153-162, 2025.
- DOI seen in PDF and secondary metadata: `10.17576/jqma.2102.2025.11`.
- Topic tags: `ring theory`, `graph theory`, `perfect codes`, `zero-divisor graph`, `finite rings of matrices`.

## Evidence Rechecked

Remote-hashed document routes:

| Route | Status | Type | Bytes | SHA-256 |
| --- | ---: | --- | ---: | --- |
| JQMA issue page | 200 | `text/html; charset=UTF-8` | 49791 | `429A5A71B782B372115288BC75CD82D8D417C93AF8B0BFB1B19D8E7ED1CAAFF6` |
| Abstract PDF | 200 | `application/pdf` | 87845 | `72C98A51F4F6157995F9E6C0419E856327D9F9898CADC63CCEC0762EA0C7C565` |
| Full paper PDF | 200 | `application/pdf` | 326549 | `72CFA07DBC482140F28B639CA942A523AF05814CB81BC563F603BD8C3A8E1CB5` |

Policy/access sidecars:

| Route | Status | Signal |
| --- | ---: | --- |
| JQMA About the Journal | 200 | Scope includes algebra and graph theory; journal publishes manuscripts in English or Malay. |
| JQMA Guide for Authors | 200 | Author guide mentions Malay/English title/abstract expectations, PDF/manuscript formats, and a LaTeX template route. The template is not an article source package. |
| JQMA Ethics Statement | 200 | Provides a CC BY 4.0 author-license signal for published work; this lane still claims no license clearance. |

Bibliographic and mirror routes:

- MALRep record resolves and points to `journalarticle.ukm.my`, JQMA, and the article metadata.
- Direct `journalarticle.ukm.my` repository and PDF routes timed out over HTTP and HTTPS in this probe.
- ResearchGate mirror confirms DOI and metadata but says author content may be subject to copyright; it remains secondary/dynamic metadata only.
- UTM Applied Algebra and Analysis Group indexed listing confirms the article in a 2025 publication list; it is bibliography/provenance only.

## Source-Package Search

GitHub code search returned zero TeX hits for six exact query clusters:

- `"Perfect Codes in Graph Theory" "Ring-Theoretic Perspective"`
- `"Kod-kod Sempurna" "Teori Gelanggang"`
- `"jqma.2102.2025.11"`
- `"Nurhidayah Zaid" "Nor Haniza Sarmin" "Ibrahim Gambo"`
- `"zero divisor graph" "perfect codes" "Zaid"`
- `"Paper_11" "JQMA" "Ring-Theoretic"`

GitHub repository search returned no article/source repositories. One unrelated broad-title false positive, `AltoTenor/Perfect_Italian_Domination`, was recorded as a negative control, not source evidence.

## Disposition

The article is now stronger than a loose discovery hit, but it is still not merged into the 59-row master required-field table in this pass.

Recommended next action:

- Add it later as a Malaysian Malay remote-hashed PDF fallback/source-canon witness only if the master table is explicitly updated to include post-intake addenda.
- Carry the source-package status as `no_tex_or_article_source_package_found_in_followup_searches`.
- Carry the license/access signal as `JQMA ethics page gives CC BY 4.0 author-license signal; no license clearance claimed`.
- Carry `journalarticle.ukm.my` as an access-blocked retry route.
- Keep issue HTML hashes as access snapshots because the issue page hash changed between the earlier intake and this recheck; prefer the stable PDF hashes for document identity.

## Validation Snapshot

- Normalization rows: 12.
- Required columns missing: 0.
- Blank critical rows: 0.
- Bad boundary rows: 0.
- Bad upload-policy rows: 0.
- Raw source/PDF/HTML payloads written to `outputs`: 0.

## Boundary

Every row carries:

```text
not translation evidence; not term approval; no native review;
no canonical approval; no license clearance; no gate promotion;
no completion claim
```

This is source-canon/provenance maintenance only. The JQMA article is not term authority, not review evidence, not a bridge approval, and not a license-clearance claim.

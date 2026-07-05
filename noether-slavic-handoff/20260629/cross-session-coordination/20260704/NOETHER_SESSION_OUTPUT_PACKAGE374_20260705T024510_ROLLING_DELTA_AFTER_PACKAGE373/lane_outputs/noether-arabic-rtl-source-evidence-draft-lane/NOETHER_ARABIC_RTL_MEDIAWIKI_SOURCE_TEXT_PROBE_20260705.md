# Noether Arabic RTL MediaWiki Source-Text Probe

Created: 2026-07-05

Status: draft source-canon/provenance bookkeeping only. Non-canonical, not native reviewed, not approved, not license-cleared, not a translation artifact, not a package, and not a completion claim.

## Purpose

This heartbeat continuation checked the source-package tier again, then pinned Arabic MediaWiki raw wikitext pages by revision ID as fallback source-text provenance for algebra, ring, module, group, field, and linear-algebra topics.

## Source-Package Probe Result

GitHub code search was probed for ten Arabic `extension:tex` phrase clusters covering invariant theory, rings/ideals, vector spaces, linear maps, homomorphisms, and modules. No Arabic mathematical TeX/source-package witness was admitted. One query returned a false-positive i18n QA corpus under `ClanClanClanClan/latex_perf`, and the final `مودول` plus `حلقة` query hit HTTP 403 code-search access/rate limiting.

## Raw Wikitext Witnesses

| Row | Page | Oldid | Hash | Use |
| --- | --- | ---: | --- | --- |
| `AR-MW-20260705-002` | `حلقة (رياضيات)` | `75116766` | `CCF371C68549D7590DE25003FCC6D3A7C9961B999D4338277CCDA83193298227` | Ring fallback source text. |
| `AR-MW-20260705-003` | `زمرة (رياضيات)` | `75199155` | `9EE18CBE01DD2845B3E248E4FD3BF1F6863D2CDF7D815582B7A17D66F84124E0` | Group fallback source text. |
| `AR-MW-20260705-004` | `حقل (رياضيات)` | `75116379` | `8D1508EE0DA4DEC0962F8BADA8ED9088CA04BDA550686647F922A5F4C618089D` | Field fallback source text. |
| `AR-MW-20260705-005` | `حلقية (رياضيات)` | `75116824` | `8B5519D05F1B4000AC695D03F717600167E2CA5B93555D243B90B9145A1D1504` | Module / `مودول` fallback source text. |
| `AR-MW-20260705-006` | `جبر مجرد` | `75057721` | `663C75B6560B85A8C41EDF6429B2310A9E4CA25FEBCE6294904CF33C4A28005D` | Abstract-algebra fallback source text. |
| `AR-MW-20260705-007` | `نظرية الزمر` | `75472653` | `F1D1832F54A86DE26B36C07A2D73FCB313AA5C37912C0B3D2F5782808319B513` | Group-theory fallback source text. |
| `AR-MW-20260705-008` | `جبر خطي` | `75057716` | `3762E086A6268F425014603D2E31867CB8B2A566F4AA1D9559D511E9B8173103` | Existing linear-algebra raw-text witness revalidated. |
| `AR-MW-20260705-009` | `شباه` | `75235422` | `148178221B31F83F8B1E7C6C0A1F0844D7980E41DD476D99DF2AE7AC88E5D91C` | Homomorphism-adjacent fallback text; use cautiously because the page mapping is not direct ring-homomorphism authority. |

## License / Access Signal

The raw pages are Arabic Wikipedia wikitext pinned to revision IDs. They carry Wikimedia text-license signals such as CC BY-SA/GFDL through Wikimedia terms, but this artifact does not make a license-clearance claim.

## Current Source-Canon Effect

- Adds hashable Arabic raw source text for rings, groups, fields, modules, abstract algebra, and group theory.
- Revalidates the existing Arabic linear-algebra raw-text hash.
- Adds a cautioned homomorphism-adjacent raw-text witness, without approving homomorphism/isomorphism terminology.
- Leaves direct Arabic TeX/LaTeX/arXiv/e-print/source-package gaps open.
- Leaves specialist invariant-theory, Artinian, and ring-homomorphism/isomorphism authority gaps open.

## RTL / Layout Notes

These files are UTF-8 Arabic RTL wikitext with inline math and template markup. They are useful for source-text provenance and hashable revision capture. They are not TeX/PDF reader artifacts and do not resolve formula-neighboring bidi layout or Arabic punctuation QA.

## Boundary

No raw source bodies are placed in `outputs`. Local downloaded/cache files stay under `sources/...` for provenance hashing. This pass makes no translation, glossary, term approval, bridge promotion, native-review, canonical-approval, license-clearance, gate-promotion, reviewer-packet, package, Git staging, commit, or push claim.

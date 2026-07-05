# Noether Arabic RTL Homomorphism / Isomorphism Source Probe

Created: 2026-07-05

Status: draft source-canon/provenance bookkeeping only. Non-canonical, not native reviewed, not approved, not license-cleared, not a translation artifact, not a package, and not a completion claim.

## Purpose

This heartbeat continuation targets the Arabic lane's direct homomorphism/isomorphism gap. The pass prioritizes official or institutional Arabic PDF/HTML witnesses, then records weaker lecture-platform evidence and blockers. It does not translate or approve terms.

No TeX, LaTeX, arXiv, e-print, or source archive was found or admitted.

## Admitted Witnesses

| Row | Source | Hash | Use |
| --- | --- | --- | --- |
| `AR-HOMISO-20260705-002` | Damascus article page, `تمثيلُ زمرةٍ منتهيةٍ على أنواعٍ خاصةٍ من المودولات` | `34B3604079FFC0584287F5BDD4B51F67E24F0475B95968A4D2CD0313A62FAA5C` | Official module/Artinian metadata; `dir=rtl`. |
| `AR-HOMISO-20260705-003` | Damascus PDF | `58C1254FC8F2F7D3C8C6018E2F889B444D631CE212DE371D9BB560DA9EC69B2D` | Official module-representation PDF fallback. |
| `AR-HOMISO-20260705-005` | ENS Kouba `alg411.pdf` | `97281366546BA5019A01B7212659AF3C0999BF55FB0629215076F9368768B29B` | Institutional ring-homomorphism/isomorphism PDF fallback. |
| `AR-HOMISO-20260705-006` | SyriaMath `البنى الجبرية 2` | `35519D9ABFBCF427125ECB8985F4832EDDB8F425A9F3022E78B26D9F7D9C9AB2` | Weak public lecture fallback for `التشاكل الحلقي`. |
| `AR-HOMISO-20260705-007` | SVU Pedia `الجبر الرياضي` | `9D96C60E5A2A47E668B805C7C599A0D7DED1BEBB174E2EB141E68E6825676930` | Education-platform fallback with morphism/isomorphism vocabulary. |

## Text Verification Signals

Textcheck extracts are cached for provenance only:

- Damascus module PDF textcheck: `7193D398DFA06C56026F6821D0B40D871E168B51DA1EE9EC99C1CE4FA31F25F1`
- ENS Kouba textcheck: `9D031CCB8B18EA2C6CE27ED4E2BC849AB0F348C1319AF9B8261A17BC1CBCDA34`
- SyriaMath textcheck: `54B8DA5463AA44406006D2F5296F5710971A4419371F8F05B0397B6530A1D14C`
- SVU textcheck: `EA5F38EC57FB15F629F0032A0DD6FDD010D3E087D565069E64435B85470165F2`

NFKC-normalized counts confirm direct vocabulary support:

- Damascus: `تشاكل` 5, `تماثل` 7, `مودول` 141, `مودولي` 10, `زمرة` 51.
- ENS Kouba: `تشاكل` 2, `تماثل` 7, `تماثلات` 2, `حلقة` 30, `Hom` 6.
- SyriaMath: `تشاكل` 22, `تماثل` 11, `حلقة` 117, `نواة` 2, `Hom` 1.
- SVU: `تشاكل` 16, `مورفيزم` 86, `إيزومورفيزم` 15, `نواة` 24, `صورة` 61.

These counts support source-canon provenance only. They do not authorize Arabic terms, punctuation, formula placement, or reviewer-packet text.

## Blocker

Yarmouk University's BSc mathematics curriculum PDF appeared in web search with `المبرهنة الأساسية في تشاكل الحلقات`, but the lane shell could not fetch the PDF:

- URL: `https://science.yu.edu.jo/images/2025/BScMath.pdf`
- Blocker hash: `32683E7C2A22B2A0F5E360A5E6159C443AF341092AD40AAA43EA62F78A5A337E`
- Cached blocker text: `FETCH_FAILED: An error occurred while sending the request.`

It remains a blocked potential official curriculum witness, not an admitted source body.

## License / Access Signals

Damascus page metadata carries a 2023 `DC.Rights` copyright string for the Damascus University Journal of Basic Sciences. ENS Kouba, SyriaMath, and SVU PDFs were accessible by HTTP 200, but no explicit reuse license was found or cleared. This pass records access and rights signals only, not license clearance.

## RTL / Layout Notes

The Damascus article page is explicitly `dir=rtl`. PDFs have valid `%PDF` signatures and searchable textcheck extracts, but no visual PDF QA was performed. Mixed Arabic/Latin/math text, bidi ordering, and formula-neighboring layout remain unapproved.

## Boundary

No raw source bodies are placed in `outputs`. Local cached HTML, PDFs, textcheck extracts, and blocker notes stay under `sources/...` for provenance hashing. This pass makes no translation, glossary, term approval, bridge promotion, native-review, canonical-approval, license-clearance, gate-promotion, reviewer-packet, package, Git staging, commit, or push claim.

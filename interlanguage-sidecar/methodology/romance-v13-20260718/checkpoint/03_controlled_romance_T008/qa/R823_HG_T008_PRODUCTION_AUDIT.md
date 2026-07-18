# R823-HG-T008 production audit

Date: 2026-07-18  
Scope: `R823_HG_T008` only  
Review status: model-assisted production/source/semantic/visual self-audit; zero human or native-reader review

## Bounded result

T008 packages the complete §6 at German authority lines **21291-21307**: 17 source lines, 10 nonblank lines, 8 clause segments, 11 target blocks, 21 terminology decisions, 13 grammar decisions, one editable target TeX unit, and a 2-page A4 PDF. Line 21308 is blank; the continuation cursor is line **21309**, `§ 7. Die Isomorphismen eines Körpers`.

The validator status is `PASS_BOUNDED_PROVISIONAL_UNIT_ONLY`. This proves the declared source binding, semantic invariants, deterministic build, output-copy equality, extraction, and pinned-render checks for this unit. The live validator now derives and checks the invariant demonstrative surface `iste es contenite` and rejects lexical `istes`. It is not a completed R823 or Romance-lane claim.

## Authority

- Pinned ZIP: `${LOCAL_USER_ROOT}\Documents\Papors\Chatnotes\CHat translates and clean\Noether Multilingual\Noether_R823_WebB_R822_P20p27_31_RunInDashRefine_20260717_COMPLETE.zip`
- ZIP SHA-256: `7AFC1B865EC710F6BECE507260605CBA7C950E5CC089C7464F63CBC20A8BD738`
- Unique cumulative member and extracted authority SHA-256: `EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21`
- Exact LF source slice: 2,245 bytes; SHA-256 `9DE53B572F81D96A2278AF906F158794816C68A0056497B31D92A48F2598D794`
- Numbered source: `FA6F7A98A0116C3D636447853ECECDCE3E69E20FF7B7200B37CBF1078AF010DA`
- Source metadata: `6C869BC52DB7D0836FE98EE163A883F7EDEB6E3FEF8D5D42C508E333E1A57552`
- Source manifest: `CDDACAE135ECFDCF2F0E7F4ECC29E417D42CFE065CBEB34FCA2B3756C85375E7`

Every nonblank authority line is covered exactly once in the clause map. The target marker set equals the clause-map marker set exactly.

## Semantic controls

The target preserves: the commutative-system scope; algebraically closed extension-field hypothesis for `Omega`; both directions of the reduction from `Z` to `Z_Omega`; the source's compact basis-element clause; the locally defined regular representation; unqualified `Radikal` without an invented Jacobson/nilradical subtype; the fully-reducible/direct-sum/finite-degree/algebraic-closure inference chain; multiplicative identity sense `T60-S1` rather than generic unit sense `T60-S4`; exactly `t` irreducible representation classes of degree one with `t <= n`; the literal equality `pi^{-1} alpha pi = alpha`; and exactly `t` homomorphisms onto subrings without a premature upgrade to §7 isomorphisms or automorphisms.

Terminology uses 25 verified WordWeb v10 sense links and one extension-node link. Ten missing specialist qualifiers/objects remain explicit `none_*_not_in_wordweb_v10` gaps. No form is promoted. The access ledger remains 106 senses × 9 cohorts = 954 rows, with zero human observations, zero pilot-eligible rows, and zero promotions.

## Build and visual QA

The following were replayed successfully:

```powershell
python R823_HG_T008\scripts\prepare_source.py
& 'R823_HG_T008\scripts\build_t008.ps1'
python R823_HG_T008\scripts\validate_t008.py
python R823_HG_T008\scripts\validate_t008.py
```

Primary build, repeat build, and final output copy are byte-identical after the controlled-language repair from plural `istes` to invariant `iste` in T-080:

- `R823_HG_T008/build/R823_HG_T008_romance.pdf`
- `R823_HG_T008/build_repeat/R823_HG_T008_romance.pdf`
- `${INTERLANGUAGE_ROOT}\output\pdf\R823_HG_T008_controlled_romance.pdf`
- Bytes: 93,483
- SHA-256: `4AA696322AB593F88736EEB0C5CAD0648E06ABC7F14325EC73CFDDCAACD8D1E8`

The two 150-dpi renders are 1241 × 1754 pixels and were inspected at original resolution:

- page 1: `F5387A3D7C982842EBDE61A078C5E579CE0018DD2747573C1D6F18E0B46DABA2`
- page 2: `CF9B8359F13251E51F03C1F76E2445A4504D33AB58D251CD9E72AF3FEBA3E214`

No clipping, overlap, missing glyph, black box, top-boundary collision, or accidental blank page was observed. Page 2 begins below a deliberate top inset; its lower whitespace is intentional. Visual review concerns layout only.

The validation JSON is byte-stable across two consecutive runs:

- `R823_HG_T008/qa/R823_HG_T008_validation.json`
- Replay 1 SHA-256: `21191BB18E391DD2A858755E31EF30A8C61F3F8C851096961D9E780B9A4A9AC5`
- Replay 2 SHA-256: `21191BB18E391DD2A858755E31EF30A8C61F3F8C851096961D9E780B9A4A9AC5`

## Control hashes

| Artifact | SHA-256 |
|---|---|
| Clause seed | `F98D3244C6346D1D65D0E59863E753BE63ED73E1A61902C2A5726622FFB7107E` |
| Clause map | `3459E41888627F497673BEA2927A9EA56A610225B9057DE08BD65BEC22C34151` |
| Terminology CSV | `984A754A430E7940118AB24ACAAB8F5066B385B085598E3D1DCD58CCC25BA864` |
| Grammar CSV | `CCD12853FE774DBF7C0978D364EBF0D40DAF6062065E01F9CEAF80D96798DCC8` |
| Target TeX | `A137F0F53DDA7F16835BDCCCD9751A213ED578A58D7DA85F4C96458C00B47AC6` |
| Prepare script | `BCAC905C5CEECCAD229F8FFDECD6446D7A8B20D26FF98910928F37875817EA86` |
| Build script | `6DCA0C02B77F2C76790EDE422BCAC09B61F5878B3CBD68E5CD0CBF14D5B6AF95` |
| Validator script | `2CCEBDEF29F7BCEAC324F48B944086256885B7DA9AD82BCD1324D2307FFBA489` |
| Extracted PDF text | `929BA310D849D93D7E8753F095CEC5C4253BF4E18119E1AE034BB6D524881937` |
| pdfinfo | `3F817A62250883F05DEA5E3AEDC6E3733471F189FDE8D7E949B3253C69B6BF82` |
| Visual-QA note | `7A0393F02008C820B4520C680801646B9EE5A869469D9CC8DECD0930B57DBBC0` |
| Cursor | `2F9ACA2370A3731F617CBC81179F368FCFC014BE6643AE099BC5DA84C4DCD42F` |
| Build TeX log | `63E7FD7D0F7293F3FACC785BC6807BD841034561461E6987ECA0E761E6B6F34F` |
| Repeat TeX log | `597C01E42BD2AFDAA5681685546ACDB2E62CBEF52A9F7A020C13A3F8CEEE895A` |
| Build console log | `DCE65665C4BF69B676BE31177BFB1FFC1D385D1E39C339E5D958B50F30FAEE04` |
| Repeat console log | `46BF8A2D4FE9CE28A1B285F9446C4E4A0104F7676C1161C046E5B83C1B12E468` |
| Build pass-one log | `30C418798236D514513C862445EC4947F6D8EF41A322846A7EEC4946734C40E6` |
| Repeat pass-one log | `D47BA694FC185F86C7A8306480ACECB2A7640101913540EBD78773ED2CEE333E` |

Frozen semantic inputs: WordWeb v10 `CF4521D7758C4B22E6260EA56BD04D57CF89B0F2083C70DDFE012BE50274F3E9`; effective links v10 `53EC1CBD5F74451B59DC19ED49A8E94EA20B6521372547B3515770FA54445D3B`; access ledger v10 `25F0724672E8C635E0CACE4F03579BAA46B0F4A3F86DEADAAE0AD1B802871236`; semantic-link contract `0EEC70319DA18D5321C6B05FC9D27F270A9121BAD1E7901C9D8CFB5133B5B5B7`.

## Superseded held checkpoint

The initial T008 artifact set was held before publication when the plural surface `istes` was found to violate the established invariant demonstrative decision. Its identities are retained here as provenance, not as current or publishable files: target TeX `47089E2A3AF3C44555D95BA408AA7A4F134D828B8DE2E62ED0AAE61224A4F7E8`; grammar CSV `E8E84FEF063CDD63BEFC755ACB308E7C647EA7858BED899A9C6484B69FB2DCB1`; PDF/output copy `CA79655CE5A72F573B279A80B86C9C34B033766B2A751C4B6BD0523377869E7E`; page-1 render `02B46BBD019480522FA6442090722A5B104697D0E3A4C9B06310A45630F3FE56`; page-2 render `CF9B8359F13251E51F03C1F76E2445A4504D33AB58D251CD9E72AF3FEBA3E214`; validation JSON `43BC4F9EE5F3208A7D2B74488560551FDD2CB8B61D46DF14FCBDDA2A731FAC06`; production audit `16ABBDEACAC14848689ED2F0C289CFD3A5EB428FC4DF38D27EB97972F30DD3C4`.

Only the repaired identities recorded above are current. Page 2 is byte-identical across the repair because the changed word appears on page 1.

## Caveats

All controlled-Romance forms are provisional construction candidates. Human/native review, pilot observations, and empirical intelligibility observations are all zero. Source and machine QA for one bounded unit cannot certify the controlled language globally. This repaired T008 set replaces the held, unpublished pre-repair T008 checkpoint; no earlier published public PDF is superseded. It extends T001-T007. The continuation cursor is line **21309**.

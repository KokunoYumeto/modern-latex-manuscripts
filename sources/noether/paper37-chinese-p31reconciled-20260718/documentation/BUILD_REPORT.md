# Build report

The accepted German control, `zh-Hans-CN`, and controlled-generic `zh-Hant` TeX files were each compiled twice with XeLaTeX and halt-on-error. Their final logs contain zero error, warning, overfull, underfull, missing-character, fatal-error, or undefined-control matches.

| Artifact | Engine | Pages | TeX SHA-256 | PDF SHA-256 | Log SHA-256 | Current result |
|---|---|---:|---|---|---|---|
| German control | XeLaTeX | 5 | `0AA0DBE6A75C70BABDD08E5CC93BA953ED904F913BEDBDA85F48D3DCB2BE2909` | `509F53D9ADF50FA29375F59BE8B9CE93E8E04E237319AC24B3760F40D291686F` | `986CFD311B6E18E27C1961810F2106A1DFFDC2578C5847FB0C3AEF40C149BEEF` | pass |
| `zh-Hans-CN` | XeLaTeX | 4 | `A4A0A97E548840915650FE813AED8FC120D2ABE79F3FA76F9ADF35D5EDAB1B0C` | `86C7274D137A51469F91D6939D3F3583BFB982CFE69ACE264064A473DA62405A` | `19B9D236D9B316B70E4D254C6AD970BC2398CEC3682170362DF71AF613D3EA72` | pass |
| controlled generic `zh-Hant` | XeLaTeX | 4 | `FC2493ADE14D66835C0EBAAD7C84C78AFFD33A357594F45384CD518C94F32012` | `35ADCF5A0B9FD5AEEAD16F7E126DFB89B1A9D4BB509FE9661A268C6B897AC36A` | `C31DC7CBFE272A7E5088B193FE0FFB372ED362CC7227F7875C35E78BACB86B8A` | pass |

The German standalone contains the exact sealed logical LF body once, unchanged; its Unicode wrapper correction addressed rendering of German `ß` without changing the sealed body. That wrapper issue is not a source defect.

`qa/BUILD_LOG.json`, SHA-256 `70636F48074C1B2BD714E251CC85D04F0B45E8C00C2F8B87175FFA686A2BB2B7`, is the machine-readable record generated after all final-render dependencies and the explicit internal visual-inspection attestation were present. Compilation success is not represented as linguistic, regional, external, or human validation.

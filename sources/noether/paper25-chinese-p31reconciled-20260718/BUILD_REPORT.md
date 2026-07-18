# Build report

On 2026-07-18, the German control, `zh-Hans-CN`, and controlled generic `zh-Hant` TeX files were each compiled twice with halt-on-error. Final logs contain zero error, warning, overfull, underfull, missing-character, or undefined-control matches.

| Artifact | Engine | Pages | TeX SHA-256 | PDF SHA-256 | Result |
|---|---|---:|---|---|---|
| German control | pdfLaTeX | 3 | `7759735DFD7BCB5FCA7B9DF7A5C7110FFB3FCC992D05A7E800CEBB37A3D6F582` | `0E5DFFE46C26A9B39004C0048939FF0CFACCD1815CEA3B240E799BF3BE01B9E6` | pass |
| `zh-Hans-CN` | XeLaTeX | 2 | `FA11708D0CC956F7CC065B21716AB947484954C6392720325F624DFDF1CD130C` | `7762F68FF167DAE239D55670E64001BC1979FEB71C9B648C29E34C54C21FC4C7` | pass |
| controlled `zh-Hant` | XeLaTeX | 2 | `F1831DCCBA2FABDAA1DA9E7DB60D0B9981D9D64B765A77F97596CE7D5D25B963` | `55EC6115116AF900A59D4EB846A51148395FADCE240E1D51565698621F9F7D56` | pass |

`qa/BUILD_LOG.json` is the machine-readable build record. Compilation success is not represented as proof of translation fidelity.


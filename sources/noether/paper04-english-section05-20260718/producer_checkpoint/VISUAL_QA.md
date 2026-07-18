# Visual QA

Both packaged PDF pages were rendered at 200 dpi and inspected individually at full rendered resolution. The two-page contact sheet was also inspected.

- Page 1: 524,798 bytes; SHA-256 `B5D34DBCCD5A20841D3C1E8CF5AB59B64EACC5371A2FB02E0915792D7DF1A2AC`.
- Page 2: 582,532 bytes; SHA-256 `1E3D47698536632D6C3F520A17AA2BA9682ED41839C8149698E8A379A0C516B8`.
- Contact sheet: 552,157 bytes; SHA-256 `214A7E8BA96C90F65E300C80112247102D2D2779585F4F85DDE5235FE840ED64`.

Fresh isolated-build renders reproduce both packaged page images exactly: absolute-error pixel count 0 and RMSE 0 for each page. No clipping, collision, unreadable formula, broken footnote flow, missing relation label, or visible rendering defect was found. The bounded whitespace at the bottom of page 2 follows the three footnotes and closing-section flow and is not a defect.


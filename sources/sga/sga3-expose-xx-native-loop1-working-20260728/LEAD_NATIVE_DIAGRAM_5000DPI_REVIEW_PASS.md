# SGA 3 Exposé XX — lead native-diagram 5000-dpi review PASS

Date: 2026-07-28

Status: PASS for the complete Exposé-XX native-diagram Loop-2 surface.
This is a top-level lead review. Mathematical and visual judgment was not
delegated.

## Scope and authority

- Scope: all ten atomic diagram panels in Exposé XX.
- Authority: `Exp20-13oct24.pdf`, local pages 1–35 / combined pages
  1060–1094.
- Authority bytes: 332,777.
- Authority SHA-256:
  `9B8B790E1F07EA4B6E07DA98A2ABAE048A8D40648A8F7C5EC909EA73B92411FA`.
- Hard stop: before Exposé XXI local page 1 / combined page 1095.
- Delivery is native editable TeX only. No raster diagram is active in
  the delivered source.

Private PNG crops listed below are source-comparison evidence only. They
are not delivered diagram implementations. Existing 600- and 1200-dpi
evidence remains legitimate append-only history and context. No
300-dpi image carries a fidelity decision in this review.

## Manual panel-by-panel result

| ID | Authority / delivered locator | Lead decision |
|---|---|---|
| D001 | local p. 6; `02_expose_XX_proof17_through_proof110_en.tex:149`; physical p. 8 | PASS after repair. The predecessor put `g_C` on the target-right side of the vertical arrow. The successor moves it to the source-left side, matching the authority and `g_B`. |
| D002 | local p. 18; `08_expose_XX_lemma214_through_theorem31_statement_en.tex:11`; physical p. 22 | PASS without repair. |
| D003 | local p. 18; same component line 28; physical p. 22 | PASS without repair. |
| D004 | local p. 18; same component line 40; physical p. 22 | PASS without repair. |
| D005 | local p. 23; `11_expose_XX_remark39_through_prop311_en.tex:9,18`; physical p. 28 | PASS after repair. The predecessor split the two-row diagram across physical pages 27–28. A native unbreakable container now keeps both rows together on physical p. 28, matching the authority. |
| D006 | local p. 24; same component line 97; physical p. 29 | PASS without repair. |
| D007 | local p. 25; `12_expose_XX_prop312_through_cor44_en.tex:89`; physical p. 31 | PASS without repair. |
| D008 | local p. 29; `13_expose_XX_section5_par51_through_par56_en.tex:245`; physical p. 35 | PASS without repair. |
| D009 | local p. 30; `14_expose_XX_par57_through_theorem511_en.tex:6`; physical p. 35 | PASS without repair. |
| D010 | local p. 30; same component line 27; physical p. 36 | PASS without repair. |

For every panel the lead compared the authority and delivered result at
approximately 5000 dpi at original detail. The comparison covered every
node, arrow, direction, arrowhead, attachment point, label text, label
side, prime, subscript, superscript, star, tensor exponent, and relevant
relative placement. No unresolved ambiguity remained, so no 9000-dpi
escalation was necessary.

## Exact 5000-dpi authority evidence

| ID | Bytes | SHA-256 |
|---|---:|---|
| D001 | 342,190 | `55F906217926A0E5DF8494D83EA05FE7A326DD593E821DE64649BA3605451400` |
| D002 | 342,536 | `CAFBA6393ACC46599A9E1E206E8A8ED116C29794399216CC3784B4B360812C6F` |
| D003 | 227,932 | `C8E09EBB97AD45204C08B32D42E0C1377DCF7424E644F785477C891006D3DC10` |
| D004 | 335,225 | `533371B1CFC1524331D25699DA2A8AA300EAE4E9807140359A1FFBFE0316E472` |
| D005 | 560,042 | `2C6DE941E8F758162252931BE52A722FD77507633F2E9DFD885E55ED484100F2` |
| D006 | 531,122 | `BF786B876659032F3A1CDFCF087E0932F45AC45D2FAED0160C97E78D307484DA` |
| D007 | 735,853 | `1CB5DE2E515F1029EFF5121FBE9A4B27C7653C0BD9D10E54345E5AD03E19C390` |
| D008 | 4,142,182 | `E14DBE0EDBA85CD9D0949ECAC6A42305D6A263CEF5603487EDD9D485EA5C59E4` |
| D009 | 2,177,737 | `9C6AAA077E1EE03228A8D3DA6BF7E720EFBA9790A17615F3E92D31BA6E05156D` |
| D010 | 4,094,197 | `1C5F158596E91AC1EBCB7F62D32A0BB1285A975CC43D55D09E770D17C7FA3F0E` |

## Exact delivered 5000-dpi evidence

Evidence root:
`qa/native_redo_20260728/delivered_5000dpi`.

| ID | File | Bytes | SHA-256 |
|---|---|---:|---|
| D001 | `xx_d001_proof110_delivered_5000dpi_r5_final.png` | 1,016,565 | `4D425196028D82BF1C53B603A1FF4CF6AB7DDCFDD4AC5A1F57D1751F8DB30584` |
| D002 | `xx_d002_lemma214_1_delivered_5000dpi.png` | 2,241,213 | `C1E4EADD2749C0D40777D4DF991D4DBE82EF9BA2ABF0982175F77580E53D024D` |
| D003 | `xx_d003_lemma214_2_delivered_5000dpi.png` | 1,798,182 | `3FAA04BEBD9B455DCF694A9168E38E82418CF687E96A3A098F45AA18E6DCFA92` |
| D004 | `xx_d004_lemma214_3_delivered_5000dpi.png` | 2,755,673 | `ABEE45E621E5E962D4721811720CBE4281536C6681437C7AF91D595B3690246C` |
| D005 | `xx_d005_remark39_delivered_5000dpi_r5_final.png` | 2,638,335 | `22B1BE1DDAF910DA1E617D5D46944A297EA668D2CA550CB40475D58AF0C4850E` |
| D006 | `xx_d006_prop311_delivered_5000dpi.png` | 2,523,920 | `3B2093737855B196228898FEAD11D04BAA7F7D533B3D66297CB7BA34B512873F` |
| D007 | `xx_d007_theorem41_delivered_5000dpi.png` | 1,806,260 | `BD86D08E580A1B3296DEA6C27CD314862DDBD16A355BF1650B187FA565D8F24F` |
| D008 | `xx_d008_par56_delivered_5000dpi.png` | 2,836,439 | `D16B5CA1F1EEA909674BCD3413C8AC180104625B2DF89C32B14D5FB6E9417038` |
| D009 | `xx_d009_par57_1_delivered_5000dpi.png` | 3,724,608 | `315825DCF7D2184E183FF99066BA0DC8FD976F78928B34BC01C2CAEF8F6EE79A` |
| D010 | `xx_d010_par57_2_delivered_5000dpi.png` | 4,093,446 | `6C202A9B174D51A8E5F134495D197B7DA2222A43B88FB0BA6B538877CE9E7B70` |

The earlier D001 crop (wrong `g_C` side) and D005 crops (split layout)
remain append-only adverse evidence and are not final-PASS evidence.

## Native source and build closure

- Master: 2,163 B, SHA-256
  `9DF5337BDDADAC34B59626159D543660FAE6AA9F84A85F2FAB2516EBB4535D6C`.
- D001 component: 5,224 B, SHA-256
  `1D0E88F8F4F894327DC030EA5F2B441F8728650ACF399394CAEAD32C2B181A97`.
- D002–D004 component: 4,730 B, SHA-256
  `8F16792D19896D1E74A74FE8D57A185DAC16D69EE51AA0D504608E9A1D386CFE`.
- D005–D006 component: 5,607 B, SHA-256
  `B245CEB65CC82FC7C1D9AA06B0A1BA461F3FE5CFDB24F14AF158F46BA6AD6D2E`.
- D007 component: 6,178 B, SHA-256
  `5CB41ECE651C38B6ABAD864DCFF2A1707871671F1DCA16C501D7960B61602CBD`.
- D008 component: 8,426 B, SHA-256
  `67E44F09C52373554CCC18F482403B93CBF46A726293DC88D85920C1466F2D08`.
- D009–D010 component: 6,944 B, SHA-256
  `509648B88D0B34F6B688921BD51BBEE7BB932B54B9E4D9B308F35B5CD755990F`.
- Final reader: `build_native_r5/SGA3_Expose_XX_English.pdf`,
  41 A4 pages / 236,960 B, SHA-256
  `AE0C41D952065552E86E161F968B273DC9229443E46492E5300D110A9180148D`.
- Final log: 39,602 B, SHA-256
  `4FBD19EC672C0A2D8A443EFAA93CED72024CFB12793FC862346FCE4B10DE144A`.
- Three clean XeLaTeX passes exit 0. The final log has zero fatal,
  undefined-control, multiply-defined/duplicate-destination,
  missing-character, overfull/underfull-box, or rerun diagnostics.
- Active `\includegraphics` calls in the delivered TeX tree: 0.
- Native diagram panels: 10/10.

`build_native_r3` and `build_native_r4` preserve command-invocation
failures (wrong working-directory/PowerShell argument handling). They
are adverse execution history, not mathematical or visual PASS
evidence, and were not overwritten.

## Disposition

The Exposé-XX native-diagram surface is closed: 8/10 panels passed
without repair and 2/10 passed after explicit copy-on-write repair.
Reference-v2 closure, cumulative-volume integration, release packaging,
archive transport, publication, and public readback remain unclaimed.

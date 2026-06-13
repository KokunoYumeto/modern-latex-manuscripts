# Pending Zenodo Uploads

This page lists local packages that have been discovered, extracted, checksummed, and staged, but are not yet present in the public Zenodo file catalog. Do not cite these as public Zenodo files until a token-backed upload/publish pass succeeds and the public file catalog is regenerated.

## 2026-06-13: Noether Paper 13 GDZ source-witness locator, targeted crops, and source-audit webdrop

Manifest: [20260613_noether_p13_gdz_source_witness_locator.json](../manifests/pending-zenodo-uploads/20260613_noether_p13_gdz_source_witness_locator.json)

- Noether: `Noether_P13_GDZ_Source_Witness_Locator_20260613.zip`, 60.2304 MB, SHA256 `BB4AB280D72D9B38289BFD09635251E954471028C3F44DD7467AFFCC9E655C0F`.
- Noether: `Noether_P13_GDZ_Targeted_Witness_Crops_20260613.zip`, 8.4044 MB, SHA256 `9A7A0E9B1519F5E365F141494F29159846D5C101CE6A97F85373245A21A6B3B2`.
- Noether: `Noether_P13_GDZ_Source_Audit_WebDrop_20260613.zip`, 8.8276 MB, SHA256 `6C150A46E979E56713DBAAE1B2AF0E581A095D93186FE68C3E4E144877E423DD`.
- Contents: source-master witness/provenance support and targeted audit material for Paper 13, not a corrected TeX branch. The locator package includes the GDZ full-volume source PDF, IIIF manifest, source metadata page, article page/canvas map for original printed pp.235-257, and full-resolution page-image witnesses. The crops package adds seven labeled high-resolution page-local witnesses for front matter, footnote/citation readings, derivative-index notation, the `u_i`/`v_i` initial-system check, and formula (30). The source-audit webdrop adds CSV findings, patch suggestions, source-quality note, and witness manifests; it reports a high-priority source-confirmed formula (30) defect, a derivative-index source-fidelity correction, a Lie citation omission, and front-matter/orthography editorial decisions.

Next action when Zenodo API credentials are available: upload with the next Noether source-audit/provenance Zenodo version, then update record IDs, metadata JSON, `manifests/public-file-catalog.csv`, generated record pages, and status docs. Use these files to support Paper 13 correction, but do not treat them as Paper 13 source closure, applied TeX, or an edition.

## 2026-06-13: Noether Paper 14 targeted source-audit results web drop

Manifest: [20260613_noether_p14_audit_results_webdrop.json](../manifests/pending-zenodo-uploads/20260613_noether_p14_audit_results_webdrop.json)

- Noether: `Noether_P14_Audit_Results_WebDrop_20260613.zip`, 0.0166 MB, SHA256 `32B14684CAF5D836B1E64E4D912477C5C8180ECDA8B21F2CD30C9EC11295F310`.
- Noether: `Noether_P14_Targeted_Source_Audit_Witnesses_20260613.zip`, 75.1752 MB, SHA256 `0D0AD8172561859596187768AE954BD9CFAF15C97AA3FFC542DC60753BAA0C8C`.
- Contents: Paper 14 targeted German source-audit results for `Die arithmetische Theorie der algebraischen Funktionen einer Veraenderlichen in ihrer Beziehung zu den uebrigen Theorien und zur Zahlkoerpertheorie`, JDMV 38 (1919), printed pp.182-203. The compact package records findings; the witness package carries the source PDF, page PNG witnesses, and OCR/raw text locator material. No patched cumulative TeX branch is included. The audit reports three high-severity source-confirmed mismatches: printed p.190 has `(z-c)`, not `(z-\alpha)`; printed p.198 has factorization exponents `\rho_i` and terminal `\sigma`, not `e_i` and terminal `\rho`; printed p.200 uses exponent pair `\rho,\sigma`, not `\nu,\nu'`. Checked no-fix anchors for other formula blocks are included.

Next action when Zenodo API credentials are available: create a new Noether Zenodo version, upload these ZIPs together with the other pending Noether source-audit packages if still pending, publish, then update record IDs, metadata JSON, `manifests/public-file-catalog.csv`, generated record pages, and status docs. Also use these findings as explicit patch targets in the next canonical German cumulative TeX pass. Do not treat this as whole-corpus or complete Paper 14 closure.

## 2026-06-13: Noether Paper 15 targeted source-audit web drop

Manifest: [20260613_noether_p15_targeted_source_audit_webdrop.json](../manifests/pending-zenodo-uploads/20260613_noether_p15_targeted_source_audit_webdrop.json)

- Noether: `Noether_P15_Targeted_Source_Audit_WebDrop_20260613.zip`, 59.1544 MB, SHA256 `7C6C7422FF618B374CD40E49D79EB3E21586C8118D7E1084D7778118AAA86D74`.
- Contents: Paper 15 targeted source-audit drop for `Die Endlichkeit des Systems der ganzzahligen Invarianten binaerer Formen`, Goettinger Nachrichten 1919, pp.138-156. The package reports two source-confirmed corrections: the normalization block on printed p.152 uses ordinary italic Latin `x_1,...,x_{\rho+\sigma}` index symbols, not Greek `\chi`, and the Schur citation on printed p.154 is `S. 355 (1912)`, not `S. 555 (1912)`. The local working TeX was patched, and a patched cumulative TeX copy is included under `applied_fixed_tex/`.

Next action when Zenodo API credentials are available: create a new Noether Zenodo version, upload this ZIP together with the other pending Noether source-audit packages if still pending, publish, then update record IDs, metadata JSON, `manifests/public-file-catalog.csv`, generated record pages, and status docs. Do not treat this as whole-corpus or complete Paper 15 closure.

## 2026-06-13: Noether Paper 16 source-audit web drop

Manifest: [20260613_noether_p16_source_audit_webdrop.json](../manifests/pending-zenodo-uploads/20260613_noether_p16_source_audit_webdrop.json)

- Noether: `Noether_P16_Source_Audit_WebDrop_20260613.zip`, 2.4034 MB, SHA256 `F90F1E83EEF65BBFE0F6F7CFFC60EA761F726DEC6FC143485878615120D52C8B`.
- Contents: Paper 16 compact source-audit drop for `Zur Reihenentwicklung in der Formentheorie`, Math. Ann. 81 (1920), pp.25-30. The package reports one high-severity source-confirmed drift on printed p.30: the source says the invariants are composed from `F` and forms from `M`, not from `\Phi` and forms from `M`. The local working TeX was patched from `aus $\Phi$ und aus Formen aus $M$` to `aus $F$ und aus Formen aus $M$`, and a patched cumulative TeX copy is included under `applied_fixed_tex/`.

Next action when Zenodo API credentials are available: create a new Noether Zenodo version, upload this ZIP together with the other pending Noether source-audit packages if still pending, publish, then update record IDs, metadata JSON, `manifests/public-file-catalog.csv`, generated record pages, and status docs. Do not treat this as whole-corpus or complete Paper 16 closure.

## 2026-06-13: Noether Paper 17 targeted source-audit web drop

Manifest: [20260613_noether_p17_targeted_audit_webdrop.json](../manifests/pending-zenodo-uploads/20260613_noether_p17_targeted_audit_webdrop.json)

- Noether: `Noether_P17_Targeted_Audit_WebDrop_20260613.zip`, 19.6794 MB, SHA256 `6F6A87DD3614F9092FD808785AE07FF39619D5EE4A83C9099FF35803E375C9B3`.
- Contents: Paper 17 targeted source-audit drop for Noether-Schmeidler, `Moduln in nichtkommutativen Bereichen, insbesondere aus Differential- und Differenzenausdruecken`, Math. Zs. 8 (1920), pp.1-35. The package reports two source-confirmed missing footnotes around formula (39): footnote 21 after the displayed equality ending `=r^{\sigma\rho}b_\rho`, and footnote 22 after the `=a_\sigma` relation. The local working TeX was patched, and a patched cumulative TeX copy is included under `applied_fixed_tex/`.

Next action when Zenodo API credentials are available: create a new Noether Zenodo version, upload this ZIP together with the other pending Noether source-audit packages if still pending, publish, then update record IDs, metadata JSON, `manifests/public-file-catalog.csv`, generated record pages, and status docs. Do not treat this as whole-corpus or complete Paper 17 closure.

## 2026-06-13: Noether Paper 18 source-audit web drop

Manifest: [20260613_noether_p18_source_audit_webdrop.json](../manifests/pending-zenodo-uploads/20260613_noether_p18_source_audit_webdrop.json)

- Noether: `Noether_P18_Source_Audit_WebDrop_20260613.zip`, 1.1477 MB, SHA256 `9C37798142FE0978C562EDA776F9FA941D2D33109E37AC00967F500DA93D9938`.
- Contents: Paper 18 source-audit drop for `Ueber eine Arbeit des im Kriege gefallenen K. Hentzelt zur Eliminationstheorie`, source p.101. The package reports one high-severity source-confirmed resultant-display defect: the source relation is congruence modulo `\mathfrak M`, not equality. The local working TeX was patched from `R^{(n)}(x_n)=0(\mathfrak M)` to `R^{(n)}(x_n)\equiv0(\mathfrak M)`, and a patched cumulative TeX copy is included under `applied_fixed_tex/`.

Next action when Zenodo API credentials are available: create a new Noether Zenodo version, upload this ZIP together with the other pending Noether source-audit packages if still pending, publish, then update record IDs, metadata JSON, `manifests/public-file-catalog.csv`, generated record pages, and status docs. Do not treat this as whole-corpus or complete Paper 18 closure.

## 2026-06-13: Noether Paper 08 targeted source-audit web drop

Manifest: [20260613_noether_p08_targeted_audit_webdrop.json](../manifests/pending-zenodo-uploads/20260613_noether_p08_targeted_audit_webdrop.json)

- Noether: `Noether_P08_Targeted_Source_Audit_WebDrop_20260613.zip`, 41.7576 MB, SHA256 `7BD3E884E7FEAE867656D9BC2F7D06E1642277073548968FDE5ED2DA21CE8ED1`.
- Contents: Paper 08 targeted source-audit drop for `Ueber ganze rationale Darstellung der Invarianten eines Systems von beliebig vielen Grundformen`, printed pp.93-102. The local working TeX was patched for three source-confirmed math-level defects: `(zy)x` replaces `(xy)x` in the binary substitution formula; the first operator argument is `\partial/\partial\lambda`; and the Omega-process display now includes the missing middle equality. The package still leaves the broader Paper 08 source-style symbolic footnote apparatus open.

Next action when Zenodo API credentials are available: create a new Noether Zenodo version, upload this ZIP together with the other pending Noether source-audit packages if still pending, publish, then update record IDs, metadata JSON, `manifests/public-file-catalog.csv`, generated record pages, and status docs. Do not treat this as whole-corpus or complete Paper 08 closure.

## 2026-06-13: Noether RA43 Paper 06 pp.161-p166

Manifest: [20260613_noether_ra43_p06_p161_166.json](../manifests/pending-zenodo-uploads/20260613_noether_ra43_p06_p161_166.json)

- Noether: `N_SYM_RA43_P06_p161_166_20260613.zip`, 9.6944 MB, SHA256 `C7AAD79F1F42644ED490F83C549277ABB42E865470734B7BED0964D520BFEBAA`.
- Contents: source-critical German audit tranche for Paper 06, `Koerper und Systeme rationaler Funktionen`, Math. Ann. 76 source scan, printed pp.161-166. Package notes say this continues the page-by-page workflow after Papers 01, 02, 04, and 05 and records compact-argument notation plus left-numbered display heuristics.

Next action when Zenodo API credentials are available: create a new Noether Zenodo version, upload this ZIP together with the other pending Noether source-audit packages if still pending, publish, then update record IDs, metadata JSON, `manifests/public-file-catalog.csv`, generated record pages, and status docs. Do not treat this as whole-corpus or complete Paper 06 closure.

## 2026-06-13: Noether RA44 Paper 06 pp.167-p172

Manifest: [20260613_noether_ra44_p06_p167_172.json](../manifests/pending-zenodo-uploads/20260613_noether_ra44_p06_p167_172.json)

- Noether: `N_SYM_RA44_P06_p167_172_20260613.zip`, 7.6813 MB, SHA256 `8154D098DD36C6D0B5302F52C839B4B392138306656C8B590CDA9A3AA65A93F9`.
- Contents: source-critical German audit tranche for Paper 06, `Koerper und Systeme rationaler Funktionen`, Math. Ann. 76 source scan, printed pp.167-172. Package notes report corrected `k(x)` continuation in the §2 Hilfssatz, restored compact dotted argument notation, restored source-style left-numbered displays in the §§3-5 range, converted checked-range footnote markers to source-style page-local symbols, and rebuilt cumulative German TeX/PDF. Workspace status reports Paper 06 pp.161-172 checked, with p.173 onward, full Paper 06 symbolic footnote conversion, and non-German propagation still open.

Next action when Zenodo API credentials are available: create a new Noether Zenodo version, upload this ZIP together with the other pending Noether source-audit packages if still pending, publish, then update record IDs, metadata JSON, `manifests/public-file-catalog.csv`, generated record pages, and status docs. Do not treat this as whole-corpus or complete Paper 06 closure.

## 2026-06-13: Gordan `Vorlesungen ueber Invariantentheorie` Bd.1 p010-p028

Manifest: [20260613_gordan_vb1_02_p010_028.json](../manifests/pending-zenodo-uploads/20260613_gordan_vb1_02_p010_028.json)

- Gordan: `Gordan_VB1_02_p010_028_DE_EN_20260613.zip`, 46.5065 MB, SHA256 `2FA5FEBE71A6550622E01483713EE2C7FC9740073F7CB6525173F8F5B06A75DD`.
- Contents: German transcription and English translation continuation for Paul Gordan, `Vorlesungen ueber Invariantentheorie`, Bd. 1, source TIFF witnesses 0010-0028. The package covers the Inhaltsverzeichniss pages VIII-XI, blank scan-only source page 0014/label XII, and printed pages 1-14 through §1 paragraphs 1-12. It includes current/cumulative German/English TeX/PDF, GDZ 600ppi source witnesses, render checks, ledgers, and no reported red flags.

Next action when Zenodo API credentials are available: create a new Gordan/Clebsch-Gordan Zenodo version, upload this ZIP together with the other pending Gordan packages if still pending, publish, then update record IDs, metadata JSON, `manifests/public-file-catalog.csv`, generated record pages, and status docs.

## 2026-06-13: Noether Paper 19 tail source-audit web drop

Manifest: [20260613_noether_p19_tail_audit_webdrop.json](../manifests/pending-zenodo-uploads/20260613_noether_p19_tail_audit_webdrop.json)

- Noether: `Noether_P19_Tail_Source_Audit_WebDrop_20260613.zip`, 5.2554 MB, SHA256 `46593900222F7DA23A114753B7F2DBF624FEE4F8412D90EB60C655BC00C1C4C2`.
- Contents: Paper 19 tail source-audit drop for `Idealtheorie in Ringbereichen`, printed pp.58-66, focusing on §§10-12 and the final element-divisor proof. The package reports one high-severity source-confirmed mathematical index error in the element-divisor proof: the source uses C/D exponent systems `s_1...s_\lambda` and `t_1...t_\mu`, and the continuation inequality `r_\nu=s_1\le s_2\le\cdots\le s_\lambda\le r_\nu`, not the current `s_\nu...s_i` / `t_\nu...t_i` shift. It also reports one low-severity source-order cleanup for the congruence pair after `Wegen`. Both fixes were applied locally and a patched cumulative TeX copy is included under `applied_fixed_tex/`. Checked no-fix anchors for pp.59-66 are included.

Next action when Zenodo API credentials are available: create a new Noether Zenodo version, upload this ZIP together with the other pending Noether source-audit packages if still pending, publish, then update record IDs, metadata JSON, `manifests/public-file-catalog.csv`, generated record pages, and status docs. Do not treat this as whole-corpus or complete Paper 19 closure.

## 2026-06-13: Noether Paper 20 Lean/source-audit web drop

Manifest: [20260613_noether_p20_lean_audit_webdrop.json](../manifests/pending-zenodo-uploads/20260613_noether_p20_lean_audit_webdrop.json)

- Noether: `Noether_P20_Lean_Audit_WebDrop_20260613.zip`, 1.752 MB, SHA256 `4562CEAC5C2BAEAA110857D7DF27B41A2AA9BE93ED7632A1E76E83409584158C`.
- Contents: Paper 20 Lean/source-audit drop for `Ein algebraisches Kriterium für absolute Irreduzibilität`, printed pp.26-33. The audit requests one source-confirmed formula (13) correction: the two factor-sum indices should be `\kappa,\lambda`, not `\mu,\nu`; the following prose products `\varrho_\mu\sigma_\nu` remain unchanged. The local working TeX branch was patched and the corrected cumulative TeX copy is included under `applied_fixed_tex/`. The audit also records that Paper 20 uses ordinary numbered footnotes, so the Paper 06-Paper 08 symbolic-footnote correction pattern should not be applied to Paper 20.

Next action when Zenodo API credentials are available: create a new Noether Zenodo version, upload this ZIP together with the other pending Noether source-audit packages if still pending, publish, then update record IDs, metadata JSON, `manifests/public-file-catalog.csv`, generated record pages, and status docs. Do not treat this as whole-corpus or complete Paper 20 closure.

## 2026-06-13: Kneser `Lehrbuch der Variationsrechnung` p0234-p0248

Manifest: [20260613_kneser_lvr_p0234_0248.json](../manifests/pending-zenodo-uploads/20260613_kneser_lvr_p0234_0248.json)

- Kneser: `Kneser_LVR_p0234_0248_DE_EN_20260613.zip`, 107.952 MB, SHA256 `5E27483A484886DB5BD80268A497A0FE8E333B024D4929DD5D391488E035F037`.
- Contents: German/English source-visible working continuation for Adolf Kneser's `Lehrbuch der Variationsrechnung`, current slice source p0234 lower-p0248, sections 53-55, completing the Sixth Section. The package uses the higher-quality archive.org source witness, includes current-slice and cumulative German/English TeX/PDF through p0248, HQ current/cumulative source scans, render checks, ledgers, and mathematical source checks for formulas (37)-(50). The worklist reports 248/336 source pages done, 73.8%, with next start at p0249, Seventh Section, section 56.

Next action when Zenodo API credentials are available: create a new additional-author-cluster Zenodo version, upload this ZIP together with other pending mixed-author packages if still pending, publish, then update record IDs, metadata JSON, `manifests/public-file-catalog.csv`, generated record pages, and status docs. Consider a dedicated Kneser author record if the sequence keeps growing.

## 2026-06-13: Noether Paper 07 targeted source-audit web drop

Manifest: [20260613_noether_p07_targeted_audit_webdrop.json](../manifests/pending-zenodo-uploads/20260613_noether_p07_targeted_audit_webdrop.json)

- Noether: `Noether_P07_Targeted_Source_Audit_WebDrop_20260613.zip`, 28.4518 MB, SHA256 `F6B2196E902DE0BC839953928B8CF80E9C04AC061A38791E72D58C9B64F148CC`.
- Contents: targeted Paper 07 source-audit / witness drop for `Der Endlichkeitssatz der Invarianten endlicher Gruppen`, printed pp.89-92. The package reports content largely present at checked formula anchors, but flags the same footnote-apparatus issue as Paper 06: the source uses page-local symbolic notes `*)` and `**)`, while the current cumulative TeX uses ordinary numbered footnotes for all six Paper 07 notes. It also records checked no-fix anchors for the Galois resolvent display and the Weber II, section 58 derivative correction formula.

Next action when Zenodo API credentials are available: create a new Noether Zenodo version, upload this ZIP together with earlier pending Noether source-audit packages if still pending, publish, then update record IDs, metadata JSON, `manifests/public-file-catalog.csv`, generated record pages, and status docs. Do not treat this as whole-corpus or complete Paper 07 closure.

## 2026-06-13: Bianchi A2 p0135 compact core same-name collision

Manifest: [20260613_bianchi_a2_p0135_edge_core_collision.json](../manifests/pending-zenodo-uploads/20260613_bianchi_a2_p0135_edge_core_collision.json)

- Bianchi: `Bianchi_A2_core_p0001_0135_IT_EN_20260613_EDGE_5MB_NAME_COLLISION.zip`, 5.7126 MB, SHA256 `2EBA2F62F138EAE9898CBD5A1116895B9820348CB3B0256D4EF6705207C45E01`.
- Contents: compact/core A2 Italian-English working package through source p0135, containing current/cumulative TeX/PDF, ledgers, formula/equation indexes, render checks, logs, and package manifest. The package README says source witness PDFs/images are excluded and should be taken from the full package or direct source witness files.
- Collision note: the original Edge filename was `Bianchi_A2_core_p0001_0135_IT_EN_20260613.zip`, which matches an already cataloged Zenodo file but has a different size/hash. The routed local copy is intentionally renamed and must not silently replace the published catalog entry until a new Zenodo version is actually published.

Next action when Zenodo API credentials are available: decide whether this compact re-export should supplement or replace the already published p0135 package, publish it under a disambiguated filename if appropriate, then update record IDs, metadata JSON, `manifests/public-file-catalog.csv`, generated record pages, and status docs.

## 2026-06-13: Noether Paper 06 targeted source-audit web drop

Manifest: [20260613_noether_p06_targeted_audit_webdrop.json](../manifests/pending-zenodo-uploads/20260613_noether_p06_targeted_audit_webdrop.json)

- Noether: `Noether_P06_Targeted_Source_Audit_WebDrop_20260613.zip`, 23.673 MB, SHA256 `84B466C387424552DF485A2045CBBE9B8DB267751F35363205B74B8003E6DCBF`.
- Contents: targeted Paper 06 source-audit / witness drop for `Körper und Systeme rationaler Funktionen`, source `Math. Ann. 76 (1915), S. 161-196`. It includes source PDF, selected 650 dpi source page renders, labelled witness crops, OCR locator text, and audit CSV/Markdown ledgers. It is explicitly not a complete Paper 06 certification. The drop reports a systematic source-fidelity issue: source pages use page-local symbolic footnote markers such as `*)` and `**)`, while current TeX uses ordinary numbered footnotes throughout the Paper 06 block. It also records checked no-fix rows for the p.196 `Umstand` phrase and tail formulas.

Next action when Zenodo API credentials are available: create a new Noether Zenodo version, upload this ZIP together with the other pending Noether source-audit packages if still pending, publish, then update record IDs, metadata JSON, `manifests/public-file-catalog.csv`, generated record pages, and status docs. Do not treat this as whole-corpus or complete Paper 06 closure.

## 2026-06-13: Noether RA42 Paper 05 source-audit web drop

Manifest: [20260613_noether_ra42_p05_webdrop.json](../manifests/pending-zenodo-uploads/20260613_noether_ra42_p05_webdrop.json)

- Noether: `Noether_P05_RA42_Source_Audit_WebDrop_20260613.zip`, 21.3821 MB, SHA256 `9B8C126FDB657089623E85E1A5B80181319ADBC0381BD05D16792A130DC3F98F`.
- Contents: Paper 05 source-audit / witness drop for `Rationale Funktionenkörper`, source pp.316-319. It contains the newer standalone RA42 PDF copy, source PDF copy, 650 dpi source page renders, 220 dpi RA42 render witnesses, labelled witness crops, OCR/PDF text locators, and audit CSV/Markdown ledgers. The drop reports RA42 standalone Paper 05 as source-clean at checked page-level anchors and flags one source-confirmed RA41 cumulative integration defect: the source-visible title footnote `Vortrag, gehalten auf der Naturforscherversammlung Wien 1913.` is missing in RA41 cumulative but restored in RA42.

Next action when Zenodo API credentials are available: create a new Noether Zenodo version, upload this ZIP together with the already pending RA37/RA40/RA41 ZIPs and source-audit support set if still pending, publish, then update record IDs, metadata JSON, `manifests/public-file-catalog.csv`, generated record pages, and status docs. Do not treat this as whole-corpus closure.

## 2026-06-13: Weber Batch136 recursive gap audit

Manifest: [20260613_weber_batch136.json](../manifests/pending-zenodo-uploads/20260613_weber_batch136.json)

- Weber: `Weber_Cumulative_ThreeVolumes_Batch136_RecursiveGapAudit_Vol1_Sections56_63_64_68_70_73_78_89_100_113_20260613.zip`, 77.9325 MB, SHA256 `013DE46E707D32366A018A28F0A29BE23488F1E4D2CF07477C4DCEE898BFE5FF`.
- Contents: recursive gap-audit / scan-reviewed no-change closure packet for Volume I sections 56, 63, 64, 68, 70, 73, 78, 89, 100, and 113. Package status reports the active 112-row ledger at 101 closed / 11 open, Tier-3 closed 11/11, with direct audited slices and source scans supplied for independent checking. Cumulative Volume I/II/III TeX/PDF is re-included unchanged.

Next action when Zenodo API credentials are available: create a new Weber Zenodo version, upload this ZIP together with earlier pending Weber Batch134 if still wanted, publish, then update record IDs, metadata JSON, `manifests/public-file-catalog.csv`, generated record pages, and status docs.

## 2026-06-13: SGA repair030

Manifest: [20260613_sga_repair030.json](../manifests/pending-zenodo-uploads/20260613_sga_repair030.json)

- SGA: `sga5_sga6_repair030_cumulative_20260613.zip`, 4.0404 MB, SHA256 `D41EEF7D04AD1AA450EC2730598DC03102E9215E794FFC819394818E073EF9A1`.
- Contents: compact SGA5/SGA6 cumulative French-output refresh containing SGA5/SGA6 cumulative French TeX/PDF only. README explicitly says it contains no source-index-expanded audit PDFs. A duplicate copy was found in the Noether Multilingual folder with the same SHA256; the SGA continuation copy is the canonical route.

Next action when Zenodo API credentials are available: create a new SGA Zenodo version, upload this ZIP together with earlier pending repair029 if still wanted, publish, then update record IDs, metadata JSON, `manifests/public-file-catalog.csv`, generated record pages, and status docs.

## 2026-06-13: Noether RA41 Paper 04 closure

Manifest: [20260613_noether_ra41.json](../manifests/pending-zenodo-uploads/20260613_noether_ra41.json)

- Noether: `N_SYM_RA41_P04_complete_20260613.zip`, 12.9468 MB, SHA256 `78D5ADAFC2C1D6CEE084DCA6ABB9A0E16438F7FA187EF93BD55E3CC441948CE3`.
- Contents: source-critical German Paper 04 closure package at the current source-symbol standard. Package status reports Paper 04 source pages corresponding to printed pp.118-154 opened/rendered and checked across RA36-RA41; source PDF tail p.155 belongs to the next article and is excluded. The package includes cumulative German TeX/PDF, standalone Paper 04 German critical TeX/PDF, source PNGs p146-p154 for this tranche, render checks, logs, source-page/display/symbol ledgers, and a page-check dossier. This does not certify the whole Noether corpus: the package reports 3/43 German source-symbol closed papers, Papers 01, 02, and 04.

Next action when Zenodo API credentials are available: create a new Noether Zenodo version, upload this ZIP together with the already pending RA37/RA40 ZIPs and source-audit support set if still pending, publish, then update record IDs, metadata JSON, `manifests/public-file-catalog.csv`, generated record pages, and status docs.

## 2026-06-13: Noether German source-audit support core and companions

Manifest: [20260613_noether_german_source_audit_support.json](../manifests/pending-zenodo-uploads/20260613_noether_german_source_audit_support.json)

- Noether: `Noether_German_Source_Canonical_Audit_CORE_20260613.zip`, 469.33 MB, SHA256 `EA233B32EB56961231803A396F94FE799E3B50332F8E5541EF32D7F42766F6BF`.
- Noether: `Noether_German_Source_HighDPI_Witness_Companion_20260613.zip`, 409.1823 MB, SHA256 `4AD3D2F5A36E4B5415463CCA4643E8E9DA7D44EE0C1451E936032F5244033B7A`.
- Noether: `Noether_German_Source_Auxiliary_OCR_Locator_Companion_20260613.zip`, 31.2363 MB, SHA256 `E62E90C315549EA1470719B673E37299F03EC2F7703AC11A50D1C1C677D1E20A`.
- Contents: source-critical German audit support package and companions. The core package collects current `N_SYM_RA*.zip` packages, compact source-original handoff files, normalized source-audit/error ledgers, high-DPI visual follow-up rows for selected Paper 02 `KH^3u` candidates, one source-confirmed Paper 02 prose-subscript fix request, and checksums. The high-DPI companion contains 650/1000 dpi visual witnesses for Papers 02, 08, 17, and 19. The OCR/Markdown companion is explicitly locator-only and non-authoritative.

Next action when Zenodo API credentials are available: create a new Noether Zenodo version, upload these three ZIPs together with the already pending RA37/RA40 ZIPs if still pending, publish, then update record IDs, metadata JSON, `manifests/public-file-catalog.csv`, generated record pages, and status docs.

## 2026-06-13: Frobenius RA05 recursive auditfix

Manifest: [20260613_frobenius_ra05.json](../manifests/pending-zenodo-uploads/20260613_frobenius_ra05.json)

- Frobenius: `Frobenius_all_GE_EN_cum_scans_RA05_20260613.zip`, 163.9990 MB, SHA256 `497956E905347D2DFB86E7D235499D60BAD75624675EAA3ABF3AA043DFECE8A9`.
- Contents: recursive German/English working-auditfix package for selected group-character items 053, 054, 056, 057, 058, 059, 060, 061, 070, and 071. Package notes report English item 070 formula-punctuation fixes, directly compilable all-author cumulative TeX/PDF replacing source-archive concatenations, verified ZIP extraction, 221/221 aid source page images present, zero German/English structural flags, zero `\fnum` skeleton mismatches after correction, and repaired cumulative German/English PDFs of 173/171 pages plus 241 cumulative source-scan pages.

Next action when Zenodo API credentials are available: create a new Frobenius Zenodo version, upload this ZIP, publish, then update record IDs, metadata JSON, `manifests/public-file-catalog.csv`, generated record pages, and status docs.

## 2026-06-13: Noether RA40 Paper 04 pp.140-p145

Manifest: [20260613_noether_ra40.json](../manifests/pending-zenodo-uploads/20260613_noether_ra40.json)

- Noether: `N_SYM_RA40_P04_p140_145_20260613.zip`, 16.1672 MB, SHA256 `C9E10E182D0AA6395546586F4457DEACA50D982FA4F683491136900E1788DEE4`.
- Contents: Paper 04 source-critical page-level German audit package for printed/source pp.140-145. Package notes report Paper 04 progress at 28/38 source pages checked, printed pp.118-145 checked, and six display/symbol corrections in this tranche, including source-style paired summation bounds on p140, formula (45)/(46) condition repairs, p143 phi-prime and prime-on-p repairs, and p144 formula (57) corrected from `\sim\Delta` to `=\Delta`.

Next action when Zenodo API credentials are available: create a new Noether Zenodo version, upload this ZIP together with the already pending RA37 ZIP if still pending, publish, then update record IDs, metadata JSON, `manifests/public-file-catalog.csv`, generated record pages, and status docs.

## 2026-06-13: Gordan/Clebsch-Gordan `Abelsche` FinalAuditFix02

Manifest: [20260613_gordan_abelsche_finalauditfix02.json](../manifests/pending-zenodo-uploads/20260613_gordan_abelsche_finalauditfix02.json)

- Gordan / Clebsch-Gordan: `Gordan_Abelsche_FinalAuditFix02_DE_EN_20260613.zip`, 45.8149 MB, SHA256 `DA48DEA62A420AC5078605B752817692C30F21DD129B0694EAC9BEDC33F54C4A`.
- Contents: German/English source-witnessed auditfix package for the final `Theorie der Abelschen Functionen` tranche, with current and cumulative TeX/PDF through source p355, source witnesses through p362, crops, render checks, ledgers, and a FIX02 notation correction from `n_k^{(h)}` to source-visible `w_k^{(h)}` in §91's composed-period family.

Next action when Zenodo API credentials are available: create a new Gordan/Clebsch-Gordan Zenodo version, upload this ZIP together with the already pending `De linea` ZIP if still pending, publish, then update record IDs, metadata JSON, `manifests/public-file-catalog.csv`, generated record pages, and status docs.

## 2026-06-13: Gordan `Vorlesungen ueber Invariantentheorie` Bd. 1 p001-p009

Manifest: [20260613_gordan_vb1_01_p001_009.json](../manifests/pending-zenodo-uploads/20260613_gordan_vb1_01_p001_009.json)

- Gordan: `Gordan_VB1_01_p001_009_DE_EN_20260613.zip`, 32.2733 MB, SHA256 `F3A9950D13C8447353C18C406467ED12F40AD6CD398BF6A5D18A43F70024ECF7`.
- Contents: German/English source-witnessed working start for `Vorlesungen ueber Invariantentheorie`, Bd. 1, `Determinanten`, source witnesses 0001-0009. Canonical output covers the clean title page, dedication to Charles Hermite, and full `Vorwort`; duplicate/marginal title witness, library stamp, and blank reverse pages are retained as scan-only witnesses. Package includes 600ppi GDZ/SUB Goettingen TIFF witnesses, source maps, current and cumulative German/English TeX/PDF, render checks, prior Abelsche audit context, and a noncanonical OCR scaffold.

Next action when Zenodo API credentials are available: create a new Gordan/Clebsch-Gordan Zenodo version, upload this ZIP together with the other pending Gordan packages if still pending, publish, then update record IDs, metadata JSON, `manifests/public-file-catalog.csv`, generated record pages, and status docs.

## 2026-06-13: Gordan `De linea geodetica` p025-p047

Manifest: [20260613_gordan_de_linea_p025_047.json](../manifests/pending-zenodo-uploads/20260613_gordan_de_linea_p025_047.json)

- Gordan / Clebsch-Gordan: `Gordan_de_linea_p025_047_final_LA_EN_scans_20260613.zip`, 26.5073 MB, SHA256 `13F6113993B07FE45CACC371BC85EF626C6262A054AF007D534335D819F68AF4`.
- Contents: Latin/English working package for Gordan's `De linea geodetica`, final tranche p025-p047 plus cumulative Latin/English TeX/PDF through p001-p047, source scans, ledgers, and render checks.

Next action when Zenodo API credentials are available: create a new Gordan/Clebsch-Gordan Zenodo version, upload this ZIP, publish, then update record IDs, metadata JSON, `manifests/public-file-catalog.csv`, generated record pages, and status docs.

## 2026-06-13: SGA repair029

Manifest: [20260613_sga_repair029.json](../manifests/pending-zenodo-uploads/20260613_sga_repair029.json)

- SGA: `sga5_sga6_repair029_cumulative_20260613.zip`, 4.0436 MB, SHA256 `6A30D66204A2D6A7D79528DC1A43030ECDFC547515AF843498E0F407177C8B62`.
- Contents: compact cumulative French-output refresh for SGA5 and SGA6, with `sga5_fr.{tex,pdf}`, `sga6_fr.{tex,pdf}`, and checksum CSV.

Next action when Zenodo API credentials are available: create a new SGA Zenodo version, upload this ZIP, publish, then update record IDs, metadata JSON, `manifests/public-file-catalog.csv`, generated record pages, and status docs.

## 2026-06-13: Noether RA37 and Weber Batch134

Manifest: [20260613_noether_ra37_weber_batch134.json](../manifests/pending-zenodo-uploads/20260613_noether_ra37_weber_batch134.json)

- Noether: `N_SYM_RA37_P04_p122_127_20260613.zip`, 10.5395 MB, SHA256 `BF60D4B5D29744AD2E702F69D29AB13FC386B1DB1243022A68839D3C73A26AAB`.
- Weber: `Weber_Cumulative_ThreeVolumes_Batch134_RecursiveGapAudit_Vol1_Sections12_14_16_20_22_20260612.zip`, 234.1134 MB, SHA256 `8BDFF1D92B2B9D6B70C5F302ADA82A61DD617A8D23E44C70EA4DF5E7E2D77526`.

Next action when Zenodo API credentials are available: create new Zenodo versions for the Noether and Weber records, upload these ZIPs, publish, then update record IDs, metadata JSON, `manifests/public-file-catalog.csv`, generated record pages, and status docs.

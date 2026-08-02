# SGA 7 II English production logbook

## 2026-08-01 — French canon/corrected-reading distinction

- Adopted Floris's EGA French-source instruction as the analogous SGA rule in
  `FRENCH_CANON_AND_CORRECTED_READING_POLICY_20260801.md`.
- The French canonical TeX must reproduce the printed authority faithfully,
  correcting transcription deviations but retaining genuine printed typos.
  Printed defects are catalogued outside that body.
- The existing corrected French workpass remains a separate editorial reading
  layer synchronized with the English. Every English source intervention is a
  mandatory scan-recheck point. Individual French verification readers remain
  valid archival controls; no omnibus public French PDF is implied.
- Rechecked the full EGA analogue supplied at
  `<REDACTED_USER_HOME>\<REDACTED_CODEX_STATE>\attachments\<REDACTED_TASK_ID>\pasted-text.txt`.
  Its exact SGA consequence is archival diplomatic French TeX plus bounded
  verification identities, while corrected readings remain explicitly separate.

## Durable post-SGA7 queue

- After SGA 7 II closes, this lane owns FAC, then GAGA.
- After those current author-corpus items close, this lane owns internal-reference
  cleanup for the standalone SGA readers and one no-overwrite cumulative SGA
  1–7.2 reader with working cross-volume links. That pass will coordinate exact
  inputs before mutation, preserve reviewed/public layers, no-op exact prior
  work, and carry complete candidate/edge/residual ledgers, provenance/rights
  caveats, build/render checks, privacy-clean packaging, and no duplicate concept
  or archive transport. The separate EGA task owns the analogous EGA 0–IV reader;
  there is no EGA overlap here.

## 2026-08-01 — Exposé XVIII §6.1–§6.4 closed

- Completed the English through Proposition 6.2, Theorem 6.3, Corollary 6.4,
  and Lemma 6.4.2; exact next source cursor is frozen French line 2586, §6.5,
  scan index 329 / folio 322.
- Added `source/components/131_expose_XVIII_proposition_6_2_through_corollary_6_4.tex`,
  4,633 B, SHA-256
  `981CCD2ECC31E299A54CB93A7353AB23B1FC974C6A301ED5A72B7444A5038C45`.
- Lead source comparison used Number12 physical pages 327–330 at 1100 dpi.
  The page-image SHA-256 values are, in order,
  `7A7E1A19534373C79AB6A766671B3916956F93B5E91862F35BBF96CBAB02DEDD`,
  `14A5CF20938FBA605D2452A7966A59123B2BB37F38AF8940070D2567FA3C73C1`,
  `A894050C04DBF33CF87DBB7233332C22AAE646874094A0BAB2FC0F5DE6814514`,
  and `30DEE9668FDAFD069FA3FB17DE2F8EC327F766F7C4F93B4D362270BB2D9AE41C`.
- English three-pass build: 191 A4 pages, 1,031,510 B, PDF SHA-256
  `440F1CCF3B5FC277E096239929F69CE70625DA19729B88C3A230B9B63304A694`;
  final log SHA-256
  `9BDCDD7A18A68B981F2EAA04F02444D0FAC12BA248A83955079CFD6ECC4AA72D`;
  pass 2 and pass 3 are byte-identical, SHA-256
  `7F6DBD408434C38C60D47F852D4F3FF42529068B001386984317BA33774BB149`;
  critical diagnostics 0.
- Corrected-French verification build: 201 A4 pages, 1,379,477 B, PDF
  SHA-256
  `48F4616C7F6F0F48AADDF58DDD21B6DBE5F50EE572A3B549142D8E7CC11196C6`;
  final log SHA-256
  `F681EEAE7484B53317FEC67AA6AF394D0080D53B4F6202F5D8F3CEDAD249BBDA`;
  pass 2 and pass 3 are byte-identical, SHA-256
  `F79408D46C67339392212A6B52CF5D518583F6BC775B5329B0959A8067BCD309`.
  Only two inherited, unrelated overfull warnings remain.
- Lead render review PASS: English pages 190–191 at 600 dpi and the
  corrected-French corresponding pages 163–164 at 600 dpi. The preceding r2
  §6.1 render also confirms that the vertical $i_{\bar\eta*}$ label is now on
  the authority's right-hand side.
- One malformed build invocation created literal `source/$out` directories.
  They are non-adjudicative build contamination and excluded from every source
  identity, manifest, and future package; the controlling PDFs are only in the
  named `build` and `french_source_corrected_workpass/build_check_*` roots.

## 2026-08-01 — root and first English block

- Opened the no-overwrite SGA 7 II English successor.
- Preserved the coherent Claude French package through scan index 406 under
  authority_snapshot/.
- Confirmed that the mutable Claude workspace has no source body beyond index 406.
- Located the older Kimi pages 351–444 TeX, compared its overlap with the coherent
  Claude source, and rejected it as a source/translation substrate because it is a
  condensed reconstruction with materially altered formulae.
- Translated Exposé X from scan indices 8–12, through Corollary 1.9.
- Inspected Number12 scan index 12 at 1100 dpi. The scan clearly contains commas in
  the pairs (D_i,D_j); the English formula restores the comma omitted in one line of
  the frozen French TeX. Evidence:
  qa/source_idx12_1100dpi/Number12_idx12_1100dpi.png, SHA-256
  7B3C45102C9912C4D46EDA786035F8DEAA748FAD08C0140B05304BBCACE1F2A5.
- Next translation cursor: scan index 13 / folio 6 / §1.10.
- Follow-on queue retained: FAC, then GAGA, after both SGA 7 tomes close.

## 2026-08-01 — Exposé X §1 completed

- Translated scan indices 13–17 and the opening portion of index 18, completing
  Exposé X §1 through the exercise after Lemma 1.16.
- Preserved both source diagrams natively in tikzcd; no raster figure was
  introduced.
- Personally inspected authority indices 13, 14, and 18 at 1100 dpi. The English
  corrects three unambiguous printed-source slips while preserving the intended
  mathematics:
  - printed index 13 says the relative dualizing sheaf $\omega_{X/S}$ is “on
    $S$”; the English places it on $X$;
  - printed index 14 writes $\deg_D(Rg^!\underline O_D)$ once, although (1.10.2)
    and the calculation require $Rg^!\underline O_S$;
  - printed index 18 repeats $n_i$ under the sum in equation (*); the English
    restores $n_j$, giving
    $n_i=\frac12\sum_{j\ne i}n_j(D_i,D_j)$.
- Source image identities:
  - index 13: SHA-256
    61AF86AC008E91EE1EF54EE541F1F59C8BBCCC1906A2FB376AF641825CF374BB;
  - index 14: SHA-256
    051BFA90C4F96D3FA7E137FCA72B6E50C02B20235E4E15ED425805A2A2136F3A;
  - index 18: SHA-256
    49E85CC99B6D52EA10C02CE48F777ED6BE1CFAED46A446743A5FEA48170F328F.
- Added component
  source/components/002_expose_X_1_10_through_section_1.tex, 10,404 B,
  SHA-256 66983C2CA5839A97904FD5D259A32E525DEE20A838BEE09524E30D26E89B8E91.
- Three-pass cumulative build PASS: 6 A4 pages; PDF SHA-256
  2BDDFFCDFFD6C9AFF65EE4C415161351DC5D0D1CD21EFD7672D730D381CD14B2;
  final log SHA-256
  80DDAF88ACB990055DB14C986D0540D963E8AEA3E6DB76C0B126E2A20A3AFA7C;
  no TeX diagnostics. Pages 3–6 were personally inspected from 600-dpi renders.
- Exact next cursor: scan index 18 / folio 11, §2 “Italian intersections.”

## 2026-08-01 — Exposé X advanced through Theorem 2.11

- Translated the remainder of scan index 18 and indices 19–28, completing the
  opening of §2, Theorem 2.9 and its proof, and Theorem 2.11 and its proof.
- Added components:
  - source/components/003_expose_X_section_2_opening_through_2_9_statement.tex,
    10,702 B, SHA-256
    CE79BD650F30D37D9EA9D59F907BD9A77ABA0B2A03763114216EEE5172CFD5EF;
  - source/components/004_expose_X_theorem_2_9_proof_through_2_11.tex,
    6,727 B, SHA-256
    BD09830203F7122D7CFD8AA759B4B49297E0C16B7C15A905158603485036C9E1.
- Personally inspected authority indices 25–28 at 1100 dpi. Exact source-image
  hashes are, respectively:
  2BB0E857CF2D13A1F699234097C91A3EC5DA02E9436A86CA1A1F37C0FB9DE129,
  54298B506919BBB2006E3960318BCCD40FF0BFF3FE6FF468E1EB3CAD6A990694,
  28506F5E1E4232B8950A2206875E5EAEC15D5F911DDA2A5B8FA050B589EAB165,
  and D5D5BD97DE5376FEFC7E634209D5A856754B5E94B52B7C98895D6EE81551632D.
- The English makes the following mathematically forced source repairs:
  - (2.9.2) uses $\mu_s(D)s^*$, not the printed $\mu_s(S)s^*$;
  - (2.11.3) reads $(s^*,D')$, as required by the immediately preceding
    sentence, not the printed $(s^*,D)$;
  - all pullback and direct-image maps in (2.11.4)–(2.11.9) use the declared
    blow-up map $p$, rather than the printed alternation between $p$ and $f$;
  - the short exact sequence following (2.11.8) is ordered
    $0\to p_*\underline O_E\to p_*\underline O_{D'\cap E}
    \to p_*\underline O_{D'}/\underline O_D\to0$;
  - accordingly, (2.11.9) subtracts
    $\frac12\mu_s(D)(\mu_s(D)+1)$ from $\mu_s(D)^2$, yielding the printed
    intended result $\frac12\mu_s(D)(\mu_s(D)-1)$. The printed first line has
    the subtraction reversed and is algebraically incompatible with its own
    second line.
- Three-pass cumulative build PASS: 11 A4 pages; PDF SHA-256
  960EF1A9A78BA2DDFD1BBCC8747B78937FE050BAF20A63D3BF7D83431A6A3BC0;
  final log SHA-256
  2FCE84EE850396A8B68B73B41893C49A7BAD56546C1DEB913B9277159869CF72;
  diagnostics zero. Pages 9–11 were personally inspected from 600-dpi renders.
- Exact next cursor: scan index 28 / folio 21, §2.12.

## 2026-08-01 — Exposé X advanced through Example 2.24

- Translated scan indices 29–36 and the remainder of index 28, completing
  §§2.12–2.24. Exact next cursor: scan index 37 / folio 30, Example 2.25.
- Added components:
  - source/components/005_expose_X_2_12_through_2_14.tex, 9,739 B,
    SHA-256 D6E02ED160AC6C7399DE3F89303BFEA2600409BDB733E32EB88ADB998A100ADF;
  - source/components/006_expose_X_2_15_through_2_24.tex, 5,820 B,
    SHA-256 598D06ABA0ECF6062C5E61B58F0506B3CC30C5F24657288BEAE3243369DAA304.
- Personally inspected authority indices 29–36 at 1100 dpi. Their source-image
  SHA-256 values, in order, are:
  8C7654998368C1302C3BB5F0CAEB1A02515C3789F6D0046120F9B843ACF0743E,
  618CB0E6B5E4D266518852DD67162751159498183BDB322900DA0AE4AA0059BA,
  2D905CD45818A97FCF2EB22A8ED0499F2EB6223B959E9C951F65F385819D63B7,
  88131ED40CECA9DCDCD6BF4852382A305BBD8388907F178CE2BA4A3095551430,
  4E76C409CB578A6C6E7225542524224AC2B721F8D3A76713CCE590A3E1159E5D,
  53BD36743FEBBD01F5E6BEB5F91BA86346881075F9AF944D485760AEB99A7246,
  766CFDCCC1547797FAAD9F7D8B9035457CE153D4872FC7A64C19217E566CB6FD,
  and 30FB5716C71495829652EA4B131BE72913FB629DD397A81D8D06756AF84527CC.
- Source-backed repairs and dispositions:
  - the printed transition in the proof of Lemma 2.14(ii) is syntactically
    garbled; the English states its mathematically explicit consequence that
    $D'$ meets $s^*$ with length one, so the bound on $T\cap s^*$ gives the
    required bound on $(D'\cup T)\cap s^*$;
  - the frozen French TeX omits a closing parenthesis in the definition of
    $S^*$ in 2.15; the scan makes the closure unambiguous and the English
    restores it;
  - the last sentence of 2.24 prints $S_2$ although the non-étale locus of
    $f:S_1\to S_2$ and the generalized curve in question lie on $S_1$; the
    English transparently uses $S_1$;
  - formula (2.18) retains the printed factor $[k(t'):k]$; it was not silently
    normalized to a different residue-field degree.
- Three-pass cumulative build PASS: 16 A4 pages; PDF SHA-256
  DE21CE70234701A2382AB83F57EDAB6D20E94231AAC6E35F3FDF9DADF4274302;
  final log SHA-256
  714E9CECC69A978B8583CAFBEAD2C489E2FF8CF07C454FB2558FEC2DCA15A701;
  diagnostics zero. Pages 12–16 were personally inspected from 600-dpi
  renders; the two cramped “for $i>0$” displays in component 005 were repaired
  before this build.

## 2026-08-01 — Exposé X Example 2.25 translated with native diagrams

- Translated Example 2.25 across scan indices 37–38. Exact next cursor:
  scan index 38 / folio 31, §2.26.
- Added source/components/007_expose_X_example_2_25.tex, 6,725 B,
  SHA-256 F1108111A4149712279FA01107DE6C48F3EB171129D71109987C340466B043E9.
- Personally inspected both authority pages at 1100 dpi:
  - index 37: qa/source_idx37_1100dpi/Number12_idx37_1100dpi.png,
    SHA-256 EEB8056CE44B7440B733A07214A54C52140A39D49D961E3F6670AE5D40FE2C92;
  - index 38: qa/source_idx38_1100dpi/Number12_idx38_1100dpi.png,
    SHA-256 E1EEAC773BC7C64428A2F09E8F02C4EDC805F25351953F9F8E3F232F06D6C7DD.
- The four elementary plane-singularity diagrams were already unambiguous at
  1100 dpi. The two dense space-curve diagrams were inspected in targeted
  5000-dpi-equivalent magnifications, not by wastefully rendering the full
  scanned page at that scale:
  - (2.25.1) crop SHA-256
    4501F398F382E96309A5119AC220463F515EFC66282E937F2EFD47C5F2FC06CF;
  - (2.25.2) crop SHA-256
    A82C47DC4AB15C685EC84109E6A8BFECC77C16EAC846EF4C0CFB05E5CDBD6154.
  The underlying PDF page is an approximately 300-dpi embedded scan, so the
  targeted enlargement is a viewing aid and does not manufacture new source
  information.
- Reconstructed all four source sketches and all six Enriques graphs as native
  TikZ. The English preserves the exact vertex multiplicities, branch geometry,
  eight-edge and twelve-edge crossing patterns in (2.25.1) and (2.25.2), label
  sides, and continuation dots. It loads no raster figure.
- Three-pass cumulative build PASS: 17 A4 pages; PDF SHA-256
  0521047A491959E2532B94A71D232F604EA814E54E339167730347CE6A45F702;
  final console SHA-256
  50CDAE30CD9073F233BA3DDF31819ED4F272100ACB2D9B67362EFF4B480DD033;
  diagnostics zero. Pages 16–17 were personally inspected from fresh 600-dpi
  renders after correcting the direction of the large grouping braces.

## 2026-08-01 — Exposé X completed

- Translated §§2.26–2.34 and the complete bibliography, closing Exposé X at
  scan index 45 / folio 38. Exact next cursor: scan index 46 / folio 39,
  Exposé XI opening.
- Added components:
  - source/components/008_expose_X_2_26_through_2_30.tex, 5,826 B,
    SHA-256 29DCBF7C6615A6FAD10E2D5F7E6312EEB049595D7476E4ADF725A00F9D0EFD2E;
  - source/components/009_expose_X_2_31_through_bibliography.tex, 5,832 B,
    SHA-256 23B0D8D91441B4AF1A9FEE323559D174E4795C4163FFD62A9A1678CEA716108F.
- Personally inspected authority indices 39–45 at 1100 dpi. Source-image
  SHA-256 values, in order, are:
  C4FD8ECA34F16CA227F3BBC029E5A78F40C51AACAEC7655BAAB3FB2764B89651,
  1547831BD60D15C6FA6BAE31C96C7C452B401230631D3457E1190538C6E33E34,
  2A470969DC09E14C141F1C69D3A3FFB3CF7493A562910760D66217C763849B14,
  9F0B7219E537D94DE788B94CF66C10B7D532FFD38995FF6CEDB4D14B4846F70E,
  A08F6FFB01243D030FFBB5C9007E8AA07233A973933A71B4DF615EF9109C01C7,
  DD7548EB40543AAEED673CE8B348A4DBDC341590158138511CD5BD6C38067AD5,
  and 26BFB52C71C0947DEBFD8C3EFAB016D021B7F1F9ED02F83D27E3F64F932CE0A5.
- Source-backed notation/typo dispositions:
  - (2.29.2) reads $\dim(E_0)=3p-3$ in English. The scan prints $\dim(E)$,
    but the generic smooth fiber under discussion lies over $E_0$, and only
    the corrected expression combines with (2.29.1) and (2.29.3) to prove
    Theorem 2.27;
  - in Lemma 2.28, the English uses $H^0$, $T_0$, and the previously declared
    point $t_2$ where the printed text has the evident slips $H^o$, $S_0$,
    and an unsubscripted $t$;
  - in the proof of Proposition 2.32, the dimension equation uses $M_0^E$,
    matching the proposition and the chosen component $E$, rather than the
    printed $M_0$.
- Three-pass cumulative build PASS: 20 A4 pages; PDF SHA-256
  6143F6DECA9A9918C12578F00A39CDFB584DE9A8CADF27416F1A997DC7F2E428;
  final console SHA-256
  1BEC06F69C659EAA649AABDEFE25B6F6D7FA215F6183E61648A84D26FF371C66;
  diagnostics zero. Pages 18–20 were personally inspected from fresh 600-dpi
  renders and pass.

## 2026-08-01 — Exposé XI completed

- Translated Exposé XI continuously from its opening through §2.10 and the
  complete bibliography, covering authority scan indices 46–68. Added
  components 010–017; their SHA-256 identities are:
  - 010 `F5ED8474DE1F230A38357EE89AB90192395A218014EF06802654624B3826A04B`;
  - 011 `C8A30E353AD7958026F9E8BA1BCA67D5D05B25758D6602227E70596CEC097053`;
  - 012 `68D9FD95930EE66829B964F566985BEBAC3F2272856C79060B08F32B02FC7E5C`;
  - 013 `ACAE0DFA5F40179014ADB78A4A848C3C6CA96BDE5BD025B54A8B279BF1FE3E11`;
  - 014 `AB28F7FCC97874BBD6F879A734242FDA795951911292058300C511FAEEBD2EB8`;
  - 015 `7BAA5F29A1057CED2B5BA2A847B4699F29744B80633B77880E4E60A219096619`;
  - 016 `94377F505A48F6A3DE389920EF085633BC15E3D4D64DAD112B66E325E1012787`;
  - 017 `F392BBB86C20B66E54621F2828397FB4E3344FA8FA32B1116550C8A531B080C2`.
- Personally read all 23 authority pages at 1100 dpi. Image hashes for indices
  46–68, in order, are:
  `5895E9CD3309CD11633C91E24574B93E204B195BC2C595953203EB30BFDEAB19`,
  `2F7BADAAA54015B1C13BB1693E9EA3546DA77A02EED2A0056C7879BD45CC8A83`,
  `AD54988213B13DCA1E97C9B0488D819B5EE4E13DF3261DA55E3277DD52ABBE9F`,
  `E118E30340A4D3091BDB2D32625C27DACF8A0309D38026C8DD25265A73956CDE`,
  `16C0024C494C7F421A927549C61740C1987DF76470C731006B9527C93FA146C3`,
  `4091DC50D448E6E96A333D2F309A6E35B80C918ECED1375C8A7EEA6BDC36955E`,
  `11970EE0EDDEDC9705BCC46516EE8507CED935EB7439AEA7CF1F8AB29673F5E6`,
  `A1F9D21D97BEC70E45E06A251439FD529922CA177304CEFB93FEB0F5E5492D94`,
  `FF04D8B5478DA6CA8D0327CBFE14CCEF469920B4D5E4C98595E3D700E4223DC3`,
  `6A5F5AC32975F5DA9999F0AA3885EC6840EC2B5BC600355BE8B4E040E5016515`,
  `A952A69FC748186B2305F18CE1A737381D85DE0205A2D13291CC685795666F7C`,
  `4A3F593DF928832EEBF786A1ADB181D2C64E7D016DF5BCB8622C92B04B527953`,
  `4F4235CAF5461B3FCD12F6B2DA521A8421A87F0A2172A88CE7370F4ABA53ADAB`,
  `8D32282308953CDCE0EA53E1774C6C428DB764232234208AC09E558913348323`,
  `3EF0FCACA2C0C058F8A4109373CF24E2AC5E3F9ECB109A644BF0C94A89742F6A`,
  `830F469353D07B825D660C89256937B191F8F1B92E0D551BDFB177498F260C76`,
  `5D5F05376480FDEB5B94D3405E8858E3524745464C32ED56D01D7D3DBCACA746`,
  `B6B1C6E14DB21F10C896BA91FFB5BD97E80E6A34EBAC10DFA3D0C0D97888427F`,
  `1E0567AF61EA9B977EA14B07C6FA6A39359F87CFE47765A751EE2B6A4DC67AF7`,
  `C3C4C1F224223B3ECE8B17787CB7E9C7F8B52D07626D111D9EA06CBED35C23EC`,
  `40472321778404F6F7D51E597E9F8E00C65E31E6D9D494FB94B80FA6D7B32D43`,
  `99AEF2B0680F5254B3256BA6A07AD10EAE888720CA9778043944E4683672D38D`,
  and `DE6B814C8E81A383BBE4B32DC9EB6D1CBC9518C409586D459910B15C76BBFCBD`.
- Source-backed correction dispositions:
  - §1.2 uses the required summation range `0≤i≤j`, not printed `a≤i≤j`;
  - Proposition 1.3 uses the natural restriction direction from the ambient
    projective space to the hyperplane, consistently replaces an undefined
    `Y` by `H`, and uses the section `s` rather than capital `S`;
  - Theorem 1.5(iii)(a) uses `Omega_{Y/S}`, and (1.5.1) uses the same natural
    restriction direction;
  - (2.2) reads `(1+yz)`, confirmed in the authority image, rather than the
    frozen transcription's `(i+yz)`;
  - the proof of Corollary 2.4 uses the internally consistent denominator
    `(1+y)^a z-(1+z)^a y`, variables `y,z`, and index interval `[1,d]`;
  - Definition 2.7 gives the Hodge bound
    `min(n,2 dim(X)-n)`. The printed page really omits the factor 2; targeted
    crop `idx65_hodge_level_target_5000eq.png` has SHA-256
    `1D083743913A87C49E2CAF9FAE1E8DA3D7B02338A4CCB0B82CC5BE1D5B8DDD7B`.
    The correction is disclosed in the English reader.
- Three-pass Exposé-XI-complete build PASS: 34 A4 pages, PDF SHA-256
  `93E0E9D3C5E86E8A0E2D1B38DB1C7ED5904C619BD0CDF1974C328FC452E64D84`;
  diagnostics zero. Current pages 31–34 were inspected at 600 dpi and pass.

## 2026-08-01 — Exposé XII opened through §1.3

- Personally inspected authority indices 69–72 at 1100 dpi. Image SHA-256
  values, in order, are
  `A31323876D366A7D6DC3FF7C9179CE23708A15852BC366D3EF2A2DE6CDF19FCE`,
  `635E40DFD85C31161681ED089260D700EBD8104E38488F80F2D2697F6A9483C9`,
  `644819379EF49B99CCB880917AD4EC3F80D060DFDA5FD3D027E5C08AC047E5F9`,
  and `A517984DB8A2BB17F76F8BE287B17B9C66548F09AFAB3E9B2B5AFFBE0C009E26`.
- Added `source/components/018_expose_XII_opening_through_1_3.tex`, 6,004 B,
  SHA-256 `29BFA623993BD3E73D74D4A216F3A1863EF77E6019577E533608DE685B9AA2FE`.
- The authority itself prints upper limit `m-1` in both ordinary-form sums;
  this would leave a two-dimensional radical. The English uses the standard
  and proof-required limit `m` and discloses the correction. It likewise
  corrects printed `f=-Q(f')e+f` to `f=-Q(f')e+f'` with an explicit note.
  The frozen transcription's `card(A)=2` is restored to the visibly printed
  and mathematically intended `char(A)=2`.
- Current three-pass cumulative build PASS: 36 A4 pages, 495,514 B, PDF
  SHA-256 `5E65D4F0DD470BB094DC7E5BB59AF09A7B161370DFED7AE1F7733296A8B0AEC0`.
  All three console logs are byte-identical, SHA-256
  `5B2961DFB97AB02D89F77EAD9983E31DB124840D23096AC8FC4D0CBC35BCA81E`,
  with diagnostics zero. Pages 35–36 were inspected at 600 dpi and pass.
- Exact next cursor: scan index 72 / folio 65,
  `authority_snapshot/source/expose_XII_body.tex` line 87, §1.4.

## 2026-08-01 — Exposé XII completed

- Translated Exposé XII continuously from §1.4 through §3.8 and the complete
  bibliography, closing the exposé at scan index 88 / folio 81. The next
  cursor is scan index 89, the Exposé XIII title/contents page; its body starts
  at scan index 90 / folio 83, `expose_XIII_body.tex` line 5.
- Added components and exact identities:
  - 019 `source/components/019_expose_XII_1_4_through_1_9.tex`, 5,703 B,
    SHA-256 `69BBC1890E9F08E19CA927DB088D3EB104A44A5109FB0444BAC2EAEDD39BE4D4`;
  - 020 `source/components/020_expose_XII_1_10_through_2_2.tex`, 3,821 B,
    SHA-256 `8265F28CBB42791345E5F000B0328CB933D9C1E9AE3FBCBBED88E34973040401`;
  - 021 `source/components/021_expose_XII_2_3_through_2_8.tex`, 7,077 B,
    SHA-256 `6BFB01F0BEAEFA81DD6B6AAD715321DC7B715DB3FAB785448BA2C9B5AD614E48`;
  - 022 `source/components/022_expose_XII_3_1_through_3_5.tex`, 6,240 B,
    SHA-256 `92EC1BF74FB2DDEF7655AE38135A55F33E066C59221DB4A1737F5E2A62ED5E1C`;
  - 023 `source/components/023_expose_XII_3_6_through_bibliography.tex`,
    6,257 B, SHA-256
    `BE8DE3963997A464B2FC6DB943E772CF4535F3A9D212FC6EC359D5228A9B1424`.
- Personally inspected authority indices 73–89 at 1100 dpi. Image SHA-256
  values, in order, are
  `17BA73BDB8CD883CA3A3C8B8260A948899B3B2C604E241A952D0E0D85F4F2BB6`,
  `4C5ABB615F1FE4F1C5A46A3C052643EBBBAFAB2ECE5BE2D9F72F05091A631DF2`,
  `223B7CED35C9B4320953ED225815C090D8665A5FCDCC3F41773836F6C3AE868B`,
  `1B5F1D4A3829007363CF86A8E78036C6916FB3A3AF38D3F29C8748573263FCD7`,
  `3354C5B5897725D03BA6A22A6AE5EDF162992F1578FD7030916C3486BBCEF006`,
  `CC9D54F81C5E71FA5A2EA795A7EEF2E7FBEEA6FFEA15A7BC40E99269FEDF611C`,
  `547028A2314A2729A868DEE071EAD1BEBFE13FA32B571CF4682D8C8038C9A5E7`,
  `7DD252C52AB78772672E67B28C6B0239ABEA492D73BDF3DBFB0490F879CF8091`,
  `548998917E756490F5B4CE5CD27105D513B05DA5C72D207B8C26B92B84A84F9C`,
  `54B9BC4EA2BA4BE996D0EE1FDCF723D7464F8FF2B57B9A32020840D290A1740E`,
  `0CB82AB40D89CD71F9B1B6C5E74767AC507091C1A64916F510C8036C41F32283`,
  `DBF1DDA4DDDD1BEEC8339350DB2226E4F89912AC7F3066C6A885387C0EAC8797`,
  `711B5C5EAC6F9747F457DE859D796E32367B4EE402E4FA0A429ED5DD4936A543`,
  `8209E0B05850BCEBA54D2B851916D4DED7E2BB5D1092E74DA0CEDA7841801AD0`,
  `F0B90B03589FD53513CA9195367D22D8D68B9E1C74D4372918D5E4C06E3B914B`,
  `8097131792C5B08CCF9517CC26A0B5EAD1CDDA320F26B40CD42AAFCF4FDB7D3D`,
  and `56E8135FD21B0CBEB1060D1CC1D1068F7FBB1A5796A7A5BC43E4B688095CF5A4`.
- Direct image/source dispositions include:
  - the contraction in §1.4 uses the standard sign `(-1)^{i-1}` and first
    basis vector `e_1`; the print visibly has `(-1)^i` and undefined `e_0`;
  - §1.6's connected-to-étale factorization and §1.8's cross-reference are
    corrected and disclosed; Lemma 1.10's native diagram was checked for
    exact label side and terminal structure;
  - §2.5 cites the Picard computation 2.3(ii), uses the consistently named
    projection `rho`, and cites the base-change statement 2.3(iv);
  - §3.1 uses `R^2 p_*` rather than the print's impossible `R^1 p_*`;
    (3.3.1), the ambient `P^{2m+1}`, and the top intersection power
    `eta^{2m}` are restored from the proof-required mathematics, with visible
    source notes;
  - §3.6 corrects printed `r=2m+1`, `3.5.3`, and the lower-row twist `(m)`
    to `n=2m+1`, `(3.6.3)`, and `(m+1)`. All three diagrams are native TikZ;
    arrows, hooks, label sides, equality bars, and closing punctuation were
    personally compared with the 1100-dpi authority pages.
- Final Exposé-XII-complete cumulative build PASS: 45 A4 pages, 583,055 B,
  PDF SHA-256 `CA1220BE5C5F0304B98E17BCF589D696165318DC2D163E38A79E25138C68C5BC`.
  Passes 2 and 3 have identical console SHA-256
  `1AB297040B9C63F54C3BA98FDDBF14B7B7A8C483FBEDC6EFDA24D68719DF7D54`;
  diagnostics are zero. Pages 39–45 were personally reviewed at 600 dpi,
  including a fresh post-repair render of all three diagram displays.

## 2026-08-01 — Exposé XIII opened through §1.1

- Added `source/components/024_expose_XIII_title_introduction_through_0_2.tex`,
  9,772 B, SHA-256
  `785B49DC2BF3946421CE7CF72BC49540F90F378ACE12DFC3E336C517585E7E03`,
  covering the title/contents, Introduction, Construction 0.1, and all of 0.2.
- Added `source/components/025_expose_XIII_section_1_opening_through_1_1.tex`,
  5,284 B, SHA-256
  `858DF51F9A01EA4460DF8C6EB110C3D5778E8D1DF71F0E9B4516EB0919EA1D30`,
  covering the opening of §1 and all of 1.1 through Reminder 1.1.3.
- Personally inspected authority scan indices 90–96 at 1100 dpi. The scan
  confirms that the functor in Reminder 1.1.3 sends `F` to `bar F`; the frozen
  TeX's vector accent is not the printed reading. The scan also controlled the
  full nested invariant/pullback formula across folios 88–89.
- The first 600-dpi English render exposed an underlined prose phrase that had
  accidentally been placed in math mode and therefore lost its word spacing.
  That TeX was corrected, rebuilt, and re-rendered; final pages 49–50 are clean.
  Their PNG SHA-256 values are
  `19E049595320A28CEAC2A865258E75F5CE69B39BEA9565D32DE83ACE459C8669`
  and `77BAE8A602AA2348EA33BF6725EE7F3A67A1EC1C14A20F1329BAE7075393C462`.
- Current three-pass cumulative build PASS: 50 A4 pages / 624,077 B, PDF
  SHA-256 `4A6DE6F46EF7D1C79931E7681180E7253F3CD5EB67A68B416232483D72F951C8`;
  pass 2 and pass 3 console SHA-256 are both
  `1734CB14CDF5996CD78AD0A7A3C896888C5DC497131A6E3DF1ADBBC675E6824D`;
  diagnostics are zero.
- Exact continuation cursor: scan index 96 / folio 89,
  `authority_snapshot/source/expose_XIII_body.tex` line 185, §1.2.
- Durable lane order remains: complete SGA 7 II, then FAC, then GAGA. Neither
  later corpus is represented here as complete merely because a Claude-era
  transcription or partial English witness exists.

## 2026-08-01 — Exposé XIII advanced through §1.3

- Added `source/components/026_expose_XIII_section_1_2_opening_through_1_2_4.tex`,
  6,318 B, SHA-256
  `2E1DDA4F48C98B4251CAB53D6E6E0D11EDF86699122C28EAB8F3656EF329820C`,
  and `027_expose_XIII_section_1_2_5_through_1_2_9.tex`, 3,578 B, SHA-256
  `B8836CFD1F34F88B3DE67B552A53B480D58B93B205D95D5B33AD02089834AFDC`.
  Together they cover §1.2.1–1.2.9 without a gap.
- Added `source/components/028_expose_XIII_section_1_3.tex`, 5,483 B,
  SHA-256
  `6CFEF02667C2222300AA057ABB8EC918A14EF1C78A6A4AC977833C2F6E722357`,
  covering §1.3.1–1.3.10 without a gap.
- Personally inspected source indices 97–104 at 1100 dpi. The five stored
  images for indices 97–101 have SHA-256 values
  `EAA183B5AD4C57E8EF0A41EA88F4206737901D5D8067D13244542AB6CA09F35B`,
  `786BF5333CAEBC52B0C4811234C7D4268F9B50020520C6BC03C0D77DCC9B19B6`,
  `A36BAEC53E3874B6F260A1D130E25D14514B61E3CC80BC83B5192B0B387F5521`,
  `D0FFA504223802F6EDD92199F4D161C91A882C5A2412025476C5267B9D24B88A`,
  and `47859859DE1EEBF61FDFF3B3752578DC133FE5F833044AD46F906C6703FDD932`.
  The images for indices 102–104 have SHA-256 values
  `48DEE996C125866347796C4A0DD29AFE229356DAEF14B3DA2C8BD0B882FB39BF`,
  `B2735ED6CDC490F534E45978538DABBEE556C30F075F8FF46256C0E9E6280DDF`,
  and `BADB141E7FA2A54B89A2BF57D3FF3B576F6A46D69711E80D80BA81A2A656EB18`.
  No detail required escalation beyond 1100 dpi.
- Source corrections made transparently: §1.2.2(c) writes the composite as
  `sp=sp∘j`; §1.3.2 uses the required base change `X×_S bar S`; and
  diagram (1.3.5.1) restores the bar omitted from the printed top-middle
  `bar X`, with an adjacent explanatory note.
- §1.2 cumulative build: 53 A4 pages / 651,012 B, PDF SHA-256
  `C7F267DE3A710F4C67603013850F33EE0922FD37CAF4CC2DE623B8CFAA9579DB`;
  pass-2/pass-3 console SHA-256
  `BE05A3CC10CEB5E0B4543DD1C224258B0CA6D13647AB0063784A601756818B6D`.
  English pages 50–53 were personally inspected at 600 dpi; their image
  SHA-256 values are
  `06110CC09B296793CF5C36C6774B7C3E6B06FF75EF0C0FE5002ADF3E67C680E9`,
  `E1CFC800CEF0865097268BD9C1BAEAD8AB7016A0CA8D6DA7ECCADAC5BEA2B725`,
  `2591399154D68D84DD485129AF835C6A5D6E92FBD8D7ECAA102704B8C829E4B3`,
  and `57235FCE088219B0DD1E9B106BEB8D8AF0B9B9D9B37421B11F9AE03DDA4EFF11`.
- §1.3 cumulative build: 55 A4 pages / 669,752 B, PDF SHA-256
  `76FA561DBB52838DD1A75C0ABC88D300B6D037ECD81B7DB39E2244C67F809460`;
  pass-2/pass-3 console SHA-256
  `FB167A8B443F3A777C90ABA995904ABD593AA3DC5BEA36376D22A97054F3807A`.
  English pages 53–55 were personally inspected at 600 dpi; image SHA-256
  values are
  `2316C9AF4889D6BD4B65BC662E8B0B2233E4A355B36BA30F4825F0D0F1E3D209`,
  `0707440C9CDE71DAB1DA43DC17C8E1A064C053324BD3B0331279CBD7F48892E1`,
  and `0EEB51FF51A92D039C5CE769346BC01F8B2E474EF2A2BCDDA0C98B758C38417C`.
  Both three-pass builds have zero diagnostics.
- Exact continuation cursor: scan index 104 / folio 97,
  `authority_snapshot/source/expose_XIII_body.tex` line 529, §1.4.

## 2026-08-01 — Exposé XIII advanced through the end of §2.1

- Added `source/components/029_expose_XIII_section_1_4.tex`, 3,572 B,
  SHA-256
  `5B48EE16A9687817E15A1240B50FCCA87267D3771F58F2B5852FCA6DAA4EBF2E`,
  covering §1.4.1–1.4.5.
- Added `source/components/030_expose_XIII_section_2_1_1_through_2_1_6.tex`,
  5,650 B, SHA-256
  `C47177E109537F2B27529FF9FEFAC4C175D530544AB72F6A7F8F0A49458D901F`,
  and `031_expose_XIII_section_2_1_7_through_2_1_8.tex`, 4,992 B,
  SHA-256
  `D159CA66C0DFB54A2FE420DD554763BA342E01D79E8D46D7CE6383EEB9D10709`.
  Together they cover §2.1.1–2.1.8 without a gap.
- Added `source/components/032_expose_XIII_section_2_1_9_through_2_1_13.tex`,
  7,124 B, SHA-256
  `B0B176147B01CF7A0738210F8957A4936A1A0201B24180AC0BB441CE6B771165`,
  closing §2.1 through 2.1.13. The cumulative master is now 3,012 B,
  SHA-256
  `4F4A0AE022AF1D81284EABC6A13E43E6AA19EB16C35FCF2A3D0E47625CCB81F9`.
- Personally inspected source indices 105–114 at 1100 dpi. Their stored image
  SHA-256 values, in order, are
  `B3198C3215D54056B67226B9527E1646E364A79C3416585DAE21A159F11A3D11`,
  `03BD58042B3699A59BBDFBB0393999CF40F29C3D953A564F62316C675167C304`,
  `98E2EEA96E9FCAB4AF220D965B0B7414E547C0C2EBF7B641841790C175E4DE8E`,
  `1584AF5D312992344D5988589959AE217F09708C6D4205BD870444672B49DB84`,
  `3FA0412ABED20FA20EC806FF9E8D318DABE309C6D37C867F6F8A37F95724264A`,
  `806E334370EBE47D08B7EB989C25373D9888D7AF0A7E076C588F8A280FEA0522`,
  `13F61185DB1849698C104E549E27C22C8CDA4D6AD489B14AFB1B7E98AF6249DE`,
  `70328D53DF826E38FDE9622CCD619D313132A02D5D99C58E9C13F9BED9CD777F`,
  `E70399727BAE56D965EDA7472F9B21C69675FDBA205203A77F3C21605E426E29`,
  and `C2C41251D93B49A4FAA00BC99D58E36B5D874C4A26F0D9EFBE521B9A1D68C075`.
  The index-114 derived-category formula was additionally examined in a
  targeted enlargement (654,337 B, SHA-256
  `F7C4BBB45C7C85F669F3C3FDADE7EF4C59DFED8A91A4472DB5571073A7C65AA6`),
  confirming that the final $S$ in $X_s\times_sS$ is not barred.
- Transparent source corrections in this tranche: §1.4.2 fixes the scheme named
  in the variation construction from the printed $X$ to its actual fixed target
  $Y$; (2.1.2.4) uses $R\Psi_\eta(K_\eta)$ rather than the impossible printed
  $K_s$; (2.1.7.3) and (2.1.7.4) point to the mathematically matching proper and
  \'{e}tale inverses; and (2.1.8.8) restores the missing bar and closing
  parenthesis. The authority's arrowless upper connector in (2.1.8.7) is
  intentionally retained, because the 1100-dpi image makes that difference
  unambiguous.
- Intermediate cumulative builds through §1.4, §2.1.6, and §2.1.8 reached 56,
  58, and 60 A4 pages respectively, all in three clean passes. The final §2.1
  build is 62 A4 pages / 729,556 B, PDF SHA-256
  `958DC1300694E135ACB93014C6FE9CAE124A8E97318F0FE5D84BAD9BFFE77ED8`;
  pass 2 and pass 3 console SHA-256 are both
  `86DF1C35A73CC745C496AACDB42F8EA2F4F210FC59CE081FA7C24A8F2AAC14EA`;
  the final log has zero diagnostics.
- The final English pages 60–62 were personally inspected at 600 dpi. Their PNG
  SHA-256 values are
  `AE4AB2BA8A07DF521AB95F69B9D866258931A775AC449E065E0007FA6FE7C7B5`,
  `43CB6DA89D112CFA78D2AA71C1804C144FC3AC24DA6B6638605EF48140659685`,
  and `3DFE3252C611AF6196A03358EB87C68DBD6A34F58C98DD1F1211983732B36F6B`.
  The proposition, lemmas, native factorization diagram, and derived tensor
  formula are all legible and correctly attached to their surrounding prose.
- A pre-existing enumitem `Negative labelwidth` warning in the Exposé-XIII
  notation list was removed by using the ordinary description layout; this was
  a layout-only change. The current component 024 is 9,740 B, SHA-256
  `CEDA53E42AAE040C69BD5974B08D227A764187A3FE7C326A6FF52D4EFF78C90C`.
- Exact continuation cursor: scan index 114 / folio 107,
  `authority_snapshot/source/expose_XIII_body.tex` line 963, §2.2,
  “A compatibility (trace morphisms).”

## 2026-08-01 — Exposé XIII §2.2 complete

- Added `source/components/033_expose_XIII_section_2_2.tex`, 6,186 B,
  SHA-256
  `D3897607BF4DB9D3A7CA08D17D078CA14222C33C7970F6ADD4E05EC045E3CC4D`,
  covering 2.2.1 through Scholium 2.2.6 without a gap. The current master is
  3,059 B, SHA-256
  `EB7FB135364F99A1DC2270A695CEE80DDD750A187DD219B3A3419149782CBAAF`.
- Personally inspected source indices 115–117 at 1100 dpi. Their SHA-256 values
  are `E9084E1D5EC3FAD7CCE0DBD39D1C4DB2CBA92F1CCE593F9AC83837220615A938`,
  `E89012422DEC2F5908C686FF2D515A33354E146333AFC6E60BF1766B6B95A261`,
  and `7FBED30E4E93E598FF4F5C59DAAC1590FD49F8C1D6621BCAE58A16184CAF428F`.
  Targeted trace-diagram and scholium enlargements have SHA-256 values
  `E52CC8C0F04D7737B09E9B0AD3F630B399AF45D87E5B59E9F7D71635A3DE5179`,
  `CBAFFE6A1D5ED5A5A27D6D0B2CB9C7D28CEBC0D7A0A608976011843C01E78082`,
  and `79557BE238D5744FEF43F6E423A511251EACC1C5E5EF91DD323E3DE31FB528B3`.
- The English preserves the printed trace-diagram labels
  (2.1.10.1)/(2.1.10.2), but corrects four internally forced slips: the
  coefficient-ring reference 2.2.1 to 2.1.1; the first functor in (2.2.5.1)
  from $Rf_\Phi$ to the defined $Rg_\Phi$; the right-hand support of the local
  isomorphism from $\{x\}$ to $\{y\}$; and the scholium's 2.3.5.1/2 references
  to the immediately preceding 2.2.5.1/2. It also uses $\Phi=\{y\}$ because
  $\Phi\subset Y_s$.
- Three-pass cumulative build PASS: 64 A4 pages / 743,733 B, PDF SHA-256
  `A32D676EF28E833B70B3761CCB44E3289CABC1A2E095AD26696BE6EDCD9A15BD`;
  pass-2/pass-3 console SHA-256
  `1D23007F559E96422AD9638057AABDB135A1BC9FCE70446F6D6A7B76D51AB3F1`;
  diagnostics zero.
- English pages 62–64 were personally inspected at 600 dpi. Their PNG SHA-256
  values are `8C7C10BA63E07E549F505825ADB9116FB63D31FA22F9A2D06A4986B8E0864086`,
  `F4ECAF993B3EE1BEE3B7615E1DB6E272206F30E7DDA30C9EA66BD45A3D71B223`,
  and `5D8FBD2FE723841E87168013691F5987489662E4AB7699622D7A3B4EAB363E2F`.
  All five trace diagrams are native and visually clean.
- Exact continuation cursor: scan index 117 / folio 110,
  `authority_snapshot/source/expose_XIII_body.tex` line 1124, §2.3,
  “Finiteness theorem (in equal characteristic zero).”

## 2026-08-01 — Exposé XIII complete

- Added `source/components/034_expose_XIII_section_2_3.tex`, 3,597 B,
  SHA-256
  `C44D1D827AFD6970A199524DFBE1456BB2DAD0DDE00BA012A4858836540715D3`;
  `035_expose_XIII_section_2_4_1_through_2_4_4.tex`, 2,872 B,
  SHA-256
  `65B222C882F518A8C1CCD2C6A993217542CAFA0BCCE06D90D5AA70AD95295E27`;
  `036_expose_XIII_section_2_4_5_through_2_4_6_6.tex`, 4,820 B,
  SHA-256
  `3C271262FF1E89F01BDE012812EEAC6C8A04EA7BAEBE3AC7427667E932501C8F`;
  and `037_expose_XIII_second_2_4_6_and_bibliography.tex`, 2,090 B,
  SHA-256
  `45F7782078D032ABE2D3E397992EEAB89F71FADF3C225B6944B60C0D0E14952E`.
  Together they close §2.3, all of §2.4, the second printed occurrence of
  2.4.6, and the bibliography without a source gap.
- Personally inspected source scan indices 118–122 at 1100 dpi. Their stored
  image SHA-256 values are
  `E521AA4014FBCB4CFDC22C01BF5CF82A7E59C3A8D7E28AEDC17183F731AB6433`,
  `7531200CB914987A78479608C64FFCD8452435DFA267316A6D500D0D21E62529`,
  `196FED707C6F261F69502F86842E6297B4279E318577D1FABCE98310DE6D3283`,
  `F8F797446277A963F6ED943AD71591A512DCD3A3933FCE250D6617AC3C7AD58D`,
  and
  `44860E1B7CA0EE9F5BCB55D9DCEF3EE5B8BEB6E7FC53DB6F8CAB8EF2863FEFD3`.
  At that resolution the arrows, equality bars, labels, stalk subscripts,
  and circled-arrow marker are all unambiguous; no artificial escalation was
  needed.
- Transparent source dispositions: 2.4.1's “smooth at $X$” is the obvious
  “smooth at $x$”; the general-complex direct summand is
  $R\Phi(K)$, not the printed $R\Phi(F)$; and the variation map cited
  after (2.4.6.2) is (2.4.5.1), not the nonexistent (2.4.4.1). The authority
  genuinely repeats both paragraph number 2.4.6 and diagram number
  (2.4.6.1). The English retains those visible numbers, marks the second
  occurrence explicitly, and notes that it is the one cited by Exposé XV,
  2.2.6.
- Final three-pass cumulative build PASS:
  `build/c037_expose_XIII_complete/SGA7_II_English_source_first_workpass.pdf`,
  69 A4 pages / 773,942 B / SHA-256
  `4CEB7FB7456A2EC7CB3B5E9F1C2B0876E822E143AA53054AF0070CCF976F460D`.
  Pass 2 and pass 3 console SHA-256 are both
  `463A11ABD79B834FB9C63DDF586D8999014097A01CF111B6F9BC5D1AA919081F`;
  the final log has zero diagnostics. The cumulative master is 3,299 B,
  SHA-256
  `C24596ED6550CDB30864F521F714F082B8EF36880E9D652F4D922805CA54A6BA`.
- English pages 65–69 were personally inspected at 600 dpi across the
  successive stable builds. Their final-content PNG SHA-256 values are
  `5AE199A59D5FCE2CC843C25007A38949F43B9A46F61EA01520E0D1E99794271F`,
  `3002645A8CAB4B6AC82154BA6EE3FFB1BD2CCA47EBB402B1934797E1781D2400`,
  `E0FF2700D62970C77410D2D8B199EC1A88D21ED475CCC05280E79349A8B1C738`,
  `1A348C1D92047D34FEF426B27C5CD8120F40A0A4C2DEA186414D7D3797B8ABD1`,
  and
  `14B2B2DFBFA4381928C847583D85A46B174A6AB8F450DB1A9278F587BF153A23`.
  All native diagrams, equation tags, bibliography entries, and page seams
  are legible and unclipped.
- Exact continuation cursor: scan index 123 / folio 116,
  `authority_snapshot/source/expose_XIV_body.tex` line 1, Exposé XIV,
  “Comparison with transcendental theory.”

## 2026-08-01 — Exposé XIV through §1.2

- Added `source/components/038_expose_XIV_title_introduction_through_1_1_5.tex`,
  4,729 B, SHA-256
  `32855C6990FB9CA31CDAC6226CEEB24BA3C6E0165337B6D0DBBD9BB250E05966`;
  `039_expose_XIV_section_1_1_6_through_1_1_11.tex`, 4,980 B, SHA-256
  `61CA0A53DF19C9B3407332189E860C08CC09A2992265F7AFA431CB3C1AD1BDAE`;
  `040_expose_XIV_section_1_2_1_through_1_2_4.tex`, 3,886 B, SHA-256
  `B9BB4996F4F956234D1D753C914894B2BEFA0695D9DA758074E088A4D68E2C09`;
  `041_expose_XIV_section_1_2_5_through_1_2_6.tex`, 1,536 B, SHA-256
  `0C75D8677BF9EEF5B3176A816ECC50759DC5C4CE1665A4DC612D48BA74B84BDF`;
  and `042_expose_XIV_section_1_2_7_through_1_2_8.tex`, 2,109 B, SHA-256
  `222A92B8D876C8DCD5AEF6C0F45425E511DFB70FDC13417C0C1F9DADAE8C3767`.
  Together they translate the title, Introduction, all of §1.1, and all of
  §1.2 without a source gap.
- Personally inspected source indices 123–132 at 1100 dpi. The stored images
  for indices 129–132 have SHA-256 values
  `566F1E1262D36B6C4E731FB4E293EA280E9CB57BA2625881AA8843D8B7334E9D`,
  `D36C2ECF174D02F07CBD145283497A6D59F18569EED3F8BF8506B1C4529BBA1A`,
  `2D57AC3FA47740C496C0804F3B3CA1CF123B978EEF6A6D8A8D58D8DE5578FD64`,
  and `69EE9D7380239C9BF9C27F170CAEECE42DD85D5A64B07FE508F3F3332B08B2B7`.
  The targeted 1100-dpi diagram crop has SHA-256
  `C2843B8A48C517104A8FC73930DDEFA69D5B2E07F9131817248A36C4BC5485AB`.
- The source image confirms two definite frozen-transcription/print
  dispositions. In (1.2.7.1), the print omits the overline from the top-right
  node even though the preceding definition and $p'$ force $\overline X^*$;
  the English restores it and gives an editorial note. In the definition of
  $\Psi_\eta$, the authority target is $X_0\times\mathcal D^*$ rather than the
  transcription's $X_0\times\widetilde D^*$.
- Three-pass cumulative build PASS:
  `build/c042_expose_XIV_section_1_2_complete/SGA7_II_English_source_first_workpass.pdf`,
  76 A4 pages / 806,176 B / SHA-256
  `02519F787284DB446996A614C2B3475F2444A570D9C50457939C59781B259AD7`.
  Pass 2 and pass 3 console SHA-256 are both
  `E21BCA607B8E53AE310CF74B04816DF0268BB98AB1BEF6B66D4ADCB8165F9A14`;
  the final log has zero diagnostics. The cumulative master is 3,615 B,
  SHA-256
  `9AEA57F611AA763D68A425ABB085EA5AB52AB9C9196803F290762A5A16D3C2E5`.
- English pages 70–76 were personally inspected at 600 dpi. The final §1.2
  render hashes for pages 74–76 are
  `6576864FF020938EEE5C88B108773284350AC14169F45E33480845AE7DD5D067`,
  `36754372574E3C83F9C40BEB94B5AF8231545A15180B3E96B8FF696A9F45F583`,
  and `0983D9D96758412F9BAB219D6707C158D1A5292DA6BAF4B90835388A7A6AFECB`.
  All new diagrams, labels, equation tags, and the editorial note are legible
  and unclipped.
- Removed the accidental non-adjudicative `source/$out` build directory after
  re-running the build into its intended isolated directory.
- Exact continuation cursor: scan index 132 / folio 125,
  `authority_snapshot/source/expose_XIV_body.tex` line 375, §1.3,
  “The functor $R\Psi$.”

## 2026-08-01 — Exposé XIV §1 complete

- Added `source/components/043_expose_XIV_section_1_3_1_through_1_3_3.tex`,
  2,600 B, SHA-256
  `7BDFC6AC5BC7565E474B5C5DEE66DEF912831645CF9BEAB432D3C448C1FEEF15`;
  `044_expose_XIV_section_1_3_4_through_1_3_6.tex`, 3,501 B, SHA-256
  `17D4A469968CAC5EBFE3F94FEC6F8763298A7A737D11C43BAD616EB5A78D2FF4`;
  `045_expose_XIV_section_1_4_1_through_1_4_2.tex`, 2,600 B, SHA-256
  `25E1DFEADA67D5FC2AA6948891CC9EF6B1B75CE3A3485DAA3B494F6782089605`;
  `046_expose_XIV_section_1_4_3_through_1_4_5.tex`, 2,050 B, SHA-256
  `09E1952EFB19030AF449CEF164FC026DDA0320C9CDB0D1E34E8EF7033DC21406`;
  and `047_expose_XIV_section_1_4_6_through_1_4_7.tex`, 2,303 B,
  SHA-256
  `6AB21EBDDF1506B3B430748CB4F8AB2F032CEAEE880F036BDC6B2F28F7702810`.
  They complete §§1.3–1.4 and hence all of Exposé XIV §1 without a gap.
- Personally inspected source indices 133–138 at 1100 dpi. The stored image
  SHA-256 values for indices 133–138 are
  `FB5B699D04608F4C31F431D076914DDA947ECDB2D7CFF2BF69A8A690216F8856`,
  `B0562CD95CDC39F094C8BB8E7C948774A87501E72AECE2EF262DED1D14A18C0B`,
  `17C75791B160177C589E176DD9916845053FC5C4123B2EFA931DA25E0CE9DEDC`,
  `2D37EC6DCEBE5AEB9D27A4E9B176D82F50C41EA1A805971EFFCD0655B31131F6`,
  `44DD6FF7D0DCD2B6EC02740A699CADFFDDDD58D767F271326BDA287488CFFFFE`,
  and `B32F378FB64CD8B984AA415EA93459A7754FA8936108984C86254BFE5AB130A9`.
- Direct-image dispositions: the frozen transcription's $\widetilde D$ targets
  in 1.3.1 are the printed script topoi $\mathcal D$ and $\mathcal D^*$; the
  fiber space in 1.3.3 is $X_{\widetilde U^*}$ with its star; and the long exact
  sequence of 1.3.6 comes from the distinguished triangle in 1.2.6, despite the
  print's impossible “triangle 1.2.1” citation. The English makes the latter
  correction explicit.
- Three-pass cumulative build PASS:
  `build/c047_expose_XIV_section_1_complete/SGA7_II_English_source_first_workpass.pdf`,
  81 A4 pages / 828,871 B / SHA-256
  `11AF178C6E6E7C0913EC65722D93CD4286DD579F0288A7EFEBD45692449F54B5`.
  Pass 2 and pass 3 console SHA-256 are both
  `052997D8822215FFE4AEA2039186A3C0E95C369806245FE5E04921B3780481E8`;
  the final log has zero diagnostics. The cumulative master is 3,925 B,
  SHA-256
  `BCD2B091EF5ABF74D27B9195FA561B0678F5B67DC0C56139925584466061841A`.
- English pages 76–81 were personally inspected at 600 dpi. Final render
  hashes for pages 78–81 are
  `59BD098C755CD7044FCD17500DE6837A3D352C13DE33E7DB18BE9EA82DAD59CB`,
  `CDA51215724B1D6352D9DA5E0A63CA2EFADB3FAA9CFFB0337838E8EF8D8F9C55`,
  `08140174810FC4C655ED2509A0C0D00F28D6A65E5A021222CB2D7131FEBB621C`,
  and `D1407C5DC70AACDD2A9C7FD6DF1C03EA7A02D026017BE2C9D3B5D71C2BC75478`.
  All native diagrams, theorem text, support formulas, and page seams are clean.
- Exact continuation cursor: scan index 138 / folio 131,
  `authority_snapshot/source/expose_XIV_body.tex` line 601, §2,
  “The comparison theorem.”

## 2026-08-01 — Exposé XIV §2 complete

- Added `source/components/048_expose_XIV_section_2_1_through_2_5.tex`,
  2,720 B, SHA-256
  `51E36E8CD9A35AB1CDD4A26BDA63AD4FC84514F22DC88D74C55B67F090EE0A6F`;
  `049_expose_XIV_section_2_6.tex`, 2,250 B, SHA-256
  `AB9571E97C599D62919B12F511CB5B428CAB48691C491B5992B6E9AA4CBA27CA`;
  and `050_expose_XIV_section_2_7_through_2_8.tex`, 1,384 B, SHA-256
  `6CE2946DDA39BF64872323DF88A715A3D30BA38897A330CA20E4763FCD75D202`.
  Together they translate all of §2 through Theorem 2.8 and its proof, with a
  hard boundary before §3.
- Personally inspected source indices 139–142 at 1100 dpi. The stored image
  SHA-256 values are
  `FD9B0F3F5CE3D77B833241A5E13D8BEEA9157457E76DB3D8F94EAF64ED0B8D7F`,
  `53FD77E42DE9EE22D7B0EDD5A23FEAB69514A7698F2EFF48054E1E5B11DCDC23`,
  `F39D24DE8E567ABA949B9FD2BC97267E09F04040C0AB388E0709069438D5FAEF`,
  and `67D1E869E565803C1FAC8E648962475A47DF38107B60342A4DF3D4F051C1B4C2`.
  All formulas and small labels were clear at that resolution; no escalation
  was needed.
- Three-pass cumulative build PASS:
  `build/c050_expose_XIV_section_2_complete/SGA7_II_English_source_first_workpass.pdf`,
  83 A4 pages / 837,934 B / SHA-256
  `E18C3028CACCA46D523371A9BA0751A26A1BFC67EB3987F71F0EAF7E32F40626`.
  Pass 2 and pass 3 console SHA-256 are both
  `370CABA6464A632C2FEC472FDA4A75E68AB7D6CA707B7F018F31AB8E97D184E9`;
  the final log has zero diagnostics. The cumulative master is 4,087 B,
  SHA-256
  `6838557D2EA62C9125799F51A0CD1C5CAC31898B437883843DD7EC1E62217B50`.
- English pages 80–83 were personally inspected at 600 dpi. Their PNG
  SHA-256 values are
  `08140174810FC4C655ED2509A0C0D00F28D6A65E5A021222CB2D7131FEBB621C`,
  `E70C7E9C13D6110E293F3332052D85CB395E95232FAEEE4C6A75A25837397185`,
  `6AB193DCD654FBADC2D94E4611564743BA6F44FB0C19422A1222588CDC4F1478`,
  and `148B300DC903D17F57F7D1411A5614FE1C53B3E25842761EAF0D06937EABE6A4`.
  The section transition, comparison morphisms, inverse-limit display, and
  theorem text are clean and unclipped.
- Exact continuation cursor: scan index 142 / folio 135,
  `authority_snapshot/source/expose_XIV_body.tex` line 721, §3,
  “Isolated singularities.”

## 2026-08-01 — Exposé XIV §3.1 complete

- Added `source/components/051_expose_XIV_section_3_1_1_through_3_1_3.tex`,
  4,384 B, SHA-256
  `52E569A640C2C8D300228CB842B307B3F7873867BF8DE3ED34864199B07B1F97`;
  `052_expose_XIV_section_3_1_4_through_3_1_5.tex`, 6,228 B, SHA-256
  `6FD0866C495E6DA1BA8DA4F37818DE0095F67C3255E85171F7098865932FAF95`;
  `053_expose_XIV_section_3_1_6_through_3_1_8.tex`, 5,729 B, SHA-256
  `F82EBDBE8201FD9EA03813704255FC9CE16446298E18149ACD286B6BE139BF51`;
  `054_expose_XIV_section_3_1_9_through_3_1_10.tex`, 6,153 B, SHA-256
  `4C0C1C53D97C172E3376125DC47B1145AB19BE10C97AA46B8B8FFBBBABC3339B`;
  and `055_expose_XIV_section_3_1_11_through_3_1_13.tex`, 3,080 B,
  SHA-256
  `7C6AB6612A92949E891A309C28467A5BA0EB018EB4D2B79041E2E27A10462D5B`.
  They translate §3.1 continuously through 3.1.13.
- Personally inspected authority scan indices 142–153 at 1100 dpi. Exact
  SHA-256 values for the newly generated idx143–153 page witnesses are
  `5BA594D643A40C30FAB7A8CAE255CB65EA0EE7CFBFC4906140531E83D8AD1EEC`,
  `E92C0AF618DC366E047F194AE46775E18E841E31648A4EDDD1C257730AE72BC2`,
  `3C6547A05D22421CD68AB2563F7542B08416F2BF39B109D17DCF7621BA043F5A`,
  `8F6323AF60F5197AFF895E11D55CD7316C5D72DC9924970B0DFFF7819248F997`,
  `FFA71826B9E6317FF337B05DD5FCC1EB2B8B33C9002775C2E95EE5DAD20DD80B`,
  `84167A5A4FBACBAE9EB2F0D402B4C59C23F16A9414DAA31150104F342E435ECB`,
  `61826C1503A26364F42B7D96A8F4DF46FF3355B15ACB1762EC834A74746B6094`,
  `167457BFA24ABB7F969FB4BBEDE92D967DB3CBFC0007061F6DFE28076D3B7DFE`,
  `5D66924A389673F2B4FFAAD400BA15397EB755165122880CFB43E5FBFC3903B4`,
  `2E0542C54B05F26A1D1731A54D14A84BE5D3D0E32CD932788473EC549AB09827`,
  and `E2F2A12F615C7CB398BFF66DC5604BDEDFDEDE342EC67F69DC7392CB365E98B1`.
  Index 142 retains the previously recorded witness SHA
  `67D1E869E565803C1FAC8E648962475A47DF38107B60342A4DF3D4F051C1B4C2`.
- Source-backed dispositions: use $t\leq\tau(d)$ rather than the printed
  $r(d)$; order $d\alpha(u)$ according to the displayed target
  $\partial V\times D_t$; write the proposition's box as $B_{t,d}$ rather
  than the inconsistent $B_{s,t}$; restore the missing $f$ in $f(x)=0$;
  and use the mathematically necessary map
  $\overline B^*\to{}_1\overline B^*$ in the quotient diagram rather than
  repeating the quotient node in both rows.
- The four hand-drawn proof sketches and the $\tau/\varphi_i$ graph were
  reconstructed as native TikZ from the direct authority page. All subsequent
  §3.1 diagrams are also native TeX; no raster is loaded by the reader.
- Three-pass cumulative build PASS:
  `build/c055_expose_XIV_section_3_1_complete/SGA7_II_English_source_first_workpass.pdf`,
  91 A4 pages / 894,287 B / SHA-256
  `B96F64B8B2FDD7F4EA0104D549E5EDBA3FA8EF42FDF8079E88109A1FFC819545`.
  Pass 2 and pass 3 console SHA-256 are both
  `6DD33F8777840A2D3CE732D52B971B38E2F112A09D7B2ABFE2799356C199EF07`;
  the final log has zero diagnostics. The cumulative master is 4,400 B,
  SHA-256
  `15841D439E6EC02FF473C91394CDD5068329D1EEB3B1608FECA55873559C4BBC`.
- English pages 83–91 were personally inspected at 600 dpi across the stable
  builds. Final page-87–91 PNG SHA-256 values are
  `B64242A6DB9022F047F4705A547CB5D60E4F1D689BEFBE554206C7D555555079`,
  `015BE3672A9A6DA925FF81ED2180D31D30CD42D52342DA430D206709773D4662`,
  `C931C45DA565F224D5766C77828D6DD186DE54001EA7526B9FC8A25F294176D8`,
  `BD36F763EDC51D8B3845FB914531DABB9E0F811EBCF846B166B07D1BAE0F3C0D`,
  and `971457812FDEFC286E997D6F44E87DD39E6F0850E27FF5BA54D6AA3923C572DB`.
  All diagrams, equation tags, page seams, and final monodromy formulas are
  legible and unclipped.
- Exact continuation cursor: scan index 153 / folio 146,
  `authority_snapshot/source/expose_XIV_body.tex` line 1112, §3.2,
  “The Picard–Lefschetz formula (transcendental case).”

## 2026-08-01 — Exposé XIV §3.2 complete

- Added `source/components/056_expose_XIV_section_3_2_1_through_3_2_5.tex`,
  4,061 B, SHA-256
  `3D49137E8252FA8342BCF15DBAD155C46CD9D4E1F968FC345A091A014B9D80D8`;
  `057_expose_XIV_section_3_2_7_through_3_2_9.tex`, 2,470 B, SHA-256
  `06E1D5F39085E63C36920A5F5D8C3B1EA3BE92D707C66A6B44B58F0240C6BB35`;
  and `058_expose_XIV_section_3_2_10_through_3_2_11.tex`, 4,382 B,
  SHA-256
  `43A8B3E54CE34BB68D8FDE9C2DD463824FFEAD566D9233D547FDB91144CAB45E`.
  Together they translate §3.2 continuously through Theorem 3.2.11; the source
  itself has no paragraph numbered 3.2.6, which the English does not invent.
- Personally inspected authority scan indices 153–159 at 1100 dpi. Exact
  image SHA-256 values are
  `E2F2A12F615C7CB398BFF66DC5604BDEDFDEDE342EC67F69DC7392CB365E98B1`,
  `F441D7BD1AFF7DE5F3C89B2F64B17AACBB7BF27420A80A532D4B924210306999`,
  `D636677AE3FF2FB5E06CC2DAC5AD55B6D3F761FBB3A73F721558E40B13850F82`,
  `9AA335BA43694E9E7FAC8340A8A5DD19563A29950C0B260F9EA056E3C6E8FA64`,
  `EDADA5210FA7A088F5807E4C1A175EB3A0B701E7705C18A9AE113C6F07F5B186`,
  `8C2B258F2181E0D889713F534629095694DB158A1614B51D59CB2476C3C544A4`,
  and `A79C0E061EB856254D426AA69FED2993006CCB4F59C799DF3E1A31F687AD3400`.
  The page-151 diagram crop is fully legible at this scale; escalation would
  only enlarge already-resolved source pixels.
- Source-backed dispositions: correct the ambient orthogonality space from the
  printed $\mathbb R^n$ to $\mathbb R^{n+1}$; use one general dimension symbol
  $d$ where the print mixes $x$, $n$, and $d$; restore the missing closing
  parenthesis in $-\pi(1-\varphi(|u|))$. These definite print typos are
  disclosed in the English footnotes where mathematically material.
- Reconstructed both $n=1$ variation drawings as native TikZ, preserving all
  three nested boundaries, the radial cut, arrow directions, labels
  $\delta,\delta',\varepsilon,1,2$, and the spiral defining
  $\operatorname{Var}(\delta')$. No raster image is loaded.
- Three-pass cumulative build PASS:
  `build/c058_expose_XIV_section_3_2_complete/SGA7_II_English_source_first_workpass.pdf`,
  95 A4 pages / 913,789 B / SHA-256
  `858F291A09209C191C1162C1703ED023922560A8936B4A436E6A447D12D3A098`.
  Pass 2 and pass 3 console SHA-256 are both
  `005C7CB4A283560050FC6058E31538DCBE5D4808B9A25B8AFCCA179A3CDE789B`;
  the final log has zero diagnostics. The cumulative master is 4,588 B,
  SHA-256
  `BD173A7E8DD6431D635828A7EFC8B5C33B51503310CF8483DE2796C5E07F07EB`.
- English pages 91–95 were personally inspected at 600 dpi. Their PNG
  SHA-256 values are
  `465B34BDD2BE9F6C9ABF8A5D68B95343D90401B16FAA3D583D6E62E3E7CE5336`,
  `EA66610E1EBB5ACC59023CD408D32579E94317A599FE107D46FEF7F29658DBA7`,
  `EF9D7F157427B70EE6A73C2E1503F6C872239C3A25A898C860CA9947F753DFAD`,
  `9EF3886DB86C07978F1129E285396C8DF015F856CED146E8F99F939748DFFAE9`,
  and `739B534F5A6368F5EE1CDA38625BF7056186AE7B729D43C5D52DE1E9E7246AD2`.
  The section seam, footnotes, equations, both native drawings, theorem text,
  and sign table are clean and unclipped.
- Exact continuation cursor: scan index 159 / folio 152,
  `authority_snapshot/source/expose_XIV_body.tex` line 1341, §4,
  “De Rham cohomology.”

## 2026-08-01 — Exposé XIV §4 and Exposé XIV complete

- Added `source/components/059_expose_XIV_section_4_1_through_4_4.tex`,
  2,959 B, SHA-256
  `219CEAA9E025491272B8423E445D3096A22C11F68C26504C3A5A243CE9316EE0`;
  `060_expose_XIV_section_4_5_through_4_8.tex`, 5,430 B, SHA-256
  `4A10D378F78CCC4949D175EB9235732BBE971DE523635B2E4DEB5CB5429DD911`;
  `061_expose_XIV_section_4_9_through_4_17.tex`, 4,835 B, SHA-256
  `4F443E16C52EDF24E16B4438584B4D3B20ECFD92FEAC522B4CECB3BA974F5629`;
  `062_expose_XIV_section_4_18.tex`, 6,791 B, SHA-256
  `C642B83245125C45AC9909F5E8647050449D62036185C5D5EA6F98BADC539FD4`;
  and `063_expose_XIV_section_4_19_through_bibliography.tex`, 3,034 B,
  SHA-256
  `548F4867546E3CA374DD9AE4A012E7CA0B1168E666BFD1B017B024EBF3504789`.
  Together they translate §4 continuously through Remark 4.20 and the
  bibliography, completing Exposé XIV.
- Personally inspected authority scan indices 160–171 at 1100 dpi. The exact
  SHA-256 values for physical pages 161–172 are
  `BAB3ACFC03C37E04C3A144F31AA852FF259FFC72A6B7F48034421954A9FC836A`,
  `D1567FCC84E900F56329523409CF48DE9BA581BAB96029525B4F5AC99ED8DD97`,
  `82E531988F9B329AE22A54BD94350A9B659C7B5F30CD856CBBB46AD6652FE608`,
  `FC266766DF555B965C74CC448066E60AD27CE8D35EC2829DB961DF46AD054571`,
  `998202DC56EC23F4DE25AF8AA442555CE83B40EAA3D8741A3170FF03D10264B9`,
  `76A709BAC5915014A071427512567E7226FF075E0A7BD57F6E37D25148599431`,
  `16C36ED1E8595E1206B082DE11C1E05B3DA6C03687E830FE5316ECF5B631A872`,
  `466CBD98B7C51318E08E6517E42E77E3EEF403580F252522FB49F36D55686318`,
  `93587C37ECC4845324401CC14724C73A7A14C625B0CDF42A4A6A1BE35DAE111C`,
  `A0BEBD6320DC94499748579EAEF6426A0FA9DBD2B475B75747ABAD233BB94718`,
  `79CF7A82BA7082F91D82E934C0B81BE630D7EE1A05460172AA0CAAB4F3F257FE`,
  and `94A522E24135674831842C1BC5F1A5EB282572A608EBBD3CC0974363DAE9D0CC`.
- Source-backed dispositions: restore $U^*$ in (4.18.2), where the print has
  the impossible $U$; restore the rank-one system $V$ in the first term of
  Lemma 4.18.4, where the print has $\mathbb C$; read the letter/zero slip as
  $E_2^{0n}$; correct the proof's mistaken reference from 4.18.4 to 4.18.5;
  and restore $u^*$ in the higher-direct-image term of the Grauert argument.
  These changes preserve the statements actually proved and are disclosed in
  the reader where material.
- Reconstructed both closing commutative diagrams as native TikZ from the
  direct authority images. The final render preserves all nodes, arrows,
  equality bars, left/right label placement, isomorphism marks, and terminal
  punctuation; no raster is loaded.
- Three-pass cumulative build PASS:
  `build/c063_expose_XIV_complete_r2/SGA7_II_English_source_first_workpass.pdf`,
  104 A4 pages / 974,922 B / SHA-256
  `D98C1E1238356FE4A438606D743B6581AB6F042C02C26ECD44D39E3CF397560D`.
  Pass 2 and pass 3 console SHA-256 are both
  `67DE15BE61C7F1614633E5CB96AF90CC43659D9D8FCB8AD37315D53314D61A70`;
  the final log has zero diagnostics. The cumulative master is 4,878 B,
  SHA-256
  `718B59D94DA0B687064708641C8E35E3A4C33928AE71849EABBBB751FA9D381C`.
- English pages 95–104 were personally inspected at successive 600-dpi
  component boundaries. Final page-100–104 PNG SHA-256 values are
  `123080979F5AAF8484AE8544883071FFA65CB6DB39BBCE2416CA668FCDA14F4A`,
  `C32D9360EC9FF6BAF7041A1159C5F8A815C995DDC7EED1BA95D6D2DD9F7D3BEA`,
  `26F4725A83BC69454A83C5E2B51CD454267032BDD96F2584E55D975C790CBD3D`,
  `F29C927889BEA93426CA59E6A0C7BA32B77028D893661FCA2EDE171CE9972E24`,
  and `6F633AB3ED3F0AB4919562EAA3BCD0E3D2C134C0A28472C6B7964FC39FAE7355`.
  The final diagrams, footnotes, formulas, section seam, and bibliography are
  clean and unclipped.
- Exact continuation cursor: scan index 172 / folio 165,
  `authority_snapshot/source/expose_XV_body.tex` line 5, Exposé XV title and
  contents, followed by §1.

## 2026-08-01 — Exposé XV opening through §1.2 complete

- Added `source/components/064_expose_XV_title_through_1_1_4.tex`, 5,463 B,
  SHA-256
  `C8A959A86C810E71D1C4B259FAB9086B1142878BD1770464E839274CEDAE2A06`;
  `065_expose_XV_section_1_2_1_through_1_2_6_reduction.tex`, 3,498 B,
  SHA-256
  `616F9950137BE1E5775DE6FA7B24B512CD0F775A25F417EB31AD97672236CCAC`;
  and `066_expose_XV_section_1_2_7_through_1_2_12.tex`, 7,898 B,
  SHA-256
  `D50B66B5D00D24AE6C9623B1BEEE8BA89A069205270D3002D1B598C20C9E72AC`.
  Together they translate the title, contents, §§1.1--1.2, Theorem 1.2.6 and
  its complete proof, and Remark 1.2.12.
- Personally inspected authority scan indices 172–181 at 1100 dpi. Physical
  page 173–182 image SHA-256 values are
  `97FF03249E7082BAE46F28A7ED6908FB49E459767C793B4780785624C00EEC19`,
  `CFF4237AE8155A5D315544D60677448BD1C42F43E1C3B6B673856C7C5841CD7B`,
  `C6439FC361A64D94588206E5820C84FB4B66A3E87CB61D0AD9F3996FDBB4E24C`,
  `2203A3868E86DCF6620AEA3BEFC476E7471F69050C536BDF9543D684E9FAE123`,
  `A460DA203E9E54D937FADB183713B2048FCE103575752487C39DC2E0EDC881B0`,
  `6E6E4B42A7F20BE6C3767CD205E536E2516D32197ED6DE41854812150869DE30`,
  `80CB008D51F9D36EDB992D38291EF42DF1A81B3576BB6ED08656A87F5D53BDCA`,
  `E57CB7F4513A81D0132431E4AC7A3B63E665CBF180143DC1A2CC4C5C777891E8`,
  `67D810C56E8D9C15A4AA3BC4B600C74E2DB4F8C8C07F2F231D1E001822489FCA`,
  and `5FF5B51818284AC56525A57EF4BF5361AE3C282E57E29D5FBDDD2B6725BBA5A3`.
  All prose, formula characters, and diagrams were clear at that scale; no
  higher-detail escalation was needed.
- Source-backed dispositions: restore the local equation tag (1.2.1.1) and
  remove the printed extra equals sign after $Q$; correct the print's reference
  “4.3” to Example 1.2.3 and “4.11.1” to (1.2.11.1); retain the concluding
  congruence $Q(x_i)\equiv0\pmod{\delta^2\mathfrak q+(f)}$. Each materially
  visible correction is disclosed beside the English text.
- Three-pass cumulative build PASS:
  `build/c066_expose_XV_section_1_2_complete/SGA7_II_English_source_first_workpass.pdf`,
  110 A4 pages / 1,016,178 B / SHA-256
  `DDF9B156B56C5E17658B36EB616016D1AC5020132B28A5CEF13510F755AF467A`.
  Pass 2 and pass 3 console SHA-256 are both
  `CB88BB0F1BB2277F91DF37D5863C3F79B6B45E60951158F319B7B247702EDEC0`;
  the final log is 38,391 B, SHA-256
  `67A0147B6CB2C0B8B99B1FC649BB97AC36D206AAA3CD08A3553ED7B846BA0FB8`,
  with zero diagnostics. The cumulative master is 5,064 B, SHA-256
  `3BC78A3A9BED469F21C95EC555D88E478D04AC361A725C70678D1C85180EFAEC`.
- English pages 107–110 were personally inspected at 600 dpi. Their PNG
  SHA-256 values are
  `B1EE9452E0BBFDC885D65ED116A0FFB41B0594534A4FB2208D842D55E80F598C`,
  `0D11D7A94D40D76F01A378E1C52C3D187678B8890E1F2873200A182D28B15F94`,
  `D2E07A2DDF0CBB8A28572A9553EC0580ADE94C645833D28026ADA89D3FCA3ED0`,
  and `E88254CF3D464F7632C23367FC9D78C3A6A96E61CD34F2456BB098899D7DA774`.
  The theorem underlining, normal forms, native triangle, long congruence proof,
  footnotes, and page seams are clean and unclipped.
- Exact continuation cursor: scan index 181 / folio 174,
  `authority_snapshot/source/expose_XV_body.tex` line 280, §1.3, “Moduli of
  quadratic singularities.”

## 2026-08-01 — Exposé XV through §3.2.3

- Added the continuous English source from §1.3 through §3.2.3 in components
  067–076.  Current component identities from §2.2 onward are:
  `071_expose_XV_section_2_2_1_through_2_2_4.tex`, 3,545 B, SHA-256
  `3A8B93C6BDDBD2AF138295D4E54D6AFB2FA58ABD64EEAABCF27C8A7491ABADA0`;
  component 072, 2,374 B, SHA-256
  `652C1A65F293F5AF00F0BBC4632B0ABCA986245D44492F4EB0A6C2A428EC36EB`;
  component 073, 2,999 B, SHA-256
  `F28BA44407244EB3F14642349E970B47B7966B3665C8039333967253F9A8555B`;
  component 074, 2,871 B, SHA-256
  `8C2E022B72E9F72116ACE86D681FE235C27CF722015655D780F6FB18BA8E3022`;
  component 075, 2,122 B, SHA-256
  `BA89E4EEEF5A2192310F3124505EED36366F9457BB087C0167F77771072C9EE5`;
  component 076, 2,737 B, SHA-256
  `FB244E801D44B2F833D4700F99EE178E6F9BB0DD36ECA27492BB7B13C1627865`.
- Personally inspected authority physical pages 183–198 at 1100 dpi.  Their
  SHA-256 sequence is
  `5D67CC93391FC1AD0121E89ADB2ADC3F8F1AC99DC6B098A83C574D9E6F38EF76`,
  `B9A8D8960DCFC05BF4E3FC8FFE793D435989E40F6F20A276CC993FDB92166F6F`,
  `A6561479CCF805AAE2049A5312879A57072FE402509BE3AE73E993DFD7F8C8F6`,
  `027A24F16BC7F9881F36BAF3278CDF9AC276AA7FD19B9DB8BA84A01BBC9E210C`,
  `0903F630D21458A7A26576C95A295C024821A2F6FF429FFA99A5E8B77E24B749`,
  `D83DD0E6B0BF0409421A83B7F166E695BEC83931B8A85F4AFA13DECF59498B1E`,
  `24FD137299D23D404736A20F5F27F89C1F073526DC43DA30B3BC361C812BCC60`,
  `13778D808A8F69F53B77EB45C0F9B1C61458FC8D169BF7C61766C32B1E883941`,
  `0DB030888348D924FAC7683CD0FCB08B404DE090712C3A7D3AD38C37A37CBBCC`,
  `3E0C5099E56DF431841A57CDEF6BD440B858FEA70CBB65BF2B36A2D80B688C38`,
  `ABDA536479EA54A2909981FB3BDEDA80DBECFE3066CD8589CC888F5D07966199`,
  `1958AD5F32F95447D535E0507061D164A56B4B94861FBB4E4617BCE66DCCD0F3`,
  `ABC3E0D446C7F28D043A49D0970DA287202F08A5346335C41846D80D930D3B8A`,
  `4C8C69E3AB7540963CC5F316370C1F3CB44908DDB1D7087BDB9E4A14E1A9B7BD`,
  `F605123A5A13186D20D17580B425AABD418C0D2DBA359664FD2AEE7F4A20D8AC`,
  and `2A84CB86F44D011E2D6EBCFCF8F860C701EC0153882D4060893F9139C20C4457`.
- Source-backed corrections are disclosed in situ: $X'_s\to X_s$,
  $H^o\to H^0$, the dropped $\bar\eta$, the pairing comma, the degree
  $H_c^i\to H_c^n$, $x\to x_0$ in the support, \emph{seul}\to\emph{nul},
  and $R^n\psi\to R\psi$ in the two statements whose cited results fix the
  complex.  The native specialization label was moved above its arrow after
  the first English render exposed the layout mismatch.
- Latest three-pass cumulative build PASS:
  `build/c076_expose_XV_section_3_2_complete/SGA7_II_English_source_first_workpass.pdf`,
  121 A4 pages / 692,478 B / SHA-256
  `27D11BAE431747BF9342EC8AEB3CB37C36074BBE8AE1EE1DCDF439EF2BB86A11`.
  Pass 2 and pass 3 console SHA-256 are both
  `FE866590761ADD4D9F0E8955573D54F80637C83555FC4FDA60823A9F70890DD7`;
  the final log is 35,136 B, SHA-256
  `336D7D72A7E932C2BCE6E47FA0362DD5B2DFBC9CFDDA12ACBA1535EBE78D585B`,
  with zero critical diagnostics.  The cumulative master is 5,628 B,
  SHA-256 `E688C699065D802D4C17E2DA6CBEB3F0F08F1EA05EC0C3832B9A181BE2E5EE34`.
- English pages 119–121 were personally inspected at 600 dpi; SHA-256 values
  are `92D15C547482A51F5988348DBBEA39AE0297B8DE22811BFDB87409DC3CEC863A`,
  `10C0681E4E8963FBB1E1D4189945C140EB7FD75213D4B9D75813E7B6348C461A`,
  and `C7B652200EA8C1FC6FB5091624BDD42E3578DF7B6FD54DC95E2D47185470BDA1`.
  All three native diagrams, underlined theorem text, footnotes, formula tags,
  and page seams are clean and unclipped.
- Exact continuation cursor: scan index 197 / folio 190,
  `authority_snapshot/source/expose_XV_body.tex` line 947, §3.3, “Odd
  relative dimension.”

## 2026-08-01 — Exposé XV §3.3 through terminal §3.4 complete

- Added five continuous English components:
  - `077_expose_XV_section_3_3_1_through_3_3_3.tex`, 3,700 B, SHA-256
    `A40A36A01D525F42313727241B735E04B1DEED8F39097CBD2E4F2F58DE039EE1`;
  - `078_expose_XV_section_3_3_4_through_proposition_3_3_6.tex`, 1,730 B,
    SHA-256 `4D51A832237099314F4170F2FE908F406EB66D6836C324EBBA88B5E05A432C22`;
  - `079_expose_XV_proofs_3_3_5_3_3_6_A_through_C.tex`, 1,976 B, SHA-256
    `465420EA2C90604241A427B91686DCC190C4C151F77084CDBA98A7782EB880C3`;
  - `080_expose_XV_proofs_3_3_5_3_3_6_D_through_F.tex`, 2,943 B, SHA-256
    `CC088BF3A718BA557029651556C73526FF0B9EF4E09A76EE153675C795AF2AD4`;
  - `081_expose_XV_section_3_4_summary.tex`, 2,231 B, SHA-256
    `E5108E57365CD7F4EE99D0883CE0B92A59A2344E2FCCE8313359837D5C9E3356`.
- Direct 1100-dpi authority images for physical pages 199–204 have SHA-256
  `86D780AE438D66DC9A099A41545DAD1194BD572E4AA6A5ACFFC62E57A37B0C0A`,
  `4009538088787D827E23A58C1DB1E3827E44212AE4BE14245F4926E78F11F97F`,
  `1367CD0CC981EBD84655C1AD45DAE26C3CFE9A95C016407A0AF615483136150F`,
  `143C67D48279B1F353F2762AB1EA6C757E8AD0E23D51B4B138E0722842F92AD2`,
  `A7D5346DC22A659B6955F7630A6843B618815F10E4C2523D97DF8786926C57B1`,
  and `0CE3701B83496850A58B131009A80D52C173306839A685072F63186ED831CE17`.
  All formulas and diagram details were decisive at 1100 dpi; no artificial
  higher-resolution escalation was needed.
- The first c081 render exposed item (D) running into the end of item (C) at
  the component seam. A copy-on-write paragraph-boundary repair produced r2.
  The r3 build additionally converts twelve inherited Unicode smart quotes to
  TeX quotes in components 001, 003, 005, and 020; this removes the twelve
  prior missing-glyph diagnostics without changing the translation.
- Final three-pass build:
  `build/c081_expose_XV_complete_r3/SGA7_II_English_source_first_workpass.pdf`,
  125 A4 pages / 715,273 B / SHA-256
  `6E4D81DC5F9BD3A4EA0A33E0970AD77EA76A702800EF663527B2B6B863057F76`.
  Passes 2 and 3 have identical console SHA-256
  `1E154F6F49B5D001EE7C3837A09DB3E4D648BE47BC4F187AF2C910B5C9A35156`;
  final log 34,763 B / SHA-256
  `6D63FC3F047177EDED707D0C42B6900E76A60645F78F43C6454612A74F63DAF0`,
  with zero critical diagnostics. The cumulative master is 5,943 B / SHA-256
  `F74BE52E7D9CC43BB8BF442EBFBC56ADFA180001B4ED1259C4E830E119B747EF`.
- Final 600-dpi English renders pages 122–125 have SHA-256
  `1CA1A197F7E44F08E200B6397C3EC9F3029D3F9CDD11C59B4C351CA144E161D0`,
  `CB31880FDB1BD97EE7EEA8B9F06AB09AB60B20ABDD41B8313F50907F13391973`,
  `7A0AFB6F30CB948F58AA5DF4649C12AA65B20D282D244C12B482B8F2DB917B9B`,
  and `825367DDC119C937C073DD903F0DD06D96C4F2ED67A0ABBAC36C37816F760779`.
  Lead review PASS: both native diagrams, proof divisions, exact sequence,
  theorem formulas, underlining, and page seams are clean and unclipped.
- A malformed first build invocation created a literal `source/$out` scratch
  subtree. It is preserved as non-adjudicative history and excluded from all
  source/build/package identities; c081 r1–r3 under `build/` are the intended
  build lineage.
- Exposé XV is complete. Exact continuation cursor: scan index 204 / folio 197,
  `authority_snapshot/source/expose_XVI_body.tex` line 5, Exposé XVI, “The
  Milnor formula.”

## 2026-08-01 — Exposé XVI complete

- Added eight continuous English components covering the title through the
  bibliography:
  - `082_expose_XVI_title_through_1_5.tex`, 4,243 B, SHA-256
    `44958861F447617D901FBDD6DB8782ABFB67B700B9F8781E2A000DF8FD58C4C2`;
  - `083_expose_XVI_sections_1_6_through_1_10.tex`, 3,462 B, SHA-256
    `97ABBAFA3726531ED414D7CA68EC19A2C1F6313D769D46E848F2A01B27C38291`;
  - `084_expose_XVI_sections_1_11_through_1_12.tex`, 2,098 B, SHA-256
    `8FE9F877358A180E8B56104AFB78780DEF04FE2BE7DCE06092E2C905BA35E594`;
  - `085_expose_XVI_section_1_13.tex`, 2,684 B, SHA-256
    `1AF1E6E61810368966818523BB58515F6C07868F96884AEEDCE83F1A0A5A70C4`;
  - `086_expose_XVI_section_2_1.tex`, 3,690 B, SHA-256
    `F239A502EBFC2FA81C639B1E10B83974FDD8F02E0604CA9D6E65A7E7978A8EFE`;
  - `087_expose_XVI_section_2_2.tex`, 2,439 B, SHA-256
    `27CCE5570DA6206123BD6DF42FF74896D2BF56857D0F20AD43B1E5412775B1F3`;
  - `088_expose_XVI_sections_2_3_through_proposition_2_5.tex`, 2,716 B,
    SHA-256 `EC0379A65FAC2CD57C7A7EE6740DE7F1972E38C956D3E07D13842408C5098B5A`;
  - `089_expose_XVI_proof_2_5_and_bibliography.tex`, 3,637 B, SHA-256
    `E2ADE2E25DF4E837A1ADB50C1CC9B452A5C627A2417BBB160357ADEE235EA4AC`.
- Personally inspected authority physical pages 205–219 (scan indices 204–218)
  at 1100 dpi. Their image SHA-256 values are
  `1AE24A5D9889331B767033B5B8897CB8733A32ABC39367BD04C3CFFFBE0A405B`,
  `3759CBC54B5AC367691E2583ECDA792804F19ED2880B8C9B1E86CECD27EE80A8`,
  `E1C7D02480C5C57ED65DEFE2CE993116201B97797F1849FD81490A39829212AE`,
  `DAF9EDB64D772ED87BE35F7DD98F2F1439E2FDE1965EA99253D7D11B238CE8AD`,
  `B3F6759B44736B145A199A53A2AADF3C85021CBFC25EA21C2DA219F6A4AE57B1`,
  `40C6FE34E8F328EF1BAA52AFDE4763C4C9C6A812215B3E9366028D4F0B6E62D0`,
  `50125415D7B328CB2C4F2A4462CD32D44BE3DA8F5D4DF65C362D4C1C40E0694B`,
  `A9905DE91165CED5C1E3C86A18CBEDB8DB3396620E3404D1970F4CB1E2D739EA`,
  `A2EC209835EA39BE409EE91F3BD087135467462A14BBAD02F3A5794D6C0CF885`,
  `6504A61ACDCC5272B081026E9F2FC55811FB36C3DE7E61DCBDAA53BBE20D364A`,
  `D8A3AFF39A19261CFF73E88142926C50FB04B981FB4AC1907FC16BF326A6E948`,
  `DE1914BC037C5456AEC54BD0EE1873B2688679A5408D81975BFD9E08C1C9DA62`,
  `4E1C55B007D0BD7A23ED0D9FCA7D07C6B07011A14B63583555B250DAF253D07B`,
  `0A1AFFB08AD957CD27ADBDDDAA3829EEAEDB7DA705502B203374AD66966E5506`,
  and `5EBE76AE3A466A47C0C68350DFC71B12349A2EF1AAECE246DB18C000A2E1BE54`.
  The exposé contains no diagrams, and every small formula detail was decisive at
  this scale, so no artificial high-resolution escalation was made.
- Source-critical dispositions: use printed $\mathbb Z_\ell$ rather than frozen
  $\mathbb Z/\ell$; use printed $\mu$ in the Chern-zero sums; correct the obvious
  $\Phi^i/\Phi^n$ and $X\times_sS'/X\times_SS'$ slips; disclose rather than fill
  the blank citation in Proposition 1.13; correct the printed minus before the
  Swan term because the cited Artin-conductor formula and the source's own
  identity (c) force a plus; and replace the undefined $Y/T$ with the morphism
  $Y/\mathbb P^1_k$ actually defined in Proposition 2.5, with an explicit note.
- The first complete render exposed a missing backslash before
  `\operatorname{pr}_1`, which compiled but printed the literal word
  `operatornamepr`. Component 089 was repaired copy-on-write and the r2 page was
  re-rendered and personally checked.
- Final three-pass cumulative build:
  `build/c089_expose_XVI_complete_r2/SGA7_II_English_source_first_workpass.pdf`,
  134 A4 pages / 762,104 B / SHA-256
  `3E37F88F935932039BF6B642A989C2A1BA5639AD58F45106C1080823DC68EC8D`.
  Passes 2 and 3 have identical console SHA-256
  `6F6FE36DDEC01B4E70DA9AF104534511D6559ED3A8BD4118A19D95F12FDEE68A`;
  final log 35,250 B / SHA-256
  `BB20B1413FD79C37F49064B95812F801F73BAF17CB69C04FA73C51BB79415100`,
  with zero critical diagnostics. The cumulative master is 6,387 B / SHA-256
  `08AC1AD97343B43E333E3226D79D07513E494D406BF40C54CD6DD6DD288ED0B5`.
- Final 600-dpi English renders pages 131–134 have SHA-256
  `BACB6559A8B36855D591AE57E92A30CC90CAA7695DAC040AC18B15A350EDEDEB`,
  `C4108C692DEC648C520459B7C2FD993D5736501A55E71201A41C8BB415709E6F`,
  `03429F75CA4A944B1C739FF97A6A8B6AF1489D1F02992B3334010E15847696CE`,
  and `173B00C5529971275DADB9121572CD1037C4A8DA4CE18457C217D02083C42BEE`.
  Lead review PASS: all theorem seams, displayed identities, correction notes,
  projection notation, and bibliography are clean and unclipped.
- Exposé XVI is complete. Exact continuation cursor: scan index 219 / folio 212,
  `authority_snapshot/source/expose_XVII_body.tex` line 5, Exposé XVII,
  “Lefschetz pencils: existence theorem.”

## 2026-08-01 — Exposé XVII through §3.7

- Added ten continuous English components covering the Exposé-XVII title
  through §3.7. The exact component identities are:
  - `090_expose_XVII_title_introduction_and_section_1.tex`, 3,889 B, SHA-256
    `9246370BBE6C911CBAFA5CFB41094AB71CBA930D7DF6B58E1F590775AB4D2C09`;
  - `091_expose_XVII_section_2.tex`, 3,583 B, SHA-256
    `DB35293A03D4ACA3D9C076DF7C04B5604781608FF7F2270253BE340909F06AC7`;
  - `092_expose_XVII_section_3_1.tex`, 2,629 B, SHA-256
    `BD469543200B7A3849E7BBA7BD4C9DBB4996C6A062A52D977E2AAD0256DD6090`;
  - `093_expose_XVII_section_3_2_and_proposition_3_3.tex`, 4,337 B, SHA-256
    `8FA4258BDF1B4756155D407575C4CAF4A3080D264800D12615BCAAD8D6438F4A`;
  - `094_expose_XVII_proof_3_3_coordinates.tex`, 3,992 B, SHA-256
    `920B8FB069370FCA227402E0A48952C4C982A9BF69682D6EA92344B549D2A1BE`;
  - `095_expose_XVII_proof_3_3_matrix_and_example_3_4.tex`, 1,877 B, SHA-256
    `78921D8E72258C296FE4FF5720A97783814F628D5B6A543C1A22AC61D96A62AD`;
  - `096_expose_XVII_proposition_3_5_and_opening_proof.tex`, 4,018 B,
    SHA-256 `070B6DE6D072CCAD2D5E67632931D727D53E0E993670BF6BC149F350566CD97B`;
  - `097_expose_XVII_lemma_3_6.tex`, 3,085 B, SHA-256
    `C27A111A00D57046621A2693EB04D5205EBF8568561A19FC116CB222499A39C7`;
  - `098_expose_XVII_completion_of_proof_3_5.tex`, 2,324 B, SHA-256
    `FC4DD07B35D908A97FEB306446DE9BB1171B7A505A2B77F1EB09985E09E29FE5`;
  - `099_expose_XVII_section_3_7.tex`, 1,551 B, SHA-256
    `145020D71FD98C16ADC259E133A54B8DE60AC0540CAABDB0104E4E0537C7B638`.
- Personally inspected authority physical pages 220–243 at 1100 dpi. Every
  formula and diagram detail in this range was decisive at that scale, so no
  artificial high-resolution escalation was needed. The image SHA-256 sequence
  is `D08299D66E61358CA0284EE1CE46F8B5D9829C3D424F5250F3131FCCFDF36E9D`,
  `7A8AA297BD98E818E26F0808B311B616BD2714BEC57741569502B3B27F953A50`,
  `CE0BB17DED1505451384C721345952D2B03DBBA29D7E5D83EC106829714BE313`,
  `75BCC9A7A5605A938B35CF10F0569CBB1101BB21A27C75A90478910EE92DCAA2`,
  `D7EABD1215CB55D6D215B18C23D5D9240917F7158E48CCC48D2D17B540FFEF6C`,
  `B5D3CCCEC3FC5C7BBBE17A1C3C7C21DD18F44CCD3ECDD5DD73F6153D338D249E`,
  `63457AABA2DA2FD7035D9975CDCAA50061231040FC6830226DA28A69AD683E07`,
  `34A22B88D052B1F9874660414D14B7FDCF00BAE7ED7262DB1655395CEF96C4C4`,
  `CBE1192554C6B19A9E4A19A7540310D13C506990C18A0931565C44E6A0A9F3D2`,
  `7F60D74E9EFC6D2803983FAAFAFBDE9E5DB485E6F7622E87EE20F3FD8C392BBE`,
  `285F4CC478FB2AD0E09C2A39064B765DA3CD401324EC7A8CA0C3DE83BAAC80E7`,
  `4557000D89E38B6AA402CF080B7F9DF438FBDB6157D164C2ECB3E30E6D3B1B84`,
  `501DFB5594F9292D28B257F1AB52ABD35B217B251542562B62C9851906BE4BF6`,
  `CFEC9748CE3EB76D20E1FC74D588D86BEC5AEB878A26FA384F4338A6BC77B918`,
  `CD88BB06CE78ADA9A9B5F051C4B0D8D462ABDE0BE25478837A8077C65577E019`,
  `EC145D6A089FD88F21CDA8B4275ECF88AF0E725A254437E0FF0C70E48BAE8A4A`,
  `8F0096D682418520B3696F7B37CA2AC6510739C8FCC96297057DB5E5AD42FE55`,
  `71D3F5C980A30DA9D03BECF6F52C513D25A8D7B641615C1374D67412BF45BF9D`,
  `A193D650FDCDB2EC80719C7A4E784C721B730BF9928D038547D209E1972D331D`,
  `34B70E0B76C7F22BE6146B198590382EB9B007F00305410554B00179044A8E19`,
  `CF2D5E77057539F5A587BEB78B8867E8754A43E0D25B7281828D73F4B3DE0040`,
  `4E24BB0A7C0CA10EF99D8292B6DF391059CEABC23E4BDF12137F1D0F94E13BEA`,
  `A38BC44BC20FA4210C84060AE5BD291875BC53D42DF87EDC8CA56C29029A5AAF`,
  and `E406ADFF2F94AAE56BEE754ED360938602194E66E2F07FE8C7C4FEC14BA5742E`.
- Source-critical choices: French `génériquement net` is rendered
  `generically unramified`; the three odd-dimensional quadratic forms in §3.7
  are preserved exactly; the final printed `dim X <= r-2` is transparently
  corrected to `dim check X <= r-2`, since Corollary 3.5.0 and the criterion
  immediately cited require the dual variety. The English note discloses that
  correction. Render review also corrected the side of the `psi_1` label in
  diagram (3.5.2), removed a stray comma from `\mathcal O_V^{r-n}`, and restored
  the missing backslash in `\longmapsto`.
- Final three-pass cumulative build:
  `build/c099_expose_XVII_through_section_3_7_r3/SGA7_II_English_source_first_workpass.pdf`,
  145 A4 pages / 1,227,948 B / SHA-256
  `6770B0738DCF72A7DC5FB4683CD0B7A0BAA2C23D39838FE8ED04447C6BFA040F`.
  Passes 2 and 3 have identical console SHA-256
  `B109D9277A47D20CD87DC68B98FFD86DEDC2DBC00C6B7CA94E0C782A672B3DEE`;
  final log 41,299 B / SHA-256
  `F7AC36EE6E0A2826D0E834ECC325CF3BA8C74DF2F3D35902B222F4E0BB70D6BC`,
  with zero critical diagnostics. The cumulative master is 6,959 B / SHA-256
  `7972F552881FB39A08B3CB5515EF3293E1FB33957534589D4E9E2AB221CF41CA`.
- Final 600-dpi English renders pages 140–145 have SHA-256
  `DD4FEA958ED2765B7F81198C38D250D894313946DFB8ADDCF0619366D841DF68`,
  `E011C6C2ACF0BFB694C48D329197A3A5B2A10B62A8AA70904DE114E664D50DF7`,
  `3DA01451E0ED985D401A440FDED911934E998A9710B552511DB3084858070544`,
  `42F35ADF6386BE8EDC6033D94698B1E41677CF5A13A15575F7AC746DDF44C815`,
  `F0B725994520B02E4D23B4D7102B85B09304C01050C8E6650ACDB3750FAD4F20`,
  and `A0633568028EC19982C4952B681777E5ABE16D340CAE07DDBB072BA357A913B5`.
  Lead review PASS: the local-coordinate formulas, diagram (3.5.2), proof
  seams, correction note, quadratic forms, and page breaks are clean and
  unclipped.
- Exact continuation cursor: scan index 243 / folio 236,
  `authority_snapshot/source/expose_XVII_body.tex` line 590, §4, “The
  general case.”

## 2026-08-01 — Exposé XVII §4 through references complete

- Added and integrated components 100–108. Their exact identities are:
  - 100, 2,700 B, SHA-256
    `AA9BECAA8A34736D33DB78EB531986CF837899343885D9D88E34B166C51D2744`;
  - 101, 2,933 B, SHA-256
    `F496B6A9B1A26B4B3201C566C2010A242B569FECA05C36D736FB67369429156E`;
  - 102, 2,801 B, SHA-256
    `B5B5C662DB6D467004C37B844388480F5ACC208D9076A71C3A7CFC1A645FC066`;
  - 103, 1,950 B, SHA-256
    `C54317216566590D8B1E298F102C5959E8057BD7A4D6B079C47C85EE5B605BBF`;
  - 104, 3,565 B, SHA-256
    `6877B70F8976DDAED098BEA9621B0C45ACE39774910616724B50215D3E9B7F5E`;
  - 105, 2,604 B, SHA-256
    `E68E57814F750076CDA0B7B59619A6A761D77E3B387F8F8EAC944AB9B6F2CE60`;
  - 106, 1,897 B, SHA-256
    `4482840CE7D09B4007C7A39983DCAD7F8E689C103BF4A554C84F2535C4D48EB4`;
  - 107, 2,424 B, SHA-256
    `4204CAEF64B946411B82225CC221718D9BBA12E68CDAF5868F92F116A800E183`;
  - 108, 4,671 B, SHA-256
    `5338343492EDC4B8CEAB40575094096F9CFAFA0A1F5528E347EAF6A8A9F63742`.
- Personally inspected authority pages covering scan indices 243–260 at 1100
  dpi. The displayed formulas were decisive at that scale. In particular,
  (5.3.9) visibly mixes i and j and prints an impossible output coefficient;
  the two immediately preceding pushforward identities force U_(a-1).
- Source-critical corrections are disclosed in both languages: 3.8.1/F2 to
  3.7.1/F1; both ambient Veronese dimensions; restored 4.1.4, 4.2.5, and
  4.2.6; x2 and A_(1j) in Proposition 4.3; O_X in (5.1.3); dim dual-X in
  §5.2; the second 5.2.6 distinguished as 5.2.6-prime; (5.3.9) corrected to
  U_(a-1); the missing upper bound a restored in (5.4.7); and the sign in
  (5.6.1) retained as (-1)^n, as forced by (5.5.1) and confirmed by (5.7.3).
- The frozen French witness remains byte-preserved. The parallel corrected
  French workpass is at `french_source_corrected_workpass`. Its Exposé-XVII
  body is 71,321 B, SHA-256
  `0F4CE887C69305B377053D8D71E05D53C65F951FF84A6DF2BACFC8965B68A6A1`;
  the 17-entry correction register is 3,008 B, SHA-256
  `2742091386D09D9EF1CF13619C81136B1D3580789F3FECDFD18472A81CBC15CE`.
- Final cumulative build:
  `build/c108_expose_XVII_complete_r1/SGA7_II_English_source_first_workpass.pdf`,
  155 A4 pages / 863,544 B / SHA-256
  `BBEDE9430276AAE4A8E81C212850FC3E6C77F3D3D037B2F8E0EEAAA99EAD2640`.
  Three passes exit 0; pass 2 and pass 3 console SHA-256 are both
  `BEF896EE31D33858E1E924D06401BE1F39D3D3DB354D0F0637A2FBFC277BCFE5`.
  Final log SHA-256 is
  `9923B6FDF997832E72B87F7C17192CD181079FA560C69C6FEF47F55109EA535D`,
  with zero critical diagnostics.
- Lead 600-dpi review PASS for cumulative pages 148–155. The new equations,
  correction notes, long underlined statements, footnotes, general-base
  notation, and terminal reference page are legible and unclipped.
- Exact next cursor: scan index 261 / folio 254,
  `authority_snapshot/source/expose_XVIII_body.tex` line 1.

## 2026-08-01 — corrected French workpass build verification

- The frozen French authority snapshot remains unchanged. The separate
  `french_source_corrected_workpass` was checked with its intended pdfLaTeX
  engine after the 17 recorded Exposé-XVII corrections. The inherited master
  uses the pdfTeX-only `\pdfinfo` primitive, so XeLaTeX is not an applicable
  build test for this source.
- pdfLaTeX exited 0 and produced
  `french_source_corrected_workpass/build_check_exposeXVII_repairs_pdflatex_r1/SGA7II_French_Source_Transcription_Working_X-XXI_Partial_20260731.pdf`,
  201 pages / 1,379,048 B / SHA-256
  `D7C573FE71C81ED8F2864141DCBB7CB34B5EE9847949D1F92EB0CD40631C4816`.
  The log retains inherited underfull/overfull diagnostics, but the corrected
  Exposé-XVII body compiles without a content failure.

## 2026-08-01 — Exposé XVIII opening and §1 complete

- Personally checked authority scan indices 261–264 at 1100 dpi. The text and
  formula details were decisive at that scale; no ambiguity required artificial
  higher-DPI escalation.
- Added component 109,
  `source/components/109_expose_XVIII_title_introduction_and_section_1.tex`,
  5,921 B / SHA-256
  `97690834583AAF811B5D9CDCD0B197057F96A8002D6D1A77118D5B8045BD46E2`.
  It covers the title, contents, introduction, and all of §1.
- The authority exposed four French-workpass entries: the frozen
  `succintes` transcription was repaired to printed `succinctes`; the
  contents agreement was corrected to `hypothèse ... vérifiée`; and the
  printed (1.2.2) upper bound `n`, degree `q-2-j`, and missing
  parenthesis were corrected to the `r`, `q-2j` formula forced by
  the rank, defining map, and proof. The English discloses the mathematical
  correction in a footnote. The corrected French Exposé-XVIII body is
  178,901 B / SHA-256
  `FB8FF337F2750524533176206F17C12217470565DE5D4146DF19A014EABE2CD5`;
  the 21-entry correction register is 3,725 B / SHA-256
  `3B256AD453BB59D95B2106FABBFBA5AD85680ECD2E6A55A26FCAF975FA528FC6`.
- English three-pass cumulative build:
  `build/c109_expose_XVIII_through_section_1_r1/SGA7_II_English_source_first_workpass.pdf`,
  157 A4 pages / 874,350 B / SHA-256
  `ECA82C27F4C4AF336580607534D5EE1CD258471B3C6A3FAD8FAF0C48C8DD56B5`.
  Passes 2 and 3 are byte-identical (SHA-256
  `0C034FDF3AD1ABCFB73E3A8576A91929429EB0F15C4C560E681776824E4192D4`);
  the final log has zero critical diagnostics. Lead 600-dpi review of pages
  155–157 PASS: the title/contents, theorem seams, corrected (1.2.2),
  filtration formula, footnotes, and page furniture are clean and unclipped.
- The corrected French master was rebuilt with pdfLaTeX after these repairs:
  201 pages / 1,379,028 B / SHA-256
  `EB4EEA28CA0A7BDFE92C330290B27A36E7ABD17B9B061D98C094EDEB047B93B3`,
  with zero fatal diagnostics.
- Exact continuation cursor: scan index 265 / folio 258,
  `authority_snapshot/source/expose_XVIII_body.tex` line 113, §2.

## 2026-08-01 — Exposé XVIII §§2–3 complete

- Personally checked authority scan indices 265–278 at 1100 dpi. The source
  text, formulas, and diagrams were decisive at that scale. The small local
  intersection-length abbreviation in the proof of Proposition 3.2.10 was
  additionally checked in a targeted 5000-dpi crop; the print reads `rg`,
  while the argument requires the local length `lg`/`length`.
- Added and integrated the following components:
  - 110, 3,925 B, SHA-256
    `49CDA9EA419C6CC5D010C6234E1375D555796832D5EA09E4CDDE017173764083`;
  - 111, 5,281 B, SHA-256
    `0E210E8F182A80D76B37EC74990025E7CA53EB80BC9F1A33351BC87FBCC9380A`;
  - 112, 4,330 B, SHA-256
    `13F14163AB92E3B618672F1FB2FD97529E44C41A786139907F033594EF6C25B3`;
  - 113, 7,225 B, SHA-256
    `3ECA2D0E3313047D983A46D2AB7D3D50F39FB607D53C9BBD4055394DA9717D59`.
- Components 110–112 cover all of §2 through Corollary 2.3. Component 113
  covers all of §3 through Remark 3.2.12. Every source diagram is rebuilt as
  native TeX. A first c112 build exposed a purely mechanical ampersand-catcode
  failure in the resized (2.2.25–26) `tikzcd`; the component was corrected
  copy-on-write with an explicit ampersand replacement and the next three-pass
  build succeeded.
- Lead 600-dpi English render review PASS for pages 159–164. The review covers
  every new commutative diagram, the spectral-sequence differential diagrams,
  the (2.2.25–26) ladder, the Hesse-pencil triangle, all formula tags and
  source-correction footnotes. It caught and corrected the side of the
  $\operatorname{pr}_1$ label in (2.1.6.3) and the placement of the preceding
  footnote before the final builds.
- Source-critical repairs are propagated in both languages. The French
  workpass now records 37 XVII–XVIII entries, including the numeric initial
  index in §2.1, the Leray abutment in (2.2.1), $E_{r+1}$ in (2.2.13),
  $d_{r+1}$ after (2.2.14), the $F^pH^p$ denominator, the degree shift in
  (2.3.1), the §3.1 dimension and closing parenthesis, the scanned exponent
  $n$ in (3.2.3–4), $\rho$ in place of the undefined printed $S$, the Hesse
  condition $\mu^3=-1$, and the local intersection length in Proposition
  3.2.10. The frozen French snapshot remains byte-unchanged.
- Current corrected French Exposé-XVIII body: 180,699 B, SHA-256
  `A16D1AD0A32761564C3CF64E229D9B8B1246DF15084BB3D5833854D98124B527`.
  Correction register: 6,570 B, SHA-256
  `9CB8FF0423710AD4F5044B8FC22D727C7EB0E8360BAFC32E23FDCDFF1ED6E488`.
  Two-pass pdfLaTeX build exits 0 and produces the 201-page, 1,379,810 B
  corrected French control PDF with SHA-256
  `EC260F358C7FCD2B2256AA5F22277DB7C6B57C98923855529BC5FF7D28B713A1`;
  no fatal diagnostic is present (two inherited overfull boxes remain).
- Current English master: 7,812 B, SHA-256
  `5DEFECFEAB648CC8F3873B6D06DC0422421F7052D6A6AB83D4CCBDA54224AA2C`.
  Current cumulative PDF:
  `build/c113_expose_XVIII_through_section_3_r1/SGA7_II_English_source_first_workpass.pdf`,
  164 A4 pages / 907,128 B / SHA-256
  `EF7FB95B2B429CEE0149700761CB8F0B3C7F79CE2DFE69E81516E37E154C23C5`.
  Three XeLaTeX passes exit 0; passes 2 and 3 are byte-identical at SHA-256
  `51CB9599D248A97AEB8BDFC2CC18024F7DFFAB9073DF9615F03AB8B7CE6D9129`.
  The final 37,537 B log has zero critical diagnostics and SHA-256
  `39D44BC5888FEC79E04AB45C8C5B8131A93E98979039BB1CBAB6E85EBE02121A`.
- Exact continuation cursor: scan index 278 / folio 271,
  `authority_snapshot/source/expose_XVIII_body.tex` line 658, §4.

## 2026-08-01 — Exposé XVIII §§4–5.1 complete

- Personally checked authority scan indices 279–288 at 1100 dpi. The diagrams,
  arrow labels, formulas, and proof text were decisive at that scale; no small
  source feature in this tranche remained ambiguous after direct inspection.
- Added and integrated components:
  - 114, 5,771 B, SHA-256
    `189C25FA2E970D58E9F67C5535590044E0BE3E4A475B9C3530B07D1778300CF1`;
  - 115, 5,608 B, SHA-256
    `343B9DAAA8FCA79951C84CFBFD1B76FA4939B6C979E824B05FBC849ECE7AB651`;
  - 116, 4,141 B, SHA-256
    `6BF02CB5561C4E80CC36682210253DDA322E550FBC82B41430D398F6BEAF580D`.
  Components 114–115 cover all of §4; component 116 covers all of §5.1.
- Source-critical readings were propagated to the parallel French workpass
  while the frozen authority snapshot remained byte-unchanged. The correction
  register now has 52 entries. In §4 the workpass restores the lower inclusion
  label $j$, the necessary minus sign on $g_*i^*$, the missing isomorphism and
  degree marks, and the formula punctuation. In §5.1 it restores the visibly
  printed lower $j$, corrects the source-level $h^*/h_*$ Gysin defect, fixes the
  coefficient twist and propagated minus sign, and repairs the corollary's
  inconsistent $h^*/k^*$ prose and projection-formula parenthesis.
- Current corrected French Exposé-XVIII body: 181,968 B / SHA-256
  `FA8058C35033E6A519A64F8278151805C70BCA4748B08145B9E28862B1F4224C`.
  Correction register: 9,437 B / SHA-256
  `813C526BE3E1EB8E7A6EBDFE05F3C15CDC3CEC5F8E057D93458EC000A0011A04`.
  Two pdfLaTeX passes exit 0 and produce the corrected 201-page French control
  PDF, 1,379,974 B / SHA-256
  `60821C198FE1911C0D8F317204D65F301698093BBBD5E3A53F53551536C25418`.
- Current English master: 7,994 B / SHA-256
  `B877E73B60E579276EBF785B96B082AE25081713B19431B030A6832AB54B8013`.
  Current cumulative reader:
  `build/c116_expose_XVIII_through_section_5_1_r1/SGA7_II_English_source_first_workpass.pdf`,
  170 A4 pages / 930,531 B / SHA-256
  `A03A363AC659E628A5AFE06E5CF9F84C5EE23CC57EB8F01CBB658189D7817D75`.
  Three XeLaTeX passes exit 0; passes 2 and 3 have identical console SHA-256
  `55D343D164F7019C69FDEE6FFDFE5645A1C42A938DFD29EF7F5707FC9B6D5D8A`.
  The final 37,396 B log has zero critical diagnostics and SHA-256
  `119143E4EE104CF1C1C762919AC7F8E772538411EDFF53624D5B4C17DE598D1A`.
- Lead 600-dpi English render review PASS for pages 165–170. Every §4 and §5.1
  native diagram is legible; all hooks, directions, labels, signs, degree
  shifts, underlined statements, proof seams, and terminal formulas are
  visible and unclipped. Final render hashes for pages 168–170 are
  `FBC7F5DFF27B6F672ECE663054F5526E181427F517F6A6A040177C93AFC3E61C`,
  `1682A2D092BF36A0B8AE0AC3CA09CD1C913EC5E575ABD7F92613B206D81FAAB7`,
  and `C2744A4C3C12362B5FA93462C2CBDF290A7D646D6EBE4823F593B35BD6DD5E4E`.
- Exact continuation cursor: scan index 288 / folio 281,
  `authority_snapshot/source/expose_XVIII_body.tex` line 1132, §5.2.

## 2026-08-01 — Exposé XVIII §5.2 complete

- Personally checked authority scan indices 289–294 at 1100 dpi. The four
  native diagrams, all arrow labels, exponent signs, Tate twists, and proof
  references are clear at that scale.
- Added and integrated component 117,
  `source/components/117_expose_XVIII_section_5_2.tex`, 7,303 B / SHA-256
  `43CC949CDC5B3A63B2443E8411F8CE19373F4F828D17EC9E2A4633498D4644DA`.
  It covers all of §5.2 through Corollary 5.2.7.
- Ten additional French-workpass dispositions close the missing parenthesis in
  the definition of $L_S$; correct the doubled primitive-part twist; regularize
  $m/\tau$ notation and source grammar; restore formula tag (5.2.4.7); correct
  its target twist; repair the nonexistent (5.2.5) citation; restore degree
  $n+i$ in the surjectivity square; replace $H^{ii}$ by $H^{2i}$; and point the
  universal-family proof to Lemma 5.2.6. These readings follow directly from
  the displayed operators, not from OCR inference.
- Current corrected French Exposé-XVIII body: 181,971 B / SHA-256
  `758B6994E0015EE073FC4020A39752990C9A0E46A4960C80847CEEEF61E842CD`.
  The 62-entry register is 11,299 B / SHA-256
  `1862EB2C08B7CE833D6BA213CB7C22F43CCC0E42B2A2C1C2D95810A9728EC074`.
  Two pdfLaTeX passes exit 0 and produce a 201-page corrected French control,
  1,379,945 B / SHA-256
  `17BB792E66D08D5B1C0EF09443F2B31248E7F2DE3AF648EDD486D21D2A70062B`.
- Current English master: 8,042 B / SHA-256
  `ED805804C8F425898E4703753A61C915FF3821D692847AF05D5B747DE67DD58B`.
  Current reader:
  `build/c117_expose_XVIII_through_section_5_2_r2/SGA7_II_English_source_first_workpass.pdf`,
  173 A4 pages / 945,380 B / SHA-256
  `9524A076012770829272C963B41DD3890E0B1D7847A87BAE60B7A1859AC705CB`.
  Three XeLaTeX passes exit 0; pass 2 and pass 3 console SHA-256 are both
  `3BC1C216A25BDF605BE13B925413F7D61057C9C84C1E1B4C4FD3271D2F01476B`.
  The final 37,460 B log has zero critical diagnostics and SHA-256
  `A81141B9734BD34394D3C15DB82693BBC4FD8BCCF5738B3850F78CA5AE03FB01`.
- Lead 600-dpi render review PASS for pages 170–173. Final render hashes are
  `CB48C58D4CE584FFA8917A41DD367CBD2BAC640BF009D0D5CD1A0A37968230FC`,
  `4AC89B5F5BB93A696D478E822F1986B980EF70091EE58475369ED45683C4BCCB`,
  `86D54612183736903AB0A005E25CACEF3EE2BAC8D436DB29D07AAA75B8755239`,
  and `0A8D893B2BE1A221BD7C4BEDD51A98CDDC9CD50AE0D7328B984C8710BA098304`.
- Exact continuation cursor: scan index 294 / folio 287,
  `authority_snapshot/source/expose_XVIII_body.tex` line 1328, §5.3.

## 2026-08-01 — Exposé XVIII §§5.3–5.5 complete

- Personally checked authority scan indices 295–298 at 1100 dpi. All prose,
  functor symbols, Tate twists, and the orthogonal-complement display are
  decisive at that scale; no ambiguity required higher-detail escalation.
- Added and integrated:
  - component 118, `source/components/118_expose_XVIII_section_5_3.tex`,
    2,001 B / SHA-256
    `67AB3696F38F547AB7B309EA596D8E7D6102D62D7C3015B14037E8FEDC936959`;
  - component 119,
    `source/components/119_expose_XVIII_lemmas_5_4_and_5_5.tex`,
    3,425 B / SHA-256
    `3FFA70336297178D44F8CF730DAAC9EDF99182F32324AE0FFF9AE516934AA040`.
  These cover condition (A), Lemma 5.4, the vanishing-cohomology sheaf, and
  Lemma 5.5 continuously through frozen French line 1421.
- Three further parallel French-workpass dispositions restore the missing
  parenthesis in $f^*c_1(\mathcal O_X(1))$, replace the frozen
  transcription's $\rho^*$ by the directly scanned $\rho_*$ in (5.4.3), and
  correct the printed agreement “la flèche … est injective.” The frozen
  French snapshot remains byte-unchanged.
- Current corrected French Exposé-XVIII body: 181,970 B / SHA-256
  `2DF322CF3BC727BE15D3C817B2794244DB769B56BE0A134EE21BF62CB16EDABD`.
  The 65-entry register is 11,775 B / SHA-256
  `8BC03ED1E446FE075CA589CEB457C1E7FAA390A97B371B7B1C422243C734B10D`.
  Two pdfLaTeX passes exit 0 and produce the 201-page corrected French control,
  1,379,920 B / SHA-256
  `6589E28B1FF46DF06CF6D9D4822AF5B821698FED4E5D77ED14DD6A0BCE5AAA3B`;
  only the two inherited overfull-box notices remain. The first r1 invocation
  from the parent directory is preserved as a build-path failure; r2 is the
  valid build.
- The first English c119 build exposed a single malformed TeX array-line
  delimiter in (5.4.4.1) and is retained as diagnostic history. The corrected
  r2 build succeeds in three passes. Current master: 8,145 B / SHA-256
  `455732B0AD66FB27AEC6712C093A9C533124F9B2F15F2C6B000F8F0C4365A5EA`.
  Current reader:
  `build/c119_expose_XVIII_through_section_5_5_r2/SGA7_II_English_source_first_workpass.pdf`,
  175 A4 pages / 954,807 B / SHA-256
  `576180E62C776BE7F40D7593CA1588EC9E6A9F5E43D32B25ED76AD29773E1272`.
  Passes 2 and 3 have identical console SHA-256
  `F5922E27D1698430DD3EB06EC258F31B25A1B50D98E0419F14267DC8A8F8CF7D`;
  the 37,571 B final log has zero critical diagnostics and SHA-256
  `60013A477A7A83571DCDF8F3F5AC9B057ACB6E9E221F3763887BA7B043B33584`.
- Lead 600-dpi render review PASS for pages 172–175. The seam, all statement
  underlining, formulas (5.3.1.1)–(5.5.2), the wide
  orthogonal-complement brace, and page furniture are clean and unclipped.
  Final render hashes are
  `86D54612183736903AB0A005E25CACEF3EE2BAC8D436DB29D07AAA75B8755239`,
  `DB3CD62968509EB7314F65264CB93CCCCD48C27AB017529E1D2DED3DE963326A`,
  `C3332578EF63FCBF2346979CB0085CF6A5FACC943273D390F0502B5BCDC95D55`,
  and
  `33E54E87D7A0068D9370271EFC48DB5A5CB60DC6D08F679808EEC6DB5E9CF517`.
- Exact continuation cursor: scan index 297 / folio 290,
  `authority_snapshot/source/expose_XVIII_body.tex` line 1423,
  Theorem 5.6.

## 2026-08-01 — Exposé XVIII §5.6 complete

- Personally checked authority scan indices 298–305 / folios 291–298 at
  1100 dpi through Corollary 5.6.10. The text, indices, arrows, label sides,
  and punctuation were decisive at that scale. The retained targeted locator
  crop for the dense formula (5.6.5) is
  `qa/authority_expose_XVIII_1100dpi/page-300-formula-5.6.5-locator2.png`,
  SHA-256
  `FAA0DA47EAF143DA187082415ADC897563B4ACF01AC8DFE1891A2375F64A3B4C`.
- Added and integrated:
  - component 120, `source/components/120_expose_XVIII_theorem_5_6_and_computation.tex`,
    5,327 B / SHA-256
    `6FFFA8AC27C515C9C438C3CD6F2C72157F520AF03FC2A78046115260AB14A7E7`;
  - component 121, `source/components/121_expose_XVIII_theorem_5_6_8_first_proof.tex`,
    4,449 B / SHA-256
    `48F91F34CDCE8EFC88CF7F6DF1FD14D35896B83765F55F4FA1873EF29F7FE904`;
  - component 122,
    `source/components/122_expose_XVIII_theorem_5_6_8_completion_and_corollary.tex`,
    3,438 B / SHA-256
    `A99803D8048237CD9FE1CE44B62094E3895E23AF63D32F5093723C6DBB014909`.
  Together they cover Theorem 5.6, the full spectral-sequence computation,
  Theorem 5.6.8 and its proof, and Corollary 5.6.10 through frozen line 1688.
- Parallel French-workpass entries XVIII-049–XVIII-058 correct the theorem's
  hypothesis reference to condition (A) of 5.3.5; the Leray abutment
  $H^{p+q}$; zero misread as the letter `o`; the parenthesis in (5.6.2.5);
  $\rho_*$ in the proof; the coefficient parentheses, target parenthesis, and
  missing plus sign in (5.6.5); the kernel reference to (5.6.5); the missing
  $\mathcal O_X(1)$; the forced degree in (5.6.8.8); the $d_2$ target and
  $R^n\rho_*$; the continued primitive direct sum; and the missing $E_2$
  symbols in (5.6.8.15). The frozen French snapshot remains unchanged.
- Current corrected French Exposé-XVIII body: 182,006 B / SHA-256
  `7F9969F96E7BC131E1B507B342DD5AE629AEACAAA2531C721186685DD5ED0E33`.
  The 75-entry register is 14,147 B / SHA-256
  `D22FE679F89181B25E240C2ADC51E37F69642A1451C1E22C943092B1443B88E8`.
  The pdfLaTeX check produces 201 pages / 1,379,882 B / SHA-256
  `85482FD09737A258E96F26A5886D79B5DBB23341EAE8BF18B780A21D81FF99E7`;
  its 37,790-byte-equivalent source build layer has no fatal diagnostic, and
  the French log SHA-256 is
  `A075DD5D3F01CCAC83D5090D836731BBD1CB0E273333C2DB90A0F50F76C750BB`.
- Current English master: 8,346 B / SHA-256
  `348F2AD76AC527FF666712BF0D2D5AB0C0FAA4E95E16E28C8A810AE112F3D6C1`.
  Current cumulative reader:
  `build/c122_expose_XVIII_through_section_5_6_r2/SGA7_II_English_source_first_workpass.pdf`,
  179 A4 pages / 977,832 B / SHA-256
  `786E90338798BEF4057CF938B9D0C2D4B870E309196CF95FD67757E16F50C8AA`.
  Three XeLaTeX passes exit 0; passes 2 and 3 have identical console SHA-256
  `AEDF8E69E2113982A04E7CADC3FAD6813664D78AA593C13FB84C38CA1D71AA0D`.
  The final 37,790 B log has zero critical diagnostics and SHA-256
  `8D30652274BB335429F9C4D46FC5C0A5F6EC4F947DAE3139B54D66EF313BE85D`.
- Lead render review PASS for pages 175–179. The r1 review caught one strict
  layout mismatch in the commutative square on page 178: the left vertical
  $d_2$ label was on the wrong side of its shaft. Component 122 was repaired
  copy-on-write and the r2 page 178 was rendered at 600 dpi and personally
  checked against the authority. Final page-178 render: 874,176 B / SHA-256
  `1EC6B3F76F23A3C0E5220EDBB82F942226B647CFDC6FF4C47D81174F06C304FA`.
- Exact continuation cursor: scan index 305 / folio 298,
  `authority_snapshot/source/expose_XVIII_body.tex` line 1690,
  Theorem 5.7.

## 2026-08-01 — Exposé XVIII §5.7 complete

- Personally checked authority scan indices 306–308 / folios 299–301 at
  1100 dpi. Source-image SHA-256 values are
  `DE7D7E870DBDC0DC7AA20E2EE85BA7E3E1A8376F8E5BA9E0BA44C714B3E5496B`,
  `46559338C93A55ECE4CD6E82D03346B612B8646D7AF841050259196D1BCD0FBF`,
  and
  `47A4CBFA5A6521247FCF3D2C3CAD62D065E980227CABCED72D4E89BF37BA396F`.
  A direct 1100-dpi crop of the maps (5.7.2)–(5.7.6) is 715,003 B /
  SHA-256
  `31A800B05B31929A5D90F477437E4A0C053403AD427409DD78FB9957F04137EC`.
- Added and integrated component 123,
  `source/components/123_expose_XVIII_theorem_5_7.tex`,
  4,585 B / SHA-256
  `25D7123DE43DE2EDAF9520B1C1D7CAC2B3CAA2E806E2661420BDC3F98FA51307`.
  It covers Theorem 5.7, the full primitive/vanishing decomposition proof,
  native Gysin square (5.7.9), and Remark 5.7.10 continuously through frozen
  line 1797.
- Parallel French-workpass entries XVIII-059–XVIII-063 restore scanned
  $h_*$ in (5.7.2); replace the printed $2^*$ by the inverse blow-up map
  $i^*$ in (5.7.6); replace printed $F^2H^N$ by $F^2H^n$; restore the
  Tate twist $(-1)$ and remove the extra parenthesis in the Gysin display;
  and use the defined projection $\wp$ with the degree-$n$ primitive
  summand in (5.7.9). The frozen French snapshot remains byte-unchanged.
- Current corrected French Exposé-XVIII body: 181,997 B / SHA-256
  `108C227C8335E3F70DC278FFC2BECE9F7528DD7E6C4ACA2817D8286A0B35E6FE`.
  The 80-entry XVII–XVIII register is 15,368 B / SHA-256
  `3C5E79930D502A56049035C5954DB8AFD8484FE1D6EC71F97958DE4BE4071B2A`.
  The two-pass pdfLaTeX check produces 201 pages / 1,379,686 B /
  SHA-256
  `BC3C24CA8BC4F6FA1BA929EE0DCCE607AD83C81AE4E5E3DE6209035E7F206CE3`;
  fatal diagnostics are zero and the final log is 41,079 B / SHA-256
  `330F90241BCFB39DFB7714C6A22888DFD8ED020AC6FA9E32958D542D3DDBFFDD`.
- Current English master: 8,394 B / SHA-256
  `C9C00A1ECA9A644160FF62592E75B9AE1A7EC762A752F681910F439749019589`.
  Current cumulative reader:
  `build/c123_expose_XVIII_through_section_5_7_r3/SGA7_II_English_source_first_workpass.pdf`,
  181 A4 pages / 984,749 B / SHA-256
  `79525713FB60872894E9CD4AEF05141EA52D5F3A4451F92DB7BB0E8BCE5B4937`.
  Three XeLaTeX passes exit 0; passes 2 and 3 have identical console SHA-256
  `DB7BDBC128411D4E6433166C404AFDD3CBA36D4690A20DE09240C3E549F6B75B`.
  The final 37,807 B log has zero critical diagnostics and SHA-256
  `35CF352E6B2745F83A02F6B323F8722AD372D6E0907C837F1C59DDFEE03AF669`.
  An earlier invocation that passed the output variable literally created a
  source/`$out` build-only subtree; the exact generated subtree was
  path-checked and removed before the valid no-overwrite r2/r3 builds.
- Lead 600-dpi render review PASS for pages 179–181. The r2 review prompted
  one editorial layout refinement: source-correction footnote marks were
  attached to their governing prose rather than left between displays. The
  r3 render preserves the authority's hook, four arrow directions, two
  isomorphism marks, label sides, and terminal punctuation in (5.7.9).
  Final render SHA-256 values are
  `ADCF33719501512E1912B97F78D3DDD96217364641C80F62D7098A7C07B2D7AE`,
  `840E35882287FD35A7163736E47B3C523032C215F97FF940041E2B13CECE3AD1`,
  and
  `04153B23B559D9FEA13EF6BBBC9642EF485EA1000CD570D6FD75CADA21E9E1DC`.
- Exact continuation cursor: scan index 308 / folio 301,
  `authority_snapshot/source/expose_XVIII_body.tex` line 1800,
  §5.8.

## 2026-08-01 — Exposé XVIII §5.8 complete

- Personally checked authority scan indices 309–318 / folios 302–311 at
  1100 dpi; no feature in the final §5.8 pages required an artificial
  high-resolution escalation.  Source-image SHA-256 values for indices
  315–318 are
  `C9641FEB8C5A1CDF677FF5E71684907679BFB41342D5B2CBAB2BC9471EC72C27`,
  `3A3ED93614DFDDE66BBB97AB85FC890604771A8DA8FFF13034926FFC19AF04F3C`,
  `BD2AF940057180CB7A4C4F8768B8028E7F677A7A2762DC58426984094BCAF107`,
  and `FB9E46FA13FC63C75FCF45173859CBF78C6E8C6CF6A10D5E38BFB64DE1740B56`.
- Added and integrated components 124–126. Their exact SHA-256 identities are
  `A9A645DF2041578536082A7D249CF40941F4FA1264877B2E82DACFB16338FF4F`,
  `E13EF15958C2065462565271E677B2A8FA63DFC71DB8675E32F12DD7331DC3F4`,
  and `32E2DA494C1AD76603F07E6C9444A2B9B9DA947AC6B95F30069867299E445285`.
  Together they translate §5.8.1 through Corollary 5.8.7, including every
  displayed formula and five native diagrams.
- Parallel French-workpass entries XVIII-064–XVIII-079 repair the malformed
  spectral-sequence and trace formulas, restore omitted indices, twists,
  delimiters and tag (5.8.7.3), disclose the contextually supplied damaged
  `[U^n]` label, and put the four leftward-arrow labels on the scanned sides.
  The frozen French snapshot remains byte-unchanged.  The corrected French
  body is 180,211 B / SHA-256
  `2B7699B63ECA5BDBA42FBFE81C1EDE1AB9EEA51E35D136F51B8BF5A8ED963DCD`;
  the 96-row register is 19,220 B / SHA-256
  `E563EBB46CD580617E405A43525E1D02275BB5E2999CFA57B7F30D2B672E2070`.
- The corrected French pdfLaTeX check is 201 pages / 1,379,337 B / SHA-256
  `84D333961BAD2B8ADD193C9C096CFCEF2A62D05176DD6F650C36EA760D11FA8B`;
  its final log is 40,809 B / SHA-256
  `C1BC77537B2EBE4C386762AECC158C55C47C24F7AE7D3AE971ED2F9A301AF697`,
  with zero critical diagnostics.
- Current English master is 8,605 B / SHA-256
  `CEFE21A1570970C517F77C0291F676CC61636341FB56D8B1A11CB7DC73FB34B0`.
  Three converged XeLaTeX passes produce 186 A4 pages / 1,007,834 B / SHA-256
  `65D8B29B948CA866F8688AB6E1604C945178EDEFB42A0006BB3E9AE7C10B0037`.
  Passes 2 and 3 are byte-identical at SHA-256
  `5AE097840C305962510124872761C98410FAAD6FA0AE68BB6964A919CE44B5BC`;
  the 38,054 B final log has zero critical diagnostics and SHA-256
  `1407E5D66C7692F43DA38D337E57B42E8576EEB063DD5B75C2EF5283FA281D8B`.
- Lead 600-dpi render review PASS for pages 182–186.  The r1 review caught the
  label sides of alpha_S, alpha_V, pi, and pi-mu; the r2 diagrams now match
  the authority. Final page-184–186 render SHA-256 values are
  `4195564B5BE3A01F69DA37FCBD15963998D9ABFB7CE0B6770E36BF73CDF7EB5F`,
  `B9DE5FA3F664B2DD1EEA12DA761E6881EBFB9E1985F1C884B4E075F33DD99AC0`,
  and `C1B48B35DFD990EA5833C52BC8AA3EC11AB35005503AC74577AEB52FB9350D21`.
- Exact continuation cursor: scan index 318 / folio 311,
  `authority_snapshot/source/expose_XVIII_body.tex` line 2284, §5.9.

## 2026-08-01 — Exposé XVIII complete through bibliography

- Personally checked authority scan indices 330–334 / folios 323–327 at
  1100 dpi through the terminal bibliography. The targeted 5000-dpi crop
  `qa/source_idx331_target_5000dpi/Number12_idx331_theorem66_symbol_5000dpi.png`
  is 428,627 B / SHA-256
  `71F1144C57DD5F3CC9EFAAF0B2EBD35DD9568DE77986B241BA3137270D3BA588`.
  It confirms that the circular “inertia group of delta_i” phrase is printed,
  rather than introduced by the frozen transcription.
- Added and integrated components 132 and 133. Their exact identities are
  5,958 B / SHA-256
  `A8DD0A75460C463CBB9F5D10BE1FF8E3AB4D816F551027C70870FEFFD03242C3`
  and 2,846 B / SHA-256
  `7CBB1DC2E0EC6BB05509C1639B5F51C379F7D708D4545C6DFACA8326F8E015C6`.
  Together they translate §§6.5–6.7 and the bibliography continuously through
  the end of Exposé XVIII, with the simple monodromy diagram rebuilt natively.
- Parallel corrected-French entries XVIII-103–XVIII-112 repair the reflection
  formula label and degree, coefficient-group delimiters, circular inertia
  phrase, generic-fiber ambient space, generated-group symbol, invariant-space
  formulas, dual-projective notation, variables in the irreducibility proof,
  and the two bibliographic defects. The diplomatic authority snapshot remains
  untouched. Corrected body: 180,944 B / SHA-256
  `751C9A6841137667BBFA948D2E6FB367755F2F6AD85463A4993EA3EB09B3F01D`;
  129-entry register: 26,451 B / SHA-256
  `3A51FDE3496C5E26EE55197DD8C0EA8D3142C2440A5AD3F9098F3B20E668135B`.
- Current English master: 9,049 B / SHA-256
  `E2CC89668DB33DF7FF78C18B0E425E549B5C5E4300A1C982F1A9846197B387B4`.
  Three converged XeLaTeX passes produce 194 A4 pages / 1,043,433 B /
  SHA-256
  `6ED0615A5E440A5F4C5C52B85BE4825C51DE9D1D0CCAFCCB165CB8462EA88DE6`.
  Passes 2 and 3 are byte-identical at SHA-256
  `1C286544F0FD2922B8DCE41C52F318C6000E78CDBAB94E6439E5CDCA111CB922`;
  the 38,487 B log has zero critical diagnostics and SHA-256
  `93604FB4F5BB1B8FE5ADD18AD18176C8D02F4B600B72230B8E78D9CC7728D291`.
- The corrected-French three-pass pdfLaTeX check remains 201 pages and is
  1,379,665 B / SHA-256
  `D158F20143FD6697551857DA1837561AD9C95904C00EA600D313A30C5044B439`.
  Passes 2 and 3 are byte-identical at SHA-256
  `A51A6128E78DBDCB41EE65DCBD25100326218AF6D05BF8771CA751A00A6620EC`;
  final log SHA-256
  `F0E521C298F4C708210DE861D171EEF7DD1FEAF37986331D5B359A96EA90B1BD`.
- Lead 600-dpi render review PASS for English pages 190–194 and corrected-French
  pages 164–168. The formulas, three correction footnotes, native L-shaped
  diagram, terminal punctuation, and both bibliographies are legible and
  unclipped.
- Exact continuation cursor: Exposé XIX opening, scan index 335 / folio 328,
  `authority_snapshot/source/expose_XIX_body.tex` line 2.

## 2026-08-01 — Exposé XIX complete; French-canon rule bound

- Personally checked authority scan indices 335–347 / folios 328–340 at
  1100 dpi through the terminal bibliography. Direct 5000-dpi monochrome crops
  controlled the fan on index 343 and diagram (4.3.1) on index 344.
- Added and integrated components 136–138. Their exact SHA-256 identities are
  `AEBF1869DB4E0A2262DE89D6E03579440209B79A6C0F8B15940F9CEDA079737F`,
  `F291D94319D1F95D915FF71FD65873131EB2189F92D8956C4D406E3F454DF5F9`,
  and `CDDE6FE8ABED48D6ABF4001BF750868B8AF64A47BF72A7EF7A7F91331284CB62`.
- Current English master is 9,306 B / SHA-256
  `92DB937A85822171588FA1DFE81CF473C926B9606EB04903A1CF576B6F24B69D`.
  Three converged XeLaTeX passes produce 203 A4 pages / 1,077,752 B /
  SHA-256
  `52E978B6DB2694B1B86CBA26592BF6F73B1C65EB5459A45802258DF2DA8BA596`.
  Passes 2 and 3 are byte-identical at SHA-256
  `766027A644035407849E7262FC17FB50467CB994E1842A22109F3E09740E4484`;
  the 38,825 B final log has zero critical diagnostics and SHA-256
  `1E2F0581C8138E47F8F09C18D95D805F819E4C3DA485789195F84B5B133147C8`.
- Lead render review passes English pages 199–203. It caught and repaired two
  detached source-correction footnote markers before the final r2 build.
- The explicit corrected-reading layer records 147 cumulative dispositions.
  Its Exposé-XIX body is 30,631 B / SHA-256
  `2A0D707764BD847BB1B20FDA8BB6EF838F21F29C3A34912615E0254DFB006904`;
  the 30,289 B register has SHA-256
  `B18ED4E93E2F016E9D5E10BE3C9B2B59F675E5CE92CBE471019707F6234B0AEF`.
  The corrected-French build is 201 pages / 1,379,918 B / SHA-256
  `7ADB2A93D8FCA4A48926DF7C875E6EEA5C225CB47904EA57B33F83D318CD04B6`;
  French pages 170–173 pass render review.
- Bound Floris's analogous EGA instruction to SGA through
  `FRENCH_CANON_AND_CORRECTED_READING_POLICY_20260801.md`. The archival French
  canon remains diplomatic; suspected print defects are catalogued externally.
  The editorial corrected-reading workpass remains preserved as a separate
  transparent layer and may not replace the canon silently.
- Exact continuation cursor: Exposé XX opening, scan index 348 / folio 341,
  `authority_snapshot/source/expose_XX_body.tex` line 2.

## 2026-08-01 — Exposé XX opening through Corollary 1.4

- Read and bound Floris's EGA French-canon instruction as the analogous SGA
  rule, then created the no-overwrite `french_source_diplomatic_canon` tree.
  Its copied source remains diplomatic; admission is page-bounded rather than
  inferred from filenames. The current tree has 20 files / 922,634 B.
- Personally compared scan indices 348--353 / folios 341--346 at 1100 dpi and
  the five diagram/detail regions at 5000 dpi. This triple-check established
  that several suspicious readings are really printed defects: (1.0.6)
  visibly has the apostrophe and wrong minus twist; (1.0.9) visibly lacks the
  differential prime; Lemma 1.1 visibly prints first bidegree $a$; Lemma 1.3
  visibly prints $b-2d_1$. The diplomatic body therefore stays unchanged,
  while `SOURCE_DEFECTS.md`, the editorial register, and the English notes
  carry the distinctions.
- Added component 139 through Corollary 1.4, 7,585 B / SHA-256
  `9CC9D79B82D4B21F7C2292971985EC1C2A0EBE8EB2AE5C845A17462020803F52`,
  and integrated it into master SHA-256
  `C1B2918B1DFA27DC2310F20608B5531D3210D130CE162AAFB83CDFE869051A4A`.
- The first render exposed two literal `Longrightarrow` strings caused by
  missing control-sequence slashes in (1.1.0)--(1.1.1). Repaired them before
  admission and rebuilt in no-overwrite r2. The final 206-page English PDF is
  1,089,370 B / SHA-256
  `03A2B8C6B63D12DB157CEB46E39A33333394FC8869C39CC8B38D5A0ACEFC4D05`.
  Three passes converge, pass-2/pass-3 console SHA-256 is
  `4FFCA1EB1B337BFCE03DCC83304A40C9664B99E92B32BDBBF3E67D2A93FDFEA1`,
  and the final 38,966 B log has zero critical diagnostics and SHA-256
  `CA586850D6888E38BFB0E8C46CAF79CA24EE46307F16513F92B9CFFBB1BFED60`.
- Lead 600-dpi render review passes final English pages 204--206: all five
  native diagrams, formula tags, corrected arrows, footnotes, punctuation,
  and vertical-label sides are legible and source-consistent. The unchanged
  final r2 pages 204 and 206 are pixel-identical to the already-reviewed r1
  renders; page 205 was re-inspected after the arrow repair.
- Added nine Exposé-XX editorial dispositions, bringing the corrected-French
  register to 156 rows. Its body SHA is
  `C9E36B7FFD4679B897718564E83D001EBC0ECBE459081BA985EBEFE3A2368051`;
  register SHA is
  `CFB1D089CB9270DB950CB0F215D8A3AD703C0FDC1F8246186EB4B9A476AA4EDD`.
  The corrected-French three-pass control is 201 pages / 1,379,858 B / SHA
  `BE5EF5FF30C28D3D404F3AA4E6CDD2128F1442BDDD2EDBF7AB564253A68C8F9A`;
  pages 174--176 pass lead 600-dpi review.
- Removed the accidental literal `source/$out` build directory created by the
  first native-command argument form; it contained only this turn's generated
  build scratch and is recoverable from the admitted r2 build.
- Exact continuation cursor: Exposé XX §1.5, scan index 353 / folio 346,
  `authority_snapshot/source/expose_XX_body.tex` line 232.

## 2026-08-01 — Exposé XX §§1.5--3.2; analogous French-canon rule applied

- Kept the attached EGA instruction as the controlling analogous SGA rule.
  The diplomatic French TeX reproduces the bounded print; actual inherited
  transcription deviations are repaired to the scan; suspected printed
  defects are catalogued externally and corrected only in the transparent
  editorial/English layer.  No aggregate French publication reader is
  implied.
- Personally checked direct authority indices 353--360 / folios 346--353.
  The scan confirms that `annexe`, capital $X$ and $Z_{\bar\eta}$, $f(s)$ and
  $g(s)$, joined `constantstordus`, `hypersurfacesde`, $E^{2n-1}$, and the
  blank relation in the Proposition 3.2 proof are printed peculiarities.
  Conversely, the frozen $g$ in (2.0.8), the omitted labels
  (3.1.0)--(3.1.6)/(3.2.2), and the omitted closing parenthesis are genuine
  transcription deviations and have been repaired in the diplomatic canon.
- Integrated components 140--142.  Their exact SHA-256 identities are
  `18137B09FCB7929375865DFA84508523CF9834BE71D4E494D5F58D23D4E9566D`,
  `A1495E244AC30E40A7F83E4469EAA39060B77910A3F7E4ACD4D8FB502DCC445D`,
  and `643F1BC84EB0D3477CA7AADA6342CB6DB1AD92AA3755E7F44695EBFA268769E5`.
- Current English master: 9,524 B / SHA-256
  `742AAFB0A5B933B0211DF7240B231C8FBFB8783877FC14847524AD0BAC22DA4E`.
  Three converged XeLaTeX passes produce 211 pages / 1,103,740 B / SHA-256
  `DCF95AE21A5AA44EE34FD1FE0E629212030880B37B2AB47597D8973B978DE669`.
  Passes 2 and 3 are byte-identical at SHA-256
  `DD34964491BF2F7ED96AF48D875E2D9C7D97FB56D83A217417F56A9E1D8AEB38`;
  the 39,290 B log has zero critical diagnostics and SHA-256
  `254B3FAF62992477AD2095ADA824C530300376474BCFFBF4BB5B49527932BC41`.
- English pages 207--211 and corrected-French pages 178--181 pass lead
  600-dpi render review.  The §3.1 correction footnote stays with its formula;
  all restored tags, long equations, proof seams, and the §3.3 boundary are
  legible and unclipped.
- The diplomatic Exposé-XX body is 41,998 B / SHA-256
  `3EC1736E63D201F495A78D51787651E70C66167600B901A53F6B0090BC86B4F2`.
  The corrected-French body is 41,895 B / SHA-256
  `CFE909B6E7B5654746B962F1730CCFE66C7A457F12DFDFE57BFDCD2EB82D201A`;
  the 166-row register is 34,511 B / SHA-256
  `9BCCD8C0BC9509A527306FE2F4C2A2056F0B3261E7256A7081218E822196F1BA`.
  Its converged 201-page PDF is 1,379,817 B / SHA-256
  `F38EAE641198FB3EF97D2940EE73527D80F870C4874D8554B499FAAF34DE2E7D`.
- Exact continuation cursor: Exposé XX §3.3, scan index 361 / folio 354,
  `authority_snapshot/source/expose_XX_body.tex` line 485.

## 2026-08-01 — Exposé XX §§3.3--4.3; attached canon rule retained

- Re-read Floris's attached EGA instruction and confirmed the existing SGA
  policy is the correct analogue: diplomatic French TeX reproduces the
  bounded print, real transcription deviations are repaired, printed defects
  remain diplomatic and are catalogued, and the corrected French workpass is
  an explicit editorial layer rather than a replacement canon. Attachment:
  16,563 B / SHA-256
  `D9B79248A162437F4AEFE7015015317E2EBA54C67EF290757B8D81DD7CB7DE77`;
  SGA policy SHA-256
  `5191EAC46F20B6F7C03759C275E3371E4177C8ACAFC08C2371051B5C61908F8D`.
- Personally checked scan indices 361--363 / folios 354--356 at 1100 dpi.
  Repaired two genuine inherited transcription deviations: the omitted bar in
  $X_{\bar\eta}$ in (3.3.4), and the missing closing parenthesis after the
  §3.4 citation. Preserved the printed $m^*$ in (4.1.3), §4.2 punctuation,
  and §4.3 characteristic sign in the diplomatic body while correcting them
  transparently in the editorial-French/English layers.
- Integrated components 143 and 144, SHA-256
  `D77434478C11D6093819325FE0D1D1E46ED0D724FC56C38FD398B5C7EF88554B`
  and
  `439F0FFDE24BA1B3A6778242E86F5AA76AF70719DFDBFB6D169E2B0EC6DE5C13`.
  Current master SHA-256 is
  `3755341D8F82F581AC0160E2889FD19A673B757DA4E2B8FDFA7DAEE57DBECBC2`.
- Three converged XeLaTeX passes produce 212 A4 pages / 1,108,748 B /
  SHA-256
  `BE785D0E6E87122F08254B4E09BED82E16214C8C5E40BDB0B9F15583D7D7E4C8`.
  Pass-2/pass-3 console SHA-256 is
  `5B13814A06D8D7D5B5CF6D54DC880CFADAFCE785CE47C54CA75A15DB6977B569`;
  final log SHA-256 is
  `F6599D0387E91EF27E01AD8CF26924E44F871371214D918FE33E8A8BA2A7047D`,
  with zero critical diagnostics.
- Diplomatic Exposé-XX body: 42,008 B / SHA-256
  `3693890EAD0120DF30E5FC6A5A4D8A6EE69E093CDA042F84E2201A29339D4BA2`.
  Corrected-French body: 41,941 B / SHA-256
  `4691204209C06CA568BF1CBF377A94411D1ACCBFF68C0ADBDA76EB02D9C4DE50`;
  register SHA-256
  `F6265E74D3557F13FD190F71EF96AFB7926D17D2A505B5F5D5BB33DA67621E19`.
  Its converged 201-page PDF SHA-256 is
  `23B807BD53A522303907899172870FD3D1252F705DE293859759458237F339BC`.
- Lead 600-dpi review passes English pages 210--212 and corrected-French
  pages 179--181. Exact continuation cursor: Exposé XX §4.4, scan index 363 /
  folio 356, authority line 547.

## 2026-08-02 — Exposé XX §4.4; proof of Griffiths's theorem

- Personally checked authority indices 363--367 / folios 356--360 at
  1100 dpi.  Used direct 5000-dpi details for (4.4.6), (4.4.10), the two
  dense Griffiths expressions, and the four quadrants of the commutative
  diagram.  The diagram inventory is five nodes and five plain arrows; label
  sides, arrow directions, attachments, and punctuation all agree with the
  source.
- Repaired only three real inherited transcription deviations in the
  diplomatic French body: restored $P_{\bar\eta}$ in the composite defining
  $Q_{\bar\eta}$, restored the minus in (4.4.10), and restored
  $\mathrm{pr}_1^*$ in the definition of $z_U$.  Preserved printed defects
  diplomatically and recorded seven separate editorial-French dispositions,
  SGA7II-FR-XX-025 through -031.
- Integrated component 145, 6,840 B / SHA-256
  `AAFD8A32C59C91197BE428170D1FEF3599E10CFB3F9204ECB2A8481E9E9D650B`.
  Current master: 9,697 B / SHA-256
  `C016649D20D9CBDB9007A1BEA3057726F30CB90000D7D04F696D7592DE1FAA97`.
- Three converged XeLaTeX passes produce 214 A4 pages / 1,116,572 B /
  SHA-256
  `332AE51DA915962032F355C2771E70479A037CB948985D60520A802B07678C61`.
  Passes 1--3 are byte-identical at SHA-256
  `AD2B61AE735CFBEEB2DCE861405AE2D13E1F139B01B73D208788E6B1CCB70255`;
  the 39,401 B final log has zero critical diagnostics and SHA-256
  `975AC8F59DB800F8B015CA1E35F7FF7D6C5304914E6FCBEFD874F8F2937D13D8`.
- Diplomatic body: 42,016 B / SHA-256
  `EB545002453B806EC9F5EF4DC932B5382C2CBF6052E80EA9921DE5FF44DE8D5B`.
  Corrected-French body: 41,934 B / SHA-256
  `896FABC17E52445812E50C7B87F3494C1272E233BD5FA4551AD6B6691B2BF670`;
  register: 37,606 B / SHA-256
  `414376F2F0D711FCF9E60631BF2C7AD4372543F15ECA92AA72FCFD7F0BDAE785`.
  Its converged 201-page control PDF is 1,379,738 B / SHA-256
  `FE93BF9F5D544D1D9274A246C09D477F0327AFC2496969F2AD50361B548C8329`.
- Lead 600-dpi render review passes English pages 212--214 and corrected-French
  pages 181--184, including the §4.4/§5 seam.  No clipping, malformed formula,
  or diagram/layout discrepancy remains.
- Exact continuation cursor: Exposé XX §5, scan index 367 / folio 360,
  `authority_snapshot/source/expose_XX_body.tex` line 711.

## 2026-08-02 — Exposé XX §5 and references complete

- Personally checked scan indices 367--369 / folios 360--362.  Whole pages
  361--362 were inspected at 1100 dpi.  The native 300-dpi CCITT scan crop
  around the last parenthetical was enlarged pixel-for-pixel to 9000-dpi
  equivalent and confirms the literal printed string `(4.2)`; the surrounding
  dimensions force the editorial specialization $m=2$.
- Found no inherited transcription deviation in §5.  Preserved every printed
  peculiarity in the diplomatic body and added explicit corrected-French
  dispositions SGA7II-FR-XX-032 through -036.
- Integrated component 146, 3,917 B / SHA-256
  `C510D481AEA1DF62723377A6F64542265775BE675B31D115BC14104607B896B3`.
  Master: 9,755 B / SHA-256
  `BE634E455A5FAFE2820C215DB2F54C055789C06EBADE4DADA6CC79ECB200101B`.
- Three converged XeLaTeX passes produce 215 A4 pages / 1,120,901 B /
  SHA-256
  `5F0D2233C7175B066B90E701313E7CEB9A40842651E9E85A8FDBE501F64892FA`.
  Pass-2/pass-3 console SHA-256 is
  `C386F869E57D216B996F5D409977747CC8894475883C0461E31BAC373388BF32`;
  final log SHA-256 is
  `CAF6B9BA65BA0B7139596CF9501D5812CFD932A8E07C0C3FB9F2512F127203DE`,
  with zero critical diagnostics.
- Diplomatic body remains 42,016 B / SHA-256
  `EB545002453B806EC9F5EF4DC932B5382C2CBF6052E80EA9921DE5FF44DE8D5B`.
  Corrected-French body is 41,968 B / SHA-256
  `5709AC2CB0116B76E103BADF523A3E703E10B561BCCE60738F90DE225E3A85D3`;
  register is 38,849 B / SHA-256
  `595797F00A99D087B0E9B157DAF79C0C2FC3C61EC07521E218FEB5F65DFDF465`.
  Its converged 201-page PDF is 1,379,813 B / SHA-256
  `E7ECC5ED5D2387C08EE147FC7F1FD2CFA32D1313C09EAEF93AAB9955ABA43540`.
- English pages 214--215 and corrected-French page 184 pass lead 600-dpi
  review.  Exposé XX is now complete through its references.
- Exact continuation cursor: Exposé XXI title/summary, scan index 370 /
  folio 363, `authority_snapshot/source/expose_XXI_body.tex` line 1.

## 2026-08-02 — Exposé XXI opening through Definition 1.0

- Personally checked scan indices 370--373 / folios 363--366 at 1100 dpi.
  The title, contents, Introduction, section heading, Definition 1.0, and
  formulas (1.0.1)--(1.0.3) are admitted through source line 79.  No inherited
  transcription deviation was found.
- Preserved the five printed wording/locator defects in the diplomatic canon;
  added corrected-French dispositions SGA7II-FR-XXI-001 through -003 without
  allowing the editorial layer to replace the diplomatic source.
- Integrated component 147, 4,047 B / SHA-256
  `60CD80817F3F916DB774A7666B741E1C45EDEDC17DC7E72B245D683060DB5653`.
  Master: 9,827 B / SHA-256
  `03A4D1FF3D0D62573E27FE5601A607D2996035A605E5743991BF44A9A69FC062`.
- Three byte-identical XeLaTeX console passes produce 217 A4 pages /
  1,126,149 B / SHA-256
  `788CAA769B5906A3256EBE4BD98501087424F79F033281E7A24400493BB4FD9E`;
  final log SHA-256 is
  `7CA2DCFF9747A734374D91810E55688BE8A7FB41449447AC78CDF34A33BF69F5`,
  with zero critical diagnostics.
- Diplomatic Exposé-XXI body: 70,201 B / SHA-256
  `A9B2CC851B0BFB505F555299454B4B4260426819B1EF860085034C53DDDAFAC1`.
  Corrected body: 70,238 B / SHA-256
  `4D6A3124D67CC2057C5F049F58AEB1A89EA855CA78A9C7D6E0EB370151C3ECD8`.
  Correction register: 39,624 B / SHA-256
  `C27BE5F68E4B4B3EF1F0D41F761E4C263E7DB34899A44D5378B8089C2BACF68C`.
- Corrected-French PDF: 201 A4 pages / 1,379,764 B / SHA-256
  `096AC65A9335A32999749982BAC7F56A0F9B65A726241F9BD96CB1D27AB20281`.
  English pages 216--217 and corrected-French pages 185--187 pass lead
  600-dpi layout review; French admission nonetheless stops at source line 79.
- Exact continuation cursor: Theorem 1.1, scan index 373 / folio 366,
  `authority_snapshot/source/expose_XXI_body.tex` line 81.

## 2026-08-02 — Exposé XXI Theorem 1.1 through Proposition 1.1.5

- Personally checked scan indices 373--375 / folios 366--368 at 1100 dpi.
  The full universal-family and trace arguments are admitted through source
  line 136.  No inherited transcription deviation was found.
- Preserved the printed grammar, spacing, syntax, and spelling defects in the
  diplomatic canon; added editorial dispositions SGA7II-FR-XXI-004 through
  -006 in the separate corrected-French workpass.
- Integrated component 148, 3,320 B / SHA-256
  `026F773D2ADB06E34C630E827060017237C80010FEDACDF3D68C04DB8D8E1A75`.
  Master: 9,895 B / SHA-256
  `62F5E1D99848815A28D5AB60FEF7A621A5225505FA8876478E3792E7E41D0417`.
- Three XeLaTeX passes produce 218 A4 pages / 1,130,049 B / SHA-256
  `6E4BF362475EEB07FD051E6AC189AC8CAB950619A5AC081E172EB73704650277`;
  pass 2/pass 3 SHA-256 is
  `1967E6D0296B700A73B0123762C01EA0871993154266DEAE0F637241CCB7823D`,
  and the final zero-critical-diagnostic log has SHA-256
  `6AD094375D564E05925A6647390C63A4F9050C0266432D9D0A663777952BF54C`.
- Corrected-French PDF: 201 A4 pages / 1,379,744 B / SHA-256
  `C4A695A3968AFD622B33CAF0811EA9ACD0F3E2B567B422B9E48DDA34D3B75DA0`.
  English pages 217--218 and corrected-French pages 185--187 pass lead
  600-dpi layout review; the French admission boundary remains line 136.
- Exact continuation cursor: Proposition 1.2, scan index 375 / folio 368,
  `authority_snapshot/source/expose_XXI_body.tex` line 138.

## 2026-08-02 — Exposé XXI Proposition 1.2

- Personally checked scan indices 375--377 / folios 368--370 at 1100 dpi.
  The three formula-sensitive readings were also checked from the native
  300-dpi CCITT pixels enlarged point-for-point to a 5000-dpi equivalent
  view.  This is a display enlargement, not a claim of added source detail.
- Confirmed that the inherited French transcription exactly reproduces the
  printed defects in (1.2.1), the lower bound `d_1\geq a_0`, and the final
  `H_r` variable block.  No diplomatic transcription change was made.
  Corrected-French and English readings are recorded append-only as
  SGA7II-FR-XXI-007 through -010.
- Integrated component 149, 2,105 B / SHA-256
  `D456560CFF215AA8CA329A739621087C7655651E88318AE71B5C7D5C3E7D4D98`.
  Master: 9,945 B / SHA-256
  `E78A190A6CF24264057237697582F0B66DF07226A9FAF2D815D311FC31A226D9`.
- Three XeLaTeX passes produce 219 A4 pages / 1,132,799 B / SHA-256
  `02D6DB000FCADA9D009F736E0DEE311882CFFB6FA7C40821C3C913EA6EFEBE06`;
  pass-2/pass-3 SHA-256 is
  `11AF4B038EA35154685915CE973BF7D3AF39C72BB791F07FF21EE5EB16B570B5`,
  and the zero-critical-diagnostic final log has SHA-256
  `8A3CEDD83E2A146FA3C198B2CA8B7A4668305DB7AE0D201B84FB4F8C1BE4C8F5`.
- Diplomatic body remains 70,201 B / SHA-256
  `A9B2CC851B0BFB505F555299454B4B4260426819B1EF860085034C53DDDAFAC1`.
  Corrected body: 70,256 B / SHA-256
  `00D47E4CCCECE0B9E1886C07D4DFE051759DF34E891CC6F510065ABC703E3F2E`;
  correction register SHA-256
  `85331470A051B81E7670B643784145F8A04537E6A1FF793F0F9DF0B65AAA46B6`.
- Corrected-French PDF: 201 A4 pages / 1,379,736 B / SHA-256
  `B20EF081BDB73499DEF8B945DA468AB16D1DA9162FFAEB48C6E261FF19C7787D`;
  pass-2/pass-3 SHA-256
  `EC16B8265B3E815BD49FD1529FF8AAE66C64F611D7A5366E7435BD998B73D4E7`.
  English pages 218--219 and corrected-French pages 186--188 pass lead
  600-dpi layout review; admission remains bounded through source line 192.
- Exact continuation cursor: Theorem 1.3, scan index 377 / folio 370,
  `authority_snapshot/source/expose_XXI_body.tex` line 193.

## 2026-08-02 — Exposé XXI Theorem 1.3

- Personally checked scan indices 377--381 / folios 370--374 at 1100 dpi,
  with formula and diagram details inspected from native 300-dpi pixels at a
  point-preserving 5000-dpi-equivalent display scale.
- Corrected actual inherited transcription deviations in the diplomatic
  French canon while preserving printed mathematical/editorial peculiarities.
  The separate corrected-French and English readings are recorded as
  SGA7II-FR-XXI-011 through -016.
- Integrated components 150 and 151, respectively 2,929 B / SHA-256
  `B84C2704B0735FEB86A0B2FBF8CEDC37972789FA9CB27C31236559DF688C8230`
  and 2,849 B / SHA-256
  `EFDD0261F1BF9EB4B56654D28A73B61F530714249EADDE4B0FBD4A2E9467378B`.
  Master: 10,068 B / SHA-256
  `CE7D455771A51A6F7E5C7603773A4F0DB0DF37BF4128344D8F4BF65287783A0C`.
- Three XeLaTeX passes produce 221 A4 pages / 1,140,478 B / SHA-256
  `EFE8691C779F787FA859CF9D5D25F95820179ECECBE7B74446D6DE950495398A`;
  pass-2/pass-3 SHA-256 is
  `BEB15548F4C760DBEA9F86BE7F402F436592CE17999B65D7A43F92D203C868DC`,
  with zero critical diagnostics.
- Corrected-French PDF: 201 A4 pages / 1,379,745 B / SHA-256
  `D6553F8DC324804C3C97EEA230CCE79436CC30E9734CF9444617D1ACEB20699A`;
  pass-2/pass-3 SHA-256
  `B23D0768E868E4016573FA175474FCBB923C5286BA8904961C4CA55E9D82CFE6`.
  English pages 220--221 and corrected-French pages 189--190 pass lead
  600-dpi layout review; admission remains bounded through source line 312.
- Exact continuation cursor: Theorem 1.4, scan index 381 / folio 374,
  `authority_snapshot/source/expose_XXI_body.tex` line 316.

## 2026-08-02 — Exposé XXI Theorem 1.4

- Personally checked scan indices 381--384 / folios 374--377 at 1100 dpi.
  The coordinate spelling, relation signs in (1.4.6), and ellipsis in
  (1.4.8) were checked from native 300-dpi pixels at a point-preserving
  5000-dpi-equivalent display scale.
- Restored three actual inherited transcription deviations in the diplomatic
  French canon and kept the distinct printed editorial defects diplomatic.
  Corrected-French and English readings are recorded append-only as
  SGA7II-FR-XXI-017 through -022.
- Integrated component 152, 4,683 B / SHA-256
  `1EE4FBBFDDE90C2599786DA31E701D95E3748BFCA16676B5DEC6B7F6007E5E2C`.
  Master: 10,114 B / SHA-256
  `B7D3D7C555A425015A8102ADB1709CFE5EE332D11C4F33809A8B5017AD03A489`.
- Three XeLaTeX passes produce 223 A4 pages / 1,146,316 B / SHA-256
  `B5F1526D7794755BA48554EEDE527A4CFC85BA1B46ABBD0383CBCDBBC13180B5`;
  pass-2/pass-3 SHA-256 is
  `6709942C252A57282C7A3ABBF0E6D96038FDCAAF876489661170CF7E64322EE0`,
  with zero critical and zero overfull diagnostics.
- Corrected-French PDF: 201 A4 pages / 1,379,715 B / SHA-256
  `AEB8F5D6BF3F2F4D867E0C07B303B027962C07A3D11381D622B25451657A7AAE`;
  pass-2/pass-3 SHA-256
  `8DEB6AB9889455C7195041528CB880DCE927ACBC874009E73230B58E5DA6E54F`.
  English pages 221--223 and corrected-French pages 190--191 pass lead
  600-dpi layout review; admission remains bounded through source line 383.
- Exact continuation cursor: §2, scan index 384 / folio 377,
  `authority_snapshot/source/expose_XXI_body.tex` line 389.

## 2026-08-02 — Exposé XXI §2

- Personally checked scan indices 384--386 / folios 377--379 at 1100 dpi.
  The overstruck finite-extension phrase and terminal Galois-module map were
  checked from native 300-dpi pixels at a point-preserving
  5000-dpi-equivalent display scale.
- Found no inherited transcription deviation.  Kept the diplomatic French
  unchanged and recorded the four distinct editorial readings as
  SGA7II-FR-XXI-023 through -026.
- Integrated component 153, 3,154 B / SHA-256
  `537DBEDB6E4389A3C798EBAE84A5B58F05B48DDEB2CA656086D46B6348D3158F`.
  Master: 10,158 B / SHA-256
  `1DB73EA21CB53E1EC2B1857F95740EAE67FE3DE908751B38159342C40B6575F5`.
- Three XeLaTeX passes produce 224 A4 pages / 1,150,581 B / SHA-256
  `347468FE2203A91A65697D47AF20998B176DCA7D906D8DED7AC0772FFBF9BC73`;
  pass-2/pass-3 SHA-256 is
  `1654FA623EFC265D2CC1FDB7CD6FCE200F111862FD2E9029D2581601B17FFC4C`,
  with zero critical and zero overfull diagnostics.
- Corrected-French PDF: 201 A4 pages / 1,379,333 B / SHA-256
  `DDD2FFAEC3A3B8E1E00A89ECE1856DAA7FCE7EE262D270130C68BA85D6324F62`;
  pass-2/pass-3 SHA-256
  `A1E044118E098D20F561A27F06BB1EFFDD26B15939EC667CAC1594B81D18E26F`.
  English pages 223--224 and corrected-French pages 191--192 pass lead
  600-dpi layout review; admission remains bounded through source line 428.
- Exact continuation cursor: §3, scan index 386 / folio 379,
  `authority_snapshot/source/expose_XXI_body.tex` line 434.

## 2026-08-02 — Exposé XXI §3 opening through Corollary 3.1

- Adopted Floris's EGA French-canon rule analogously for SGA in
  `FRENCH_CANON_AND_CORRECTED_READING_POLICY_20260801.md`, 2,100 B / SHA-256
  `5191EAC46F20B6F7C03759C275E3371E4177C8ACAFC08C2371051B5C61908F8D`:
  the diplomatic French TeX follows the printed authority; transcription
  deviations are repaired there; printed defects remain diplomatic and are
  regularized only in the separate corrected workpass.
- Personally checked scan indices 386--388 / folios 379--381 at 1100 dpi.
  No inherited French transcription deviation was found.  The two editorial
  readings are recorded as SGA7II-FR-XXI-027 and -028.
- Integrated component 154, 3,424 B / SHA-256
  `CBA5397F87988F264C6EFD562968056C88D4DA7CB4A73CF15A14A9651FF850FC`.
  Render review caught literal `equiv` in English formula (3.0.5); this was
  corrected to `\equiv`, rebuilt, and the repaired page was re-reviewed.
  Master: 10,232 B / SHA-256
  `8BB984B09995F5EB1AE1874A0D42222A9ABA4D7F9D4D2D5775B5F76902B5FCE9`.
- Three XeLaTeX passes produce 225 A4 pages / 1,154,535 B / SHA-256
  `D2C9DC467C683DB4D9DFA0B158E9E89F85D54CCF5DD8BF8D2F671073FF504F09`;
  pass-2/pass-3 SHA-256 is
  `5C338E675866D4D532E5E93A7D69BB7238107922DBECB6B25D711396AE472E2A`,
  with zero critical and zero overfull diagnostics.
- Corrected-French PDF: 201 A4 pages / 1,379,356 B / SHA-256
  `C98BA8B73AB37903FF0F1D39E9DA0217F44A3074FF8FC7BFC1615C8CA8673B51`;
  pass-2/pass-3 SHA-256
  `6A61F00FA653EB96968B0A8BFDC362CAB11AF0E396372142984C0C15B3B8F32E`.
  English pages 224--225 and corrected-French pages 192--193 pass lead
  600-dpi layout review; admission remains bounded through source line 498.
- Exact continuation cursor: Proposition 3.2, scan index 388 / folio 381,
  `authority_snapshot/source/expose_XXI_body.tex` line 500.

## 2026-08-02 — Exposé XXI Proposition 3.2

- Personally checked scan indices 388--389 / folios 381--382 at 1100 dpi,
  including every node, arrow, label side, direction, and punctuation mark in
  diagram (3.2.3).  No inherited transcription deviation was found.
- Kept the printed slash generic-fiber notation diplomatic and recorded the
  standard subscript form used by corrected French and English as
  SGA7II-FR-XXI-029.
- Integrated component 155, 1,831 B / SHA-256
  `95D59D2B364EDCD1A95B80BCBD7AC73197763CFF44478431A5C54CFA2A6994FB`.
  Master: 10,282 B / SHA-256
  `23DB4A3FFD5CC02F773CB8C246095CB747057E563CAE6B1F5151AF8F6B08333B`.
- Three XeLaTeX passes produce 225 A4 pages / 1,156,665 B / SHA-256
  `8B2993E1629A42D7A5F360D702011D1C0253FB35C941461C6AE41B02382DF390`;
  pass-2/pass-3 SHA-256 is
  `0AF7342DF6F4422402C92C17BFCD06D43D542FCF7C94A08248D2F10A6AE275A1`,
  with zero critical and zero overfull diagnostics.
- Corrected-French PDF: 201 A4 pages / 1,379,346 B / SHA-256
  `4C4D48F5C38AC0ACE7977B933DF93064A9189C4AD34C3E9459C8456005A8E895`;
  pass-2/pass-3 SHA-256
  `AA83B2CFA5115FD3B7AB47EDB0E038371984CBB59145511D10E3ACA94A6D0EEE`.
  English page 225 and corrected-French page 193 pass lead 600-dpi review.
- Exact continuation cursor: §4, scan index 389 / folio 382,
  `authority_snapshot/source/expose_XXI_body.tex` line 548.

## 2026-08-02 — Exposé XXI §4 and bibliography

- Personally checked scan indices 389--390 / folios 382--383 at 1100 dpi.
  No inherited transcription deviation was found.  Disposition
  SGA7II-FR-XXI-030 records the printed lower summation limit and unaccented
  phrase, with the explicit/standard readings confined to corrected French
  and English.
- Integrated component 156, 2,017 B / SHA-256
  `CA7D663CE5085CDE713CFC9044820BEF7919168264591F0433E5DE59AF557CF1`.
  Master: 10,343 B / SHA-256
  `CE1A54433642F6210F1A035BCDD7B7606C54D7976350544D764AFAB243C7610A`.
- Three XeLaTeX passes produce 226 A4 pages / 1,159,050 B / SHA-256
  `5C08B788FBBB197983115B6C197965D5C6F19E3A7C0A5755F095B73A6FDB7E33`;
  pass-2/pass-3 SHA-256 is
  `076C3C09868E80F8539DA6334391F4FF1BE4FE6167EC17EF5C1C5A345726098E`,
  with zero critical and zero overfull diagnostics.
- Corrected-French PDF: 201 A4 pages / 1,379,370 B / SHA-256
  `C858138157FE1649F1E7409ADE1D988E9599F08110A44B5DA74B045AD520073F`;
  pass-2/pass-3 SHA-256
  `A2C55519EC22EB0229FD475811B66E5DE4C1A311CC3225F9D4624382A8F73D52`.
  English pages 225--226 and corrected-French pages 193--194 pass lead
  600-dpi layout review.
- Exact continuation cursor: §5 appendix, scan index 391 / folio 384,
  `authority_snapshot/source/expose_XXI_body.tex` line 600.

## 2026-08-02 — Exposé XXI Appendix §5 through Corollary 5.3 setup

- Personally checked authority scan indices 391--396 / folios 384--389 at
  1100 dpi, including both diagrams node-by-node and edge-by-edge.
- Repaired three inherited transcription classes to print in both French
  layers and logged two distinct printed-source corrections only in the
  editorial French/English layers as SGA7II-FR-XXI-031 through -033.
- Integrated components 157 and 158, SHA-256 respectively
  `FD35E44CBAF2A4B32CBD5845502F27635DA240E197EF44A37812182C71B966D4`
  and
  `29B8B6350992F29FF86204A2393D591FE14572077654B62FABE9D39D8451A805`.
  Master SHA-256:
  `F5C32E058DDE62144B556B2E96CDFE753B73CF0A9AC397C43F0923803564547A`.
- Render review caught the literal `simeq` produced by a missing TeX
  backslash.  Preserved r1 as adverse history, repaired the source, rebuilt,
  and re-reviewed the affected page.
- Final three-pass English build: 229 A4 pages / 1,173,457 B / SHA-256
  `1E9EE49990BA1879CBCA8605DBF4415005FB33D3D88638F7A88F97B099CCC538`;
  pass-2/pass-3 SHA-256
  `1F14E5855E24279B570FCBAE97857F415BCD43DA3A36DAB581F3EA0A3943E71A`;
  zero critical/overfull diagnostics.  English pages 226--229 pass final
  600-dpi review.
- Corrected-French PDF: 201 A4 pages / 1,379,664 B / SHA-256
  `0F47F6C722A579A25E258CB4108A475742E254796E54054EADC83116A46FDBF5`;
  pass-2/pass-3 SHA-256
  `A4BED35C6EFFBD90A0DF1EA83CD05B7C2EFDA1D43867D1EA4B73C7262442FD88`.
  Corrected-French pages 194--196 pass 600-dpi review; only the two inherited
  Exposé-XVII overfull diagnostics remain.
- Exact continuation cursor: Lemma 5.3.1, scan index 396 / folio 389,
  `authority_snapshot/source/expose_XXI_body.tex` line 747.

## 2026-08-02 — Exposé XXI Lemmas 5.3.1--5.3.2 and Theorem 5.4

- Personally checked authority scan indices 396--399 / folios 389--392 at
  1100 dpi, including every mathematical element and punctuation mark in the
  three-row Theorem 5.4 diagram.  No French transcription deviation was found.
- Logged the three printed-source mathematical/citation peculiarities as
  SGA7II-FR-XXI-034 and -035; the diplomatic French is unchanged, while the
  corrected French and English use the explicit invariant-space dimension,
  the exact lemma locator, and \emph{indecomposable}.
- Integrated components 159 and 160, SHA-256 respectively
  `8E193A99C487F86F3078C12D7B8CDC18CD8692E70B4BF6B028C956958A305F63`
  and
  `7003D60B9E443DAB3EB7CB9C38EC2635AE8CB035C8C9724E1F90C3050136D689`.
  Master SHA-256:
  `C0CCABB6CC02230D4B794ECFF7A448DDC534E3FF176016F216102DC0035BC69B`.
- Preserved two adverse builds: r1 exposed unavailable curly-quote glyphs;
  r2 compiled cleanly but direct visual comparison caught a source comma
  rendered as a period in the diagram's third row.  Both defects were fixed
  copy-on-write and the final page was rebuilt and re-reviewed.
- Final r3 English build: 231 A4 pages / 1,180,973 B / SHA-256
  `5156D9A69E7B2314079190E9B19B67041772D92CAE54A0E34AE66F23B97983B6`;
  pass-2/pass-3 SHA-256
  `CD91B80F075A36BA2E86034342F6A88A2BF2FB13FDF8631566E75A8B95D129A4`;
  zero critical/overfull/missing-character diagnostics.  English pages
  229--231 pass final 600-dpi review.
- Corrected-French PDF: 201 A4 pages / 1,379,867 B / SHA-256
  `E50CF28CE9A47B44A951FC729C8144D1E0AC3AD0BADFB1BE5C61CD2B392AD045`;
  pass-2/pass-3 SHA-256
  `22D7274EF01E72AB8667FD3F2AE13961447E75A47EF2D2C890401846D72249A3`.
  Corrected-French pages 196--197 pass 600-dpi review; only two inherited
  Exposé-XVII overfull diagnostics remain.
- Exact continuation cursor: §5.5, scan index 399 / folio 392,
  `authority_snapshot/source/expose_XXI_body.tex` line 831.

## 2026-08-02 — Exposé XXI §§5.5--5.6 complete

- Personally checked scan indices 399--408 / folios 392--401 at 1100 dpi,
  with targeted full-resolution notation crops and approximately 5000-dpi-
  equivalent inspection of all three §5.6 diagrams.
- Restored two genuine inherited transcription classes in both French layers:
  missing underlines on $G/H$ in Theorem 5.5.2; wrong-side $j$ plus calligraphic
  rather than Fraktur Galois notation in §5.6.  Logged the distinct printed-
  source editorial readings as SGA7II-FR-XXI-036 through -043.
- Integrated components 161 and 162, SHA-256 respectively
  `4DB88480602DC3AD01245A38F4646220505380F5CC76BF029E472E1732A280A8`
  and
  `F50B948A1960A5C7AEA59699BAB5FBA1EA63629F6CCE5A8FF50FD7695E4EE8EA`.
  Current master SHA-256:
  `FC9BCECD27A1AFC5A48CADC8E33D941FAAC0A568238590C8BE36728DA6BDBA81`.
- Final English build: 235 A4 pages / 1,198,343 B / SHA-256
  `6CA36419DB4E8087DAA8FB563B0B5B9B0E9EEDFE0EB625D4003B7D58DD1C7D52`;
  pass-2/pass-3 SHA-256
  `4355941039B8D78029DF8DCCC508E91CED0DF3FDDCFA3CAA072D5D897C45CA5B`;
  zero critical/overfull/missing-character diagnostics.  English pages
  231--235 pass final 600-dpi review.
- Final corrected-French verification reader: 201 A4 pages / 1,379,889 B /
  SHA-256
  `7FB00AD7000FB4F5B816A6F221CBFA76F9E997C80982C369B737DAB0FB129F20`;
  pass-2/pass-3 SHA-256
  `30488AB20F1851C4557DF35F4A8CEAB2AA812A60E7AC750CDFFBCCB56CFFFC00`.
  Corrected-French pages 198--201 pass final 600-dpi review.
- Exposé XXI is complete.  Exact continuation is Exposé XXII, scan index 409 /
  folio 402.  No frozen Exposé-XXII TeX exists; personally transcribe and
  translate indices 409--445 through volume EOF.

## 2026-08-02 — append-only scan-boundary correction before Exposé XXII

- Direct inspection of the authority page seam corrects the preceding locator:
  scan index 407 / folio 400 is the terminal Exposé-XXI bibliography page.
  Exposé XXII begins on its title page at scan index 408 / folio 401, not at
  index 409.  Its exact remaining extent is therefore indices 408--445
  inclusive (38 scan pages).  The earlier locator is retained above as
  adverse history and is not used as the live cursor.
- The current active cursor is Exposé XXII, scan index 408 / folio 401.

## 2026-08-02 — Exposé XXII opening through Proposition 1.2 proof opening

- Personally transcribed scan indices 408--412 / folios 401--405 into both
  French layers and translated them into English. The authority images were
  inspected at 1100 dpi; a targeted full-detail crop of (1.0.7) established
  the large operator as $\bigcap$, not a sum. Existing OCR/text extraction was
  used only as a locator and did not decide the reading.
- Diplomatic French preserves the printed surface. Corrected French records
  four append-only dispositions, SGA7II-FR-XXII-001 through -004, for
  `peut-être`, spacing/agreement collisions, `Una application`, the omitted
  verb in `si elle additive`, and sentence punctuation.
- Integrated English components 163 and 164. Component 163 is 3,822 B,
  SHA-256
  `F655785E83E050E11FE181D114531B788A6D3DED97B7036250D6259320DFF769`;
  component 164 is 3,619 B, SHA-256
  `1EC240C1641645C75DA9EB3F75B0DF7814F75259BCED73ADBFE855A6783BBE10`.
- The first build r1 is retained as adverse evidence: visual review caught
  one lost TeX backslash that rendered `qquad` literally in (1.1.3). It was
  repaired in English and both French layers, and all affected pages were
  rebuilt and re-reviewed.
- Final r2 English build: 239 A4 pages / 1,207,525 B / SHA-256
  `88D1B190F19AF126E475B3915BB018546EF5A45D4ABC24B2E295F1AD3093B518`;
  pass-2/pass-3 SHA-256
  `8133B9E63314281F629680AEAA53B76B7C0CA97F5FAAA58FE297FA4E039F15B5`;
  zero critical, overfull, missing-character, or rerun diagnostics. English
  pages 236--239 pass 600-dpi review.
- Final r2 corrected-French verification reader: 204 A4 pages / 1,392,334 B /
  SHA-256
  `AE76EA102995623C78A17AFDC2B3793361AF980DA30ACF9B92D49D043D0A736C`;
  pass-2/pass-3 SHA-256
  `AAE8CAA89A720A4054E479BB505B0F1D294D7885914BD3AF43DF315359568456`.
  French pages 202--204 pass 600-dpi review; the only overfull diagnostics are
  the two inherited Exposé-XVII lines already present before this tranche.
- Exact next cursor: continuation of the proof of Proposition 1.2, scan index
  413 / folio 406.

## 2026-08-02 — Exposé XXII through Proposition 2.2.5

- Personally transcribed and translated scan indices 413--416 / folios
  406--409. The full authority pages were read at 1100 dpi, with targeted
  detail crops for the barred Frobenius operators, tensor fields, and the
  concluding inverse.
- Completed Proposition 1.2, §2, Proposition 2.0, Corollary 2.1, and all of
  §2.2 through Proposition 2.2.5. English components 165 and 166 are,
  respectively, 3,048 B / SHA-256
  `BC7E3BBD3CE084E77948980E6CD0AA20236EAD88BBD5FA63B0F652BA54F1721B`
  and 5,468 B / SHA-256
  `E63381B19AB5A152D8FBB4A6A83A4C6E010E46A2305B9DBF03B531D3512477C4`.
- Restored three lost `\simeq` command backslashes in the initial French
  entry. These were transcription deviations and were repaired in both French
  layers. The final printed proof sentence also drops the inverse on
  $\varphi_q$ even though Proposition 2.2.5 states $\varphi_q^{-1}$ and the
  immediately preceding argument proves the actions inverse. Diplomatic
  French retains the print; corrected French and English use
  $\varphi_q^{-1}$. Dispositions SGA7II-FR-XXII-005 through -007 record the
  distinction.
- English build r1 is adverse history: its first 600-dpi render exposed a
  literal Unicode-escape token in place of the word `étale` and showed that
  the earlier source note
  had become stranded inside the completed proof of Proposition 1.2. Both
  presentation defects were repaired copy-on-write without changing the
  mathematical text.
- Final English r2: 241 A4 pages / 1,215,208 B / SHA-256
  `AE8EF3113657D69347E886EFAEA2377F7F565E2D98B4F718EFDEDB6030312E2E`;
  three XeLaTeX passes exit 0, final log 40,917 B / SHA-256
  `87AD0257FC4EC56D0F071141548CE38DED15F7387D00B183C28326DDDE3798F3`,
  with zero critical, overfull, missing-character, or rerun diagnostics.
  Pages 239--241 pass personal 600-dpi layout and formula review.
- Corrected-French reader: 206 A4 pages / 1,403,821 B / SHA-256
  `88D2AD262A6CDC10CD2290ACBC9AE785CCF7A3D7B23745C056AFC6BC177DBE2E`;
  final log 41,288 B / SHA-256
  `77D9A6CF049BF6C3BC1B94D3B79A8DE7F4CFA41F9A09C7BAC410ABE3C0BB896E`.
  Pages 202--206 pass personal 600-dpi review; the only overfull diagnostics
  are the two inherited Exposé-XVII lines already present before this tranche.
- Exact next cursor: Exposé XXII §3, scan index 417 / folio 410.

## 2026-08-02 — Exposé XXII §3 through Lemma 3.9

- Personally transcribed and translated scan indices 417--421 / folios
  410--414; full authority pages were read at 1100 dpi and targeted detail
  resolved the §3 locators and Frobenius indices.
- Diplomatic French preserves the printed broken locators and indices.
  Corrected French and English use (3.1.2), (3.2.1)--(3.2.2), (3.3.1),
  $(\mathrm{fr}_q^X)^*$, $p\ne0$, and (3.4.1) as context requires.
  Dispositions SGA7II-FR-XXII-008 through -010 record the changes.
- English build `build\c168_expose_XXII_through_section_3_r1`: 245 pages /
  1,721,311 B / SHA-256
  `CADA3AB952A4A41EEEFCB5F3BD46A6C991160CB12E56442E6BBB1DA1A96A420A`;
  three passes clean, pass-2/pass-3 console SHA-256
  `91CF1CF026A98957737170F631280E4421EFAB71809B267B754413D80035F49B`.
  Pages 240--245 pass personal 600-dpi review.
- Corrected-French build
  `french_source_corrected_workpass\build_check_exposeXXII_through_section3_pdflatex_r1`:
  209 pages / 1,418,669 B / SHA-256
  `9620AD73ABAEBEAEE63A2602BF0F9C0F565F8067993ACE048F1117E6BC84DF74`.
  Pages 204--209 pass personal 600-dpi review; only the two inherited
  Exposé-XVII overfull diagnostics remain.
- Exact next cursor: Exposé XXII §4, scan index 422 / folio 415.

## 2026-08-02 — Exposé XXII §§4--6, bibliography, and SGA 7 II EOF

- Personally transcribed and translated scan indices 422--445 / folios
  415--438.  Full authority pages were read at 1100 dpi, with targeted
  high-detail crops where formula indices, operators, arrow labels, or tiny
  superscripts required them.  In particular, a direct
  4,950-dpi-equivalent crop establishes that the print really has H^{i+1} in
  (6.3.4); the corrected French and English use the contextually forced
  H^{n+1}, while diplomatic French preserves the print.
- Added English components 169--183 and completed Exposé XXII through
  Proposition 6.3 and its bibliography.  The master now binds 183/183 unique
  components with zero missing or duplicate inputs.
- Added the complete terminal French body to both the diplomatic canon and
  corrected workpass.  Each French master binds all 13 Exposé bodies,
  X--XXII, with zero missing inputs.
- Added stable correction dispositions SGA7II-FR-XXII-011 through -028.
  The last tranche includes the omitted verb in Lemma 4.6.6, duplicated
  5.0.7 numbering, q^if/q^it, the Lemma 4.4.6/4.6.6 locator, agreement in
  'met en relation', 4.5.24/4.5.33, R_B/R_S, ord(a)/ord(q), and
  H^{i+1}/H^{n+1}.  The register now has 254 unique correction IDs.
- The initial complete English r2 visual check caught one remaining target
  slip: the §6 calculation said modulo p\mathcal O[[t]] although both the
  authority and Corollary 6.0.12 require \pi\mathcal O[[t]].  Component 179
  was repaired copy-on-write and rebuilt as r3.
- Final English r3:
  264 A4 pages / 1,785,484 B / SHA-256
  '930446AC789F5B67C7093C02D5604AFB5A4ED1E0554B1A25CC7EEF633C9F0960';
  final log SHA-256
  '8D9434E616374119643F0ADB3A31E82C455F4FAF562CED77FC83A82D1097C413';
  pass-2/pass-3 console SHA-256
  'D4CB4A12074932A2782B7D7393F36041F3099596169C52FBD4463202BCD7E7EE'.
  The final log has zero critical, overfull, missing-character,
  undefined-reference, fatal, or rerun diagnostics.  Page 258 was freshly
  rendered at 600 dpi after the \pi repair; the rest of pages 254--264 retain
  the immediately preceding complete visual PASS.
- Final diplomatic French:
  227 A4 pages / 1,505,168 B / SHA-256
  'C5FD43DF4A58BF860115D0D48F284FA9059B952CCCDC387266456D2E1A3F7AAD';
  pass-2/pass-3 console SHA-256
  '53B6830183FA7EF9444A25A1594679B8C39DCF84FC84F8759C821AEC836CFC5D'.
- Final corrected French:
  227 A4 pages / 1,506,305 B / SHA-256
  'C5FD45E9127603EC6E347C7AB7DFD77AF17DB0176F5DEAF5F59553752F96D513';
  final log SHA-256
  '8727952C4AA5419853A03E362F45B66D22B4FA1645FAE56DAF2A84C6AC1A426C';
  pass-2/pass-3 console SHA-256
  'A55CD7C1E8D3CFABD8B0AB113F254EDAD970DE1C62A71A345B6D5206DFC90388'.
- Corrected-French pages 217--227 and all changed diplomatic counterparts
  pass personal 600-dpi review.  Pixel comparison identified the unchanged
  diplomatic pages, which inherit the reviewed corrected render exactly.
  Direct footer crops confirm complete three-digit page numbers where the
  whole-page viewer preview showed only the final digit.
- Exact SGA 7 II cursor: EOF.  Local diplomatic French, corrected French, and
  English body coverage is complete.  Publication, exhaustive reference-v2,
  and archive transport remain separate gates.
- Floris's archival decision is bound: retain complete French TeX and
  bounded/per-volume French witnesses; the cumulative public-facing reader
  may remain English and no omnibus public French PDF is implied.

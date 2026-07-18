# French syntax QA: root-owned P30/P40/P41/P42/P43 files

Status: text review complete; cumulative build and page-render QA intentionally pending until the moving P02 and parallel metadata/post-P43 edits are frozen.

Authority: `authority/R823/pkg_r823/Noether_R823_WebB_R822_P20p27_31_RunInDashRefine_20260717/1/01_cumulative/Noether_R823_cum_de.tex`, SHA-256 `EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21`.

Method: every exact `il suit` and `se laisse + infinitive` survivor in the files below was read in its complete French sentence and checked against the cited German `folgt`/`lässt sich` source sentence. The repair is syntactic only: implications, hypotheses, formula order, mathematical objects, equation labels, and note anchors were not changed. Depending on the source construction, the French now uses `on obtient`, `on en déduit`, `entraîne`, `montre`, `donne`, `s'écrit`, `admet un plongement`, or `peut se formuler`.

| Target and live SHA-256 | Target loci | R823 authority loci | Reviewed decision |
|---|---:|---:|---|
| `N30_s03_fr_body.tex` — `0F093EED9787C4CD6F57B2F739C8F6ABA5AEEBC2C41882CF06740BC57BD29980` | line 31 | line 14867 | `lässt sich ... darstellen` is the unique product decomposition: `s'écrit ... comme produit` rather than the German calque `se laisse représenter`. |
| `N30_s07_fr_body.tex` — `BCC1C12053E27DEC787723AB4339150894F1B68803476A9D0CB6A76B33E7164C` | line 55 | line 15059 | The hypotheses introduce the next consequence: `Les hypothèses donnent encore le résultat suivant`. |
| `N30_s08_fr_body.tex` — `12CBA56F8B99A4D6ABE76897337B1F71B500F0680D5C2839DDD54602FC9120AF` | lines 30, 52, 69, 99, 116 | lines 15111–15119, 15136–15142, 15168–15172, 15188–15195 | Recast five proof transitions as `On a`, `le lemme montre`, `En multipliant ... on obtient`, and `l'hypothèse entraîne`; the displayed congruences remain unchanged. |
| `N30_s09_fr_body.tex` — `5116E7CFBABDF08D1D0A59407F769A7CD3275B725E8B0DC495973C3ECC0BF418` | lines 55, 100, 112, 126, 134, 140 | lines 15256–15261, 15308–15310, 15322–15324, 15336–15350 | Recast six deductions with explicit antecedents (`le point 3/6γ montre`, `la relation entraîne`, `on obtient`), preserving all ideal/module formulas. |
| `N40_s06_fr_body.tex` — `59724232CB480E1FE513DF91BD753FFCA17A9C243D62BAD5CED2105D700E0290` | line 86 | lines 19555–19559 | The representations `sont toutes distinctes` (static mathematical assertion), and the equality supplies the extension relation: `la relation ... donne`. |
| `N40_s07_fr_body.tex` — `B8FCC0D062329C6C28DA408216705796100149F72E8298D0BB045CB12AEB00BD` | lines 15, 40 | lines 19582–19584, 19600–19602 | `A` `admet un plongement irréductible`; the maximal-commutative-ring remark is introduced by `On en déduit`. |
| `N40_s09_fr_body.tex` — `BEE6489D0468DD3C0BA5358670C4A9C94D8462DF84D90289897C05DA8F6D5F44` | line 25 | lines 19745–19753 | The cited earlier result `donne également` the stated consequence. |
| `N41_fr_body.tex` — `CE7334BD16F0D8392F68F3E8945CA4030728842EF0B899CB1CBF12D1294EDF73` | line 9 | lines 19778–19780 | The principal-genus theorem `peut ... se formuler` hypercomplexly; no change to the theorem's mathematical scope. |
| `N42_fr_body.tex` — `057F8C498FEDDCADDCC3A25F1953861D47BC884B57E028FC37C8E3CD570D45A4` | line 183 | lines 20053–20062 | From maximality, `on en déduit aussi` the trace-ideal identity. |
| `N43_rebuild_intro_s03_fr.tex` — `EF5BCA4BB77568909312AEF32509DAE68942CEFD1A6CCC18BC3B8994BE27E2CF` | line 34 | lines 20846–20857 | The coefficient condition immediately yields the complementary-module quotient description: `on en déduit aussitôt`. |

## P34 article-wide follow-up

The same occurrence-by-occurrence method was then applied to the 20 remaining exact calques in the active P34 fragments. The authority locators below identify the corresponding German deductions or `lässt sich` construction; the displayed mathematics and article structure were left unchanged.

| Target and live SHA-256 | Target loci | R823 authority loci | Reviewed decision |
|---|---:|---:|---|
| `N34_intro_s01_fr_body.tex` — `6C5BB67F976DFE520740969FB753BF3D56DA04635FA153EAF8349078CC176F15` | line 109 | line 16404 | The Abelian group `peut être considéré ... comme un module sur cet anneau`; this removes the literal `se laisse concevoir` without changing the operator-ring assertion. |
| `N34_s04_fr_body.tex` — `89C9ADB3C662D66BEE409398C0851D8F9870CA2BD141BEAF89043618C5877B31` | line 43 | line 16517 | Direct indecomposability means that the group `ne peut pas être représenté` as a nontrivial direct product. |
| `N34_s05_fr_body.tex` — `AA242419671F521582F1C7F8E5C22FFA9A23C73327F472DAEC7BAA4A632C133E` | line 35 | line 16625 | The preceding direct-factor equality now introduces the quotient isomorphism with `on en déduit`. |
| `N34_s07_fr_body.tex` — `7B9AB1BC4D42D807025AB1ADD16705C16B48A589CF62BFB35FD24E16CE18580B` | line 26 | line 16726 | The implication is explicit: `PA=0` `entraîne` the displayed equality and hence `A=0`. |
| `N34_s09_fr_body.tex` — `42FADB7B1BC6E4D0C8C93922E9BF7776528DD6C534372AD9E207C4AC31B22BC0` | lines 44, 65 | lines 16806, 16827 | The formulas `donnent` the inclusions/equalities; specialization and multiplication `donnent` the subsequent displays. |
| `N34_s10_fr_body.tex` — `D28C8CD305A00357383577F4FFF8D539435EC0C9856A6B625AF99BBDE2E40FFE` | line 30 | line 16879 | Relations (1) and (2) `montrent` that the modules are two-sided ideals. |
| `N34_s11_fr_body.tex` — `E8D1C3E706E41F7AEFDB876ACFE9F07257275C91FADBEB7103C3CDF8E4556E1F` | line 26 | line 16973 | The stand-alone transition before the displayed decomposition is `on obtient`. |
| `N34_s13_fr_body.tex` — `94E5A386A37A2576DD48E12F8A0ADD02C34131E2C91BE42DA379A1A3334D6B69` | lines 27, 29 | lines 17082, 17084 | Minimality `donne` the ideal equality, while `ab=0` `entraîne b=0`; no proof hypothesis changed. |
| `N34_s14_fr_body.tex` — `C79F98FC89B812C05140F7D475ACFFB0159A7CB38E71FB4DF717E4AA02467C8F` | lines 21, 33, 79, 83, 119, 176 | lines 17185, 17197, 17243, 17247, 17283, 17340 | Six formula transitions now use `on obtient`, `donne`, or `on a ... en général`; all matrix-unit identities and indices are unchanged. |
| `N34_s15_fr_body.tex` — `D04CE14CB20EA55180356EF6FA189F6C40928C8609C36F6BDF1B5379AA74EA8C` | line 71 | line 17487 | The homomorphism relations are introduced by `on obtient`. |
| `N34_s21_fr_body.tex` — `E3FD4F58F98A62FD36512F269266AD5E52838646886774F44EBB82D9F1C5BFA7` | line 62 | line 17939 | The radical criterion is stated as `on dispose encore du fait suivant`, retaining the same sufficient condition and note anchor. |
| `N34_s25_fr_body.tex` — `B344FA399EAB1E6E5128C4F8D2F749A84EA4AE2CED59E0002646750586A2A588` | line 30 | line 18182 | The alternate-basis discriminant formula is now explicitly `déduite` from (1). |

Pre-edit copies are preserved under `working/backups/syntax_qa_root_pre_20260718/tex/` and `working/backups/syntax_qa_p34_pre_20260718/`. Dependency-scoped post-edit scans found zero exact `il suit` and zero `se laisse`/`se laissent` in both reviewed sets. This artifact records language QA only and does not promote source-parity state by itself.

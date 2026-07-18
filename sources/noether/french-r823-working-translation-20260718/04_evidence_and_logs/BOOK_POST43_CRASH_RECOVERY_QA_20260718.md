# QA de récupération P33/P34 et post43 — 18 juillet 2026

Statut : **contrôle terminé**. Ce dossier consigne la reprise après interruption, sans modifier aucun cumulatif, manifeste final ni corps d'article P33/P34.

## Portée et résultat

- P33 : ouverture validée en lecture seule.
- P34 : métadonnées, introduction, §§18--20 et notes correspondantes validées en lecture seule.
- Post43 : corrections sémantiques ciblées, scans canoniques, doubles compilations LuaLaTeX isolées et contrôle visuel terminés pour le livre, Kapferer--Noether et les matières terminales.
- Fichiers explicitement laissés intacts : `working/r823_fr/tex/cum_fr_R823_COMPLETE.tex`, tous les cumulatifs P33/P34 et tous les corps `N33*`/`N34*`.

## P33/P34 : validation en lecture seule

| Source de production | Octets | SHA-256 |
|---|---:|---|
| `working/r823_fr/tex/N33_fr_body.tex` | 9 195 | `98C8B505BAF19705DC938BCBA20E98BE84F5AE7C6B3EA381999F89A13A1E0639` |
| `working/r823_fr/tex/N34_intro_s01_fr_body.tex` | 18 532 | `064E2F97264C78846978AC18D14617878CE5DF66B167E8D5DD689D1E4D89D0C9` |
| `working/r823_fr/tex/N34_s18_fr_body.tex` | 6 293 | `11D0F2560F17334EF0157525E4544CB63BF77D44910CA127A2E99C8C7AA764B3` |
| `working/r823_fr/tex/N34_s19_fr_body.tex` | 4 846 | `EF6BFDE9F592B03A3756046E7965AC1FC5AF9037E6FB2DA47D90E7BE2E0DD444` |
| `working/r823_fr/tex/N34_s20_fr_body.tex` | 8 237 | `9F28D1DA02501BEB8E6AA72485A6F5784A4AA26D109ACFF71998A4274483E3CD` |
| `working/r823_fr/tex/cum_fr_P34_s26.tex` | 328 398 | `474C57D99062760C6E13E0F7EF4ADD21B4EFEA3D3176992DF4BEB8DDD89C5B95` |

Deux témoins de compilation antérieurs et postérieurs à ces sources ont été vérifiés :

- cumulatif P34, deux passes pdfLaTeX : `build/p34_parity_20260717/cum_fr_P34_s26.pdf`, 357 pages, 2 332 272 octets, SHA-256 `34E2016A4AAB875A28FA553BC62EB3C5F082C9B7B5D3EDDA936D244FFA6845CD`; log `3E2A38142216E916159DCD455B0F63241F5712AD1CB3005AF2FEB53B15FC526F`; sorties de passes identiques `43ED2BAA1BE458D2E2AFA0DD508B24135B2D59EE75AA1DCD34B5C189A368B35F`; zéro erreur, avertissement de mise en page ou boîte défectueuse.
- cumulatif complet, deux passes LuaLaTeX : `build/full_lualatex_probe_20260717/cum_fr_R823_COMPLETE.pdf`, 485 pages, 3 667 228 octets, SHA-256 `D6D7F35FBD84016B242FD10430A6B36B5BAA46DDB633CB16560E846F241F99B5`; log `7C45A1A3C564227BE8C5D81F3FA97D383320232B613604F1ED32B77C97D57A33`; passes `F3DAF3F64DE207E56C173AC8EC92CA369A0250C988B71B8A084D76FCFE458F2F` et `D5F8A7C8007B346D9B6E4D339A8DCC0D903FBFDE0288BBA0EEAD6C1ED2243808`; zéro erreur ou boîte défectueuse, avec seulement trois avertissements bénins de substitution de tailles `rsfs`.

Inspection Poppler 144 dpi du cumulatif complet :

- P33, ouverture : page PDF 325, PNG `684D3669609827F4EFF2131A0C8547E23FB61583A4435B7E47B9559B2BD44B49`.
- P34, métadonnées et introduction : page 327, PNG `3056CBAEAC6E59D32DD2EF2C28A302704A73B966FA1145728F0B6DB9A0ED3370`.
- P34, §§18--20 : pages 349--352, PNG `00759F860C430B2E55E56B7FC1F7AFC51C11E037E9BD70140B930E421B22E9E1`, `7F2324DBDE3D8CC1BD1E74F3D06EF626E180AEDB7DF9D1D5750BB4ACB47AF64E`, `CD8DF3C23D457749DC33637FB512781600FC518D512BA9F5213D9CEC513D50BF`, `281FF7206446B551E5C0A9A53BB0EBCE89331CC01E4389AE1AFCF6BAFAD87570`.
- Notes 17--19 et transition vers §21 : page 353, PNG `F1F3B7FE63D15316504EF3D880242A0449531C13202B503019D5D71B9FF62BBD`.
- Résultat visuel : aucune coupure, superposition, formule brisée, note illisible, corruption d'encodage ni glyphe manquant.

## Corrections post43 contrôlées contre R823

- `book_ch03_ch04_fr.tex:256,258,260` : `K` est rendu par « corps gauche » conformément au sens imposé par les automorphismes intérieurs et le centre (R823 l. 21794, 21796, 21798).
- `book_ch03_ch04_fr.tex:412` : hypothèse « corps gauche dont le centre est P » (R823 l. 21945).
- `book_ch05_ch06_fr.tex:197,214,492,503,735,846,883,1236,1270` : suppression du calque « il suit » au profit de `il résulte`, `il s'ensuit` ou de la tournure déductive exigée par le contexte; autorités respectives R823 l. 22534--22536, 22549--22553, 22829--22831, 22834--22848, 23086--23098, 23224--23226, 23253--23263, 23616--23620 et 23648--23652.
- `kapferer_noether_fr.tex:148` : « conditions pour que soit satisfaite »; R823 l. 23862 n'énonce pas des conditions nécessaires.
- `kapferer_noether_fr.tex:163` : accord pluriel `forment`, conforme à la série sujet et à R823 l. 23876.
- `kapferer_noether_fr.tex:173,193,218` : tournures `on déduit` / `il résulte`, contre R823 l. 23884--23886, 23904--23909 et 23927--23934.

## Empreintes post43 finales

| Fichier | Octets | SHA-256 |
|---|---:|---|
| `book_frontmatter_fr.tex` | 3 320 | `63EB4DBBA51258C64FE96BE36BFACF31ECC76A7228973EA8D8ADA7EEFA550DD5` |
| `book_intro_ch01_fr.tex` | 13 350 | `F1693EEDEEECE010CE20556F3C89A02397E16FF06AFE4941BA302026A6775DA7` |
| `book_ch02_fr.tex` | 21 271 | `D1AA8A59F080DE0D7B422606F29C73F656DB991AC561B1A7629FB28EA854FE06` |
| `book_ch03_ch04_fr.tex` | 52 759 | `37060D6DA0A4F23CF901542A13009FE3C761A73723499B957C19AAD6B4787900` |
| `book_ch05_ch06_fr.tex` | 90 696 | `5004532A430A72F214131A2A4AACA2FDDADB8150C18B6ECA73399CC4965C7E6E` |
| `kapferer_noether_fr.tex` | 24 314 | `E7620BB4AF317B2BEF806923E942A7ADD29CC3D42DDDB90DC8877A1A7726E0FF` |
| `terminal_matter_fr.tex` | 9 264 | `73840187B90DA346836B46FB15B45589EE6CF27D1D77C351C8628175F9B08C99` |

Scan sur ces sept fichiers : zéro occurrence des calques interdits, zéro `il suit`, zéro `se laisse`, zéro motif d'encodage suspect (`Ã`, `Â`, `â€`, caractère de remplacement). Comptages témoins : `corps gauche` 26; `corps gauche des endomorphismes` 11; `corps des endomorphismes` 0; `corps non commutatif` 5; `corps des invariants` 17; `domaine des invariants` 12; `anneau quotient` 1; `classe résiduelle` 1; `système de facteurs` 30; `produit croisé` 10; `anti-isomorph` 11; `représentation réciproque` 17; `bimodule` 13.

## Probes LuaLaTeX isolées, deux passes

| Composant | Pages | PDF SHA-256 | Log SHA-256 | FLS SHA-256 | Passes console | Diagnostic |
|---|---:|---|---|---|---|---|
| Livre (`build/post43_recovery_20260718_final/book`) | 44 | `0DAC197F0030A67EAE87D4316664D223F3281732E88B0BD7519F5DFF23DC157C` | `336DE24F2196037236F079181BFC72626A62AF851752ACFFD1301B911D1D6436` | `00C954B1F675BD5EC41CBBF4333EDB9EF7D08CF2E197C1C9F1F3979F09F2EE11` | `42111C1348230BDC32222E414378184B7869991B599143A6A6F85933E6B9E6A3`; `01B9D3442AA25F5FAEB7D4FD987753501CFB2E917893868A5EB2B70C5DB86827` | zéro hit |
| Kapferer (`build/post43_recovery_20260718_final_microfix/kapferer`) | 6 | `F57850A0EF6331FEB952D258D2CB145A6B7D08DEA9BF47975DA7C5E6FC3C16C7` | `A1B6530EFE2744E79734709BF224299388D49DA0E0EC2066F92F4F1D757537F3` | `53984C3975A5ED62BDAF5C56EC6F92E1A3504B00D69519215D25B123685978C5` | `FE916BBE35F445EEB840F5B27C4C11A8CA7279FCED7B3754556C00D833D5393F`; `9D59A129B5A5A79EA39538CFF2E054F4888C9678F31C35C70E1F27B6E0B85ED8` | avertissement `inputenc` bénin; une boîte `Underfull` badness 1281, ligne 148, visuellement saine |
| Matières terminales (`build/post43_recovery_20260718_final/terminal`) | 4 | `712123F200CD21DDF9BA65497C905EF77BA76D2FAFB1A842A741F0CF19FFB2C5` | `ACE75736C623650F4ED13C90ABA51F30E999ADB92AD23FD97FFBC4FF95831DAE` | `6FCDD703271E407037C1DDBD5CC447CF9A80D72835D4D4BBFE0CAAF8EEB8C3B3` | `066409FAECC307E2B3A99B6A02CA65E52A3AA7E9C081A8BA577F29C8F2C91585`; `9B386792ADBCE78A06B0CD6CEA86E2C889A09E6826F43B5132E1D8CED1961530` | seul avertissement `inputenc` bénin |

Contrôle visuel Poppler 144 dpi :

- livre, pages affectées 14, 16, 20, 21, 27, 31, 34, 36, 42, 43 : SHA-256 PNG respectifs `C601630E5FB6EAD62314639EC05D0CAF360E2E07BB4AC77E7110BD2253A8C057`, `E15D11FD29645460F2100ABD1F65A24A7F56E742E06D6E80C2CF3869FD24A534`, `5BA95B9DCC3A1856FCAE77770C70F36BA64DA4499A41CCDE5D7FBBEB99F433C9`, `25FEEEF4F7F56BFA8DABF9741D4FF8F2E0FF2A19028774C9D961C120B8E7BF79`, `9D2A4FF0517B3033F10AD209F43247AE6AA334D2901D2B6F6F44D491B75E423F`, `4D7E7AD39F6E08521CE40A9FFEC5FDC478A38D98BB23C6604D7B8B510B30BC58`, `C7C035BEF8B72EE2DD37CC049ACF9B3A2A4EA594ECF98FFD00A6552F45B7AF46`, `CA0BBD106701C345F8B896B2C104DDE3B57662B9B883B0FBEE0520976C7F9DAB`, `326BE4E39CE1975C630E65458524F741589328D744AB778273743B2523C10351`, `9C2982AE69CF4B51D98A2328DD63E5E486A0ABF9327AB8BCAA189A3575B5BA6D`.
- Kapferer, pages 4--5 : `25E35F9C1AF1F80A41DC3FE880A701E60191B62903E5A397B36C3CD832D0BA4B`, `B62054501799792BBE5F0083300E35D5C4B71FA83E8CA19550FD9850608A2954`.
- matières terminales, pages 1--4 : `F813BF4A382225ABB641DB101ACE830E8B5959F1F2BF9CE82FF168F52EBC97F3`, `C1D9022ECBF4778BD7E12C7E414F8FDAA780EFC7627DC9C63232467AFD786E0E`, `502E89F0E966420E12AB261DB9E9937EB29E7A0F0708DAC5840596AAD9A04EE1`, `30349880AD1FF6E851810F5DC36CFEDEA3FD46ED30A834481F5BF663332E67FE`.
- Résultat : aucune coupure, collision, formule brisée, note illisible, corruption d'encodage ou perte de glyphe.

## Registre terminologique

- `evidence/GERMAN_FRENCH_TERMINOLOGY_LEDGER.csv` : 93 lignes de données, 93/93 avec localisateur strict R823 ou français natif exact; zéro champ vide, doublon de terme ou doublon intégral; SHA-256 `0A7B1704481609CF5C4A8B3B7B5CC03EC59ADC4E511FF39D4A0D6AF910448B77`.
- Miroir Markdown : 93 termes, zéro terme manquant ou surnuméraire; SHA-256 `CB0EEC5C7F1CEB9424EBA2730563D56A7AB2BDBF639E351B11CE70B68BD697ED`.
- Ajouts/hardening notables : `Restgruppe` → `groupe quotient`; `Diskriminante` → `discriminant`; `Wurzelzahlen` → `résolvantes de Lagrange`; `Integritätsbasis` → `base d'intégrité` avec première discussion R823 l. 4578 et définition VI l. 5369; `zweiseitig einfacher Ring` avec R823 l. 21025/21790.

## Curseur et limite de propriété

- Les corps P34 n'ont pas été corrigés dans cette passe. Le scan y relève 20 hits sur 19 lignes : 18 fois `il suit` et deux fois `se laisse` aux localisateurs `N34_intro_s01:109`, `s04:43`, `s05:35`, `s07:26`, `s09:44` (deux hits), `s09:65`, `s10:30`, `s11:26`, `s13:27,29`, `s14:21,33,79,83,119,176`, `s15:71`, `s21:62`, `s25:30`.
- Ce sont des défauts linguistiques hors propriété de cette passe; ils doivent être traités par le propriétaire P34 avec contrôle d'autorité.
- Aucun manifeste final n'a été généré ou modifié.

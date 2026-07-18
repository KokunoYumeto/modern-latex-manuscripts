# P31 — réconciliation structurelle et terminologique avec R823

Date de gel : 2026-07-17 (Europe/Berlin)

## Résultat

Le corps français de P31 a été reconstruit contre la tranche allemande R823 complète. Le déficit initial n'était pas un delta mathématique R704→R823 : R704 et R823 ont ici le même contenu mathématique. Il provenait d'une version française récupérée qui abrégeait réellement les démonstrations, notes et dispositifs mathématiques, surtout aux §§4–8.

Le fichier final passe l'audit structurel v3 du dépôt, compile seul et dans le cumul P1–31, et ses 14 pages ont été inspectées visuellement. Les calques terminologiques bloquants signalés pour P31 ont tous un résiduel nul.

## Autorités, copie de travail et sauvegarde

| Rôle | Chemin | Octets | SHA-256 |
|---|---|---:|---|
| TeX cumulatif R823 | `C:\Users\Floris\Documents\interlanguage\03_projects\noether\03_translation_workspaces\romance_rebase_20260717\authority_r823\pkg_r823\Noether_R823_WebB_R822_P20p27_31_RunInDashRefine_20260717\1\01_cumulative\Noether_R823_cum_de.tex` | 2,125,031 | `EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21` |
| Tranche allemande P31 R823 | `C:\Users\Floris\Documents\interlanguage\03_projects\noether\03_translation_workspaces\romance_rebase_20260717\work\spanish\evidence\_agent_papers\P31_de_R823.tex` | 81,066 | `FD212098954191FF9AFF83A6D1AEA2EFD9597AB0420079A2FEC0A5999FD674AC` |
| Tranche allemande P31 R704, contrôle TM | `C:\Users\Floris\Documents\interlanguage\03_projects\noether\03_translation_workspaces\romance_rebase_20260717\work\spanish\evidence\_agent_papers\P31_de_R704.tex` | 81,067 | `F220AD48124D18C711B0A9D7C34E82839F60FD93843583081B3D7AFDD15A4322` |
| Sauvegarde française avant réconciliation | `C:\Users\Floris\Documents\interlanguage\03_projects\noether\03_translation_workspaces\fr_r823_20260717\working\backups\P31_pre_R823_structural_reconciliation_20260717\tex\N31_fr_body.tex` | 69,013 | `6B72FA9F173F0EBB475DB4FE07A247E204B4D4090E17AAF3F83098BC0E0BE2E9` |
| Corps français final | `C:\Users\Floris\Documents\interlanguage\03_projects\noether\03_translation_workspaces\fr_r823_20260717\working\r823_fr\tex\N31_fr_body.tex` | 81,703 | `03C03340E8F959699F25D0736564E1FDBE1350AE41D0C7A6687200FFF90D09ED` |

La sauvegarde a été faite avant toute modification et n'a pas été altérée. Le corps final compte 535 lignes, contre 470 dans la sauvegarde.

## Diagnostic et réparation

### Audit structurel avant/après

| Mesure P31 | Avant | Après gel |
|---|---:|---:|
| caractères source | 80,004 | 80,004 |
| caractères cible | 65,861 | 78,442 |
| ratio caractères | 0.8232 | 0.9805 |
| jetons mathématiques source | 5,961 | 5,961 |
| jetons mathématiques cible | 4,075 | 5,509 |
| ratio mathématique brut | 0.6836 | 0.9242 |
| displays source / cible | 33 / 47 | 33 / 36 |
| lignes de displays source / cible | 18 / 5 | 18 / 16 |
| statut v3 | risque structurel brut | `present-structural-review` |

Les trois displays cibles excédentaires après réparation sont des formules allemandes en ligne que la mise en page française rend en display. Les deux lignes de display encore différentes sont les retours typographiques des titres allemands centrés des §§4 et 7, rendus sur une seule ligne par les sous-titres français. Elles ne représentent aucun contenu mathématique manquant.

### Matière restaurée

- Introduction : ligne d'auteur « Par Emmy Noether, à Göttingen », filet typographique, exposant exact `q=p^e`.
- §§1–3 : inventaire complet des displays confirmé; indices de sous-famille `i_\sigma`, idéal nul `\overline{0}` dans l'anneau étendu et corps d'extension `\Omega` remis en conformité avec R823.
- §4 : représentation matricielle complète, ordre des produits, note non commutative, changement de base et équivalence, classes d'idéaux/de représentations, trace, norme et démonstration complète du discriminant.
- §5 : preuve de la somme directe, matrices-blocs, anneaux/idéaux quotients, deux déterminants-blocs, produit des idéaux discriminants et passage aux extensions.
- §6 : bases spéciales et longue note de représentation, preuve pour les anneaux primaires, critère discriminantiel, déterminant des éléments conjugués et théorème final.
- §7 : cadre des ordres, preuve complète du passage modulo `p`, correspondance des décompositions, théorème du discriminant et exemple détaillé de l'idéal premier de seconde espèce.
- §8 : anneaux de multiplication, définition de l'idéal discriminant, localisés, preuve locale-globale, longue note Hilbert–Hecke, théorème général, spécialisation et clausule de Göttingen.

### Contrôle mathématique indépendant

Verdict externe indépendant communiqué par la tâche racine, coupe du 2026-07-17 : après normalisation des macros, la source possède 5,492 atomes mathématiques sémantiques et la cible 5,493; la reconstruction a rétabli +1,418 jetons mathématiques cibles réellement omis. La couverture est : introduction + 8/8 sections, 29/29 unités numérotées plus §3 2a–2c, 48/48 notes et 33/33 displays. Ce contrôle conclut également à l'absence de delta mathématique P31 entre R704 et R823.

## Décisions terminologiques françaises

Les remplacements ont été faits contextuellement, sans substitution globale aveugle.

| Calque audité | Disposition française | Occurrences contrôlées | Résiduel final |
|---|---|---:|---:|
| `Primfunktion` → « fonction première » | `polynôme irréductible séparable` ou `polynôme irréductible inséparable`, selon le sens | 5 | 0 |
| `Restklassenring` / `Restklasse` | `anneau quotient`, `corps résiduel`, `classe modulo …` selon la syntaxe | 24 expressions d'anneau; 31 occurrences du calque de classe | 0 |
| `Quotientenring` | `localisé`, `localisation`; `corps des fractions` pour `Quotientenkörper` | 8 expressions d'anneau; 2 expressions de corps supplémentaires | 0 |
| calques de domaine polynomial | `anneau de polynômes` / `anneau de polynômes quotient` | 4 blocages signalés, plus les contextes adjacents | 0 |
| « base de module » | `base du module` ou `base de X comme R-module`, scalaire conservé | 17 blocages non qualifiés, plus 7 variantes déjà qualifiées | 0 |
| `Hauptordnung` → « ordre principal » | `ordre maximal` | 20 | 0 |
| `Basispolynom` | aucune occurrence dans P31 R823 ni dans la cible | 0 | 0 |

`Hauptidealring` et les idéaux principaux restent distincts : ils demeurent respectivement « anneau principal » et « idéal principal ». Le registre mathématique français n'a donc pas confondu anneau principal et ordre maximal. Le calque « linéarité indépendante » a aussi été corrigé en « indépendance linéaire ».

## Audit structurel v3 final

Commande exécutée :

```powershell
python C:\Users\Floris\Documents\interlanguage\scripts\noether_r823_paper_structure_audit.py --language french --authority-tex C:\Users\Floris\Documents\interlanguage\03_projects\noether\03_translation_workspaces\romance_rebase_20260717\authority_r823\pkg_r823\Noether_R823_WebB_R822_P20p27_31_RunInDashRefine_20260717\1\01_cumulative\Noether_R823_cum_de.tex --target-tex C:\Users\Floris\Documents\interlanguage\03_projects\noether\03_translation_workspaces\fr_r823_20260717\working\r823_fr\tex\cum_fr_R823_COMPLETE.tex --output-csv C:\Users\Floris\Documents\interlanguage\03_projects\noether\03_translation_workspaces\fr_r823_20260717\evidence\P31_R823_STRUCTURE_POSTRECONCILIATION.csv
```

Sortie : 130 fichiers TeX cibles développés; 43 `present-structural-review`; 0 `gross-structural-risk`. Ligne P31 : 80,004/78,442 caractères (0.9805), 33/36 displays, 18/16 lignes de display, 5,961/5,509 jetons mathématiques bruts (0.9242), statut `present-structural-review` sans note.

- CSV : `C:\Users\Floris\Documents\interlanguage\03_projects\noether\03_translation_workspaces\fr_r823_20260717\evidence\P31_R823_STRUCTURE_POSTRECONCILIATION.csv`
- SHA-256 CSV : `3DC96A23A94A96360B006D2ADFA419388B083F49D1ADFE186CDAF2D4E3F3E673`
- SHA-256 du document cible développé : `6C86D2BE2AB697A11DB859BED8E147E124E04DBB7678B78097D2FEB8080D656B`

## Compilation

Les deux cibles ont été compilées par `latexmk`/MiKTeX 26.5, deux passes `pdflatex`, avec `-halt-on-error -file-line-error`. Le balayage des logs pour erreur fatale, commande indéfinie, avertissement LaTeX/package, référence/citation indéfinie, `Overfull` et `Underfull` est vide.

| Cible | Pages | Octets | SHA-256 PDF | SHA-256 log |
|---|---:|---:|---|---|
| P31 autonome | 14 | 396,379 | `85804C1D0DC10EE3966796BECB31D5062E261D1F73598CB58496CC51733181C0` | `286CE02A07F4062A9E3A971EEA32C0A611EEDDCFB383091B7E85FE3294C1C1F4` |
| Cumul P1–31 | 319 | 2,113,765 | `20DCA302CA5795F3E324530B7788D9547EC72C31C60B8B09D58665B6F07ED653` | `E9FADDEC5C15E087A7900B159FC003555E368FBBD63CABD82D9D2B193A372939` |

Répertoires :

- autonome : `C:\Users\Floris\Documents\interlanguage\03_projects\noether\03_translation_workspaces\fr_r823_20260717\working\build\P31_R823_STRUCTURAL_RECONCILIATION\unit`
- cumulatif : `C:\Users\Floris\Documents\interlanguage\03_projects\noether\03_translation_workspaces\fr_r823_20260717\working\build\P31_R823_STRUCTURAL_RECONCILIATION\cumulative`

Une première invocation, dont l'argument PowerShell avait été mal cité, a produit un répertoire littéral `working\r823_fr\tex\$o`. Cet artefact de diagnostic a été conservé; il n'est pas une cible faisant autorité. Les deux builds ci-dessus ont ensuite été recréés avec des chemins absolus explicites.

## QA visuelle

Rendu Poppler PNG à 120 ppp : les 14/14 pages autonomes et les pages cumulatives 305–319 ont été rendues. Les quatre planches-contact ont été inspectées, puis les pages autonomes denses 1, 7, 10, 12 et 14 ont été revues à leur résolution originale. Cela couvre le titre et l'appareil introductif, les matrices du §4, les blocs des §§5–6, les longues notes du §7 et la fin/localisation du §8.

Constat : aucune page blanche, coupure, collision, formule hors cadre, note tronquée, glyphe manquant ni rupture à l'entrée/sortie du cumul. Le début P31 se trouve à la page cumulative 306; sa fin, la date et le filet terminal à la page 319. La page 305, fin de P30, a été contrôlée comme frontière amont.

| Planche | SHA-256 |
|---|---|
| `P31_unit_pages_01_08_contact.png` | `6BBA722F646E14F89A2948B86347333E033A218F989CE7C48B2B1609F7A640D6` |
| `P31_unit_pages_09_14_contact.png` | `24DDD12207D5CEABDA4E387F6A17AC11F6BD6E86A10C797963F374B9B85C57D9` |
| `P31_cum_pages_305_312_contact.png` | `AB3FFD5F85DD122AC0C4F9BC0923D5C661FDCC78706B0DC7F4BD307371C10FEB` |
| `P31_cum_pages_313_319_contact.png` | `2AAEDF655D8E7C5FE1A27DFC611D976005A7C2D765F0EE3C9225EF37467221C4` |

Les 43 hachages de sources, sauvegarde, cible, audits, PDF/logs et rendus PNG sont consignés dans `C:\Users\Floris\Documents\interlanguage\03_projects\noether\03_translation_workspaces\fr_r823_20260717\evidence\P31_R823_ARTIFACT_HASHES.csv` (SHA-256 `9096495BCA4D40A3646DAB644FBFFD1DC842806430FE73BD52EF0A9B7A98BB84`).

## Curseur de continuation

`P31_COMPLETE_R823_FR_20260717`

- Fichier gelé : `N31_fr_body.tex`, SHA-256 `03C03340E8F959699F25D0736564E1FDBE1350AE41D0C7A6687200FFF90D09ED`.
- Gate P31 : source/parité, terminologie contextuelle, audit structurel, compilation autonome/cumulative et QA visuelle satisfaits.
- Aucun fichier P30, P34, P37, P38, P39 ou P40 n'a été modifié dans cette réconciliation.
- Prochaine action autorisée : intégration par la tâche racine dans son cumul R823 français global; ne pas rouvrir P31 sans nouveau delta d'autorité ou défaut de QA reproductible.

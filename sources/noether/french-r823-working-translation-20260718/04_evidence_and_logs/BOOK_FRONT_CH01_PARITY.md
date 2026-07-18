# R823 — frontispice, introduction et chapitre I (§§ 1–4)

Date de revue : 17 juillet 2026  
Statut : traduction française directe réconciliée avec R823; l'ancienne matière post44 n'est pas autorité.

## Sources et fichiers de production

- Autorité : `authority/R823/pkg_r823/Noether_R823_WebB_R822_P20p27_31_RunInDashRefine_20260717/1/01_cumulative/Noether_R823_cum_de.tex`, lignes 20985–21259.
- Autorité cumulative SHA-256 : `EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21`.
- Frontispice/table : `working/r823_fr/post43/book_frontmatter_fr.tex`, SHA-256 `63EB4DBBA51258C64FE96BE36BFACF31ECC76A7228973EA8D8ADA7EEFA550DD5`.
- Introduction/chapitre I : `working/r823_fr/post43/book_intro_ch01_fr.tex`, SHA-256 `F1693EEDEEECE010CE20556F3C89A02397E16FF06AFE4941BA302026A6775DA7`.

## Parité des cinq unités de la gate

Les hachages de source viennent du manifeste R823 gelé; ceux de cible ont été recalculés sur l'expansion TeX intégrée après la revue.

| Unité | Caractères source | SHA-256 source | Caractères cible | SHA-256 cible | Ratio |
|---|---:|---|---:|---|---:|
| `BOOK_TITLE_INTRO` | 4 784 | `EE0961B423D3DE5325AFF57DDE559CE64817FBE1CB8F1D1A1B290BC9ECA020F6` | 5 371 | `52688FB239F926722775674DA41E3DC94D99DF0E0E2D92B33A71C675679DF5DD` | 1,123 |
| `BOOK_S01` | 1 835 | `0F1710DAE06E6F55E55E84904AD8D5FA0789C3C56A057E9FBB43F955A34A3A04` | 1 849 | `C8F128905E49DB1759306E456646B2C3CC7BD3D58138DF0B78B2A30C8A3BE6E5` | 1,008 |
| `BOOK_S02` | 964 | `A3AA3EFEEBF94086BDD3A6D87D8387541EE1B354E9984A08E363C6B6D174D800` | 1 022 | `E4FFE2040507FE0FF5A595A2010369AEA32F5D0261154805E55B8101DAE64F8E` | 1,060 |
| `BOOK_S03` | 1 426 | `9D7E0692722A3C86C224ABA3F486F10586059EADB62DD25263CCC512368ED72F` | 1 440 | `86008A890ED192FBCB211F6543326069D684E3BBFCE1AE64A8E204A213D44C24` | 1,010 |
| `BOOK_S04` | 7 171 | `7D170972E675BDA90D9FFE5BD14EEA8CB4A45384BB27624AAEA3E75774B65E9F` | 7 058 | `6CD15645AAA38BBE32A8B17155016D982CCC60DAC15AB63A0055F64E387183F6` | 0,984 |

## Revue source→cible

- La table conserve les six chapitres et les 31 sections dans le même ordre, avec tous les renvois de pages historiques.
- L'introduction conserve les quatre paragraphes de R823, les deux cours de référence et le statut formellement nouveau de la représentation réciproque.
- Les §§ 1–4 ont été relus ligne à ligne sur les lignes 21061–21259 : deux définitions de représentation, deux classes, deux types de modules, les deux assertions de correspondance, la démonstration, les changements de base et toutes les formules sont présents.
- Audit structurel des §§ 1–4 : 3/3, 0/0, 2/2 et 17/20 blocs affichés; les trois affichages supplémentaires du § 4 proviennent uniquement de la mise en pages séparée de règles de calcul que l'autorité donne dans un long paragraphe mathématique. Les dix lignes d'`aligned` du § 4 sont conservées 10/10.
- Terminologie contraignante : le `reziprok ringhomomorph` qui inverse l'ordre est nommé `antihomomorphisme d'anneaux`; le cas bijectif est un `anti-isomorphisme`. L'étiquette historique `représentation réciproque` est maintenue.
- Dans la prose, `nichtkommutativer Körper/Schiefkörper` est rendu par `corps gauche`; les titres historiques explicatifs des §§ 19–21 gardent `corps non commutatif`.
- L'autorité écrit à la ligne 21091 une inclusion typographiquement impossible `C\subseteq\mathfrak D` pour une matrice-élément; la cible donne le sens mathématique requis `C\in\mathfrak D`, sans modifier l'argument.
- Aucun contenu pan-roman n'a été introduit.

## Compilation et rendu

Le composant appartient au livre complet de 44 pages documenté dans `BOOK_COMPLETE_BUILD_QA.md`; les pages de titre, de table, d'introduction, les changements de section et les pages denses du § 4 ont été inspectés. Une nouvelle passe du cumul final est requise après tout changement de hachage et sera portée dans la ledger visuelle finale.

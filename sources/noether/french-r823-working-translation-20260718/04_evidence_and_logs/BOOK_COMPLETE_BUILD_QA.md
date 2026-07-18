# Livre R823, §§ 1–31 — compilation complète et QA visuelle

Date : 17 juillet 2026  
Statut : composant post-P43 validé pour l'intégration cumulative; cette validation ne vaut pas validation du cumul P1–43.

## Périmètre et entrées

- Pilote TeX : `working/r823_fr/post43/book_complete_smoke.tex`
- SHA-256 du pilote : `987119D599E17DAA4898A403238D44B2D8A8368568D52453589B4F4CC32D242E`
- Fragments intégrés :
  - `book_frontmatter_fr.tex`
  - `book_intro_ch01_fr.tex`
  - `book_ch02_fr.tex`
  - `book_ch03_ch04_fr.tex`
  - `book_ch05_ch06_fr.tex`
- Structure : 6 chapitres, 31/31 sections numérotées.
- Prérequis explicitement exercés : `mathrsfs` pour `\mathscr`; famille sûre `\srcfn`, `\srcfnmark`, `\srcfntext` pour les notes de source.

## Normalisation terminologique finale

Les fichiers antérieurs aux corrections ont été conservés sous `backups/terminology_normalization_20260717/`.

| Fragment final | SHA-256 final | Décision exercée |
|---|---|---|
| `book_intro_ch01_fr.tex` | `F1693EEDEEECE010CE20556F3C89A02397E16FF06AFE4941BA302026A6775DA7` | `antihomomorphisme d'anneaux`, `anti-isomorphisme`; prose `corps gauche`; phrase m.r.d./m.r.r. relue |
| `book_ch03_ch04_fr.tex` | `3BD82DA55DEE5C5D299B2B8BAE605285441680670A1E839051623BCE474BAFE5` | `corps gauche` dans la prose et les énoncés; titres historiques conservés |
| `book_ch05_ch06_fr.tex` | `603FC2E8A97FDA101EB69C90F4588C152486C80E7BFB1CE57F4FD9B342DB9C28` | `anneau/corps des endomorphismes`; `corps gauche` dans la prose |

Contrôle négatif : aucune occurrence de `corps d'automorphismes`, `corps des automorphismes`, `anneau(x) des automorphismes` au sens de l'anneau d'endomorphismes ne subsiste. Les seules occurrences de `corps non commutatif(s)` conservées sont les titres historiques des §§ 19–21 et leurs entrées de table.

## Compilation reproductible

- Moteur : LuaHBTeX / LuaLaTeX 1.25.7 (MiKTeX 26.5).
- Commande, exécutée deux fois depuis `working/r823_fr/post43/` :

  `lualatex -interaction=nonstopmode -halt-on-error -file-line-error -recorder -output-directory=<build> book_complete_smoke.tex`

- Répertoire : `build/book_complete_final_20260717/`
- PDF : `book_complete_smoke.pdf`
- SHA-256 du PDF : `D7965E4B491A8A05794A3C01F1C524C5CD1691CB21552D8E0882D00B1F8ECD7C`
- Format : A4, 44 pages, 659 963 octets.
- SHA-256 du journal TeX final : `52926F4389C082C1EBBFB7D74B0A149E3C11D26C07126E37B5D882724B38C887`
- SHA-256 du fichier enregistreur `.fls` : `0DCFA9FC907C555862B5D8FAA188D869B37646E2E9CFCC39AB12A7E77C1BCFC2`.
- Le `.fls` nomme le pilote, chacun des cinq fragments et les sorties PDF/journal du même build.
- SHA-256 des sorties console des deux passes finales : `5B56DD5176E4870E54C3FCFF773951B17AA8C22762DD5B10D56B346E2CD84E4D` (sorties identiques).
- Scan du journal final : aucune erreur LaTeX, aucune commande ou référence indéfinie, aucune étiquette multiple, aucune boîte `Overfull`/`Underfull`, aucun glyphe manquant et aucun avertissement de paquet. Le chargement désormais inutile d'`inputenc` a été retiré du pilote UTF-8 natif; son état antérieur est conservé dans `working/backups/inputenc_cleanup_20260717/`.

## QA visuelle

- Rendu Poppler final à 120 ppp : `evidence/rendered_qa/book_complete_final_20260717/page-01.png` à `page-44.png` (44/44 images).
- Les trois planches couvrant les 44 pages ont été inspectées : `contact_01_16.jpg` (`2127F2D7…`), `contact_17_32.jpg` (`4D88A342…`) et `contact_33_44.jpg` (`41A9F075…`).
- Toutes les pages modifiées par la normalisation ou la dernière relecture ont ensuite été contrôlées à plus grande échelle : 3, 5, 19, 21, 24, 25, 27, 30, 32, 40 et 43. La planche correspondante a le SHA-256 `89597B7F539772DAA7B92A906B5FD44F6DE90DB8D8391341AB61B31D02B7F65B`.
- Étendue des contrôles : titres et changements de chapitre, tableaux/formules, notes en pied de page, fins de sections, pages denses et page terminale.
- Résultat : aucun chevauchement, aucune coupure de marge, aucune formule tronquée, aucun glyphe manquant ou corrompu, aucune note détachée; la pagination reste 44 pages.

Le livre est donc prêt comme composant R823 pour le cumul français final. P43 et les unités postérieures sont déjà intégrés; la gate du corpus entier reste conditionnée à la fermeture des dernières réconciliations d'articles, au build racine frais et à sa QA visuelle v3.

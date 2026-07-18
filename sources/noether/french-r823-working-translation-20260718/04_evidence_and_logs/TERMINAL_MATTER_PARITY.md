# Parité R823 — bibliographie et listes terminales

Statut : traduction/réconciliation française directe complète, contrôlée le 17 juillet 2026.

## Autorité et cible

- Autorité : `authority/R823/.../01_cumulative/Noether_R823_cum_de.tex`, lignes 23964–24121 incluses.
- Tranche normalisée LF, UTF-8 sans BOM : 158 lignes, 8 188 caractères, 8 243 octets, SHA-256 `AAF6DA0B27D6B7A152785C3AACC997672D9E765D71BE6D692E4CEB3CDDAA037C`.
- Cible : `working/r823_fr/post43/terminal_matter_fr.tex`, 164 lignes, 9 088 caractères, 9 264 octets, SHA-256 normalisé `73840187B90DA346836B46FB15B45589EE6CF27D1D77C351C8628175F9B08C99`.
- Rapport brut cible/source : `1.1099`.

## Contrôle structurel et bibliographique

- 43/43 notices dans la bibliographie numérotée, dans l'ordre R823.
- Citation séparée de l'article Kapferer avec complément commun : présente.
- 12/12 communications brèves.
- 5/5 comptes rendus.
- 2/2 livres réalisés avec la participation d'Emmy Noether.
- Les millésimes, volumes, parties et pages ont été repris de R823. La cible corrige les erreurs de la vieille mémoire, notamment les pages 20–21, 21, 81 et 11–12 ainsi que les indications de partie II.
- L'entrée Dedekind est normalisée bibliographiquement comme « E. Noether et Ø. Ore »; la coquille de lieu « Brauschweig » de l'autorité devient « Brunswick ». Ces corrections sont explicites et ne changent pas le périmètre.

## Build et QA visuelle

- Wrapper : `working/r823_fr/post43/terminal_matter_smoke.tex`.
- Commande : `lualatex -interaction=nonstopmode -halt-on-error -file-line-error`.
- Journal : `build/terminal_direct/terminal_matter_smoke.log`; sortie capturée : `build/terminal_direct/terminal_matter_build_stdout.txt`.
- Résultat : 4 pages A4, SHA-256 PDF `E82EBB1B53F5CEAEC3FE665C6B1000750DDD87D10870A0797764BE346C1E19FA`; aucune erreur TeX, aucun glyphe manquant, aucun débordement signalé. Seul avertissement : `inputenc` ignoré par LuaLaTeX.
- Rendu Poppler 144 dpi : `tmp/pdfs/terminal_direct_lualatex_final/page-1.png` à `page-4.png`.
- Les quatre pages ont été inspectées individuellement : numérotation 1–43 continue, accents et caractères `Ø`/`Œ` corrects, marges et coupures lisibles, aucune superposition ni corruption. La page 4 est volontairement clairsemée, car R823 place la liste des deux livres après un saut de page.

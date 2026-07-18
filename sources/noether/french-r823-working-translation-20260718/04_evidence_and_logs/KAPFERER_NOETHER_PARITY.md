# Parité R823 — article Kapferer–Noether et complément commun

Statut : traduction française directe complète, contrôlée le 17 juillet 2026.

## Autorité et cible

- Autorité : `authority/R823/.../01_cumulative/Noether_R823_cum_de.tex`, lignes 23718–23961 incluses.
- Tranche normalisée LF, UTF-8 sans BOM : 244 lignes, 23 242 caractères, 23 428 octets, SHA-256 `6D37CD705097E13A01AB10E2DFDE57ED06DE322C1AF06D71E9EE174B5F50C595`.
- Cible : `working/r823_fr/post43/kapferer_noether_fr.tex`, 250 lignes, 23 695 caractères, 24 314 octets, SHA-256 normalisé `DF11DD4E2C153ABA0A6A90B85B608E727A1433ED210F3DB9AC84D3B7EA03ACC0`.
- Rapport brut cible/source : `1.0195`. L'ancien post45 est conservé exclusivement comme mémoire de traduction.

## Contrôle structurel

- 18/18 blocs mathématiques affichés.
- 6/6 numéros d'équations, `(1)`–`(6)`, dans le même ordre.
- Théorèmes Ia, Ib, II, III et IV; lemmes auxiliaires I et II; compléments I et II; complément au théorème III; complément commun avec E. Noether; remarques I et II : tous présents.
- Notes de source 1)–16) : toutes présentes et uniques. La note 16 utilise intentionnellement une marque puis un texte de note séparés.
- Les 12 blocs de titre/énoncé/structure repérés dans l'autorité ont leurs 12 correspondants dans la cible.
- La mention de réception du 24 octobre 1926 est conservée.

Les singularités suivantes sont conservées parce qu'elles appartiennent à R823 : la répétition des membres (K_1,K_2) dans (3), `d(y)` après `d_i(y)`, `f(0,y)` après `f_i(0,y)`, et `q_i` là où le voisinage emploie `q^{(i)}`. Elles ne sont pas des modernisations conjecturales de la traduction.

## Build et QA visuelle

- Wrapper : `working/r823_fr/post43/kapferer_noether_smoke.tex`.
- Commande : `lualatex -interaction=nonstopmode -halt-on-error -file-line-error`.
- Journal : `build/post45_direct/kapferer_noether_smoke.log`; sortie capturée : `build/post45_direct/kapferer_noether_build_stdout.txt`.
- Résultat : 6 pages A4, SHA-256 PDF `8463E11B4FAA791D7F2720DA28FEB92DA8AC148FB231F5D5F0507B8EFBAD7B0F`; aucune erreur TeX, aucun glyphe manquant, aucun débordement signalé. Seul avertissement : `inputenc` ignoré par LuaLaTeX.
- Rendu Poppler 144 dpi : `tmp/pdfs/kapferer_direct_lualatex_final/page-1.png` à `page-6.png`.
- Les six pages ont été inspectées individuellement : texte, formules, exposants/indices, numéros d'équations et notes sont lisibles; aucune coupure, superposition ou corruption d'encodage. La page 6 ne contient que la mention de réception, conformément au saut de page terminal du fragment autonome.

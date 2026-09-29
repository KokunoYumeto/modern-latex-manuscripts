# D016 - Les constantes des équations fonctionnelles des fonctions L

Pierre Deligne, *Modular functions of one variable II*, Lecture Notes in
Mathematics349 (1973), pages501-597. Le témoin de comparaison comporte97pages
physiques, avec la note postérieure reproduite sur sa dernière page.

Ordre de lecture : D016_FR.pdf, D016_FR.tex, puis l'archive complète des sources.
L'édition anglaise correspondante est D016_EN.pdf et D016_EN.tex. Les deux
fichiers TeX contiennent tout le texte, les macros et les diagrammes TikZ ; aucun
chapitre privé ou fichier de corps de texte absent n'est nécessaire.

Vérification du témoin et mises à jour éditoriales de cette révision : OpenAI
Codex, GPT-6 Sol, effort Ultra. Les étapes antérieures restent documentées dans
les éléments de provenance conservés. Aucune relecture humaine n'est revendiquée.
Le texte distingue les lectures imprimées, les restaurations et les émendations
mathématiques ; les notes E01-E59 sont extérieures au texte de l'auteur.

La comparaison cumulée couvre toutes les pages1-97, y compris l'appendice, les
vingt références, SGA et la note postérieure. La référence[12] restitue1958,
lecture du témoin ; E59 distingue l'attestation bibliographique1968. Le témoin
original n'a pas été modifié. SOURCE/D016_SOURCE_001_097.pdf est aussi le
repli en image pour toutes les pages du témoin, séparé du lecteur composé.

## Reconstruction

Décompresser l'archive dans un dossier vide. Installer Python3 et un environnement
standard pdfLaTeX, sans téléchargement automatique de paquets pendant le contrôle.
Les paquets utilisés sont fontenc, inputenc, lmodern, amsmath, amssymb,
mathtools, geometry, enumitem, tabularx et tikz-cd. Les classes, styles et
fichiers TeX standard effectivement ouverts lors de la construction sont fournis
dans TEX_DEPENDENCIES, avec leurs noms portables et empreintes. Le moteur,
son format et les polices standard installées demeurent des prérequis du runtime ;
il ne s'agit pas d'une copie complète de la distribution TeX.

Sous Windows, exécuter `python rebuild.py`. Le script utilise exclusivement un
mutex Global\InterlanguageTeXSlotV1, une seule acquisition de30secondes et un
job capturé limité à1GiB. Il ne touche aucun autre processus. Il crée seulement
rebuild/ dans le dossier décompressé, effectue trois passes par langue, vérifie
les logs et l'identité des deux dernières passes ainsi que celle des PDF cibles.
Les noms internes Deligne_FR.tex et Deligne_EN.tex sont nécessaires pour
reproduire exactement les PDF ; leurs octets sont ceux des fichiers directs D016.
Un mutex occupé produit un échec borné, sans attente répétée ni processus lancé.

La construction de référence emploie MiKTeX26.5, pdfTeX1.40.29,
LaTeX2025-11-01, SOURCE_DATE_EPOCH=946684800 et le fuseau UTC.
Le contrôle déterministe de l'archive rejoue les noms, tailles et SHA256 inscrits
dans MANIFEST.json. Le dossier AUDIT contient les choix et contrôles, pas un
substitut au texte. Les anciens états restent historiques, avec leur portée propre.
La réussite locale du paquet n'annonce pas une nouvelle version publique de corpus.

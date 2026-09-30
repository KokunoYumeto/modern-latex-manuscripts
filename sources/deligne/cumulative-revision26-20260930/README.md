# Pierre Deligne — Sources intégrales de 39 travaux / Complete sources of 39 works

## Français

Deligne_FR.tex et Deligne_EN.tex contiennent chacun le texte intégral du corpus,
en LaTeX modifiable, et non un simple pilote d'assemblage de PDF. Le périmètre
est D001–D023, D025–D031, D033–D036, D038–D040 et D042–D043. Les quatre autres
numéros sont des lacunes d'inclusion publique, pas une absence de téléchargements.
D016 est intégré à la révision 26. Les corps mathématiques des 38 autres travaux
sont conservés ; seuls les titres courants français de D017 sont corrigés et
localisés. Les deux lecteurs cumulatifs ont passé les contrôles de compilation
et de convergence. Les changements ont fait l'objet d'une inspection visuelle
ciblée ; aucune nouvelle vérification intégrale des 39 travaux n'est revendiquée.

assets/ contient les figures et dépendances ; papers/ les sources natives et
l'appareil D042. native/D016/ contient l'édition individuelle complète, ses deux
lecteurs, le témoin de 97 pages et les dépendances TeX. Les témoins restent
distincts des éditions de lecture. Les deux fichiers cumulatifs directs ont les
mêmes octets que leurs membres dans cette archive.

Extraire toute l'archive en conservant les chemins, dans un répertoire neuf.
Installer XeLaTeX, les paquets indiqués dans les préambules, les polices de
FONT_REQUIREMENTS.txt, Python 3.11 ou ultérieur et PyMuPDF 1.27.2.3. Sous Windows :

    python build_windows.py EN FR

Le lanceur réserve Global\InterlanguageTeXSlotV1 pendant toute la compilation,
avec un unique délai borné. Il limite chaque arbre moteur à 1 Gio, interdit
shell escape et les installations automatiques, et exécute trois à quatre
passes par langue jusqu'à convergence. Il refuse de reprendre des auxiliaires
préexistants ou tronqués. Aucun échec ne provoque une relance automatique.
Un créneau occupé termine cet essai sans moteur ni boucle d'attente.
Le fichier reproductible est Deligne_EN_deterministic.pdf ou
Deligne_FR_deterministic.pdf. Le post-traitement réserve 384 Mio avant les imports
PDF et ne normalise que les bits inutilisés en fin de lignes monochromes :
aucun pixel visible ni texte n'est modifié. Les empreintes attendues figurent
dans FINAL_REPRODUCTION.json. Une autre version de PyMuPDF ou de la distribution
TeX peut modifier la sérialisation ; les classes et polices système sont des
prérequis déclarés, pas des dépendances propres au projet omises.

Pour D016 seul, consulter native/D016/README_FR.md et rebuild.py (pdfLaTeX).
L'appareil D042 conserve sa propre source complète. E01–E59 sont des notes
éditoriales, non 59 erreurs mathématiques ni des errata de l'auteur.
Comparaison D016 et intégration initiale : OpenAI Codex — GPT-6 Sol, effort Ultra.
Nouvelle vérification ciblée, réparation du lanceur et du conditionnement,
localisation des titres courants : OpenAI Codex — GPT-6.1 Sol, effort Ultra.
Les interventions antérieures conservent leurs attributions documentées ;
aucune traduction, correction ou relecture humaine n'est revendiquée.

SOURCE_MANIFEST.json lie chaque membre à sa taille et son SHA-256.
Cette archive décrit des octets locaux validés, pas une nouvelle publication.
Lignée : https://doi.org/10.5281/zenodo.20410853 ; prédécesseur public :
https://doi.org/10.5281/zenodo.22937093. D016 individuel est accessible dans
sources/deligne/d016-revision26 sur la branche GitHub codex/github-maint-20260804.

## English

Deligne_EN.tex and Deligne_FR.tex each contain the complete editable corpus,
not PDF-assembly drivers. Scope is D001–D023, D025–D031, D033–D036, D038–D040
and D042–D043. The other four numbers are public-inclusion gaps, not missing
downloads. D016 revision 26 is integrated. The other 38 mathematical bodies
are preserved; only D017's French running headers are corrected and localized.
Both cumulative readers passed compilation and convergence checks. Changed
pages received scoped visual review; no fresh full review of all 39 works is claimed.

assets/ retains figures and dependencies; papers/ native sources and D042's
apparatus. native/D016/ retains the complete standalone edition, both readers,
97-page witness and TeX dependencies. Witnesses remain separate from reading
editions. Direct cumulative TeX downloads have the same bytes as the ZIP members.

Extract everything into a fresh directory, preserving paths. Install XeLaTeX,
preamble packages, fonts in FONT_REQUIREMENTS.txt, Python 3.11+ and PyMuPDF
1.27.2.3. On Windows run:

    python build_windows.py EN FR

The launcher holds Global\InterlanguageTeXSlotV1 throughout the captured tree,
uses one bounded acquisition, caps each engine tree at 1 GiB, disables shell
escape and automatic installation, and runs three to four passes per language
until convergence. It rejects preexisting or truncated auxiliary files.
No failure automatically retries; a busy slot ends the attempt without an engine.
The reproducible outputs are Deligne_EN_deterministic.pdf and
Deligne_FR_deterministic.pdf. The postprocessor reserves 384 MiB before PDF
imports and changes only unused row-padding bits, never visible pixels or text.
FINAL_REPRODUCTION.json records expected hashes. Different PyMuPDF or TeX
versions may change serialization. System classes and fonts remain declared
prerequisites, not omitted project-specific inputs.

For standalone D016 see native/D016/README_EN.md and rebuild.py (pdfLaTeX).
D042's apparatus keeps its own complete source. E01–E59 are editorial notes,
not 59 mathematical errors or author-issued errata.
D016 comparison and initial integration: OpenAI Codex — GPT-6 Sol, Ultra effort.
Fresh scoped verification, launcher/packaging repair and French running-header
localization: OpenAI Codex — GPT-6.1 Sol, Ultra effort. Earlier work retains its
documented attribution; no human translation, correction or review is claimed.

SOURCE_MANIFEST.json binds every payload member to its size and SHA-256.
This describes accepted local bytes, not a new publication. Lineage:
https://doi.org/10.5281/zenodo.20410853; public predecessor:
https://doi.org/10.5281/zenodo.22937093. Standalone D016 is under
sources/deligne/d016-revision26 on GitHub branch codex/github-maint-20260804.

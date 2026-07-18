# P24/P25 — terminologie française canonique et réconciliation R823

Date de contrôle : 17 juillet 2026  
Portée : papier 24, introduction et §§1–7; papier 25 complet.  
Statut : texte actif réconcilié, deux cumulatifs compilés en deux passes, toutes les pages modifiées inspectées.

## Autorité et sauvegarde

- Autorité allemande cumulative R823 : `authority/R823/pkg_r823/Noether_R823_WebB_R822_P20p27_31_RunInDashRefine_20260717/1/01_cumulative/Noether_R823_cum_de.tex`; SHA-256 `EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21`.
- Extraction P24 R704 : `../romance_rebase_20260717/work/spanish/evidence/_agent_papers/P24_de_R704.tex`; SHA-256 `CB04F6BD04E5EFFC62A44B4BF43181F0E04E6E43702B4D6435157BF3F1F8E0C2`.
- Extraction P24 R823 : `../romance_rebase_20260717/work/spanish/evidence/_agent_papers/P24_de_R823.tex`; SHA-256 `68C8AF8C01AA8B2837BA72203AEDC5AB98E8809298C43142B70A6C0B1BE34AE2`.
- Sauvegarde antérieure à la révision : `working/backups/p24_p25_pre_terminology_20260717/tex` (24 fichiers; conservée, non restaurée).

| Fichier | SHA-256 sauvegarde | SHA-256 actif |
|---|---|---|
| `N24_intro_s01_fr_body.tex` | `2D8BE0974E2FBECC12C5B17F9C46FD92CB17D3EABB6277AB2C371521EFBB57C3` | `522BBAB506F5CE6B3FAABA794ABA08CC43F7F4CE4ED44D01967443611CF79F46` |
| `N24_s02_fr_body.tex` | `B439DE3F580941B2D4424109C5C1B70C1A89D66A1332BEC72983E93ED974C4E3` | `B2C0F2178171F94AA2CA4D3E66CF77BA80C1B3CFC32AB0BFF1454A03A0605BFB` |
| `N24_s03_fr_body.tex` | `17C9AFD6B18ABF76FCBF78FA3FC3575B10851802909268B6EA52BEE74867DD2B` | `9398C273B18ED739C35660F7E42B0244FA98E7FC5985040E495593099E49541D` |
| `N24_s04_fr_body.tex` | `22BD8A835215740AE4C797406CE21C37B01FD47AC8FF2DC5551D456CC848DA26` | `F52671B198DD52D0E7D2043533BFC5DEFF067B43469DCEC27032C5934A3C692B` |
| `N24_s05_fr_body.tex` | `9F0525EDD3B58B9DFBEC47A7EFA5E9C04E5E3F2927CD461CC38042F214969C2E` | `5B73AF5FC0370F44309652B6898A3C59F5A2D05875EE5BC8BD6335E447304766` |
| `N24_s06_fr_body.tex` | `A517F9C233B5B93A1EA9397740117A5E1328B3D2C6B57B40D180E5B534BE37DD` | `8D2A5B4FC598FDA5368F543A76DBBD83E925FE9ECC4F78DAB18E96D6C54E7126` |
| `N24_s07_fr_body.tex` | `A987175912A6B35F91D8B257E07FC5ADEF678B71C361B739AFBE7D6EEC5AA1C1` | `A7A8C2AE885923DD90F2C28DE84FEE0BB11127EF0EE109C04CA9D9C89ACAA576` |
| `N25_fr_body.tex` | `6A13C155AF97F1C137DCC1574EB4908AD284A517FD39CA05F0833D63F722C3DC` | `1CB6A10A9F31603EB6426C272F5ED5F6B98A1D3D892391C05AB30E9527BD6524` |

## Deux différences exactes R704 → R823 de P24

Le `git diff --no-index --unified=1` des deux extractions ci-dessus ne donne que deux hunks substantiels.

1. R823 remplace `N(\frakG_{i-1},\frakM_{i-1})` par `N(\frakG_{i-1}\mid\frakM_{i-1})`. Le texte français actif possédait déjà la barre verticale; elle est retenue dans `N24_intro_s01_fr_body.tex:86`.
2. Dans la dernière proposition du paragraphe du lemme V, R823 remplace l'indice fautif `t_{\mu\nu}` par `t_{\mu r}`. La correction est appliquée dans `N24_s03_fr_body.tex:40`. La confrontation directe avec le même passage R823 a aussi réparé les erreurs du brouillon français environnant : l'autre indéterminée est `x_{i+\lambda}` (non `x_{i+1}`), les familles pertinentes sont `u_{\mu r}` et `t_{\mu r}`, tandis que le polynôme transformé reste bien un polynôme en `x_i^{p^{f'}}`, comme dans l'allemand.

## Décisions terminologiques contextuelles

La révision a été faite occurrence par occurrence dans les huit corps TeX; aucun remplacement aveugle n'a été employé.

| Allemand R823 | Français de production | Application |
|---|---|---|
| *Primfunktion* | polynôme irréductible | Définition unique avec la glose allemande historique dans `N24_intro_s01_fr_body.tex:99`; ensuite terme français canonique. |
| *Primärfunktion* | polynôme primaire, défini comme puissance d'un polynôme irréductible | La distinction irréductible/primaire est maintenue partout; *eigentliche Primärfunktion* devient « polynôme primaire propre ». |
| *Restklassenring / Restklasse* | anneau quotient / classe modulo l'idéal nommé | *Restklassenkörper* est rendu selon le contexte par « corps des fractions de l'anneau quotient », « corps quotient » ou « corps résiduel ». |
| *Polynombereich* | anneau de polynômes | Les calques « domaine polynomial/de polynômes » sont supprimés. |
| *Basispolynom* (P25, idéal principal univarié) | générateur de l'idéal principal | Choix contextuel dans `N25_fr_body.tex:30,51`; aucune uniformisation hors contexte. |

Inventaire avant révision : P24 comportait 63 formes de type « fonction première » et 13 de type « fonction primaire »; P25, respectivement 8 et 2. Scan actif final sur P24/P25 : zéro `fonction(s) première(s)`, zéro `fonction(s) primaire(s)`, zéro `classes de restes`, zéro `domaine polynomial`, zéro `polynôme de base`. Les formes canoniques actives comptent 54 occurrences singulières/plurielles de « polynôme(s) irréductible(s) » et 15 de « polynôme(s) primaire(s) ».

Contrôle supplémentaire de *Teilring der Restklassen* : les deux occurrences R823 pertinentes sont explicitement rendues par « sous-anneau de l'anneau quotient par … » dans `N24_intro_s01_fr_body.tex:31` et `N24_s05_fr_body.tex:108`, et non par le raccourci ambigu « sous-anneau du quotient ».

Le registre terminologique a été mis à jour avec les attestations de production :

- `evidence/GERMAN_FRENCH_TERMINOLOGY_LEDGER.md`, SHA-256 `D8D1AB4E18720DAC287DC547E3209B7DAD3FF66A37497D2F4A5BFA283F9F93BA`;
- `evidence/GERMAN_FRENCH_TERMINOLOGY_LEDGER.csv`, SHA-256 `D928E12D683608B9C44BBF7FA8A9AEF5573E61183D0F75E717E4949D37D3FB28`.

## Compilation

Moteur : MiKTeX pdfTeX 1.40.29, `pdflatex -interaction=nonstopmode -halt-on-error`, deux passes par pilote, depuis `working/r823_fr/tex`.

| Pilote | PDF | Pages | SHA-256 PDF | SHA-256 journal | Scan du journal |
|---|---|---:|---|---|---|
| `cum_fr_P24s07.tex` | `build/p24_p25_terminology_20260717/cum_fr_P24s07.pdf` | 275 | `8B1EAF0AAB396295AF1C89A68C9F7BC48CE6F1B88B05CF73070B389D096DD18F` | `B7CD271CE91F1F3E2A83B6F10CAC7A31B55F5161D429986C18D8AD22D1D38113` | zéro warning/error/undefined/overfull/underfull |
| `cum_fr_P25.tex` | `build/p24_p25_terminology_20260717/cum_fr_P25.pdf` | 278 | `5FBF3D6BB37FFF6BF8E1529DA68E9BBC5AAFFCC762A05BC6BD63292DD44E7748` | `B54B7B5F8D54673EF3AF097585BDD95ACCCC5B02FF00997030812396C88CB8F6` | zéro warning/error/undefined/overfull/underfull |

Les quatre sorties console des deux passes sont conservées dans le même répertoire de build.

## Contrôle visuel

Le PDF P25 contient la totalité de P24 et P25. Toutes les pages modifiées, 257–278 incluses (22 pages), ont été rendues à 144 ppp avec Poppler et inspectées. Résultat : aucune coupure, collision, formule débordante, glyphe absent, corruption d'accent, page blanche imprévue ou anomalie de marge. La grande zone blanche de la page 278 est la fin normale de P25 après la date de réception.

Rendus : `tmp/pdfs/p24_p25_terminology_20260717/page-257.png` à `page-278.png`. Planches de contrôle :

| Planche | Pages | SHA-256 |
|---|---:|---|
| `contact_257_260.png` | 257–260 | `09E8BC51D8395981A0FCC2F9A7B083A4E63FDFCD2CEE11BA048712148028C36A` |
| `contact_261_264.png` | 261–264 | `0B411576061C8E245D39D11CD5BCF3B660FBB9B4E9D3797ADB3AC3114E13B8B4` |
| `contact_265_268.png` | 265–268 | `A4F4726E8D22DBECA60371C7977CF28835740AFFAEB66552C68FC6BEEBF56867` |
| `contact_269_272.png` | 269–272 | `8759355E04487836C758781ED51616C95CA6E85BF77C0DEE9E59459AF92225EF` |
| `contact_273_276.png` | 273–276 | `3C0DB524BA876E6EA8DE8EB02992033FA1A45DA53B4C69C21F31CC71885DA63C` |
| `contact_277_278.png` | 277–278 | `595ECA8C9FF1C9ED3A0B87DA53C25640E0CBF6E14F82698480D44D5E3FAA2F91` |

Après l'explicitation finale de « sous-anneau de l'anneau quotient », les pages touchées 258 et 271 ont été rerendues et inspectées individuellement (`page-258.png`, SHA-256 `D0B334F3C5B0684DA97869A587C7824ED5E7336A00C5335CA283DC0CC7DDCCEB`; `page-271.png`, SHA-256 `BA4D941673C0E0C859DBE9B033E2173E9DFB079B2FD7888542AEBBF96108AB9D`). Les pages 277 et 278 ont aussi été inspectées individuellement (`page-277.png`, SHA-256 `D620D9F9A70E7749C09ABAA7F96C728C5FAE8B50EA05C2BF8A894004AA68A382`; `page-278.png`, SHA-256 `62495F550C80792E7CACCD27DBBFE19E55A801A931EEE7CC7F86EDED36A41C5A`).

## Conclusion

P24 et P25 sont terminologiquement canoniques dans le français mathématique moderne demandé, les deux seules différences exactes P24 R704→R823 sont explicitement disposées, les erreurs d'indices adjacentes du brouillon ont été réparées d'après R823, et le résultat est compilé et contrôlé visuellement.

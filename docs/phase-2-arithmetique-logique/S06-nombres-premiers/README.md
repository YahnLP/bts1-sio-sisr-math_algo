# S06 – Nombres premiers et décomposition

| Élément | Détail |
|---|---|
| **Niveau** | BTS SIO option SISR, 1re année – mathématiques pour l'informatique |
| **Séance** | S06 (séance 6 sur 19) – Phase 2 |
| **Durée** | 4 heures |
| **Chapitre du programme** | Arithmétique – nombres premiers, décomposition en facteurs premiers |
| **Prérequis** | S05 (divisibilité, PGCD). |
| **Outils** | Papier, calculatrice, éditeur Python intégré au site |

> [!NOTE]
> **Question qui guide la séance :** *« Comment reconnaître un nombre premier et décomposer un entier en facteurs premiers de façon fiable ? »*

## Objectifs

À la fin de la séance, l'étudiant est capable de :

1. **Définir** un nombre premier et **justifier** qu'il suffit de tester les diviseurs jusqu'à \(\sqrt{n}\) ;
2. **Dresser** la liste des nombres premiers jusqu'à \(N\) par le crible d'Ératosthène ;
3. **Décomposer** un entier en produit de facteurs premiers ;
4. **En déduire** le PGCD, le PPCM et le nombre de diviseurs ;
5. **Programmer** un test de primalité et une décomposition.

## Contenu de la séance

| Document | Rôle |
|---|---|
| [Cours – Nombres premiers](01-cours.md) | Cours |
| [Exercices – Primalité, décomposition, crible](02-exercices.md) | Exercices |
| [TP Python – Premiers et décomposition](03-tp-python.md) | TP (éditeur Python intégré) |
| [Aide-mémoire – Nombres premiers](04-aide-memoire.md) | Aide-mémoire |

## Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Rappel** S05 et accroche : « 91 est-il premier ? » | Oral |
| 0 h 20 – 1 h 30 | **Cours** : primalité, crible, décomposition, applications | Cours et questions |
| 1 h 30 – 2 h 45 | **Exercices** | Individuel, puis binômes |
| 2 h 45 – 3 h 45 | **TP Python** : crible, décomposition, premiers palindromes | Individuel |
| 3 h 45 – 4 h 00 | **Auto-évaluation** | Individuel |

*Durées indicatives : la séance dure 4 h ; l'enseignant ajuste selon le rythme du groupe.*

## Application en informatique

Les nombres premiers servent à la cryptographie à clé publique (S07 en donne un avant-goût avec les congruences) et au hachage (tailles de tables).

## Évaluation

- Feuille d'exercices corrigée, scripts du TP validés.
- Auto-évaluation « Je sais faire » en fin d'exercices.

<details markdown="1">
<summary>Notes pour l'enseignant</summary>

- **Programme :** le chapitre est rattaché au programme officiel de mathématiques pour l'informatique (voir [Programme et épreuve E3](../../ressources/programme-e3.md)) ; la répartition en séances est une proposition à valider.
- Le programme prévoit des algorithmes de recherche de nombres premiers et de factorisation en travaux pratiques.

</details>

# S16 – Graphes : représentations, chemins et niveaux

| Élément | Détail |
|---|---|
| **Niveau** | BTS SIO option SISR, 1re année – mathématiques pour l'informatique |
| **Séance** | S16 (séance 16 sur 19) – Phase 4 |
| **Durée** | 4 heures |
| **Chapitre du programme** | Théorie des graphes |
| **Prérequis** | S09 (ensembles, relations), S13 (matrices). |
| **Outils** | Papier, calculatrice, éditeur Python intégré au site |

> [!NOTE]
> **Question qui guide la séance :** *« Comment représenter un réseau, des dépendances ou des étapes par un graphe, et compter ses chemins ? »*

## Objectifs

À la fin de la séance, l'étudiant est capable de :

1. **Représenter** un graphe orienté fini simple par un dessin, un tableau de successeurs, une matrice d'adjacence ;
2. **Reconnaître** chemin, circuit, boucle, chemin hamiltonien ;
3. **Interpréter** les puissances de la matrice d'adjacence (nombre de chemins de longueur \(p\)) ;
4. **Calculer** la fermeture transitive avec des produits booléens ;
5. **Déterminer** les niveaux d'un graphe sans circuit.

## Contenu de la séance

| Document | Rôle |
|---|---|
| [Cours – Graphes](01-cours.md) | Cours |
| [Exercices – Graphes, matrices d’adjacence et chemins](02-exercices.md) | Exercices |
| [TP Python – Matrice d’adjacence et chemins](03-tp-python.md) | TP (éditeur Python intégré) |
| [Aide-mémoire – Graphes](04-aide-memoire.md) | Aide-mémoire |

## Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Accroche** : dessiner les dépendances entre services d'une infrastructure | Oral |
| 0 h 20 – 1 h 35 | **Cours** : vocabulaire, représentations, puissances, niveaux | Cours et questions |
| 1 h 35 – 2 h 50 | **Exercices** | Individuel, puis binômes |
| 2 h 50 – 3 h 45 | **TP Python** : matrice d'adjacence, puissances, fermeture | Individuel |
| 3 h 45 – 4 h 00 | **Auto-évaluation** | Individuel |

*Durées indicatives : la séance dure 4 h ; l'enseignant ajuste selon le rythme du groupe.*

## Application en informatique

Topologie d'un réseau, ordre de démarrage de services interdépendants, détection de dépendances circulaires.

## Évaluation

- Feuille d'exercices corrigée, scripts du TP validés.
- Auto-évaluation « Je sais faire » en fin d'exercices.

<details markdown="1">
<summary>Notes pour l'enseignant</summary>

- **Programme :** le chapitre est rattaché au programme officiel de mathématiques pour l'informatique (voir [Programme et épreuve E3](../../ressources/programme-e3.md)) ; la répartition en séances est une proposition à valider.
- **Corrigé :** dans `corriges/` à la racine du dépôt (hors du site publié).
- Le programme précise que, dans une évaluation, tout énoncé sur ces algorithmes doit indiquer la méthode à suivre : les exercices le font.

</details>

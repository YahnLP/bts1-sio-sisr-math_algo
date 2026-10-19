# Aide-mémoire – Écrire, tester et déboguer

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S18*

> Un mot ou un sigle inconnu ? Passe la souris dessus, ou ouvre le [glossaire](../../ressources/glossaire.md).

## De l'énoncé au programme

1. Entrées, sortie. 2. Exemple à la main. 3. Schéma. 4. Pseudo-code, puis Python. 5. Tests.

| Schéma | Initialisation | Remarque |
|---|---|---|
| Compteur | `n = 0` | `n = n + 1` dans le `if` |
| Accumulateur | `s = 0` | `s = s + x` |
| Recherche avec arrêt | `return -1` **après** la boucle | `return i` dans la boucle |
| Maximum | `m = t[0]` | liste non vide ; `>` strict = première apparition |
| Série consécutive | `courante = 0`, `meilleure = 0` | mise à jour de `meilleure` dans la boucle |

## Jeux de tests

Cas normal, vide, un élément, valeurs égales ou à la frontière, toujours vrai, jamais vrai, début et fin.

## Suivi de variables

Une ligne par tour, une colonne par variable ; chercher le **premier** écart avec ce qui est attendu.

## Erreurs classiques

| Erreur | Réflexe |
|---|---|
| Indice hors domaine | indices de 0 à \(n - 1\) ; `range(len(t))` |
| Parcours qui oublie le début | `range(len(t))`, pas `range(1, len(t))` |
| Mauvaise initialisation | `m = t[0]` pour un maximum |
| Arrêt trop tôt | `return False` dans la boucle, `return True` après |
| Boucle infinie | le variant doit changer à chaque tour |
| Égalité de flottants | tolérance, entiers ou `Fraction` |
| Division entière | multiplier avant de diviser, ou `/` |
| Effet de bord | `list(l)` pour travailler sur une copie |

---
render_macros: true
---

# TP Python – Récursivité, comptage d’opérations et débogage

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S18*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

## Exercice A – Trois fonctions récursives

Écris `somme(n)`, `puissance(x, n)` et `pgcd(a, b)` **de façon récursive** (sans boucle).

**J'anticipe.** Quel est le cas de base de chaque fonction ? Quelle valeur décroît à chaque appel ?

{{ IDE('recursion', MAX="+") }}

## Exercice B – Binaire

Écris `binaire_rec(n)` (récursive) et `binaire_iter(n)` (avec une boucle) pour \(n \ge 0\) ; `binaire(0)` vaut `"0"`.

{{ IDE('binaire', MAX="+") }}

## Exercice C – Fibonacci

Écris `fib_rec(n)`, `fib_iter(n)` et `appels_fib(n)` : le nombre d'appels que fait `fib_rec(n)` (1 pour `n < 2`, sinon 1 plus les appels de `n - 1` et de `n - 2`).

**Je comprends.** Compare `appels_fib(20)` à `20`, nombre d'additions de la version itérative.

{{ IDE('fibonacci', MAX="+") }}

## Exercice D – Compter les comparaisons

Écris `recherche_sequentielle(t, x)` et `dichotomie(t, x)` qui renvoient `(indice, comparaisons)` (indice `-1` si `x` est absent ; on compte une comparaison à chaque test d'égalité de `x` avec un élément).

**Je comprends.** Pour un tableau trié de 1 000 éléments, quel est le nombre maximal de comparaisons de chaque algorithme ?

{{ IDE('comptage', MAX="+") }}

## Exercice E – Déboguer

Les trois fonctions de `debug.py` sont incorrectes. Fais passer les tests en les corrigeant. Pour chacune, écris en commentaire l'erreur trouvée :

- `maximum(t)` : valeur maximale d'une liste non vide ;
- `somme_positifs_moyenne(t)` : moyenne des valeurs strictement positives (0 s'il n'y en a pas) ;
- `trie_sans_modifier(t)` : renvoie une copie triée **sans modifier** `t`.

{{ IDE('debug', MAX="+") }}

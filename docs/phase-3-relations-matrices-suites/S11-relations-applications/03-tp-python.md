---
render_macros: true
---

# TP Python – Relations et applications sur des ensembles finis

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S11*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

Dans ce TP, une **relation** est un ensemble de couples (`{(1, 2), (2, 2)}`) et une **application** est un dictionnaire (`{1: "a", 2: "b"}`) dont les clés forment l'ensemble de départ.

## Exercice A – Produit cartésien

Écris `produit(a, b)` qui renvoie l'ensemble des couples `(x, y)` avec `x` dans `a` et `y` dans `b`.

**J'anticipe.** Combien de couples pour `a` de 3 éléments et `b` de 4 ? Que renvoie `produit(a, set())` ?

{{ IDE('produit', MAX="+") }}

## Exercice B – Propriétés d'une relation

Écris `est_reflexive(r, e)`, `est_symetrique(r)`, `est_antisymetrique(r)` et `est_transitive(r)`. `r` est un ensemble de couples, `e` l'ensemble sur lequel on travaille.

**Je comprends.** Pour la transitivité, pourquoi faut-il deux boucles imbriquées sur les couples ? Quelle propriété est vraie « à vide » pour la relation vide ?

{{ IDE('proprietes', MAX="+") }}

## Exercice C – Classes d'équivalence

Écris `classes(r, e)` qui renvoie la liste des classes d'équivalence (des ensembles) d'une relation d'équivalence `r` sur `e`, rangées par plus petit élément croissant.

{{ IDE('classes', MAX="+") }}

## Exercice D – Injective, surjective, bijective

Écris `est_injective(f)`, `est_surjective(f, b)` et `est_bijective(f, b)` pour une application `f` (dictionnaire) d'ensemble d'arrivée `b`.

**Je comprends.** Pourquoi peut-on tester l'injectivité en comparant le nombre de valeurs distinctes au nombre de clés ?

{{ IDE('injectivite', MAX="+") }}

## Exercice E – Images, réciproque et composée

Écris `image_directe(f, x)`, `image_reciproque(f, y)`, `composee(g, f)` (le dictionnaire de \(g \circ f\)) et `reciproque(f)` (l'application réciproque d'une bijection, ou `None` si `f` n'est pas injective).

{{ IDE('composition', MAX="+") }}

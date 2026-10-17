---
render_macros: true
---

# TP Python – Ensembles en Python

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S09*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

## Exercice A – Quantificateurs sur une liste

Écris `pour_tout(pred, liste)` et `il_existe(pred, liste)` qui renvoient `True` ou `False` selon que le prédicat `pred` (une fonction) est vrai pour **tous** les éléments, ou pour **au moins un**. Sans utiliser `all` ni `any`. Que renvoie `pour_tout(pred, [])` ? Et `il_existe(pred, [])` ?

**J'anticipe.** Pour la liste `[3, 5, 7, 9]` et le prédicat « est impair » : quelle est la valeur de chacune des deux fonctions ? Même question avec « est premier ».

{{ IDE('pour_tout', MAX="+") }}

{{ IDE('il_existe', MAX="+") }}

## Exercice B – L'ordre des quantificateurs

La relation d'accès est un ensemble de couples `(utilisateur, serveur)`. Écris `chacun_a_un_serveur(acces, utilisateurs, serveurs)` (\(\forall u\, \exists s\)) et `un_serveur_pour_tous(acces, utilisateurs, serveurs)` (\(\exists s\, \forall u\)).

**Je comprends.** Construis une relation où la première est vraie et la seconde fausse. Peut-on en construire une où c'est l'inverse ?

{{ IDE('ordre_quantificateurs', MAX="+") }}

## Exercice C – Opérations sur les ensembles

Écris `operations(a, b)` qui renvoie le tuple `(intersection, réunion, différence a \ b, différence symétrique)` sous forme d'ensembles Python, **sans** utiliser les opérateurs `&`, `|`, `-`, `^` (utilise des boucles et le test `in`).

{{ IDE('operations', MAX="+") }}

## Exercice D – Les parties d'un ensemble

Écris `parties(elements)` qui renvoie la liste des parties de la liste `elements` (chaque partie est un ensemble). Utilise les nombres de 0 à \(2^n - 1\) : le bit de rang `i` de `k` dit si `elements[i]` est dans la partie numéro `k`.

{{ IDE('parties', MAX="+") }}

## Exercice E – Groupes communs

Écris `groupes_communs(groupes, u, v)` qui renvoie l'ensemble des **noms** de groupes auxquels appartiennent à la fois les utilisateurs `u` et `v`. `groupes` est un dictionnaire `nom → ensemble de membres`.

{{ IDE('groupes_communs', MAX="+") }}

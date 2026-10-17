---
render_macros: true
---

# TP Python – Seuils et sommes avec Python

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S15*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

## Exercice A – Termes et sommes

Écris `terme_arith(u0, r, n)`, `terme_geom(u0, q, n)`, `somme_arith(u0, r, n)` (somme de \(u_0\) à \(u_n\), par la formule) et `somme_geom(u0, q, n)` (idem, en traitant \(q = 1\) à part). Pour des résultats exacts, les tests utilisent des entiers ou des `Fraction`.

**J'anticipe.** Pour \(u_0 = 7\), \(r = 4\), \(n = 10\) : que valent \(u_{10}\) et la somme ? Vérifie avec le cours.

{{ IDE('formules_suites', MAX="+") }}

## Exercice B – Suite par récurrence

Écris `suite(f, u0, n)` qui renvoie la liste \([u_0, u_1, \dots, u_n]\) pour la suite définie par \(u_{k+1} = f(u_k)\).

**Je comprends.** Pourquoi la liste contient-elle \(n + 1\) termes ?

{{ IDE('suite_recurrente', MAX="+") }}

## Exercice C – Seuils

Écris `seuil_croissant(u0, q, limite)` (plus petit \(n\) tel que \(u_0 q^n \ge\) `limite`, avec \(q > 1\)) et `seuil_decroissant(u0, q, limite)` (plus petit \(n\) tel que \(u_0 q^n \le\) `limite`, avec \(0 < q < 1\)). Les tests utilisent des `Fraction` pour des calculs exacts.

**Je comprends.** Quel est le variant de la boucle ? Que se passerait-il avec \(q = 1\) ?

{{ IDE('seuils', MAX="+") }}

## Exercice D – Vérifier une formule

Écris `somme_termes(f, a, b)` (somme de `f(k)` pour \(k\) de `a` à `b` inclus) puis utilise-la dans la console pour contrôler \(1 + \dots + n = n(n+1)/2\) pour \(n\) de 1 à 50.

{{ IDE('somme_termes', MAX="+") }}

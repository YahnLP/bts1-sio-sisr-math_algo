---
render_macros: true
---

# TP Python – Chiffrement, clés de contrôle et parcours circulaires

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S07*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

## Exercice A – Puissance modulo \(n\)

Écris `puissance_mod(a, k, n)` qui calcule \(a^k \bmod n\) en **réduisant à chaque tour** (la valeur reste inférieure à \(n\)), sans utiliser `**` ni `pow`.

**J'anticipe.** Pour `puissance_mod(7, 100, 10)`, quelle réponse attends-tu ? Quelle propriété du cours te permet de la prévoir ?

{{ IDE('puissance_mod', MAX="+") }}

## Exercice B – Inverse modulo \(n\)

Écris `inverse_mod(a, n)` qui renvoie l'inverse de `a` modulo `n` (un entier entre 1 et `n - 1`) ou `None` s'il n'existe pas : essaie les valeurs `x` de 1 à `n - 1`.

**Je comprends.** Pour quelles valeurs de `a` la fonction renvoie-t-elle `None` quand `n = 12` ? Compare avec le PGCD.

{{ IDE('inverse_mod', MAX="+") }}

## Exercice C – Chiffre affine

Complète `chiffrer(texte, a, b)` et `dechiffrer(texte, a, b)` pour un texte en **majuscules** (les autres caractères restent inchangés). `ord("A")` vaut 65 : le rang d'une lettre est `ord(lettre) - 65`.

{{ IDE('affine', MAX="+") }}

**Je comprends.** Vérifie que `dechiffrer(chiffrer(t, 5, 8), 5, 8)` redonne `t`. Que se passe-t-il avec `a = 13` ?

## Exercice D – Clé du numéro de sécurité sociale

Écris `cle_nir(numero)` qui reçoit les 13 premiers chiffres (un entier) et renvoie la clé \(97 - (N \bmod 97)\).

{{ IDE('cle_nir', MAX="+") }}

## Exercice E – ISBN-13

Écris `isbn13_valide(code)` qui reçoit un texte de 13 chiffres et renvoie `True` si la somme pondérée (poids 1, 3, 1, 3, …) est un multiple de 10.

{{ IDE('isbn13', MAX="+") }}

## Exercice F – Parcours d'une liste circulaire

Écris `cases_visitees(n, k)` qui renvoie l'ensemble des cases visitées en partant de 0 par sauts de `k` dans une liste de `n` cases, jusqu'à revenir en 0. Compare avec le PGCD.

{{ IDE('cases_visitees', MAX="+") }}

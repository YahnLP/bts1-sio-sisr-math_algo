---
render_macros: true
---

# TP Python – Inverse par la méthode de Gauss en Python

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S14*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

Les calculs utilisent des **fractions exactes** (`Fraction`) pour éviter les erreurs d'arrondi des décimaux : `Fraction(1, 2) + Fraction(1, 3)` vaut exactement `Fraction(5, 6)`.

## Exercice A – Matrice identité et produit

Écris `identite(n)` et `produit(a, b)` (ils servent à tout vérifier). Les coefficients peuvent être des `Fraction`.

{{ IDE('base_matrices', MAX="+") }}

## Exercice B – Vérifier un inverse

Écris `est_inverse(a, b)` qui renvoie `True` si \(AB = I\) et \(BA = I\).

**J'anticipe.** Pourquoi vérifier les deux produits ? (pour des matrices carrées l'un suffit, mais il est utile de comprendre pourquoi le test complet est plus sûr à écrire.)

{{ IDE('verifier_inverse', MAX="+") }}

## Exercice C – Inverse par la méthode des lignes

Écris `inverse(a)` qui renvoie l'inverse de la matrice carrée `a` (liste de listes d'entiers) sous forme de matrice de `Fraction`, ou `None` si elle n'est pas inversible. Suis la méthode du cours : colonne par colonne, choisir un pivot non nul (échanger des lignes si besoin), le ramener à 1, annuler le reste de la colonne, en appliquant **les mêmes opérations** à la matrice identité.

**Je comprends.** À quel moment la fonction détecte-t-elle qu'une matrice n'est pas inversible ?

{{ IDE('inverse', MAX="+") }}

## Exercice D – Résoudre un système

Écris `resoudre(a, b)` qui renvoie la liste des solutions (en `Fraction`) du système \(AX = B\) (`b` : liste des seconds membres), ou `None` si \(A\) n'est pas inversible. Utilise `inverse`.

{{ IDE('resoudre', MAX="+") }}

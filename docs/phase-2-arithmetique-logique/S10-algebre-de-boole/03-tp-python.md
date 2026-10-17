---
render_macros: true
---

# TP Python – Circuits, tableaux de Karnaugh et masques

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S10*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

## Exercice A – Les mintermes d'une fonction

Écris `mintermes(f, n)` qui renvoie la liste des numéros de lignes (de 0 à \(2^n - 1\), l'ordre de la table de vérité) pour lesquelles la fonction `f` de `n` arguments vaut 1. Le numéro de ligne `k` donne les valeurs des variables par son écriture binaire sur `n` bits (le bit de poids fort est la première variable).

**J'anticipe.** Pour `f = lambda a, b, c: (a and c) or not b`, quelles lignes attends-tu ? Compare à l'exercice 3 des exercices.

{{ IDE('mintermes', MAX="+") }}

## Exercice B – Vérifier une simplification

Écris `meme_fonction(f, g, n)` qui renvoie `True` si `f` et `g` donnent le même résultat sur les \(2^n\) combinaisons. Utilise-la pour contrôler tes simplifications de la feuille d'exercices.

**Je comprends.** Pourquoi suffit-il de tester les \(2^n\) combinaisons pour être sûr de l'égalité de deux expressions ? Pourquoi ne peut-on pas faire de même avec des nombres entiers ?

{{ IDE('meme_fonction', MAX="+") }}

## Exercice C – Tout avec des NAND

Écris `non_nand`, `et_nand`, `ou_nand` et `xor_nand` en n'utilisant que la fonction `nand` fournie.

{{ IDE('portes_nand', MAX="+") }}

## Exercice D – Additionneur

Écris `additionneur_complet(a, b, c)` qui renvoie `(somme, retenue)` pour trois bits (0 ou 1), à l'aide de `^`, `&` et `|`. Puis écris `additionne(x, y)` qui additionne deux chaînes de bits de même longueur et renvoie la somme sur une position de plus. Exemple : `additionne("0110", "0111")` donne `"01101"` (6 + 7 = 13).

{{ IDE('additionneur', MAX="+") }}

## Exercice E – Masques et adresses

Écris les fonctions de `masques.py` : `prefixe_vers_masque(n)` (par exemple `26` donne `"255.255.255.192"`), `adresse_reseau(ip, masque)` (ET bit à bit octet par octet), `diffusion(ip, masque)` (les bits de machine mis à 1) et `nb_machines(n)` (adresses utilisables pour le préfixe `n`).

**Je comprends.** Pourquoi retire-t-on 2 au nombre d'adresses du réseau ?

{{ IDE('masques', MAX="+") }}

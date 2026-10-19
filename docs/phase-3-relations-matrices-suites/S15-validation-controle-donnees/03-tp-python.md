---
render_macros: true
---

# TP Python – Validation et contrôle de données

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S15*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

## Exercice A – Valider des formats

Complète `est_octet(s)`, `ipv4_valide(s)` et `mac_valide(s)`. N'utilise pas d'expression régulière : parcours les chaînes avec des boucles et des tests.

**J'anticipe.** Que renvoie `ipv4_valide("192.168.10.77.1")` ? Quelle règle est violée ?

{{ IDE('validation', MAX="+") }}

## Exercice B – Bit de parité

Complète `bit_parite(bits)`, `ajoute_parite(bits)` (qui renvoie une **nouvelle** liste) et `mot_valide(mot)`.

**Je comprends.** Pourquoi `mot_valide` peut-il s'écrire avec `bit_parite` ? Que valent `bit_parite([])` et `mot_valide([])` ?

{{ IDE('parite', MAX="+") }}

## Exercice C – Parité à deux dimensions

Complète `lignes_incorrectes(g)`, `colonnes_incorrectes(g)` et `corrige(g)`. La grille contient déjà ses bits de parité (dernière ligne et dernière colonne).

**Je comprends.** Que doit faire `corrige` si deux lignes sont fausses ? Pourquoi ne peut-on pas corriger dans ce cas ?

{{ IDE('parite_2d', MAX="+") }}

## Exercice D – Sommes de contrôle

Complète `somme_controle(octets)`, `trame_valide(octets, c)` et `xor_controle(octets)`.

**J'anticipe.** Pour `[10, 20, 30]`, quelle est la somme de contrôle ? Vérifie avec le cours.

{{ IDE('controle', MAX="+") }}

## Pour aller plus loin

Dans la console, écris une fonction `ajoute_erreur(octets, i)` qui inverse un bit d'un octet (opérateur `^` avec une puissance de 2) et vérifie qu'une somme de contrôle détecte toute erreur sur **un seul** bit.

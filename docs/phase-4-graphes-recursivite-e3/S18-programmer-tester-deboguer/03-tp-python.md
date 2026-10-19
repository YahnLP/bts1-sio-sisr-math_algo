---
render_macros: true
---

# TP Python – Relevés et débogage

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S18*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

## Exercice A – Analyser des relevés

Complète `nb_alertes(releves, seuil)`, `premiere_alerte(releves, seuil)`, `plus_longue_serie(releves, seuil)` et `ecart_max(releves)`. Un relevé est *en alerte* s'il est **strictement** supérieur au seuil.

**J'anticipe.** Pour `[21, 25, 27, 26, 31, 32, 33, 24, 29, 30]` et le seuil 25, quels résultats attends-tu pour les quatre fonctions ?

**Je comprends.** Pourquoi `plus_longue_serie` met-elle `meilleure` à jour **dans** la boucle et pas seulement quand la série s'arrête ?

{{ IDE('releves', MAX="+") }}

## Exercice B – Déboguer (1)

Les trois fonctions de `debug.py` sont incorrectes. Fais passer les tests en les corrigeant. Pour chacune, écris en commentaire l'erreur trouvée :

- `maximum(t)` : valeur maximale d'une liste non vide ;
- `somme_positifs_moyenne(t)` : moyenne des valeurs strictement positives (0 s'il n'y en a pas) ;
- `trie_sans_modifier(t)` : renvoie une copie triée **sans modifier** `t`.

{{ IDE('debug', MAX="+") }}

## Exercice C – Déboguer (2)

Même consigne pour `debug2.py` :

- `compte_pairs(t)` : nombre d'éléments pairs de `t` ;
- `est_croissant(t)` : `True` si `t` est rangé dans l'ordre croissant (au sens large) ;
- `pourcentage(partie, total)` : pourcentage de `partie` dans `total` (0 si `total` vaut 0).

**Je comprends.** Pour chaque erreur, quel test du jeu de tests la révèle ? Quel tableau de suivi la ferait apparaître ?

{{ IDE('debug2', MAX="+") }}

## Pour aller plus loin

Dans la console, écris **avant** de coder trois tests pour une fonction `pic(connexions)` qui renvoie `(valeur, indice)` du premier maximum (exercice 8 de la feuille d'exercices), puis écris la fonction.

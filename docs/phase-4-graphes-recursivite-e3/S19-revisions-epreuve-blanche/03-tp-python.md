---
render_macros: true
---

# TP Python – Auto-évaluation et exercices de programmation

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S19*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

Ces trois exercices reprennent le type de programmation de l'épreuve : une fonction à écrire à partir d'un énoncé, avec des tests.

## Exercice A – Première série en alerte

Écris `premiere_serie(releves, seuil, k)` : l'indice du premier relevé de la première série d'au moins `k` relevés consécutifs strictement supérieurs au seuil (avec `k >= 1`), ou `-1`.

**J'anticipe.** Pour `[30, 10, 30, 31, 32, 10]`, le seuil 25 et `k = 3`, quel résultat attends-tu ?

{{ IDE('serie_alerte', MAX="+") }}

## Exercice B – Journal

Écris `compte_erreurs(lignes)` : un dictionnaire adresse → nombre de lignes de niveau `ERROR`. Puis `adresse_la_plus_active(lignes)` : l'adresse qui a le plus d'erreurs (la plus petite dans l'ordre alphabétique en cas d'égalité), ou `None` s'il n'y a pas d'erreur.

{{ IDE('journal_erreurs', MAX="+") }}

## Exercice C – Bilan de relevés

Écris `bilan_releves(releves, seuil)` qui renvoie un quadruplet `(minimum, maximum, nombre de relevés en alerte, pourcentage de relevés en alerte)` pour une liste non vide.

**Je comprends.** Pourquoi faut-il écrire `n * 100 / len(releves)` et non `n // len(releves) * 100` ?

{{ IDE('bilan_releves', MAX="+") }}

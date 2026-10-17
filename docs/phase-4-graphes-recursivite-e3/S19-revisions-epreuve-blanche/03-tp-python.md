---
render_macros: true
---

# TP Python – Auto-évaluation et exercices de programmation

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S19*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

Ces trois exercices reprennent le type de programmation de l'épreuve : une fonction à écrire à partir d'un énoncé, avec des tests.

## Exercice A – Seuil

Écris `premier_mois(v0, q, capacite)` : le plus petit entier \(n\) tel que `v0 * q**n >= capacite` (avec \(q > 1\)).

**J'anticipe.** Pour `v0 = 120`, `q = 1.08` en fraction (`Fraction(27, 25)`) et `capacite = 200`, quel résultat attends-tu ?

{{ IDE('premier_mois', MAX="+") }}

## Exercice B – Journal

Écris `compte_erreurs(lignes)` : un dictionnaire adresse → nombre de lignes de niveau `ERROR`. Puis `adresse_la_plus_active(lignes)` : l'adresse qui a le plus d'erreurs (la plus petite dans l'ordre alphabétique en cas d'égalité), ou `None` s'il n'y a pas d'erreur.

{{ IDE('journal_erreurs', MAX="+") }}

## Exercice C – Bilan de stockage

Écris `volumes(v0, q, n)` (liste de \(V_0, \dots, V_n\)) et `bilan(v0, q, capacite)` qui renvoie un couple `(mois_de_saturation, volume_ce_mois)`.

**Je comprends.** Quelle est la différence entre la liste des volumes jusqu'au mois \(n\) et le nombre d'éléments qu'elle contient ?

{{ IDE('bilan_stockage', MAX="+") }}

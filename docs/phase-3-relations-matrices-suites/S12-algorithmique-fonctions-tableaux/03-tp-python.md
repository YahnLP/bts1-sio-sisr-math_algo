---
render_macros: true
---

# TP Python – Tableaux, chaînes et journaux

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S12*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

## Exercice A – Moyenne et maximum

Écris `moyenne(t)`, `maximum(t)` et `indice_du_max(t)` (premier indice du maximum) pour une liste non vide de nombres. N'utilise ni `sum`, ni `max`, ni `index`.

**J'anticipe.** Pour `[14, 3, 27, 9, 27, 5]`, quels résultats attends-tu pour les trois fonctions ?

{{ IDE('statistiques', MAX="+") }}

## Exercice B – Rechercher

Écris `position(t, x)` (premier indice de `x`, ou `-1`), `compte(t, x)` (nombre d'occurrences) et `dichotomie(t, x)` (indice de `x` dans la liste **triée** `t`, ou `-1`).

**Je comprends.** Que se passe-t-il si tu appelles `dichotomie` sur une liste non triée ?

{{ IDE('recherche', MAX="+") }}

## Exercice C – Trier

Écris `tri_selection(t)` qui renvoie une **nouvelle** liste triée, sans modifier `t` et sans `sorted` ni `sort`.

**Je comprends.** Pourquoi commence-t-on par `r = list(t)` ?

{{ IDE('tri', MAX="+") }}

## Exercice D – Tableaux à deux dimensions

Écris `somme_lignes(g)`, `somme_colonnes(g)` et `transposee(g)` pour une grille rectangulaire (liste de listes).

{{ IDE('grille', MAX="+") }}

## Exercice E – Chaînes

Écris `inverse(s)`, `est_palindrome(s)` (sans tenir compte des majuscules) et `acronyme(phrase)` (les initiales en majuscules : `"systèmes et réseaux"` donne `"SER"`).

{{ IDE('chaines', MAX="+") }}

## Exercice F – Exploiter un journal

Chaque ligne d'un journal a la forme `date heure adresse événement compte`. Écris `echecs_par_adresse(lignes)` (dictionnaire adresse → nombre de lignes dont l'événement est `LOGIN_FAILED`) et `adresses_suspectes(lignes, seuil)` (liste triée des adresses ayant **au moins** `seuil` échecs).

{{ IDE('journal', MAX="+") }}

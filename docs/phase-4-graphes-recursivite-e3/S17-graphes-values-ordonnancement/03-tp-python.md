---
render_macros: true
---

# TP Python – Dates au plus tôt et au plus tard en Python

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S17*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

Un graphe valué est un dictionnaire `{(origine, arrivée): valeur}` ; un projet est un dictionnaire `{tâche: (durée, [prédécesseurs])}`.

## Exercice A – Dijkstra

Écris `dijkstra(arcs, source, sommets)` qui renvoie `(distance, predecesseur)` (deux dictionnaires), puis `reconstruire(predecesseur, cible)` qui renvoie la liste des sommets du chemin de la source à `cible`. Pour « l'infini », utilise `float("inf")`.

**J'anticipe.** Dans le graphe du cours, quelle valeur attends-tu pour `T` ? Par quels sommets passe le chemin ?

{{ IDE('dijkstra', MAX="+") }}

## Exercice B – Dates au plus tôt

Écris `dates_au_plus_tot(taches)` qui renvoie un dictionnaire tâche → date au plus tôt. Tant que toutes les dates ne sont pas calculées, traite les tâches dont tous les prédécesseurs ont une date.

**Je comprends.** Pourquoi la boucle `while` s'arrête-t-elle quand le projet n'a pas de circuit ? Et sinon ?

{{ IDE('plus_tot', MAX="+") }}

## Exercice C – Marges et chemin critique

Écris `analyse(taches)` qui renvoie `(duree_projet, marges_totales, critiques)` : la durée minimale, le dictionnaire des marges totales, et la liste **triée** des tâches critiques. Les dates au plus tôt sont fournies par `dates_au_plus_tot`.

{{ IDE('analyse_projet', MAX="+") }}

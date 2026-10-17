---
render_macros: true
---

# TP Python – Matrice d’adjacence et chemins en Python

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S16*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

Un graphe à \(n\) sommets numérotés de 0 à \(n - 1\) est représenté par sa **matrice d'adjacence** (liste de listes de 0 et de 1).

## Exercice A – Matrice d'adjacence

Écris `matrice_adjacence(n, arcs)` (liste de couples), `successeurs(m, i)` (liste triée) et `demi_degres(m)` qui renvoie `(exterieurs, interieurs)`.

**J'anticipe.** Pour les arcs `[(0, 1), (0, 2), (1, 3)]` avec `n = 4`, écris la matrice puis les demi-degrés.

{{ IDE('graphe_base', MAX="+") }}

## Exercice B – Compter les chemins

Écris `produit(a, b)` et `nb_chemins(m, p, i, j)` (nombre de chemins de longueur `p` de `i` à `j`, par la puissance `p` de la matrice).

**Je comprends.** Que renvoie `nb_chemins(m, 0, i, j)` ?

{{ IDE('nb_chemins', MAX="+") }}

## Exercice C – Détecter un circuit

Écris `a_un_circuit(m)` : le graphe a un circuit si et seulement si la puissance \(n\) de `m` (\(n\) = nombre de sommets) n'est pas la matrice nulle. Justifie-le dans un commentaire : un chemin de longueur \(n\) passe par \(n + 1\) sommets.

{{ IDE('circuit', MAX="+") }}

## Exercice D – Fermeture transitive

Écris `fermeture(m)` : somme **booléenne** de \(M, M^{[2]}, \dots, M^{[n-1]}\) (produit booléen : `ou` de `et`).

{{ IDE('fermeture', MAX="+") }}

## Exercice E – Niveaux

Écris `niveaux(m)` qui renvoie la liste des niveaux (chaque niveau est une liste de sommets) ou `None` si le graphe a un circuit. Méthode : retirer à chaque tour les sommets sans prédécesseur parmi ceux qui restent.

**Je comprends.** Pourquoi la boucle est-elle sûre de s'arrêter ?

{{ IDE('niveaux', MAX="+") }}

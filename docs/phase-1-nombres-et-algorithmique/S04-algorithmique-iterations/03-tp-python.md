---
render_macros: true
---

# TP Python – Boucles en Python

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S04*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

## Exercice A – Somme des carrés

Écris `somme_carres(n)` qui renvoie \(1^2 + 2^2 + \dots + n^2\).

**J'anticipe.** Pour `n = 4`, écris la trace de `s` sur ta feuille avant de coder.

{{ IDE('somme_carres', MAX="+") }}

## Exercice B – Factorielle

Écris `factorielle(n)` (\(n \ge 0\)) avec une boucle. Rappel : \(0! = 1\).

{{ IDE('factorielle', MAX="+") }}

## Exercice C – Chiffres d'un nombre

Écris `somme_chiffres(n)` et `nombre_chiffres(n)` pour un entier \(n \ge 0\) (avec `nombre_chiffres(0)` égal à 1), sans utiliser `str`.

{{ IDE('chiffres', MAX="+") }}

## Exercice D – Seuil de saturation

Un volume de sauvegardes double chaque mois à partir de 1 Go. Écris `mois_avant_saturation(capacite)` qui renvoie le plus petit nombre de mois \(k\) tel que le volume \(2^k\) Go **atteint ou dépasse** la capacité (en Go) du disque.

**Je comprends.** Quel est le variant de ta boucle ? Pourquoi s'arrête-t-elle ?

{{ IDE('saturation', MAX="+") }}

## Exercice E – Adresses d'une plage

Écris `plage(prefixe, debut, fin)` qui renvoie la liste des adresses `prefixe.k` pour \(k\) de `debut` à `fin` inclus, par exemple `plage("192.168.1", 10, 12)` donne `["192.168.1.10", "192.168.1.11", "192.168.1.12"]`.

{{ IDE('plage', MAX="+") }}

## Exercice F – Syracuse

Écris `syracuse(n)` qui renvoie le nombre d'étapes pour atteindre 1 à partir de \(n \ge 1\) (si \(n\) est pair on prend \(n/2\), sinon \(3n+1\)).

{{ IDE('syracuse', MAX="+") }}

**Je comprends.** Pourquoi ne peut-on pas affirmer, comme pour une boucle `POUR`, que cette boucle s'arrête ?

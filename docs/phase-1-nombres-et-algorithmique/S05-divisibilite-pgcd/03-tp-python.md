---
render_macros: true
---

# TP Python – L'algorithme d'Euclide en Python

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S05*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

## Exercice A – La division euclidienne sans `//` ni `%`

Écris `division_euclidienne(a, b)` (\(a \ge 0\), \(b > 0\)) qui renvoie le couple `(q, r)` en retranchant `b` tant que c'est possible.

**J'anticipe.** Pour `a = 17` et `b = 5`, combien de soustractions ? Quel est le variant de ta boucle ?

{{ IDE('division_euclidienne', MAX="+") }}

## Exercice B – Diviseurs

Écris `diviseurs(n)` (\(n \ge 1\)) qui renvoie la liste **croissante** des diviseurs positifs de `n`.

{{ IDE('diviseurs', MAX="+") }}

## Exercice C – PGCD par l'algorithme d'Euclide

Écris `pgcd(a, b)` avec une boucle `while`, sans utiliser `math.gcd`.

**Je comprends.** Que renvoie `pgcd(7, 0)` ? `pgcd(0, 7)` ? Justifie avec l'algorithme.

{{ IDE('pgcd', MAX="+") }}

## Exercice D – PPCM et nombres premiers entre eux

À l'aide de `pgcd`, écris `ppcm(a, b)` et `premiers_entre_eux(a, b)`.

{{ IDE('ppcm', MAX="+") }}

## Exercice E – Compter les étapes

Écris `nombre_divisions(a, b)` qui renvoie le nombre de divisions euclidiennes effectuées par l'algorithme d'Euclide jusqu'au reste nul (pour `(252, 198)`, quatre divisions : voir le cours).

{{ IDE('nombre_divisions', MAX="+") }}

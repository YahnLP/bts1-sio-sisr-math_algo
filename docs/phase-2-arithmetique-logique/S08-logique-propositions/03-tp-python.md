---
render_macros: true
---

# TP Python – Vérifier une équivalence par énumération

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S08*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

## Exercice A – Toutes les combinaisons de valeurs

Écris `combinaisons(n)` qui renvoie la liste des \(2^n\) combinaisons de `n` booléens, sous forme de tuples, dans l'ordre de la table de vérité (`False` avant `True`, la **première** variable change le moins vite). Indice : le numéro de ligne `k`, écrit en binaire sur `n` bits (S01), donne les valeurs.

**J'anticipe.** Que doit renvoyer `combinaisons(2)` ? Quelle ligne de la table correspond à `k = 2` ?

{{ IDE('combinaisons', MAX="+") }}

## Exercice B – Équivalence par énumération

À l'aide de `combinaisons`, écris `equivalentes(f, g, n)` qui renvoie `True` si les fonctions `f` et `g` (à `n` arguments booléens) donnent le même résultat sur toutes les combinaisons.

{{ IDE('equivalentes', MAX="+") }}

**Je comprends.** Vérifie avec `equivalentes` les lois de De Morgan et l'équivalence \(p \Rightarrow q \equiv \neg p \vee q\). Quelle différence avec une preuve par table sur papier ?

## Exercice C – Tautologie et comptage

Écris `est_tautologie(f, n)` et `nombre_de_vrais(f, n)`.

{{ IDE('tautologie', MAX="+") }}

## Exercice D – La règle de pare-feu

Écris `autorise(protocole, port)` qui applique la règle \((t \wedge (a \vee b)) \vee i\) de l'exercice 7.

{{ IDE('autorise', MAX="+") }}

## Exercice E – Table de vérité affichée

Écris `afficher_table(f, n)` qui affiche une ligne par combinaison, avec `V` ou `F` (essaie avec `lambda p, q: p and q`).

{{ IDE('afficher_table', MAX="+") }}

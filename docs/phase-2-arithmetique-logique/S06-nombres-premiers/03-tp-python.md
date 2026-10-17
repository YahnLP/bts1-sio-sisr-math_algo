---
render_macros: true
---

# TP Python – Chercher et décomposer des nombres premiers

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S06*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

## Exercice A – Test de primalité

Écris `est_premier(n)`. Teste les diviseurs de 2 à \(\sqrt{n}\) : la condition de la boucle est `d * d <= n`.

**J'anticipe.** Pour `n = 91`, quels diviseurs seront testés et à quel moment s'arrête la boucle ?

{{ IDE('est_premier', MAX="+") }}

## Exercice B – Le crible d'Ératosthène

Écris `crible(N)` qui renvoie la liste des nombres premiers inférieurs ou égaux à \(N\), à l'aide d'une liste de booléens.

{{ IDE('crible', MAX="+") }}

## Exercice C – Décomposition en facteurs premiers

Écris `decomposition(n)` qui renvoie un dictionnaire `{premier: exposant}`, par exemple `{2: 3, 3: 2, 5: 1}` pour 360.

**Je comprends.** Pourquoi suffit-il de boucler tant que `d * d <= n` et de traiter le reste à part ?

{{ IDE('decomposition', MAX="+") }}

## Exercice D – Nombre de diviseurs

Écris `nombre_de_diviseurs(n)` à partir de la décomposition (produit des exposants augmentés de 1).

{{ IDE('nombre_de_diviseurs', MAX="+") }}

## Exercice E – Premiers palindromes

Un nombre est un **palindrome** si son écriture décimale se lit de la même façon dans les deux sens (131, 757…). Écris `premiers_palindromes(N)` qui renvoie la liste croissante des nombres premiers palindromes inférieurs ou égaux à \(N\).

{{ IDE('premiers_palindromes', MAX="+") }}

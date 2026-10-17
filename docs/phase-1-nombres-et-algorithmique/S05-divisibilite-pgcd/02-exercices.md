# Exercices – Division euclidienne, diviseurs, PGCD

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S05*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**, avec la méthode du cours : écris les étapes, pas seulement le résultat. Ouvre ensuite « Voir la réponse » pour te corriger. À l'épreuve, **aucune réponse sans justification** n'est complète.

## Exercice 1 – Divisions euclidiennes

Effectuer la division euclidienne de \(a\) par \(b\) et écrire \(a = bq + r\) : \((a, b) = (100, 7)\), \((7, 100)\), \((2\,024, 24)\), \((-23, 6)\).

<details markdown="1">
<summary>Voir la réponse</summary>

| \((a, b)\) | Écriture |
|---|---|
| (100, 7) | \(100 = 7 \times 14 + 2\) |
| (7, 100) | \(7 = 100 \times 0 + 7\) |
| (2024, 24) | \(2024 = 24 \times 84 + 8\) |
| (-23, 6) | \(-23 = 6 \times -4 + 1\) |

Pour \((-23, 6)\) : le reste doit rester entre 0 et 5, donc le quotient est \(-4\) (et non \(-3\)).

</details>

## Exercice 2 – Vrai ou faux ?

Justifier chaque réponse (preuve ou contre-exemple).

1. Si \(6 \mid n\), alors \(3 \mid n\).
2. Si \(4 \mid n\) et \(6 \mid n\), alors \(24 \mid n\).
3. Si \(a \mid b\) et \(a \mid c\), alors \(a \mid (2b - 3c)\).
4. \(0\) divise \(5\).

<details markdown="1">
<summary>Voir la réponse</summary>

1. **Vrai** : \(n = 6k = 3 \times (2k)\).
2. **Faux** : \(n = 12\) est divisible par 4 et par 6, mais pas par 24. (Il est divisible par \(\operatorname{PPCM}(4, 6) = 12\).)
3. **Vrai** : si \(b = ak\) et \(c = ak'\), alors \(2b - 3c = a(2k - 3k')\).
4. **Faux** : \(0 \mid b\) signifie \(b = 0 \times k = 0\) ; seul \(0\) est divisible par \(0\).

</details>

## Exercice 3 – Critères de divisibilité

Sans effectuer de division, dire par lesquels des nombres 2, 3, 4, 5, 9, 10 chacun des entiers suivants est divisible : 4 536, 1 990, 2 024.

<details markdown="1">
<summary>Voir la réponse</summary>

| \(n\) | par 2 | par 3 | par 4 | par 5 | par 9 | par 10 | Somme des chiffres |
|---|---|---|---|---|---|---|---|
| 4 536 | oui | oui | oui | non | oui | non | 18 |
| 1 990 | oui | non | non | oui | non | oui | 19 |
| 2 024 | oui | non | oui | non | non | non | 8 |

Exemple de justification pour 4 536 : la somme des chiffres vaut \(4+5+3+6 = 18\), multiple de 9 (donc de 3) ; ses deux derniers chiffres, 36, sont divisibles par 4.

</details>

## Exercice 4 – Diviseurs

1. Lister les diviseurs de 84 et de 90.
2. En déduire leurs diviseurs communs et \(\operatorname{PGCD}(84, 90)\).
3. Combien de diviseurs positifs possède 36 ? Les regrouper par paires \((d, 36/d)\).

<details markdown="1">
<summary>Voir la réponse</summary>

1. Diviseurs de 84 : 1, 2, 3, 4, 6, 7, 12, 14, 21, 28, 42, 84. Diviseurs de 90 : 1, 2, 3, 5, 6, 9, 10, 15, 18, 30, 45, 90.
2. Communs : 1, 2, 3, 6 ; \(\operatorname{PGCD}(84, 90) = 6\).
3. 36 a 9 diviseurs : (1, 36), (2, 18), (3, 12), (4, 9), (6, 6) (le diviseur 6 est son propre partenaire, puisque \(36 = 6^2\)).

</details>

## Exercice 5 – Algorithme d'Euclide

Calculer avec l'algorithme d'Euclide, en posant chaque division : \(\operatorname{PGCD}(756, 540)\), \(\operatorname{PGCD}(1\,071, 462)\), \(\operatorname{PGCD}(17, 5)\). Dire si les entiers sont premiers entre eux.

<details markdown="1">
<summary>Voir la réponse</summary>

**PGCD(756, 540)**

| Étape | Division euclidienne |
|---|---|
| 1 | 756 = 540 × 1 + 216 |
| 2 | 540 = 216 × 2 + 108 |
| 3 | 216 = 108 × 2 + 0 |

\(\operatorname{PGCD}(756, 540) = 108\) : non premiers entre eux.

**PGCD(1 071, 462)** = 21 (voir le cours).

**PGCD(17, 5)**

| Étape | Division euclidienne |
|---|---|
| 1 | 17 = 5 × 3 + 2 |
| 2 | 5 = 2 × 2 + 1 |
| 3 | 2 = 1 × 2 + 0 |

\(\operatorname{PGCD}(17, 5) = 1\) : **premiers entre eux**.

</details>

## Exercice 6 – Écrans

1. Quelle est la taille du plus grand carré qui découpe exactement un écran de \(1\,366 \times 768\) pixels ?
2. Même question pour \(1\,920 \times 1\,200\) pixels. Quel est le rapport largeur : hauteur après simplification ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(\operatorname{PGCD}(1\,366, 768) = 2\) : le plus grand carré a 2 pixels de côté (\(1\,366 = 2 \times 683\) et \(768 = 2^8 \times 3\), 683 est premier avec 768).
2. \(\operatorname{PGCD}(1\,920, 1\,200) = 240\) ; \(1\,920 / 240 = 8\) et \(1\,200 / 240 = 5\), soit un rapport \(8 : 5\) (c'est le rapport 8 : 5, ou 16 : 10).

</details>

## Exercice 7 – PPCM

1. Calculer \(\operatorname{PPCM}(12, 18)\) et \(\operatorname{PPCM}(15, 25)\) avec la relation \(\operatorname{PGCD} \times \operatorname{PPCM} = a \times b\).
2. Une sauvegarde complète a lieu tous les 12 jours et une vérification d'intégrité tous les 18 jours. Elles ont lieu ensemble le jour 0. Dans combien de jours coïncident-elles de nouveau ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(\operatorname{PPCM}(12, 18) = \dfrac{12 \times 18}{6} = 36\) ; \(\operatorname{PPCM}(15, 25) = \dfrac{15 \times 25}{5} = 75\).
2. Au bout de \(\operatorname{PPCM}(12, 18) = 36\) jours.

</details>

## Exercice 8 – Démonstration

Montrer que si \(a > b > 0\), alors \(\operatorname{PGCD}(a, b) = \operatorname{PGCD}(a - b, b)\). En déduire une version de l'algorithme d'Euclide qui n'utilise que des **soustractions**. L'appliquer à \((a, b) = (48, 18)\).

<details markdown="1">
<summary>Voir la réponse</summary>

Un entier \(d\) qui divise \(a\) et \(b\) divise \(a - b\). Réciproquement, un entier qui divise \(a - b\) et \(b\) divise \(a = (a - b) + b\). Les couples \((a, b)\) et \((a - b, b)\) ont les mêmes diviseurs communs, donc le même PGCD.

Algorithme : tant que \(a \ne b\), remplacer le plus grand des deux par la différence ; à la fin, \(a = b\) = PGCD. Pour \((48, 18)\) :

| a | b |
|---|---|
| 48 | 18 |
| 30 | 18 |
| 12 | 18 |
| 12 | 6 |
| 6 | 6 |

Le PGCD est 6. Cette version est plus lente quand \(a\) est très grand devant \(b\) : par exemple \((1\,000, 3)\) demande de nombreuses soustractions là où une seule division suffit.

</details>


## Je sais faire

Coche honnêtement ; ce que tu ne coches pas se reprend avant la séance suivante.

- [ ] Faire une division euclidienne et écrire \(a = bq + r\) ;
- [ ] Appliquer les critères de divisibilité ;
- [ ] Calculer un PGCD par Euclide et poser les étapes ;
- [ ] Dire si deux entiers sont premiers entre eux ;
- [ ] Calculer un PPCM.

**Ce que je dois reprendre :** ______________________

**Ma question à poser à l'enseignant :** ______________________

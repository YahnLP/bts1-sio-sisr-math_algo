# Exercices – Suites arithmétiques et géométriques, limites

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S15*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**, avec la méthode du cours : écris les étapes, pas seulement le résultat. Ouvre ensuite « Voir la réponse » pour te corriger. À l'épreuve, **aucune réponse sans justification** n'est complète.

## Exercice 1 – Premiers termes

1. Calculer \(u_0, \dots, u_4\) pour \(u_n = 2n^2 - 3\).
2. Calculer \(v_0, \dots, v_5\) pour \(v_0 = 3\), \(v_{n+1} = 2v_n + 1\). Conjecturer \(v_n\) en fonction de \(n\), puis le démontrer.

<details markdown="1">
<summary>Voir la réponse</summary>

1. -3, -1, 5, 15, 29.
2. 3, 7, 15, 31, 63, 127. Chaque terme est une puissance de 2 moins 1 : on conjecture \(v_n = 2^{n+2} - 1\) (vérifié pour \(n\) de 0 à 20). Si \(v_n = 2^{n+2} - 1\), alors \(v_{n+1} = 2(2^{n+2} - 1) + 1 = 2^{n+3} - 1\) : c'est la formule au rang \(n + 1\).

</details>

## Exercice 2 – Arithmétique

La suite \((u_n)\) est arithmétique, \(u_0 = 7\), \(r = 4\).

1. Calculer \(u_{10}\).
2. Calculer \(u_0 + u_1 + \dots + u_{10}\).
3. Pour quel rang \(u_n = 103\) ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(u_{10} = 7 + 10 \times 4 = 47\).
2. 11 termes : \(11 \times \dfrac{7 + 47}{2} = 297\).
3. \(7 + 4n = 103 \iff n = \dfrac{96}{4} = 24\).

</details>

## Exercice 3 – Géométrique

La suite \((u_n)\) est géométrique, \(u_0 = 5\), \(q = 3\). Calculer \(u_6\) et \(u_0 + \dots + u_6\).

<details markdown="1">
<summary>Voir la réponse</summary>

\(u_6 = 5 \times 3^6 = 5 \times 729 = 3645\). Somme : \(5 \times \dfrac{3^7 - 1}{3 - 1} = 5 \times \dfrac{2186}{2} = 5465\).

</details>

## Exercice 4 – Reconnaître

Dire si chaque suite est arithmétique, géométrique ou ni l'une ni l'autre, et donner la raison :

(a) 3, 7, 11, 15, … ; (b) 2, 6, 18, 54, … ; (c) 1, 4, 9, 16, … ; (d) \(u_n = 5 \times 2^n\) ; (e) \(u_n = 5n + 2\) ; (f) \(u_0 = 1\), \(u_{n+1} = u_n + n\).

<details markdown="1">
<summary>Voir la réponse</summary>

(a) Arithmétique, \(r = 4\). (b) Géométrique, \(q = 3\). (c) Ni l'une ni l'autre : différences 3, 5, 7 et rapports \(4,\ 2{,}25,\ \dots\) non constants. (d) Géométrique, \(q = 2\). (e) Arithmétique, \(r = 5\). (f) Ni l'une ni l'autre : \(u_{n+1} - u_n = n\) n'est pas constant (termes de \(u_0\) à \(u_5\) : 1, 1, 2, 4, 7, 11).

</details>

## Exercice 5 – Volume de sauvegardes

1. Un serveur contient 40 Go et gagne 5 Go par mois. Donner \(u_n\) et le premier mois où il atteint 200 Go.
2. Un autre contient 100 Go et grossit de 3 % par mois. Donner \(v_n\) et le premier mois où il atteint 200 Go.

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(u_n = 40 + 5n\) ; \(40 + 5n \ge 200 \iff n \ge 32\) : au mois **32** (exactement 200 Go).
2. \(v_n = 100 \times 1{,}03^n\). En calcul exact : \(v_{23} \approx 197,36 < 200\) et \(v_{24} \approx 203,28 \ge 200\) : mois **24**.

</details>

## Exercice 6 – Sommes

Calculer : (a) \(1 + 2 + \dots + 50\) ; (b) \(1 + 2 + \dots + 99\) et le comparer au nombre de comparaisons du tri par sélection de 100 éléments ; (c) \(1 + 2 + 4 + \dots + 2^9\) ; (d) \(1 + \frac12 + \dots + \frac{1}{2^{10}}\).

<details markdown="1">
<summary>Voir la réponse</summary>

(a) \(\dfrac{50 \times 51}{2} = 1275\). (b) \(\dfrac{99 \times 100}{2} = 4950\) = \(\dfrac{n(n-1)}{2}\) pour \(n = 100\). (c) \(2^{10} - 1 = 1023\). (d) \(2 - \dfrac{1}{1024} = \dfrac{2047}{1024}\).

</details>

## Exercice 7 – Variations et limites

Pour chaque suite, étudier le sens de variation à l'aide de \(u_{n+1} - u_n\) ou de la raison, et conjecturer la limite :

(a) \(u_n = 3 + \dfrac{1}{n}\) (\(n \ge 1\)) ; (b) \(u_n = 2n + 1\) ; (c) \(u_n = (0{,}5)^n\) ; (d) \(u_n = (-2)^n\) ; (e) \(u_n = 10 - 3n\).

<details markdown="1">
<summary>Voir la réponse</summary>

| Suite | Variation | Limite |
|---|---|---|
| (a) | décroissante (\(1/n\) diminue) | 3 |
| (b) | croissante (arithmétique, \(r = 2\)) | \(+\infty\) |
| (c) | décroissante (géométrique, \(0 < q < 1\)) | 0 |
| (d) | alternée (\(q < 0\)) | pas de limite : 1, -2, 4, -8, 16, -32… |
| (e) | décroissante (arithmétique, \(r = -3\)) | \(-\infty\) |

</details>

## Exercice 8 – Seuil

On place 1 000 € à 5 % par an.

1. Dérouler l'algorithme de seuil du cours pour les premières années (tableau).
2. À partir de quelle année dépasse-t-on 2 000 € ?
3. Même question avec 1 200 € perdant 20 % par an : à partir de quelle année passe-t-on sous 300 € ?

<details markdown="1">
<summary>Voir la réponse</summary>

1–2. | \(n\) | \(u_n\) (€) | \(u_n < 2000\) ? |
|---|---|---|
| 0 | 1000,00 | oui |
| 1 | 1050,00 | oui |
| 2 | 1102,50 | oui |
| 3 | 1157,63 | oui |
| 5 | 1276,28 | oui |
| 10 | 1628,89 | oui |
| 14 | 1979,93 | oui |
| 15 | 2078,93 | non | La boucle s'arrête à \(n = 15\).
3. \(n = 7\) (valeur \(≈ 251,66\) €).

</details>


## Je sais faire

Coche honnêtement ; ce que tu ne coches pas se reprend avant la séance suivante.

- [ ] Calculer les premiers termes d'une suite ;
- [ ] Donner le terme général d'une suite arithmétique ou géométrique ;
- [ ] Calculer une somme de termes consécutifs ;
- [ ] Comparer les croissances de \(n^2\), \(2^n\), \(\ln n\) ;
- [ ] Écrire un algorithme de seuil.

**Ce que je dois reprendre :** ______________________

**Ma question à poser à l'enseignant :** ______________________

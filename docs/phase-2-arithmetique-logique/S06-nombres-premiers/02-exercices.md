# Exercices – Primalité, décomposition, crible

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S06*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**, avec la méthode du cours : écris les étapes, pas seulement le résultat. Ouvre ensuite « Voir la réponse » pour te corriger. À l'épreuve, **aucune réponse sans justification** n'est complète.

## Exercice 1 – Premier ou composé ?

Dire si chaque entier est premier ; s'il est composé, donner une factorisation : 51, 53, 57, 59, 91, 97, 101, 119, 121, 143, 221, 223.

<details markdown="1">
<summary>Voir la réponse</summary>

| \(n\) | Résultat |
|---|---|
| 51 | composé : 3 × 17 |
| 53 | **premier** |
| 57 | composé : 3 × 19 |
| 59 | **premier** |
| 91 | composé : 7 × 13 |
| 97 | **premier** |
| 101 | **premier** |
| 119 | composé : 7 × 17 |
| 121 | composé : 11 × 11 |
| 143 | composé : 11 × 13 |
| 221 | composé : 13 × 17 |
| 223 | **premier** |

Pour conclure qu'un nombre est premier, on teste les premiers jusqu'à \(\sqrt{n}\) : par exemple pour 223, \(\sqrt{223} \approx 14.93\), on teste 2, 3, 5, 7, 11, 13 : aucun ne divise 223.

</details>

## Exercice 2 – Crible

Dresser la liste des nombres premiers inférieurs ou égaux à 60 avec le crible d'Ératosthène. Quels nombres premiers faut-il utiliser pour barrer ?

<details markdown="1">
<summary>Voir la réponse</summary>

Comme \(\sqrt{60} \approx 7.75\), il suffit de barrer les multiples de 2, 3, 5, 7. Les nombres premiers inférieurs à 60 sont : 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59 (17 nombres).

</details>

## Exercice 3 – Décompositions

Décomposer en produit de facteurs premiers : 84, 360, 1 001, 1 024, 2 024, 5 040.

<details markdown="1">
<summary>Voir la réponse</summary>

| \(n\) | Décomposition |
|---|---|
| 84 | \(2^{2} \times 3 \times 7\) |
| 360 | \(2^{3} \times 3^{2} \times 5\) |
| 1 001 | \(7 \times 11 \times 13\) |
| 1 024 | \(2^{10}\) |
| 2 024 | \(2^{3} \times 11 \times 23\) |
| 5 040 | \(2^{4} \times 3^{2} \times 5 \times 7\) |

</details>

## Exercice 4 – Nombre de diviseurs

Sans les lister, donner le nombre de diviseurs de 360, de 1 024 et de 5 040. Vérifier le premier en listant les diviseurs.

<details markdown="1">
<summary>Voir la réponse</summary>

- \(360 = 2^{3} \times 3^{2} \times 5\) : \((3+1) \times (2+1) \times (1+1) = 24\) diviseurs.
- \(1\,024 = 2^{10}\) : \((10+1) = 11\) diviseurs.
- \(5\,040 = 2^{4} \times 3^{2} \times 5 \times 7\) : \((4+1) \times (2+1) \times (1+1) \times (1+1) = 60\) diviseurs.

Vérification pour 360 : 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 60, 72, 90, 120, 180, 360 (24 diviseurs).

</details>

## Exercice 5 – PGCD et PPCM par la décomposition

Calculer le PGCD et le PPCM de 84 et 90, puis de 360 et 756 en utilisant les décompositions en facteurs premiers.

<details markdown="1">
<summary>Voir la réponse</summary>

**84 et 90** : \(84 = 2^{2} \times 3 \times 7\), \(90 = 2 \times 3^{2} \times 5\).

| Premier \(p\) | exposant dans 84 | exposant dans 90 | min | max |
|---|---|---|---|---|
| 2 | 2 | 1 | 1 | 2 |
| 3 | 1 | 2 | 1 | 2 |
| 5 | 0 | 1 | 0 | 1 |
| 7 | 1 | 0 | 0 | 1 |

\(\operatorname{PGCD} = 2^{1} \times 3^{1} = 6\) ; \(\operatorname{PPCM} = 2^{2} \times 3^{2} \times 5^{1} \times 7^{1} = 1260\). Contrôle : \(6 \times 1260 = 7560 = 84 \times 90 = 7560\).

**360 et 756** : \(\operatorname{PGCD} = 36\), \(\operatorname{PPCM} = 7 560\) (voir le cours).

</details>

## Exercice 6 – 997 est-il premier ?

Montrer que 997 est premier en indiquant exactement quels diviseurs sont à tester.

<details markdown="1">
<summary>Voir la réponse</summary>

\(\sqrt{997} \approx 31.58\) donc \(\lfloor \sqrt{997} \rfloor = 31\). Il suffit de tester les nombres premiers inférieurs ou égaux à 31 : 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31. Les restes de la division de 997 sont respectivement 1, 1, 2, 3, 7, 9, 11, 9, 8, 11, 5 : aucun n'est nul, donc **997 est premier**.

</details>

## Exercice 7 – Un produit de deux premiers

Décomposer \(n = 3233\) sachant que l'un de ses facteurs premiers est compris entre 50 et 60. Pourquoi ce genre de décomposition devient-il très difficile pour des nombres de plusieurs centaines de chiffres ?

<details markdown="1">
<summary>Voir la réponse</summary>

On teste les nombres premiers entre 50 et 60 : 53 et 59. \(3233 = 53 \times 61\). Les deux facteurs sont premiers (61 l'est aussi).

Pour un produit de deux grands nombres premiers, il n'existe pas d'algorithme connu de factorisation qui s'exécute en un temps raisonnable ; la recherche par division essaie de l'ordre de \(\sqrt{n}\) diviseurs, ce qui est impraticable pour un nombre de 300 chiffres.

</details>

## Exercice 8 – Un polynôme qui produit des premiers (jusqu'à un certain point)

Pour \(n \in \mathbb{N}\), on pose \(f(n) = n^2 + n + 41\). Calculer \(f(0), f(1), f(2)\) et vérifier qu'ils sont premiers. Montrer que \(f(40)\) n'est pas premier.

<details markdown="1">
<summary>Voir la réponse</summary>

\(f(0) = 41\), \(f(1) = 43\), \(f(2) = 47\) : tous trois sont premiers. On peut montrer que \(f(n)\) est premier pour tous les entiers de 0 à 39. Mais \(f(40) = 40^2 + 40 + 41 = 1681 = 41^2\) : il est divisible par 41.

**Leçon :** vérifier une propriété sur plusieurs cas ne la démontre pas.

</details>


## Je sais faire

Coche honnêtement ; ce que tu ne coches pas se reprend avant la séance suivante.

- [ ] Tester la primalité d'un entier jusqu'à \(\sqrt{n}\) ;
- [ ] Faire un crible d'Ératosthène ;
- [ ] Décomposer un entier en facteurs premiers ;
- [ ] Calculer PGCD, PPCM et nombre de diviseurs à partir de la décomposition ;
- [ ] Programmer un test de primalité.

**Ce que je dois reprendre :** ______________________

**Ma question à poser à l'enseignant :** ______________________

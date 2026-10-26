# Exercices – Réels en binaire, opérations et unités

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S02*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**, avec la méthode du cours : écris les étapes, pas seulement le résultat. Ouvre ensuite « Voir la réponse » pour te corriger. À l'épreuve, **aucune réponse sans justification** n'est complète.

## Exercice 1 – Du binaire au décimal

Convertir en décimal, en écrivant la somme des puissances de 2 : \((110,101)_2\), \((1011,0011)_2\), \((0,0101)_2\).

<details markdown="1">
<summary>Voir la réponse</summary>

- \((110,101)_2 = 1\times2^{2} + 1\times2^{1} + 0\times2^{0} + 1\times2^{-1} + 0\times2^{-2} + 1\times2^{-3} = 6,625\).
- \((1011,0011)_2 = 1\times2^{3} + 0\times2^{2} + 1\times2^{1} + 1\times2^{0} + 0\times2^{-1} + 0\times2^{-2} + 1\times2^{-3} + 1\times2^{-4} = 11,1875\).
- \((0,0101)_2 = 0\times2^{0} + 0\times2^{-1} + 1\times2^{-2} + 0\times2^{-3} + 1\times2^{-4} = 0,3125\).

</details>

## Exercice 2 – Du décimal au binaire

Écrire en binaire : \(5{,}75\) ; \(0{,}3125\) ; \(13{,}375\) ; \(0{,}2\) (donner la période).

<details markdown="1">
<summary>Voir la réponse</summary>

- \(5{,}75\) : \(5 = (101)_2\) ; \(0{,}75 \times 2 = 1{,}5\) (1) puis \(0{,}5 \times 2 = 1{,}0\) (1) : \(5{,}75 = (101,11)_2\).
- \(0{,}3125 = \frac{5}{16}\) : \(0{,}3125 = (0,0101)_2\).
- \(13{,}375\) : \(13 = (1101)_2\) et \(0{,}375 = (0,011)_2\) donc \(13{,}375 = (1101,011)_2\).
- \(0{,}2\) : 001100110011… La suite \(0011\) se répète : \(0{,}2 = (0,\overline{0011})_2\).

</details>

## Exercice 3 – Écriture finie ou non ?

Parmi 0,5 ; 0,75 ; 0,1 ; 0,375 ; 0,2 ; 0,0625, lesquels ont une écriture **finie** en binaire ? Justifier en écrivant chaque nombre sous forme de fraction irréductible.

<details markdown="1">
<summary>Voir la réponse</summary>

| Nombre | Fraction irréductible | Dénominateur puissance de 2 ? | Écriture finie |
|---|---|---|---|
| 0,5 | 1/2 | oui (2^1) | oui |
| 0,75 | 3/4 | oui (2^2) | oui |
| 0,1 | 1/10 | non | non |
| 0,375 | 3/8 | oui (2^3) | oui |
| 0,2 | 1/5 | non | non |
| 0,0625 | 1/16 | oui (2^4) | oui |

</details>

## Exercice 4 – Troncature et erreur

1. Tronquer \(0{,}1\) à 6 chiffres après la virgule en binaire.
2. Calculer l'erreur commise et la comparer à \(2^{-6}\).

<details markdown="1">
<summary>Voir la réponse</summary>

1. D'après le cours, les chiffres de \(0{,}1\) commencent par 000110 : \(0{,}1 \approx (0,000110)_2 = \dfrac{6}{64} = 0,09375\).
2. Erreur : \(0{,}1 - 0,09375 = 0,00625\). Comme \(2^{-6} = 0,015625\), l'erreur est bien strictement inférieure à \(2^{-6}\).

</details>

## Exercice 5 – Opérations en binaire

Poser et contrôler en décimal : \((1011)_2 + (0111)_2\) ; \((10110)_2 - (1101)_2\) ; \((1101)_2 \times (101)_2\).

<details markdown="1">
<summary>Voir la réponse</summary>

- \((1011)_2 + (0111)_2 = (10010)_2\). Contrôle : \(11 + 7 = 18\).
- \((10110)_2 - (1101)_2 = (1001)_2\). Contrôle : \(22 - 13 = 9\).
- \((1101)_2 \times (101)_2 = (1000001)_2\). Contrôle : \(13 \times 5 = 65\).

</details>

## Exercice 6 – Décalages

1. Écrire \(25\) en binaire, puis calculer \(25 \times 8\) par décalage.
2. Quel est le quotient de la division euclidienne de \((1101101)_2\) par \(2^3\) ? Quel est le reste ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(25 = (11001)_2\) ; trois zéros à droite : \((11001000)_2 = 200\).
2. On supprime les 3 derniers chiffres : quotient \((1101)_2 = 13\), reste \((101)_2 = 5\). Contrôle : \(109 = 8 \times 13 + 5\).

</details>

## Exercice 7 – Débordement

Un registre de 8 bits contient \(180\), on lui ajoute \(90\).

1. Quelle est la somme exacte ? Tient-elle sur 8 bits ?
2. Quelle valeur reste-t-il dans le registre ? Écrire le résultat en binaire.

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(180 + 90 = 270 > 255\) : elle ne tient pas sur 8 bits.
2. Le registre garde \(270 - 256 = 14 = (00001110)_2\).

</details>

## Exercice 8 – Complément à deux (pour aller plus loin)

1. Écrire \(-18\) sur 8 bits en complément à deux.
2. Quel entier relatif représente \((11110000)_2\) sur 8 bits ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(256 - 18 = 238 = (11101110)_2\).
2. \((11110000)_2 = 240\), premier bit à 1 : le nombre est négatif et vaut \(240 - 256 = -16\).

</details>

## Exercice 9 – Unités

1. Un disque annoncé « 2 To » contient combien de Tio (arrondir au centième) ?
2. Un fichier de \(700\) Mio représente combien de Mo (arrondir au dixième) ?
3. À \(1\) Gbit/s, combien de temps faut-il, au minimum, pour transférer \(50\) Go ?
4. Une image de \(1\,920 \times 1\,080\) pixels, codés chacun sur \(24\) bits, occupe combien d'octets sans compression ? et combien de Mio (arrondir au centième) ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(2 \times 10^{12} / 2^{40} = 1,82\) Tio.
2. \(700 \times 2^{20} = 734 003 200\) o \(= 734,0\) Mo.
3. \(t = \dfrac{50 \times 10^9 \times 8}{10^9} = 400\) s, soit 6 min 40 s.
4. \(1\,920 \times 1\,080 \times 3 = 6 220 800\) o \(\approx 5,93\) Mio.

</details>


## Exercice 10 – Chiffres significatifs

1. Combien de chiffres significatifs ont 0,00305 ; 2 500 ; 47,20 ?
2. Arrondir 2/3 et 0,0123456 à 3 chiffres significatifs.
3. Un débit est mesuré à 94,7 Mbit/s. On le convertit en Mo/s en divisant par 8 : la calculatrice affiche 11,8375. Que faut-il annoncer ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. 0,00305 : 3 (3, 0, 5) ; 2 500 : 4 si le zéro final est mesuré, sinon 2 ou 3, on précise donc par la notation scientifique (\(2{,}5 \times 10^3\) pour 2 chiffres) ; 47,20 : 4.
2. \(2/3 \approx 0{,}667\) ; \(0{,}0123456 \approx 0{,}0123\).
3. La mesure a 3 chiffres significatifs : on annonce 11,8 Mo/s. Écrire 11,8375 laisserait croire à une précision que la mesure n'a pas.

</details>

## Je sais faire

Coche honnêtement ; ce que tu ne coches pas se reprend avant la séance suivante.

- [ ] Convertir un nombre à virgule entre les bases 2 et 10 ;
- [ ] Dire si un décimal a une écriture finie en base 2 ;
- [ ] Arrondir et majorer une erreur ;
- [ ] Donner un résultat avec un nombre de chiffres significatifs imposé ;
- [ ] Additionner et multiplier en binaire ;
- [ ] Convertir des unités (bit, octet, ko, Kio…) et calculer un temps de transfert.

**Ce que je dois reprendre :** ______________________

**Ma question à poser à l'enseignant :** ______________________

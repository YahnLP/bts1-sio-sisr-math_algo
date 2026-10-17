# Exercices – Conversions et lecture de nombres

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S01*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**, avec la méthode du cours : écris les étapes, pas seulement le résultat. Ouvre ensuite « Voir la réponse » pour te corriger. À l'épreuve, **aucune réponse sans justification** n'est complète.

## Exercice 1 – De la base \(b\) vers la base 10

Convertir en base 10, en écrivant la somme pondérée : \((101101)_2\), \((3E8)_{16}\), \((FF)_{16}\), \((1000)_2\).

<details markdown="1">
<summary>Voir la réponse</summary>

- \((101101)_2 = 1\times32 + 0\times16 + 1\times8 + 1\times4 + 0\times2 + 1\times1 = 45\).
- \((3E8)_{16} = 3\times256 + 14\times16 + 8\times1 = 1000\).
- \((FF)_{16} = 15\times16 + 15 = 255\).
- \((1000)_2 = 1\times 2^3 = 8\).

</details>

## Exercice 2 – De la base 10 vers la base 2

Écrire en binaire, avec la méthode des divisions successives : 37, 100, 255, 1 000. **Vérifier** chaque résultat en le reconvertissant en base 10.

<details markdown="1">
<summary>Voir la réponse</summary>

| Nombre | Binaire | Vérification |
|---|---|---|
| 37 | 100101 | 1\times32 + 0\times16 + 0\times8 + 1\times4 + 0\times2 + 1\times1 = 37 |
| 100 | 1100100 | 1\times64 + 1\times32 + 0\times16 + 0\times8 + 1\times4 + 0\times2 + 0\times1 = 100 |
| 255 | 11111111 | 1\times128 + 1\times64 + 1\times32 + 1\times16 + 1\times8 + 1\times4 + 1\times2 + 1\times1 = 255 |
| 1000 | 1111101000 | 1\times512 + 1\times256 + 1\times128 + 1\times64 + 1\times32 + 0\times16 + 1\times8 + 0\times4 + 0\times2 + 0\times1 = 1000 |

</details>

## Exercice 3 – De la base 10 vers la base 16

Écrire en hexadécimal : 255, 1 000, 4 096, 65 535.

<details markdown="1">
<summary>Voir la réponse</summary>

| Nombre | Hexadécimal | Vérification |
|---|---|---|
| 255 | FF | 255 = 15×16 + 15×1 |
| 1000 | 3E8 | 1000 = 3×256 + 14×16 + 8×1 |
| 4096 | 1000 | 4096 = 1×4096 + 0×256 + 0×16 + 0×1 |
| 65535 | FFFF | 65535 = 15×4096 + 15×256 + 15×16 + 15×1 |

</details>

## Exercice 4 – Binaire et hexadécimal

1. Écrire en hexadécimal : \((10110111)_2\) et \((1111101000)_2\).
2. Écrire en binaire sur 12 bits : \((5A3)_{16}\).

<details markdown="1">
<summary>Voir la réponse</summary>

1. \((1011\ 0111)_2 = (B7)_{16}\). Pour le second, on complète à gauche : \((0011\ 1110\ 1000)_2 = (3E8)_{16}\).
2. \(5 = 0101\), \(A = 1010\), \(3 = 0011\) donc \((5A3)_{16} = (010110100011)_2\).

</details>

## Exercice 5 – Combien de bits ?

1. Combien de valeurs différentes peut-on représenter avec 10 bits ? avec 12 bits ?
2. Quel est le plus grand entier écrit avec 10 bits ?
3. Combien faut-il de bits au minimum pour numéroter 1 000 objets, de 0 à 999 ?
4. Combien de bits faut-il pour écrire l'entier 300 en binaire ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(2^{10} = 1024\) et \(2^{12} = 4096\).
2. \(2^{10} - 1 = 1023\).
3. Il faut \(2^n \ge 1\,000\). Comme \(2^9 = 512 < 1\,000\) et \(2^{10} = 1024 \ge 1\,000\), il faut **10 bits**.
4. \(2^8 = 256 \le 300 < 512 = 2^9\), donc **9 bits** : \(300 = (100101100)_2\).

</details>

## Exercice 6 – Adresses IPv4

1. Écrire en binaire l'adresse `10.0.0.255`.
2. Écrire en décimal l'adresse `10101100.00010000.00000101.00010100`.
3. Pourquoi `172.16.256.1` n'est-elle pas une adresse IPv4 valide ?
4. Combien d'adresses IPv4 existe-t-il, de `0.0.0.0` à `255.255.255.255` ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. `00001010.00000000.00000000.11111111`
2. `172.16.5.20`
3. Le troisième octet vaut 256, supérieur à 255 : il ne s'écrit pas sur 8 bits.
4. Quatre octets indépendants de 256 valeurs chacun : \(256^4 = 2^{32} = 4294967296\) adresses (à lire : 4 294 967 296).

</details>

## Exercice 7 – Adresses MAC et couleurs

1. Écrire en binaire l'octet `3C` de l'adresse MAC `00:1A:2B:3C:4D:5E`.
2. Combien de bits compte une adresse MAC ? Combien d'adresses MAC différentes existe-t-il en théorie ?
3. Donner en décimal les trois composantes de la couleur `#1E90FF`.

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(3 = 0011\) et \(C = 1100\), donc `00111100` (soit \(60\)).
2. 6 octets, donc 48 bits ; \(2^{48} = 281474976710656\) adresses possibles.
3. `1E` = \(1\times16+14 = 30\) ; `90` = \(9\times16 = 144\) ; `FF` = 255. La couleur est (30, 144, 255).

</details>

## Exercice 8 – Trouver l'erreur

Un étudiant écrit : « \(37 = (101001)_2\) ». Il a lu les restes dans le mauvais sens.

1. Que vaut en réalité \((101001)_2\) ?
2. Quelle est la bonne écriture binaire de 37 ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. \((101001)_2 = 1\times32 + 0\times16 + 1\times8 + 0\times4 + 0\times2 + 1\times1 = 41\), ce n'est pas 37.
2. En lisant les restes **de bas en haut** : \(37 = (100101)_2\) ; contrôle : \(1\times32 + 0\times16 + 0\times8 + 1\times4 + 0\times2 + 1\times1 = 37\).

</details>


## Je sais faire

Coche honnêtement ; ce que tu ne coches pas se reprend avant la séance suivante.

- [ ] Écrire un entier en base \(b\) sous forme de somme de puissances ;
- [ ] Convertir 10 → 2 → 10 et 2 → 16 → 2 sans calculatrice ;
- [ ] Donner le nombre de valeurs et le maximum pour \(n\) bits ;
- [ ] Lire une adresse MAC et une adresse IPv4 en binaire ;
- [ ] Vérifier une conversion avec `bin`, `hex` et `int`.

**Ce que je dois reprendre :** ______________________

**Ma question à poser à l'enseignant :** ______________________

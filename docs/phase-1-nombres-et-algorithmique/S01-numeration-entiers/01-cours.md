# Cours – Numération : entiers en base 2, 10 et 16

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S01 – à lire avant les [exercices](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** Aucun (puissances, divisions). Pour le TP : [S00 – Introduction à Python](../S00-introduction-python/README.md), à faire hors classe.
> - **Outils :** Papier, calculatrice, éditeur Python intégré au site

## À la fin de ce cours tu sauras

- [ ] **Écrire** un entier naturel sous la forme d'une somme de puissances d'une base \(b\) (\(b = 2, 10, 16\)) ;
- [ ] **Convertir** un entier de la base 10 vers la base 2 ou 16 (divisions successives) et inversement (somme pondérée) ;
- [ ] **Passer** directement de la base 2 à la base 16 et inversement (groupes de 4 bits) ;
- [ ] **Déterminer** combien de valeurs on représente avec \(n\) bits et quel est le plus grand entier ;
- [ ] **Lire** une adresse MAC, une adresse IPv4 et un code couleur, et **vérifier** ses conversions avec Python.

## I. Écrire un nombre : la notation positionnelle

Dans l'écriture **1 407** en base 10, la valeur d'un chiffre dépend de sa **position** :

\[
1\,407 = 1 \times 10^3 + 4 \times 10^2 + 0 \times 10^1 + 7 \times 10^0 .
\]

Cette idée marche avec n'importe quelle **base** \(b \ge 2\). Dans la base \(b\), on utilise les \(b\) chiffres \(0, 1, \dots, b-1\) et un entier s'écrit

\[
N = a_{k}\, b^{k} + a_{k-1}\, b^{k-1} + \dots + a_1\, b + a_0 , \qquad 0 \le a_i \le b-1 .
\]

On note alors \(N = (a_k a_{k-1} \dots a_1 a_0)_b\). Les trois bases utiles en informatique sont :

| Base | Nom | Chiffres | Usage |
|---|---|---|---|
| 10 | décimale | 0 à 9 | Notre écriture usuelle |
| 2 | binaire | 0 et 1 | Représentation interne des données (un **bit** vaut 0 ou 1) |
| 16 | hexadécimale | 0 à 9 puis A, B, C, D, E, F | Écriture compacte du binaire |

En hexadécimal, les lettres représentent les chiffres de dix à quinze :

| Lettre | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| Valeur | 10 | 11 | 12 | 13 | 14 | 15 |

> [!NOTE]
> **Notation.** On indique la base en indice : \((1011)_2\), \((CD)_{16}\). Sans indice, c'est la base 10. En Python, `0b1011` est un nombre binaire et `0xCD` un nombre hexadécimal.

## II. De la base \(b\) vers la base 10

Il suffit de calculer la somme pondérée de la définition.

**Exemple.** \((1101)_2\) :

\[
(1101)_2 = 1\times8 + 1\times4 + 0\times2 + 1\times1 = 13 .
\]

**Exemple.** \((3F)_{16}\) : le chiffre F vaut 15, donc

\[
(3F)_{16} = 3 \times 16 + 15 \times 1 = 63 .
\]

## III. De la base 10 vers la base \(b\) : les divisions successives

On divise le nombre par \(b\), puis on divise les quotients successifs, jusqu'à obtenir un quotient nul. Les **restes**, lus **du dernier au premier**, donnent l'écriture dans la base \(b\).

**Exemple.** Écrire 205 en binaire.

| Division | Quotient | Reste |
|---|---|---|
| 205 = 2 × 102 + 1 | 102 | **1** |
| 102 = 2 × 51 + 0 | 51 | **0** |
| 51 = 2 × 25 + 1 | 25 | **1** |
| 25 = 2 × 12 + 1 | 12 | **1** |
| 12 = 2 × 6 + 0 | 6 | **0** |
| 6 = 2 × 3 + 0 | 3 | **0** |
| 3 = 2 × 1 + 1 | 1 | **1** |
| 1 = 2 × 0 + 1 | 0 | **1** |

On lit les restes de bas en haut : \(205 = (11001101)_2\).

**Exemple.** Écrire 205 en hexadécimal.

| Division | Quotient | Reste |
|---|---|---|
| 205 = 16 × 12 + 13 | 12 | **D** |
| 12 = 16 × 0 + 12 | 0 | **C** |

Le reste 13 s'écrit D et le reste 12 s'écrit C : \(205 = (CD)_{16}\).

> [!TIP]
> **Contrôle systématique.** On revient à la base 10 : \((CD)_{16} = 12 \times 16 + 13 = 205\). Une conversion non vérifiée est une conversion à moitié faite.

## IV. Binaire et hexadécimal : le passage direct

Comme \(16 = 2^4\), **un chiffre hexadécimal correspond exactement à quatre bits**.

| Hexa | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | A | B | C | D | E | F |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Binaire | 0000 | 0001 | 0010 | 0011 | 0100 | 0101 | 0110 | 0111 | 1000 | 1001 | 1010 | 1011 | 1100 | 1101 | 1110 | 1111 |

**Binaire → hexadécimal** : on découpe en groupes de 4 bits **à partir de la droite**, en complétant à gauche par des zéros.

\[
(11001101)_2 = (1100\ 1101)_2 = (CD)_{16} .
\]

**Hexadécimal → binaire** : chaque chiffre est remplacé par ses quatre bits. Ainsi \((2F)_{16} = (00101111)_2\) (on a écrit 2 = 0010 et F = 1111).

## V. Bits, octets et nombre de valeurs

Un **bit** est un chiffre binaire. Un **octet** est un groupe de 8 bits.

Avec \(n\) bits, on peut écrire \(2^n\) valeurs différentes : les nombres de 0 à \(2^n - 1\). En effet, chaque bit a deux états, indépendamment des autres. Le plus grand nombre s'écrit avec \(n\) chiffres 1 :

\[
(\underbrace{11\dots1}_{n})_2 = 2^{n-1} + \dots + 2 + 1 = 2^n - 1 .
\]

| Nombre de bits | Valeurs possibles | Plus grand entier |
|---|---|---|
| 4 | 16 | 15 |
| 8 | 256 | 255 |
| 16 | 65536 | 65535 |
| 32 | 4294967296 | 4294967295 |

Puissances de 2 à connaître :

| \(k\) | \(2^k\) |
|---|---|
| 0 | 1 |
| 1 | 2 |
| 2 | 4 |
| 3 | 8 |
| 4 | 16 |
| 5 | 32 |
| 6 | 64 |
| 7 | 128 |
| 8 | 256 |
| 9 | 512 |
| 10 | 1024 |
| 11 | 2048 |
| 12 | 4096 |
| 13 | 8192 |
| 14 | 16384 |
| 15 | 32768 |
| 16 | 65536 |

## VI. Où rencontre-t-on ces écritures ?

### Adresse IPv4

Une adresse IPv4 compte **32 bits**, présentés en **4 octets** séparés par des points. Chaque octet est écrit en décimal, donc entre 0 et 255.

\[
192.168.1.10 \;=\; 11000000.10101000.00000001.00001010 .
\]

Un « octet » de valeur 256 n'existe pas dans une adresse IPv4 : \(256 = 2^8\) dépasse \(2^8 - 1\).

### Adresse MAC

Une adresse MAC compte **48 bits**, soit 6 octets, écrits en **12 chiffres hexadécimaux** (deux par octet), par exemple `00:1A:2B:3C:4D:5E`. Le premier octet `00` vaut \((00000000)_2\) et le dernier `5E` vaut \((01011110)_2 = 94\).

### Couleur web

Le code `#FF8000` donne l'intensité de rouge (FF = 255), de vert (80 = 128) et de bleu (00 = 0), chacune sur un octet.

## VII. Vérifier avec Python

```python
>>> bin(205)
'0b11001101'
>>> hex(205)
'0xcd'
>>> int("11001101", 2)
205
>>> int("CD", 16)
205
```

Python sert à **contrôler** un résultat posé à la main, pas à le remplacer : à l'épreuve, la méthode et les étapes sont évaluées.

## À retenir

- En base \(b\), \(N = \sum a_i b^i\) avec \(0 \le a_i \le b-1\).
- **10 → \(b\)** : divisions successives, restes lus de bas en haut. **\(b\) → 10** : somme pondérée.
- **Un chiffre hexadécimal = 4 bits** : le passage 2 ↔ 16 se fait par groupes de 4.
- \(n\) bits : \(2^n\) valeurs, de 0 à \(2^n - 1\) ; un octet : 0 à 255.
- IPv4 : 4 octets (32 bits) en décimal ; MAC : 6 octets (48 bits) en hexadécimal.

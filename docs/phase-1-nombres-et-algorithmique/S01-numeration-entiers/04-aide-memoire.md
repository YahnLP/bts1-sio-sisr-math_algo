# Aide-mémoire – Numération : bases 2, 10 et 16

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S01*

> Un mot ou un sigle inconnu ? Passe la souris dessus, ou ouvre le [glossaire](../../ressources/glossaire.md).

## Définition

\[
N = (a_k \dots a_1 a_0)_b = \sum_{i=0}^{k} a_i\, b^i , \qquad 0 \le a_i \le b-1 .
\]

## Méthodes

| Je veux… | Méthode |
|---|---|
| \(b \to 10\) | Somme pondérée des chiffres par les puissances de \(b\) |
| \(10 \to b\) | Divisions successives par \(b\) ; **restes lus de bas en haut** |
| \(2 \to 16\) | Groupes de **4 bits** à partir de la droite |
| \(16 \to 2\) | Chaque chiffre hexa donne **4 bits** |

## Hexadécimal

| A | B | C | D | E | F |
|---|---|---|---|---|---|
| 10 | 11 | 12 | 13 | 14 | 15 |

## Nombre de valeurs

- \(n\) bits : \(2^n\) valeurs, de 0 à \(2^n - 1\).
- 1 octet = 8 bits : 0 à 255.
- Nombre de bits pour écrire \(N \ge 1\) : le plus petit \(n\) tel que \(N < 2^n\).

## Puissances de 2

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

## Adresses

| Objet | Taille | Écriture |
|---|---|---|
| IPv4 | 32 bits (4 octets) | 4 nombres décimaux de 0 à 255 séparés par des points |
| MAC | 48 bits (6 octets) | 12 chiffres hexadécimaux |
| Couleur web | 24 bits (3 octets) | `#RRGGBB` |

## Python

```python
bin(205)           # '0b11001101'
hex(205)           # '0xcd'
int("11001101", 2) # 205
int("CD", 16)      # 205
```

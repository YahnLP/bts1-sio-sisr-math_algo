# Cours – Algorithmique : données, instructions et conditions

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S03 – à lire avant les [exercices](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** S01, S02 (bases, opérations en binaire).
> - **Outils :** Papier, calculatrice, éditeur Python intégré au site

## À la fin de ce cours tu sauras

- [ ] **Écrire** l'en-tête d'un algorithme (nom, rôle, entrées, sortie, variables typées) ;
- [ ] **Choisir** le type d'une donnée : entier, réel, booléen, chaîne ;
- [ ] **Écrire** des expressions avec les opérateurs numériques, de comparaison, booléens et **bit à bit** (masque, mise à 1, mise à 0, changement d'état) ;
- [ ] **Écrire** une structure conditionnelle (si… alors… sinon) en pseudo-code indenté et en Python ;
- [ ] **Dérouler** un algorithme à la main sur un jeu d'essai (trace) et **tester** un programme.

## I. Qu'est-ce qu'un algorithme ?

Un **algorithme** est une suite finie et ordonnée d'instructions qui permet de résoudre un problème. Il se décrit en **pseudo-code** (indépendant du langage) puis se **traduit** dans un langage de programmation, ici **Python**.

Tout algorithme commence par un **en-tête** : son nom, son rôle, ses données d'entrée, son résultat, ses variables avec leur type. Voici le format utilisé sur tout le site.

```text
ALGORITHME est_pair
  RÔLE      : dire si un entier est pair
  ENTRÉE    : n (entier)
  SORTIE    : un booléen (vrai si n est pair)
  VARIABLES : reste (entier)
DÉBUT
  reste ← n mod 2          // reste de la division euclidienne par 2
  RETOURNER reste = 0
FIN
```

Le même algorithme en Python :

```python
def est_pair(n):
    """Rôle : dire si l'entier n est pair."""
    reste = n % 2
    return reste == 0
```

> [!NOTE]
> **Règles d'écriture.** Début et fin sont explicites ; chaque bloc est **indenté** ; l'affectation se note `←` en pseudo-code (et `=` en Python) ; les commentaires expliquent le **pourquoi**, pas le quoi.

## II. Les données

Une **variable** est un nom associé à une valeur gardée en mémoire. **L'affectation** `x ← expression` calcule l'expression puis range le résultat dans `x`. Chaque donnée a un **type**.

| Type | Exemples | Python | Remarque |
|---|---|---|---|
| Entier naturel / relatif | `0`, `42`, `-7` | `int` | Pas de limite de taille en Python |
| Réel | `3.14`, `-0.5` | `float` | Valeur approchée (S02) |
| Booléen | vrai, faux | `bool` (`True`, `False`) | Résultat d'une comparaison |
| Chaîne de caractères | `"192.168.1.10"` | `str` | Texte ; `"42"` n'est pas le nombre 42 |

Deux instructions d'échange : **lire** une valeur (`input` en Python, toujours une chaîne) et **afficher** (`print`). Pour passer d'un type à l'autre on **convertit** (on parle de **transtypage**) : `int("42")` donne l'entier 42, `float("3.5")` le réel 3,5, `str(42)` la chaîne `"42"`. Convertir un réel en entier supprime la partie décimale : `int(3.9)` donne 3. Une conversion impossible (`int("abc")`) provoque une erreur.

> [!WARNING]
> **Piège classique.** `"1" + "2"` donne `"12"` (concaténation de chaînes) alors que `1 + 2` donne `3`. Une saisie `input()` est une chaîne : on la convertit avant de calculer.

## III. Les opérateurs

### Opérateurs numériques et de comparaison

| Opération | Pseudo-code | Python | Exemple | Résultat |
|---|---|---|---|---|
| Quotient entier | `div` | `//` | `17 // 5` | 3 |
| Reste | `mod` | `%` | `17 % 5` | 2 |
| Division réelle | `/` | `/` | `7 / 2` | 3.5 |
| Puissance | `^` | `**` | `2 ** 10` | 1024 |
| Égal / différent | `=` / `≠` | `==` / `!=` | `3 == 3.0` | True |
| Comparaisons | `<` `≤` `>` `≥` | `<` `<=` `>` `>=` | `4 >= 5` | False |

Pour des entiers positifs, `a // b` et `a % b` sont le **quotient** et le **reste** de la division euclidienne de \(a\) par \(b\) : \(a = b \times q + r\) (S05). Pour un diviseur \(b > 0\), Python donne toujours un reste compris entre 0 et \(b-1\), même si \(a\) est négatif : `-17 // 5` vaut -4 et `-17 % 5` vaut 3, car \(-17 = 5 \times (-4) + 3\). Dans d'autres langages (C, Java), le reste d'un nombre négatif peut être négatif : attention au langage.

### Opérateurs booléens

| Opérateur | Pseudo-code | Python | Vrai quand… |
|---|---|---|---|
| Non | `non` | `not` | l'opérande est faux |
| Et | `et` | `and` | les deux opérandes sont vrais |
| Ou | `ou` | `or` | au moins un opérande est vrai |
| Ou exclusif | `oux` | `^` (sur des booléens) | exactement un opérande est vrai |

Les tables de vérité sont étudiées en S08. Retenons une règle de **priorité** : `non` avant `et` avant `ou` (on parenthèse dans le doute).

> [!NOTE]
> **Évaluation partielle.** Dans `a et b`, si `a` est faux, `b` n'est **pas évalué** (le résultat est déjà faux). Cela évite une erreur dans `x != 0 and 10 / x > 1`.

### Opérateurs bit à bit

Ils agissent sur chaque bit de l'écriture binaire des entiers (S01).

| Opération | Python | Effet |
|---|---|---|
| Et bit à bit | `a & b` | bit à 1 si les **deux** bits valent 1 |
| Ou bit à bit | `a | b` | bit à 1 si **au moins un** bit vaut 1 |
| Ou exclusif | `a ^ b` | bit à 1 si les bits **diffèrent** |
| Décalage à gauche | `a << k` | multiplie par \(2^k\) |
| Décalage à droite | `a >> k` | quotient par \(2^k\) |

| Expression | Écriture sur 8 bits | Valeur |
|---|---|---|
| `12` | `00001100` | 12 |
| `10` | `00001010` | 10 |
| `12 & 10` | `00001000` | 8 |
| `12 | 10` | `00001110` | 14 |
| `12 ^ 10` | `00000110` | 6 |
| `1 << 4` | `00010000` | 16 |
| `200 >> 3` | `00011001` | 25 |

#### Les masques

Un **masque** est un entier dont les bits à 1 désignent les bits qu'on veut manipuler. Pour agir sur le bit de poids \(2^k\), le masque vaut \(m = 2^k\) (`1 << k`).

| Je veux… | Expression | Effet sur les bits du masque |
|---|---|---|
| **Tester** un bit | `(x & m) != 0` | vrai si le bit est à 1 |
| **Mettre à 1** | `x | m` | les bits du masque passent à 1 |
| **Mettre à 0** | `x & ~m` | les bits du masque passent à 0 |
| **Changer d'état** | `x ^ m` | les bits du masque sont inversés |

**Exemple : droits d'accès.** On code lecture = 4 (`100`), écriture = 2 (`010`), exécution = 1 (`001`). Des droits « lecture + écriture » valent \(4 + 2 = 6\) (`110`).

| Opération | Expression | Résultat |
|---|---|---|
| Ajouter l'exécution | `6 | 1` | 7 (`111`) |
| Retirer l'écriture | `6 & ~2` | 4 (`100`) |
| Basculer la lecture | `6 ^ 4` | 2 (`010`) |
| L'écriture est-elle accordée ? | `(6 & 2) != 0` | True |

**Application réseau.** L'adresse de réseau s'obtient en faisant un **ET bit à bit** entre l'adresse IP et le masque, octet par octet : `192.168.1.10` ET `255.255.255.0` donne `192.168.1.0` (S10).

## IV. Les structures conditionnelles

Une **conditionnelle** exécute un bloc seulement si une condition (une expression booléenne) est vraie.

```text
SI condition ALORS
  bloc 1
SINON
  bloc 2
FIN SI
```

```python
if condition:
    bloc_1
else:
    bloc_2
```

Plusieurs cas s'enchaînent avec `SINON SI` (`elif`). Les conditions sont examinées **dans l'ordre** : la première qui est vraie est exécutée, les autres sont ignorées. L'ordre des tests est donc essentiel.

**Exemple : année bissextile.** Une année est bissextile si elle est divisible par 4 sans l'être par 100, ou si elle est divisible par 400.

```text
ALGORITHME est_bissextile
  RÔLE      : dire si une année du calendrier grégorien est bissextile
  ENTRÉE    : annee (entier)
  SORTIE    : un booléen
DÉBUT
  RETOURNER (annee mod 4 = 0 et annee mod 100 ≠ 0) ou (annee mod 400 = 0)
FIN
```

| Année | Divisible par 4 | par 100 | par 400 | Bissextile |
|---|---|---|---|---|
| 1900 | oui | oui | non | **non** |
| 2000 | oui | oui | oui | **oui** |
| 2023 | non | non | non | **non** |
| 2024 | oui | non | non | **oui** |
| 2100 | oui | oui | non | **non** |

## V. Dérouler un algorithme : la trace

Pour comprendre ou tester un algorithme, on le **déroule à la main** en notant l'état des variables après chaque instruction : c'est la **trace**.

```text
ALGORITHME mystere
  ENTRÉE : a, b (entiers)
DÉBUT
  c ← a
  a ← b
  b ← c
FIN
```

| Instruction | `a` | `b` | `c` |
|---|---|---|---|
| (départ avec a = 3, b = 8) | 3 | 8 | — |
| `c ← a` | 3 | 8 | 3 |
| `a ← b` | 8 | 8 | 3 |
| `b ← c` | 8 | 3 | 3 |

L'algorithme **échange** les valeurs de `a` et de `b`.

### Tester un algorithme

Un **jeu d'essai** est un ensemble d'entrées avec les résultats attendus, calculés **indépendamment** de l'algorithme. On choisit des cas **typiques** et des **cas limites** : par exemple, pour `est_bissextile`, 2024 (typique), 1900 et 2000 (cas limites des siècles).

## À retenir

- Un algorithme a un **en-tête** (rôle, entrées, sortie, variables typées) et une écriture **indentée**.
- Types : entier, réel, booléen, chaîne ; `//` quotient, `%` reste.
- Booléens : `not`, `and`, `or` ; **bit à bit** : `&`, `|`, `^`, `<<`, `>>`.
- Masques : tester `(x & m) != 0`, mettre à 1 `x | m`, mettre à 0 `x & ~m`, basculer `x ^ m`.
- `SI … SINON SI … SINON` : le **premier** test vrai gagne, l'ordre compte.
- On valide un algorithme par une **trace** et un **jeu d'essai** avec cas limites.

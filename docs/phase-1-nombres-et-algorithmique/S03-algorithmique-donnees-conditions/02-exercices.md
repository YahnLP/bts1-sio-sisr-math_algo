# Exercices – Lire et écrire de petits algorithmes

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S03*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**, avec la méthode du cours : écris les étapes, pas seulement le résultat. Ouvre ensuite « Voir la réponse » pour te corriger. À l'épreuve, **aucune réponse sans justification** n'est complète.

## Exercice 1 – Types

Donner le type Python (`int`, `float`, `bool`, `str`) de chaque valeur : `42`, `4.0`, `"42"`, `True`, `"True"`, `10 > 3`, `7 // 2`, `7 / 2`.

<details markdown="1">
<summary>Voir la réponse</summary>

| Valeur | Type | Explication |
|---|---|---|
| `42` | `int` | entier |
| `4.0` | `float` | réel (présence d'un point) |
| `"42"` | `str` | chaîne (guillemets) |
| `True` | `bool` | booléen |
| `"True"` | `str` | chaîne : c'est du texte |
| `10 > 3` | `bool` | booléen : résultat d'une comparaison |
| `7 // 2` | `int` | entier : quotient |
| `7 / 2` | `float` | réel : la division `/` donne toujours un réel |

</details>

## Exercice 2 – Évaluer des expressions

Donner la valeur de chaque expression Python.

1. `29 // 6`, `29 % 6`, `2 ** 5`, `-13 // 4`, `-13 % 4`.
2. `(10 % 3 == 1) and (4 > 5)`, `(10 % 3 == 1) or (4 > 5)`, `not (3 == 3.0)`.
3. `12 & 10`, `12 | 10`, `12 ^ 10`, `1 << 5`, `100 >> 2`.

<details markdown="1">
<summary>Voir la réponse</summary>

| Expression | Valeur |
|---|---|
| `29 // 6` | `4` |
| `29 % 6` | `5` |
| `2 ** 5` | `32` |
| `-13 // 4` | `-4` |
| `-13 % 4` | `3` |
| `(10 % 3 == 1) and (4 > 5)` | `False` |
| `(10 % 3 == 1) or (4 > 5)` | `True` |
| `not (3 == 3.0)` | `False` |
| `12 & 10` | `8` |
| `12 | 10` | `14` |
| `12 ^ 10` | `6` |
| `1 << 5` | `32` |
| `100 >> 2` | `25` |

Contrôle des divisions : \(29 = 6 \times 4 + 5\) et \(-13 = 4 \times (-4) + 3\).

</details>

## Exercice 3 – Masques et droits

Les droits sont codés lecture = 4, écriture = 2, exécution = 1. Un fichier a les droits \(5\).

1. Quels droits possède-t-il (écrire en binaire sur 3 bits) ?
2. Quelle expression ajoute l'écriture ? Quelle est la nouvelle valeur ?
3. Quelle expression retire ensuite la lecture ? Quelle est la valeur obtenue ?
4. Quelle expression teste si l'exécution est accordée aux droits \(6\) ? Que vaut-elle ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(5 = (101)_2\) : lecture (4) et exécution (1), pas d'écriture.
2. `5 | 2` vaut 7 (`111`).
3. `7 & ~4` vaut 3 (`011`) : écriture et exécution.
4. `(6 & 1) != 0` vaut False : \(6 = (110)_2\), le bit d'exécution est à 0.

</details>

## Exercice 4 – Trace

On considère l'algorithme suivant.

```text
ALGORITHME classer
  ENTRÉE  : n (entier)
  SORTIE  : un texte
DÉBUT
  SI n mod 15 = 0 ALORS
    RETOURNER "tous"
  SINON SI n mod 3 = 0 ALORS
    RETOURNER "trois"
  SINON SI n mod 5 = 0 ALORS
    RETOURNER "cinq"
  SINON
    RETOURNER "aucun"
  FIN SI
FIN
```

1. Donner le résultat pour \(n = 30\), \(9\), \(10\), \(7\).
2. Que se passerait-il pour \(n = 30\) si on inversait l'ordre des deux premiers tests ?

<details markdown="1">
<summary>Voir la réponse</summary>

| n | Résultat |
|---|---|
| 30 | tous |
| 9 | trois |
| 10 | cinq |
| 7 | aucun |

2. Si le test `n mod 3 = 0` venait en premier, \(30\) (divisible par 3) donnerait `"trois"` : le cas `"tous"` ne serait **jamais** atteint. Le test le plus **particulier** doit précéder les plus généraux.

</details>

## Exercice 5 – Pseudo-code et Python

1. Traduire en pseudo-code (avec en-tête) la fonction Python :

```python
def est_majeur(age):
    return age >= 18
```

2. Traduire en Python :

```text
ALGORITHME niveau
  ENTRÉE : note (réel)
  SORTIE : un texte
DÉBUT
  SI note < 8 ALORS RETOURNER "insuffisant"
  SINON SI note < 12 ALORS RETOURNER "passable"
  SINON RETOURNER "bon"
  FIN SI
FIN
```

<details markdown="1">
<summary>Voir la réponse</summary>

1.

```text
ALGORITHME est_majeur
  RÔLE   : dire si une personne est majeure
  ENTRÉE : age (entier)
  SORTIE : un booléen
DÉBUT
  RETOURNER age ≥ 18
FIN
```

2.

```python
def niveau(note):
    if note < 8:
        return "insuffisant"
    elif note < 12:
        return "passable"
    else:
        return "bon"
```

Dans le second algorithme, le deuxième test n'a pas besoin de vérifier `note >= 8` : on n'y arrive que si le premier test est faux.

</details>

## Exercice 6 – Adresses privées

Une adresse IPv4 est **privée** si elle appartient à l'une des plages suivantes : `10.0.0.0` à `10.255.255.255` ; `172.16.0.0` à `172.31.255.255` ; `192.168.0.0` à `192.168.255.255`.

1. Écrire la condition portant sur le premier octet \(a\) et le deuxième octet \(b\).
2. Dire si chaque adresse est privée : `10.4.5.6`, `172.32.0.1`, `172.20.1.1`, `192.168.0.1`, `192.169.0.1`, `8.8.8.8`.

<details markdown="1">
<summary>Voir la réponse</summary>

1. `a == 10 or (a == 172 and 16 <= b <= 31) or (a == 192 and b == 168)`.
2.

| Adresse | Privée ? |
|---|---|
| `10.4.5.6` | oui |
| `172.32.0.1` | non |
| `172.20.1.1` | oui |
| `192.168.0.1` | oui |
| `192.169.0.1` | non |
| `8.8.8.8` | non |

</details>

## Exercice 7 – Adresse de réseau

Calculer l'adresse de réseau (ET bit à bit octet par octet) de `192.168.5.77` avec le masque `255.255.255.192`, puis de `172.16.37.200` avec le masque `255.255.240.0`. Justifier les octets qui changent en binaire.

<details markdown="1">
<summary>Voir la réponse</summary>

- Premier cas : seul le dernier octet change : \(77 = (01001101)_2\), \(192 = (11000000)_2\), \(77 \,\&\, 192 = (01000000)_2 = 64\). Adresse de réseau : `192.168.5.64`.
- Second cas : \(37 = (00100101)_2\), \(240 = (11110000)_2\), \(37 \,\&\, 240 = (00100000)_2 = 32\) ; \(200 \,\&\, 0 = 0\). Adresse de réseau : `172.16.32.0`.

</details>

## Exercice 8 – Trouver les erreurs

Chaque ligne contient une erreur. Laquelle ? Corriger.

```python
if x = 5:
    print("cinq")
```

```python
age = input("Âge ? ")
if age >= 18:
    print("majeur")
```

```python
if note >= 10:
    mention = "reçu"
elif note >= 16:
    mention = "très bien"
```

<details markdown="1">
<summary>Voir la réponse</summary>

1. `=` est l'**affectation** ; la comparaison s'écrit `==` : `if x == 5:`.
2. `input` renvoie une **chaîne** ; comparer une chaîne à un entier provoque une erreur. Il faut convertir : `age = int(input("Âge ? "))`.
3. Le second test n'est jamais atteint : si `note >= 16`, alors `note >= 10` est déjà vrai. Il faut tester le cas le plus **exigeant** d'abord : `if note >= 16: ... elif note >= 10: ...`.

</details>


## Je sais faire

Coche honnêtement ; ce que tu ne coches pas se reprend avant la séance suivante.

- [ ] Écrire l'en-tête d'un algorithme ;
- [ ] Choisir un type de donnée adapté ;
- [ ] Évaluer une expression avec `//`, `%`, `and`, `or`, `not`, `&`, `|`, `^`, `<<`, `>>` ;
- [ ] Écrire une conditionnelle imbriquée en pseudo-code et en Python ;
- [ ] Dérouler un algorithme sur un jeu d'essai.

**Ce que je dois reprendre :** ______________________

**Ma question à poser à l'enseignant :** ______________________

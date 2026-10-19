# Exercices – Lire et prévoir un programme

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S00*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**, sans lancer le programme. Ouvre ensuite « Voir la réponse » pour te corriger, puis, si tu veux, vérifie dans l'éditeur du TP.

## Exercice 1 – Affectation

Qu'affiche ce programme ?

```python
a = 17
b = 5
print(a // b, a % b)
a = a + 1
print(a)
```

<details markdown="1">
<summary>Voir la réponse</summary>

`17 // 5` vaut 3 et `17 % 5` vaut 2 : la première ligne affichée est `3 2`. Puis `a` devient 18 : la seconde ligne est `18`.

</details>

## Exercice 2 – Nombres ou texte ?

Donner la valeur de chaque expression : (a) `5 + 3` ; (b) `"5" + "3"` ; (c) `int("5") + 3` ; (d) `str(5) + "3"` ; (e) `len("réseau")` ; (f) `"réseau"[0]` et `"réseau"[-1]`.

<details markdown="1">
<summary>Voir la réponse</summary>

(a) 8. (b) `"53"` : deux textes collés. (c) 8. (d) `"53"`. (e) 6. (f) `"r"` et `"u"`.

</details>

## Exercice 3 – Condition

On définit :

```python
def resultat(note):
    if note < 8:
        return "ajourné"
    elif note < 10:
        return "rattrapage"
    else:
        return "admis"
```

Que renvoient `resultat(7.5)`, `resultat(8)`, `resultat(10)` ?

<details markdown="1">
<summary>Voir la réponse</summary>

`resultat(7.5)` : `"ajourné"`. `resultat(8)` : `8 < 8` est faux, `8 < 10` est vrai : `"rattrapage"`. `resultat(10)` : les deux premières conditions sont fausses : `"admis"`.

</details>

## Exercice 4 – Boucle `for`

Qu'affiche ce programme ? Quelle valeur a `total` à la fin ?

```python
total = 0
for i in range(3, 7):
    print(i * i)
    total = total + i
```

<details markdown="1">
<summary>Voir la réponse</summary>

`range(3, 7)` donne 3, 4, 5, 6. Affichage : 9, 16, 25, 36 (un nombre par ligne). `total` vaut \(3 + 4 + 5 + 6 = 18\).

</details>

## Exercice 5 – Trace d'une boucle `while`

```python
n = 2026
s = 0
while n > 0:
    s = s + n % 10
    n = n // 10
```

Écrire le tableau de suivi de `n` et `s`. Que calcule ce programme ?

<details markdown="1">
<summary>Voir la réponse</summary>

| Tour | `n` au début | `s` à la fin | `n` à la fin |
|---|---|---|---|
| 1 | 2026 | 6 | 202 |
| 2 | 202 | 8 | 20 |
| 3 | 20 | 8 | 2 |
| 4 | 2 | 10 | 0 |

Le programme calcule la **somme des chiffres** de \(n\) : \(2 + 0 + 2 + 6 = 10\).

</details>

## Exercice 6 – Trouver les erreurs

Trouver l'erreur de chaque extrait :

(a) `if n = 5:` ; (b) `def double(n)` suivi de `return 2 * n` (indenté) ; (c) `print("5" + 3)` ; (d) `while n > 0:` dont le corps ne modifie jamais `n`.

<details markdown="1">
<summary>Voir la réponse</summary>

(a) `=` range une valeur : il faut `==` pour comparer. (b) Il manque le `:` à la fin de la ligne `def`. (c) `TypeError` : on ne peut pas ajouter un texte et un nombre ; écrire `int("5") + 3` ou `"5" + str(3)`. (d) `n` ne change jamais : la condition reste vraie, la boucle ne s'arrête pas.

</details>

## Exercice 7 – Liste

Qu'affiche ce programme ?

```python
l = [4, 8, 15]
l.append(16)
print(len(l), l[0], l[-1], sum(l))
```

<details markdown="1">
<summary>Voir la réponse</summary>

Après `append`, `l` vaut `[4, 8, 15, 16]` : `4 4 16 43` (longueur 4, premier 4, dernier 16, somme \(4 + 8 + 15 + 16 = 43\)).

</details>

## Je sais faire

Coche honnêtement ; ce que tu ne coches pas se reprend avant S01.

- [ ] Lancer un script et lire un message d'erreur ;
- [ ] Prévoir ce que fait un programme avec `//` et `%` ;
- [ ] Distinguer un nombre d'un texte (`int`, `str`, `len`) ;
- [ ] Lire une condition `if` / `elif` / `else` ;
- [ ] Écrire un tableau de suivi pour une boucle `while` ;
- [ ] Compléter une fonction avec `def` et `return`.

**Ce que je dois reprendre :** ______________________

**Ma question à poser à l'enseignant :** ______________________

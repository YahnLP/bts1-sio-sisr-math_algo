# Exercices – Boucles, suivi de variables et construction

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S04*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**, avec la méthode du cours : écris les étapes, pas seulement le résultat. Ouvre ensuite « Voir la réponse » pour te corriger. À l'épreuve, **aucune réponse sans justification** n'est complète.

## Exercice 1 – Trace d'une boucle `POUR`

```text
s ← 0
POUR i DE 1 À 5 FAIRE
  s ← s + i × i
FIN POUR
```

Dérouler l'algorithme et donner la valeur finale de `s`. Quelle somme calcule-t-il ?

<details markdown="1">
<summary>Voir la réponse</summary>

| Tour | `i` | `s` avant | `s` après |
|---|---|---|---|
| 1 | 1 | 0 | 1 |
| 2 | 2 | 1 | 5 |
| 3 | 3 | 5 | 14 |
| 4 | 4 | 14 | 30 |
| 5 | 5 | 30 | 55 |

`s` vaut 55 à la fin : \(1^2 + 2^2 + 3^2 + 4^2 + 5^2\).

</details>

## Exercice 2 – Nombre de tours

```text
i ← 1
c ← 0
TANT QUE i < 1000 FAIRE
  i ← i × 3
  c ← c + 1
FIN TANT QUE
```

Donner la valeur de `i` et de `c` à la sortie. Quel est le variant qui garantit la terminaison ?

<details markdown="1">
<summary>Voir la réponse</summary>

`i` prend les valeurs 1, 3, 9, 27, 81, 243, 729, 2187 : à la sortie `i` vaut 2187 (le premier \(3^k \ge 1\,000\) car \(3^6 = 729 < 1\,000\)) et `c` vaut 7.

Le variant n'est pas `i` (qui augmente) mais l'entier \(1\,000 - i\) tant qu'il est positif : il diminue **strictement** à chaque tour (puisque `i` augmente) ; la boucle s'arrête donc.

</details>

## Exercice 3 – Terminaison

Dire pour chaque boucle si elle s'arrête, et pourquoi.

1. `i ← 10` ; `TANT QUE i > 0 FAIRE i ← i − 3`
2. `i ← 10` ; `TANT QUE i ≠ 0 FAIRE i ← i − 3`
3. `i ← 1` ; `TANT QUE i > 0 FAIRE i ← i + 1`

<details markdown="1">
<summary>Voir la réponse</summary>

1. Oui : `i` prend les valeurs 10, 7, 4, 1, -2 ; dès qu'il devient négatif ou nul, la condition est fausse. Le variant est `i`, qui décroît strictement (de 3) tout en restant un entier ; il atteint une valeur ≤ 0.
2. Non : `i` prend les valeurs 10, 7, 4, 1, -2, -5, … et ne vaut **jamais** 0 (10 n'est pas multiple de 3). Une condition `≠` est dangereuse : on préfère `>`.
3. Non : `i` augmente, donc reste strictement positif.

</details>

## Exercice 4 – Construire une boucle

Écrire en pseudo-code, avec en-tête, un algorithme qui calcule la somme des multiples de 3 compris entre 1 et 100. Donner le résultat.

<details markdown="1">
<summary>Voir la réponse</summary>

```text
ALGORITHME somme_multiples_de_3
  RÔLE      : somme des multiples de 3 de 1 à 100
  SORTIE    : s (entier)
  VARIABLES : i, s (entiers)
DÉBUT
  s ← 0
  POUR i DE 1 À 100 FAIRE
    SI i mod 3 = 0 ALORS
      s ← s + i
    FIN SI
  FIN POUR
  RETOURNER s
FIN
```

Résultat : \(3 + 6 + \dots + 99 = 3 \times (1 + 2 + \dots + 33) = 3 \times \dfrac{33 \times 34}{2} = 1683\).

</details>

## Exercice 5 – Chiffres d'un nombre

1. Dérouler `nombre_de_chiffres` du cours pour \(n = 90\,210\).
2. Écrire un algorithme `somme_des_chiffres` et le dérouler pour \(n = 2\,024\).

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(90\,210 \to 9\,021 \to 902 \to 90 \to 9 \to 0\) : 5 tours, donc 5 chiffres.
2.

```text
ALGORITHME somme_des_chiffres
  ENTRÉE : n (entier ≥ 0)
  SORTIE : s (entier)
DÉBUT
  s ← 0
  TANT QUE n > 0 FAIRE
    s ← s + (n mod 10)
    n ← n div 10
  FIN TANT QUE
  RETOURNER s
FIN
```

Pour 2 024 : \(4 + 2 + 0 + 2 = 8\).

</details>

## Exercice 6 – Conversion en base \(b\)

Dérouler l'algorithme `vers_base` du cours pour \(n = 205\) et \(b = 16\), puis \(n = 37\) et \(b = 2\).

<details markdown="1">
<summary>Voir la réponse</summary>

**205 en base 16** :

| Tour | `n` avant | `reste` | `n` après | `texte` |
|---|---|---|---|---|
| 1 | 205 | 13 | 12 | `D` |
| 2 | 12 | 12 | 0 | `CD` |

Résultat : CD (les restes 13 et 12 s'écrivent D et C).

**37 en base 2** :

| Tour | `n` avant | `reste` | `n` après | `texte` |
|---|---|---|---|---|
| 1 | 37 | 1 | 18 | `1` |
| 2 | 18 | 0 | 9 | `01` |
| 3 | 9 | 1 | 4 | `101` |
| 4 | 4 | 0 | 2 | `0101` |
| 5 | 2 | 0 | 1 | `00101` |
| 6 | 1 | 1 | 0 | `100101` |

Résultat : 100101.

</details>

## Exercice 7 – Maximum

On parcourt la liste `[4, 9, 2, 9, 7]`. Dérouler la recherche du maximum avec son **premier** indice (les indices commencent à 0).

<details markdown="1">
<summary>Voir la réponse</summary>

```text
m ← L[0] ; position ← 0
POUR i DE 1 À longueur(L) − 1 FAIRE
  SI L[i] > m ALORS
    m ← L[i] ; position ← i
  FIN SI
FIN POUR
```

| i | L[i] | L[i] > m ? | m après | position après |
|---|---|---|---|---|
| 1 | 9 | oui | 9 | 1 |
| 2 | 2 | non | 9 | 1 |
| 3 | 9 | non | 9 | 1 |
| 4 | 7 | non | 9 | 1 |

Départ : `m = 4`, `position = 0`. À la fin : `m = 9` et `position = 1`. L'inégalité **stricte** `>` garde le premier maximum : le second 9 (indice 3) n'est pas plus grand que `m`.

</details>

## Exercice 8 – Boucles imbriquées

```text
c ← 0
POUR i DE 1 À 6 FAIRE
  POUR j DE i + 1 À 6 FAIRE
    c ← c + 1
  FIN POUR
FIN POUR
```

1. Combien de couples \((i, j)\) sont comptés ?
2. Généraliser pour \(n\) au lieu de 6.

<details markdown="1">
<summary>Voir la réponse</summary>

1. Pour \(i = 1, 2, \dots, 6\), la boucle intérieure fait \(5, 4, 3, 2, 1, 0\) tours : \(5 + 4 + 3 + 2 + 1 + 0 = 15\).
2. \((n-1) + (n-2) + \dots + 1 + 0 = \dfrac{n(n-1)}{2}\). Pour \(n = 6\) : \(\dfrac{6 \times 5}{2} = 15\). C'est le nombre de paires que l'on peut former avec \(n\) éléments.

</details>


## Je sais faire

Coche honnêtement ; ce que tu ne coches pas se reprend avant la séance suivante.

- [ ] Choisir le bon type de boucle ;
- [ ] Appliquer la méthode initialisation / test / mise à jour ;
- [ ] Justifier la terminaison d'une boucle ;
- [ ] Écrire deux boucles imbriquées ;
- [ ] Écrire la conversion d'un entier en base \(b\).

**Ce que je dois reprendre :** ______________________

**Ma question à poser à l'enseignant :** ______________________

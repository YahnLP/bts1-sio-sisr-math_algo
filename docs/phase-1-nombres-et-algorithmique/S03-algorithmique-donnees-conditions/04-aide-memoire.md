# Aide-mémoire – Algorithmique : données et conditions

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S03*

> Un mot ou un sigle inconnu ? Passe la souris dessus, ou ouvre le [glossaire](../../ressources/glossaire.md).

## En-tête d'un algorithme

```text
ALGORITHME nom
  RÔLE      : ...
  ENTRÉE(S) : ... (type)
  SORTIE    : ... (type)
  VARIABLES : ... (type)
DÉBUT
  ...
FIN
```

## Types et opérateurs

| Type | Python | Exemple |
|---|---|---|
| Entier | `int` | `42` |
| Réel | `float` | `3.14` |
| Booléen | `bool` | `True` |
| Chaîne | `str` | `"192.168.1.10"` |

| Opération | Python |
|---|---|
| Quotient / reste (division euclidienne) | `a // b`, `a % b` |
| Puissance | `a ** b` |
| Égalité / différence | `==`, `!=` |
| Non, et, ou | `not`, `and`, `or` |
| Et, ou, ou exclusif bit à bit | `&`, `|`, `^` |
| Décalages | `<<`, `>>` |

## Masques

| Je veux… | Expression |
|---|---|
| Tester un bit | `(x & m) != 0` |
| Mettre à 1 | `x | m` |
| Mettre à 0 | `x & ~m` |
| Changer d'état | `x ^ m` |

## Conditionnelle

```python
if condition_1:
    ...
elif condition_2:
    ...
else:
    ...
```

Le premier test vrai l'emporte : **le plus particulier d'abord**.

## Méthode de test

1. Choisir un jeu d'essai (cas typiques et cas limites).
2. Calculer les résultats attendus **sans** passer par l'algorithme.
3. Dérouler l'algorithme (trace) et comparer.

# Aide-mémoire – Division euclidienne et PGCD

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S05*

> Un mot ou un sigle inconnu ? Passe la souris dessus, ou ouvre le [glossaire](../../ressources/glossaire.md).

## Division euclidienne

\[
a = b\,q + r , \qquad 0 \le r < b , \qquad (q, r) \text{ unique} .
\]

`q = a // b` et `r = a % b` en Python (avec \(b > 0\)). \(b \mid a \iff r = 0\).

## Critères de divisibilité

| Par | Critère |
|---|---|
| 2 | dernier chiffre pair |
| 3 | somme des chiffres divisible par 3 |
| 4 | deux derniers chiffres divisibles par 4 |
| 5 | dernier chiffre 0 ou 5 |
| 9 | somme des chiffres divisible par 9 |
| 10 | dernier chiffre 0 |

## PGCD et PPCM

\[
\operatorname{PGCD}(a, b) = \operatorname{PGCD}(b, r) , \qquad \operatorname{PGCD}(a, 0) = a , \qquad \operatorname{PGCD} \times \operatorname{PPCM} = a \times b .
\]

```python
def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
```

- Le **dernier reste non nul** est le PGCD.
- **Premiers entre eux** : \(\operatorname{PGCD} = 1\).
- Variant : la suite des restes, strictement décroissante.

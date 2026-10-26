# Aide-mémoire – Congruences

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S07*

> Un mot ou un sigle inconnu ? Passe la souris dessus, ou ouvre le [glossaire](../../ressources/glossaire.md).

## Définition

\[
a \equiv b \pmod n \iff n \mid (a - b) \iff \text{même reste dans la division par } n .
\]

## Calculs

Compatible avec \(+\), \(-\), \(\times\) et les puissances : **on réduit à chaque étape**. Pas de simplification automatique.

## Inverse modulo n

- \(a\) a un inverse modulo \(n\) ⟺ \(\operatorname{PGCD}(a, n) = 1\).
- Résoudre \(a x \equiv c\) : \(x \equiv a' c\) où \(a' a \equiv 1\).
- Inverses modulo 26 : 1→1, 3→9, 5→21, 7→15, 9→3, 11→19, 15→7, 17→23, 19→11, 21→5, 23→17, 25→25.

## Applications

| Application | Formule |
|---|---|
| César | \(y \equiv x + s \pmod{26}\) |
| Affine | \(y \equiv a x + b \pmod{26}\), \(\operatorname{PGCD}(a, 26) = 1\) ; \(x \equiv a'(y - b)\) |
| NIR | clé \(= 97 - (N \bmod 97)\) |
| ISBN-13 | \(\sum\) poids (1, 3, …) × chiffre \(\equiv 0 \pmod{10}\) |
| IBAN | nombre réarrangé \(\equiv 1 \pmod{97}\) |
| Hachage | case \(= x \bmod m\) |
| Liste circulaire (taille \(n\), saut \(k\)) | tout est visité ⟺ \(\operatorname{PGCD}(k, n) = 1\) |

## Python

```python
a % n              # reste (entre 0 et n-1 pour n > 0)
pow(a, k, n)       # a**k modulo n
pow(a, -1, n)      # inverse modulo n (Python 3.8 et plus), erreur s'il n'existe pas
```

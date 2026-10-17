# Aide-mémoire – Réels, arrondis et calcul en binaire

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S02*

> Un mot ou un sigle inconnu ? Passe la souris dessus, ou ouvre le [glossaire](../../ressources/glossaire.md).

## Partie fractionnaire

\[
(a_k \dots a_0 , a_{-1} \dots a_{-m})_2 = \sum_{i=-m}^{k} a_i\, 2^i .
\]

| Je veux… | Méthode |
|---|---|
| Fraction binaire → décimal | Somme des \(a_i \times 2^{i}\) (poids \(\frac12, \frac14, \frac18, \dots\)) |
| Partie fractionnaire décimal → binaire | **× 2** répété ; chiffres = parties entières, lus de haut en bas |
| Fini en binaire ? | Fraction irréductible \(\frac{k}{2^m}\) |

## Erreur avec \(p\) chiffres binaires après la virgule

| Méthode | Erreur |
|---|---|
| Troncature | \(< 2^{-p}\) |
| Arrondi | \(\le 2^{-(p+1)}\) |

## Opérations binaires

| Opération | Règle |
|---|---|
| \(1 + 1\) | \(10\) : on pose 0, retenue 1 |
| \(1 + 1 + 1\) | \(11\) |
| \(\times\, 2^k\) | Décaler de \(k\) rangs à gauche (`x << k`) |
| \(\div\, 2^k\) | Quotient = `x >> k` ; reste = `x & (2**k - 1)` |
| Sur \(n\) bits | Résultat modulo \(2^n\) ; débordement si la somme est \(> 2^n - 1\) |

## Unités

| Décimal (SI) | Binaire (CEI) |
|---|---|
| 1 ko = \(10^3\) o | 1 Kio = \(2^{10}\) o = 1 024 o |
| 1 Mo = \(10^6\) o | 1 Mio = \(2^{20}\) o |
| 1 Go = \(10^9\) o | 1 Gio = \(2^{30}\) o |
| 1 To = \(10^{12}\) o | 1 Tio = \(2^{40}\) o |

- 1 octet = 8 bits ; débit en bit/s ; durée \(= \dfrac{\text{octets} \times 8}{\text{débit en bit/s}}\).

## Python

```python
0.1 + 0.2 == 0.3          # False : ne pas comparer des float avec ==
abs(a - b) < 1e-9         # comparaison à une tolérance
from fractions import Fraction   # calcul exact
x << 3                    # x * 8
x >> 2                    # x // 4
```

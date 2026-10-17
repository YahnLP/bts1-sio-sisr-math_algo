# Aide-mémoire – Suites numériques

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S15*

> Un mot ou un sigle inconnu ? Passe la souris dessus, ou ouvre le [glossaire](../../ressources/glossaire.md).

## Formules

| | Arithmétique (raison \(r\)) | Géométrique (raison \(q\)) |
|---|---|---|
| Récurrence | \(u_{n+1} = u_n + r\) | \(u_{n+1} = q\,u_n\) |
| Terme général | \(u_n = u_0 + nr\) | \(u_n = u_0\,q^n\) |
| Somme \(u_0 + \dots + u_n\) | \((n+1)\dfrac{u_0 + u_n}{2}\) | \(u_0 \dfrac{1 - q^{n+1}}{1 - q}\) (\(q \neq 1\)) |
| Variations | croissante si \(r > 0\) | croissante si \(q > 1\) et \(u_0 > 0\) |

- \(1 + 2 + \dots + n = \dfrac{n(n+1)}{2}\) ; \(1 + 2 + 4 + \dots + 2^n = 2^{n+1} - 1\).

## Limites de référence

| \(n,\ n^2,\ \sqrt{n}\) | \(+\infty\) |
|---|---|
| \(1/n,\ 1/n^2,\ 1/\sqrt{n}\) | 0 |
| \(q^n\), \(q > 1\) | \(+\infty\) |
| \(q^n\), \(-1 < q < 1\) | 0 |
| \(q^n\), \(q \le -1\) | pas de limite |

## Algorithme de seuil

```python
n, u = 0, u0
while u < limite:
    u = u * q
    n = n + 1
```

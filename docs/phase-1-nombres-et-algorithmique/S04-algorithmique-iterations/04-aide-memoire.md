# Aide-mémoire – Algorithmique : itérations

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S04*

> Un mot ou un sigle inconnu ? Passe la souris dessus, ou ouvre le [glossaire](../../ressources/glossaire.md).

## Les trois boucles

| Structure | Pseudo-code | Python | Test |
|---|---|---|---|
| Déterministe | `POUR i DE a À b` | `for i in range(a, b + 1):` | Nombre de tours connu |
| Tant que | `TANT QUE cond` | `while cond:` | Avant le tour |
| Répéter | `RÉPÉTER … JUSQU'À cond` | `while True: … if cond: break` | Après le tour |

`range(n)` : \(0 \dots n-1\) ; `range(a, b)` : \(a \dots b-1\) ; `range(a, b, p)` : de \(p\) en \(p\).

## Méthode

1. Initialiser. 2. Condition de continuation. 3. Mettre à jour (se rapprocher de la fin). 4. Justifier la terminaison par un **variant** (entier qui décroît strictement). 5. Traiter après la boucle.

## Schémas

| Besoin | Initialisation | Corps |
|---|---|---|
| Somme | `s = 0` | `s += x` |
| Produit | `p = 1` | `p *= x` |
| Comptage | `c = 0` | `if cond: c += 1` |
| Maximum | `m = L[0]` | `if x > m: m = x` |
| Chiffres | — | `n % 10` (dernier), `n // 10` (reste) |
| Base \(b\) | `texte = ""` | `texte = chiffre(n % b) + texte` ; `n //= b` |

## Vérifier

- Trace sur un petit cas, puis cas limites (0 tour, 1 tour).
- Éviter `≠` dans une condition d'arrêt si on n'est pas sûr de tomber pile.
- Au plus **deux niveaux** d'imbrication.

## Sommes à connaître

\[
1 + 2 + \dots + n = \frac{n(n+1)}{2} , \qquad (n-1) + \dots + 1 = \frac{n(n-1)}{2} .
\]

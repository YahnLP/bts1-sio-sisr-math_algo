# Aide-mémoire – Récursivité et complexité

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S18*

> Un mot ou un sigle inconnu ? Passe la souris dessus, ou ouvre le [glossaire](../../ressources/glossaire.md).

## Récursivité

```python
def f(n):
    if n == 0:        # cas de base
        return ...
    return ... f(n - 1) ...   # appel sur un problème plus petit
```

- Terminaison : un entier naturel qui diminue strictement à chaque appel.
- Sans cas de base : `RecursionError` (environ 1 000 appels imbriqués).
- Récursive terminale (appel en dernier) : facile à transformer en boucle.
- Fibonacci récursif : nombre d'appels \(= 2F_{n+1} - 1\) ; version à boucle : \(n\) additions.

## Complexité (pire cas)

| Algorithme | Comparaisons |
|---|---|
| Recherche séquentielle | \(n\) |
| Dichotomie (tableau trié) | \(\lfloor \log_2 n \rfloor + 1\) |
| Tri par sélection | \(\dfrac{n(n-1)}{2}\) |

## Erreurs classiques

| Erreur | Réflexe |
|---|---|
| Indice hors domaine | indices de 0 à \(n - 1\) ; `range(len(t))` |
| Mauvaise initialisation | `m = t[0]` pour un maximum |
| Boucle infinie | le variant doit changer à chaque tour |
| Égalité de flottants | tolérance, entiers ou `Fraction` |
| Effet de bord | `list(l)` pour travailler sur une copie |

Méthode : reproduire, tracer les variables, trouver le premier écart, corriger, retester les cas limites.

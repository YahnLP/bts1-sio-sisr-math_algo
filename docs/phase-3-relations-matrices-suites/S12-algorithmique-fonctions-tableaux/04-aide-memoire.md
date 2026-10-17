# Aide-mémoire – Fonctions, tableaux et chaînes

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S12*

> Un mot ou un sigle inconnu ? Passe la souris dessus, ou ouvre le [glossaire](../../ressources/glossaire.md).

## Fonctions

```python
def nom(parametres):
    ...
    return resultat
```

- `return` renvoie une valeur ; `print` l'affiche seulement.
- Variable créée dans la fonction = **locale**.
- Une liste passée en paramètre peut être modifiée par la fonction ; `list(t)` en fait une copie.

## Tableaux et chaînes

| | Tableau (liste) | Chaîne |
|---|---|---|
| Indices | 0 à \(n-1\) | 0 à \(n-1\) |
| Longueur | `len(t)` | `len(s)` |
| Dernier | `t[-1]` | `s[-1]` |
| Tranche | `t[a:b]` (exclut `b`) | `s[a:b]` |
| Modifiable | oui | **non** |
| Grille | `g[ligne][colonne]` | |

- `s.split()` découpe sur les espaces ; `"-".join(liste)` assemble.
- Parcourir un tableau : `for i in range(len(t))` (indice) ou `for x in t` (valeur).

## Algorithmes

| Algorithme | Coût |
|---|---|
| Maximum / recherche séquentielle | \(n - 1\) comparaisons / jusqu'à \(n\) |
| Tri par sélection | \(\dfrac{n(n-1)}{2}\) comparaisons |
| Dichotomie (tableau trié) | au plus \(\lfloor \log_2 n \rfloor + 1\) étapes |

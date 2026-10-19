# Aide-mémoire – Syntaxe Python

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S00*

> Un mot ou un sigle inconnu ? Passe la souris dessus, ou ouvre le [glossaire](../../ressources/glossaire.md).

## Calculs

| Écriture | Sens |
|---|---|
| `a + b`, `a - b`, `a * b` | somme, différence, produit |
| `a // b`, `a % b` | quotient, reste de la division euclidienne |
| `a ** b` | puissance |
| `a / b` | division décimale (flottant) |
| `==`, `!=`, `<`, `<=`, `>`, `>=` | comparaisons (`True` / `False`) |
| `and`, `or`, `not` | et, ou, non |

## Texte

| Écriture | Sens |
|---|---|
| `len(t)` | nombre de caractères |
| `t[0]`, `t[-1]` | premier, dernier caractère |
| `a + b` | colle deux textes |
| `str(n)`, `int(t)` | nombre vers texte, texte vers nombre |
| `t.split(".")` | découpe en liste de textes |

## Structures

```python
if condition:          # sinon si : elif, sinon : else
    ...
for i in range(a, b):  # i vaut a, a+1, ..., b-1
    ...
while condition:       # une variable doit changer à chaque tour
    ...
def nom(parametre):
    return resultat
```

## Listes

`l = [4, 8, 15]` · `len(l)` · `l[0]` · `l.append(v)` · `for x in l:`

## Erreurs

| Message | Cause probable |
|---|---|
| `IndentationError` | bloc mal décalé (4 espaces) |
| `SyntaxError` | `:` oublié, guillemets non fermés |
| `NameError` | variable inconnue ou mal écrite |
| `TypeError` | texte et nombre mélangés |

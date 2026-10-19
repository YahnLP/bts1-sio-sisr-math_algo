---
render_macros: true
---

# Annexe – Python : premiers pas

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S01 – à lire avant le [TP Python](03-tp-python.md)*

> [!NOTE]
> **À quoi sert cette annexe.** Les TP des séances S01 et S02 te demandent de **compléter** de petits programmes Python. Les notions de base (variables, conditions, boucles, fonctions) sont reprises **en détail en S03 et S04** ; ici, tu n'apprends que ce qu'il faut pour ces TP. Tu n'as rien à installer : l'éditeur est dans la page. Garde cette page ouverte pendant le TP.

## I. Le programme et l'éditeur

Un programme Python est une suite d'instructions, exécutées **de haut en bas**. Dans l'éditeur du TP :

- le bouton **Lancer** (▶) exécute le script ; ce que le programme `print` s'affiche en dessous ;
- le bouton **Valider** (✓) exécute les tests du TP et dit lesquels échouent ;
- les lignes qui commencent par `#` sont des **commentaires** : Python les ignore, elles t'expliquent le programme ;
- les `...` à remplacer et les lignes « à compléter » sont **ce que tu dois écrire**.

## II. Variables et affectation

Une **variable** est un nom qui garde une valeur. Le signe `=` n'est pas une égalité mathématique : il **range** la valeur de droite dans la variable de gauche.

```python
n = 6
n = n + 1       # n vaut maintenant 7 : on lit la valeur, on ajoute 1, on la range dans n
print(n)        # affiche 7
```

## III. Les calculs sur les entiers

| Écriture | Sens | Exemple | Résultat |
|---|---|---|---|
| `+`, `-`, `*` | addition, soustraction, produit | `3 * 4` | 12 |
| `//` | **quotient** de la division euclidienne | `7 // 2` | 3 |
| `%` | **reste** de la division euclidienne | `7 % 2` | 1 |
| `**` | puissance | `2 ** 8` | 256 |
| `/` | division décimale (attention !) | `7 / 2` | 3.5 |

Pour la division euclidienne \(a = bq + r\), `a // b` donne \(q\) et `a % b` donne \(r\). C'est exactement ce qu'il faut pour les conversions de base du cours.

Les comparaisons `==` (égal), `!=` (différent), `<`, `<=`, `>`, `>=` donnent `True` ou `False`. Attention : `=` **range** une valeur, `==` **compare**.

## IV. Le texte (chaînes de caractères)

Un texte s'écrit entre guillemets. Les chiffres d'une conversion se manipulent comme du **texte**.

```python
t = "1101"
len(t)          # 4 : nombre de caractères
t[0]            # "1" : premier caractère (les positions commencent à 0)
t[-1]           # "1" : dernier caractère
"ab" + "cd"     # "abcd" : on colle deux textes
str(13)         # "13" : nombre vers texte
int("13")       # 13 : texte vers nombre
```

> [!WARNING]
> `"5" + "3"` donne `"53"` (deux textes collés), pas 8. Pour calculer, il faut des nombres.

On accède à un chiffre d'une liste de symboles par sa position : si `CHIFFRES = "0123456789ABCDEF"`, alors `CHIFFRES[11]` vaut `"B"`.

## V. La condition : `if`

```python
if n == 0:
    print("zéro")
else:
    print("non nul")
```

Les deux-points `:` et le **décalage** (4 espaces) sont obligatoires : tout ce qui est décalé fait partie du bloc. Les lignes décalées ne s'exécutent que si la condition est vraie.

## VI. La répétition

**`while` (tant que).** Le bloc décalé se répète tant que la condition est vraie. Il faut que quelque chose **change** à chaque tour, sinon la boucle ne s'arrête jamais.

```python
n = 6
while n > 0:
    print(n)
    n = n // 2      # n diminue : 6, puis 3, puis 1, puis 0 : la boucle s'arrête
```

Affiche 6, 3, 1.

**`for` (pour chaque).** Répète un bloc pour chaque valeur d'une suite : `range(4)` donne 0, 1, 2, 3 ; `range(1, 4)` donne 1, 2, 3.

```python
for k in range(1, 4):
    print(k * 5)    # affiche 5, 10, 15
```

## VII. La fonction : `def` et `return`

Une **fonction** a un nom, des **paramètres** (ses données d'entrée) et **renvoie** un résultat avec `return`. Le bloc décalé est son corps.

```python
def nb_chiffres(n):
    """Nombre de chiffres décimaux de l'entier n (n > 0)."""
    compteur = 0
    while n > 0:
        n = n // 10
        compteur = compteur + 1
    return compteur
```

- les trois guillemets sous la ligne `def` sont un **commentaire d'explication** ;
- `nb_chiffres(2026)` appelle la fonction et vaut 4.

**Suivi pas à pas (la « trace »).** Pour comprendre ou corriger un programme, on note la valeur des variables à chaque tour :

| Tour | `n` au début | `n` à la fin | `compteur` à la fin |
|---|---|---|---|
| 1 | 2026 | 202 | 1 |
| 2 | 202 | 20 | 2 |
| 3 | 20 | 2 | 3 |
| 4 | 2 | 0 | 4 |

Quand `n` vaut 0, la condition `n > 0` est fausse : la boucle s'arrête, la fonction renvoie 4.

## VIII. À toi : lire et modifier un programme

Anticipe sur ta feuille ce que le script ci-dessous affiche (trois lignes pour `nb_chiffres`, puis les restes), lance-le, puis change les nombres.

{{ IDE('premiers_pas', MAX="+") }}

## IX. Messages d'erreur fréquents

| Message | Cause probable |
|---|---|
| `IndentationError` | un bloc n'est pas décalé de la même façon partout (4 espaces) |
| `SyntaxError` | un `:` oublié après `if`, `while` ou `def`, ou des guillemets non fermés |
| `NameError` | une variable est utilisée avant d'avoir reçu une valeur, ou mal orthographiée |
| `TypeError` | on mélange un texte et un nombre (`"5" + 3`) |
| le script ne s'arrête pas | boucle `while` dont la condition ne change jamais : recharge la page |

## À retenir

- `=` range une valeur ; `==` compare.
- `n // b` est le quotient, `n % b` le reste de la division euclidienne.
- Un bloc (`if`, `while`, `def`) se termine par `:` et se décale de 4 espaces.
- Dans une boucle `while`, une variable doit changer pour que la boucle s'arrête.
- Un texte se colle avec `+` et se lit par position (à partir de 0).

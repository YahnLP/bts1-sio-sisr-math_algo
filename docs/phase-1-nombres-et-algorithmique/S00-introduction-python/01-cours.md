# Cours – Premiers pas en Python

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S00 – à lire avant les [exercices](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** aucun.
> - **Outils :** Papier, éditeur Python intégré au site. Chaque exemple de ce cours peut être recopié dans l'éditeur du [TP](03-tp-python.md) pour être essayé.

## À la fin de ce cours tu sauras

- [ ] **Lancer** un script et **lire** un message d'erreur ;
- [ ] **Calculer** avec des variables et les opérations sur les entiers ;
- [ ] **Manipuler** du texte ;
- [ ] **Écrire** une condition et une boucle ;
- [ ] **Écrire** une fonction et **parcourir** une liste.

## I. Un programme, un éditeur

Un programme Python est une suite d'**instructions**, exécutées **de haut en bas**, une ligne après l'autre. Dans l'éditeur du site :

- le bouton **Lancer** exécute le script ; ce que le programme demande d'afficher avec `print` apparaît en dessous ;
- le bouton **Valider** exécute les tests du TP et indique ceux qui échouent ;
- une ligne qui commence par `#` est un **commentaire** : Python l'ignore, elle explique le programme.

```python
print("Bonjour")
print(2 + 3)
```

Affiche `Bonjour` puis `5`. `print(...)` affiche ce qui est entre parenthèses ; un texte s'écrit entre guillemets.

## II. Variables et affectation

Une **variable** est un nom qui garde une valeur. Le signe `=` n'est pas une égalité mathématique : il **range** la valeur de droite dans la variable de gauche (c'est l'**affectation**).

```python
n = 6
n = n + 1       # on lit n (6), on ajoute 1, on range 7 dans n
print(n)        # affiche 7
```

Un nom de variable commence par une lettre et ne contient ni espace ni accent de préférence : `total`, `nb_chiffres`, `reste`.

## III. Les calculs sur les entiers

| Écriture | Sens | Exemple | Résultat |
|---|---|---|---|
| `+`, `-`, `*` | addition, soustraction, produit | `3 * 4` | 12 |
| `//` | **quotient** de la division euclidienne | `7 // 2` | 3 |
| `%` | **reste** de la division euclidienne | `7 % 2` | 1 |
| `**` | puissance | `2 ** 8` | 256 |
| `/` | division décimale (attention !) | `7 / 2` | 3.5 |

Pour la division euclidienne \(a = bq + r\) (S05), `a // b` donne \(q\) et `a % b` donne \(r\). C'est ce qu'il faut pour convertir un nombre dans une autre base.

Les **comparaisons** `==` (égal), `!=` (différent), `<`, `<=`, `>`, `>=` donnent `True` (vrai) ou `False` (faux). On les combine avec `and` (et), `or` (ou), `not` (non).

> [!WARNING]
> `=` **range** une valeur, `==` **compare**. Écrire `if n = 5:` est une erreur.

## IV. Le texte (chaînes de caractères)

Un texte s'écrit entre guillemets. Les chiffres d'un nombre en binaire ou en hexadécimal se manipulent comme du **texte**.

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
> `"5" + "3"` donne `"53"` (deux textes collés), pas 8. Pour calculer, il faut des **nombres** : `int("5") + int("3")` donne 8.

Si `CHIFFRES = "0123456789ABCDEF"`, alors `CHIFFRES[11]` vaut `"B"` : on lit un symbole par sa position.

## V. La condition : `if`

```python
if n == 0:
    print("zéro")
elif n > 0:
    print("positif")
else:
    print("négatif")
```

- les deux-points `:` après la condition sont obligatoires ;
- le **décalage** de 4 espaces (l'**indentation**) indique ce qui fait partie du bloc ;
- `elif` (« sinon si ») et `else` (« sinon ») sont facultatifs ; un seul bloc est exécuté.

## VI. La répétition

**`for` : répéter pour chaque valeur.** `range(4)` donne 0, 1, 2, 3 ; `range(1, 4)` donne 1, 2, 3 (la valeur de fin est **exclue**).

```python
total = 0
for i in range(1, 5):
    total = total + i
print(total)        # affiche 10 (1 + 2 + 3 + 4)
```

**`while` : répéter tant que la condition est vraie.** Il faut que quelque chose **change** à chaque tour, sinon la boucle ne s'arrête jamais.

```python
n = 2026
compteur = 0
while n > 0:
    n = n // 10          # on enlève le dernier chiffre
    compteur = compteur + 1
print(compteur)          # affiche 4
```

**Suivi pas à pas (la « trace »).** Pour comprendre un programme, on note les variables à chaque tour :

| Tour | `n` au début | `n` à la fin | `compteur` à la fin |
|---|---|---|---|
| 1 | 2026 | 202 | 1 |
| 2 | 202 | 20 | 2 |
| 3 | 20 | 2 | 3 |
| 4 | 2 | 0 | 4 |

Quand `n` vaut 0, la condition `n > 0` est fausse : la boucle s'arrête.

## VII. La fonction : `def` et `return`

Une **fonction** a un nom, des **paramètres** (ses données d'entrée) et **renvoie** un résultat avec `return`. Le bloc décalé est son corps.

```python
def est_pair(n):
    """Renvoie True si n est pair."""
    return n % 2 == 0

print(est_pair(10))     # True
print(est_pair(7))      # False
```

- les trois guillemets sous la ligne `def` sont un commentaire d'explication ;
- `return` termine la fonction et renvoie la valeur ;
- une fonction peut renvoyer plusieurs valeurs : `return (q, r)` renvoie un **couple**.

Dans les TP, on te donne l'en-tête de la fonction et on te laisse écrire les lignes marquées `...` ou `À compléter`.

## VIII. Les listes

Une **liste** range plusieurs valeurs : `[4, 8, 15]`. Comme pour un texte, les positions commencent à 0.

```python
l = [4, 8, 15]
l.append(16)        # ajoute 16 à la fin : [4, 8, 15, 16]
len(l)              # 4
l[0]                # 4
for x in l:         # parcourt les éléments un par un
    print(x)
```

Un texte se découpe en liste avec `split` : `"192.168.1.10".split(".")` donne `["192", "168", "1", "10"]`.

## IX. Lire un message d'erreur

| Message | Cause probable |
|---|---|
| `IndentationError` | un bloc n'est pas décalé de la même façon partout (4 espaces) |
| `SyntaxError` | un `:` oublié après `if`, `while` ou `def`, ou des guillemets non fermés |
| `NameError` | une variable est utilisée avant d'avoir reçu une valeur, ou mal orthographiée |
| `TypeError` | on mélange un texte et un nombre (`"5" + 3`) |
| `ZeroDivisionError` | division par 0 |
| le script ne s'arrête pas | boucle `while` dont la condition ne change jamais : recharge la page |

La **dernière ligne** du message dit ce qui ne va pas ; la ligne précédente indique où.

## À retenir

- `=` range une valeur ; `==` compare.
- `n // b` est le quotient, `n % b` le reste de la division euclidienne.
- Un bloc (`if`, `for`, `while`, `def`) commence par `:` et se décale de 4 espaces.
- `range(a, b)` va de `a` à `b - 1`.
- Dans une boucle `while`, une variable doit changer pour que la boucle s'arrête.
- Un texte se colle avec `+` et se lit par position (à partir de 0) ; `int` et `str` convertissent.

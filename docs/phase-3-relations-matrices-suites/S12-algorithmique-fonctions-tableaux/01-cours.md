# Cours – Fonctions, tableaux et chaînes de caractères

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S12 – à lire avant les [exercices](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** S03, S04 (instructions, boucles) ; S07 (modulo).
> - **Outils :** Papier, calculatrice, éditeur Python intégré au site

## À la fin de ce cours tu sauras

- [ ] **Écrire** une fonction avec paramètres et valeur retournée, et **distinguer** variable locale et globale ;
- [ ] **Manipuler** un tableau à une ou deux dimensions (parcours, indices, recherche, minimum) ;
- [ ] **Éviter** les erreurs d'indice hors domaine ;
- [ ] **Manipuler** des chaînes de caractères (parcours, extraction, concaténation) ;
- [ ] **Programmer** un tri simple et une recherche.

## I. Découper en fonctions

Une **fonction** est un bloc de code nommé, qui reçoit des **paramètres**, effectue un traitement et **retourne** un résultat. Elle sert à :

- **ne pas répéter** le même code ;
- **tester** une partie du programme séparément ;
- **nommer** une idée (`est_privee(ip)` se lit mieux que cinq lignes de conditions).

```text
FONCTION moyenne(t, n)
  RÔLE      : moyenne des n valeurs du tableau t
  ENTRÉES   : t (tableau de nombres), n (entier, n ≥ 1)
  SORTIE    : m (nombre)
  VARIABLES : i (entier), s (nombre)
DÉBUT
  s ← 0
  POUR i DE 0 À n - 1 FAIRE
    s ← s + t[i]
  FIN POUR
  RETOURNER s / n
FIN
```

```python
def moyenne(t):
    s = 0
    for x in t:
        s = s + x
    return s / len(t)

print(moyenne([12, 8, 15]))   # 11.666666666666666
```

Une fonction qui n'**affiche** que (sans `return`) renvoie `None` : on ne peut pas réutiliser son résultat. **Retourner** et **afficher** sont deux actions différentes.

### Variables locales et globales

Une variable créée **dans** une fonction est **locale** : elle n'existe que pendant l'exécution de la fonction. Une variable créée **hors** de toute fonction est **globale**.

```python
total = 100            # globale

def ajoute(x):
    total = x + 1      # nouvelle variable LOCALE, la globale n'est pas modifiée
    return total

print(ajoute(5), total)
```

Ce programme affiche `6 100`. Pour modifier la variable globale il faudrait écrire `global total`, ce qu'on **évite** : il vaut mieux passer les valeurs en paramètres et récupérer le résultat avec `return`.

> [!WARNING]
> **Les listes sont modifiables.** Quand on passe une liste à une fonction, la fonction reçoit la liste elle-même (pas une copie) : si elle la modifie (`t[0] = 0`, `t.append(...)`), l'appelant voit le changement. Pour travailler sur une copie : `t2 = list(t)`.

## II. Les tableaux

Un **tableau** est une suite d'éléments repérés par leur **indice**. Convention de ce cours : les indices vont de **0 à n − 1** (comme en Python, où le tableau est une `list`).

| Opération | Pseudo-code | Python |
|---|---|---|
| Lire un élément | `t[i]` | `t[i]` |
| Modifier un élément | `t[i] ← v` | `t[i] = v` |
| Nombre d'éléments | \(n\) | `len(t)` |
| Dernier élément | `t[n - 1]` | `t[-1]` ou `t[len(t) - 1]` |

> [!WARNING]
> **Indice hors domaine.** Si le tableau a \(n\) éléments, les indices valides sont \(0, \dots, n - 1\). Accéder à `t[n]` provoque l'erreur `IndexError`. Une boucle `POUR i DE 0 À n` (au lieu de `n - 1`) est l'erreur classique.

### Parcours et recherche d'un maximum

```text
ALGORITHME maximum
  RÔLE      : plus grande valeur d'un tableau non vide
  ENTRÉES   : t (tableau), n (nombre d'éléments, n ≥ 1)
  SORTIE    : m (valeur maximale)
  VARIABLES : i (entier), m (nombre)
DÉBUT
  m ← t[0]
  POUR i DE 1 À n - 1 FAIRE
    SI t[i] > m ALORS
      m ← t[i]
    FIN SI
  FIN POUR
  RETOURNER m
FIN
```

Sur `t = [14, 3, 27, 9, 27, 5]` (\(n = 6\)), `m` vaut 14 au départ, puis 14, **27**, 27, 27, 27 après chacun des cinq tours : le maximum est 27. Pour obtenir sa **position**, on mémorise l'indice. Le premier indice du maximum est 2 (la valeur 27 apparaît aussi à l'indice 4 : avec `>` strict, la première occurrence est conservée).

### Recherche séquentielle

On parcourt le tableau jusqu'à trouver la valeur.

```python
def position(t, x):
    for i in range(len(t)):
        if t[i] == x:
            return i
    return -1          # convention : -1 signifie « absent »
```

Dans le pire cas (valeur absente), on compare \(n\) fois. Sur un tableau **trié**, on peut faire mieux (partie V).

### Tableaux à deux dimensions

Un tableau à deux dimensions est un tableau de tableaux : `g[i][j]` est l'élément de la **ligne** `i` et de la **colonne** `j`.

| | C0 | C1 | C2 | C3 |
|---|---|---|---|---|
| **L0** | 12 | 8 | 15 | 10 |
| **L1** | 9 | 14 | 11 | 7 |
| **L2** | 16 | 13 | 6 | 18 |

`g[1][2]` vaut 11 ; la ligne `g[2]` est `[16, 13, 6, 18]`. Pour parcourir toute la grille, on utilise **deux boucles imbriquées** :

```python
for i in range(len(g)):           # lignes
    for j in range(len(g[0])):    # colonnes
        ...g[i][j]...
```

Sommes par ligne : [45, 41, 53] ; par colonne : [37, 35, 32, 35]. Les deux totaux sont égaux : 139 = 139.

## III. Les chaînes de caractères

Une **chaîne** est une suite de caractères indexée comme un tableau (de 0 à \(n - 1\)), mais **non modifiable** : `s[0] = "x"` est interdit.

| Opération | Exemple avec `s = "srv-web-01"` | Résultat |
|---|---|---|
| Longueur | `len(s)` | 10 |
| Caractère | `s[0]`, `s[-1]` | `s`, `1` |
| Tranche `s[a:b]` (de `a` à `b - 1`) | `s[4:7]` | `web` |
| Concaténation | `s + "-b"` | `srv-web-01-b` |
| Découpage | `s.split("-")` | `['srv', 'web', '01']` |
| Majuscules | `s.upper()` | `SRV-WEB-01` |
| Appartenance | `"web" in s` | True |

> [!NOTE]
> Dans une tranche, la borne de droite est **exclue** (comme `range`). `s[a:b]` contient \(b - a\) caractères.

### Exploiter un journal

Une ligne de journal est une chaîne dont les champs sont séparés par des espaces :

```text
2026-03-14 08:13:02 192.168.1.77 LOGIN_FAILED admin
```

`ligne.split()` renvoie la liste `['2026-03-14', '08:13:02', '192.168.1.77', 'LOGIN_FAILED', 'admin']` : date en `[0]`, heure en `[1]`, adresse en `[2]`, événement en `[3]`, compte en `[4]`. Pour compter les échecs de connexion par adresse, on utilise un **dictionnaire** :

```python
def echecs(lignes):
    d = {}
    for ligne in lignes:
        c = ligne.split()
        if c[3] == "LOGIN_FAILED":
            d[c[2]] = d.get(c[2], 0) + 1
    return d
```

Sur les 6 lignes de l'exercice, le résultat est `{'192.168.1.77': 3, '192.168.1.23': 1}` : l'adresse `192.168.1.77` cumule 3 échecs, ce qui ressemble à une tentative de devinette de mot de passe.

## IV. Le tri par sélection

Pour trier un tableau par ordre croissant : à chaque passe \(i\), on cherche le **minimum** des éléments d'indices \(i\) à \(n - 1\) et on l'échange avec l'élément d'indice \(i\).

```text
ALGORITHME tri_selection
  RÔLE      : trier t (n éléments) par ordre croissant
  ENTRÉES   : t (tableau), n (entier)
  SORTIE    : t trié
  VARIABLES : i, j, m (entiers), tmp (même type que t)
DÉBUT
  POUR i DE 0 À n - 2 FAIRE
    m ← i
    POUR j DE i + 1 À n - 1 FAIRE
      SI t[j] < t[m] ALORS
        m ← j
      FIN SI
    FIN POUR
    tmp ← t[i] ; t[i] ← t[m] ; t[m] ← tmp
  FIN POUR
FIN
```

Trace sur `[7, 3, 5, 1]` :

| Passe \(i\) | Minimum cherché dans | Position du min | Échange | Tableau après |
|---|---|---|---|---|
| 0 | indices 0 à 3 | 3 | oui | `[1, 3, 5, 7]` |
| 1 | indices 1 à 3 | 1 | non | `[1, 3, 5, 7]` |
| 2 | indices 2 à 3 | 2 | non | `[1, 3, 5, 7]` |

Résultat : `[1, 3, 5, 7]`. Le nombre de comparaisons est 6 \(= \dfrac{n(n-1)}{2}\) avec \(n = 4\) : \(\dfrac{4 \times 3}{2} = 6\). C'est vrai quelle que soit la disposition initiale (la boucle intérieure ne dépend pas des valeurs) : n = 10 : 45 ; n = 100 : 4950 ; n = 1000 : 499500 comparaisons.

Remarque : dans cette séance on étudie un tri **écrit à la main** ; Python propose `sorted(t)` et `t.sort()`, qu'on utilise en pratique.

## V. Recherche dichotomique

Dans un tableau **trié**, on compare la valeur cherchée à l'élément du **milieu**, ce qui élimine la moitié du tableau à chaque étape.

```text
début ← 0 ; fin ← n - 1
TANT QUE début ≤ fin FAIRE
  milieu ← (début + fin) DIV 2
  SI t[milieu] = x ALORS RETOURNER milieu
  SINON SI t[milieu] < x ALORS début ← milieu + 1
  SINON fin ← milieu - 1
FIN TANT QUE
RETOURNER -1
```

Recherche de 38 dans `[2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44]` (15 éléments) :

| Étape | début | fin | milieu | `t[milieu]` | Décision |
|---|---|---|---|---|---|
| 1 | 0 | 14 | 7 | 23 | 38 > 23 : on cherche à droite |
| 2 | 8 | 14 | 11 | 35 | 38 > 35 : on cherche à droite |
| 3 | 12 | 14 | 13 | 41 | 38 < 41 : on cherche à gauche |
| 4 | 12 | 12 | 12 | 38 | trouvé |

Trouvé à l'indice 12 en 4 étapes (au lieu de 13 comparaisons en séquentiel). Au pire, la taille de la zone est divisée par 2 à chaque étape : il faut au plus \(\lfloor \log_2 n \rfloor + 1\) étapes. Mesuré sur toutes les positions possibles : 4 étapes au plus pour 15 éléments, 10 pour 1 000 éléments, 11 pour 1 024. Le tableau doit être **trié** : sinon le résultat est faux.

## À retenir

- Une fonction **retourne** une valeur (`return`) ; les variables créées dedans sont **locales**.
- Tableau de \(n\) éléments : indices de **0 à n − 1** ; hors de ces bornes, `IndexError`.
- Tableau 2D : `g[ligne][colonne]` ; deux boucles imbriquées.
- Chaîne : indices de 0 à \(n - 1\), tranche `s[a:b]` (borne droite exclue), `split`, non modifiable.
- Tri par sélection : \(\dfrac{n(n-1)}{2}\) comparaisons. Dichotomie (tableau trié) : au plus \(\lfloor \log_2 n \rfloor + 1\) étapes.

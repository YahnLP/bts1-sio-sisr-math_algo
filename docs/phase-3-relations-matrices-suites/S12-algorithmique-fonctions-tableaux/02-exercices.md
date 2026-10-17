# Exercices – Fonctions, tableaux et chaînes

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S12*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**, avec la méthode du cours : écris les étapes, pas seulement le résultat. Ouvre ensuite « Voir la réponse » pour te corriger. À l'épreuve, **aucune réponse sans justification** n'est complète.

## Exercice 1 – Une fonction à tracer

On considère :

```python
def mystere(t):
    r = 0
    for x in t:
        if x % 2 == 0:
            r = r + x
    return r
```

1. Que renvoie `mystere([3, 4, 7, 10, 2])` ? Écrire la trace de `r`.
2. Que calcule cette fonction ? Que renvoie `mystere([])` ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. Les valeurs paires sont 4, 10, 2 : `r` passe de 0 à 4, puis 14, puis 16. Résultat 16.
2. La **somme des éléments pairs**. Pour un tableau vide, la boucle ne s'exécute pas : le résultat est 0.

</details>

## Exercice 2 – Portée des variables

Quel est l'affichage de ce programme ? Expliquer.

```python
x = 10

def f(x):
    x = x + 1
    return x

def g():
    y = 5
    return y * 2

a = f(3)
b = g()
print(a, b, x)
```

<details markdown="1">
<summary>Voir la réponse</summary>

Affichage : `4 10 10`. Dans `f`, `x` est un **paramètre local** (valeur 3, puis 4) : la variable globale `x` reste à 10. `y` n'existe que dans `g`.

</details>

## Exercice 3 – Maximum et position

Pour `t = [14, 3, 27, 9, 27, 5]` : (a) donner le maximum et l'indice de sa première occurrence ; (b) donner le minimum et sa position ; (c) combien de comparaisons fait la recherche du maximum (algorithme du cours) ?

<details markdown="1">
<summary>Voir la réponse</summary>

(a) Maximum 27, première position 2.
(b) Minimum 3, position 1.
(c) \(n - 1 = 5\) comparaisons (une par élément à partir de l'indice 1).

</details>

## Exercice 4 – Où est l'erreur ?

Cet algorithme doit afficher tous les éléments d'un tableau `t` de `n` éléments.

```text
POUR i DE 1 À n FAIRE
  AFFICHER t[i]
FIN POUR
```

1. Quelles deux erreurs contient-il (indices de 0 à \(n - 1\)) ?
2. Corriger. Même question pour `for i in range(len(t) + 1):`.

<details markdown="1">
<summary>Voir la réponse</summary>

1. L'élément `t[0]` n'est jamais affiché, et `t[n]` n'existe pas (erreur d'indice hors domaine).
2. `POUR i DE 0 À n - 1` ; en Python `for i in range(len(t))`. Avec `range(len(t) + 1)`, le dernier tour accède à `t[len(t)]` : `IndexError`.

</details>

## Exercice 5 – Tableau à deux dimensions

Voici le nombre de connexions par jour et par serveur :

| | Serveur A | Serveur B | Serveur C | Serveur D |
|---|---|---|---|---|
| **Lundi** | 12 | 8 | 15 | 10 |
| **Mardi** | 9 | 14 | 11 | 7 |
| **Mercredi** | 16 | 13 | 6 | 18 |

1. Que vaut `g[1][2]` ? Que désigne `g[2][0]` ?
2. Calculer le total par jour, puis par serveur. Vérifier que les deux totaux généraux sont égaux.
3. Écrire le pseudo-code du total par jour.

<details markdown="1">
<summary>Voir la réponse</summary>

1. `g[1][2]` = 11 (mardi, serveur C) ; `g[2][0]` = 16 (mercredi, serveur A).
2. Par jour : [45, 41, 53] ; par serveur : [37, 35, 32, 35] ; total général 139 dans les deux cas.
3. ```text
   POUR i DE 0 À 2 FAIRE
     s ← 0
     POUR j DE 0 À 3 FAIRE
       s ← s + g[i][j]
     FIN POUR
     AFFICHER s
   FIN POUR
   ```

</details>

## Exercice 6 – Chaînes

Avec `s = "ADMIN-2026-srv01"` donner : `len(s)`, `s[0]`, `s[-1]`, `s[:5]`, `s[6:10]`, `s[-5:]`, `s.split("-")`, `s.lower()`.

<details markdown="1">
<summary>Voir la réponse</summary>

| Expression | Résultat |
|---|---|
| len(s) | `16` |
| s[0] | `'A'` |
| s[-1] | `'1'` |
| s[:5] | `'ADMIN'` |
| s[6:10] | `'2026'` |
| s[-5:] | `'srv01'` |
| s.split("-") | `['ADMIN', '2026', 'srv01']` |
| s.lower() | `'admin-2026-srv01'` |

</details>

## Exercice 7 – Journal

Avec les lignes de journal suivantes :

```text
2026-03-14 08:12:45 192.168.1.23 LOGIN_OK alice
2026-03-14 08:13:02 192.168.1.77 LOGIN_FAILED admin
2026-03-14 08:13:09 192.168.1.77 LOGIN_FAILED admin
2026-03-14 08:13:15 192.168.1.77 LOGIN_FAILED root
2026-03-14 08:14:20 192.168.1.23 LOGIN_FAILED alice
2026-03-14 08:15:01 192.168.1.40 LOGIN_OK bob
```

1. Extraire pour la 2e ligne : l'heure, l'adresse, l'événement, le compte.
2. Combien d'échecs par adresse IP ?
3. Quelle adresse dépasse 2 échecs ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. `c = ligne.split()` donne `['2026-03-14', '08:13:02', '192.168.1.77', 'LOGIN_FAILED', 'admin']` : heure `c[1]` = `08:13:02`, adresse `c[2]` = `192.168.1.77`, événement `c[3]` = `LOGIN_FAILED`, compte `c[4]` = `admin`.
2. {'192.168.1.77': 3, '192.168.1.23': 1}.
3. `192.168.1.77` (3 échecs).

</details>

## Exercice 8 – Tri par sélection

1. Dérouler le tri par sélection sur `[7, 3, 5, 1]` en complétant le tableau de passes.
2. Combien de comparaisons ? d'échanges ?
3. Même question pour `[1, 2, 3, 4]` (déjà trié).

<details markdown="1">
<summary>Voir la réponse</summary>

1–2. | Passe \(i\) | Minimum cherché dans | Position du min | Échange | Tableau après |
|---|---|---|---|---|
| 0 | indices 0 à 3 | 3 | oui | `[1, 3, 5, 7]` |
| 1 | indices 1 à 3 | 1 | non | `[1, 3, 5, 7]` |
| 2 | indices 2 à 3 | 2 | non | `[1, 3, 5, 7]` | 6 comparaisons, 1 échanges.
3. Toujours 6 comparaisons (elles ne dépendent pas des valeurs), mais aucun échange réel (le minimum est déjà en place à chaque passe).

</details>

## Exercice 9 – Dichotomie

Tableau trié : `[2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44]`.

1. Chercher 14 par dichotomie : tableau des étapes.
2. Chercher 15 (absent). Combien d'étapes ?
3. Combien d'étapes au plus pour un tableau de 1 000 éléments ? de 1 000 000 ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. | Étape | début | fin | milieu | `t[milieu]` | Décision |
|---|---|---|---|---|---|
| 1 | 0 | 14 | 7 | 23 | 14 < 23 : on cherche à gauche |
| 2 | 0 | 6 | 3 | 11 | 14 > 11 : on cherche à droite |
| 3 | 4 | 6 | 5 | 17 | 14 < 17 : on cherche à gauche |
| 4 | 4 | 4 | 4 | 14 | trouvé |
2. 4 étapes puis `-1`.
3. \(\lfloor \log_2 1000 \rfloor + 1 = 9 + 1 = 10\) ; pour un million : \(\lfloor \log_2 10^6 \rfloor + 1 = 19 + 1 = 20\) (\(2^{19} = 524288 \le 10^6 < 2^{20} = 1048576\)).

</details>

## Exercice 10 – Écrire des fonctions

1. `inverse(s)` renvoie la chaîne à l'envers.
2. `est_palindrome(s)` : `"radar"` et `"kayak"` oui, `"serveur"` non.
3. `nb_voyelles(s)`.

<details markdown="1">
<summary>Voir la réponse</summary>

```python
def inverse(s):
    r = ""
    for c in s:
        r = c + r
    return r

def est_palindrome(s):
    return s == inverse(s)

def nb_voyelles(s):
    n = 0
    for c in s.lower():
        if c in "aeiouy":
            n = n + 1
    return n
```

Contrôle : `inverse("serveur")` donne `ruevres` ; `nb_voyelles("Serveur")` donne 3 (avec `y` compté comme voyelle).

</details>


## Je sais faire

Coche honnêtement ; ce que tu ne coches pas se reprend avant la séance suivante.

- [ ] Écrire une fonction avec paramètres et retour ;
- [ ] Parcourir un tableau sans sortir des indices ;
- [ ] Manipuler un tableau à deux dimensions ;
- [ ] Extraire une partie d'une chaîne ;
- [ ] Trier un tableau avec un algorithme écrit à la main.

**Ce que je dois reprendre :** ______________________

**Ma question à poser à l'enseignant :** ______________________

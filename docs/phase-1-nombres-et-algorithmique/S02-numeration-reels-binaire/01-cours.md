# Cours – Nombres à virgule, arrondis et calcul en binaire

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S02 – à lire avant les [exercices](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** S01 (bases 2, 10, 16).
> - **Outils :** Papier, calculatrice, éditeur Python intégré au site

## À la fin de ce cours tu sauras

- [ ] **Convertir** un nombre à virgule entre les bases 10 et 2 (parties entière et fractionnaire) ;
- [ ] **Reconnaître** les nombres qui s'écrivent avec un nombre fini de chiffres après la virgule en base 2 ;
- [ ] **Arrondir** et **tronquer** un nombre, et **majorer** l'erreur commise ;
- [ ] **Additionner**, **soustraire** et **multiplier** des entiers en binaire, et **décaler** pour multiplier ou diviser par une puissance de 2 ;
- [ ] **Distinguer** unités décimales (ko, Mo, Go) et binaires (Kio, Mio, Gio), bits et octets, et **calculer** des volumes et des durées de transfert.

## I. Les nombres à virgule en base 2

En base \(b\), les chiffres placés **après la virgule** ont pour poids les puissances négatives de \(b\) :

\[
x = (a_k \dots a_0 , a_{-1} a_{-2} \dots a_{-m})_b = \sum_{i=-m}^{k} a_i\, b^i .
\]

**Exemple.** \((101,011)_2 = 1\times2^{2} + 0\times2^{1} + 1\times2^{0} + 0\times2^{-1} + 1\times2^{-2} + 1\times2^{-3} = 5,375\).

### Convertir la partie fractionnaire de la base 10 vers la base 2

On **multiplie par 2** la partie fractionnaire, on note la partie entière obtenue (0 ou 1), puis on recommence avec la nouvelle partie fractionnaire, jusqu'à obtenir 0 ou jusqu'à la précision voulue. Les chiffres se lisent **de haut en bas**, après la virgule. (La partie entière du nombre, elle, se convertit par divisions successives, comme en S01.)

**Exemple.** Écrire \(0,8125\) en binaire.

| Multiplication par 2 | Partie entière | Partie fractionnaire restante |
|---|---|---|
| 13/16 × 2 = 13/8 | **1** | 5/8 |
| 5/8 × 2 = 5/4 | **1** | 1/4 |
| 1/4 × 2 = 1/2 | **0** | 1/2 |
| 1/2 × 2 = 1 | **1** | 0 |

Donc \(0,8125 = (0,1101)_2\). **Contrôle** : \(\frac{1}{2} + \frac{1}{4} + \frac{1}{16} = \frac{13}{16}\).

**Exemple.** \(6{,}375\) : partie entière \(6 = (110)_2\), partie fractionnaire \(0{,}375 = (0,011)_2\), donc \(6{,}375 = (110,011)_2\).

### Quels décimaux ont une écriture finie en base 2 ?

Un nombre s'écrit avec un nombre **fini** de chiffres après la virgule en base 2 si et seulement si c'est un **rationnel \(\dfrac{k}{2^m}\)** (fraction irréductible dont le dénominateur est une puissance de 2). Avec \(m\) chiffres après la virgule, on atteint exactement les multiples de \(2^{-m}\).

Or \(0{,}1 = \dfrac{1}{10}\) et \(10 = 2 \times 5\) : le dénominateur contient le facteur 5, donc **0,1 n'a pas d'écriture finie en binaire**. Ses chiffres se répètent :

| Multiplication par 2 | Partie entière | Partie fractionnaire restante |
|---|---|---|
| 1/10 × 2 = 1/5 | **0** | 1/5 |
| 1/5 × 2 = 2/5 | **0** | 2/5 |
| 2/5 × 2 = 4/5 | **0** | 4/5 |
| 4/5 × 2 = 8/5 | **1** | 3/5 |
| 3/5 × 2 = 6/5 | **1** | 1/5 |
| 1/5 × 2 = 2/5 | **0** | 2/5 |
| 2/5 × 2 = 4/5 | **0** | 4/5 |
| 4/5 × 2 = 8/5 | **1** | 3/5 |

Le reste fractionnaire 0,2 est revenu, donc la suite se répète : \(0{,}1 = (0{,}0\,\overline{0011})_2\), avec les quatre chiffres \(0011\) qui se répètent à l'infini. Les 16 premiers chiffres sont 0001100110011001.

## II. Troncature, arrondi, erreur

Quand l'écriture est infinie ou trop longue, on garde \(p\) chiffres après la virgule :

- **troncature** : on supprime les chiffres suivants ;
- **arrondi** : on choisit la valeur à \(p\) chiffres la plus proche.

L'**erreur** est la distance entre la valeur exacte et la valeur retenue. En base 2 avec \(p\) chiffres après la virgule : l'erreur d'une **troncature** est strictement inférieure à \(2^{-p}\) ; celle d'un **arrondi** est au plus \(2^{-(p+1)}\).

**Exemple.** On tronque \(0{,}1\) à 8 chiffres binaires : \((0,00011001)_2 = \dfrac{25}{256} = 0,09765625\). L'erreur vaut \(0{,}1 - 0,09765625 = 0,00234375\), qui est bien inférieure à \(2^{-8} = 0,00390625\).

## III. Les nombres « à virgule » dans un ordinateur

Un `float` Python est un nombre binaire **à précision finie** (53 chiffres binaires significatifs). La plupart des décimaux ne sont donc que des **valeurs approchées** :

```python
>>> 0.1 + 0.2
0.30000000000000004
>>> 0.1 + 0.2 == 0.3
False
```

> [!WARNING]
> **Ne jamais tester l'égalité de deux `float` avec `==`.** On teste que l'écart est petit : `abs(a - b) < 1e-9`, ou `math.isclose(a, b)`. Pour calculer exactement avec des fractions, on utilise `fractions.Fraction`.

Les entiers Python (`int`) n'ont pas de limite de taille. Dans beaucoup d'autres langages et dans les circuits, un entier est codé sur un **nombre fixe de bits** : on parle alors de **débordement** quand le résultat dépasse la capacité (§ V).

## IV. Calculer en binaire

### Addition

On additionne colonne par colonne en propageant la retenue :

| Somme | Résultat |
|---|---|
| \(0 + 0\) | 0 |
| \(0 + 1\) | 1 |
| \(1 + 1\) | 10 (on pose 0, **retenue 1**) |
| \(1 + 1 + 1\) | 11 (on pose 1, **retenue 1**) |

**Exemple.** \((1011)_2 + (0111)_2\) :

```text
  retenues : 1 1 1
             1 0 1 1      (11)
           + 0 1 1 1      ( 7)
           ---------
           1 0 0 1 0      (18)
```

Contrôle : \(11 + 7 = 18 = (10010)_2\).

### Soustraction

On soustrait colonne par colonne avec **emprunt**. Contrôle toujours par l'addition : \((10110)_2 - (1101)_2 = (1001)_2\), car \(10110 = 1101 + 1001\) (22 = 13 + 9).

### Multiplication

Multiplier par un chiffre binaire, c'est recopier (×1) ou écrire 0 (×0), avec un décalage à chaque rang, puis additionner.

**Exemple.** \((1101)_2 \times (101)_2\) (13 × 5) :

```text
      1 1 0 1
    ×   1 0 1
    ---------
      1 1 0 1      (× 1)
    0 0 0 0        (× 0, décalé d'un rang)
  1 1 0 1          (× 1, décalé de deux rangs)
  ---------------
  1 0 0 0 0 0 1    (65)
```

Contrôle : \(13 \times 5 = 65 = (1000001)_2\).

### Multiplier et diviser par une puissance de 2 : décaler

- **Multiplier par \(2^k\)** : ajouter \(k\) zéros à droite (décalage de \(k\) rangs vers la gauche). \((11001)_2 \times 2^3 = (11001000)_2\), soit \(25 \times 8 = 200\).
- **Division euclidienne par \(2^k\)** : supprimer les \(k\) derniers chiffres : ce qui reste est le **quotient** et les \(k\) chiffres supprimés forment le **reste**. \((11001)_2 = 25\) divisé par \(4 = 2^2\) : quotient \((110)_2 = 6\), reste \((01)_2 = 1\), car \(25 = 4 \times 6 + 1\).

En Python, `x << k` multiplie par \(2^k\), `x >> k` donne le quotient de la division par \(2^k\) et `x & (2**k - 1)` donne le reste.

## V. Capacité limitée et débordement

Sur \(n\) bits, un entier naturel est compris entre 0 et \(2^n - 1\). Si le résultat d'une addition dépasse \(2^n - 1\), le bit de retenue en trop est **perdu** : le résultat obtenu est le reste de la division par \(2^n\).

**Exemple (8 bits).** \(200 + 100 = 300\) dépasse \(255\). Le circuit conserve \(300 - 256 = 44\), c'est-à-dire \((00101100)_2\).

### Pour aller plus loin : les entiers relatifs (complément à deux)

Pour représenter des entiers **relatifs** sur \(n\) bits, on utilise le **complément à deux** : un nombre négatif \(-x\) est codé par l'entier naturel \(2^n - x\). Sur 8 bits, on représente les entiers de \(-128\) à \(127\).

**Exemple.** \(-5\) sur 8 bits : \(256 - 5 = 251 = (11111011)_2\). Même résultat avec la règle pratique : on écrit 5 = \(00000101\), on **inverse tous les bits** (\(11111010\)), puis on **ajoute 1** (\(11111011\)). Le premier bit vaut 1 pour un nombre négatif.

> [!NOTE]
> Cette sous-section prolonge le cours (entiers relatifs) ; elle n'est pas nécessaire pour la suite.

## VI. Unités : bits, octets et préfixes

Un **octet** (o) vaut 8 **bits** (b). Les tailles de données se donnent en octets, les **débits** en bits par seconde.

| Préfixe décimal (SI) | Valeur | Préfixe binaire (CEI) | Valeur |
|---|---|---|---|
| ko (kilooctet) | \(10^3\) o | Kio (kibioctet) | \(2^{10} = 1024\) o |
| Mo (mégaoctet) | \(10^6\) o | Mio (mébioctet) | \(2^{20} = 1 048 576\) o |
| Go (gigaoctet) | \(10^9\) o | Gio (gibioctet) | \(2^{30} = 1 073 741 824\) o |
| To (téraoctet) | \(10^{12}\) o | Tio (tébioctet) | \(2^{40} = 1 099 511 627 776\) o |

> [!WARNING]
> **Ne pas confondre Go et Gio.** Un disque annoncé « 500 Go » contient \(500 \times 10^9\) octets, soit \(\dfrac{500 \times 10^9}{2^{30}} \approx 465,66\) Gio : c'est cette dernière valeur que certains systèmes affichent (parfois en l'appelant « Go »).

**Débit et durée.** Un débit de \(100\) Mbit/s correspond à \(\dfrac{100 \times 10^6}{8} = 12,5\) Mo/s. Pour transférer un fichier de \(2\) Go (\(2 \times 10^9\) o) à ce débit, la durée théorique, sans tenir compte des protocoles, est

\[
t = \frac{\text{taille en bits}}{\text{débit en bit/s}} = \frac{2 \times 10^9 \times 8}{100 \times 10^6} = 160 \text{ s}.
\]

## À retenir

- Après la virgule, les poids sont \(2^{-1}, 2^{-2}, \dots\) ; on convertit la partie fractionnaire en la **multipliant par 2** à répétition.
- Un nombre est exact en binaire si et seulement s'il s'écrit \(\dfrac{k}{2^m}\) : 0,1 ne l'est pas, d'où \(0{,}1 + 0{,}2 \ne 0{,}3\) en `float`.
- Troncature à \(p\) chiffres binaires : erreur \(< 2^{-p}\) ; arrondi : erreur \(\le 2^{-(p+1)}\).
- Multiplier ou diviser par \(2^k\) = **décaler** de \(k\) rangs.
- Sur \(n\) bits, on perd la retenue au-delà de \(2^n - 1\) : résultat modulo \(2^n\).
- 1 octet = 8 bits ; ko, Mo, Go (puissances de 10) ≠ Kio, Mio, Gio (puissances de 2).

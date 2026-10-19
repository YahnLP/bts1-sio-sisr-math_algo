---
render_macros: true
---

# TP Python – Précision des nombres flottants et décalages

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S02*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

> [!TIP]
> **Python est nouveau pour toi ?** Reprends la séance [S00 – Introduction à Python](../S00-introduction-python/README.md). Avant chaque exercice, un encadré « Syntaxe utile » rappelle les commandes à employer.

## Exercice A – Pourquoi `0.1 + 0.2 != 0.3`

> [!TIP]
> **Syntaxe utile.** `==` : test d'égalité ; `math.isclose(a, b)` : vrai si `a` et `b` sont presque égaux ; `Fraction(1, 10)` : le rapport exact 1/10 ; `from fractions import Fraction` et `import math` : à écrire en tête du script (c'est déjà fait).

**J'anticipe.** Que vaut, selon toi, `0.1 + 0.2 == 0.3` ? Et `0.5 + 0.25 == 0.75` ? Justifie avec le cours (§ I).

{{ IDE('flottants', MAX="+") }}

**Je comprends.** `Fraction` calcule exactement avec des rapports d'entiers ; `math.isclose` accepte un petit écart. Quelles valeurs sont exactes en binaire parmi celles du script ?

## Exercice B – Les chiffres binaires d'une partie fractionnaire

> [!TIP]
> **Syntaxe utile.** `x * 2` : multiplication ; `int(x)` : partie entière de `x` ; `x - int(x)` : partie fractionnaire ; `for _ in range(p):` : répète `p` fois ; `texte = texte + str(chiffre)` : ajoute un chiffre à droite.

Écris `chiffres_apres_virgule(x, p)` qui renvoie le texte des `p` premiers chiffres binaires de la partie fractionnaire de `x` (`0 <= x < 1`), par multiplications successives par 2.

**J'anticipe.** Pour `x = 0.8125` et `p = 4`, écris les quatre multiplications avant de coder.

{{ IDE('chiffres_apres_virgule', MAX="+") }}

## Exercice C – Additionner deux nombres binaires « à la main »

> [!TIP]
> **Syntaxe utile.** `a.zfill(n)` : complète à gauche par des 0 jusqu'à `n` caractères ; `a[i]` : caractère de position `i` ; `int(a[i])` : ce caractère en nombre ; `range(n - 1, -1, -1)` : `i` vaut `n - 1`, `n - 2`, ..., 0 (de droite à gauche) ; `total % 2` et `total // 2` : reste et quotient ; `str(c)` : nombre vers texte.

Écris `addition_binaire(a, b)` qui reçoit deux **textes** binaires et renvoie leur somme en texte binaire, **sans** convertir en entier : tu additionnes de droite à gauche en gérant la retenue.

{{ IDE('addition_binaire', MAX="+") }}

## Exercice D – Débordement sur \(n\) bits

> [!TIP]
> **Syntaxe utile.** `2 ** n` : puissance ; `x % m` : reste de la division de `x` par `m` ; `a + b > 2 ** n - 1` : comparaison, donne `True` ou `False` ; `return (resultat, debordement)` : renvoie deux valeurs.

Écris `addition_n_bits(a, b, n)` qui renvoie le couple `(résultat, débordement)` : le résultat tient sur `n` bits (reste modulo \(2^n\)) et `débordement` vaut `True` si la somme exacte dépasse \(2^n - 1\).

{{ IDE('addition_n_bits', MAX="+") }}

## Exercice E – Durée d'un transfert

> [!TIP]
> **Syntaxe utile.** `taille * 8` : produit (un octet = 8 bits) ; `a / b` : division décimale ; `return` : renvoie le résultat ; 1 Mbit/s = `10 ** 6` bits par seconde (voir le cours, § VI).

Écris `duree_transfert(taille_octets, debit_bits_par_s)` qui renvoie la durée théorique en secondes.

{{ IDE('duree_transfert', MAX="+") }}

**Je comprends.** Calcule la durée pour 2 Go à 100 Mbit/s, puis à 1 Gbit/s, et compare avec le cours (§ VI).

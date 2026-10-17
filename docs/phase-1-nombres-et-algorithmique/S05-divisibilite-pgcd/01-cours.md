# Cours – Divisibilité, division euclidienne et PGCD

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S05 – à lire avant les [exercices](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** S01 ; S04 (boucle tant que).
> - **Outils :** Papier, calculatrice, éditeur Python intégré au site

## À la fin de ce cours tu sauras

- [ ] **Effectuer** une division euclidienne et **énoncer** son résultat \(a = bq + r\) avec \(0 \le r < b\) ;
- [ ] **Utiliser** les critères de divisibilité (2, 3, 5, 9, 10) ;
- [ ] **Déterminer** les diviseurs et les multiples d'un entier ;
- [ ] **Calculer** un PGCD par l'algorithme d'Euclide et **justifier** que l'algorithme s'arrête ;
- [ ] **Reconnaître** deux entiers premiers entre eux et **calculer** un PPCM.

## I. Diviseurs et multiples

Soient \(a\) et \(b\) deux entiers relatifs. On dit que \(a\) **divise** \(b\), et on note \(a \mid b\), s'il existe un entier \(k\) tel que \(b = a \times k\). On dit aussi que \(b\) est un **multiple** de \(a\), ou que \(b\) est **divisible** par \(a\).

**Exemples.** \(7 \mid 84\) car \(84 = 7 \times 12\) ; \(5 \nmid 84\). Tout entier divise 0 (\(0 = a \times 0\)) ; 1 divise tout entier ; \(0\) ne divise que \(0\).

**Propriétés** (si \(a \mid b\) et \(a \mid c\)) :

- \(a \mid (b + c)\) et \(a \mid (b - c)\) ;
- \(a \mid (b \times m)\) pour tout entier \(m\) ;
- si de plus \(b \mid d\), alors \(a \mid d\) (transitivité).

*Justification de la première.* Si \(b = a k\) et \(c = a k'\), alors \(b + c = a (k + k')\) avec \(k + k'\) entier.

## II. La division euclidienne

**Théorème.** Soient \(a\) un entier et \(b\) un entier **strictement positif**. Il existe un **unique** couple d'entiers \((q, r)\) tel que

\[
a = b \times q + r \qquad \text{avec} \qquad 0 \le r < b .
\]

\(q\) est le **quotient** et \(r\) le **reste**. De plus, \(b \mid a\) si et seulement si \(r = 0\).

**Exemples.**

- 100 = 7 × 14 + 2 : quotient 14, reste 2.
- 7 = 100 × 0 + 7 : si \(a < b\), le quotient est 0 et le reste est \(a\).
- -23 = 6 × -4 + 1 : pour \(a\) négatif, le reste reste **positif** (\(-23 = 6 \times (-4) + 1\) et non \(6 \times (-3) - 5\)). C'est ce que calculent `//` et `%` en Python pour \(b > 0\).

*Pourquoi \(q\) et \(r\) existent et sont uniques ?* Pour \(a \ge 0\), on retranche \(b\) autant de fois que possible : on s'arrête au premier reste inférieur à \(b\). Si \(bq + r = bq' + r'\) avec des restes entre \(0\) et \(b-1\), alors \(b(q - q') = r' - r\) est un multiple de \(b\) strictement compris entre \(-b\) et \(b\), donc nul : \(q = q'\) et \(r = r'\).

## III. Critères de divisibilité

Un entier \(n\) est divisible :

| par | si… |
|---|---|
| 2 | son dernier chiffre est pair (0, 2, 4, 6, 8) |
| 5 | son dernier chiffre est 0 ou 5 |
| 10 | son dernier chiffre est 0 |
| 4 | le nombre formé par ses deux derniers chiffres est divisible par 4 |
| 3 | la somme de ses chiffres est divisible par 3 |
| 9 | la somme de ses chiffres est divisible par 9 |

*Pourquoi 3 et 9 ?* Écrivons \(n = a_k 10^k + \dots + a_1 10 + a_0\). Or \(10^j - 1 = 99\dots9\) est un multiple de 9 (donc de 3). Ainsi \(n = (a_k + \dots + a_0) + 9m\) pour un entier \(m\) : \(n\) et la somme de ses chiffres ont le **même reste** dans la division par 9 (et par 3).

| \(n\) | par 2 | par 3 | par 4 | par 5 | par 9 | par 10 | Somme des chiffres |
|---|---|---|---|---|---|---|---|
| 4 536 | oui | oui | oui | non | oui | non | 18 |
| 1 990 | oui | non | non | oui | non | oui | 19 |
| 2 024 | oui | non | oui | non | non | non | 8 |

## IV. Diviseurs d'un entier

Pour trouver tous les diviseurs d'un entier \(n \ge 1\), on teste les entiers de 1 à \(n\). Les diviseurs vont **par paires** \((d, n/d)\) : il suffit de tester jusqu'à \(\sqrt{n}\) (S06).

**Exemple.** Les diviseurs de 84 sont 1, 2, 3, 4, 6, 7, 12, 14, 21, 28, 42, 84 ; ceux de 90 sont 1, 2, 3, 5, 6, 9, 10, 15, 18, 30, 45, 90. Leurs diviseurs communs sont 1, 2, 3, 6 : le plus grand est 6.

## V. Le PGCD

Le **PGCD** (plus grand commun diviseur) de deux entiers \(a\) et \(b\) non tous deux nuls est le plus grand entier qui divise à la fois \(a\) et \(b\). On le note \(\operatorname{PGCD}(a, b)\). Deux entiers sont **premiers entre eux** si leur PGCD vaut 1.

### L'algorithme d'Euclide

**Propriété.** Si \(a = bq + r\) (division euclidienne), alors

\[
\operatorname{PGCD}(a, b) = \operatorname{PGCD}(b, r) .
\]

*Justification.* Si \(d\) divise \(a\) et \(b\), alors \(d\) divise \(r = a - bq\). Réciproquement, si \(d\) divise \(b\) et \(r\), alors \(d\) divise \(a = bq + r\). Les couples \((a, b)\) et \((b, r)\) ont donc **exactement les mêmes diviseurs communs**, donc le même plus grand.

On répète la division jusqu'à obtenir un reste nul : le **dernier reste non nul** est le PGCD.

**Exemple.** \(\operatorname{PGCD}(252, 198)\) :

| Étape | Division euclidienne |
|---|---|
| 1 | 252 = 198 × 1 + 54 |
| 2 | 198 = 54 × 3 + 36 |
| 3 | 54 = 36 × 1 + 18 |
| 4 | 36 = 18 × 2 + 0 |

Le dernier reste non nul est 18 : \(\operatorname{PGCD}(252, 198) = 18\). Contrôle : \(252 = 18 \times 14\) et \(198 = 18 \times 11\), et ces deux quotients (14 et 11) sont premiers entre eux.

**Exemple.** \(\operatorname{PGCD}(1\,071, 462)\) :

| Étape | Division euclidienne |
|---|---|
| 1 | 1071 = 462 × 2 + 147 |
| 2 | 462 = 147 × 3 + 21 |
| 3 | 147 = 21 × 7 + 0 |

D'où \(\operatorname{PGCD}(1\,071, 462) = 21\).

**Pourquoi l'algorithme s'arrête.** Les restes successifs forment une suite d'entiers **strictement décroissante** et positive ou nulle : c'est le variant. Elle atteint donc 0 en un nombre fini d'étapes.

```text
ALGORITHME pgcd
  RÔLE      : calculer le PGCD de deux entiers naturels (non tous deux nuls)
  ENTRÉES   : a, b (entiers naturels)
  SORTIE    : le PGCD de a et b
  VARIABLES : reste (entier)
DÉBUT
  TANT QUE b ≠ 0 FAIRE
    reste ← a mod b
    a ← b
    b ← reste
  FIN TANT QUE
  RETOURNER a
FIN
```

Le cas \(b = 0\) donne directement \(\operatorname{PGCD}(a, 0) = a\).

## VI. Le PPCM

Le **PPCM** (plus petit commun multiple) de deux entiers non nuls est le plus petit multiple strictement positif commun aux deux. On a la relation (démontrée avec la décomposition en facteurs premiers, S06)

\[
\operatorname{PGCD}(a, b) \times \operatorname{PPCM}(a, b) = a \times b \quad \text{pour } a, b \ge 1 .
\]

**Exemple.** \(\operatorname{PGCD}(12, 18) = 6\) donc \(\operatorname{PPCM}(12, 18) = \dfrac{12 \times 18}{6} = 36\).

## VII. Applications

- **Découper en blocs identiques.** Un écran de \(1\,920 \times 1\,080\) pixels se découpe en carrés identiques sans reste ; le plus grand carré a pour côté \(\operatorname{PGCD}(1\,920, 1\,080) = 120\) pixels, soit 16 carrés en largeur et 9 en hauteur (le rapport 16 : 9).
- **Tâches périodiques.** Une sauvegarde toutes les 6 heures et une vérification toutes les 8 heures démarrent ensemble ; elles coïncident de nouveau après \(\operatorname{PPCM}(6, 8) = 24\) heures.
- **Simplifier un rapport** (débit, ratio) : on divise numérateur et dénominateur par leur PGCD.

## À retenir

- \(a \mid b\) ⟺ \(b = ak\) ; \(b \mid a\) ⟺ le reste de la division de \(a\) par \(b\) est 0.
- Division euclidienne : \(a = bq + r\), \(0 \le r < b\), \(q\) et \(r\) **uniques**.
- Critères : 2, 5, 10 (dernier chiffre) ; 3 et 9 (somme des chiffres) ; 4 (deux derniers chiffres).
- \(\operatorname{PGCD}(a, b) = \operatorname{PGCD}(b, r)\) : on répète jusqu'à un reste nul ; le PGCD est le dernier reste non nul.
- Premiers entre eux : \(\operatorname{PGCD} = 1\). \(\operatorname{PGCD} \times \operatorname{PPCM} = a \times b\).

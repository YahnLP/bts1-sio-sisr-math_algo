# Cours – Algèbre de Boole et simplification

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S10 – à lire avant les [exercices](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** S08, S09 (connecteurs, ensembles) ; S03 (opérateurs bit à bit).
> - **Outils :** Papier, calculatrice, éditeur Python intégré au site

## À la fin de ce cours tu sauras

- [ ] **Énoncer** les propriétés de l'algèbre de Boole (commutativité, associativité, distributivité, idempotence, absorption, complément, lois de De Morgan) ;
- [ ] **Simplifier** une expression à trois variables au plus, par calcul algébrique ou par tableau de Karnaugh ;
- [ ] **Écrire** une expression à partir d'une table de vérité (somme de produits) ;
- [ ] **Exprimer** les opérations ET, OU, NON, OU exclusif à l'aide de NAND ou NOR ;
- [ ] **Appliquer** le ET bit à bit pour calculer une adresse réseau à partir d'une adresse IPv4 et d'un masque.

## I. Variables et opérations booléennes

Une **variable booléenne** ne prend que deux valeurs, **0** et **1**. On retrouve les connecteurs de la logique (S08) avec une écriture d'algèbre :

| Opération | Notation | Logique (S08) | Python | Ensembles (S09) |
|---|---|---|---|---|
| **NON** (complément) | \(\overline{a}\) | \(\neg a\) | `1 - a` ou `not a` | \(\overline{A}\) |
| **ET** (produit) | \(a \cdot b\) | \(a \wedge b\) | `a & b` | \(A \cap B\) |
| **OU** (somme) | \(a + b\) | \(a \vee b\) | `a | b` | \(A \cup B\) |
| **OU exclusif** | \(a \oplus b\) | \(a \oplus b\) | `a ^ b` | \(A \,\Delta\, B\) |

> [!WARNING]
> Le signe « \(+\) » est le **OU** : en algèbre de Boole, \(1 + 1 = 1\) (et non 2). Le « \(\cdot\) » est le ET. La priorité est celle des nombres : le NON d'abord, puis le ET, puis le OU. Ainsi \(a + b \cdot c\) signifie \(a + (b \cdot c)\).

Tables à connaître :

| \(a\) | \(b\) | \(\overline{a}\) | \(a \cdot b\) | \(a + b\) | \(a \oplus b\) |
|---|---|---|---|---|---|
| 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 | 1 | 0 |

## II. Les propriétés

Chacune de ces propriétés a été vérifiée sur toutes les valeurs possibles de \(a\), \(b\), \(c\) (il n'y en a que 8 au plus).

| Propriété | Forme « somme » | Forme « produit » |
|---|---|---|
| **Commutativité** | \(a + b = b + a\) | \(a \cdot b = b \cdot a\) |
| **Associativité** | \((a + b) + c = a + (b + c)\) | \((a \cdot b) \cdot c = a \cdot (b \cdot c)\) |
| **Distributivité** | \(a \cdot (b + c) = a \cdot b + a \cdot c\) | \(a + b \cdot c = (a + b) \cdot (a + c)\) |
| **Élément neutre** | \(a + 0 = a\) | \(a \cdot 1 = a\) |
| **Élément absorbant** | \(a + 1 = 1\) | \(a \cdot 0 = 0\) |
| **Idempotence** | \(a + a = a\) | \(a \cdot a = a\) |
| **Complément** | \(a + \overline{a} = 1\) | \(a \cdot \overline{a} = 0\) |
| **Involution** | \(\overline{\overline{a}} = a\) | |
| **Absorption** | \(a + a \cdot b = a\) | \(a \cdot (a + b) = a\) |
| **De Morgan** | \(\overline{a + b} = \overline{a} \cdot \overline{b}\) | \(\overline{a \cdot b} = \overline{a} + \overline{b}\) |

La **distributivité du OU sur le ET** (\(a + b \cdot c = (a + b)(a + c)\)) n'a pas d'équivalent en arithmétique ordinaire : c'est une particularité de l'algèbre de Boole.

> [!NOTE]
> **Principe de dualité.** Si l'on échange partout \(+\) et \(\cdot\), et \(0\) et \(1\), une propriété vraie reste vraie. Les deux colonnes du tableau se correspondent ainsi.

### Les lois de De Morgan

\[
\overline{a + b} = \overline{a} \cdot \overline{b} \qquad\qquad \overline{a \cdot b} = \overline{a} + \overline{b}
\]

Pour **nier** une expression : on remplace chaque \(+\) par \(\cdot\), chaque \(\cdot\) par \(+\), et on complémente chaque variable.

**Exemple.** \(\overline{(a + \overline{b}) \cdot c} = \overline{a + \overline{b}} + \overline{c} = \overline{a} \cdot b + \overline{c}\).

| \(a\) | \(b\) | \(c\) | \((a + \overline{b}) \cdot c\) | \(\overline{(a + \overline{b}) \cdot c}\) | \(\overline{a} \cdot b + \overline{c}\) |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 | 1 |
| 0 | 0 | 1 | 1 | 0 | 0 |
| 0 | 1 | 0 | 0 | 1 | 1 |
| 0 | 1 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 0 | 1 | 1 |
| 1 | 0 | 1 | 1 | 0 | 0 |
| 1 | 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 | 0 |

Les deux dernières colonnes sont identiques : le calcul est confirmé.

## III. Écrire une expression à partir d'une table

Une table de vérité définit une fonction \(f\). On l'écrit comme une **somme de produits** : pour chaque ligne où \(f = 1\), on écrit le produit des variables (complémentées si elles valent 0 sur cette ligne). On additionne ces produits (les **mintermes**).

**Exemple.** Fonction à trois variables :

| \(a\) | \(b\) | \(c\) | \(f\) |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 |

Les lignes où \(f = 1\) sont les numéros 1, 3, 6, 7 (en lisant \(abc\) comme un nombre binaire : 001, 011, 110, 111). Donc :

\[
f = \overline{a}\,\overline{b}\,c + \overline{a}\,b\,c + a\,b\,\overline{c} + a\,b\,c
\]

Cette forme est exacte, mais longue : on la **simplifie**.

## IV. Simplifier par le calcul

On utilise l'**absorption**, la **distributivité** et le **complément**.

\[
\begin{aligned}
f &= \overline{a}\,c\,(\overline{b} + b) + a\,b\,(\overline{c} + c) \\
  &= \overline{a}\,c \cdot 1 + a\,b \cdot 1 \\
  &= \overline{a}\,c + a\,b
\end{aligned}
\]

Contrôle sur la table : \(\overline{a}\,c + a\,b\) vaut 1 pour les lignes 1, 3, 6, 7, comme \(f\). Deux produits au lieu de quatre, et deux variables par produit au lieu de trois.

### Autres simplifications fréquentes

| Expression | Simplification | Propriété utilisée |
|---|---|---|
| \(a\,b + a\,\overline{b}\) | \(a\) | distributivité, complément |
| \(a + \overline{a}\,b\) | \(a + b\) | distributivité du OU sur le ET |
| \(a\,b + \overline{a}\,c + b\,c\) | \(a\,b + \overline{a}\,c\) | consensus |
| \(a\,\overline{b} + a\,b\,c\) | \(a\,\overline{b} + a\,c\) | distributivité, \(\overline{b} + b\,c = \overline{b} + c\) |

Chaque ligne a été vérifiée sur les 8 combinaisons possibles.

## V. Simplifier avec un tableau de Karnaugh

Le **tableau de Karnaugh** range la table de vérité dans une grille où deux cases **voisines** ne diffèrent que d'**une** variable. Pour trois variables : les lignes sont les valeurs de \(a\), les colonnes les valeurs de \(bc\) dans l'ordre **00, 01, 11, 10** (code de Gray : un seul bit change d'une colonne à la suivante, y compris de la dernière à la première).

La fonction \(f = \overline{a}\,c + a\,b\) de la partie III :

| \(a \backslash bc\) | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| **0** | 0 | 1 | 1 | 0 |
| **1** | 0 | 0 | 1 | 1 |

**Règles de regroupement.**

1. On regroupe les 1 en **rectangles** dont le nombre de cases est une **puissance de 2** (1, 2, 4, 8).
2. Les rectangles peuvent se **chevaucher** et sont « circulaires » (la colonne 10 est voisine de la colonne 00).
3. On prend **le moins de rectangles possible**, les plus grands possible, jusqu'à couvrir tous les 1.
4. Chaque rectangle donne un produit : on garde les variables qui **ne changent pas** dans le rectangle.

Ici : le rectangle \(\{011, 001\}\) (colonnes 01 et 11 de la ligne \(a = 0\)) garde \(\overline{a}\) et \(c\) : \(\overline{a}\,c\). Le rectangle \(\{110, 111\}\) (colonnes 11 et 10 de la ligne \(a = 1\)) garde \(a\) et \(b\) : \(a\,b\).

**Autre exemple.** \(g = \overline{b} + a\,c\) :

| \(a \backslash bc\) | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| **0** | 1 | 1 | 0 | 0 |
| **1** | 1 | 1 | 1 | 0 |

Les quatre 1 des colonnes 00 et 01 forment un rectangle de 4 cases : il garde \(\overline{b}\). Le 1 restant (ligne 1, colonne 11) se regroupe avec le 1 de la colonne 01 de la même ligne : \(a\,c\). On a bien \(g = \overline{b} + a\,c\).

**Majorité** (vraie quand au moins deux des trois entrées valent 1) :

| \(a \backslash bc\) | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| **0** | 0 | 0 | 1 | 0 |
| **1** | 0 | 1 | 1 | 1 |

Trois rectangles de 2 cases : \(a\,b + a\,c + b\,c\). Aucun regroupement plus grand n'est possible.

## VI. NAND et NOR

| Porte | Définition | Table |
|---|---|---|
| **NAND** | \(\overline{a \cdot b}\) | 0 seulement si \(a = b = 1\) |
| **NOR** | \(\overline{a + b}\) | 1 seulement si \(a = b = 0\) |

| \(a\) | \(b\) | \(\text{NAND}\) | \(\text{NOR}\) |
|---|---|---|---|
| 0 | 0 | 1 | 1 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |

Chacune de ces portes suffit **seule** à réaliser toutes les autres : on dit qu'elles sont **universelles**.

| Opération | Avec des NAND | Avec des NOR |
|---|---|---|
| \(\overline{a}\) | \(\text{NAND}(a, a)\) | \(\text{NOR}(a, a)\) |
| \(a \cdot b\) | \(\text{NAND}(\text{NAND}(a,b), \text{NAND}(a,b))\) | \(\text{NOR}(\text{NOR}(a,a), \text{NOR}(b,b))\) |
| \(a + b\) | \(\text{NAND}(\text{NAND}(a,a), \text{NAND}(b,b))\) | \(\text{NOR}(\text{NOR}(a,b), \text{NOR}(a,b))\) |

Ces six égalités ont été vérifiées sur toutes les entrées. Pourquoi cela marche : \(\text{NAND}(a, a) = \overline{a \cdot a} = \overline{a}\), puis les lois de De Morgan donnent le reste.

## VII. Application : additionner en binaire avec des portes

Pour additionner deux bits \(a\) et \(b\), on cherche la **somme** \(s\) et la **retenue** \(r\) :

| \(a\) | \(b\) | \(s = a \oplus b\) | \(r = a \cdot b\) |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

C'est le **demi-additionneur** : \(1 + 1 = 10_2\) donne \(s = 0\) et \(r = 1\). Pour additionner des nombres de plusieurs bits (S02), chaque rang doit aussi tenir compte de la retenue \(c\) du rang précédent : c'est l'**additionneur complet**.

| \(a\) | \(b\) | \(c\) | \(s = a \oplus b \oplus c\) | \(r = a b + c(a \oplus b)\) |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

On vérifie sur chaque ligne que \(a + b + c = s + 2\,r\) (en nombres ordinaires). Enchaînés, \(n\) additionneurs complets additionnent deux nombres de \(n\) bits.

## VIII. Application : le ET bit à bit et les masques

Un nombre entier est une suite de bits. Le **ET bit à bit** (`&`, S03) applique le ET à chaque rang. Un **masque** sert à **garder** certains bits (là où il vaut 1) et à mettre les autres à 0.

| | Valeur |
|---|---|
| Adresse IPv4 | `192.168.10.77` = `11000000.10101000.00001010.01001101` |
| Masque `255.255.255.192` (/26) | `11111111.11111111.11111111.11000000` |
| **Adresse réseau** (ET) | `11000000.10101000.00001010.01000000` = `192.168.10.64` |

Seul le dernier octet change : \(77 = 01001101_2\) et \(192 = 11000000_2\), donc \(77 \,\&\, 192 = 01000000_2 = 64\).

La suite (diffusion, nombre de machines, découpage en sous-réseaux) est détaillée dans l'[annexe sur l'adressage](annexe-adressage.md).

## À retenir

- Algèbre de Boole : ET (\(\cdot\)), OU (\(+\)), NON (barre). \(1 + 1 = 1\).
- Propriétés : commutativité, associativité, distributivité (**dans les deux sens**), idempotence, complément, **absorption**, **De Morgan**.
- Une table de vérité s'écrit en **somme de produits** ; on simplifie par le calcul ou par un **tableau de Karnaugh** (à trois variables : rectangles de 1, 2, 4 ou 8 cases ; colonnes en ordre 00, 01, 11, 10).
- **NAND** et **NOR** sont universelles.
- Demi-additionneur : \(s = a \oplus b\), \(r = a \cdot b\).
- Un **masque** se combine à une adresse par ET bit à bit.

# Exercices – Simplifier des expressions booléennes

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S10*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**, avec la méthode du cours : écris les étapes, pas seulement le résultat. Ouvre ensuite « Voir la réponse » pour te corriger. À l'épreuve, **aucune réponse sans justification** n'est complète.

## Exercice 1 – Simplifier par le calcul

Simplifier, en indiquant la propriété utilisée à chaque étape :

(a) \(a + a\,b\) ; (b) \(a\,b + a\,\overline{b}\) ; (c) \((a + b)(a + \overline{b})\) ; (d) \(a\,\overline{b} + a\,b\,c\) ; (e) \(\overline{a\,b}\,(a + b)\).

<details markdown="1">
<summary>Voir la réponse</summary>

(a) \(a + a\,b = a\,(1 + b) = a\) (absorption).
(b) \(a\,b + a\,\overline{b} = a\,(b + \overline{b}) = a\).
(c) \((a + b)(a + \overline{b}) = a + b\,\overline{b} = a + 0 = a\) (distributivité du OU sur le ET).
(d) \(a\,\overline{b} + a\,b\,c = a\,(\overline{b} + b\,c) = a\,(\overline{b} + c) = a\,\overline{b} + a\,c\).
(e) \(\overline{a\,b}\,(a + b) = (\overline{a} + \overline{b})(a + b) = \overline{a}\,b + a\,\overline{b} = a \oplus b\) (De Morgan, puis \(a\,\overline{a} = 0\)).

Chaque résultat a été confirmé par comparaison des tables de vérité.

</details>

## Exercice 2 – Nier une expression

Écrire la négation, sans parenthèse barrée sur plus d'une variable : (a) \(a\,b + \overline{c}\) ; (b) \((a + \overline{b})\,c\) ; (c) \(\overline{a}\,b\,c + a\,\overline{c}\).

<details markdown="1">
<summary>Voir la réponse</summary>

(a) \(\overline{a\,b + \overline{c}} = \overline{a\,b} \cdot c = (\overline{a} + \overline{b})\,c\).
(b) \(\overline{a}\,b + \overline{c}\).
(c) \(\overline{\overline{a}\,b\,c} \cdot \overline{a\,\overline{c}} = (a + \overline{b} + \overline{c})(\overline{a} + c)\).

On vérifie (c) par la table :

| \(a\) | \(b\) | \(c\) | \(\overline{\overline{a}\,b\,c + a\,\overline{c}}\) | \((a + \overline{b} + \overline{c})(\overline{a} + c)\) |
|---|---|---|---|---|
| 0 | 0 | 0 | 1 | 1 |
| 0 | 0 | 1 | 1 | 1 |
| 0 | 1 | 0 | 1 | 1 |
| 0 | 1 | 1 | 0 | 0 |
| 1 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 | 1 |
| 1 | 1 | 0 | 0 | 0 |
| 1 | 1 | 1 | 1 | 1 |

</details>

## Exercice 3 – De la table à l'expression

| \(a\) | \(b\) | \(c\) | \(f\) |
|---|---|---|---|
| 0 | 0 | 0 | 1 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 |

1. Écrire \(f\) en somme de produits (mintermes).
2. Remplir un tableau de Karnaugh et en déduire une expression simplifiée.

<details markdown="1">
<summary>Voir la réponse</summary>

1. Les lignes à 1 sont 0, 1, 4, 5, 7 : \(f = \overline{a}\,\overline{b}\,\overline{c} + \overline{a}\,\overline{b}\,c + a\,\overline{b}\,\overline{c} + a\,\overline{b}\,c + a\,b\,c\).
2. Tableau de Karnaugh :

| \(a \backslash bc\) | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| **0** | 1 | 1 | 0 | 0 |
| **1** | 1 | 1 | 1 | 0 |

   Rectangle de 4 cases (colonnes 00 et 01) : \(\overline{b}\). Rectangle de 2 cases (ligne 1, colonnes 01 et 11) : \(a\,c\). Donc \(f = \overline{b} + a\,c\).

</details>

## Exercice 4 – Karnaugh

Simplifier avec un tableau de Karnaugh la fonction \(g\) à trois variables qui vaut 1 pour les lignes 0, 2, 3, 6, 7 (numéros en binaire \(abc\)).

<details markdown="1">
<summary>Voir la réponse</summary>

| \(a \backslash bc\) | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| **0** | 1 | 0 | 1 | 1 |
| **1** | 0 | 0 | 1 | 1 |

Rectangle de 4 cases (colonnes 11 et 10) : \(b\). Rectangle de 2 cases (colonnes 00 et 10 de la ligne 0 : la colonne 10 est voisine de la colonne 00 dans ce tableau circulaire) : \(\overline{a}\,\overline{c}\). Donc \(g = b + \overline{a}\,\overline{c}\).

</details>

## Exercice 5 – Une alarme à majorité

Une salle est protégée par trois capteurs \(a\), \(b\), \(c\). L'alarme se déclenche quand **au moins deux** capteurs détectent quelque chose.

1. Dresser la table de vérité et écrire l'expression en somme de produits.
2. Simplifier avec Karnaugh. Peut-on faire mieux que trois produits ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. | \(a\) | \(b\) | \(c\) | \(\text{alarme}\) |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 | Lignes à 1 : 3, 5, 6, 7 ; \(\overline{a}\,b\,c + a\,\overline{b}\,c + a\,b\,\overline{c} + a\,b\,c\).
2. | \(a \backslash bc\) | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| **0** | 0 | 0 | 1 | 0 |
| **1** | 0 | 1 | 1 | 1 | Trois rectangles de 2 cases : \(a\,b + a\,c + b\,c\). Chaque rectangle est maximal et ils sont tous nécessaires : on ne peut pas faire mieux.

</details>

## Exercice 6 – Portes NAND

1. Dessiner (ou écrire) \(\overline{a}\), \(a \cdot b\), \(a + b\) à l'aide de portes NAND uniquement.
2. Simplifier \(\text{NAND}(a, \text{NAND}(a, b))\).
3. Le OU exclusif s'écrit avec quatre NAND : \(a \oplus b = \text{NAND}\bigl(\text{NAND}(a, n),\ \text{NAND}(b, n)\bigr)\) avec \(n = \text{NAND}(a, b)\). Le vérifier avec une table.

<details markdown="1">
<summary>Voir la réponse</summary>

1. Voir le cours (partie VI).
2. \(\text{NAND}(a, \text{NAND}(a, b)) = \overline{a \cdot \overline{a\,b}} = \overline{a\,(\overline{a} + \overline{b})} = \overline{a\,\overline{b}} = \overline{a} + b\) : c'est l'implication \(a \Rightarrow b\) (S08).
3. | \(a\) | \(b\) | \(n = \text{NAND}(a,b)\) | \(\text{NAND}(a,n)\) | \(\text{NAND}(b,n)\) | \(\text{NAND}(\text{NAND}(a,n),\text{NAND}(b,n))\) | \(a \oplus b\) |
|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 1 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 | 0 | 1 | 1 |
| 1 | 0 | 1 | 0 | 1 | 1 | 1 |
| 1 | 1 | 0 | 1 | 1 | 0 | 0 | Les deux dernières colonnes sont identiques.

</details>

## Exercice 7 – Additionneur

1. Additionner à la main \(1 + 1 + 1\) en binaire. Que valent la somme \(s\) et la retenue \(r\) d'un additionneur complet pour \(a = b = c = 1\) ?
2. Poser l'addition \(0110_2 + 0111_2\) et indiquer, rang par rang, la somme et la retenue.

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(1 + 1 + 1 = 3 = 11_2\), donc \(s = 1\) et \(r = 1\).
2. \(0110_2 = 6\) et \(0111_2 = 7\), somme \(13 = 01101_2\).

| Rang (de droite à gauche) | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| \(a\) | 0 | 1 | 1 | 0 |
| \(b\) | 1 | 1 | 1 | 0 |
| retenue entrante | 0 | 0 | 1 | 1 |
| somme \(s\) | 1 | 0 | 1 | 1 |
| retenue sortante | 0 | 1 | 1 | 0 |

On lit la somme : retenue finale 0, puis les sommes des rangs 3, 2, 1, 0 : \(01101_2\) ✓.

</details>

## Exercice 8 – Adresse réseau

Pour chaque couple adresse / préfixe, donner le masque, l'adresse réseau, l'adresse de diffusion et le nombre de machines adressables (voir l'[annexe](annexe-adressage.md)) : (a) `192.168.10.77/26` ; (b) `172.16.45.200/20` ; (c) `10.4.7.19/21`.

<details markdown="1">
<summary>Voir la réponse</summary>

| Adresse | Masque | Réseau | Diffusion | Machines |
|---|---|---|---|---|
| 192.168.10.77/26 | 255.255.255.192 | 192.168.10.64 | 192.168.10.127 | 62 |
| 172.16.45.200/20 | 255.255.240.0 | 172.16.32.0 | 172.16.47.255 | 4094 |
| 10.4.7.19/21 | 255.255.248.0 | 10.4.0.0 | 10.4.7.255 | 2046 |

</details>


## Je sais faire

Coche honnêtement ; ce que tu ne coches pas se reprend avant la séance suivante.

- [ ] Appliquer De Morgan, l'absorption et la distributivité ;
- [ ] Simplifier avec un tableau de Karnaugh (3 variables) ;
- [ ] Écrire une expression à partir d'une table ;
- [ ] Réaliser NON, ET, OU avec des NAND ;
- [ ] Calculer l'adresse réseau avec un ET bit à bit.

**Ce que je dois reprendre :** ______________________

**Ma question à poser à l'enseignant :** ______________________

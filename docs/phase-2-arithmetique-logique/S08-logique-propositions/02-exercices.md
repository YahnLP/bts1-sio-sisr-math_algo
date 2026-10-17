# Exercices – Tables de vérité et équivalences

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S08*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**, avec la méthode du cours : écris les étapes, pas seulement le résultat. Ouvre ensuite « Voir la réponse » pour te corriger. À l'épreuve, **aucune réponse sans justification** n'est complète.

## Exercice 1 – Propositions ?

Parmi les énoncés suivants, lesquels sont des propositions ? Donner la valeur de vérité de celles qui en sont.

1. « 2 024 est divisible par 8. »
2. « Ferme la porte. »
3. « \(n\) est un nombre premier. »
4. « Tout entier pair supérieur à 2 n'est pas premier. »
5. « Le port 443 est utilisé par HTTPS. »

<details markdown="1">
<summary>Voir la réponse</summary>

1. Proposition, **vraie** : \(2\,024 = 8 \times 253\).
2. Pas une proposition (ordre).
3. Pas une proposition : sa valeur dépend de \(n\) (prédicat).
4. Proposition, **vraie** : un pair supérieur à 2 est divisible par 2 avec un quotient supérieur à 1.
5. Proposition, **vraie** (convention d'usage du protocole HTTPS).

</details>

## Exercice 2 – Tables de vérité

Construire la table de vérité de \((p \Rightarrow q) \wedge (q \Rightarrow p)\) et la comparer à celle de \(p \Leftrightarrow q\).

<details markdown="1">
<summary>Voir la réponse</summary>

| \(p\) | \(q\) | \(p \Rightarrow q\) | \(q \Rightarrow p\) | \((p \Rightarrow q) \wedge (q \Rightarrow p)\) | \(p \Leftrightarrow q\) |
|---|---|---|---|---|---|
| F | F | V | V | V | V |
| F | V | V | F | F | F |
| V | F | F | V | F | F |
| V | V | V | V | V | V |

Les deux dernières colonnes sont identiques.

</details>

## Exercice 3 – Équivalences

Montrer par table de vérité : (a) \(\neg(p \vee q) \equiv \neg p \wedge \neg q\) ; (b) \(p \Rightarrow q \equiv \neg q \Rightarrow \neg p\) ; (c) \(p \Rightarrow q\) n'est **pas** équivalente à \(q \Rightarrow p\).

<details markdown="1">
<summary>Voir la réponse</summary>

(a)

| \(p\) | \(q\) | \(\neg(p \vee q)\) | \(\neg p \wedge \neg q\) |
|---|---|---|---|
| F | F | V | V |
| F | V | F | F |
| V | F | F | F |
| V | V | F | F |

(b)

| \(p\) | \(q\) | \(p \Rightarrow q\) | \(\neg q \Rightarrow \neg p\) |
|---|---|---|---|
| F | F | V | V |
| F | V | V | V |
| V | F | F | F |
| V | V | V | V |

(c)

| \(p\) | \(q\) | \(p \Rightarrow q\) | \(q \Rightarrow p\) |
|---|---|---|---|
| F | F | V | V |
| F | V | V | F |
| V | F | F | V |
| V | V | V | V |

Les colonnes diffèrent pour \((p, q) = (F, V)\) et \((V, F)\).

</details>

## Exercice 4 – Tautologie ?

Les expressions suivantes sont-elles des tautologies ? (a) \(((p \Rightarrow q) \wedge p) \Rightarrow q\) ; (b) \((p \vee q) \Rightarrow p\) ; (c) \(p \vee \neg p\).

<details markdown="1">
<summary>Voir la réponse</summary>

(a) **Tautologie** (modus ponens).

| \(p\) | \(q\) | \(p \Rightarrow q\) | \((p \Rightarrow q) \wedge p\) | \(((p \Rightarrow q) \wedge p) \Rightarrow q\) |
|---|---|---|---|---|
| F | F | V | F | V |
| F | V | V | F | V |
| V | F | F | F | V |
| V | V | V | V | V |

(b) **Pas une tautologie** : pour \(p\) faux et \(q\) vrai, \(p \vee q\) est vrai et \(p\) est faux, donc l'implication est fausse.

(c) **Tautologie** : si \(p\) est vrai le « ou » est vrai, sinon \(\neg p\) est vrai.

</details>

## Exercice 5 – Réciproque et contraposée

On considère : « Si un compte est administrateur, alors il peut installer des logiciels. »

1. Écrire la réciproque, la contraposée et la négation.
2. Laquelle de ces trois propositions a la même valeur de vérité que l'énoncé de départ ?
3. L'énoncé suivant est-il équivalent : « Si un compte ne peut pas installer de logiciels, alors ce n'est pas un administrateur » ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. Réciproque : « si un compte peut installer des logiciels, alors il est administrateur ». Contraposée : « si un compte ne peut pas installer de logiciels, alors il n'est pas administrateur ». Négation : « il existe un compte administrateur qui ne peut pas installer de logiciels » (c'est \(p \wedge \neg q\)).
2. La **contraposée** est équivalente à l'énoncé de départ.
3. Oui, c'est exactement la contraposée.

</details>

## Exercice 6 – Négation de conditions

Écrire la négation de chaque condition en supprimant le « non » devant la parenthèse (De Morgan), puis l'écrire en Python.

1. \(\neg(a > 3 \wedge b \le 5)\)
2. \(\neg(\text{port} = 22 \vee \text{port} = 3389)\)
3. \(\neg(\text{age} \ge 18 \wedge \text{age} < 65)\)

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(a \le 3 \vee b > 5\) ; `a <= 3 or b > 5`.
2. \(\text{port} \ne 22 \wedge \text{port} \ne 3389\) ; `port != 22 and port != 3389`.
3. \(\text{age} < 18 \vee \text{age} \ge 65\) ; `age < 18 or age >= 65`.

On passe de \(\wedge\) à \(\vee\) (et inversement) et on **nie chaque comparaison** : \(>\) devient \(\le\), \(=\) devient \(\ne\), \(\ge\) devient \(<\).

</details>

## Exercice 7 – Règle de pare-feu

La règle est : « autoriser si (protocole TCP et port 80 ou 443) ou protocole ICMP », notée \((t \wedge (a \vee b)) \vee i\). Donner la décision pour chacun des paquets suivants.

| Protocole | Port |
|---|---|
| TCP | 80 |
| TCP | 443 |
| TCP | 22 |
| ICMP | 0 |
| UDP | 53 |
| UDP | 443 |

<details markdown="1">
<summary>Voir la réponse</summary>

| Protocole | Port | \(t\) | \(a \vee b\) | \(i\) | Autorisé ? |
|---|---|---|---|---|---|
| TCP | 80 | V | V | F | **V** |
| TCP | 443 | V | V | F | **V** |
| TCP | 22 | V | F | F | **F** |
| ICMP | 0 | F | F | V | **V** |
| UDP | 53 | F | F | F | **F** |
| UDP | 443 | F | V | F | **F** |

Remarque : (UDP, 443) est refusé, car la règle ne mentionne TCP que pour les ports 80 et 443 (HTTP/3 utilise UDP : une règle plus large serait nécessaire pour l'autoriser).

</details>

## Exercice 8 – Deux règles équivalentes ?

Règle A : « refuser si **non** (source interne **et** port = 22) ». Règle B : « refuser si source externe **ou** port ≠ 22 ». Sont-elles équivalentes ?

<details markdown="1">
<summary>Voir la réponse</summary>

Notons \(s\) : « source interne » et \(w\) : « port = 22 ». Règle A : \(\neg(s \wedge w)\). Règle B : \(\neg s \vee \neg w\). D'après De Morgan, \(\neg(s \wedge w) \equiv \neg s \vee \neg w\) : **les deux règles sont équivalentes**.

| \(s\) | \(w\) | \(\neg(s \wedge w)\) | \(\neg s \vee \neg w\) |
|---|---|---|---|
| F | F | V | V |
| F | V | V | V |
| V | F | V | V |
| V | V | F | F |

</details>

## Exercice 9 – Condition de boucle

```text
i ← 0
TANT QUE i < n ET t[i] ≠ x FAIRE
  i ← i + 1
FIN TANT QUE
```

1. Quand la boucle s'arrête-t-elle ? (utiliser De Morgan)
2. Dérouler pour `t = [4, 8, 15]`, \(n = 3\), \(x = 15\), puis \(x = 7\).
3. Que se passerait-il si on avait écrit `t[i] ≠ x ET i < n` pour \(x = 7\) ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. Elle s'arrête quand \(\neg(i < n \wedge t[i] \ne x) \equiv i \ge n \vee t[i] = x\) : tableau épuisé **ou** valeur trouvée.
2. Pour \(x = 15\) :

| `i` | `i < n` | `t[i] != x` | Condition | Action |
|---|---|---|---|---|
| 0 | V | V | V | i ← i + 1 |
| 1 | V | V | V | i ← i + 1 |
| 2 | V | F | F | arrêt |

   La boucle s'arrête avec \(i = 2\) : `x` est trouvé à l'indice 2. Pour \(x = 7\) :

| `i` | `i < n` | `t[i] != x` | Condition | Action |
|---|---|---|---|---|
| 0 | V | V | V | i ← i + 1 |
| 1 | V | V | V | i ← i + 1 |
| 2 | V | V | V | i ← i + 1 |
| 3 | F | — | F | arrêt |

   La boucle s'arrête avec \(i = 3 = n\) : `x` est absent.
3. Au dernier tour, \(i = 3\) : on évaluerait `t[3]` **avant** de tester `i < n`, c'est un accès hors du tableau (erreur d'indice). L'ordre des conditions est donc essentiel.

</details>

## Exercice 10 – Combien de tables ?

1. Combien de lignes a la table de vérité d'une expression à 4 variables ? à \(n\) variables ?
2. Combien existe-t-il de fonctions différentes de deux variables booléennes ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(2^4 = 16\) lignes ; \(2^n\) lignes.
2. Une fonction de deux variables est définie par sa colonne de résultats, qui a 4 lignes, chacune valant V ou F : \(2^4 = 16\) fonctions possibles (parmi lesquelles \(\wedge\), \(\vee\), \(\Rightarrow\), \(\Leftrightarrow\), \(\oplus\), et leurs négations).

</details>


## Je sais faire

Coche honnêtement ; ce que tu ne coches pas se reprend avant la séance suivante.

- [ ] Construire une table de vérité à 2 ou 3 variables ;
- [ ] Prouver une équivalence par table ;
- [ ] Écrire la négation et la contraposée d'une implication ;
- [ ] Reconnaître une tautologie ;
- [ ] Traduire une règle en expression logique.

**Ce que je dois reprendre :** ______________________

**Ma question à poser à l'enseignant :** ______________________

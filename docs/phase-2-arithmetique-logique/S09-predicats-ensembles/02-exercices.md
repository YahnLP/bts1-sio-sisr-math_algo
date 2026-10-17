# Exercices – Quantificateurs, négations et opérations sur les ensembles

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S09*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**, avec la méthode du cours : écris les étapes, pas seulement le résultat. Ouvre ensuite « Voir la réponse » pour te corriger. À l'épreuve, **aucune réponse sans justification** n'est complète.

## Exercice 1 – Ensemble de vérité

Dans \(E = \{1, 2, \dots, 20\}\), donner l'ensemble de vérité de chaque prédicat : (a) \(P(x)\) : « \(x\) est premier » ; (b) \(Q(x)\) : « \(x\) est multiple de 4 » ; (c) \(P(x) \wedge \neg Q(x)\) ; (d) \(R(x)\) : « \(x\) divise 12 ».

<details markdown="1">
<summary>Voir la réponse</summary>

(a) \{2, 3, 5, 7, 11, 13, 17, 19\}
(b) \{4, 8, 12, 16, 20\}
(c) \{2, 3, 5, 7, 11, 13, 17, 19\} (aucun premier n'est multiple de 4 : c'est donc l'ensemble (a))
(d) \{1, 2, 3, 4, 6, 12\}

</details>

## Exercice 2 – Vrai ou faux ?

Dans \(E = \{3, 5, 7, 9, 11\}\), dire si chaque énoncé est vrai, avec un exemple ou un contre-exemple : (a) \(\forall x \in E,\ x\) impair ; (b) \(\exists x \in E,\ x\) pair ; (c) \(\forall x \in E,\ x\) premier ; (d) \(\exists x \in E,\ x > 10\) ; (e) \(\forall x \in E,\ x \le 11\).

<details markdown="1">
<summary>Voir la réponse</summary>

|  | Valeur | Justification |
|---|---|---|
| (a) | vrai | tous impairs |
| (b) | faux | aucun pair |
| (c) | faux | contre-exemple : 9 = 3 × 3 |
| (d) | vrai | exemple : 11 |
| (e) | vrai | 11 est le plus grand |

</details>

## Exercice 3 – Négations

Écrire la négation en français puis avec des quantificateurs :

1. « Tous les postes ont un antivirus à jour. »
2. « Il existe un utilisateur dont le compte n'a jamais été utilisé. »
3. « Pour tout entier \(n > 2\) pair, \(n\) n'est pas premier. »
4. « Pour tout utilisateur, il existe un serveur auquel il a accès. »

<details markdown="1">
<summary>Voir la réponse</summary>

1. « Il existe un poste dont l'antivirus n'est pas à jour. » \(\exists p,\ \neg A(p)\).
2. « Tous les comptes ont été utilisés au moins une fois. » \(\forall u,\ \neg N(u)\) où \(N(u)\) signifie « jamais utilisé ».
3. « Il existe un entier pair \(n > 2\) qui est premier. » (L'énoncé de départ est vrai, la négation est donc fausse.)
4. « Il existe un utilisateur qui n'a accès à **aucun** serveur. » \(\exists u,\ \forall s,\ \neg A(u, s)\) : on échange chaque quantificateur.

</details>

## Exercice 4 – Ordre des quantificateurs

On donne la relation d'accès \(A(u, s)\) entre trois utilisateurs et trois serveurs.

| | `s1` | `s2` | `s3` |
|---|---|---|---|
| **u1** | accès | accès | — |
| **u2** | accès | — | accès |
| **u3** | accès | — | — |

Évaluer : (a) \(\forall u\, \exists s,\ A(u, s)\) ; (b) \(\exists s\, \forall u,\ A(u, s)\) ; (c) \(\forall s\, \exists u,\ A(u, s)\) ; (d) \(\exists u\, \forall s,\ A(u, s)\).

<details markdown="1">
<summary>Voir la réponse</summary>

|  | Valeur | Justification |
|---|---|---|
| (a) | vrai | chaque utilisateur a au moins un serveur : oui |
| (b) | vrai | `s1` est accessible à tous : exemple |
| (c) | vrai | chaque serveur est accessible à au moins un utilisateur |
| (d) | faux | aucun utilisateur n'a accès aux trois serveurs |

</details>

## Exercice 5 – Opérations

Avec \(E = \{1, \dots, 10\}\), \(A = \{1, 2, 3, 4, 5, 6\}\) et \(B = \{2, 4, 6, 8\}\), déterminer \(A \cap B\), \(A \cup B\), \(A \setminus B\), \(B \setminus A\), \(A \,\Delta\, B\), \(\overline{A}\), et le nombre de parties de \(B\). Vérifier \(|A \cup B| = |A| + |B| - |A \cap B|\).

<details markdown="1">
<summary>Voir la réponse</summary>

- \(A \cap B = \{2, 4, 6\}\) ; \(A \cup B = \{1, 2, 3, 4, 5, 6, 8\}\) ; \(A \setminus B = \{1, 3, 5\}\) ; \(B \setminus A = \{8\}\) ; \(A \,\Delta\, B = \{1, 3, 5, 8\}\) ; \(\overline{A} = \{7, 8, 9, 10\}\).
- \(|\mathcal{P}(B)| = 2^{|B|} = 2^{4} = 16\).
- \(|A \cup B| = 7\) et \(|A| + |B| - |A \cap B| = 6 + 4 - 3 = 7\).

</details>

## Exercice 6 – Inclusions

Soit \(M_6\) l'ensemble des multiples de 6 et \(P\) l'ensemble des entiers pairs (dans \(\mathbb{N}\)).

1. Montrer que \(M_6 \subseteq P\). A-t-on \(P \subseteq M_6\) ?
2. Montrer que \(M_6 = M_2 \cap M_3\) (\(M_k\) : multiples de \(k\)). Indication : S05 (PGCD, PPCM).

<details markdown="1">
<summary>Voir la réponse</summary>

1. Si \(x = 6k\), alors \(x = 2 \times (3k)\) est pair, donc \(M_6 \subseteq P\). Mais \(2 \in P\) et \(2 \notin M_6\) : \(P \not\subseteq M_6\).
2. \(M_6 \subseteq M_2 \cap M_3\) : un multiple de 6 est multiple de 2 et de 3. Réciproquement, si \(x\) est multiple de 2 et de 3, il est multiple de leur PPCM, \(\operatorname{PPCM}(2, 3) = 6\) ; donc \(x \in M_6\). Les deux ensembles sont égaux.

</details>

## Exercice 7 – Lois d'ensembles

Montrer que \(A \cap (B \cup C) = (A \cap B) \cup (A \cap C)\) en dressant le tableau d'appartenance : pour chaque combinaison de « \(x \in A\), \(x \in B\), \(x \in C\) », indiquer si \(x\) est dans chaque ensemble.

<details markdown="1">
<summary>Voir la réponse</summary>

Le tableau est la table de vérité de la distributivité (S08), où 1 signifie « \(x\) appartient » :

| \(A\) | \(B\) | \(C\) | \(B \cup C\) | \(A \cap (B \cup C)\) | \(A \cap B\) | \(A \cap C\) | \((A \cap B) \cup (A \cap C)\) |
|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 | 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 | 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

Les colonnes 5 et 8 sont identiques : les deux ensembles ont les mêmes éléments.

</details>

## Exercice 8 – Groupes d'un annuaire

Utilisateurs : \{ana, ben, chloé, dan, eli, fay\}. Groupes : Compta = \{ana, ben, chloé\} ; RH = \{chloé, dan\} ; Direction = \{ben, eli\}.

1. Qui est à la fois dans Compta et dans Direction ?
2. Qui appartient à au moins un groupe ? Qui n'appartient à aucun ?
3. Qui est dans Compta mais pas dans RH ?
4. L'ensemble RH est-il inclus dans Compta ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. Compta ∩ Direction = \{ben\}.
2. Réunion des trois groupes = \{ana, ben, chloé, dan, eli\} ; aucun groupe : \{fay\} (complémentaire dans l'ensemble des utilisateurs).
3. Compta \ RH = \{ana, ben\}.
4. Non : dan est dans RH mais pas dans Compta (RH ⊄ Compta).

</details>

## Exercice 9 – Parties et masques

1. Lister les parties de \(E = \{a, b, c\}\) à l'aide des nombres de 0 à 7 écrits en binaire.
2. Combien de parties possède un ensemble de 10 éléments ? Combien de bits faut-il pour numéroter les parties de cet ensemble ?
3. À quelle opération sur les nombres correspond la réunion de deux parties ? l'intersection ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. Voir le tableau du cours (8 parties).
2. \(2^{10} = 1024\) parties ; un numéro entre 0 et \(2^{10} - 1\) tient sur 10 bits.
3. Réunion : OU bit à bit (`|`) ; intersection : ET bit à bit (`&`) ; complémentaire : inversion des bits (`^` avec un masque de uns).

</details>


## Je sais faire

Coche honnêtement ; ce que tu ne coches pas se reprend avant la séance suivante.

- [ ] Évaluer un prédicat sur un ensemble fini ;
- [ ] Nier une phrase avec ∀ et ∃ ;
- [ ] Distinguer ∀x ∃y et ∃y ∀x ;
- [ ] Calculer union, intersection, complémentaire, différence ;
- [ ] Calculer un cardinal par la formule de la réunion.

**Ce que je dois reprendre :** ______________________

**Ma question à poser à l'enseignant :** ______________________

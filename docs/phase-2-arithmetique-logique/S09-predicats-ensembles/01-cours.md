# Cours – Prédicats, quantificateurs et ensembles

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S09 – à lire avant les [exercices](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** S08 (connecteurs logiques).
> - **Outils :** Papier, calculatrice, éditeur Python intégré au site

## À la fin de ce cours tu sauras

- [ ] **Écrire** un prédicat à une, deux ou trois variables et **évaluer** sa valeur de vérité ;
- [ ] **Utiliser** les quantificateurs ∀ et ∃ et **nier** correctement une phrase quantifiée ;
- [ ] **Expliquer** que l'ordre des quantificateurs change le sens ;
- [ ] **Manipuler** ensembles, appartenance, inclusion, parties, complémentaire, intersection, réunion, différence ;
- [ ] **Relier** connecteurs et opérations sur les ensembles et **calculer** un cardinal avec \(|A \cup B| = |A| + |B| - |A \cap B|\).

## I. Prédicats

Un **prédicat** est un énoncé qui dépend d'une ou plusieurs **variables** et devient une proposition (vraie ou fausse) quand on leur donne une valeur. Les variables prennent leurs valeurs dans un **ensemble de référence** (le domaine).

| Prédicat | Variables | Exemple de valeur |
|---|---|---|
| \(P(x)\) : « \(x\) est pair » | 1 (\(x \in \mathbb{N}\)) | \(P(6)\) vrai, \(P(7)\) faux |
| \(D(x, y)\) : « \(x\) divise \(y\) » | 2 | \(D(3, 12)\) vrai, \(D(5, 12)\) faux |
| \(A(u, s, m)\) : « l'utilisateur \(u\) peut accéder au serveur \(s\) en mode \(m\) » | 3 | selon la table des droits |

On se limite ici à **trois variables au plus**. L'**ensemble de vérité** de \(P\) dans \(E\) est \(\{x \in E \mid P(x)\}\) : l'ensemble des éléments pour lesquels \(P(x)\) est vrai.

**Exemple.** Dans \(E = \{1, \dots, 15\}\), l'ensemble de vérité de « \(x\) est un multiple de 3 ou de 5 » est \{3, 5, 6, 9, 10, 12, 15\}.

## II. Les quantificateurs

| Quantificateur | Notation | Lecture | Python (ensemble fini) |
|---|---|---|---|
| Universel | \(\forall x \in E,\ P(x)\) | pour **tout** \(x\) de \(E\), \(P(x)\) | `all(P(x) for x in E)` |
| Existentiel | \(\exists x \in E,\ P(x)\) | il **existe** (au moins) un \(x\) de \(E\) tel que \(P(x)\) | `any(P(x) for x in E)` |

Sur un ensemble fini \(E = \{e_1, \dots, e_n\}\), \(\forall x, P(x)\) revient à \(P(e_1) \wedge \dots \wedge P(e_n)\) et \(\exists x, P(x)\) revient à \(P(e_1) \vee \dots \vee P(e_n)\).

> [!NOTE]
> Sur l'ensemble vide, \(\forall x, P(x)\) est **vrai** (rien ne contredit) et \(\exists x, P(x)\) est **faux** (rien ne convient) : `all([])` vaut `True` et `any([])` vaut `False`.

**Exemple.** \(E = \{2, 4, 6, 8, 10\}\).

| Énoncé | Valeur | Pourquoi |
|---|---|---|
| \(\forall x \in E,\ x\) est pair | vrai | 2, 4, 6, 8, 10 sont tous pairs |
| \(\exists x \in E,\ x > 9\) | vrai | \(x = 10\) convient |
| \(\forall x \in E,\ x\) est divisible par 4 | faux | 2 est un contre-exemple |
| \(\exists x \in E,\ x\) est premier | vrai | \(x = 2\) convient |

Pour montrer qu'un énoncé « pour tout » est faux, il suffit d'un **contre-exemple**. Pour montrer qu'un énoncé « il existe » est vrai, il suffit d'**un exemple**.

### Négation

\[
\neg\bigl(\forall x,\ P(x)\bigr) \equiv \exists x,\ \neg P(x) \qquad\qquad \neg\bigl(\exists x,\ P(x)\bigr) \equiv \forall x,\ \neg P(x) .
\]

On échange \(\forall\) et \(\exists\), puis on nie le prédicat (cela généralise De Morgan, S08).

| Énoncé | Négation |
|---|---|
| Tous les comptes ont un mot de passe d'au moins 12 caractères | Il existe un compte dont le mot de passe a moins de 12 caractères |
| Il existe un serveur sans sauvegarde | Tous les serveurs ont une sauvegarde |
| \(\forall x,\ (x > 5 \Rightarrow x \text{ pair})\) | \(\exists x,\ (x > 5 \wedge x \text{ impair})\) |

> [!WARNING]
> La négation de « tous les comptes sont protégés » n'est **pas** « aucun compte n'est protégé », mais « au moins un compte n'est pas protégé ».

### L'ordre des quantificateurs compte

Deux quantificateurs de natures **différentes** ne commutent pas.

**Exemple dans \(\mathbb{R}\).** « \(\forall x,\ \exists y,\ y > x\) » est **vrai** (on prend \(y = x + 1\)). « \(\exists y,\ \forall x,\ y > x\) » est **faux** (quel que soit \(y\), le nombre \(x = y\) n'est pas strictement plus petit que \(y\) : c'est un contre-exemple).

**Exemple avec des droits d'accès.** Deux utilisateurs \(u_1, u_2\), deux serveurs \(s_1, s_2\) :

| | `s1` | `s2` |
|---|---|---|
| **u1** | accès | — |
| **u2** | — | accès |

- « Chaque utilisateur a accès à **au moins un** serveur » : \(\forall u,\ \exists s,\ A(u, s)\) est **vrai**.
- « Il existe **un** serveur auquel **tous** ont accès » : \(\exists s,\ \forall u,\ A(u, s)\) est **faux**.

En Python : `all(any(...) ...)` et `any(all(...) ...)` ne sont pas interchangeables. Deux quantificateurs de **même** nature commutent (\(\forall x\, \forall y\) équivaut à \(\forall y\, \forall x\)).

## III. Les ensembles

Un **ensemble** est une collection d'objets distincts, sans ordre. On écrit \(x \in A\) si \(x\) appartient à \(A\), \(x \notin A\) sinon.

- **En extension** : on liste les éléments, \(A = \{1, 2, 3\}\).
- **En compréhension** : on donne une propriété, \(A = \{x \in \mathbb{N} \mid x \text{ pair et } x < 10\} = \{0, 2, 4, 6, 8\}\).
- L'**ensemble vide** \(\varnothing\) n'a aucun élément. Le **cardinal** \(|A|\) est le nombre d'éléments d'un ensemble fini.

### Inclusion, égalité, parties

- \(A \subseteq B\) (inclusion) signifie \(\forall x,\ (x \in A \Rightarrow x \in B)\).
- \(A = B\) signifie \(A \subseteq B\) **et** \(B \subseteq A\).
- L'ensemble des **parties** de \(E\), noté \(\mathcal{P}(E)\), est l'ensemble de tous les sous-ensembles de \(E\) (y compris \(\varnothing\) et \(E\)). Si \(|E| = n\), alors \(|\mathcal{P}(E)| = 2^n\) : chaque élément est dans la partie ou n'y est pas.

Pour \(E = \{a, b, c\}\), on peut numéroter les parties de 0 à \(2^3 - 1\) : le bit de rang \(i\) vaut 1 si le \(i\)-ème élément est dans la partie (c'est exactement un **masque**, S03) :

| Nombre \(k\) | Écriture binaire | Partie |
|---|---|---|
| 0 | 000 | \varnothing |
| 1 | 001 | \{a\} |
| 2 | 010 | \{b\} |
| 3 | 011 | \{a, b\} |
| 4 | 100 | \{c\} |
| 5 | 101 | \{a, c\} |
| 6 | 110 | \{b, c\} |
| 7 | 111 | \{a, b, c\} |

(Le bit de poids faible correspond à \(a\), le suivant à \(b\), le dernier à \(c\).)

### Opérations

| Opération | Notation | Définition | Connecteur associé |
|---|---|---|---|
| Intersection | \(A \cap B\) | \(\{x \mid x \in A \wedge x \in B\}\) | \(\wedge\) |
| Réunion | \(A \cup B\) | \(\{x \mid x \in A \vee x \in B\}\) | \(\vee\) |
| Complémentaire (dans \(E\)) | \(\overline{A}\) | \(\{x \in E \mid x \notin A\}\) | \(\neg\) |
| Différence | \(A \setminus B\) | \(\{x \mid x \in A \wedge x \notin B\}\) | \(\wedge\) avec \(\neg\) |
| Différence symétrique | \(A \,\Delta\, B\) | \((A \setminus B) \cup (B \setminus A)\) | \(\oplus\) |
| Inclusion | \(A \subseteq B\) | | \(\Rightarrow\) |

Les propriétés des connecteurs (S08) passent aux ensembles. En particulier, les **lois de De Morgan** :

\[
\overline{A \cap B} = \overline{A} \cup \overline{B} , \qquad \overline{A \cup B} = \overline{A} \cap \overline{B} .
\]

**Exemple.** Avec \(E = \{1, \dots, 10\}\), \(A = \{1, 2, 3, 4, 5, 6\}\), \(B = \{2, 4, 6, 8\}\) :

| Opération | Résultat |
|---|---|
| \(A \cap B\) | \(\{2, 4, 6\}\) |
| \(A \cup B\) | \(\{1, 2, 3, 4, 5, 6, 8\}\) |
| \(A \setminus B\) | \(\{1, 3, 5\}\) |
| \(B \setminus A\) | \(\{8\}\) |
| \(A \,\Delta\, B\) | \(\{1, 3, 5, 8\}\) |
| \(\overline{A}\) | \(\{7, 8, 9, 10\}\) |

### Des prédicats aux ensembles

Si \(A_P = \{x \in E \mid P(x)\}\) et \(A_Q = \{x \in E \mid Q(x)\}\), alors l'ensemble de vérité de \(P \wedge Q\) est \(A_P \cap A_Q\), celui de \(P \vee Q\) est \(A_P \cup A_Q\), celui de \(\neg P\) est \(\overline{A_P}\), et \(P \Rightarrow Q\) est vrai pour tout \(x\) exactement quand \(A_P \subseteq A_Q\).

## IV. Compter avec les ensembles

Pour des ensembles finis,

\[
|A \cup B| = |A| + |B| - |A \cap B| , \qquad |\overline{A}| = |E| - |A| .
\]

(On a compté deux fois les éléments de \(A \cap B\) : il faut les retirer une fois.)

**Exemple.** Dans un parc de 100 postes, 70 ont l'antivirus (\(A\)), 45 ont le disque chiffré (\(C\)) et 25 ont les deux. Postes avec au moins l'une des deux protections : \(|A \cup C| = 70 + 45 - 25 = 90\). Postes sans aucune des deux : \(100 - 90 = 10\).

## V. Les ensembles en Python

```python
A = {1, 2, 3, 4, 5, 6}
B = {2, 4, 6, 8}
A & B      # intersection : {2, 4, 6}
A | B      # réunion
A - B      # différence
A ^ B      # différence symétrique
B <= A     # inclusion : False
4 in A     # appartenance : True
len(A)     # cardinal
```

**Application : groupes d'utilisateurs.** Chaque groupe d'un annuaire est un ensemble d'utilisateurs : l'**intersection** donne les personnes qui cumulent deux appartenances, la **réunion** tous les utilisateurs concernés par au moins un groupe, la **différence** ceux qui appartiennent à un groupe mais pas à l'autre.

## À retenir

- Prédicat : énoncé à variables (au plus 3 ici) ; \(\forall\) (« tout ») ↔ `all`, \(\exists\) (« il existe ») ↔ `any`.
- **Négation** : \(\neg \forall \equiv \exists \neg\) ; \(\neg \exists \equiv \forall \neg\). Un contre-exemple réfute un \(\forall\).
- \(\forall x\, \exists y\) et \(\exists y\, \forall x\) n'ont **pas** le même sens.
- \(A \subseteq B\) ↔ \(\Rightarrow\) ; \(\cap\) ↔ \(\wedge\) ; \(\cup\) ↔ \(\vee\) ; complémentaire ↔ \(\neg\) ; De Morgan s'applique.
- \(|\mathcal{P}(E)| = 2^{|E|}\) ; \(|A \cup B| = |A| + |B| - |A \cap B|\).

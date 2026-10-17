# Cours – Calcul des propositions

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S08 – à lire avant les [exercices](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** S03 (conditions).
> - **Outils :** Papier, calculatrice, éditeur Python intégré au site

## À la fin de ce cours tu sauras

- [ ] **Reconnaître** une proposition et lui **attribuer** une valeur de vérité ;
- [ ] **Construire** la table de vérité d'une expression avec ¬, ∧, ∨, ⇒, ⇔ (et ⊕, « ou exclusif ») ;
- [ ] **Identifier** une tautologie, une contradiction, deux expressions équivalentes ;
- [ ] **Écrire** la négation, la réciproque et la contraposée d'une implication ;
- [ ] **Traduire** une règle de filtrage ou une condition de boucle en expression logique.

## I. Propositions

Une **proposition** est un énoncé qui est soit **vrai** (V), soit **faux** (F), sans ambiguïté. Une question, un ordre ou un énoncé dont la valeur dépend d'une variable non précisée ne sont pas des propositions.

| Énoncé | Proposition ? | Valeur |
|---|---|---|
| « 7 est un nombre premier » | oui | V |
| « 91 est un nombre premier » | oui | F (91 = 7 × 13) |
| « Quelle heure est-il ? » | non (question) | — |
| « \(x > 3\) » | non (dépend de \(x\) : c'est un **prédicat**, S09) | — |
| « L'adresse 10.0.0.1 est privée » | oui | V |

On désigne les propositions par des lettres \(p, q, r\) et on les combine avec des **connecteurs**.

## II. Les connecteurs logiques

| Connecteur | Notation | Lecture | Python | Vrai quand… |
|---|---|---|---|---|
| Négation | \(\neg p\) | non \(p\) | `not p` | \(p\) est faux |
| Conjonction | \(p \wedge q\) | \(p\) et \(q\) | `p and q` | \(p\) et \(q\) sont vrais |
| Disjonction | \(p \vee q\) | \(p\) ou \(q\) (inclusif) | `p or q` | au moins un des deux est vrai |
| Implication | \(p \Rightarrow q\) | si \(p\) alors \(q\) | `(not p) or q` | on n'a pas (\(p\) vrai et \(q\) faux) |
| Équivalence | \(p \Leftrightarrow q\) | \(p\) si et seulement si \(q\) | `p == q` | \(p\) et \(q\) ont la même valeur |
| Ou exclusif | \(p \oplus q\) | l'un ou l'autre, pas les deux | `p != q` | \(p\) et \(q\) ont des valeurs différentes |

**Tables de vérité** :

| \(p\) | \(q\) | \(\neg p\) | \(p \wedge q\) | \(p \vee q\) | \(p \Rightarrow q\) | \(p \Leftrightarrow q\) | \(p \oplus q\) |
|---|---|---|---|---|---|---|---|
| F | F | V | F | F | V | V | F |
| F | V | V | F | V | V | F | V |
| V | F | F | F | V | F | F | V |
| V | V | F | V | V | V | V | F |

> [!NOTE]
> **Le « ou » de la langue courante.** « Fromage ou dessert » est souvent un ou **exclusif**. Le \(\vee\) mathématique est **inclusif** : il reste vrai si les deux propositions sont vraies.

### L'implication, le connecteur qui surprend

\(p \Rightarrow q\) n'est fausse que dans un seul cas : \(p\) vraie et \(q\) fausse. On la voit comme un **engagement** : « si la règle s'applique, alors le paquet est accepté ». L'engagement n'est violé que si la règle s'applique et que le paquet n'est pas accepté. Si \(p\) est faux, l'implication est vraie (on dit qu'elle est « vacuement » vraie) : « si 7 est pair, alors 3 = 5 » est une proposition vraie.

À partir de \(p \Rightarrow q\), on forme :

| Nom | Énoncé | Équivalent à \(p \Rightarrow q\) ? |
|---|---|---|
| **Réciproque** | \(q \Rightarrow p\) | **non** |
| **Contraposée** | \(\neg q \Rightarrow \neg p\) | **oui** |
| **Négation** | \(p \wedge \neg q\) | c'est le contraire de \(p \Rightarrow q\) |

**Exemple.** « Si une adresse est dans 192.168.0.0/16, alors elle est privée » (vraie). La réciproque, « si une adresse est privée, alors elle est dans 192.168.0.0/16 », est **fausse** (10.0.0.1 est privée). La contraposée, « si une adresse n'est pas privée, alors elle n'est pas dans 192.168.0.0/16 », est vraie.

## III. Expressions composées et table de vérité

Avec \(n\) propositions, il y a \(2^n\) combinaisons de valeurs : la table a \(2^n\) lignes. On calcule colonne par colonne, en respectant les parenthèses. À défaut de parenthèses, les priorités sont : \(\neg\), puis \(\wedge\), puis \(\vee\), puis \(\Rightarrow\), puis \(\Leftrightarrow\).

**Exemple.** \(E = (p \wedge \neg q) \vee r\) :

| \(p\) | \(q\) | \(r\) | \(\neg q\) | \(p \wedge \neg q\) | \((p \wedge \neg q) \vee r\) |
|---|---|---|---|---|---|
| F | F | F | V | F | F |
| F | F | V | V | F | V |
| F | V | F | F | F | F |
| F | V | V | F | F | V |
| V | F | F | V | V | V |
| V | F | V | V | V | V |
| V | V | F | F | F | F |
| V | V | V | F | F | V |

\(E\) est vraie dans 5 cas sur 8.

## IV. Tautologies, contradictions, équivalences

- Une **tautologie** est toujours vraie, quelles que soient les valeurs : \(p \vee \neg p\).
- Une **contradiction** est toujours fausse : \(p \wedge \neg p\).
- Deux expressions sont **équivalentes** (\(\equiv\)) si elles ont la même table de vérité.

### Équivalences à connaître

| Nom | Équivalence |
|---|---|
| Double négation | \(\neg \neg p \equiv p\) |
| Commutativité | \(p \wedge q \equiv q \wedge p\) ; \(p \vee q \equiv q \vee p\) |
| Distributivité | \(p \wedge (q \vee r) \equiv (p \wedge q) \vee (p \wedge r)\) ; \(p \vee (q \wedge r) \equiv (p \vee q) \wedge (p \vee r)\) |
| **Lois de De Morgan** | \(\neg(p \wedge q) \equiv \neg p \vee \neg q\) ; \(\neg(p \vee q) \equiv \neg p \wedge \neg q\) |
| Implication | \(p \Rightarrow q \equiv \neg p \vee q\) |
| Contraposée | \(p \Rightarrow q \equiv \neg q \Rightarrow \neg p\) |
| Négation d'une implication | \(\neg(p \Rightarrow q) \equiv p \wedge \neg q\) |
| Équivalence | \(p \Leftrightarrow q \equiv (p \Rightarrow q) \wedge (q \Rightarrow p)\) |
| Ou exclusif | \(p \oplus q \equiv (p \wedge \neg q) \vee (\neg p \wedge q)\) |

**Démonstration d'une loi de De Morgan** par table :

| \(p\) | \(q\) | \(\neg(p \wedge q)\) | \(\neg p\) | \(\neg q\) | \(\neg p \vee \neg q\) |
|---|---|---|---|---|---|
| F | F | V | V | V | V |
| F | V | V | V | F | V |
| V | F | V | F | V | V |
| V | V | F | F | F | F |

Les colonnes \(\neg(p \wedge q)\) et \(\neg p \vee \neg q\) sont identiques : les deux expressions sont équivalentes.

### Raisonner : deux tautologies fondamentales

- **Modus ponens** : \(((p \Rightarrow q) \wedge p) \Rightarrow q\). Si l'implication est vraie et que son hypothèse est vraie, la conclusion l'est.
- **Transitivité** : \(((p \Rightarrow q) \wedge (q \Rightarrow r)) \Rightarrow (p \Rightarrow r)\).

(Ces deux énoncés sont des tautologies : on le vérifie par table de vérité.)

## V. Traduire en logique

### Une règle de filtrage

« Autoriser un paquet si (le protocole est TCP **et** le port est 80 **ou** 443) **ou** si le protocole est ICMP. »

Avec \(t\) : « le protocole est TCP », \(a\) : « le port est 80 », \(b\) : « le port est 443 », \(i\) : « le protocole est ICMP », la règle s'écrit

\[
(t \wedge (a \vee b)) \vee i .
\]

Les parenthèses lèvent l'ambiguïté du « et… ou… » de la langue.

### Une condition de boucle

Une boucle `tant que (i < n et t[i] != x)` parcourt un tableau `t` à la recherche de `x`. Elle s'arrête quand la condition devient **fausse**. Par De Morgan :

\[
\neg(i < n \wedge t[i] \neq x) \equiv (i \ge n) \vee (t[i] = x) .
\]

La boucle s'arrête donc quand on a épuisé le tableau **ou** trouvé `x`. L'**ordre** des deux conditions compte en pratique : avec l'évaluation partielle (S03), `i < n` est testé d'abord, ce qui évite de lire `t[n]` hors du tableau.

## À retenir

- Proposition = vrai ou faux ; \(\neg, \wedge, \vee, \Rightarrow, \Leftrightarrow, \oplus\) ; table à \(2^n\) lignes pour \(n\) variables.
- \(p \Rightarrow q\) est fausse seulement si \(p\) est vraie et \(q\) fausse ; \(p \Rightarrow q \equiv \neg p \vee q \equiv \neg q \Rightarrow \neg p\) ; la réciproque n'est **pas** équivalente.
- **De Morgan** : \(\neg(p \wedge q) \equiv \neg p \vee \neg q\), \(\neg(p \vee q) \equiv \neg p \wedge \neg q\).
- Deux expressions sont équivalentes si leurs tables de vérité sont identiques.
- Une condition d'arrêt de boucle se déduit en **niant** la condition de continuation.

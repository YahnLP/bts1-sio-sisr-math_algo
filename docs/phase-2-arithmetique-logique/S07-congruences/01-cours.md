# Cours – Congruences

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S07 – à lire avant les [exercices](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** S05, S06 (division euclidienne, premiers entre eux).
> - **Outils :** Papier, calculatrice, éditeur Python intégré au site

## À la fin de ce cours tu sauras

- [ ] **Définir** la congruence modulo \(n\) et **passer** de \(a \equiv b \pmod n\) à \(n \mid a - b\) ;
- [ ] **Utiliser** les propriétés de compatibilité avec l'addition et la multiplication, et **calculer** une puissance modulo \(n\) ;
- [ ] **Déterminer** si un entier a un inverse modulo \(n\) et **le calculer** pour de petits modules ;
- [ ] **Chiffrer** et **déchiffrer** avec le code de César et le code affine ;
- [ ] **Calculer** une clé de contrôle (numéro de sécurité sociale, ISBN-13, IBAN) et **parcourir** une liste circulaire.

## I. Calculer « à l'horloge »

Il est 15 h. Quelle heure sera-t-il dans 100 heures ? Une journée compte 24 heures : \(100 = 24 \times 4 + 4\). On revient à 15 h puis on ajoute 4 heures : il sera **19 h**. On n'a gardé que le **reste** de la division par 24. C'est l'idée des congruences.

## II. Définition

Soit \(n\) un entier supérieur ou égal à 2. Deux entiers relatifs \(a\) et \(b\) sont **congrus modulo \(n\)** si leur différence est un multiple de \(n\) :

\[
a \equiv b \pmod n \iff n \mid (a - b) \iff a \text{ et } b \text{ ont le même reste dans la division par } n .
\]

| Congruence | Pourquoi |
|---|---|
| 37 ≡ 2 (mod 5) | \(37 - 2 = 35 = 5 \times 7\) |
| \(-1\) ≡ 4 (mod 5) | \(-1 - 4 = -5 = 5 \times (-1)\) |
| 100 ≡ 4 (mod 24) | \(100 - 4 = 96 = 24 \times 4\) |

Tout entier est congru, modulo \(n\), à **un seul** entier de \(\{0, 1, \dots, n-1\}\) : son reste dans la division par \(n\). On note `a % n` en Python (pour \(n > 0\) le résultat est toujours dans cet ensemble, même si \(a\) est négatif).

## III. Calculer avec les congruences

**Propriété.** Si \(a \equiv b \pmod n\) et \(c \equiv d \pmod n\), alors

\[
a + c \equiv b + d , \qquad a - c \equiv b - d , \qquad a \times c \equiv b \times d , \qquad a^k \equiv b^k \pmod n .
\]

*Justification pour le produit.* Si \(a = b + nk\) et \(c = d + nk'\), alors \(ac = bd + n(bk' + dk + nkk')\).

On peut donc **réduire à chaque étape** : on remplace chaque nombre par son reste.

**Exemple : dernier chiffre de \(7^{100}\)** (c'est le reste modulo 10). \(7^2 = 49 \equiv 9\), \(7^4 \equiv 9^2 = 81 \equiv 1 \pmod{10}\). Donc \(7^{100} = (7^4)^{25} \equiv 1^{25} = 1 \pmod{10}\) : le dernier chiffre de \(7^{100}\) est 1.

**Exemple : critère de divisibilité par 9** (S05). Comme \(10 \equiv 1 \pmod 9\), on a \(10^j \equiv 1\) et donc \(a_k 10^k + \dots + a_0 \equiv a_k + \dots + a_0 \pmod 9\) : un entier a le même reste modulo 9 que la somme de ses chiffres.

> [!WARNING]
> **On ne simplifie pas toujours.** Modulo 6, \(2 \times 3 = 6 \equiv 0 = 2 \times 0\), pourtant \(3 \not\equiv 0\). On ne peut pas « diviser par 2 » dans une congruence modulo 6 : voir le paragraphe suivant.

## IV. Multiples et inverses modulo \(n\)

Modulo \(n\), les multiples d'un entier \(a\) sont les multiples de \(\operatorname{PGCD}(a, n)\). En particulier, si \(\operatorname{PGCD}(a, n) = 1\), tous les restes apparaissent.

Un entier \(a\) a un **inverse modulo \(n\)** s'il existe \(x\) tel que \(a x \equiv 1 \pmod n\). Cela arrive **si et seulement si** \(a\) et \(n\) sont **premiers entre eux**.

*Idée.* Si \(\operatorname{PGCD}(a, n) = 1\), les produits \(a \times 0, a \times 1, \dots, a \times (n-1)\) ont des restes tous différents modulo \(n\) (sinon \(n\) diviserait \(a(x-y)\), donc \(x - y\), avec \(|x-y| < n\)). Ce sont donc tous les restes possibles, dont 1. (Si \(\operatorname{PGCD}(a, n) = d > 1\), tous les multiples de \(a\) sont des multiples de \(d\) modulo \(n\), jamais 1.)

**Table de multiplication modulo 7** (7 est premier : toute ligne non nulle contient 1) :

| \(\times\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| **0** | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **1** | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| **2** | 0 | 2 | 4 | 6 | 1 | 3 | 5 |
| **3** | 0 | 3 | 6 | 2 | 5 | 1 | 4 |
| **4** | 0 | 4 | 1 | 5 | 2 | 6 | 3 |
| **5** | 0 | 5 | 3 | 1 | 6 | 4 | 2 |
| **6** | 0 | 6 | 5 | 4 | 3 | 2 | 1 |

**Inverses modulo 7 :**

| \(a\) | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| inverse | 1 | 4 | 5 | 2 | 3 | 6 |

**Modulo 12**, seuls 1, 5, 7, 11 (premiers avec 12) ont un inverse :

| \(a\) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| inverse | 1 | aucun | aucun | aucun | 5 | aucun | 7 | aucun | aucun | aucun | 11 |

Pour résoudre \(a x \equiv c \pmod n\) avec \(\operatorname{PGCD}(a, n) = 1\), on multiplie par l'inverse \(a'\) de \(a\) : \(x \equiv a' c \pmod n\). Exemple : \(7x \equiv 4 \pmod{26}\) ; l'inverse de 7 est 15 (car \(7 \times 15 = 105 = 4 \times 26 + 1\)) ; donc \(x \equiv 15 \times 4 = 60 \equiv 8 \pmod{26}\). Vérification : \(7 \times 8 = 56 = 2 \times 26 + 4\).

## V. Applications

### Parcourir une liste circulaire

Dans une liste de \(n\) éléments numérotés de 0 à \(n-1\), on part de la case 0 et on avance par sauts de \(k\) cases : on visite les cases \(0, k, 2k, \dots\) **modulo \(n\)**.

| \(n\) | \(k\) | Cases visitées (dans l'ordre, avant de revenir à 0) | \(\operatorname{PGCD}(k, n)\) | Toutes visitées ? |
|---|---|---|---|---|
| 12 | 5 | 0, 5, 10, 3, 8, 1, 6, 11, 4, 9, 2, 7 | 1 | oui |
| 12 | 4 | 0, 4, 8 | 4 | non |
| 10 | 3 | 0, 3, 6, 9, 2, 5, 8, 1, 4, 7 | 1 | oui |
| 10 | 4 | 0, 4, 8, 2, 6 | 2 | non |

La suite revient à 0 après \(n / \operatorname{PGCD}(k, n)\) sauts : **toutes les cases sont visitées si et seulement si \(k\) et \(n\) sont premiers entre eux.**

### Le chiffre de César et le chiffre affine

On numérote les lettres de A = 0 à Z = 25. Le **chiffre de César** décale de \(s\) rangs : \(y \equiv x + s \pmod{26}\). Pour déchiffrer on retranche : \(x \equiv y - s \pmod{26}\).

Exemple avec \(s = 3\) : BONJOUR devient **ERQMRXU** ; et **KHOOR** se déchiffre en **HELLO**.

Le **chiffre affine** utilise \(y \equiv a x + b \pmod{26}\). Pour pouvoir déchiffrer, il faut que \(a\) ait un inverse modulo 26, c'est-à-dire que \(a\) soit **premier avec 26** (\(a\) impair et différent de 13). Alors \(x \equiv a'(y - b) \pmod{26}\) où \(a'\) est l'inverse de \(a\).

Les inverses modulo 26 sont :

| \(a\) | inverse de \(a\) |
|---|---|
| 1 | 1 |
| 3 | 9 |
| 5 | 21 |
| 7 | 15 |
| 9 | 3 |
| 11 | 19 |
| 15 | 7 |
| 17 | 23 |
| 19 | 11 |
| 21 | 5 |
| 23 | 17 |
| 25 | 25 |

**Exemple.** Chiffrer AFFINE avec \(a = 5\), \(b = 8\) :

| Lettre | Rang \(x\) | \(5x + 8\) | Reste mod 26 | Lettre chiffrée |
|---|---|---|---|---|
| A | 0 | 8 | 8 | I |
| F | 5 | 33 | 7 | H |
| F | 5 | 33 | 7 | H |
| I | 8 | 48 | 22 | W |
| N | 13 | 73 | 21 | V |
| E | 4 | 28 | 2 | C |

Le message chiffré est **IHHWVC**. Pour le déchiffrer, \(5' = 21\) (car \(5 \times 21 = 105 = 4 \times 26 + 1\)) : par exemple pour la lettre I (rang 8), \(x \equiv 21 \times (8 - 8) = 0\), c'est bien A.

> [!WARNING]
> **Ces chiffrements ne sont pas sûrs** : il n'y a que 25 décalages possibles pour César, \(12 \times 26 = 312\) clés pour le chiffre affine, et la fréquence des lettres trahit le message. Ils servent ici à comprendre les congruences.

Pour \(a = 13\) (non premier avec 26), \(13 \times 0 + b\) et \(13 \times 2 + b = 26 + b\) donnent la même lettre : A et C seraient chiffrées pareil, on ne pourrait plus déchiffrer.

### Les clés de contrôle

Une **clé de contrôle** est calculée à partir des autres chiffres, pour détecter une erreur de saisie ou de transmission.

- **Numéro de sécurité sociale (NIR).** Les 13 premiers chiffres forment un nombre \(N\) ; la clé, à deux chiffres, vaut \(97 - (N \bmod 97)\). Exemple (numéro fictif) : \(N = 1850578006084\), \(N \bmod 97 = 6\), clé \(= 97 - 6 = 91\). Contrôle : \(N + \text{clé}\) est un multiple de 97 : le reste de \(1850578006175\) modulo 97 est 0.
- **ISBN-13** (livres). On pondère les 13 chiffres alternativement par 1 et 3 ; la somme doit être un multiple de 10. Pour `9780306406157` : somme \(= 100\), qui est un multiple de 10.
- **IBAN** (compte bancaire). On déplace les 4 premiers caractères à la fin, on remplace chaque lettre par un nombre (A = 10, B = 11, …, Z = 35) et on vérifie que le nombre obtenu est **congru à 1 modulo 97**. Exemple d'IBAN de démonstration : `FR76 3000 6000 0112 3456 7890 189` donne le nombre `30006000011234567890189152776`, dont le reste modulo 97 est 1.

### Le hachage

Une **table de hachage** range chaque clé \(x\) dans la case \(h(x) = x \bmod m\). Avec \(m = 7\) et les clés 14, 27, 31, 44, 59 :

| Clé \(x\) | Case \(x \bmod 7\) |
|---|---|
| 14 | 0 |
| 27 | 6 |
| 31 | 3 |
| 44 | 2 |
| 59 | 3 |

Les clés 31 et 59 tombent dans la même case (**collision**), qu'il faut gérer.

### Jours de la semaine

Le 1er janvier 2024 était un lundi. Le 25 décembre est le jour numéro \(360\) de cette année bissextile (31+29+31+30+31+30+31+31+30+31+30 = 335 jours avant décembre, plus 25). Comme \(360 - 1 = 359 = 7 \times 51 + 2\), on avance de 2 jours depuis le lundi : un **mercredi**.

## À retenir

- \(a \equiv b \pmod n\) ⟺ \(n \mid a - b\) ⟺ même reste dans la division par \(n\).
- Compatible avec \(+\), \(-\), \(\times\), puissances : on **réduit à chaque étape**. Pas de simplification automatique.
- \(a\) a un inverse modulo \(n\) ⟺ \(\operatorname{PGCD}(a, n) = 1\).
- Saut de \(k\) dans une liste circulaire de taille \(n\) : tout est visité ⟺ \(\operatorname{PGCD}(k, n) = 1\).
- Chiffre affine \(y \equiv ax + b \pmod{26}\), \(a\) premier avec 26 ; clés de contrôle : NIR (97), ISBN (10), IBAN (97).

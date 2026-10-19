# Cours – Valider et contrôler des données

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S15 – à lire avant les [exercices](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** S03, S04, S12 (conditions, boucles, fonctions, chaînes, tableaux) ; S07 (modulo) ; S10 (OU exclusif).
> - **Outils :** Papier, calculatrice, éditeur Python intégré au site

## À la fin de ce cours tu sauras

- [ ] **Écrire** une fonction qui valide le format d'une donnée en parcourant une chaîne ;
- [ ] **Choisir** les cas limites à tester ;
- [ ] **Calculer** un bit de parité et **détecter** une erreur de transmission ;
- [ ] **Localiser** et **corriger** une erreur isolée avec une parité à deux dimensions ;
- [ ] **Calculer** une somme de contrôle modulo 256 et un OU exclusif de contrôle.

## I. Valider le format d'une donnée

Un programme qui reçoit une donnée (saisie, fichier, message réseau) doit d'abord vérifier qu'elle est **bien formée** avant de s'en servir. On écrit pour cela une fonction qui renvoie un **booléen**.

**Méthode.** (1) Écrire en français **toutes les règles** du format ; (2) traduire chaque règle en un test ; (3) renvoyer `False` dès qu'une règle est violée, `True` seulement si toutes sont respectées.

### Un octet décimal

Règles pour la chaîne `s` qui représente un octet d'adresse IPv4 :

1. `s` n'est pas vide et ne contient que des chiffres ;
2. `s` ne commence pas par un zéro, sauf si c'est `"0"` seul ;
3. la valeur est comprise entre 0 et 255.

```text
ALGORITHME est_octet
RÔLE : dire si une chaîne est un octet décimal valide
ENTRÉE : s, une chaîne
SORTIE : un booléen
DÉBUT
  SI s est vide OU s contient un caractère qui n'est pas un chiffre ALORS
    RENVOYER faux
  FIN SI
  SI longueur(s) > 1 ET s[0] = "0" ALORS
    RENVOYER faux
  FIN SI
  RENVOYER (0 ≤ valeur(s) ≤ 255)
FIN
```

L'ordre des tests compte : on convertit en nombre (`int(s)`) **après** avoir vérifié que `s` ne contient que des chiffres, sinon `int("1a")` provoque une erreur.

### Une adresse IPv4

Une adresse IPv4 écrite en notation décimale pointée comporte **exactement quatre** octets séparés par des points. En Python, `s.split(".")` découpe la chaîne en morceaux : `"192.168.10.77".split(".")` donne `["192", "168", "10", "77"]`.

| Chaîne | Morceaux | Valide ? | Raison |
|---|---|---|---|
| `192.168.10.77` | 4 | oui | |
| `192.168.10` | 3 | non | il manque un octet |
| `192.168.10.77.1` | 5 | non | un octet de trop |
| `192.168.300.1` | 4 | non | 300 > 255 |
| `192.168..1` | 4 | non | un morceau vide |
| `192.168.01.1` | 4 | non | zéro initial |

La validité de l'adresse **se ramène** à la validité de chacun de ses quatre morceaux : c'est l'intérêt de découper le problème en fonctions.

### Une adresse MAC

Une adresse MAC s'écrit avec six groupes de deux chiffres hexadécimaux séparés par `:`, par exemple `00:1A:2b:3C:4d:5E`. Les chiffres hexadécimaux sont `0` à `9` et `a` à `f` (majuscules ou minuscules).

### Les cas limites

Un test ne vaut que par les cas qu'il couvre. Pour un validateur, on teste toujours :

- le cas **normal** valide ;
- la chaîne **vide** ;
- les valeurs à la **frontière** (0, 255, 256) ;
- un **caractère interdit** ;
- un morceau en **trop** et un morceau en **moins**.

## II. Détecter une erreur : le bit de parité

Un message transmis ou stocké peut être altéré : un bit passe de 0 à 1 ou de 1 à 0. Le **bit de parité** est un bit ajouté au mot pour détecter une telle altération.

**Parité paire.** On ajoute un bit choisi pour que le nombre **total** de 1 (bit de parité compris) soit **pair**.

\[ \text{bit de parité} = (\text{nombre de 1 du mot}) \bmod 2 \]

| Mot (7 bits) | Nombre de 1 | Bit de parité | Mot transmis (8 bits) |
|---|---|---|---|
| `1011001` | 4 | 0 | `10110010` |
| `1011000` | 3 | 1 | `10110001` |

**Contrôle à la réception.** On recompte les 1 : si le nombre est impair, une erreur s'est produite.

Le bit de parité est aussi le **OU exclusif** (S10) de tous les bits du mot : \(1 \oplus 0 \oplus 1 \oplus 1 = 1\) pour `1011`, qui contient trois 1.

> [!WARNING]
> **Limites.** La parité détecte toute erreur sur **un nombre impair** de bits, mais **aucune** erreur sur un nombre pair de bits (deux erreurs se compensent). Et elle **ne dit pas où** est l'erreur.

### Parité à deux dimensions

On range les données dans une grille et on ajoute un bit de parité **à chaque ligne** et **à chaque colonne** (le coin contrôle les parités elles-mêmes).

Si **un seul** bit est inversé, **une** ligne et **une** colonne ont une parité fausse : le bit erroné est **à leur intersection**. On peut donc non seulement détecter l'erreur, mais la **corriger**.

```text
        col 0 col 1 col 2 | parité
ligne 0   1     0     1   |   0
ligne 1   0     1     0   |   0     ← 1 seul « 1 » (la ligne 1 devrait en compter un nombre pair)
ligne 2   1     1     0   |   0
          ------------------+----
parité    0     0     0   |   0
                          ↑ la colonne 2 compte un seul « 1 »
```

Ici, la ligne 1 et la colonne 2 ont un nombre impair de 1 : le bit `g[1][2]` (valeur 0) est faux, il faut le remplacer par 1.

## III. La somme de contrôle

On ajoute à la fin du message un octet calculé à partir de **tous** les octets. À la réception, on refait le calcul.

**Somme de contrôle modulo 256.** Pour les octets \(o_1, \dots, o_k\), on choisit l'octet \(c\) (de 0 à 255) tel que

\[ o_1 + o_2 + \dots + o_k + c \equiv 0 \pmod{256}, \quad\text{soit}\quad c = (-\textstyle\sum o_i) \bmod 256. \]

**Exemple.** Octets \(10, 20, 30\) : somme \(60\), donc \(c = 256 - 60 = 196\) ; contrôle : \(60 + 196 = 256 \equiv 0\).

En Python, `(-sum(octets)) % 256` donne directement \(c\) (le reste d'une division par 256 est toujours entre 0 et 255).

**OU exclusif de contrôle.** On peut aussi combiner les octets avec `^` : `r = r ^ o` pour chaque octet. Comme \(x \oplus x = 0\), ajouter ce résultat à la fin du message donne un OU exclusif total nul.

> [!WARNING]
> Ces contrôles **détectent** des erreurs, ils ne **protègent** rien : n'importe qui peut recalculer un contrôle correct sur un message modifié. Une somme de contrôle ne remplace pas une signature ni une empreinte cryptographique.

**Ce qu'elle ne voit pas.** Deux erreurs qui se compensent (un octet augmenté de 1, un autre diminué de 1) laissent la somme inchangée ; l'échange de deux octets aussi.

## À retenir

- Valider = écrire toutes les règles, les tester une à une, renvoyer `False` dès qu'une est violée.
- Toujours tester : cas normal, chaîne vide, frontières, caractère interdit, élément en trop ou manquant.
- Parité paire : bit \(= (\text{nombre de 1}) \bmod 2\) ; détecte un nombre impair d'erreurs, ne localise pas.
- Parité à deux dimensions : une ligne et une colonne fausses désignent le bit à corriger.
- Somme de contrôle : \(c = (-\sum o_i) \bmod 256\) ; le contrôle réussit si \((\sum o_i + c) \bmod 256 = 0\).

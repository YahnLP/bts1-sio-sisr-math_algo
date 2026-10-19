# Formulaire

Tous les aide-mémoire du cours réunis sur une seule page, dans l'ordre des séances. Utilise la recherche ou le sommaire à droite pour retrouver une formule.

> [!NOTE]
> Chaque formule a été vérifiée par le calcul sur des exemples. Pour l'épreuve, vérifie dans le sujet ce qui est rappelé et ce qui est à connaître.

## S01 · Numération : bases 2, 10 et 16

### Définition

\[
N = (a_k \dots a_1 a_0)_b = \sum_{i=0}^{k} a_i\, b^i , \qquad 0 \le a_i \le b-1 .
\]

### Méthodes

| Je veux… | Méthode |
|---|---|
| \(b \to 10\) | Somme pondérée des chiffres par les puissances de \(b\) |
| \(10 \to b\) | Divisions successives par \(b\) ; **restes lus de bas en haut** |
| \(2 \to 16\) | Groupes de **4 bits** à partir de la droite |
| \(16 \to 2\) | Chaque chiffre hexa donne **4 bits** |

### Hexadécimal

| A | B | C | D | E | F |
|---|---|---|---|---|---|
| 10 | 11 | 12 | 13 | 14 | 15 |

### Nombre de valeurs

- \(n\) bits : \(2^n\) valeurs, de 0 à \(2^n - 1\).
- 1 octet = 8 bits : 0 à 255.
- Nombre de bits pour écrire \(N \ge 1\) : le plus petit \(n\) tel que \(N < 2^n\).

### Puissances de 2

| \(k\) | \(2^k\) |
|---|---|
| 0 | 1 |
| 1 | 2 |
| 2 | 4 |
| 3 | 8 |
| 4 | 16 |
| 5 | 32 |
| 6 | 64 |
| 7 | 128 |
| 8 | 256 |
| 9 | 512 |
| 10 | 1024 |
| 11 | 2048 |
| 12 | 4096 |
| 13 | 8192 |
| 14 | 16384 |
| 15 | 32768 |
| 16 | 65536 |

### Adresses

| Objet | Taille | Écriture |
|---|---|---|
| IPv4 | 32 bits (4 octets) | 4 nombres décimaux de 0 à 255 séparés par des points |
| MAC | 48 bits (6 octets) | 12 chiffres hexadécimaux |
| Couleur web | 24 bits (3 octets) | `#RRGGBB` |

### Python

```python
bin(205)           # '0b11001101'
hex(205)           # '0xcd'
int("11001101", 2) # 205
int("CD", 16)      # 205
```

## S02 · Réels, arrondis et calcul en binaire

### Partie fractionnaire

\[
(a_k \dots a_0 , a_{-1} \dots a_{-m})_2 = \sum_{i=-m}^{k} a_i\, 2^i .
\]

| Je veux… | Méthode |
|---|---|
| Fraction binaire → décimal | Somme des \(a_i \times 2^{i}\) (poids \(\frac12, \frac14, \frac18, \dots\)) |
| Partie fractionnaire décimal → binaire | **× 2** répété ; chiffres = parties entières, lus de haut en bas |
| Fini en binaire ? | Fraction irréductible \(\frac{k}{2^m}\) |

### Erreur avec \(p\) chiffres binaires après la virgule

| Méthode | Erreur |
|---|---|
| Troncature | \(< 2^{-p}\) |
| Arrondi | \(\le 2^{-(p+1)}\) |

### Opérations binaires

| Opération | Règle |
|---|---|
| \(1 + 1\) | \(10\) : on pose 0, retenue 1 |
| \(1 + 1 + 1\) | \(11\) |
| \(\times\, 2^k\) | Décaler de \(k\) rangs à gauche (`x << k`) |
| \(\div\, 2^k\) | Quotient = `x >> k` ; reste = `x & (2**k - 1)` |
| Sur \(n\) bits | Résultat modulo \(2^n\) ; débordement si la somme est \(> 2^n - 1\) |

### Unités

| Décimal (SI) | Binaire (CEI) |
|---|---|
| 1 ko = \(10^3\) o | 1 Kio = \(2^{10}\) o = 1 024 o |
| 1 Mo = \(10^6\) o | 1 Mio = \(2^{20}\) o |
| 1 Go = \(10^9\) o | 1 Gio = \(2^{30}\) o |
| 1 To = \(10^{12}\) o | 1 Tio = \(2^{40}\) o |

- 1 octet = 8 bits ; débit en bit/s ; durée \(= \dfrac{\text{octets} \times 8}{\text{débit en bit/s}}\).

### Python

```python
0.1 + 0.2 == 0.3          # False : ne pas comparer des float avec ==
abs(a - b) < 1e-9         # comparaison à une tolérance
from fractions import Fraction   # calcul exact
x << 3                    # x * 8
x >> 2                    # x // 4
```

## S03 · Algorithmique : données et conditions

### En-tête d'un algorithme

```text
ALGORITHME nom
  RÔLE      : ...
  ENTRÉE(S) : ... (type)
  SORTIE    : ... (type)
  VARIABLES : ... (type)
DÉBUT
  ...
FIN
```

### Types et opérateurs

| Type | Python | Exemple |
|---|---|---|
| Entier | `int` | `42` |
| Réel | `float` | `3.14` |
| Booléen | `bool` | `True` |
| Chaîne | `str` | `"192.168.1.10"` |

| Opération | Python |
|---|---|
| Quotient / reste (division euclidienne) | `a // b`, `a % b` |
| Puissance | `a ** b` |
| Égalité / différence | `==`, `!=` |
| Non, et, ou | `not`, `and`, `or` |
| Et, ou, ou exclusif bit à bit | `&`, `|`, `^` |
| Décalages | `<<`, `>>` |

### Masques

| Je veux… | Expression |
|---|---|
| Tester un bit | `(x & m) != 0` |
| Mettre à 1 | `x | m` |
| Mettre à 0 | `x & ~m` |
| Changer d'état | `x ^ m` |

### Conditionnelle

```python
if condition_1:
    ...
elif condition_2:
    ...
else:
    ...
```

Le premier test vrai l'emporte : **le plus particulier d'abord**.

### Méthode de test

1. Choisir un jeu d'essai (cas typiques et cas limites).
2. Calculer les résultats attendus **sans** passer par l'algorithme.
3. Dérouler l'algorithme (trace) et comparer.

## S04 · Algorithmique : itérations

### Les trois boucles

| Structure | Pseudo-code | Python | Test |
|---|---|---|---|
| Déterministe | `POUR i DE a À b` | `for i in range(a, b + 1):` | Nombre de tours connu |
| Tant que | `TANT QUE cond` | `while cond:` | Avant le tour |
| Répéter | `RÉPÉTER … JUSQU'À cond` | `while True: … if cond: break` | Après le tour |

`range(n)` : \(0 \dots n-1\) ; `range(a, b)` : \(a \dots b-1\) ; `range(a, b, p)` : de \(p\) en \(p\).

### Méthode

1. Initialiser. 2. Condition de continuation. 3. Mettre à jour (se rapprocher de la fin). 4. Justifier la terminaison par un **variant** (entier qui décroît strictement). 5. Traiter après la boucle.

### Schémas

| Besoin | Initialisation | Corps |
|---|---|---|
| Somme | `s = 0` | `s += x` |
| Produit | `p = 1` | `p *= x` |
| Comptage | `c = 0` | `if cond: c += 1` |
| Maximum | `m = L[0]` | `if x > m: m = x` |
| Chiffres | — | `n % 10` (dernier), `n // 10` (reste) |
| Base \(b\) | `texte = ""` | `texte = chiffre(n % b) + texte` ; `n //= b` |

### Vérifier

- Trace sur un petit cas, puis cas limites (0 tour, 1 tour).
- Éviter `≠` dans une condition d'arrêt si on n'est pas sûr de tomber pile.
- Au plus **deux niveaux** d'imbrication.

### Sommes à connaître

\[
1 + 2 + \dots + n = \frac{n(n+1)}{2} , \qquad (n-1) + \dots + 1 = \frac{n(n-1)}{2} .
\]

## S05 · Division euclidienne et PGCD

### Division euclidienne

\[
a = b\,q + r , \qquad 0 \le r < b , \qquad (q, r) \text{ unique} .
\]

`q = a // b` et `r = a % b` en Python (avec \(b > 0\)). \(b \mid a \iff r = 0\).

### Critères de divisibilité

| Par | Critère |
|---|---|
| 2 | dernier chiffre pair |
| 3 | somme des chiffres divisible par 3 |
| 4 | deux derniers chiffres divisibles par 4 |
| 5 | dernier chiffre 0 ou 5 |
| 9 | somme des chiffres divisible par 9 |
| 10 | dernier chiffre 0 |

### PGCD et PPCM

\[
\operatorname{PGCD}(a, b) = \operatorname{PGCD}(b, r) , \qquad \operatorname{PGCD}(a, 0) = a , \qquad \operatorname{PGCD} \times \operatorname{PPCM} = a \times b .
\]

```python
def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
```

- Le **dernier reste non nul** est le PGCD.
- **Premiers entre eux** : \(\operatorname{PGCD} = 1\).
- Variant : la suite des restes, strictement décroissante.

## S06 · Nombres premiers

### Définitions

- **Premier** : \(p \ge 2\) avec exactement deux diviseurs positifs (1 et \(p\)). 1 n'est pas premier ; 2 est le seul premier pair.
- Premiers \(< 50\) : 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47.

### Tester la primalité

Tester les diviseurs \(d\) avec \(2 \le d \le \sqrt{n}\) (condition `d * d <= n`).

### Décomposition

\[
n = p_1^{e_1} p_2^{e_2} \cdots p_k^{e_k} \quad (\text{unique}) .
\]

| Je veux… | Formule |
|---|---|
| Nombre de diviseurs | \((e_1 + 1)(e_2 + 1) \cdots (e_k + 1)\) |
| PGCD | chaque premier avec l'exposant **minimum** |
| PPCM | chaque premier avec l'exposant **maximum** |
| Relation | \(\operatorname{PGCD} \times \operatorname{PPCM} = a \times b\) |

### Crible d'Ératosthène

Écrire 2 à \(N\) ; pour \(p\) premier avec \(p^2 \le N\), barrer ses multiples à partir de \(p^2\).

### Exemples à connaître

\[
360 = 2^3 \times 3^2 \times 5 , \quad 1\,001 = 7 \times 11 \times 13 , \quad 2\,024 = 2^3 \times 11 \times 23 , \quad 5\,040 = 2^4 \times 3^2 \times 5 \times 7 .
\]

### Piège

Un nombre qui « a l'air premier » (91 = 7 × 13, 121 = 11²) peut être composé : on teste jusqu'à \(\sqrt{n}\).

## S07 · Congruences

### Définition

\[
a \equiv b \pmod n \iff n \mid (a - b) \iff \text{même reste dans la division par } n .
\]

### Calculs

Compatible avec \(+\), \(-\), \(\times\) et les puissances : **on réduit à chaque étape**. Pas de simplification automatique.

### Inverse modulo \(n\)

- \(a\) a un inverse modulo \(n\) ⟺ \(\operatorname{PGCD}(a, n) = 1\).
- Résoudre \(a x \equiv c\) : \(x \equiv a' c\) où \(a' a \equiv 1\).
- Inverses modulo 26 : 1→1, 3→9, 5→21, 7→15, 9→3, 11→19, 15→7, 17→23, 19→11, 21→5, 23→17, 25→25.

### Applications

| Application | Formule |
|---|---|
| César | \(y \equiv x + s \pmod{26}\) |
| Affine | \(y \equiv a x + b \pmod{26}\), \(\operatorname{PGCD}(a, 26) = 1\) ; \(x \equiv a'(y - b)\) |
| NIR | clé \(= 97 - (N \bmod 97)\) |
| ISBN-13 | \(\sum\) poids (1, 3, …) × chiffre \(\equiv 0 \pmod{10}\) |
| IBAN | nombre réarrangé \(\equiv 1 \pmod{97}\) |
| Hachage | case \(= x \bmod m\) |
| Liste circulaire (taille \(n\), saut \(k\)) | tout est visité ⟺ \(\operatorname{PGCD}(k, n) = 1\) |

### Python

```python
a % n              # reste (entre 0 et n-1 pour n > 0)
pow(a, k, n)       # a**k modulo n
pow(a, -1, n)      # inverse modulo n (Python 3.8 et plus), erreur s'il n'existe pas
```

## S08 · Calcul des propositions

### Connecteurs

| Connecteur | Notation | Python |
|---|---|---|
| Négation | \(\neg p\) | `not p` |
| Et | \(p \wedge q\) | `p and q` |
| Ou (inclusif) | \(p \vee q\) | `p or q` |
| Implication | \(p \Rightarrow q\) | `(not p) or q` |
| Équivalence | \(p \Leftrightarrow q\) | `p == q` |
| Ou exclusif | \(p \oplus q\) | `p != q` |

\(p \Rightarrow q\) est **fausse** seulement pour \(p\) vrai et \(q\) faux.

### Équivalences

| | |
|---|---|
| De Morgan | \(\neg(p \wedge q) \equiv \neg p \vee \neg q\) ; \(\neg(p \vee q) \equiv \neg p \wedge \neg q\) |
| Implication | \(p \Rightarrow q \equiv \neg p \vee q\) |
| Contraposée | \(p \Rightarrow q \equiv \neg q \Rightarrow \neg p\) |
| Négation de l'implication | \(\neg(p \Rightarrow q) \equiv p \wedge \neg q\) |
| Réciproque | \(q \Rightarrow p\) : **pas** équivalente |
| Équivalence | \(p \Leftrightarrow q \equiv (p \Rightarrow q) \wedge (q \Rightarrow p)\) |

### Méthode

1. Lister les \(2^n\) combinaisons.
2. Calculer colonne par colonne, des petites expressions aux grandes.
3. Comparer les colonnes : mêmes valeurs ⟹ expressions **équivalentes** ; colonne toute V ⟹ **tautologie**.

### Négation d'une condition

Appliquer De Morgan (\(\wedge \leftrightarrow \vee\)) puis nier chaque test : \(<\) ↔ \(\ge\), \(>\) ↔ \(\le\), \(=\) ↔ \(\ne\).

### Priorités

\(\neg\) avant \(\wedge\) avant \(\vee\) avant \(\Rightarrow\) avant \(\Leftrightarrow\) ; en cas de doute, **parenthéser**.

## S09 · Prédicats et ensembles

### Quantificateurs

| Notation | Lecture | Négation |
|---|---|---|
| \(\forall x,\ P(x)\) | pour tout \(x\), \(P(x)\) | \(\exists x,\ \neg P(x)\) |
| \(\exists x,\ P(x)\) | il existe \(x\) tel que \(P(x)\) | \(\forall x,\ \neg P(x)\) |

- Pour nier : on **échange** \(\forall\) et \(\exists\), puis on nie le prédicat.
- \(\forall x\, \exists y\) n'est **pas** équivalent à \(\exists y\, \forall x\) : l'ordre compte.
- Un exemple ne prouve jamais un « pour tout » ; un contre-exemple le réfute.

### Ensembles

| Notation | Sens | Python |
|---|---|---|
| \(x \in A\) | \(x\) appartient à \(A\) | `x in A` |
| \(A \subseteq B\) | inclusion | `A <= B` |
| \(A \cap B\) | intersection | `A & B` |
| \(A \cup B\) | réunion | `A | B` |
| \(A \setminus B\) | différence | `A - B` |
| \(A \,\Delta\, B\) | différence symétrique | `A ^ B` |
| \(\overline{A}\) | complémentaire | `E - A` |
| \(\lvert A \rvert\) | cardinal | `len(A)` |

- \(\lvert \mathcal{P}(A) \rvert = 2^{\lvert A \rvert}\).
- \(\lvert A \cup B \rvert = \lvert A \rvert + \lvert B \rvert - \lvert A \cap B \rvert\).
- Une partie d'un ensemble à \(n\) éléments se code par un nombre de \(n\) bits (masque).

## S10 · Algèbre de Boole

### Opérations et propriétés

| Opération | Notation | Python |
|---|---|---|
| NON | \(\overline{a}\) | `1 - a` |
| ET | \(a \cdot b\) | `a & b` |
| OU | \(a + b\) | `a | b` |
| OU exclusif | \(a \oplus b\) | `a ^ b` |

- \(1 + 1 = 1\). Priorité : NON, puis ET, puis OU.
- Absorption : \(a + a\,b = a\) ; \(a\,(a + b) = a\).
- Distributivité dans les deux sens : \(a + b\,c = (a + b)(a + c)\).
- De Morgan : \(\overline{a + b} = \overline{a}\,\overline{b}\) ; \(\overline{a\,b} = \overline{a} + \overline{b}\).
- \(a + \overline{a}\,b = a + b\).

### Karnaugh (3 variables)

- Lignes : \(a = 0, 1\) ; colonnes : \(bc = 00, 01, 11, 10\).
- Rectangles de 1, 2, 4 ou 8 cases ; tableau circulaire ; le moins de rectangles, les plus grands.
- On garde les variables qui ne changent pas dans le rectangle.

### NAND et NOR

- \(\overline{a} = \text{NAND}(a,a)\) ; \(a\,b = \text{NAND}(n, n)\) avec \(n = \text{NAND}(a,b)\) ; \(a + b = \text{NAND}(\text{NAND}(a,a), \text{NAND}(b,b))\).

### Additionneur

- Demi : \(s = a \oplus b\), \(r = a\,b\).
- Complet : \(s = a \oplus b \oplus c\), \(r = a\,b + c\,(a \oplus b)\).

### Adressage IPv4

- Réseau = adresse **ET** masque. Diffusion = réseau **OU** (NON masque).
- Machines utilisables : \(2^{32 - n} - 2\).

## S11 · Relations et applications

### Vocabulaire

| Notion | Définition | Python |
|---|---|---|
| Produit \(A \times B\) | couples \((a, b)\) ; \(\lvert A \rvert \cdot \lvert B \rvert\) éléments | `{(x, y) for x in a for y in b}` |
| Relation sur \(E\) | partie de \(E \times E\) | ensemble de couples |
| Réflexive | \(x\,\mathcal{R}\,x\) pour tout \(x\) | `(x, x) in r` |
| Symétrique | \(x\,\mathcal{R}\,y \Rightarrow y\,\mathcal{R}\,x\) | `(y, x) in r` |
| Antisymétrique | \(x\,\mathcal{R}\,y\) et \(y\,\mathcal{R}\,x\) \(\Rightarrow x = y\) | |
| Transitive | \(x\,\mathcal{R}\,y\) et \(y\,\mathcal{R}\,z\) \(\Rightarrow x\,\mathcal{R}\,z\) | |

- **Équivalence** = réflexive + symétrique + transitive → classes qui partitionnent \(E\).
- **Ordre** = réflexive + antisymétrique + transitive ; total si tout couple est comparable.

### Applications

| Propriété | Test |
|---|---|
| Application | chaque \(x\) de \(A\) a **une seule** image |
| Injective | images toutes différentes |
| Surjective | tout élément de \(B\) est atteint |
| Bijective | injective et surjective ; réciproque \(f^{-1}\) |

- Composée : \((g \circ f)(x) = g(f(x))\) ; on applique \(f\) en premier ; non commutative.
- Image directe \(f(X)\) ; image réciproque \(f^{-1}(Y)\) (existe toujours).
- Nombre d'applications de \(A\) vers \(B\) : \(\lvert B \rvert^{\lvert A \rvert}\).
- Ensembles finis de même taille : injective \(\iff\) surjective \(\iff\) bijective.

## S12 · Fonctions, tableaux et chaînes

### Fonctions

```python
def nom(parametres):
    ...
    return resultat
```

- `return` renvoie une valeur ; `print` l'affiche seulement.
- Variable créée dans la fonction = **locale**.
- Une liste passée en paramètre peut être modifiée par la fonction ; `list(t)` en fait une copie.

### Tableaux et chaînes

| | Tableau (liste) | Chaîne |
|---|---|---|
| Indices | 0 à \(n-1\) | 0 à \(n-1\) |
| Longueur | `len(t)` | `len(s)` |
| Dernier | `t[-1]` | `s[-1]` |
| Tranche | `t[a:b]` (exclut `b`) | `s[a:b]` |
| Modifiable | oui | **non** |
| Grille | `g[ligne][colonne]` | |

- `s.split()` découpe sur les espaces ; `"-".join(liste)` assemble.
- Parcourir un tableau : `for i in range(len(t))` (indice) ou `for x in t` (valeur).

### Algorithmes

| Algorithme | Coût |
|---|---|
| Maximum / recherche séquentielle | \(n - 1\) comparaisons / jusqu'à \(n\) |
| Tri par sélection | \(\dfrac{n(n-1)}{2}\) comparaisons |
| Dichotomie (tableau trié) | au plus \(\lfloor \log_2 n \rfloor + 1\) étapes |

## S13 · Matrices : opérations

### Matrices

- Taille \(m \times n\) : \(m\) lignes, \(n\) colonnes ; \(a_{ij}\) : ligne \(i\), colonne \(j\).
- **Somme** : même taille, coefficient par coefficient. **Produit par \(k\)** : chaque coefficient.
- **Produit** \(AB\) : \((m \times n)(n \times p) = m \times p\) ;
  \(c_{ij} = \sum_{k} a_{ik}\,b_{kj}\).
- \(AB \neq BA\) en général ; \(AB = 0\) n'implique pas \(A = 0\) ou \(B = 0\).
- \((AB)C = A(BC)\) ; \(A(B + C) = AB + AC\) ; \(AI = IA = A\).
- \(A^n\) : seulement pour une matrice carrée ; \(A^0 = I\).

| Exemple | Résultat |
|---|---|
| Diagonale | \(\begin{pmatrix} a & 0 \\ 0 & b \end{pmatrix}^n = \begin{pmatrix} a^n & 0 \\ 0 & b^n \end{pmatrix}\) |
| Fibonacci | \(\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}^n = \begin{pmatrix} F_{n+1} & F_n \\ F_n & F_{n-1} \end{pmatrix}\) |

### Python

```python
a = [[1, 2], [3, 4]]   # a[i][j]
```

## S14 · Inverse et systèmes

### Inverse

- \(A\) carrée est inversible s'il existe \(A^{-1}\) avec \(A A^{-1} = A^{-1} A = I\).
- Vérification : calculer le produit.

### Système \(AX = B\)

- Si \(A\) est inversible : \(X = A^{-1}B\) (produit **à gauche**), solution unique.
- Sinon : aucune solution ou une infinité.

### Méthode des lignes

Partir de \([A \mid I]\), arriver à \([I \mid A^{-1}]\).

| Opération | Notation |
|---|---|
| Multiplier une ligne par \(k \neq 0\) | \(L_i \leftarrow k\,L_i\) |
| Ajouter un multiple d'une ligne | \(L_i \leftarrow L_i + k\,L_j\) |
| Échanger deux lignes | \(L_i \leftrightarrow L_j\) |

Pour chaque colonne : pivot **1** sur la diagonale, puis **0** ailleurs. Une ligne de zéros à gauche : non inversible.

### Python

```python
from fractions import Fraction
Fraction(1, 3) + Fraction(1, 6)   # Fraction(1, 2), exact
```

## S15 · Validation et contrôle de données

### Valider un format

1. Écrire **toutes** les règles ; 2. un test par règle ; 3. `return False` dès qu'une règle est violée ; 4. `return True` à la fin.

| Donnée | Règles |
|---|---|
| Octet décimal | non vide, chiffres seuls, pas de zéro initial (sauf `"0"`), valeur de 0 à 255 |
| Adresse IPv4 | `s.split(".")` : 4 morceaux, chacun est un octet valide |
| Adresse MAC | `s.split(":")` : 6 groupes de 2 chiffres hexadécimaux |
| Octet de masque | 0, 128, 192, 224, 240, 248, 252, 254, 255 |

Cas limites : chaîne vide, 0, 255, 256, caractère interdit, morceau en trop ou en moins.

### Parité

- Parité paire : bit \(= (\text{nombre de 1}) \bmod 2\) ; le mot transmis a un nombre pair de 1.
- Détecte un nombre **impair** d'erreurs ; ne localise pas ; ne voit pas deux erreurs.
- Deux dimensions : ligne fausse **et** colonne fausse = bit à corriger.

### Sommes de contrôle

```python
c = (-sum(octets)) % 256          # somme de contrôle
ok = (sum(octets) + c) % 256 == 0 # vérification
r = 0
for o in octets:
    r = r ^ o                     # OU exclusif de contrôle
```

- Deux erreurs qui se compensent ne sont pas détectées.
- Un contrôle détecte des erreurs, il ne protège pas contre une modification volontaire.

## S16 · Graphes

### Vocabulaire

| Terme | Sens |
|---|---|
| Arc \(x \to y\) | flèche de \(x\) vers \(y\) |
| Chemin, longueur | suite d'arcs ; nombre d'arcs |
| Circuit | chemin fermé (longueur \(\ge 1\)) ; boucle = circuit de longueur 1 |
| Hamiltonien | chemin passant une fois par chaque sommet |
| \(d^+(x)\), \(d^-(x)\) | arcs qui partent de / arrivent en \(x\) |

### Matrice d'adjacence

- \(m_{ij} = 1\) si \(i \to j\). Somme d'une **ligne** = \(d^+\) ; d'une **colonne** = \(d^-\).
- \((M^p)_{ij}\) = nombre de chemins de longueur \(p\) de \(i\) à \(j\).
- Sans circuit (\(n\) sommets) : \(M^n = 0\). Avec circuit : jamais nulle.

### Fermeture transitive

\(M^* = M + M^{[2]} + \dots + M^{[n-1]}\) (somme et produit **booléens**) : \(M^*_{ij} = 1\) s'il existe un chemin de \(i\) à \(j\).

### Niveaux (sans circuit)

1. Niveau 0 : sommets sans prédécesseur. 2. Les retirer. 3. Recommencer. Aucun sommet sans prédécesseur alors qu'il en reste : circuit.

## S17 · Chemin optimal et MPM

### Dijkstra (valeurs ≥ 0)

1. \(S\) à 0, les autres à \(\infty\). 2. Fixer le sommet non fixé de plus petite valeur. 3. Mettre à jour ses successeurs (valeur + arc plus petite ?) et noter le prédécesseur. 4. Recommencer ; lire le chemin à l'envers.

### MPM

| | Formule |
|---|---|
| Date au plus tôt | \(t(x) = \max_p \bigl(t(p) + d(p)\bigr)\), \(t(\text{Début}) = 0\) |
| Durée du projet | \(t(\text{Fin})\) |
| Date au plus tard | \(T(x) = \min_s T(s) - d(x)\), \(T(\text{Fin}) = t(\text{Fin})\) |
| Marge totale | \(M_T = T - t\) |
| Marge libre | \(M_L = \min_s t(s) - t(x) - d(x)\) |
| Marge certaine | \(M_C = \max\bigl(0, \min_s t(s) - \max_p (T(p) + d(p)) - d(x)\bigr)\) |

- \(M_C \le M_L \le M_T\).
- Tâche critique : \(M_T = 0\) ; chemin critique = plus long chemin = durée du projet.
- Retard d'une tâche non critique : sans effet tant qu'il reste dans \(M_T\).

## S18 · Écrire, tester et déboguer

### De l'énoncé au programme

1. Entrées, sortie. 2. Exemple à la main. 3. Schéma. 4. Pseudo-code, puis Python. 5. Tests.

| Schéma | Initialisation | Remarque |
|---|---|---|
| Compteur | `n = 0` | `n = n + 1` dans le `if` |
| Accumulateur | `s = 0` | `s = s + x` |
| Recherche avec arrêt | `return -1` **après** la boucle | `return i` dans la boucle |
| Maximum | `m = t[0]` | liste non vide ; `>` strict = première apparition |
| Série consécutive | `courante = 0`, `meilleure = 0` | mise à jour de `meilleure` dans la boucle |

### Jeux de tests

Cas normal, vide, un élément, valeurs égales ou à la frontière, toujours vrai, jamais vrai, début et fin.

### Suivi de variables

Une ligne par tour, une colonne par variable ; chercher le **premier** écart avec ce qui est attendu.

### Erreurs classiques

| Erreur | Réflexe |
|---|---|
| Indice hors domaine | indices de 0 à \(n - 1\) ; `range(len(t))` |
| Parcours qui oublie le début | `range(len(t))`, pas `range(1, len(t))` |
| Mauvaise initialisation | `m = t[0]` pour un maximum |
| Arrêt trop tôt | `return False` dans la boucle, `return True` après |
| Boucle infinie | le variant doit changer à chaque tour |
| Égalité de flottants | tolérance, entiers ou `Fraction` |
| Division entière | multiplier avant de diviser, ou `/` |
| Effet de bord | `list(l)` pour travailler sur une copie |

## S19 · Préparer l'épreuve E3

### Format E3

- Écrit de **2 h**, **20 points**, coefficient **3**, 2 ou 3 exercices dont **un de programmation (Python)** ; évaluation terminale.
- Vérifier chaque session le document en vigueur (moyens de calcul autorisés).

### Réponse complète

1. **Méthode** annoncée ; 2. **calcul** détaillé ; 3. **résultat** avec unité et phrase de conclusion ; 4. **vérification**.

### Formulaire de synthèse

| Domaine | À retenir |
|---|---|
| Numération | \(n = \sum a_k b^k\) ; divisions successives ; groupes de 4 bits = 1 chiffre hexadécimal |
| Division euclidienne | \(a = bq + r\), \(0 \le r < b\) ; PGCD = dernier reste non nul ; \(\text{PGCD} \times \text{PPCM} = a\,b\) |
| Congruences | \(a \equiv b \pmod n\) ; inverse de \(a\) modulo \(n\) si \(\text{PGCD}(a, n) = 1\) |
| Logique | \(\neg(p \wedge q) \equiv \neg p \vee \neg q\) ; \(\neg(p \Rightarrow q) \equiv p \wedge \neg q\) ; \(\neg \forall \equiv \exists \neg\) |
| Boole | absorption \(a + ab = a\) ; \(a + \overline{a}b = a + b\) ; Karnaugh : 1, 2, 4, 8 cases |
| Adressage | réseau = IP ET masque ; machines \(2^{32-n} - 2\) |
| Matrices | \((m \times n)(n \times p)\) ; \(X = A^{-1}B\) ; méthode des lignes \([A \mid I] \to [I \mid A^{-1}]\) |
| Contrôle de données | parité paire : bit \(= (\text{nombre de 1}) \bmod 2\) ; somme de contrôle \(c = (-\sum o_i) \bmod 256\) |
| Graphes | \((M^p)_{ij}\) = chemins de longueur \(p\) ; niveaux ; Dijkstra ; MPM \(t, T\), marges |
| Algorithmique | indices de 0 à \(n - 1\) ; cas limites (vide, un élément) ; `return False` dans la boucle, `return True` après |


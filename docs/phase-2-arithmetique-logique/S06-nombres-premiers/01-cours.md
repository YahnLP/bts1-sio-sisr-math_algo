# Cours – Nombres premiers et décomposition en facteurs premiers

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S06 – à lire avant les [exercices](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** S05 (divisibilité, PGCD).
> - **Outils :** Papier, calculatrice, éditeur Python intégré au site

## À la fin de ce cours tu sauras

- [ ] **Définir** un nombre premier et **justifier** qu'il suffit de tester les diviseurs jusqu'à \(\sqrt{n}\) ;
- [ ] **Dresser** la liste des nombres premiers jusqu'à \(N\) par le crible d'Ératosthène ;
- [ ] **Décomposer** un entier en produit de facteurs premiers ;
- [ ] **En déduire** le PGCD, le PPCM et le nombre de diviseurs ;
- [ ] **Programmer** un test de primalité et une décomposition.

## I. Nombres premiers

Un entier \(p \ge 2\) est **premier** si ses seuls diviseurs positifs sont 1 et \(p\). Un entier \(n \ge 2\) qui n'est pas premier est dit **composé**. Par convention, 1 n'est pas premier.

Les nombres premiers inférieurs à 50 sont : 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47 (15 nombres). Il y en a 25 inférieurs à 100. Le seul nombre premier pair est 2.

## II. Tester si un entier est premier

**Propriété.** Si \(n\) est composé, alors \(n\) possède un diviseur \(d\) tel que \(2 \le d \le \sqrt{n}\).

*Justification.* Si \(n = a \times b\) avec \(2 \le a \le b\), alors \(a^2 \le a b = n\), donc \(a \le \sqrt{n}\).

**Conséquence.** Pour savoir si \(n\) est premier, il suffit de chercher un diviseur entre 2 et \(\lfloor \sqrt{n} \rfloor\). Si on n'en trouve pas, \(n\) est premier.

**Exemple : 91.** \(\sqrt{91} \approx 9.54\). On teste 2, 3, 5 : aucun ne divise 91. Puis \(7\) : \(91 = 7 \times 13\). Donc 91 n'est **pas** premier (il ressemble pourtant à un nombre premier).

**Exemple : 97.** \(\sqrt{97} \approx 9.85\), on teste les entiers de 2 à 9 (tester les nombres premiers 2, 3, 5, 7 suffit) : 97 = 2 × 48 + 1; 97 = 3 × 32 + 1; 97 = 5 × 19 + 2; 97 = 7 × 13 + 6. Aucun reste nul : **97 est premier**.

```text
ALGORITHME est_premier
  RÔLE      : dire si un entier est premier
  ENTRÉE    : n (entier)
  SORTIE    : un booléen
  VARIABLES : d (entier)
DÉBUT
  SI n < 2 ALORS RETOURNER faux
  d ← 2
  TANT QUE d × d ≤ n FAIRE
    SI n mod d = 0 ALORS RETOURNER faux
    d ← d + 1
  FIN TANT QUE
  RETOURNER vrai
FIN
```

Le nombre de divisions est au plus \(\sqrt{n}\) : pour \(n\) de l'ordre de \(10^{12}\), jusqu'à \(10^6\) divisions.

## III. Le crible d'Ératosthène

Pour obtenir **tous** les nombres premiers jusqu'à \(N\) :

1. écrire les entiers de 2 à \(N\) ;
2. prendre le plus petit nombre non barré \(p\) (il est premier) et **barrer ses multiples** à partir de \(p^2\) ;
3. recommencer tant que \(p^2 \le N\) ; les nombres non barrés sont les nombres premiers.

Pour \(N = 100\), il suffit de traiter 2, 3, 5, 7 (car \(11^2 = 121 > 100\)).

| | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **2** | **3** | ~~4~~ | **5** | ~~6~~ | **7** | ~~8~~ | ~~9~~ | ~~10~~ |
| **11** | ~~12~~ | **13** | ~~14~~ | ~~15~~ | ~~16~~ | **17** | ~~18~~ | **19** | ~~20~~ |
| ~~21~~ | ~~22~~ | **23** | ~~24~~ | ~~25~~ | ~~26~~ | ~~27~~ | ~~28~~ | **29** | ~~30~~ |
| **31** | ~~32~~ | ~~33~~ | ~~34~~ | ~~35~~ | ~~36~~ | **37** | ~~38~~ | ~~39~~ | ~~40~~ |
| **41** | ~~42~~ | **43** | ~~44~~ | ~~45~~ | ~~46~~ | **47** | ~~48~~ | ~~49~~ | ~~50~~ |
| ~~51~~ | ~~52~~ | **53** | ~~54~~ | ~~55~~ | ~~56~~ | ~~57~~ | ~~58~~ | **59** | ~~60~~ |
| **61** | ~~62~~ | ~~63~~ | ~~64~~ | ~~65~~ | ~~66~~ | **67** | ~~68~~ | ~~69~~ | ~~70~~ |
| **71** | ~~72~~ | **73** | ~~74~~ | ~~75~~ | ~~76~~ | ~~77~~ | ~~78~~ | **79** | ~~80~~ |
| ~~81~~ | ~~82~~ | **83** | ~~84~~ | ~~85~~ | ~~86~~ | ~~87~~ | ~~88~~ | **89** | ~~90~~ |
| ~~91~~ | ~~92~~ | ~~93~~ | ~~94~~ | ~~95~~ | ~~96~~ | **97** | ~~98~~ | ~~99~~ | ~~100~~ |

(Les nombres premiers sont en gras, les nombres barrés sont composés.)

## IV. Décomposition en facteurs premiers

**Théorème fondamental de l'arithmétique.** Tout entier \(n \ge 2\) s'écrit comme un produit de nombres premiers, et cette écriture est **unique** à l'ordre des facteurs près. (L'existence se montre en prenant le plus petit diviseur supérieur à 1 ; l'unicité est admise ici.)

C'est la raison pour laquelle 1 n'est pas premier : \(6 = 2 \times 3 = 1 \times 2 \times 3\) n'aurait plus de décomposition unique.

**Méthode.** On divise par le plus petit nombre premier possible, puis on recommence avec le quotient.

Pour 360 :

| Nombre | Plus petit diviseur premier | Quotient |
|---|---|---|
| 360 | 2 | 180 |
| 180 | 2 | 90 |
| 90 | 2 | 45 |
| 45 | 3 | 15 |
| 15 | 3 | 5 |
| 5 | 5 | 1 |

Donc \(360 = 2^{3} \times 3^{2} \times 5\). Autres exemples : \(1001 = 7 \times 11 \times 13\) ; \(2024 = 2^{3} \times 11 \times 23\) ; \(5040 = 2^{4} \times 3^{2} \times 5 \times 7\).

## V. Ce que donne la décomposition

Soit \(n = p_1^{e_1} \times p_2^{e_2} \times \dots \times p_k^{e_k}\).

- **Diviseurs.** Les diviseurs de \(n\) sont les produits \(p_1^{f_1} \dots p_k^{f_k}\) avec \(0 \le f_i \le e_i\). Il y en a **\((e_1 + 1)(e_2 + 1) \cdots (e_k + 1)\)**. Pour 360 : \((3+1) \times (2+1) \times (1+1) = 24\) diviseurs (les listes de S05 le confirment).
- **PGCD.** On prend chaque premier avec le **plus petit** exposant. **PPCM** : chaque premier avec le **plus grand** exposant.

Pour \(360\) et \(756\) :

| Premier \(p\) | exposant dans 360 | exposant dans 756 | min | max |
|---|---|---|---|---|
| 2 | 3 | 2 | 2 | 3 |
| 3 | 2 | 3 | 2 | 3 |
| 5 | 1 | 0 | 0 | 1 |
| 7 | 0 | 1 | 0 | 1 |

\(\operatorname{PGCD}(360, 756) = 2^{2} \times 3^{2} = 36\) et \(\operatorname{PPCM}(360, 756) = 2^{3} \times 3^{3} \times 5^{1} \times 7^{1} = 7 560\).

Contrôle de la relation de S05 : \(360 \times 756 = 272 160\) et \(36 \times 7 560 = 272 160\). Elle vient de \(\min(e, f) + \max(e, f) = e + f\).

## VI. Il y a une infinité de nombres premiers

*Preuve (Euclide).* Supposons qu'il n'y ait qu'un nombre fini de nombres premiers \(p_1, \dots, p_k\). Posons \(N = p_1 p_2 \cdots p_k + 1\). Aucun \(p_i\) ne divise \(N\) (le reste de la division est 1). Pourtant \(N \ge 2\) a au moins un diviseur premier : contradiction.

## VII. À quoi cela sert-il ?

- **Cryptographie à clé publique.** Multiplier deux grands nombres premiers est facile ; retrouver les deux facteurs à partir du produit est très long. Un exemple d'école : \(3233 = 53 \times 61\). Avec des nombres de plusieurs centaines de chiffres, on ne connaît pas d'algorithme classique qui factorise en un temps raisonnable (S07 présente les congruences, qui servent à la cryptographie).
- **Tables de hachage.** On choisit souvent un nombre premier comme taille de table pour mieux répartir les clés (S07).
- **Parcours cyclique.** Parcourir une liste de taille \(n\) par sauts de \(k\) visite tous les éléments si et seulement si \(\operatorname{PGCD}(k, n) = 1\) (S07).

## À retenir

- Premier : exactement deux diviseurs positifs, 1 et lui-même ; 1 n'est pas premier ; 2 est le seul premier pair.
- Test de primalité : diviseurs de 2 à \(\sqrt{n}\) suffisent.
- Crible d'Ératosthène : barrer les multiples de \(p\) pour \(p \le \sqrt{N}\).
- Décomposition **unique** ; nombre de diviseurs \(= \prod (e_i + 1)\) ; PGCD = exposants min ; PPCM = exposants max.

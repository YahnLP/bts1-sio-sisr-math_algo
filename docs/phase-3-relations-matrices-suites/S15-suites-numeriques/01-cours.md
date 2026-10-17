# Cours – Suites numériques

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S15 – à lire avant les [exercices](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** S04 (boucles) ; fonctions usuelles.
> - **Outils :** Papier, calculatrice, éditeur Python intégré au site

## À la fin de ce cours tu sauras

- [ ] **Définir** une suite par une formule explicite ou par récurrence et **calculer** ses premiers termes ;
- [ ] **Reconnaître** une suite arithmétique ou géométrique et **donner** son terme général ;
- [ ] **Calculer** une somme de termes consécutifs ;
- [ ] **Étudier** le sens de variation et **conjecturer** la limite d'une suite à l'aide des suites de référence ;
- [ ] **Écrire** un algorithme de seuil (premier rang tel que…).

## I. Qu'est-ce qu'une suite ?

Une **suite** \((u_n)\) associe à chaque entier naturel \(n\) un nombre réel \(u_n\) (le **terme de rang \(n\)**). C'est une application de \(\mathbb{N}\) dans \(\mathbb{R}\) (S11). On la définit de deux manières.

| Mode | Principe | Exemple | Premiers termes |
|---|---|---|---|
| **Explicite** | \(u_n\) est donné en fonction de \(n\) | \(u_n = 3n + 2\) | 2, 5, 8, 11, 14, 17 |
| **Par récurrence** | on donne \(u_0\) et le lien entre \(u_{n+1}\) et \(u_n\) | \(u_0 = 5,\ u_{n+1} = 2u_n - 1\) | 5, 9, 17, 33, 65, 129 |

La forme explicite donne directement \(u_{1000}\) ; la récurrence oblige à calculer tous les termes précédents (c'est ce que fait une boucle, S04).

> [!NOTE]
> **Conjecturer puis démontrer.** On observe : \(5, 9, 17, 33, 65, \dots\) On conjecture \(u_n = 2^{n+2} + 1\). La formule est vérifiée pour \(n\) de 0 à 20. Pour la **démontrer** : si \(u_n = 2^{n+2} + 1\), alors \(u_{n+1} = 2u_n - 1 = 2\,(2^{n+2} + 1) - 1 = 2^{n+3} + 1\) : la formule passe de \(n\) à \(n+1\).

## II. Suites arithmétiques

Une suite est **arithmétique** de raison \(r\) si l'on passe d'un terme au suivant en **ajoutant** toujours \(r\) :

\[
u_{n+1} = u_n + r
\]

**Terme général :** \(u_n = u_0 + n\,r\), ou \(u_n = u_p + (n - p)\,r\).

**Exemple.** Un volume de sauvegardes vaut 40 Go et augmente de 5 Go par mois : \(u_n = 40 + 5n\). Après 12 mois : 100 Go ; il atteint 200 Go à \(n = 32\) mois.

**Somme de termes consécutifs.** La somme de \(k\) termes consécutifs d'une suite arithmétique vaut :

\[
S = k \times \frac{\text{premier terme} + \text{dernier terme}}{2}
\]

*Cas fondamental :* \(1 + 2 + \dots + n = \dfrac{n(n+1)}{2}\). Pour \(n = 100\) : \(\dfrac{100 \times 101}{2} = 5050\).

**Exemple.** \(u_n = 7 + 4n\) : \(u_0 + \dots + u_{10}\) comporte 11 termes, \(u_{10} = 47\), donc \(S = 11 \times \dfrac{7 + 47}{2} = 297\).

## III. Suites géométriques

Une suite est **géométrique** de raison \(q\) si l'on passe d'un terme au suivant en **multipliant** toujours par \(q\) :

\[
u_{n+1} = q\,u_n \qquad u_n = u_0\,q^n
\]

**Exemple.** Une sauvegarde de 1 Go double chaque mois : \(u_n = 2^n\). Au bout de 10 mois : 1024 Go ; de 30 mois : 1073741824 Go (plus d'un milliard de Go).

**Somme de termes consécutifs.** Pour \(q \neq 1\) :

\[
1 + q + q^2 + \dots + q^n = \frac{1 - q^{n+1}}{1 - q}
\]

(formule vérifiée pour plusieurs valeurs de \(q\), dont \(\frac12\), 3, −2, \(\frac23\)). Donc \(u_0 + u_1 + \dots + u_n = u_0 \cdot \dfrac{1 - q^{n+1}}{1 - q}\). Si \(q = 1\), la suite est constante et la somme vaut \((n+1)\,u_0\).

**Exemples.**

- \(1 + 2 + 4 + \dots + 2^9 = \dfrac{1 - 2^{10}}{1 - 2} = 2^{10} - 1 = 1023\).
- \(1 + \dfrac12 + \dfrac14 + \dots + \dfrac{1}{2^{10}} = \dfrac{1 - (1/2)^{11}}{1 - 1/2} = 2 - \dfrac{1}{1024} = \dfrac{2047}{1024}\).
- \(u_n = 5 \times 3^n\) : \(u_0 + \dots + u_6 = 5 \times \dfrac{3^7 - 1}{2} = 5465\).

## IV. Sens de variation et limites

La suite \((u_n)\) est **croissante** si \(u_{n+1} - u_n \ge 0\) pour tout \(n\), **décroissante** si \(u_{n+1} - u_n \le 0\). Pour comparer, on étudie le **signe de la différence** \(u_{n+1} - u_n\).

- Arithmétique : \(u_{n+1} - u_n = r\). Croissante si \(r > 0\), décroissante si \(r < 0\).
- Géométrique avec \(u_0 > 0\) : croissante si \(q > 1\), décroissante si \(0 < q < 1\), constante si \(q = 1\). Si \(q < 0\), les signes **alternent**.

### Limite : le comportement quand \(n\) devient grand

On dit que \((u_n)\) a pour **limite** \(\ell\) si \(u_n\) s'approche autant qu'on veut de \(\ell\) pour \(n\) assez grand ; la limite est \(+\infty\) si \(u_n\) dépasse tout nombre donné. On se contente ici de l'idée intuitive et des **suites de référence** :

| Suite | Limite quand \(n \to +\infty\) |
|---|---|
| \(n\), \(n^2\), \(\sqrt{n}\) | \(+\infty\) |
| \(\dfrac{1}{n}\), \(\dfrac{1}{n^2}\), \(\dfrac{1}{\sqrt{n}}\) | 0 |
| \(q^n\) avec \(q > 1\) | \(+\infty\) |
| \(q^n\) avec \(-1 < q < 1\) | 0 |
| \(q^n\) avec \(q \le -1\) | pas de limite (oscille) |
| suite constante \(c\) | \(c\) |

On peut **conjecturer** une limite à l'aide d'un tableau de valeurs (sans que ce soit une preuve) :

| \(n\) | \(1/n\) | \((0{,}8)^n\) | \((1{,}05)^n\) | \(3 + 1/n\) |
|---|---|---|---|---|
| 1 | 1,0000 | 0,800000 | 1,05 | 4,0000 |
| 10 | 0,1000 | 0,107374 | 1,63 | 3,1000 |
| 50 | 0,0200 | \(1{,}43 \times 10^{-5}\) | 11,47 | 3,0200 |
| 100 | 0,0100 | \(2{,}04 \times 10^{-10}\) | 131,50 | 3,0100 |

On lit : \(1/n \to 0\), \((0{,}8)^n \to 0\), \((1{,}05)^n\) devient grand (croissance exponentielle), \(3 + 1/n \to 3\).

## V. Algorithme de seuil

Un algorithme de **seuil** cherche le **premier rang** \(n\) à partir duquel une condition est vérifiée. On répète le calcul du terme suivant **tant que** la condition n'est pas atteinte.

**Exemple.** Un placement de 1 000 € à 5 % par an : \(u_n = 1000 \times 1{,}05^n\). À partir de quelle année dépasse-t-il 2 000 € ?

```text
ALGORITHME seuil
  RÔLE      : plus petit n tel que 1000 × 1,05^n ≥ 2000
  SORTIE    : n (entier)
  VARIABLES : n (entier), u (réel)
DÉBUT
  n ← 0 ; u ← 1000
  TANT QUE u < 2000 FAIRE
    u ← u × 1,05
    n ← n + 1
  FIN TANT QUE
  RETOURNER n
FIN
```

Résultat : **\(n = 15\)**. Contrôle exact : \(1000 \times 1{,}05^{14} \approx 1979,93 < 2000\) et \(1000 \times 1{,}05^{15} \approx 2078,93 \ge 2000\).

> [!WARNING]
> **Calculs en décimaux.** Avec des nombres à virgule, l'ordinateur arrondit : une comparaison de valeurs très proches peut être fausse. Quand c'est possible, on travaille en nombres entiers ou en fractions (`Fraction`, S14). Ici les calculs de ce cours sont faits en **fractions exactes**.

**Autre exemple (décroissance).** Un matériel de 1 200 € perd 20 % de sa valeur par an : \(u_n = 1200 \times 0{,}8^n\). Il passe sous 300 € pour \(n = 7\) (valeur \(≈ 251,66\) €, contre \(≈ 314,57\) € l'année précédente).

> [!NOTE]
> **Lien avec la complexité (S18).** Un tri par sélection (S12) fait \(1 + 2 + \dots + (n-1) = \dfrac{n(n-1)}{2}\) comparaisons : pour \(n = 100\), \(4950\). Les sommes de suites arithmétiques servent à **compter** les opérations d'une boucle.

## À retenir

- Suite explicite \(u_n = f(n)\) ou par récurrence \(u_{n+1} = f(u_n)\).
- Arithmétique : \(u_n = u_0 + nr\) ; somme = nombre de termes × (premier + dernier) / 2 ; \(1 + \dots + n = \frac{n(n+1)}{2}\).
- Géométrique : \(u_n = u_0 q^n\) ; somme \(= u_0\frac{1 - q^{n+1}}{1 - q}\) (\(q \neq 1\)).
- Limites de référence : \(n \to +\infty\), \(1/n \to 0\), \(q^n\) selon \(q\).
- Seuil : boucle `TANT QUE`, calculs exacts si possible.

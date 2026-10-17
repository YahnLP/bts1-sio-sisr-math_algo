# Aide-mémoire – Nombres premiers

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S06*

> Un mot ou un sigle inconnu ? Passe la souris dessus, ou ouvre le [glossaire](../../ressources/glossaire.md).

## Définitions

- **Premier** : \(p \ge 2\) avec exactement deux diviseurs positifs (1 et \(p\)). 1 n'est pas premier ; 2 est le seul premier pair.
- Premiers \(< 50\) : 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47.

## Tester la primalité

Tester les diviseurs \(d\) avec \(2 \le d \le \sqrt{n}\) (condition `d * d <= n`).

## Décomposition

\[
n = p_1^{e_1} p_2^{e_2} \cdots p_k^{e_k} \quad (\text{unique}) .
\]

| Je veux… | Formule |
|---|---|
| Nombre de diviseurs | \((e_1 + 1)(e_2 + 1) \cdots (e_k + 1)\) |
| PGCD | chaque premier avec l'exposant **minimum** |
| PPCM | chaque premier avec l'exposant **maximum** |
| Relation | \(\operatorname{PGCD} \times \operatorname{PPCM} = a \times b\) |

## Crible d'Ératosthène

Écrire 2 à \(N\) ; pour \(p\) premier avec \(p^2 \le N\), barrer ses multiples à partir de \(p^2\).

## Exemples à connaître

\[
360 = 2^3 \times 3^2 \times 5 , \quad 1\,001 = 7 \times 11 \times 13 , \quad 2\,024 = 2^3 \times 11 \times 23 , \quad 5\,040 = 2^4 \times 3^2 \times 5 \times 7 .
\]

## Piège

Un nombre qui « a l'air premier » (91 = 7 × 13, 121 = 11²) peut être composé : on teste jusqu'à \(\sqrt{n}\).

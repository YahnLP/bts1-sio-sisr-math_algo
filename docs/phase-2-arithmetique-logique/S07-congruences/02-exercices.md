# Exercices – Calculs modulo n et applications

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S07*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**, avec la méthode du cours : écris les étapes, pas seulement le résultat. Ouvre ensuite « Voir la réponse » pour te corriger. À l'épreuve, **aucune réponse sans justification** n'est complète.

## Exercice 1 – Congruences

Dire si chaque congruence est vraie, en calculant la différence : \(38 \equiv 3 \pmod 7\) ; \(-5 \equiv 9 \pmod 7\) ; \(100 \equiv 1 \pmod 9\) ; \(52 \equiv 4 \pmod{12}\) ; \(17 \equiv 5 \pmod 8\).

<details markdown="1">
<summary>Voir la réponse</summary>

| Congruence | Différence | Vraie ? |
|---|---|---|
| \(38 \equiv 3 \pmod{7}\) | \(38 - (3) = 35\) | oui |
| \(-5 \equiv 9 \pmod{7}\) | \(-5 - (9) = -14\) | oui |
| \(100 \equiv 1 \pmod{9}\) | \(100 - (1) = 99\) | oui |
| \(52 \equiv 4 \pmod{12}\) | \(52 - (4) = 48\) | oui |
| \(17 \equiv 5 \pmod{8}\) | \(17 - (5) = 12\) | **non** |

Pour la dernière, \(17 \equiv 1 \pmod 8\), pas 5.

</details>

## Exercice 2 – Restes et derniers chiffres

1. Reste de 12 345 dans la division par 9 (sans effectuer la division).
2. Dernier chiffre de \(3^{2024}\) et de \(13^{2025}\).
3. Reste de \(2^{10}\) modulo 7, puis de \(2^{100}\) modulo 7.

<details markdown="1">
<summary>Voir la réponse</summary>

1. La somme des chiffres est \(1+2+3+4+5 = 15\), donc \(12\,345 \equiv 6 \pmod 9\). Contrôle : \(12\,345 = 9 \times 1371 + 6\).
2. \(3^2 = 9\), \(3^3 = 27 \equiv 7\), \(3^4 = 81 \equiv 1 \pmod{10}\), donc les derniers chiffres de \(3^k\) reviennent tous les 4 : \(3, 9, 7, 1\). Comme \(2024 = 4 \times 506\), le dernier chiffre de \(3^{2024}\) est 1. \(13 \equiv 3 \pmod{10}\), \(2025 = 4 \times 506 + 1\), donc \(13^{2025} \equiv 3^{1} = 3\).
3. \(2^3 = 8 \equiv 1 \pmod 7\), donc \(2^{10} = (2^3)^3 \times 2 \equiv 2\) (reste 2, vérification : \(1\,024 = 7 \times 146 + 2\)). \(2^{100} = (2^3)^{33} \times 2 \equiv 2\) (reste 2).

</details>

## Exercice 3 – Inverses

1. Dresser la table des inverses modulo 9.
2. Résoudre \(5x \equiv 3 \pmod 9\).
3. Pourquoi \(6x \equiv 1 \pmod 9\) n'a-t-elle pas de solution ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. | \(a\) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| inverse | 1 | 5 | aucun | 7 | 2 | aucun | 4 | 8 |
2. L'inverse de 5 modulo 9 est 2 (\(5 \times 2 = 10 = 2 \times 9 + 1\)), donc \(x \equiv 2 \times 3 = 6 \equiv 6 \pmod 9\). Vérification : \(5 \times 6 = 30 = 3 \times 9 + 3\), et le reste vaut bien 3.
3. \(\operatorname{PGCD}(6, 9) = 3 \ne 1\) : les multiples de 6 modulo 9 sont seulement 0, 3, 6 (des multiples de 3), jamais 1.

</details>

## Exercice 4 – Parcours circulaire

Une liste circulaire compte \(n = 15\) cases. On part de la case 0 et on avance de \(k\) cases à chaque saut.

1. Pour \(k = 6\), quelles cases sont visitées ? Combien ?
2. Pour \(k = 4\), est-ce que toutes les cases sont visitées ? Pourquoi ?
3. Quelles valeurs de \(k\) entre 1 et 14 visitent toutes les cases ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(\operatorname{PGCD}(6, 15) = 3\). Cases : 0, 6, 12, 3, 9, soit 5 cases.
2. \(\operatorname{PGCD}(4, 15) = 1\) : oui, toutes les 15 cases sont visitées.
3. Les \(k\) premiers avec 15 : 1, 2, 4, 7, 8, 11, 13, 14 (8 valeurs).

</details>

## Exercice 5 – César et affine

1. Chiffrer RESEAU avec le chiffre de César de décalage 5.
2. Déchiffrer KHOOR ZRUOG (décalage 3).
3. Chiffrer OK avec \(y \equiv 7x + 3 \pmod{26}\) ; en déduire la formule de déchiffrement et vérifier sur le résultat.
4. Pourquoi \(a = 13\) est-il interdit ? Donner deux lettres qui seraient chiffrées de la même façon.

<details markdown="1">
<summary>Voir la réponse</summary>

1. **WJXJFZ**.
2. **HELLO WORLD**.
3. | Lettre | Rang \(x\) | \(7x + 3\) | Reste mod 26 | Lettre chiffrée |
|---|---|---|---|---|
| O | 14 | 101 | 23 | X |
| K | 10 | 73 | 21 | V |
   Résultat : **XV**. L'inverse de 7 modulo 26 est 15, donc \(x \equiv 15 (y - 3) \pmod{26}\). Pour X (rang 23) : \(15 \times 20 = 300 \equiv 14\), soit la lettre O.
4. \(\operatorname{PGCD}(13, 26) = 13\) : 13 n'a pas d'inverse. Par exemple A (rang 0) et C (rang 2) donnent \(13 \times 0 + b = b\) et \(13 \times 2 + b = 26 + b \equiv b\) : même lettre chiffrée.

</details>

## Exercice 6 – Clés de contrôle

1. Calculer la clé du numéro (fictif) dont les 13 premiers chiffres sont \(2\,990\,175\,123\,456\) : \(97 - (N \bmod 97)\).
2. Vérifier que `9780306406157` est un ISBN-13 valide.
3. Quelle propriété du nombre \(N + \text{clé}\) permet de vérifier un numéro reçu ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(N \bmod 97 = 48\), clé \(= 97 - 48 = 49\).
2. Poids 1, 3, 1, 3… : somme \(= 100\), multiple de 10 : valide.
3. \(N + \text{clé}\) doit être un multiple de 97 ; sinon, il y a eu une erreur. Cette méthode détecte toute erreur sur un seul chiffre ; elle ne corrige rien.

</details>

## Exercice 7 – Hachage

On range les clés 110, 120, 130, 140, 150 dans une table de 10 cases avec \(h(x) = x \bmod 10\), puis dans une table de 11 cases avec \(h(x) = x \bmod 11\). Comparer les collisions.

<details markdown="1">
<summary>Voir la réponse</summary>

| Clé | \(\bmod 10\) | \(\bmod 11\) |
|---|---|---|
| 110 | 0 | 0 |
| 120 | 0 | 10 |
| 130 | 0 | 9 |
| 140 | 0 | 8 |
| 150 | 0 | 7 |

Avec 10 cases, les cinq clés tombent toutes dans la case 0 (quatre collisions successives). Avec 11 cases, elles occupent les cases 0, 10, 9, 8, 7, toutes différentes. Quand les clés ont une régularité (ici, des multiples de 10), un module premier avec cette régularité répartit mieux : c'est pourquoi on prend souvent un nombre premier comme taille de table.

</details>


## Je sais faire

Coche honnêtement ; ce que tu ne coches pas se reprend avant la séance suivante.

- [ ] Calculer modulo \(n\) en réduisant à chaque étape ;
- [ ] Reconnaître et calculer un inverse modulo \(n\) ;
- [ ] Chiffrer et déchiffrer avec le code affine ;
- [ ] Calculer une clé de contrôle ;
- [ ] Dire quand un parcours par sauts de \(k\) visite toute la liste circulaire.

**Ce que je dois reprendre :** ______________________

**Ma question à poser à l'enseignant :** ______________________

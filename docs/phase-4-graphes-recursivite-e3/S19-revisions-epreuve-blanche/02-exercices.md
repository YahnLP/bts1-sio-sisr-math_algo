# Exercices – Sujet d'entraînement et révisions

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S19*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**, avec la méthode du cours : écris les étapes, pas seulement le résultat. Ouvre ensuite « Voir la réponse » pour te corriger. À l'épreuve, **aucune réponse sans justification** n'est complète.

## Auto-diagnostic : une question par séance

Réponds à chaque question **sans aide**, puis ouvre la réponse. Entoure les séances où tu t'es trompé : ce sont tes révisions prioritaires.

| Séance | Question | Réponse |
|---|---|---|
| S01 | Convertir 1000 en binaire et en hexadécimal. | <details markdown="1"><summary>Réponse</summary>\(1111101000_2\) et \(3E8_{16}\)</details> |
| S02 | Combien d'octets dans 1 Mio ? | <details markdown="1"><summary>Réponse</summary>\(2^{20} = 1048576\)</details> |
| S03 | 2100 est-elle une année bissextile ? | <details markdown="1"><summary>Réponse</summary>Non : divisible par 100 mais pas par 400.</details> |
| S04 | Que vaut \(1 + 2 + \dots + 100\) (boucle `POUR`) ? | <details markdown="1"><summary>Réponse</summary>5050</details> |
| S05 | PGCD et PPCM de 84 et 36. | <details markdown="1"><summary>Réponse</summary>PGCD 12, PPCM 252</details> |
| S06 | Décomposer 360 ; combien de diviseurs ? | <details markdown="1"><summary>Réponse</summary>\(360 = 2^3 \times 3^2 \times 5\) ; \((3+1)(2+1)(1+1) = 24\) diviseurs</details> |
| S07 | Reste de \(3^{100}\) dans la division par 7 ? | <details markdown="1"><summary>Réponse</summary>\(3^6 \equiv 1\) ; \(100 = 6 \times 16 + 4\) ; \(3^4 = 81 \equiv 4\) (mod 7)</details> |
| S08 | Nier \(p \Rightarrow q\). | <details markdown="1"><summary>Réponse</summary>\(p \wedge \neg q\)</details> |
| S09 | Nier \(\forall x\, \exists y,\ P(x, y)\). | <details markdown="1"><summary>Réponse</summary>\(\exists x\, \forall y,\ \neg P(x, y)\)</details> |
| S10 | Simplifier \(a + \overline{a}\,b\). | <details markdown="1"><summary>Réponse</summary>\(a + b\)</details> |
| S11 | \(x \mapsto x \bmod 5\) de \(\{0,\dots,9\}\) dans \(\{0,\dots,4\}\) est-elle injective ? surjective ? | <details markdown="1"><summary>Réponse</summary>Surjective, pas injective (0 et 5 ont la même image).</details> |
| S12 | Pour `t = [4, 8, 15, 16]`, que valent `len(t)` et l'indice de 15 ? | <details markdown="1"><summary>Réponse</summary>`len(t)` vaut 4 ; 15 est à l'indice 2 (les indices vont de 0 à 3).</details> |
| S13 | Un produit \((2 \times 3)(3 \times 4)\) existe-t-il ? taille ? | <details markdown="1"><summary>Réponse</summary>Oui, \(2 \times 4\).</details> |
| S14 | Résoudre \(\begin{cases} x + 2y = 5 \\ 3x + 7y = 16 \end{cases}\) avec \(A^{-1} = \begin{pmatrix} 7 & -2 \\ -3 & 1 \end{pmatrix}\). | <details markdown="1"><summary>Réponse</summary>\(X = A^{-1}B = (3,\ 1)\)</details> |
| S15 | `10.0.0.256` est-elle une adresse IPv4 valide ? Bit de parité (paire) de `1011001` ? | <details markdown="1"><summary>Réponse</summary>Non (256 > 255). Quatre 1, donc bit de parité 0.</details> |
| S16 | Graphe \(a \to b,\ a \to c,\ b \to d,\ c \to d\) : nombre de chemins de longueur 2 de \(a\) à \(d\) ? | <details markdown="1"><summary>Réponse</summary>2 (par \(b\) et par \(c\)).</details> |
| S17 | Dans le graphe valué du cours (sites \(S\) à \(T\)), valeur minimale de \(S\) à \(T\) ? | <details markdown="1"><summary>Réponse</summary>13 (méthode de Dijkstra, S17).</details> |
| S18 | Que renvoie `est_croissant([1, 3, 2])` si la fonction fait `return True` dès que `t[i] <= t[i+1]` ? | <details markdown="1"><summary>Réponse</summary>`True` (arrêt trop tôt, dès le couple `1, 3`) ; attendu `False`.</details> |

## Exercices de synthèse

Ces exercices mêlent plusieurs chapitres. La **méthode à suivre** est indiquée.

### Synthèse 1 – Réseau et arithmétique

Une machine a l'adresse `172.16.77.130/26`. (a) Donner le masque, l'adresse réseau et l'adresse de diffusion. (b) Combien de machines peut-on adresser ? (c) `172.16.77.200` est-elle dans le même réseau ?

<details markdown="1">
<summary>Voir la réponse</summary>

(a) masque `255.255.255.192` ; réseau `172.16.77.128` ; diffusion `172.16.77.191` (\(130 \,\&\, 192 = 128\) ; \(128 + 63 = 191\)). (b) \(2^6 - 2 = 62\). (c) Non : \(200 \,\&\, 192 = 192\), réseau `172.16.77.192`.

</details>

### Synthèse 2 – Congruences

Résoudre \(7x \equiv 3 \pmod{26}\). (Méthode : chercher l'inverse de 7 modulo 26 avec l'algorithme d'Euclide étendu ou par essais.)

<details markdown="1">
<summary>Voir la réponse</summary>

\(7 \times 15 = 105 = 4 \times 26 + 1\) : l'inverse de 7 est 15. Donc \(x \equiv 15 \times 3 = 45 \equiv 19 \pmod{26}\). Contrôle : \(7 \times 19 = 133 = 5 \times 26 + 3\) ✓.

</details>

### Synthèse 3 – Contrôle de données

Trois octets \(120, 200, 77\) sont envoyés avec un octet de contrôle \(c\) tel que la somme des quatre octets soit un multiple de 256. (a) Calculer \(c\). (b) On reçoit \(120, 201, 76\) et \(c\) : l'erreur est-elle détectée ? (c) L'adresse `192.168.1.256` est-elle une adresse IPv4 valide ?

<details markdown="1">
<summary>Voir la réponse</summary>

(a) Somme \(397\) ; \(397 \bmod 256 = 141\) ; \(c = 256 - 141 = 115\) (contrôle : \(397 + 115 = 512\)). (b) \(120 + 201 + 76 + 115 = 512\) : le contrôle réussit alors que deux octets sont faux ; deux erreurs qui se compensent ne sont pas détectées. (c) Non : le dernier octet, 256, dépasse 255.

</details>

### Synthèse 4 – Boole et matrices

(a) Simplifier \(f = a\,b + a\,\overline{b}\,c + \overline{a}\,b\,c\) par un tableau de Karnaugh. (b) Résoudre \(\begin{cases} 3x + y = 11 \\ 5x + 2y = 19 \end{cases}\) (méthode : inverse de la matrice, donnée : \(\begin{pmatrix} 2 & -1 \\ -5 & 3 \end{pmatrix}\)).

<details markdown="1">
<summary>Voir la réponse</summary>

(a) Les lignes à 1 sont 3, 5, 6, 7 : trois rectangles de 2 cases, \(f = a\,b + a\,c + b\,c\) (majorité). (b) \(X = \begin{pmatrix} 3 \\ 2 \end{pmatrix}\), soit \(x = 3\), \(y = 2\) ; contrôle : \(3 \times 3 + 2 = 11\), \(5 \times 3 + 2 \times 2 = 19\).

</details>


## Je sais faire

Coche honnêtement ; ce que tu ne coches pas se reprend avant la séance suivante.

- [ ] Gérer 2 h pour 2 ou 3 exercices ;
- [ ] Justifier chaque réponse ;
- [ ] Écrire un algorithme complet (en-tête, indentation, commentaires) ;
- [ ] Vérifier un résultat par un autre chemin ;
- [ ] Établir mon plan de révision.

**Ce que je dois reprendre :** ______________________

**Ma question à poser à l'enseignant :** ______________________

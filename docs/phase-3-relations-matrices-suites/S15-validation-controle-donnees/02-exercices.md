# Exercices – Formats, parité et sommes de contrôle

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S15*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**, avec la méthode du cours : écris les étapes, pas seulement le résultat. Ouvre ensuite « Voir la réponse » pour te corriger. À l'épreuve, la calculatrice est autorisée selon les consignes du sujet : entraîne-toi à poser les calculs.

## Exercice 1 – Octet valide ?

Pour chaque chaîne, dire si elle représente un octet décimal valide (règles du cours) : `"192"`, `"256"`, `"07"`, `""`, `"12a"`, `"0"`.

<details markdown="1">
<summary>Voir la réponse</summary>

`"192"` : oui. `"256"` : non (supérieur à 255). `"07"` : non (zéro initial). `""` : non (vide). `"12a"` : non (caractère qui n'est pas un chiffre). `"0"` : oui (zéro seul).

</details>

## Exercice 2 – Adresse IPv4 valide ?

Dire si chaque chaîne est une adresse IPv4 valide et donner la première règle violée : (a) `10.0.0.1` ; (b) `10.0.0` ; (c) `172.16.256.1` ; (d) `192.168.1.1.` ; (e) `1.2.3.04`.

<details markdown="1">
<summary>Voir la réponse</summary>

(a) valide. (b) non : 3 morceaux au lieu de 4. (c) non : 256 > 255. (d) non : `split(".")` donne 5 morceaux, le dernier est vide. (e) non : `"04"` a un zéro initial.

</details>

## Exercice 3 – Masque valide ?

Les octets possibles d'un masque de sous-réseau sont ceux dont l'écriture binaire est une suite de 1 suivie de 0.

1. Écrire les neuf valeurs possibles d'un octet de masque.
2. Parmi `255.255.255.192`, `255.255.255.100`, `255.255.0.255`, dire lesquels sont des masques valides.

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(0, 128, 192, 224, 240, 248, 252, 254, 255\) (de zéro à huit bits à 1, en tête).
2. `255.255.255.192` : valide. `255.255.255.100` : non, \(100 = 01100100_2\) n'est pas de la forme 1…10…0. `255.255.0.255` : non, après un octet nul, tous les octets suivants doivent être nuls.

</details>

## Exercice 4 – Bit de parité

1. Donner le bit de parité (parité paire) de `1011001`, `1110000`, `0000000`, `1111111`.
2. Parmi les mots reçus `10110010`, `11100001`, `10011000`, `11000011` (parité paire, bit de parité compris), lesquels sont acceptés ?
3. Le mot `10110010` est altéré en `10010011` pendant la transmission. Le contrôle le détecte-t-il ? Pourquoi ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. `1011001` : 4 uns, bit 0. `1110000` : 3 uns, bit 1. `0000000` : 0 un, bit 0. `1111111` : 7 uns, bit 1.
2. Nombre de 1 : 4, 4, 3, 4. Seul `10011000` (nombre impair) est refusé.
3. Deux bits ont changé (rangs 3 et 8). Le mot reçu contient 4 uns : le nombre est pair, **l'erreur n'est pas détectée**. La parité ne voit pas un nombre pair d'erreurs.

</details>

## Exercice 5 – Parité à deux dimensions

La grille suivante (3 lignes et 3 colonnes de données, plus les bits de parité) a été reçue avec **au plus une** erreur.

```text
1 0 1 | 0
0 1 0 | 0
1 1 0 | 0
------+--
0 0 0 | 0
```

1. Quelles lignes et quelles colonnes ont une parité fausse ?
2. Quel bit est erroné ? Donner la grille corrigée.

<details markdown="1">
<summary>Voir la réponse</summary>

1. Ligne 1 (un seul 1) et colonne 2 (un seul 1). Les autres lignes et colonnes comptent 2 uns ou aucun.
2. Le bit à l'intersection, ligne 1, colonne 2 : il vaut 0, on le remplace par 1. La ligne 1 devient `0 1 1 | 0`, la colonne 2 compte 2 uns : toutes les parités sont justes.

</details>

## Exercice 6 – Somme de contrôle

1. Calculer l'octet de contrôle \(c\) pour les octets \(200, 100, 50\).
2. On reçoit \(200, 100, 51\) avec \(c = 162\). Le contrôle réussit-il ?
3. On reçoit \(201, 99, 50\) avec \(c = 162\). Le contrôle réussit-il ? Que conclure ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. Somme \(350\) ; \(350 \bmod 256 = 94\) ; \(c = 256 - 94 = 162\). Vérification : \(350 + 162 = 512 = 2 \times 256\).
2. \(200 + 100 + 51 + 162 = 513 \equiv 1 \pmod{256}\) : le résultat n'est pas nul, l'erreur est détectée.
3. \(201 + 99 + 50 + 162 = 512 \equiv 0\) : le contrôle réussit alors que deux octets sont faux. Deux erreurs qui se compensent ne sont pas détectées.

</details>

## Exercice 7 – OU exclusif de contrôle

1. Calculer \(\texttt{0xC0} \oplus \texttt{0xA8} \oplus \texttt{0x0A} \oplus \texttt{0x4D}\) (ce sont les octets de `192.168.10.77`), en binaire puis en hexadécimal.
2. Quel est le OU exclusif des cinq octets obtenus en ajoutant ce résultat aux quatre premiers ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(11000000 \oplus 10101000 = 01101000\) ; \(00001010 \oplus 01001101 = 01000111\) ; \(01101000 \oplus 01000111 = 00101111\), soit `0x2F` (47 en décimal).
2. 0 : chaque bit apparaît un nombre pair de fois, car \(x \oplus x = 0\).

</details>

## Exercice 8 – Choisir les tests

On écrit une fonction `mac_valide(s)`. Proposer six chaînes de test : deux valides et quatre invalides, chacune pour une raison différente.

<details markdown="1">
<summary>Voir la réponse</summary>

Valides : `00:1A:2b:3C:4d:5E` (mélange majuscules et minuscules) et `ff:ff:ff:ff:ff:ff`. Invalides : `00:1A:2b:3C:4d` (5 groupes) ; `00:1A:2b:3C:4d:5G` (`G` n'est pas hexadécimal) ; `0:1A:2b:3C:4d:5E` (groupe d'un seul caractère) ; la chaîne vide. D'autres choix sont possibles : l'essentiel est que chaque règle soit violée par au moins un test.

</details>

## Je sais faire

Coche honnêtement ; ce que tu ne coches pas se reprend avant la séance suivante.

- [ ] Écrire les règles d'un format et les traduire en tests ;
- [ ] Choisir des cas limites pour un validateur ;
- [ ] Calculer un bit de parité et contrôler un mot reçu ;
- [ ] Localiser une erreur isolée avec une parité à deux dimensions ;
- [ ] Calculer une somme de contrôle et un OU exclusif de contrôle.

**Ce que je dois reprendre :** ______________________

**Ma question à poser à l'enseignant :** ______________________

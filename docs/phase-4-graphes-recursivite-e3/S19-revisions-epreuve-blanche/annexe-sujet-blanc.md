# Annexe – Sujet blanc E3 (2 heures, 20 points)

> [!NOTE]
> **Conditions.** Compose ce sujet **sans aide** et **chronométré** (2 heures). Les trois exercices sont indépendants. Calculatrice : selon les règles de la session (voir le programme). Le corrigé et le barème détaillé sont remis après la séance. Cette épreuve est un **entraînement** : elle ne compte pas dans une note officielle.

## Exercice 1 – Adresses, codes et arithmétique (6 points)

**1. (1,5 point)** Numération.

a) Écrire 213 en binaire sur 8 bits.
b) Convertir le nombre hexadécimal `A7` en décimal.
c) Additionner en binaire, sur 8 bits, `11010110` et `00101101`. Y a-t-il un dépassement de capacité ? Justifier.

**2. (1,5 point)** Adressage. Une machine a l'adresse `172.16.77.130/26`.

a) Donner le masque de sous-réseau en notation décimale pointée.
b) Calculer l'adresse du réseau et l'adresse de diffusion.
c) Combien de machines peut-on adresser dans ce réseau ?
d) La machine d'adresse `172.16.77.200` est-elle dans le même réseau ? Justifier.

**3. (1,5 point)** Arithmétique.

a) Calculer le PGCD de 1260 et 198 par l'algorithme d'Euclide (détailler les divisions).
b) Vérifier le résultat avec les décompositions en facteurs premiers de 1260 et de 198.

**4. (1,5 point)** Congruences. Un code associe à un nombre \(x\) (de 0 à 25) le nombre \(y\) défini par \(y \equiv 7x \pmod{26}\).

a) Montrer que 15 est l'inverse de 7 modulo 26.
b) On reçoit \(y = 3\). Retrouver \(x\), puis vérifier.

## Exercice 2 – Logique, ensembles et matrices (6 points)

**1. (2 points)** Une règle d'accès à une ressource dépend de trois conditions \(a\), \(b\), \(c\) :
\[
f = a\,b + a\,\overline{b}\,c + \overline{a}\,b\,c
\]

a) Dresser la table de vérité de \(f\).
b) Simplifier \(f\) à l'aide d'un tableau de Karnaugh. Quelle est la signification de la règle simplifiée ?

**2. (1 point)** Dans une entreprise de 100 salariés, 70 utilisent un VPN, 45 utilisent la messagerie chiffrée et 25 utilisent les deux. Combien de salariés n'utilisent aucun des deux services ?

**3. (3 points)** Deux types de licences ont des prix unitaires (en euros) \(x\) et \(y\) inconnus. Un premier achat de 3 licences du type 1 et 1 du type 2 coûte 11 euros ; un second, de 5 licences du type 1 et 2 du type 2, coûte 19 euros.

a) Écrire le système sous la forme \(AX = B\) avec \(A\), \(X\), \(B\) matrices.
b) On donne \(P = \begin{pmatrix} 2 & -1 \\ -5 & 3 \end{pmatrix}\). Vérifier que \(P\) est l'inverse de \(A\).
c) En déduire \(x\) et \(y\).

## Exercice 3 – Journaux et volumétrie, avec programmation Python (8 points)

Le volume \(V_n\) (en Go) des journaux d'un serveur, au bout de \(n\) mois, vaut 120 Go au départ (\(V_0 = 120\)) et augmente de 8 % chaque mois.

**1. (3 points)** Étude de la suite.

a) Justifier que \((V_n)\) est une suite géométrique ; donner sa raison et \(V_n\) en fonction de \(n\).
b) Calculer \(V_3\) (arrondir au centième).
c) Le disque a une capacité de 200 Go. Écrire un algorithme (pseudo-code) qui détermine le premier mois où le volume atteint ou dépasse 200 Go. Donner la réponse.

**2. (2 points)** Écrire en Python une fonction `premier_mois(v0, q, capacite)` qui renvoie le plus petit entier \(n\) tel que `v0 * q**n >= capacite` (on suppose \(q > 1\)).

**3. (2 points)** Une ligne de journal a la forme `date heure adresse niveau message`, par exemple `2026-03-14 08:13:02 10.0.0.9 ERROR timeout db`. Écrire une fonction `compte_erreurs(lignes)` qui, à partir d'une liste de lignes, renvoie un dictionnaire qui à chaque adresse associe son nombre de lignes de niveau `ERROR`.

**4. (1 point)** Un tableau trié contient 1 000 éléments. Quel est le nombre maximal de comparaisons d'une recherche par dichotomie ? Comparer avec une recherche séquentielle.

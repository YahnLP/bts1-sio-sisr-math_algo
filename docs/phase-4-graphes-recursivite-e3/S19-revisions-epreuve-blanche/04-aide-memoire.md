# Aide-mémoire – Préparer l'épreuve E3

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S19*

> Un mot ou un sigle inconnu ? Passe la souris dessus, ou ouvre le [glossaire](../../ressources/glossaire.md).

## Format E3

- Écrit de **2 h**, **20 points**, coefficient **3**, 2 ou 3 exercices dont **un de programmation (Python)** ; évaluation terminale.
- Vérifier chaque session le document en vigueur (moyens de calcul autorisés).

## Réponse complète

1. **Méthode** annoncée ; 2. **calcul** détaillé ; 3. **résultat** avec unité et phrase de conclusion ; 4. **vérification**.

## Formulaire de synthèse

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

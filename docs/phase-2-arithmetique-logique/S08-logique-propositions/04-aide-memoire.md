# Aide-mémoire – Calcul des propositions

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S08*

> Un mot ou un sigle inconnu ? Passe la souris dessus, ou ouvre le [glossaire](../../ressources/glossaire.md).

## Connecteurs

| Connecteur | Notation | Python |
|---|---|---|
| Négation | \(\neg p\) | `not p` |
| Et | \(p \wedge q\) | `p and q` |
| Ou (inclusif) | \(p \vee q\) | `p or q` |
| Implication | \(p \Rightarrow q\) | `(not p) or q` |
| Équivalence | \(p \Leftrightarrow q\) | `p == q` |
| Ou exclusif | \(p \oplus q\) | `p != q` |

\(p \Rightarrow q\) est **fausse** seulement pour \(p\) vrai et \(q\) faux.

## Équivalences

| | |
|---|---|
| De Morgan | \(\neg(p \wedge q) \equiv \neg p \vee \neg q\) ; \(\neg(p \vee q) \equiv \neg p \wedge \neg q\) |
| Implication | \(p \Rightarrow q \equiv \neg p \vee q\) |
| Contraposée | \(p \Rightarrow q \equiv \neg q \Rightarrow \neg p\) |
| Négation de l'implication | \(\neg(p \Rightarrow q) \equiv p \wedge \neg q\) |
| Réciproque | \(q \Rightarrow p\) : **pas** équivalente |
| Équivalence | \(p \Leftrightarrow q \equiv (p \Rightarrow q) \wedge (q \Rightarrow p)\) |

## Méthode

1. Lister les \(2^n\) combinaisons.
2. Calculer colonne par colonne, des petites expressions aux grandes.
3. Comparer les colonnes : mêmes valeurs ⟹ expressions **équivalentes** ; colonne toute V ⟹ **tautologie**.

## Négation d'une condition

Appliquer De Morgan (\(\wedge \leftrightarrow \vee\)) puis nier chaque test : \(<\) ↔ \(\ge\), \(>\) ↔ \(\le\), \(=\) ↔ \(\ne\).

## Priorités

\(\neg\) avant \(\wedge\) avant \(\vee\) avant \(\Rightarrow\) avant \(\Leftrightarrow\) ; en cas de doute, **parenthéser**.

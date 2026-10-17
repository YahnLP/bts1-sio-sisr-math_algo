# Aide-mémoire – Chemin optimal et MPM

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S17*

> Un mot ou un sigle inconnu ? Passe la souris dessus, ou ouvre le [glossaire](../../ressources/glossaire.md).

## Dijkstra (valeurs ≥ 0)

1. \(S\) à 0, les autres à \(\infty\). 2. Fixer le sommet non fixé de plus petite valeur. 3. Mettre à jour ses successeurs (valeur + arc plus petite ?) et noter le prédécesseur. 4. Recommencer ; lire le chemin à l'envers.

## MPM

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

# Aide-mémoire – Graphes

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S16*

> Un mot ou un sigle inconnu ? Passe la souris dessus, ou ouvre le [glossaire](../../ressources/glossaire.md).

## Vocabulaire

| Terme | Sens |
|---|---|
| Arc \(x \to y\) | flèche de \(x\) vers \(y\) |
| Chemin, longueur | suite d'arcs ; nombre d'arcs |
| Circuit | chemin fermé (longueur \(\ge 1\)) ; boucle = circuit de longueur 1 |
| Hamiltonien | chemin passant une fois par chaque sommet |
| \(d^+(x)\), \(d^-(x)\) | arcs qui partent de / arrivent en \(x\) |

## Matrice d'adjacence

- \(m_{ij} = 1\) si \(i \to j\). Somme d'une **ligne** = \(d^+\) ; d'une **colonne** = \(d^-\).
- \((M^p)_{ij}\) = nombre de chemins de longueur \(p\) de \(i\) à \(j\).
- Sans circuit (\(n\) sommets) : \(M^n = 0\). Avec circuit : jamais nulle.

## Fermeture transitive

\(M^* = M + M^{[2]} + \dots + M^{[n-1]}\) (somme et produit **booléens**) : \(M^*_{ij} = 1\) s'il existe un chemin de \(i\) à \(j\).

## Niveaux (sans circuit)

1. Niveau 0 : sommets sans prédécesseur. 2. Les retirer. 3. Recommencer. Aucun sommet sans prédécesseur alors qu'il en reste : circuit.

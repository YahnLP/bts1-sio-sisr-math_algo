# Aide-mémoire – Relations et applications

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S11*

> Un mot ou un sigle inconnu ? Passe la souris dessus, ou ouvre le [glossaire](../../ressources/glossaire.md).

## Vocabulaire

| Notion | Définition | Python |
|---|---|---|
| Produit \(A \times B\) | couples \((a, b)\) ; \(\lvert A \rvert \cdot \lvert B \rvert\) éléments | `{(x, y) for x in a for y in b}` |
| Relation sur \(E\) | partie de \(E \times E\) | ensemble de couples |
| Réflexive | \(x\,\mathcal{R}\,x\) pour tout \(x\) | `(x, x) in r` |
| Symétrique | \(x\,\mathcal{R}\,y \Rightarrow y\,\mathcal{R}\,x\) | `(y, x) in r` |
| Antisymétrique | \(x\,\mathcal{R}\,y\) et \(y\,\mathcal{R}\,x\) \(\Rightarrow x = y\) | |
| Transitive | \(x\,\mathcal{R}\,y\) et \(y\,\mathcal{R}\,z\) \(\Rightarrow x\,\mathcal{R}\,z\) | |

- **Équivalence** = réflexive + symétrique + transitive → classes qui partitionnent \(E\).
- **Ordre** = réflexive + antisymétrique + transitive ; total si tout couple est comparable.

## Applications

| Propriété | Test |
|---|---|
| Application | chaque \(x\) de \(A\) a **une seule** image |
| Injective | images toutes différentes |
| Surjective | tout élément de \(B\) est atteint |
| Bijective | injective et surjective ; réciproque \(f^{-1}\) |

- Composée : \((g \circ f)(x) = g(f(x))\) ; on applique \(f\) en premier ; non commutative.
- Image directe \(f(X)\) ; image réciproque \(f^{-1}(Y)\) (existe toujours).
- Nombre d'applications de \(A\) vers \(B\) : \(\lvert B \rvert^{\lvert A \rvert}\).
- Ensembles finis de même taille : injective \(\iff\) surjective \(\iff\) bijective.

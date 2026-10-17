# Aide-mémoire – Prédicats et ensembles

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S09*

> Un mot ou un sigle inconnu ? Passe la souris dessus, ou ouvre le [glossaire](../../ressources/glossaire.md).

## Quantificateurs

| Notation | Lecture | Négation |
|---|---|---|
| \(\forall x,\ P(x)\) | pour tout \(x\), \(P(x)\) | \(\exists x,\ \neg P(x)\) |
| \(\exists x,\ P(x)\) | il existe \(x\) tel que \(P(x)\) | \(\forall x,\ \neg P(x)\) |

- Pour nier : on **échange** \(\forall\) et \(\exists\), puis on nie le prédicat.
- \(\forall x\, \exists y\) n'est **pas** équivalent à \(\exists y\, \forall x\) : l'ordre compte.
- Un exemple ne prouve jamais un « pour tout » ; un contre-exemple le réfute.

## Ensembles

| Notation | Sens | Python |
|---|---|---|
| \(x \in A\) | \(x\) appartient à \(A\) | `x in A` |
| \(A \subseteq B\) | inclusion | `A <= B` |
| \(A \cap B\) | intersection | `A & B` |
| \(A \cup B\) | réunion | `A | B` |
| \(A \setminus B\) | différence | `A - B` |
| \(A \,\Delta\, B\) | différence symétrique | `A ^ B` |
| \(\overline{A}\) | complémentaire | `E - A` |
| \(\lvert A \rvert\) | cardinal | `len(A)` |

- \(\lvert \mathcal{P}(A) \rvert = 2^{\lvert A \rvert}\).
- \(\lvert A \cup B \rvert = \lvert A \rvert + \lvert B \rvert - \lvert A \cap B \rvert\).
- Une partie d'un ensemble à \(n\) éléments se code par un nombre de \(n\) bits (masque).

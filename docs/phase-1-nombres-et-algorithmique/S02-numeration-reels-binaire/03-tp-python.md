---
render_macros: true
---

# TP Python – Précision des nombres flottants et décalages

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S02*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

> [!TIP]
> Si Python est nouveau pour toi, relis l'[annexe Python : premiers pas](../S01-numeration-entiers/annexe-python.md) de S01 (variables, `//` et `%`, `while`, `for`, texte, `def`). Les notions sont reprises en détail en S03 et S04.

## Exercice A – Pourquoi `0.1 + 0.2 != 0.3`

**J'anticipe.** Que vaut, selon toi, `0.1 + 0.2 == 0.3` ? Et `0.5 + 0.25 == 0.75` ? Justifie avec le cours (§ I).

{{ IDE('flottants', MAX="+") }}

**Je comprends.** `Fraction` calcule exactement avec des rapports d'entiers ; `math.isclose` accepte un petit écart. Quelles valeurs sont exactes en binaire parmi celles du script ?

## Exercice B – Les chiffres binaires d'une partie fractionnaire

Écris `chiffres_apres_virgule(x, p)` qui renvoie le texte des `p` premiers chiffres binaires de la partie fractionnaire de `x` (`0 <= x < 1`), par multiplications successives par 2.

**J'anticipe.** Pour `x = 0.8125` et `p = 4`, écris les quatre multiplications avant de coder.

{{ IDE('chiffres_apres_virgule', MAX="+") }}

## Exercice C – Additionner deux nombres binaires « à la main »

Écris `addition_binaire(a, b)` qui reçoit deux **textes** binaires et renvoie leur somme en texte binaire, **sans** convertir en entier : tu additionnes de droite à gauche en gérant la retenue.

{{ IDE('addition_binaire', MAX="+") }}

## Exercice D – Débordement sur \(n\) bits

Écris `addition_n_bits(a, b, n)` qui renvoie le couple `(résultat, débordement)` : le résultat tient sur `n` bits (reste modulo \(2^n\)) et `débordement` vaut `True` si la somme exacte dépasse \(2^n - 1\).

{{ IDE('addition_n_bits', MAX="+") }}

## Exercice E – Durée d'un transfert

Écris `duree_transfert(taille_octets, debit_bits_par_s)` qui renvoie la durée théorique en secondes.

{{ IDE('duree_transfert', MAX="+") }}

**Je comprends.** Calcule la durée pour 2 Go à 100 Mbit/s, puis à 1 Gbit/s, et compare avec le cours (§ VI).

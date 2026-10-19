---
render_macros: true
---

# TP Python – Premiers programmes

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S00*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes**. Les lignes `...` et « À compléter » sont **à remplacer** par ton code ; le reste est déjà écrit. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

## Exercice A – Essayer

Dans l'éditeur ci-dessous, écris des `print(...)` pour calculer : `7 // 2`, `7 % 2`, `2 ** 10`, `"ab" + "cd"`, `len("réseau")`. Compare avec ce que tu avais prévu.

{{ IDE('essayer', MAX="+") }}

## Exercice B – Quotient et reste

> [!TIP]
> **Syntaxe utile.** `a // b` : quotient ; `a % b` : reste ; `x == 0` : test d'égalité (donne `True` ou `False`) ; `return (q, r)` : renvoyer deux valeurs.

Complète `quotient_reste(a, b)`, `est_multiple(a, b)` et `conversion_secondes(s)` (durée en heures, minutes, secondes).

**J'anticipe.** Pour `s = 3725`, combien d'heures entières ? Quel reste en secondes ? Combien de minutes entières dans ce reste ?

{{ IDE('calculs', MAX="+") }}

## Exercice C – Texte

> [!TIP]
> **Syntaxe utile.** `t[0]` : premier caractère ; `t[-1]` : dernier ; `a + b` : colle deux textes ; `len(t)` : nombre de caractères ; `str(n)` : nombre vers texte ; `int(t)` : texte vers nombre.

Complète `premier_et_dernier(t)`, `entoure(t, c)`, `nb_chiffres_texte(n)` et `somme_de_textes(a, b)`.

{{ IDE('texte', MAX="+") }}

## Exercice D – Conditions

> [!TIP]
> **Syntaxe utile.**
> ```python
> if condition:
>     return ...
> elif autre_condition:
>     return ...
> else:
>     return ...
> ```
> Comparaisons : `<`, `<=`, `>`, `>=`, `==`, `!=`.

Complète `signe(n)`, `plus_grand(a, b)` et `resultat(note)`.

**Je comprends.** Pourquoi `resultat(8)` ne renvoie-t-il pas `"ajourné"` ?

{{ IDE('conditions', MAX="+") }}

## Exercice E – Boucles

> [!TIP]
> **Syntaxe utile.**
> ```python
> for i in range(1, n + 1):    # i vaut 1, 2, ..., n
>     total = total + i
> while condition:             # répète tant que la condition est vraie
>     n = n // 10              # une variable doit changer !
> ```

Complète `somme_jusqua(n)`, `nb_chiffres(n)` et `premiere_puissance(limite)`.

**J'anticipe.** Pour `nb_chiffres(2026)`, écris la trace de `n` et de `compteur` (voir le cours, § VI).

{{ IDE('boucles', MAX="+") }}

## Exercice F – Listes

> [!TIP]
> **Syntaxe utile.** `adresse.split(".")` : découpe un texte en liste de textes ; `for x in liste:` : parcourt la liste ; `liste.append(v)` : ajoute `v` à la fin ; `int(morceau)` : texte vers nombre.

Complète `somme_octets(adresse)`, `compte_superieurs(liste, seuil)` et `liste_carres(n)`.

{{ IDE('listes', MAX="+") }}

## Pour aller plus loin

Dans la console, écris une fonction `est_bissextile(annee)` (divisible par 4, sauf les multiples de 100 qui ne sont pas multiples de 400) et teste-la sur 1900, 2000, 2024, 2026.

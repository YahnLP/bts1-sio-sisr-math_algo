---
render_macros: true
---

# TP Python – Vérifier ses conversions avec Python

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S01*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

> [!TIP]
> **Python est nouveau pour toi ?** Fais d'abord la séance [S00 – Introduction à Python](../S00-introduction-python/README.md) (environ 3 h, hors classe). Avant chaque exercice, un encadré « Syntaxe utile » rappelle les commandes à employer.

## Exercice A – Découvrir `bin`, `hex` et `int`

> [!TIP]
> **Syntaxe utile.** `bin(n)` : texte de l'écriture binaire de `n` (commence par `0b`) ; `hex(n)` : écriture hexadécimale (commence par `0x`) ; `int("1101", 2)` : texte écrit en base 2 vers un entier ; `int("CD", 16)` : idem en base 16 ; `print(...)` : affiche le résultat.

**J'anticipe.** Écris sur ta feuille ce que tu penses voir s'afficher pour `bin(205)`, `hex(205)`, `int("11001101", 2)` et `int("CD", 16)`. Puis lance le script.

{{ IDE('decouvrir_bases', MAX="+") }}

**Je comprends.** `bin` et `hex` renvoient du **texte** commençant par `0b` ou `0x` ; `int(texte, base)` fait la conversion inverse. Compare avec tes réponses du cours (§ III).

## Exercice B – Écrire la conversion en binaire

> [!TIP]
> **Syntaxe utile.** `n % 2` : reste de la division par 2 ; `n // 2` : quotient ; `str(x)` : nombre vers texte ; `a + b` : colle deux textes ; `while n > 0:` : répète tant que `n` est positif ; `reste = n % 2` range un résultat dans une variable.

On reprend la méthode des divisions successives du cours. Complète la fonction `en_binaire(n)` qui renvoie le texte de l'écriture binaire de l'entier naturel `n` (sans préfixe `0b`).

**J'anticipe.** Pour `n = 6`, quels sont les restes successifs ? Dans quel ordre faut-il les assembler ?

{{ IDE('en_binaire', MAX="+") }}

**Contraintes.** N'utilise pas `bin` dans ta fonction : il sert seulement à vérifier. Pense au cas `n = 0`.

## Exercice C – Une base quelconque

> [!TIP]
> **Syntaxe utile.** `CHIFFRES[i]` : le symbole de position `i` dans le texte `CHIFFRES` (par exemple `CHIFFRES[11]` vaut `"B"`) ; `n % b` et `n // b` : reste et quotient de la division par `b` ; `while n > 0:` ; `texte = symbole + texte` : place un symbole à gauche.

Généralise : `vers_base(n, b)` renvoie l'écriture de `n` en base `b` (avec \(2 \le b \le 16\)), les chiffres 10 à 15 s'écrivant `A` à `F`.

{{ IDE('vers_base', MAX="+") }}

## Exercice D – Adresse IPv4 en binaire

> [!TIP]
> **Syntaxe utile.** `adresse.split(".")` : liste des morceaux du texte ; `for x in liste:` : parcourt la liste ; `int(x)` : texte vers nombre ; `format(v, "08b")` : `v` en binaire sur 8 chiffres ; `".".join(liste)` : colle les textes de la liste en les séparant par un point ; `liste.append(v)` : ajoute `v` à la liste.

Écris `ip_en_binaire(adresse)` qui reçoit un texte comme `"192.168.1.10"` et renvoie les quatre octets écrits sur 8 bits, séparés par des points.

*Aide.* `adresse.split(".")` découpe le texte ; `format(x, "08b")` écrit l'entier `x` en binaire sur 8 chiffres.

{{ IDE('ip_en_binaire', MAX="+") }}

## Exercice E – Octet valide ?

> [!TIP]
> **Syntaxe utile.** `texte.isdigit()` : vrai si le texte ne contient que des chiffres ; `int(texte)` : texte vers nombre ; `0 <= v <= 255` : test d'appartenance à un intervalle ; `and`, `not` : et, non ; `return True` / `return False` ; `if condition:` ... `else:`.

Écris `octet_valide(texte)` qui renvoie `True` si `texte` est l'écriture décimale d'un entier entre 0 et 255, et `False` sinon.

*Aide.* `texte.isdigit()` vérifie que le texte ne contient que des chiffres.

{{ IDE('octet_valide', MAX="+") }}

**Je comprends.** Que renvoie ta fonction pour `"256"` ? pour `"-1"` ? pour `""` ? Écris tes réponses avant de tester dans l'éditeur.

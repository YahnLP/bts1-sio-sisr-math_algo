---
author: YLP
title: 🔧 FICHE DE REMÉDIATION
---

# 🔧 FICHE DE REMÉDIATION
## Exercices Ciblés Suite à l'Évaluation Formative S10

## 🎯 Objectifs de la Remédiation

Cette séance de remédiation a pour but de :
- ✅ Reprendre les notions mal comprises en S10
- ✅ Pratiquer avec des exercices guidés
- ✅ Gagner en confiance avant S12
- ✅ Éviter le décrochage

---

## 📊 Structure de la Fiche

Cette fiche contient **3 modules** correspondant aux difficultés fréquentes identifiées :

1. **Module A** : Subnetting (si difficultés sur la partie 1 de l'éval S10)
2. **Module B** : Algorithmique de base (si difficultés sur la partie 2 de l'éval S10)
3. **Module C** : Manipulation de tableaux et listes (si difficultés sur Ex. 5-6-8)

**⚠️ Important :** Votre formateur vous indiquera quel(s) module(s) travailler en fonction de vos résultats en S10.

---

# 📘 MODULE A : SUBNETTING (20 min)

**À faire si vous avez eu des difficultés sur les exercices 1-2-3-4 de S10.**

---

## Exercice A1 : Masques de Base (Facile)

**Complétez le tableau suivant :**

| **CIDR** | **Masque décimal** | **Nombre total d'adresses** | **Nombre d'adresses utilisables** |
|---|---|---|---|
| /24 | 255.255.255.0 | 256 | 254 |
| /25 | _______________ | ________ | ________ |
| /26 | _______________ | ________ | ________ |
| /27 | _______________ | ________ | ________ |

**Rappel des formules :**
- Nombre total d'adresses = 2^(32 - CIDR)
- Nombre d'adresses utilisables = (Nombre total) - 2

---

## Exercice A2 : Calcul d'Adresses Réseau (Moyen)

Pour chaque adresse IP, calculez l'adresse réseau correspondante :

**A2.1** — IP : `192.168.10.50/24`
```
Adresse réseau : _______________________________________
```

**A2.2** — IP : `172.16.45.100/16`
```
Adresse réseau : _______________________________________
```

**A2.3** — IP : `10.0.15.80/26`
```
Adresse réseau : _______________________________________
Astuce : /26 = blocs de 64 → 80 est dans le bloc 64-127
```

---

## Exercice A3 : Découpage Simple (Moyen)

**Contexte :** Vous devez diviser le réseau `192.168.100.0/24` en **2 sous-réseaux** égaux.

**Questions :**

**A3.1** — Quel sera le nouveau masque ?
```
Nouveau CIDR : /______
Nouveau masque : _______________
```

**A3.2** — Donnez les deux sous-réseaux :
```
Sous-réseau 1 : _______________/___
Sous-réseau 2 : _______________/___
```

**A3.3** — Combien d'hôtes utilisables dans chaque sous-réseau ?
```
Nombre d'hôtes utilisables : ________
```

---

## ✅ Correction Module A

### Exercice A1

| **CIDR** | **Masque décimal** | **Nombre total** | **Utilisables** |
|---|---|---|---|
| /24 | 255.255.255.0 | 256 | 254 |
| /25 | 255.255.255.128 | 128 | 126 |
| /26 | 255.255.255.192 | 64 | 62 |
| /27 | 255.255.255.224 | 32 | 30 |

### Exercice A2

**A2.1** — `192.168.10.0`
**A2.2** — `172.16.0.0`
**A2.3** — `10.0.15.64` (bloc 64-127)

### Exercice A3

**A3.1** — `/25` (255.255.255.128)
**A3.2** — `192.168.100.0/25` et `192.168.100.128/25`
**A3.3** — 126 hôtes utilisables par sous-réseau

---

---

# 📘 MODULE B : ALGORITHMIQUE DE BASE (20 min)

**À faire si vous avez eu des difficultés sur les exercices 5-7 de S10.**

---

## Exercice B1 : Boucles FOR (Facile)

**Écrivez un algorithme en pseudo-code qui affiche tous les nombres de 1 à 10.**

```
ALGORITHME AfficherNombres
VARIABLES
    i : entier

DÉBUT
    // Complétez ici
    _________________________________________________________________
    _________________________________________________________________
    _________________________________________________________________
    _________________________________________________________________
FIN
```

**Résultat attendu :**
```
1
2
3
4
5
6
7
8
9
10
```

---

## Exercice B2 : Parcours de Tableau (Moyen)

**Contexte :** Soit le tableau suivant : `[10, 20, 30, 40, 50]`

**Écrivez un algorithme qui affiche chaque élément du tableau.**

```
ALGORITHME ParcoursTableau
VARIABLES
    tableau : TABLEAU d'entiers
    i : entier
    n : entier

DÉBUT
    tableau ← [10, 20, 30, 40, 50]
    n ← longueur(tableau)
    
    // Complétez ici
    _________________________________________________________________
    _________________________________________________________________
    _________________________________________________________________
    _________________________________________________________________
FIN
```

**Résultat attendu :**
```
10
20
30
40
50
```

---

## Exercice B3 : Condition IF (Moyen)

**Écrivez un algorithme qui affiche "Pair" si un nombre est pair, "Impair" sinon.**

**Rappel :** Un nombre est pair si le reste de sa division par 2 est 0. En pseudo-code : `nombre MODULO 2 = 0`

```
ALGORITHME PairOuImpair
VARIABLES
    nombre : entier

DÉBUT
    AFFICHER "Entrez un nombre : "
    LIRE nombre
    
    // Complétez ici
    _________________________________________________________________
    _________________________________________________________________
    _________________________________________________________________
    _________________________________________________________________
    _________________________________________________________________
FIN
```

---

## Exercice B4 : Recherche dans un Tableau (Moyen à Difficile)

**Écrivez un algorithme qui recherche si le nombre 30 est présent dans le tableau `[10, 20, 30, 40, 50]`.**

```
ALGORITHME RechercherNombre
VARIABLES
    tableau : TABLEAU d'entiers
    recherche : entier
    i : entier
    n : entier
    trouve : booléen

DÉBUT
    tableau ← [10, 20, 30, 40, 50]
    recherche ← 30
    n ← longueur(tableau)
    trouve ← FAUX
    
    // Complétez ici
    _________________________________________________________________
    _________________________________________________________________
    _________________________________________________________________
    _________________________________________________________________
    _________________________________________________________________
    _________________________________________________________________
    _________________________________________________________________
    _________________________________________________________________
    _________________________________________________________________
FIN
```

---

## ✅ Correction Module B

### Exercice B1

```
ALGORITHME AfficherNombres
VARIABLES
    i : entier

DÉBUT
    POUR i DE 1 À 10 FAIRE
        AFFICHER i
    FIN POUR
FIN
```

### Exercice B2

```
ALGORITHME ParcoursTableau
VARIABLES
    tableau : TABLEAU d'entiers
    i : entier
    n : entier

DÉBUT
    tableau ← [10, 20, 30, 40, 50]
    n ← longueur(tableau)
    
    POUR i DE 0 À n-1 FAIRE
        AFFICHER tableau[i]
    FIN POUR
FIN
```

### Exercice B3

```
ALGORITHME PairOuImpair
VARIABLES
    nombre : entier

DÉBUT
    AFFICHER "Entrez un nombre : "
    LIRE nombre
    
    SI nombre MODULO 2 = 0 ALORS
        AFFICHER "Pair"
    SINON
        AFFICHER "Impair"
    FIN SI
FIN
```

### Exercice B4

```
ALGORITHME RechercherNombre
VARIABLES
    tableau : TABLEAU d'entiers
    recherche : entier
    i : entier
    n : entier
    trouve : booléen

DÉBUT
    tableau ← [10, 20, 30, 40, 50]
    recherche ← 30
    n ← longueur(tableau)
    trouve ← FAUX
    
    POUR i DE 0 À n-1 FAIRE
        SI tableau[i] = recherche ALORS
            trouve ← VRAI
            SORTIR DE LA BOUCLE
        FIN SI
    FIN POUR
    
    SI trouve = VRAI ALORS
        AFFICHER "Le nombre 30 est présent"
    SINON
        AFFICHER "Le nombre 30 n'est pas présent"
    FIN SI
FIN
```

---

---

# 📘 MODULE C : TABLEAUX ET LISTES (20 min)

**À faire si vous avez eu des difficultés sur les exercices 5-6-8 de S10.**

---

## Exercice C1 : Accès par Indice (Facile)

Soit le tableau Python suivant :

```python
serveurs = ["SRV-01", "SRV-02", "SRV-03", "SRV-04", "SRV-05"]
```

**Questions :**

**C1.1** — Quelle est la valeur de `serveurs[0]` ?
```
Réponse : _______________________
```

**C1.2** — Quelle est la valeur de `serveurs[2]` ?
```
Réponse : _______________________
```

**C1.3** — Quelle est la valeur de `serveurs[-1]` ?
```
Réponse : _______________________
```

**C1.4** — Combien d'éléments contient ce tableau ?
```
Réponse : _______________________
```

---

## Exercice C2 : Manipulation de Listes (Moyen)

Soit la liste Python suivante :

```python
tickets = ["#001", "#002", "#003"]
```

**Écrivez le code Python pour effectuer les opérations suivantes :**

**C2.1** — Ajouter le ticket `"#004"` à la fin de la liste.
```python
_________________________________________________________________
```

**C2.2** — Supprimer le ticket `"#002"` de la liste.
```python
_________________________________________________________________
```

**C2.3** — Afficher tous les tickets restants.
```python
_________________________________________________________________
_________________________________________________________________
```

---

## Exercice C3 : Parcours avec Condition (Moyen)

**Écrivez un algorithme en pseudo-code qui parcourt le tableau `[8, 16, 4, 32, 12]` et affiche "Petit" pour les valeurs inférieures à 10.**

```
ALGORITHME ParcoursAvecCondition
VARIABLES
    valeurs : TABLEAU d'entiers
    i : entier
    n : entier

DÉBUT
    valeurs ← [8, 16, 4, 32, 12]
    n ← longueur(valeurs)
    
    // Complétez ici
    _________________________________________________________________
    _________________________________________________________________
    _________________________________________________________________
    _________________________________________________________________
    _________________________________________________________________
    _________________________________________________________________
FIN
```

**Résultat attendu :**
```
Petit
Petit
```

---

## Exercice C4 : Double Tableau (Difficile)

**Contexte :** Vous avez deux tableaux :
- `noms = ["Alice", "Bob", "Charlie"]`
- `ages = [25, 30, 22]`

**Écrivez un algorithme qui affiche chaque nom avec son âge :**

```
ALGORITHME AfficherNomsEtAges
VARIABLES
    noms : TABLEAU de chaînes
    ages : TABLEAU d'entiers
    i : entier
    n : entier

DÉBUT
    noms ← ["Alice", "Bob", "Charlie"]
    ages ← [25, 30, 22]
    n ← 3
    
    // Complétez ici
    _________________________________________________________________
    _________________________________________________________________
    _________________________________________________________________
    _________________________________________________________________
FIN
```

**Résultat attendu :**
```
Alice a 25 ans
Bob a 30 ans
Charlie a 22 ans
```

---

## ✅ Correction Module C

### Exercice C1

**C1.1** — `"SRV-01"`
**C1.2** — `"SRV-03"`
**C1.3** — `"SRV-05"` (dernier élément)
**C1.4** — 5 éléments

### Exercice C2

**C2.1** — `tickets.append("#004")`
**C2.2** — `tickets.remove("#002")` ou `del tickets[1]`
**C2.3** —
```python
for ticket in tickets:
    print(ticket)
```

### Exercice C3

```
ALGORITHME ParcoursAvecCondition
VARIABLES
    valeurs : TABLEAU d'entiers
    i : entier
    n : entier

DÉBUT
    valeurs ← [8, 16, 4, 32, 12]
    n ← longueur(valeurs)
    
    POUR i DE 0 À n-1 FAIRE
        SI valeurs[i] < 10 ALORS
            AFFICHER "Petit"
        FIN SI
    FIN POUR
FIN
```

### Exercice C4

```
ALGORITHME AfficherNomsEtAges
VARIABLES
    noms : TABLEAU de chaînes
    ages : TABLEAU d'entiers
    i : entier
    n : entier

DÉBUT
    noms ← ["Alice", "Bob", "Charlie"]
    ages ← [25, 30, 22]
    n ← 3
    
    POUR i DE 0 À n-1 FAIRE
        AFFICHER noms[i], " a ", ages[i], " ans"
    FIN POUR
FIN
```

---

---

# 📊 GRILLE DE SUIVI PERSONNALISÉ

**À remplir par l'étudiant (avec l'aide de l'enseignant si besoin) :**

| **Module** | **Exercices réalisés** | **Niveau de réussite** | **Notions à revoir** |
|---|---|---|---|
| **Module A (Subnetting)** | ☐ A1  ☐ A2  ☐ A3 | ☐ ✅  ☐ 🟡  ☐ ❌ | _________________ |
| **Module B (Algorithmique)** | ☐ B1  ☐ B2  ☐ B3  ☐ B4 | ☐ ✅  ☐ 🟡  ☐ ❌ | _________________ |
| **Module C (Tableaux)** | ☐ C1  ☐ C2  ☐ C3  ☐ C4 | ☐ ✅  ☐ 🟡  ☐ ❌ | _________________ |

**Légende :**
- ✅ = Bien compris, je peux passer à autre chose
- 🟡 = Compris partiellement, à retravailler à la maison
- ❌ = Pas compris, besoin d'aide supplémentaire

---

## 🎯 Plan d'Action Personnalisé

**À remplir avec l'enseignant :**

### Points Forts Identifiés

```
___________________________________________________________________
___________________________________________________________________
```

### Points à Travailler en Priorité

```
1. _________________________________________________________________
2. _________________________________________________________________
3. _________________________________________________________________
```

### Exercices Supplémentaires à Faire à la Maison

```
☐ _________________________________________________________________
☐ _________________________________________________________________
☐ _________________________________________________________________
```

### Rendez-vous de Suivi

```
Prochain point avec l'enseignant : Semaine _____ (S____)
```

---

## 📚 Ressources Complémentaires

**Si vous souhaitez vous entraîner davantage :**

### Subnetting
- [Subnet Calculator](https://www.subnet-calculator.com/) — Calculatrice en ligne
- [Subnetting Practice](https://subnettingpractice.com/) — Exercices interactifs

### Algorithmique
- [France IOI](https://www.france-ioi.org/) — Plateforme d'apprentissage de l'algorithmique
- [CodinGame](https://www.codingame.com/) — Apprendre en s'amusant

### Python
- [Python Tutor](https://pythontutor.com/) — Visualiser l'exécution du code
- [Codecademy Python](https://www.codecademy.com/learn/learn-python-3) — Cours interactif

---

---
author: YLP
title: 📚 FICHE DE COURS
---


# 📚 FICHE DE COURS ÉLÈVE
## Algorithmes de Tri : Tri à Bulles et Tri par Insertion

*Version 1.0 — BTS SIO SISR — Année 1 — Semaine 11*

---

## 🎯 Compétences Travaillées

| **Code** | **Compétence** |
|----------|----------------|
| **B1.1** | Gérer le patrimoine informatique |
| **B1.2** | Répondre aux incidents et aux demandes d'assistance |
| **B2.1** | Administrer les systèmes et les services informatiques |


---

## 📖 I. Introduction : Pourquoi Trier ?

### Le Problème

En tant que technicien SISR, vous manipulez constamment des données qui doivent être **organisées** :
- 📋 Trier les tickets d'incidents par priorité
- 🖥️ Trier les serveurs par charge CPU
- 📊 Trier les logs par timestamp
- 📈 Trier les utilisateurs par ordre alphabétique
- 💾 Trier les sauvegardes par date

**Question :** Comment organiser efficacement ces données ?

### La Solution : Les Algorithmes de Tri

Un **algorithme de tri** est une séquence d'instructions qui permet de réorganiser une collection d'éléments dans un ordre spécifique (croissant, décroissant, alphabétique, etc.).

**Les deux algorithmes étudiés :**
1. **Tri à bulles** (Bubble Sort) — simple mais lent
2. **Tri par insertion** (Insertion Sort) — plus efficace

---

## 🫧 II. Le Tri à Bulles (Bubble Sort)

### Principe Général

> Le **tri à bulles** consiste à **comparer des éléments adjacents** et à les **échanger** s'ils sont dans le mauvais ordre. On répète cette opération jusqu'à ce que tout soit trié.

### Analogie Physique

![Illustration : Des bulles d'air dans l'eau qui remontent progressivement vers la surface]
*Légende : Le tri à bulles tire son nom des bulles d'air qui remontent dans l'eau. Les éléments "lourds" descendent et les "légers" remontent, comme des bulles.*

**Métaphore :**
Imaginez des bulles d'air dans un verre d'eau. Les plus grosses bulles (valeurs grandes) remontent naturellement vers le haut, tandis que les plus petites restent en bas.

### Fonctionnement Détaillé

**Exemple : Trier le tableau [5, 2, 8, 1, 9] par ordre croissant**

#### 🔄 Premier Passage

On parcourt le tableau et on compare chaque élément avec son voisin de droite :

```
Étape 1 : Comparer 5 et 2
[5, 2, 8, 1, 9]  →  5 > 2 ? OUI → ÉCHANGER
[2, 5, 8, 1, 9]

Étape 2 : Comparer 5 et 8
[2, 5, 8, 1, 9]  →  5 > 8 ? NON → PAS D'ÉCHANGE
[2, 5, 8, 1, 9]

Étape 3 : Comparer 8 et 1
[2, 5, 8, 1, 9]  →  8 > 1 ? OUI → ÉCHANGER
[2, 5, 1, 8, 9]

Étape 4 : Comparer 8 et 9
[2, 5, 1, 8, 9]  →  8 > 9 ? NON → PAS D'ÉCHANGE
[2, 5, 1, 8, 9]
```

**Résultat après le 1er passage :** `[2, 5, 1, 8, 9]`

➡️ **Observation :** Le plus grand élément (9) est maintenant à sa place finale !

![Illustration : Tableau de 5 cases avec des flèches montrant les comparaisons successives entre cases adjacentes]
*Légende : Visualisation du premier passage du tri à bulles avec les comparaisons et échanges.*

#### 🔄 Deuxième Passage

On recommence, mais on peut ignorer le dernier élément (déjà trié) :

```
Étape 1 : Comparer 2 et 5
[2, 5, 1, 8, 9]  →  2 > 5 ? NON → PAS D'ÉCHANGE

Étape 2 : Comparer 5 et 1
[2, 5, 1, 8, 9]  →  5 > 1 ? OUI → ÉCHANGER
[2, 1, 5, 8, 9]

Étape 3 : Comparer 5 et 8
[2, 1, 5, 8, 9]  →  5 > 8 ? NON → PAS D'ÉCHANGE
[2, 1, 5, 8, 9]
```

**Résultat après le 2ème passage :** `[2, 1, 5, 8, 9]`

➡️ Le deuxième plus grand (8) est maintenant à sa place !

#### 🔄 Troisième Passage

```
Étape 1 : Comparer 2 et 1
[2, 1, 5, 8, 9]  →  2 > 1 ? OUI → ÉCHANGER
[1, 2, 5, 8, 9]

Étape 2 : Comparer 2 et 5
[1, 2, 5, 8, 9]  →  2 > 5 ? NON → PAS D'ÉCHANGE
[1, 2, 5, 8, 9]
```

**Résultat après le 3ème passage :** `[1, 2, 5, 8, 9]`

✅ **Le tableau est maintenant complètement trié !**

### Pseudo-Code du Tri à Bulles

```
ALGORITHME TriABulles
VARIABLES
    tableau : TABLEAU d'entiers
    n : entier (taille du tableau)
    i, j : entiers (indices)
    temp : entier (variable temporaire pour l'échange)

DÉBUT
    n ← longueur(tableau)
    
    // Boucle externe : nombre de passages
    POUR i DE 0 À n-2 FAIRE
        
        // Boucle interne : comparaisons dans un passage
        POUR j DE 0 À n-2-i FAIRE
            
            // Si deux éléments adjacents sont dans le mauvais ordre
            SI tableau[j] > tableau[j+1] ALORS
                // Les échanger
                temp ← tableau[j]
                tableau[j] ← tableau[j+1]
                tableau[j+1] ← temp
            FIN SI
            
        FIN POUR
        
    FIN POUR
    
FIN
```

### Code Python du Tri à Bulles

```python
def tri_a_bulles(tableau):
    """
    Trie un tableau par ordre croissant en utilisant le tri à bulles.
    """
    n = len(tableau)
    
    # Boucle externe : nombre de passages
    for i in range(n - 1):
        
        # Boucle interne : comparaisons dans un passage
        for j in range(n - 1 - i):
            
            # Si deux éléments adjacents sont dans le mauvais ordre
            if tableau[j] > tableau[j + 1]:
                # Les échanger
                tableau[j], tableau[j + 1] = tableau[j + 1], tableau[j]
    
    return tableau

# Exemple d'utilisation
serveurs = [5, 2, 8, 1, 9]
print("Avant tri :", serveurs)
tri_a_bulles(serveurs)
print("Après tri :", serveurs)
```

### Avantages et Inconvénients du Tri à Bulles

| **Avantages** | **Inconvénients** |
|---|---|
| ✅ Très simple à comprendre | ❌ Très lent sur de grandes données |
| ✅ Facile à coder | ❌ Beaucoup de comparaisons inutiles |
| ✅ Ne nécessite pas de mémoire supplémentaire | ❌ Inefficace même sur des données presque triées |

**🎓 À retenir :** Le tri à bulles est excellent pour **apprendre** les algorithmes de tri, mais on ne l'utilise **jamais en production** car il est trop lent.

---

## 📥 III. Le Tri par Insertion (Insertion Sort)

### Principe Général

> Le **tri par insertion** consiste à construire progressivement une **partie triée** du tableau en insérant chaque nouvel élément à sa bonne place dans cette partie triée.

### Analogie Physique

![Illustration : Une main qui tient des cartes triées et insère une nouvelle carte au bon endroit]
*Légende : Le tri par insertion fonctionne comme lorsqu'on trie des cartes dans sa main : on insère chaque nouvelle carte à sa place dans la partie déjà triée.*

**Métaphore :**
Imaginez que vous triez des cartes à jouer dans votre main :
1. Vous prenez la première carte (elle est déjà "triée")
2. Vous prenez la deuxième carte et l'insérez au bon endroit par rapport à la première
3. Vous prenez la troisième carte et l'insérez au bon endroit dans les deux déjà triées
4. Et ainsi de suite...

### Fonctionnement Détaillé

**Exemple : Trier le tableau [5, 2, 8, 1, 9] par ordre croissant**

#### 🔄 Étape 1 : Le premier élément est déjà "trié"

```
[5 | 2, 8, 1, 9]
 ↑
Partie triée
```

#### 🔄 Étape 2 : Insérer 2 dans la partie triée

```
On prend 2 et on le compare avec 5
2 < 5 ? OUI → On insère 2 avant 5

[2, 5 | 8, 1, 9]
    ↑
Partie triée
```

#### 🔄 Étape 3 : Insérer 8 dans la partie triée

```
On prend 8 et on le compare avec 5
8 > 5 ? OUI → 8 reste à sa place

[2, 5, 8 | 1, 9]
       ↑
Partie triée
```

#### 🔄 Étape 4 : Insérer 1 dans la partie triée

```
On prend 1 et on le compare avec 8, puis 5, puis 2
1 < 2 ? OUI → On insère 1 avant tout

[1, 2, 5, 8 | 9]
          ↑
Partie triée
```

#### 🔄 Étape 5 : Insérer 9 dans la partie triée

```
On prend 9 et on le compare avec 8
9 > 8 ? OUI → 9 reste à sa place

[1, 2, 5, 8, 9]
             ↑
Tout est trié !
```

![Illustration : 5 étapes montrant la progression de la partie triée (en vert) et non triée (en gris)]
*Légende : Visualisation du tri par insertion : la partie triée (à gauche) grandit progressivement.*

### Pseudo-Code du Tri par Insertion

```
ALGORITHME TriParInsertion
VARIABLES
    tableau : TABLEAU d'entiers
    n : entier (taille du tableau)
    i, j : entiers (indices)
    cle : entier (élément à insérer)

DÉBUT
    n ← longueur(tableau)
    
    // Parcourir le tableau à partir du 2ème élément
    POUR i DE 1 À n-1 FAIRE
        
        // Prendre l'élément à insérer
        cle ← tableau[i]
        j ← i - 1
        
        // Déplacer les éléments plus grands vers la droite
        TANT QUE (j >= 0 ET tableau[j] > cle) FAIRE
            tableau[j+1] ← tableau[j]
            j ← j - 1
        FIN TANT QUE
        
        // Insérer l'élément à sa place
        tableau[j+1] ← cle
        
    FIN POUR
    
FIN
```

### Code Python du Tri par Insertion

```python
def tri_par_insertion(tableau):
    """
    Trie un tableau par ordre croissant en utilisant le tri par insertion.
    """
    n = len(tableau)
    
    # Parcourir le tableau à partir du 2ème élément
    for i in range(1, n):
        
        # Prendre l'élément à insérer
        cle = tableau[i]
        j = i - 1
        
        # Déplacer les éléments plus grands vers la droite
        while j >= 0 and tableau[j] > cle:
            tableau[j + 1] = tableau[j]
            j -= 1
        
        # Insérer l'élément à sa place
        tableau[j + 1] = cle
    
    return tableau

# Exemple d'utilisation
serveurs = [5, 2, 8, 1, 9]
print("Avant tri :", serveurs)
tri_par_insertion(serveurs)
print("Après tri :", serveurs)
```

### Avantages et Inconvénients du Tri par Insertion

| **Avantages** | **Inconvénients** |
|---|---|
| ✅ Efficace sur de petites données | ❌ Lent sur de grandes données |
| ✅ Très efficace si les données sont presque triées | ❌ Moins intuitif que le tri à bulles |
| ✅ Ne nécessite pas de mémoire supplémentaire | ❌ Beaucoup de déplacements d'éléments |
| ✅ Plus rapide que le tri à bulles | |

**🎓 À retenir :** Le tri par insertion est utilisé en pratique pour **de petites listes** ou des **données presque triées**.

---

## ⚖️ IV. Comparaison : Tri à Bulles vs Tri par Insertion

### Tableau Comparatif

| **Critère** | **Tri à Bulles** | **Tri par Insertion** |
|---|---|---|
| **Principe** | Échanger les éléments adjacents | Insérer chaque élément à sa place |
| **Métaphore** | Bulles qui remontent | Cartes à trier dans la main |
| **Complexité** | O(n²) — quadratique | O(n²) — quadratique (mais plus rapide en pratique) |
| **Nombre de comparaisons** | Beaucoup (même sur données presque triées) | Peu si les données sont presque triées |
| **Facilité de compréhension** | ⭐⭐⭐⭐⭐ Très facile | ⭐⭐⭐ Moyenne |
| **Utilisation en pratique** | ❌ Jamais (trop lent) | ✅ Oui (petites données) |

### Visualisation Comparative

**Sur un tableau de 5 éléments déjà trié : [1, 2, 3, 4, 5]**

| **Algorithme** | **Nombre de comparaisons** | **Nombre d'échanges** |
|---|---|---|
| **Tri à bulles** | 10 comparaisons | 0 échange |
| **Tri par insertion** | 4 comparaisons | 0 échange |

➡️ Le tri par insertion est **plus rapide** sur des données déjà triées ou presque triées.

### Exemple Visuel

![Illustration : Deux colonnes côte à côte montrant le tri à bulles (gauche) avec beaucoup de flèches d'échange, et le tri par insertion (droite) avec des éléments qui s'insèrent directement]
*Légende : Comparaison visuelle : le tri à bulles fait beaucoup d'échanges, le tri par insertion insère directement.*

---

## 💡 V. Application SISR : Trier des Serveurs par Charge CPU

### Contexte

Vous êtes technicien SISR et vous devez surveiller la charge de 5 serveurs. Vous souhaitez les afficher **du moins chargé au plus chargé** pour identifier rapidement les serveurs disponibles.

**Données initiales :**

| **Serveur** | **Charge CPU (%)** |
|---|---|
| SRV-WEB-01 | 75 |
| SRV-DB-01 | 42 |
| SRV-MAIL-01 | 88 |
| SRV-FILE-01 | 15 |
| SRV-APP-01 | 63 |

### Solution avec le Tri par Insertion

#### Étape 1 : Représentation en Tableau

```python
charges_cpu = [75, 42, 88, 15, 63]
noms_serveurs = ["SRV-WEB-01", "SRV-DB-01", "SRV-MAIL-01", 
                  "SRV-FILE-01", "SRV-APP-01"]
```

#### Étape 2 : Algorithme de Tri (Pseudo-Code)

```
ALGORITHME TriServeursParChargeCPU
VARIABLES
    charges : TABLEAU d'entiers
    serveurs : TABLEAU de chaînes
    n : entier
    i, j : entiers
    cle_charge : entier
    cle_serveur : chaîne

DÉBUT
    n ← longueur(charges)
    
    // Tri par insertion sur les charges CPU
    POUR i DE 1 À n-1 FAIRE
        
        cle_charge ← charges[i]
        cle_serveur ← serveurs[i]
        j ← i - 1
        
        // Déplacer les serveurs plus chargés vers la droite
        TANT QUE (j >= 0 ET charges[j] > cle_charge) FAIRE
            charges[j+1] ← charges[j]
            serveurs[j+1] ← serveurs[j]
            j ← j - 1
        FIN TANT QUE
        
        // Insérer le serveur à sa place
        charges[j+1] ← cle_charge
        serveurs[j+1] ← cle_serveur
        
    FIN POUR
    
    // Afficher les serveurs triés
    POUR i DE 0 À n-1 FAIRE
        AFFICHER serveurs[i], " : ", charges[i], "%"
    FIN POUR
    
FIN
```

#### Étape 3 : Résultat Attendu

```
SRV-FILE-01 : 15%
SRV-DB-01 : 42%
SRV-APP-01 : 63%
SRV-WEB-01 : 75%
SRV-MAIL-01 : 88%
```

**Interprétation :**
- ✅ **SRV-FILE-01** est le moins chargé (15%) → peut accueillir de nouvelles tâches
- ⚠️ **SRV-MAIL-01** est le plus chargé (88%) → à surveiller ou à libérer

---

## 🔑 VI. Vocabulaire Clé à Maîtriser

| **Terme** | **Définition** |
|---|---|
| **Algorithme de tri** | Séquence d'instructions pour réorganiser des éléments dans un ordre spécifique |
| **Tri à bulles** | Algorithme qui compare et échange des éléments adjacents |
| **Tri par insertion** | Algorithme qui insère chaque élément à sa place dans une partie triée |
| **Comparaison** | Action de vérifier si un élément est plus grand/petit qu'un autre |
| **Échange** | Action de permuter deux éléments dans un tableau |
| **Passage** | Une itération complète de l'algorithme sur tout le tableau |
| **Complexité** | Mesure de l'efficacité d'un algorithme (temps d'exécution) |
| **Ordre croissant** | Du plus petit au plus grand (1, 2, 3, 4, 5) |
| **Ordre décroissant** | Du plus grand au plus petit (5, 4, 3, 2, 1) |

---

## 🎯 VII. Points Clés à Retenir

### ✅ Les 5 Règles d'Or

1. **Trier = organiser** : Le tri est essentiel pour exploiter efficacement des données.

2. **Plusieurs algorithmes existent** : Tri à bulles, tri par insertion, tri par sélection, tri fusion, tri rapide...

3. **Tri à bulles = simple mais lent** : Facile à comprendre, mais inefficace en pratique.

4. **Tri par insertion = plus efficace** : Meilleur choix pour de petites données ou données presque triées.

5. **Choisir selon le contexte** : La taille des données et leur état initial influencent le choix de l'algorithme.

### ⚠️ Erreurs Fréquentes

❌ **Erreur 1 : Oublier de comparer avec l'élément adjacent**
```python
# INCORRECT (tri à bulles)
if tableau[i] > tableau[i+2]:  # On saute un élément !
```

❌ **Erreur 2 : Oublier de déplacer les éléments dans le tri par insertion**
```python
# INCORRECT (tri par insertion)
tableau[i] = cle  # On écrase sans avoir déplacé les autres !
```

❌ **Erreur 3 : Mélanger les deux algorithmes**
- Ne pas confondre : **échange** (bulles) et **insertion** (insertion)

---

## 📝 Fiche de Référence Pseudo-Code (Aide-Mémoire)

**À garder sous les yeux pendant les exercices :**

```
═══════════════════════════════════════════════════════════════
ALGORITHMES DE TRI - AIDE-MÉMOIRE
═══════════════════════════════════════════════════════════════

--- TRI À BULLES ---
POUR i DE 0 À n-2 FAIRE
    POUR j DE 0 À n-2-i FAIRE
        SI tableau[j] > tableau[j+1] ALORS
            échanger tableau[j] et tableau[j+1]
        FIN SI
    FIN POUR
FIN POUR

--- TRI PAR INSERTION ---
POUR i DE 1 À n-1 FAIRE
    cle ← tableau[i]
    j ← i - 1
    TANT QUE (j >= 0 ET tableau[j] > cle) FAIRE
        tableau[j+1] ← tableau[j]
        j ← j - 1
    FIN TANT QUE
    tableau[j+1] ← cle
FIN POUR

═══════════════════════════════════════════════════════════════
```

---

## 📊 Quand Utiliser Quel Algorithme ?

| **Situation** | **Algorithme recommandé** |
|---|---|
| Apprentissage des algorithmes de tri | **Tri à bulles** (pédagogique) |
| Petite liste (< 20 éléments) | **Tri par insertion** |
| Données presque déjà triées | **Tri par insertion** |
| Grande liste (> 100 éléments) | **Tri rapide** ou **Tri fusion** (hors programme) |
| Production réelle | **Jamais le tri à bulles !** |

---

## 🚀 Pour Aller Plus Loin (Facultatif)

### Autres Algorithmes de Tri

**Algorithmes plus avancés (non au programme) :**
- **Tri par sélection** : Chercher le minimum à chaque fois
- **Tri fusion (Merge Sort)** : Diviser pour régner — O(n log n)
- **Tri rapide (Quick Sort)** : Le plus utilisé en pratique — O(n log n)
- **Tri par tas (Heap Sort)** : Utilise une structure de tas — O(n log n)

### Notion de Complexité

**La notation "Grand O" :**
- **O(n²)** : Temps quadratique (tri à bulles, tri par insertion)
- **O(n log n)** : Temps quasi-linéaire (tri fusion, tri rapide)
- **O(n)** : Temps linéaire (tri par comptage — cas spéciaux)

Plus le "O" est petit, plus l'algorithme est rapide.

---

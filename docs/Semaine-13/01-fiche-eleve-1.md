---
author: YLP
title: 📖 FICHE DE COURS
---

# 📖 FICHE DE COURS ÉLÈVE
## S13 — Ensembles et Relations : Appartenance, Union, Intersection, Groupes AD

*Version 1.0 — BTS SIO SISR — Année 1 — Semaine 13*

---

## 🎯 Objectifs de la Séance

À la fin de cette séance, je serai capable de :

✅ Définir un ensemble et ses propriétés  
✅ Utiliser la notation mathématique : `{a, b, c}`, `∈`, `∉`, `⊂`, `⊃`  
✅ Distinguer appartenance (∈) et inclusion (⊂)  
✅ Effectuer les opérations : union (∪), intersection (∩), différence (\\)  
✅ Représenter des ensembles avec des diagrammes de Venn  
✅ **Modéliser les groupes Active Directory comme des ensembles**  
✅ **Manipuler des ensembles en Python avec `set()`**

---

## 📚 Vocabulaire Clé à Maîtriser

| **Terme** | **Définition** | **Exemple** |
|-----------|----------------|-------------|
| **Ensemble** | Collection d'éléments distincts, sans ordre ni doublons | `{1, 2, 3}` ou `{Alice, Bob}` |
| **Élément** | Objet contenu dans un ensemble | `2` est un élément de `{1, 2, 3}` |
| **Appartenance** | Relation entre un élément et un ensemble (symbole ∈) | `Alice ∈ IT` |
| **Inclusion** | Relation entre deux ensembles (un est contenu dans l'autre, symbole ⊂) | `IT ⊂ Tous_Utilisateurs` |
| **Union** | Ensemble contenant tous les éléments de A et de B | `A ∪ B` |
| **Intersection** | Ensemble des éléments communs à A et B | `A ∩ B` |
| **Différence** | Ensemble des éléments de A qui ne sont pas dans B | `A \ B` ou `A - B` |
| **Ensemble vide** | Ensemble ne contenant aucun élément | `∅` ou `{}` |
| **Cardinal** | Nombre d'éléments dans un ensemble | `|{1, 2, 3}| = 3` |

---

## 1️⃣ Qu'est-ce qu'un Ensemble ?

### Définition

Un **ensemble** est une **collection d'objets distincts**, appelés **éléments**. Les ensembles ont 3 propriétés fondamentales :

1. **Pas d'ordre** : `{1, 2, 3}` = `{3, 1, 2}` (même ensemble)
2. **Pas de doublons** : `{1, 1, 2}` = `{1, 2}` (les répétitions sont ignorées)
3. **Éléments bien définis** : On peut toujours dire si un élément appartient ou non

### Notation Mathématique

**En extension (on liste les éléments) :**
```
A = {Alice, Bob, Charlie}
B = {1, 2, 3, 4, 5}
C = {Rouge, Vert, Bleu}
```

**En compréhension (on donne une règle) :**
```
P = {x | x est un nombre pair positif inférieur à 10}
    → P = {2, 4, 6, 8}

Admins = {u | u a des droits d'administration sur le serveur}
```

### Cardinal d'un Ensemble

Le **cardinal** (ou **cardinalité**) est le nombre d'éléments dans un ensemble.

**Notation :** `|A|` ou `card(A)` ou en Python : `len(A)`

**Exemples :**
```
A = {1, 2, 3, 4, 5}     → |A| = 5
IT = {Alice, Bob}       → |IT| = 2
∅ = {}                  → |∅| = 0 (ensemble vide)
```

---

## 2️⃣ Appartenance et Inclusion

### A. Appartenance (∈ et ∉)

Un **élément** appartient (ou n'appartient pas) à un **ensemble**.

**Notation :**
- `a ∈ A` : "a appartient à A"
- `a ∉ A` : "a n'appartient pas à A"

**Exemples :**
```
IT = {Alice, Bob, Charlie}

Alice ∈ IT        ✅ Vrai (Alice est dans le groupe IT)
Diane ∉ IT        ✅ Vrai (Diane n'est pas dans le groupe IT)
Bob ∈ RH          ❌ Faux (Bob n'est pas dans le groupe RH)
```

**En Python :**
```python
IT = {"Alice", "Bob", "Charlie"}

print("Alice" in IT)    # True
print("Diane" in IT)    # False
print("Bob" not in IT)  # False
```

---

### B. Inclusion (⊂ et ⊃)

Un **ensemble** est inclus (ou contient) un autre **ensemble**.

**Notation :**
- `A ⊂ B` : "A est inclus dans B" (tous les éléments de A sont dans B)
- `B ⊃ A` : "B contient A" (même chose, dit dans l'autre sens)

**Exemples :**
```
IT = {Alice, Bob, Charlie}
Managers = {Alice, Diane, Eve}
Tous_Utilisateurs = {Alice, Bob, Charlie, Diane, Eve, Frank, ...}

IT ⊂ Tous_Utilisateurs        ✅ Vrai (tous les IT sont des utilisateurs)
Managers ⊂ Tous_Utilisateurs  ✅ Vrai (tous les managers sont des utilisateurs)
IT ⊂ Managers                 ❌ Faux (Bob et Charlie ne sont pas managers)
```

**Inclusion stricte vs large :**
- `A ⊂ B` : Inclusion large (A peut être égal à B)
- `A ⊊ B` : Inclusion stricte (A est strictement inclus dans B, A ≠ B)

---

### 🚨 ATTENTION : Ne Pas Confondre ∈ et ⊂

| **Concept** | **Notation** | **Se lit** | **Exemple** |
|-------------|--------------|------------|-------------|
| **Appartenance** | `a ∈ A` | "a est un élément de A" | `Alice ∈ IT` |
| **Inclusion** | `A ⊂ B` | "A est inclus dans B" | `IT ⊂ Tous_Utilisateurs` |

**❌ ERREUR FRÉQUENTE :**
```
IT ∈ Tous_Utilisateurs  ❌ FAUX ! IT est un groupe, pas un utilisateur
IT ⊂ Tous_Utilisateurs  ✅ VRAI ! IT est un sous-ensemble
```

**[ILLUSTRATION 1 : Schéma appartenance vs inclusion]**  
*Légende : Deux diagrammes côte à côte. Gauche : un point "Alice" dans un cercle "IT" avec la flèche "∈". Droite : un petit cercle "IT" entièrement contenu dans un grand cercle "Tous" avec la flèche "⊂"*

---

## 3️⃣ Opérations sur les Ensembles

### A. Union (∪) — "OU"

L'**union** de deux ensembles A et B contient tous les éléments qui sont dans A **ou** dans B (ou dans les deux).

**Notation mathématique :** `A ∪ B`  
**Définition :** `A ∪ B = {x | x ∈ A ou x ∈ B}`

**Exemple :**
```
A = {1, 2, 3}
B = {3, 4, 5}

A ∪ B = {1, 2, 3, 4, 5}
```

**⚠️ Attention :** Le 3 n'est compté qu'une seule fois (pas de doublons).

**En Python :**
```python
A = {1, 2, 3}
B = {3, 4, 5}

# Méthode 1 : Opérateur |
union = A | B
print(union)  # {1, 2, 3, 4, 5}

# Méthode 2 : Méthode .union()
union = A.union(B)
print(union)  # {1, 2, 3, 4, 5}
```

**Cas d'usage AD :**
```python
Managers = {"Alice", "Diane", "Eve"}
Comptabilite = {"Diane", "Frank", "Grace"}

# Qui peut accéder au dossier finances ?
# Règle : Managers OU Comptabilité
Acces_Finances = Managers | Comptabilite
print(Acces_Finances)
# {'Alice', 'Diane', 'Eve', 'Frank', 'Grace'}
# 5 personnes (Diane compte une seule fois)
```

---

### B. Intersection (∩) — "ET"

L'**intersection** de deux ensembles A et B contient uniquement les éléments qui sont **à la fois** dans A **et** dans B.

**Notation mathématique :** `A ∩ B`  
**Définition :** `A ∩ B = {x | x ∈ A et x ∈ B}`

**Exemple :**
```
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A ∩ B = {3, 4}
```

**En Python :**
```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Méthode 1 : Opérateur &
intersection = A & B
print(intersection)  # {3, 4}

# Méthode 2 : Méthode .intersection()
intersection = A.intersection(B)
print(intersection)  # {3, 4}
```

**Cas d'usage AD :**
```python
RH = {"Eve", "Karen"}
Managers = {"Alice", "Diane", "Eve"}

# Qui peut accéder au dossier paie ?
# Règle : RH ET Managers (les deux en même temps)
Acces_Paie = RH & Managers
print(Acces_Paie)
# {'Eve'}
# Seule Eve est à la fois RH et Manager
```

---

### C. Différence (\ ou -) — "SANS"

La **différence** de A et B contient les éléments qui sont dans A mais **pas** dans B.

**Notation mathématique :** `A \ B` ou `A - B`  
**Définition :** `A \ B = {x | x ∈ A et x ∉ B}`

**Exemple :**
```
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A \ B = {1, 2}     (dans A mais pas dans B)
B \ A = {5, 6}     (dans B mais pas dans A)
```

**⚠️ Attention :** `A - B ≠ B - A` (pas commutatif)

**En Python :**
```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Méthode 1 : Opérateur -
difference = A - B
print(difference)  # {1, 2}

# Méthode 2 : Méthode .difference()
difference = A.difference(B)
print(difference)  # {1, 2}
```

**Cas d'usage AD :**
```python
# Frank quitte l'entreprise
Comptabilite = {"Diane", "Frank", "Grace"}
Comptabilite = Comptabilite - {"Frank"}
print(Comptabilite)
# {'Diane', 'Grace'}

# Ou avec .discard()
Comptabilite.discard("Frank")
```

---

### D. Complément (Ā ou A')

Le **complément** de A (noté Ā ou A') contient tous les éléments qui **ne sont pas** dans A.

**Définition :** `Ā = {x | x ∉ A}`

**⚠️ Important :** Le complément dépend de l'**univers** (ensemble de référence).

**Exemple :**
```
Univers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
A = {1, 2, 3}

Ā = {4, 5, 6, 7, 8, 9, 10}
```

**En Python :**
```python
Tous_Utilisateurs = {"Alice", "Bob", "Charlie", "Diane", "Eve", "Frank"}
IT = {"Alice", "Bob", "Charlie"}

# Qui n'est PAS dans IT ?
Non_IT = Tous_Utilisateurs - IT
print(Non_IT)
# {'Diane', 'Eve', 'Frank'}
```

---

## 4️⃣ Diagrammes de Venn

Les **diagrammes de Venn** sont des représentations visuelles des ensembles et de leurs relations.

### Union (A ∪ B)

```
     ┌───────────────┐
     │       A       │
     │   ╔═══════════╪═══════════╗
     │   ║  Zone A   ║  Zone B   ║
     └───╫───────────┘           ║
         ║        A ∩ B           ║
         ║                        ║
         ║           B            ║
         ╚════════════════════════╝

A ∪ B = Tout ce qui est coloré (A + B + intersection)
```

### Intersection (A ∩ B)

```
     ┌───────────────┐
     │       A       │
     │       ╔═══════╪═══════╗
     │       ║ A ∩ B ║       ║
     └───────╫───────┘       ║
             ║               ║
             ║       B       ║
             ╚═══════════════╝

A ∩ B = Zone centrale uniquement (éléments communs)
```

### Différence (A \ B)

```
     ┌───────────────┐
     │  ╔════════╗   │
     │  ║   A    ║───┘
     │  ║  SANS  ║   │
     └──╫────────┘───────────┐
        ║       A ∩ B         ║
        ║                     ║
        ║          B          ║
        ╚═════════════════════╝

A \ B = Partie de A sans l'intersection (A seul)
```

**[ILLUSTRATION 2 : Diagrammes de Venn colorés]**  
*Légende : Trois diagrammes de Venn montrant visuellement l'union (toute la zone colorée), l'intersection (zone centrale en surbrillance), et la différence (partie gauche seule colorée)*

---

## 5️⃣ Application aux Groupes Active Directory

### Modélisation

**En Active Directory, chaque groupe est un ensemble d'utilisateurs.**

```python
# Définition des groupes (ensembles)
IT = {"Alice", "Bob", "Charlie"}
Managers = {"Alice", "Diane", "Eve"}
Comptabilite = {"Diane", "Frank", "Grace"}
Developpeurs = {"Bob", "Henry", "Irene", "Jack"}
RH = {"Eve", "Karen"}
```

---

### Cas d'Usage 1 : Permissions par Union

**Question :** Qui peut accéder au dossier `\\serveur\finances` ?  
**Règle :** Managers **OU** Comptabilité

```python
Acces_Finances = Managers | Comptabilite
print(f"Accès finances : {len(Acces_Finances)} personnes")
print(Acces_Finances)

# Résultat :
# Accès finances : 5 personnes
# {'Alice', 'Diane', 'Eve', 'Frank', 'Grace'}
```

**Vérification individuelle :**
```python
if "Frank" in Acces_Finances:
    print("✅ Frank peut accéder au dossier finances")
else:
    print("❌ Frank ne peut PAS accéder au dossier finances")
```

---

### Cas d'Usage 2 : Permissions par Intersection

**Question :** Qui peut accéder au dossier `\\serveur\paie` ?  
**Règle :** RH **ET** Managers (les deux en même temps)

```python
Acces_Paie = RH & Managers
print(f"Accès paie : {len(Acces_Paie)} personne(s)")
print(Acces_Paie)

# Résultat :
# Accès paie : 1 personne(s)
# {'Eve'}

# Eve est la SEULE personne à la fois dans RH et Managers
```

---

### Cas d'Usage 3 : Audit de Sécurité

**Question :** Qui est dans IT mais PAS dans Managers ?  
**Objectif :** Identifier les techniciens sans responsabilités managériales

```python
IT_Sans_Manager = IT - Managers
print(f"IT sans responsabilités : {IT_Sans_Manager}")

# Résultat :
# IT sans responsabilités : {'Bob', 'Charlie'}
```

---

### Cas d'Usage 4 : Départ d'un Employé

**Contexte :** Frank quitte l'entreprise. Retirer tous ses accès.

```python
# Avant
print(f"Comptabilite avant : {Comptabilite}")
print(f"Accès finances avant : {len(Acces_Finances)}")

# Retirer Frank
Comptabilite.discard("Frank")
Acces_Finances = Managers | Comptabilite

# Après
print(f"Comptabilite après : {Comptabilite}")
print(f"Accès finances après : {len(Acces_Finances)}")

# Résultat :
# Comptabilite avant : {'Diane', 'Frank', 'Grace'}
# Accès finances avant : 5
# Comptabilite après : {'Diane', 'Grace'}
# Accès finances après : 4
```

---

## 6️⃣ Python : Type `set()` — Manipulation Pratique

### Créer un Ensemble

```python
# Méthode 1 : Avec accolades {}
IT = {"Alice", "Bob", "Charlie"}

# Méthode 2 : Avec set()
Managers = set(["Alice", "Diane", "Eve"])

# Méthode 3 : À partir d'une liste (avec déduplication automatique)
liste = ["Alice", "Bob", "Alice", "Charlie"]
IT = set(liste)
print(IT)  # {'Alice', 'Bob', 'Charlie'} (Alice compte une seule fois)

# Ensemble vide
vide = set()  # ⚠️ Pas {}, car {} crée un dictionnaire vide
```

---

### Opérations en Python

| **Opération** | **Opérateur** | **Méthode** | **Exemple** |
|---------------|---------------|-------------|-------------|
| **Union** | `A | B` | `A.union(B)` | `{1,2} | {2,3}` → `{1,2,3}` |
| **Intersection** | `A & B` | `A.intersection(B)` | `{1,2} & {2,3}` → `{2}` |
| **Différence** | `A - B` | `A.difference(B)` | `{1,2} - {2,3}` → `{1}` |
| **Différence symétrique** | `A ^ B` | `A.symmetric_difference(B)` | `{1,2} ^ {2,3}` → `{1,3}` |

---

### Ajouter et Retirer des Éléments

```python
IT = {"Alice", "Bob"}

# Ajouter un élément
IT.add("Charlie")
print(IT)  # {'Alice', 'Bob', 'Charlie'}

# Retirer un élément (2 méthodes)
IT.remove("Bob")      # ❌ Lève une erreur si Bob n'existe pas
IT.discard("Bob")     # ✅ Ne lève pas d'erreur si Bob n'existe pas

# Vider un ensemble
IT.clear()
print(IT)  # set()
```

---

### Vérifications

```python
IT = {"Alice", "Bob", "Charlie"}
Managers = {"Alice", "Diane", "Eve"}

# Appartenance
print("Alice" in IT)          # True
print("Diane" in IT)          # False

# Inclusion
Tous = {"Alice", "Bob", "Charlie", "Diane", "Eve"}
print(IT.issubset(Tous))      # True (IT ⊂ Tous)
print(Tous.issuperset(IT))    # True (Tous ⊃ IT)

# Disjonction (pas d'éléments communs)
A = {1, 2, 3}
B = {4, 5, 6}
print(A.isdisjoint(B))        # True (A ∩ B = ∅)
```

---

## 7️⃣ Script Complet : Gestion de Groupes AD

```python
"""
Script de gestion des permissions Active Directory
Utilisation des ensembles pour automatiser l'audit
"""

# ═══════════════════════════════════════════════════════════
# 1. DÉFINITION DES GROUPES
# ═══════════════════════════════════════════════════════════

IT = {"Alice", "Bob", "Charlie"}
Managers = {"Alice", "Diane", "Eve"}
Comptabilite = {"Diane", "Frank", "Grace"}
Developpeurs = {"Bob", "Henry", "Irene", "Jack"}
RH = {"Eve", "Karen"}
Stagiaires = {"Luc", "Marie", "Nathan"}

# Tous les utilisateurs
Tous_Utilisateurs = IT | Managers | Comptabilite | Developpeurs | RH | Stagiaires

# ═══════════════════════════════════════════════════════════
# 2. DÉFINITION DES PERMISSIONS
# ═══════════════════════════════════════════════════════════

Acces_Finances = Managers | Comptabilite
Acces_Serveur = IT
Acces_Code = Developpeurs
Acces_Paie = RH & Managers  # Intersection : doit être dans les DEUX

# ═══════════════════════════════════════════════════════════
# 3. RAPPORT D'AUDIT
# ═══════════════════════════════════════════════════════════

print("╔══════════════════════════════════════════════════════╗")
print("║        AUDIT DES PERMISSIONS - TECHSERVICES          ║")
print("╠══════════════════════════════════════════════════════╣")
print(f"║ Total utilisateurs : {len(Tous_Utilisateurs):26} ║")
print("╠══════════════════════════════════════════════════════╣")

# Statistiques par ressource
print("║                                                      ║")
print("║  📂 ACCÈS AUX RESSOURCES                            ║")
print("║                                                      ║")
print(f"║  Finances (Managers ∪ Compta) : {len(Acces_Finances):15} ║")
print(f"║  Serveur IT                    : {len(Acces_Serveur):15} ║")
print(f"║  Code Source (Dev)             : {len(Acces_Code):15} ║")
print(f"║  Paie (RH ∩ Managers)          : {len(Acces_Paie):15} ║")
print("║                                                      ║")

# Utilisateurs sans aucun accès
Sans_Acces = Tous_Utilisateurs - (Acces_Finances | Acces_Serveur | Acces_Code | Acces_Paie)
print(f"║  ⚠️  Sans aucun accès           : {len(Sans_Acces):15} ║")
print(f"║      → {Sans_Acces}                     ║")
print("║                                                      ║")

# Double appartenance
IT_et_Managers = IT & Managers
print(f"║  👥 IT ET Managers              : {len(IT_et_Managers):15} ║")
print(f"║      → {IT_et_Managers}                             ║")

print("╚══════════════════════════════════════════════════════╝")

# ═══════════════════════════════════════════════════════════
# 4. VÉRIFICATION INDIVIDUELLE
# ═══════════════════════════════════════════════════════════

def verifier_acces(utilisateur):
    """Vérifie tous les accès d'un utilisateur"""
    print(f"\n🔍 Analyse des accès de {utilisateur} :")
    
    acces = []
    if utilisateur in Acces_Finances:
        acces.append("Finances")
    if utilisateur in Acces_Serveur:
        acces.append("Serveur IT")
    if utilisateur in Acces_Code:
        acces.append("Code Source")
    if utilisateur in Acces_Paie:
        acces.append("Paie")
    
    if acces:
        print(f"   ✅ Accès : {', '.join(acces)}")
    else:
        print(f"   ❌ Aucun accès")

# Tests
verifier_acces("Alice")   # IT et Managers → plusieurs accès
verifier_acces("Frank")   # Comptabilité → Finances uniquement
verifier_acces("Luc")     # Stagiaire → Aucun accès
```

**Résultat attendu :**
```
╔══════════════════════════════════════════════════════╗
║        AUDIT DES PERMISSIONS - TECHSERVICES          ║
╠══════════════════════════════════════════════════════╣
║ Total utilisateurs :                             15 ║
╠══════════════════════════════════════════════════════╣
║                                                      ║
║  📂 ACCÈS AUX RESSOURCES                            ║
║                                                      ║
║  Finances (Managers ∪ Compta) :                   5 ║
║  Serveur IT                    :                   3 ║
║  Code Source (Dev)             :                   4 ║
║  Paie (RH ∩ Managers)          :                   1 ║
║                                                      ║
║  ⚠️  Sans aucun accès           :                   3 ║
║      → {'Luc', 'Marie', 'Nathan'}                   ║
║                                                      ║
║  👥 IT ET Managers              :                   1 ║
║      → {'Alice'}                                    ║
╚══════════════════════════════════════════════════════╝

🔍 Analyse des accès de Alice :
   ✅ Accès : Finances, Serveur IT

🔍 Analyse des accès de Frank :
   ✅ Accès : Finances

🔍 Analyse des accès de Luc :
   ❌ Aucun accès
```

**[ILLUSTRATION 3 : Diagramme de flux du script]**  
*Légende : Organigramme montrant : 1) Définition des groupes, 2) Calcul des permissions (union/intersection), 3) Génération du rapport, 4) Vérification individuelle*

---

## 8️⃣ Propriétés Importantes des Ensembles

### Commutativité

```
A ∪ B = B ∪ A   ✅ Vrai (union)
A ∩ B = B ∩ A   ✅ Vrai (intersection)
A \ B = B \ A   ❌ FAUX (différence n'est PAS commutative)
```

### Associativité

```
(A ∪ B) ∪ C = A ∪ (B ∪ C)   ✅ Vrai
(A ∩ B) ∩ C = A ∩ (B ∩ C)   ✅ Vrai
```

### Distributivité

```
A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)   ✅ Vrai
A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)   ✅ Vrai
```

### Lois de De Morgan

```
(A ∪ B)' = A' ∩ B'   (complément d'une union)
(A ∩ B)' = A' ∪ B'   (complément d'une intersection)
```

---

## 📝 Fiche Récapitulative (À Garder)

### Notations Mathématiques vs Python

| **Opération** | **Math** | **Python (opérateur)** | **Python (méthode)** |
|---------------|----------|------------------------|----------------------|
| **Ensemble** | `{1, 2, 3}` | `{1, 2, 3}` | `set([1, 2, 3])` |
| **Appartenance** | `a ∈ A` | `a in A` | — |
| **Non-appartenance** | `a ∉ A` | `a not in A` | — |
| **Inclusion** | `A ⊂ B` | — | `A.issubset(B)` |
| **Union** | `A ∪ B` | `A | B` | `A.union(B)` |
| **Intersection** | `A ∩ B` | `A & B` | `A.intersection(B)` |
| **Différence** | `A \ B` | `A - B` | `A.difference(B)` |
| **Cardinal** | `|A|` | `len(A)` | — |

### Aide-Mémoire : Opérations en Questions Métier

| **Question** | **Opération** | **Code Python** |
|--------------|---------------|-----------------|
| "Qui a accès SI dans A OU dans B ?" | Union | `A | B` |
| "Qui est dans les DEUX groupes ?" | Intersection | `A & B` |
| "Qui est dans A mais PAS dans B ?" | Différence | `A - B` |
| "Qui n'est dans AUCUN des groupes ?" | Complément | `Tous - (A | B)` |

---

## 🎯 Compétences Travaillées (Référentiel RNCP)

| **Code** | **Compétence** | **Application dans cette séance** |
|----------|----------------|-----------------------------------|
| **B1.3** | Mettre à disposition des utilisateurs un service informatique | Gérer les accès aux ressources partagées |
| **B2.2** | Assurer la sécurité d'un système informatique | Auditer les permissions, appliquer le moindre privilège |
| **B2.3** | Gérer le patrimoine informatique | Documenter les appartenances aux groupes |

---

## 💡 Pour Aller Plus Loin

- **Produit cartésien** : `A × B = {(a, b) | a ∈ A et b ∈ B}`
- **Relations** : Un ensemble de couples `R ⊂ A × B`
- **Partition** : Découper un ensemble en sous-ensembles disjoints
- **PowerShell Get-ADGroupMember** : Commande pour lister les membres d'un groupe AD
- **Théorie des graphes** : Modéliser les relations entre utilisateurs et groupes

---

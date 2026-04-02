---
author: YLP
title: 📌 FICHE BILAN & MÉMO
---

# 📌 FICHE BILAN & MÉMO
## Ensembles et Relations : L'Essentiel à Retenir

---

## 🎯 Synthèse de la Séance

| **Élément** | **Détail** |
|-------------|-----------|
| **Thème** | Théorie des ensembles appliquée à Active Directory |
| **Application** | Gestion des groupes et permissions |
| **Compétences** | Union, intersection, différence, appartenance, inclusion |
| **Durée** | 4 heures |
| **Livrable** | Script d'audit de permissions AD |

---

## ✅ Objectifs Atteints

À l'issue de cette séance, vous devez être capable de :

- ✅ Définir un ensemble et utiliser la notation `{a, b, c}`
- ✅ Distinguer appartenance (∈) et inclusion (⊂)
- ✅ Effectuer une union (∪), intersection (∩), différence (\\)
- ✅ Représenter des ensembles avec des diagrammes de Venn
- ✅ Modéliser les groupes AD comme des ensembles
- ✅ Manipuler les sets Python (`set()`, `|`, `&`, `-`)
- ✅ Résoudre des problèmes de permissions avec les opérations ensemblistes
- ✅ Générer un rapport d'audit automatisé

---

## 🔑 Les 4 Opérations Fondamentales

### Tableau Récapitulatif

| **Opération** | **Question** | **Math** | **Python** | **Exemple** |
|---------------|--------------|----------|------------|-------------|
| **Union** | Qui est dans A **OU** B ? | A ∪ B | `A | B` | Direction ∪ Compta |
| **Intersection** | Qui est dans A **ET** B ? | A ∩ B | `A & B` | RH ∩ Direction |
| **Différence** | Qui est dans A mais **PAS** dans B ? | A \ B | `A - B` | IT - Direction |
| **Complément** | Qui **N'EST PAS** dans A ? | Ā ou A' | `Tous - A` | Tous - Stagiaires |

### Visualisation (Diagrammes de Venn)

```
UNION (A ∪ B)          INTERSECTION (A ∩ B)      DIFFÉRENCE (A \ B)
═══════════════        ════════════════════      ═════════════════

   ┌────────┐             ┌────────┐               ┌────────┐
   │████████│             │        │               │████████│
   │████╔═══╪════╗        │    ╔═══╪════╗          │████║   │    │
   │████║███║████║        │    ║███║    ║          │████║   └────┘
   └────╫███║────┘        └────╫███║────┘          └────║
        ║███║                  ║███║                    ║
        ╚═══╝                  ╚═══╝                    ╚════════

Tout coloré           Zone centrale           Partie gauche
(pas de doublons)     uniquement              uniquement
```

---

## 📐 Notation Mathématique vs Python

### Symboles à Connaître

| **Concept** | **Math** | **Python** | **Se lit** |
|-------------|----------|------------|------------|
| Ensemble | `A = {1, 2, 3}` | `A = {1, 2, 3}` | "A est l'ensemble contenant 1, 2, 3" |
| Appartenance | `a ∈ A` | `a in A` | "a appartient à A" |
| Non-appartenance | `a ∉ A` | `a not in A` | "a n'appartient pas à A" |
| Inclusion | `A ⊂ B` | `A.issubset(B)` | "A est inclus dans B" |
| Union | `A ∪ B` | `A | B` | "A union B" |
| Intersection | `A ∩ B` | `A & B` | "A inter B" |
| Différence | `A \ B` ou `A - B` | `A - B` | "A moins B" |
| Ensemble vide | `∅` | `set()` | "Ensemble vide" |
| Cardinal | `|A|` | `len(A)` | "Cardinal de A" |

---

## 🚨 Distinction Cruciale : ∈ vs ⊂

### Appartenance (∈) : Élément → Ensemble

**Un ÉLÉMENT appartient à un ENSEMBLE.**

```python
IT = {"alice", "bob", "charlie"}

"alice" ∈ IT        # ✅ Vrai (alice est un élément de IT)
"alice" in IT       # ✅ En Python
```

**Visualisation :**
```
     ┌───────────────┐
     │      IT       │
     │               │
     │    ● alice    │  ← Alice (point) est DANS IT (cercle)
     │    ● bob      │
     │    ● charlie  │
     │               │
     └───────────────┘
```

---

### Inclusion (⊂) : Ensemble → Ensemble

**Un ENSEMBLE est inclus dans un ENSEMBLE.**

```python
IT = {"alice", "bob", "charlie"}
Tous = {"alice", "bob", "charlie", "diane", "eve", "frank"}

IT ⊂ Tous           # ✅ Vrai (IT est un sous-ensemble de Tous)
IT.issubset(Tous)   # ✅ En Python
```

**Visualisation :**
```
     ┌───────────────────────────────┐
     │         Tous                  │
     │                               │
     │   ┌───────────────┐           │
     │   │      IT       │           │  ← IT (petit cercle) est
     │   │               │           │    INCLUS dans Tous (grand cercle)
     │   └───────────────┘           │
     │                               │
     └───────────────────────────────┘
```

---

### ❌ ERREUR FRÉQUENTE

```python
IT = {"alice", "bob"}
Tous = {"alice", "bob", "diane"}

# ❌ FAUX : IT n'est pas un élément, c'est un ensemble
IT ∈ Tous  # TypeError ou False selon contexte

# ✅ VRAI : IT est un sous-ensemble
IT ⊂ Tous  # True
IT.issubset(Tous)  # True
```

---

## 💻 Sets Python : Commandes Essentielles

### Créer un Set

```python
# Méthode 1 : Avec {}
A = {"alice", "bob", "charlie"}

# Méthode 2 : Avec set()
B = set(["diane", "eve"])

# Méthode 3 : À partir d'une liste (déduplication)
liste = ["alice", "bob", "alice", "charlie"]
A = set(liste)  # {'alice', 'bob', 'charlie'}

# Ensemble vide
vide = set()  # ⚠️ PAS {}, qui crée un dictionnaire vide
```

---

### Opérations

```python
A = {1, 2, 3}
B = {3, 4, 5}

# Union (A ∪ B)
A | B              # {1, 2, 3, 4, 5}
A.union(B)         # {1, 2, 3, 4, 5}

# Intersection (A ∩ B)
A & B              # {3}
A.intersection(B)  # {3}

# Différence (A \ B)
A - B              # {1, 2}
A.difference(B)    # {1, 2}

# Différence symétrique (A △ B) — éléments dans A ou B mais pas les deux
A ^ B              # {1, 2, 4, 5}
A.symmetric_difference(B)  # {1, 2, 4, 5}
```

---

### Modifier un Set

```python
A = {"alice", "bob"}

# Ajouter un élément
A.add("charlie")         # {'alice', 'bob', 'charlie'}

# Retirer un élément (lève erreur si absent)
A.remove("bob")          # {'alice', 'charlie'}

# Retirer un élément (silencieux si absent)
A.discard("diane")       # Pas d'erreur si diane n'existe pas

# Vider le set
A.clear()                # set()
```

---

### Vérifications

```python
IT = {"alice", "bob", "charlie"}
Managers = {"alice", "diane"}
Tous = {"alice", "bob", "charlie", "diane", "eve"}

# Appartenance
"alice" in IT             # True
"diane" in IT             # False

# Inclusion
IT.issubset(Tous)         # True (IT ⊂ Tous)
Tous.issuperset(IT)       # True (Tous ⊃ IT)

# Disjonction (pas d'éléments communs)
IT.isdisjoint({1, 2, 3})  # True (aucun élément commun)
```

---

## 🏢 Cas d'Usage Active Directory

### Template Réutilisable

```python
# ═════════════════════════════════════════════════════════
# AUDIT DE PERMISSIONS AD — TEMPLATE
# ═════════════════════════════════════════════════════════

# 1. Définir les groupes
IT = {"alice", "bob"}
Managers = {"alice", "diane"}
Dev = {"bob", "charlie"}

# 2. Calculer les permissions
# Règle : Doit être dans A OU B
Acces_Serveur = IT | Managers

# Règle : Doit être dans A ET B
Acces_Admin = IT & Managers

# Règle : Dans A mais PAS dans B
Non_Managers = IT - Managers

# 3. Vérifier un utilisateur spécifique
utilisateur = "alice"
if utilisateur in Acces_Admin:
    print(f"✅ {utilisateur} a accès admin")
else:
    print(f"❌ {utilisateur} n'a PAS accès admin")

# 4. Générer un rapport
print(f"Accès serveur : {len(Acces_Serveur)} personnes")
print(f"Liste : {sorted(Acces_Serveur)}")
```

---

### Questions Métier Courantes

| **Question** | **Traduction Ensembles** | **Code** |
|--------------|--------------------------|----------|
| Qui peut accéder au serveur de fichiers ? | Direction OU Compta | `Direction | Comptabilite` |
| Qui peut modifier la paie ? | RH ET Direction | `RH & Direction` |
| Qui est technicien mais pas manager ? | IT SANS Managers | `IT - Managers` |
| Qui n'a aucun privilège admin ? | Tous SAUF IT et Direction | `Tous - (IT | Direction)` |
| Alice est-elle admin ? | Alice ∈ IT ? | `"alice" in IT` |
| Combien de personnes dans IT ? | Cardinal de IT | `len(IT)` |

---

## 📊 Propriétés des Ensembles

### Propriétés Fondamentales

```
1. Pas d'ordre :        {1, 2, 3} = {3, 1, 2}
2. Pas de doublons :    {1, 1, 2} = {1, 2}
3. Cardinal :           |{a, b, c}| = 3
```

### Commutativité

```
A ∪ B = B ∪ A   ✅ Union commutative
A ∩ B = B ∩ A   ✅ Intersection commutative
A \ B ≠ B \ A   ❌ Différence NON commutative
```

### Associativité

```
(A ∪ B) ∪ C = A ∪ (B ∪ C)   ✅ Union associative
(A ∩ B) ∩ C = A ∩ (B ∩ C)   ✅ Intersection associative
```

### Distributivité

```
A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)
A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)
```

### Lois de De Morgan

```
(A ∪ B)' = A' ∩ B'    (complément d'une union)
(A ∩ B)' = A' ∪ B'    (complément d'une intersection)
```

---

## 🧠 Auto-Évaluation

**Cochez les compétences que vous maîtrisez maintenant :**

| **Je sais...** | **Maîtrisé ?** |
|----------------|----------------|
| Créer un set en Python avec `{}` ou `set()` | ☐ |
| Utiliser `|` pour faire une union | ☐ |
| Utiliser `&` pour faire une intersection | ☐ |
| Utiliser `-` pour faire une différence | ☐ |
| Vérifier l'appartenance avec `in` | ☐ |
| Vérifier l'inclusion avec `.issubset()` | ☐ |
| Distinguer `∈` (appartenance) et `⊂` (inclusion) | ☐ |
| Calculer le cardinal avec `len()` | ☐ |
| Ajouter un élément avec `.add()` | ☐ |
| Retirer un élément avec `.discard()` | ☐ |
| Modéliser un groupe AD comme un ensemble | ☐ |
| Calculer qui a accès à une ressource (union/intersection) | ☐ |
| Générer un rapport d'audit automatisé | ☐ |

**Si vous avez coché < 10 cases, revoir la fiche de cours et refaire l'activité de découverte.**

---

## 💡 Exercices d'Entraînement

### Exercice 1 : Opérations de Base

**Données :**
```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
C = {5, 6, 7, 8}
```

**Questions :**
1. Calculer `A ∪ B`
2. Calculer `A ∩ B`
3. Calculer `A - B`
4. Calculer `(A ∪ B) ∩ C`
5. `3 ∈ A` ? Vrai ou faux ?
6. `A ⊂ B` ? Vrai ou faux ?

**Solutions :**
```python
# 1. A ∪ B
print(A | B)  # {1, 2, 3, 4, 5, 6}

# 2. A ∩ B
print(A & B)  # {3, 4}

# 3. A - B
print(A - B)  # {1, 2}

# 4. (A ∪ B) ∩ C
print((A | B) & C)  # {5, 6}

# 5. 3 ∈ A
print(3 in A)  # True

# 6. A ⊂ B
print(A.issubset(B))  # False (1 et 2 ne sont pas dans B)
```

---

### Exercice 2 : Groupes AD

**Contexte :** Petite entreprise avec 4 groupes.

```python
IT = {"alice", "bob"}
Sales = {"charlie", "diane"}
Managers = {"alice", "diane"}
Finance = {"eve"}
```

**Questions :**
1. Qui peut accéder au serveur de fichiers ? (IT OU Sales)
2. Qui peut approuver les budgets ? (Managers ET Finance)
3. Qui est dans IT mais PAS manager ?
4. Combien de personnes sont managers ?
5. Est-ce que Bob est manager ?

**Solutions :**
```python
# 1. IT OU Sales
Acces_Fichiers = IT | Sales
print(Acces_Fichiers)  # {'alice', 'bob', 'charlie', 'diane'}

# 2. Managers ET Finance
Approbation_Budget = Managers & Finance
print(Approbation_Budget)  # set() (ensemble vide, personne n'est dans les 2)

# 3. IT SANS Managers
IT_Non_Manager = IT - Managers
print(IT_Non_Manager)  # {'bob'}

# 4. Cardinal de Managers
print(len(Managers))  # 2

# 5. Bob ∈ Managers ?
print("bob" in Managers)  # False
```

---

### Exercice 3 : Audit Complet

**Mission :** Reproduire l'audit du devoir sur un cas simplifié.

```python
# Entreprise fictive : 10 employés, 4 groupes
IT = {"alice", "bob"}
Dev = {"bob", "charlie"}
Admin = {"alice", "diane"}
Users = {"eve", "frank", "grace"}

# Règles
Acces_Serveur = IT | Admin  # OU
Acces_Code = Dev            # Dev uniquement
Acces_Config = IT & Admin   # ET (les deux)

# Questions :
# 1. Combien ont accès au serveur ?
# 2. Qui peut modifier la config ?
# 3. Qui n'a AUCUN accès (Users) ?
```

**Solutions :**
```python
# 1. Accès serveur
print(len(Acces_Serveur))  # 3 (alice, bob, diane)

# 2. Accès config
print(Acces_Config)  # {'alice'} (seule à être dans IT ET Admin)

# 3. Sans accès
Tous_Acces = Acces_Serveur | Acces_Code | Acces_Config
Sans_Acces = Users - Tous_Acces
print(Sans_Acces)  # {'eve', 'frank', 'grace'} (les 3 users)
```

---

## 🔄 Lien avec les Autres Séances

| **Séance** | **Lien avec S13** |
|------------|------------------|
| **S2** | Chaînes → Les noms d'utilisateurs sont des chaînes |
| **S3** | Listes → Les groupes peuvent être convertis en listes |
| **S8** | Dictionnaires → Mapper utilisateur → groupes |
| **S14** | Relations et graphes → Modéliser les permissions comme un graphe |
| **BLOC 1 - S10** | Active Directory : création de groupes, GPO |
| **BLOC 2 - S8** | Permissions NTFS, ACL comme ensembles de droits |

---

## 📚 Ressources pour Aller Plus Loin

### Documentation et Tutoriels

- **Python Sets (officiel)** : [docs.python.org/3/library/stdtypes.html#set](https://docs.python.org/3/library/stdtypes.html#set)
- **Khan Academy** : "Ensembles et logique" (cours gratuit, sous-titres FR)
- **Wikipédia** : "Ensemble (mathématiques)" pour approfondir la théorie
- **Active Directory Groups** : [docs.microsoft.com](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups)

### Outils Pratiques

| **Outil** | **Usage** |
|-----------|-----------|
| **draw.io** | Créer des diagrammes de Venn en ligne |
| **PowerShell Get-ADGroupMember** | Lister les membres d'un groupe AD |
| **Python-AD** | Bibliothèque pour interroger AD depuis Python |
| **Neo4j** | Base de données orientée graphes (pour S14) |

---

## 🎓 Pourquoi C'est Important en Administration Système ?

### Les Ensembles Sont Partout en Infra IT

| **Domaine** | **Application des ensembles** |
|-------------|-------------------------------|
| **Active Directory** | Groupes = ensembles d'utilisateurs |
| **Pare-feu** | Règles = ensembles d'IPs autorisées/bloquées |
| **VLAN** | Segments réseau = ensembles de machines |
| **Permissions NTFS** | ACL = ensembles de droits par groupe |
| **Monitoring** | Alertes = ensembles de serveurs surveillés |
| **Sauvegarde** | Stratégies = ensembles de fichiers à sauvegarder |

### Pourquoi Automatiser avec Python ?

**Scénario réel :**
- Entreprise de 200 employés
- 50 groupes AD
- 100 ressources avec permissions complexes
- Audit de sécurité trimestriel demandé

**Approche manuelle :**
- Ouvrir Active Directory Users and Computers
- Cliquer sur chaque groupe, noter les membres
- Vérifier les permissions de chaque ressource
- Recouper les informations dans Excel
- **Temps : 8 heures**

**Approche automatisée (Python + AD) :**
- Script qui interroge AD via LDAP
- Calcul automatique des unions/intersections
- Génération du rapport en PDF
- **Temps : 30 secondes**

**Gain :** 16x plus rapide + zéro erreur humaine

---

## 💬 Citations à Retenir

> *"Un groupe Active Directory, c'est juste un ensemble avec un nom Windows-friendly."*  
> — Administrateur système, après avoir découvert la théorie des ensembles

> *"Si vous maîtrisez les unions et intersections, vous maîtrisez 80% de la gestion des permissions."*  
> — Responsable sécurité IT

> *"Les mathématiques ne sont pas abstraites. Elles modélisent la réalité. Les ensembles modélisent les groupes."*  
> — Professeur de mathématiques appliquées

---

## 📅 Prochaine Séance : S14

### Thème : Relations et Graphes

**Ce que vous allez apprendre :**
- Définir une relation mathématique (R ⊂ A × B)
- Propriétés des relations (réflexivité, symétrie, transitivité)
- Représenter des relations avec des graphes
- Modéliser les hiérarchies (organigrammes, héritage de groupes AD)

**Application :**
- Graphe des permissions (qui peut accéder à quoi)
- Détection de chemins (A peut-il devenir B via des promotions ?)
- Fermeture transitive (droits hérités)

**Prérequis S14 :** Maîtrise des ensembles (S13) ✅

---

## 🎯 Mot de la Fin

**Félicitations !** Vous venez de maîtriser un concept **fondamental** en informatique.

Les ensembles, ce n'est pas que des maths :
- 🔧 **C'est la base de la gestion des droits**
- 📊 **C'est la clé de l'audit de sécurité**
- 🚀 **C'est le fondement de SQL** (SELECT, JOIN, UNION...)
- 💡 **C'est la logique des pare-feu** (règles allow/deny)

**Un bon technicien SISR sait que :**
> Active Directory = Base de données d'ensembles  
> Permissions = Opérations ensemblistes  
> Audit = Vérification de cohérence des ensembles

**Vous êtes maintenant capable d'automatiser ce que 90% des admins sys font à la main.**

C'est ça, la valeur ajoutée d'un BTS SIO SISR.

---

## ✉️ Contact et Support

**Questions sur cette séance ?**

- 📧 Email enseignant : [email@exemple.fr]
- 💬 Discord : Salon `#maths-info`
- 📚 Plateforme : Espace de cours BTS SIO

**Ressources additionnelles :**
- [Lien vers le dépôt GitHub du cours]
- [Lien vers les exercices complémentaires]
- [Lien vers les vidéos explicatives]

---

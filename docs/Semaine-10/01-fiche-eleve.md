---
author: YLP
title: 📚 FICHE DE COURS
---


# 📚 FICHE DE COURS ÉLÈVE
## Tableaux et Listes : Structures de Données Simples

*Version 1.0 — BTS SIO SISR — Année 1 — Semaine 10*

---

## 🎯 Compétences Travaillées

| **Code** | **Compétence** |
|----------|----------------|
| **B1.1** | Gérer le patrimoine informatique |
| **B1.2** | Répondre aux incidents et aux demandes d'assistance |
| **B2.1** | Administrer les systèmes et les services informatiques |

---

## 📖 I. Introduction : Pourquoi des Structures de Données ?

### Le Problème

En tant que technicien SISR, vous devrez souvent **manipuler plusieurs valeurs** :
- 📊 Les 254 adresses IP d'un réseau /24
- 🖥️ La liste des postes du parc informatique
- 📋 Les logs de connexion d'un serveur
- ⚙️ La configuration des 48 ports d'un switch

**Question :** Comment stocker ces informations de façon efficace en programmation ?

### La Solution : Les Structures de Données

Une **structure de données** est une façon d'organiser et de stocker des données pour pouvoir les utiliser efficacement.

**Les deux structures de base :**
1. **Tableau** (array)
2. **Liste** (list)

---

## 📊 II. Les Tableaux (Arrays)

### Définition

> Un **tableau** est une structure de données qui stocke une **collection d'éléments** de même type, organisés de manière **séquentielle** et **numérotés**.

### Analogie Physique

![Illustration : Une armoire avec 5 tiroirs numérotés de 0 à 4, chaque tiroir contient un objet]
*Légende : Un tableau est comme une armoire à tiroirs numérotés. Chaque tiroir (case) a un numéro fixe (indice) et contient une valeur.*

**Caractéristiques de l'armoire :**
- 🔢 Chaque tiroir a un **numéro** (l'indice)
- 📦 Tous les tiroirs sont **créés en même temps**
- 🚫 On ne peut **pas ajouter** de tiroir entre le 3 et le 4
- ⚡ Pour accéder au tiroir 5, on y va **directement**

### Syntaxe en Python

#### Création d'un Tableau

```python
# Tableau d'adresses IP
ips = ["192.168.1.10", "192.168.1.11", "192.168.1.12", "192.168.1.13"]

# Tableau de RAM (en Go)
rams = [8, 16, 8, 32, 16]

# Tableau de ports
ports = [1, 2, 3, 4, 5, 6, 7, 8]
```

#### Accès aux Éléments

**⚠️ IMPORTANT : En informatique, on compte à partir de 0 !**

![Illustration : Tableau avec 5 cases contenant des valeurs, indices 0 à 4 affichés en dessous]
*Légende : Les indices d'un tableau commencent toujours à 0. Le 1er élément est à l'indice 0.*

```python
ips = ["192.168.1.10", "192.168.1.11", "192.168.1.12", "192.168.1.13"]

# Accéder au PREMIER élément (indice 0)
print(ips[0])  # Affiche : 192.168.1.10

# Accéder au TROISIÈME élément (indice 2)
print(ips[2])  # Affiche : 192.168.1.12

# Accéder au DERNIER élément
print(ips[-1])  # Affiche : 192.168.1.13
```

#### Modification d'un Élément

```python
ips = ["192.168.1.10", "192.168.1.11", "192.168.1.12"]

# Modifier le 2ème élément (indice 1)
ips[1] = "192.168.1.20"

print(ips)  # Affiche : ['192.168.1.10', '192.168.1.20', '192.168.1.12']
```

#### Parcourir un Tableau

```python
ips = ["192.168.1.10", "192.168.1.11", "192.168.1.12"]

# Méthode 1 : Parcours par élément
for ip in ips:
    print(ip)

# Méthode 2 : Parcours par indice
for i in range(len(ips)):
    print(f"Indice {i} : {ips[i]}")
```

### Opérations Courantes sur les Tableaux

| **Opération** | **Syntaxe Python** | **Exemple** |
|---|---|---|
| Longueur du tableau | `len(tableau)` | `len(ips)` → 3 |
| Accès par indice | `tableau[indice]` | `ips[0]` → "192.168.1.10" |
| Modification | `tableau[indice] = valeur` | `ips[1] = "192.168.1.20"` |
| Dernier élément | `tableau[-1]` | `ips[-1]` → "192.168.1.12" |

### Cas d'Usage SISR

**✅ Utiliser un tableau quand :**
- Le nombre d'éléments est **fixe** ou **prévisible**
- Vous devez accéder fréquemment aux éléments par leur **position**
- La **performance** d'accès est critique

**Exemples concrets :**
- 📊 Les 254 adresses IP d'un /24 (nombre fixe)
- ⚙️ Les 48 ports d'un switch (nombre fixe)
- 📅 Les jours de la semaine (nombre fixe)

---

## 📚 III. Les Listes (Lists)

### Définition

> Une **liste** est une structure de données qui stocke une **collection d'éléments** de manière **séquentielle** et **dynamique** (taille variable).

### Analogie Physique

![Illustration : Une pile de livres sur une étagère, avec des flèches montrant qu'on peut ajouter/retirer des livres]
*Légende : Une liste est comme une pile de livres. On peut facilement ajouter ou retirer des livres n'importe où dans la pile.*

**Caractéristiques de la pile :**
- 📚 On peut **ajouter** un livre en haut, au milieu, ou en bas
- 📚 On peut **retirer** un livre facilement
- 📏 La pile peut **grandir ou rétrécir** sans limite
- 🐢 Pour accéder au 10ème livre, il faut parfois compter depuis le début

### Syntaxe en Python

**Note :** En Python, les **listes** sont en fait des **tableaux dynamiques**. La syntaxe est identique aux tableaux vus précédemment, mais avec des méthodes supplémentaires pour ajouter/supprimer des éléments.

#### Création d'une Liste

```python
# Liste de logs de connexion (commence vide)
logs = []

# Liste de tickets d'incidents
tickets = ["#001", "#002", "#003"]
```

#### Ajouter des Éléments

```python
logs = []

# Ajouter à la FIN de la liste
logs.append("2025-02-20 10:15 - Connexion utilisateur A")
logs.append("2025-02-20 10:20 - Connexion utilisateur B")

print(logs)
# Affiche : ['2025-02-20 10:15 - Connexion utilisateur A', 
#            '2025-02-20 10:20 - Connexion utilisateur B']

# Ajouter à une POSITION SPÉCIFIQUE
logs.insert(1, "2025-02-20 10:17 - Tentative de connexion échouée")

print(logs)
# Affiche : ['2025-02-20 10:15 - Connexion utilisateur A', 
#            '2025-02-20 10:17 - Tentative de connexion échouée',
#            '2025-02-20 10:20 - Connexion utilisateur B']
```

#### Supprimer des Éléments

```python
tickets = ["#001", "#002", "#003", "#004"]

# Supprimer un élément PAR VALEUR
tickets.remove("#002")
print(tickets)  # Affiche : ['#001', '#003', '#004']

# Supprimer un élément PAR INDICE
del tickets[0]
print(tickets)  # Affiche : ['#003', '#004']

# Supprimer le DERNIER élément et le récupérer
dernier = tickets.pop()
print(dernier)   # Affiche : #004
print(tickets)   # Affiche : ['#003']
```

### Opérations Courantes sur les Listes

| **Opération** | **Syntaxe Python** | **Exemple** |
|---|---|---|
| Ajouter à la fin | `liste.append(element)` | `logs.append("log1")` |
| Ajouter à une position | `liste.insert(indice, element)` | `logs.insert(0, "log0")` |
| Supprimer par valeur | `liste.remove(element)` | `logs.remove("log1")` |
| Supprimer par indice | `del liste[indice]` | `del logs[0]` |
| Supprimer et récupérer | `liste.pop()` | `dernier = logs.pop()` |
| Vider la liste | `liste.clear()` | `logs.clear()` |
| Trier | `liste.sort()` | `nombres.sort()` |
| Inverser | `liste.reverse()` | `logs.reverse()` |

### Cas d'Usage SISR

**✅ Utiliser une liste quand :**
- Le nombre d'éléments est **variable** et **imprévisible**
- Vous devez fréquemment **ajouter ou supprimer** des éléments
- L'ordre d'insertion est important

**Exemples concrets :**
- 📋 Les logs de connexion (nombre croissant au fil du temps)
- 🎫 Une file d'attente de tickets d'incident
- 👥 La liste des utilisateurs connectés (change constamment)
- 🔄 Un historique de commandes (on ajoute en permanence)

---

## ⚖️ IV. Tableau vs Liste : Tableau Comparatif

| **Critère** | **Tableau (Array)** | **Liste (List)** |
|---|---|---|
| **Taille** | Fixe (définie à la création) | Dynamique (peut grandir/rétrécir) |
| **Ajout d'élément** | ❌ Impossible (taille fixe) | ✅ Facile (`.append()`, `.insert()`) |
| **Suppression** | ❌ Difficile | ✅ Facile (`.remove()`, `.pop()`) |
| **Accès par indice** | ⚡ Très rapide (O(1)) | ⚡ Très rapide (O(1)) |
| **Utilisation mémoire** | 📦 Compact (bloc contigu) | 📦 Plus gourmand (pointeurs) |
| **Cas d'usage** | Données fixes (config, constantes) | Données variables (logs, files) |

![Illustration : Deux colonnes côte à côte, à gauche un tableau fixe avec 5 cases numérotées, à droite une liste avec des cases reliées par des flèches et un signe + pour ajouter]
*Légende : Différence visuelle entre un tableau (taille fixe) et une liste (taille variable).*

---

## 💡 V. Exemples Concrets SISR

### Exemple 1 : Gestion d'Adresses IP

```python
# Tableau : Les 5 serveurs du réseau (nombre fixe)
serveurs = ["192.168.1.10", "192.168.1.11", "192.168.1.12", 
            "192.168.1.13", "192.168.1.14"]

# Accès au serveur 3
print(f"Serveur 3 : {serveurs[2]}")  # Indice 2 = 3ème élément

# Modifier l'IP du serveur 1
serveurs[0] = "192.168.1.20"
```

### Exemple 2 : File d'Attente de Tickets

```python
# Liste : File d'attente de tickets (nombre variable)
tickets = []

# Un nouveau ticket arrive
tickets.append("#001 - Imprimante en panne")
tickets.append("#002 - Mot de passe oublié")
tickets.append("#003 - PC ne démarre pas")

# Traiter le premier ticket
print(f"Traitement du ticket : {tickets[0]}")
tickets.pop(0)  # Supprimer le ticket traité

# Afficher les tickets restants
print(f"Tickets en attente : {len(tickets)}")
```

### Exemple 3 : Audit de RAM

```python
# Tableau : RAM de chaque poste (50 postes)
rams = [8, 16, 8, 8, 32, 16, 8, 16, 8, 8,
        16, 8, 8, 32, 16, 8, 8, 16, 8, 32,
        8, 16, 8, 8, 16, 32, 8, 8, 16, 8,
        16, 8, 32, 8, 16, 8, 8, 16, 32, 8,
        8, 16, 8, 32, 16, 8, 8, 16, 8, 8]

# Trouver tous les postes avec moins de 8 Go de RAM
postes_a_upgrader = []
for i in range(len(rams)):
    if rams[i] < 8:
        postes_a_upgrader.append(i+1)  # +1 car les postes sont numérotés de 1 à 50

print(f"Postes à upgrader : {postes_a_upgrader}")
```

---

## 🔑 VI. Vocabulaire Clé à Maîtriser

| **Terme** | **Définition** |
|---|---|
| **Structure de données** | Façon d'organiser et de stocker des données |
| **Tableau (Array)** | Structure de taille fixe avec accès par indice |
| **Liste (List)** | Structure de taille variable avec méthodes d'ajout/suppression |
| **Indice (Index)** | Position numérique d'un élément dans un tableau/liste (commence à 0) |
| **Élément** | Une valeur stockée dans un tableau ou une liste |
| **Parcours** | Action de passer en revue tous les éléments d'une structure |
| **Itération** | Une étape d'un parcours (une "boucle") |
| **Longueur** | Nombre d'éléments dans un tableau/liste |
| **Append** | Ajouter un élément à la fin d'une liste |
| **Pop** | Retirer et récupérer le dernier élément d'une liste |

---

## 🎯 VII. Points Clés à Retenir

### ✅ Les 5 Règles d'Or

1. **Les indices commencent à 0** : Le 1er élément est à l'indice 0, le 2ème à l'indice 1, etc.

2. **Tableau = taille fixe** : Une fois créé, on ne peut pas facilement ajouter/supprimer des éléments.

3. **Liste = taille variable** : On peut ajouter/supprimer des éléments avec `.append()`, `.remove()`, `.pop()`.

4. **Parcours avec `for`** : Pour traiter tous les éléments, on utilise une boucle `for`.

5. **Choisir selon le besoin** : Tableau pour données fixes, Liste pour données variables.

### ⚠️ Erreurs Fréquentes

❌ **Erreur 1 : Oublier que les indices commencent à 0**
```python
ips = ["192.168.1.10", "192.168.1.11"]
print(ips[1])  # Affiche le 2ème élément, pas le 1er !
```

❌ **Erreur 2 : Dépasser la taille du tableau**
```python
ips = ["192.168.1.10", "192.168.1.11"]
print(ips[5])  # ERREUR : IndexError (il n'y a que 2 éléments)
```

❌ **Erreur 3 : Confondre `.remove()` et `del`**
```python
tickets = ["#001", "#002", "#003"]

tickets.remove("#002")  # Supprime la VALEUR "#002"
del tickets[0]          # Supprime l'élément à l'INDICE 0
```

---

## 📝 Fiche de Référence Python (Aide-Mémoire)

**À garder sous les yeux pendant les exercices :**

```python
# ═══════════════════════════════════════════════════════════════
# TABLEAUX ET LISTES - AIDE-MÉMOIRE PYTHON
# ═══════════════════════════════════════════════════════════════

# --- CRÉATION ---
tableau = [1, 2, 3, 4, 5]
liste_vide = []

# --- ACCÈS ---
premier = tableau[0]       # Premier élément (indice 0)
dernier = tableau[-1]      # Dernier élément
longueur = len(tableau)    # Nombre d'éléments

# --- MODIFICATION ---
tableau[0] = 10            # Changer le 1er élément

# --- AJOUT (listes) ---
liste.append(6)            # Ajouter à la fin
liste.insert(0, 0)         # Ajouter à l'indice 0

# --- SUPPRESSION (listes) ---
liste.remove(3)            # Supprimer la valeur 3
del liste[0]               # Supprimer l'indice 0
dernier = liste.pop()      # Supprimer et récupérer le dernier

# --- PARCOURS ---
for element in tableau:
    print(element)

for i in range(len(tableau)):
    print(f"Indice {i} : {tableau[i]}")

# ═══════════════════════════════════════════════════════════════
```

---

## 📊 Préparation pour l'Évaluation Formative

### Ce que vous devez savoir faire

**Partie Algorithmique :**
- ✅ Créer un tableau ou une liste
- ✅ Accéder à un élément par son indice
- ✅ Modifier un élément
- ✅ Parcourir une structure avec une boucle `for`
- ✅ Ajouter/supprimer des éléments d'une liste
- ✅ Résoudre un problème simple avec ces structures

**Partie Subnetting (révision S7-S8) :**
- ✅ Calculer le nombre d'hôtes dans un réseau
- ✅ Déterminer le masque à partir du CIDR
- ✅ Identifier la plage d'adresses IP d'un sous-réseau
- ✅ Calculer l'adresse réseau et l'adresse de broadcast

### Conseils de Révision

**📅 Avant l'évaluation :**
1. Relire les fiches de S7-S8 (subnetting)
2. Refaire les exercices d'algorithmique de S6-S9
3. Pratiquer la syntaxe Python des tableaux et listes
4. Vérifier que vous comprenez la différence entre indice et valeur

**⏰ Pendant l'évaluation :**
1. Lire TOUTES les consignes avant de commencer
2. Gérer son temps : 40 min pour le subnetting, 40 min pour l'algorithmique
3. Si vous bloquez, passer à la question suivante et revenir après
4. Vérifier vos réponses si vous avez du temps

---
---
author: YLP
title: 📖 FICHE DE COURS
---

# 📖 FICHE DE COURS
## S15 — Complexité Algorithmique : O(n), O(n²), O(log n), Recherche Linéaire vs Dichotomique

*BTS SIO SISR — Année 1 — Semaine 15*

---

## 🎯 Objectifs de la Séance

À la fin de cette séance, je serai capable de :

✅ Expliquer ce qu'est la **complexité algorithmique**  
✅ Comprendre intuitivement les notations **O(1)**, **O(log n)**, **O(n)**, **O(n log n)**, **O(n²)**  
✅ Distinguer le **meilleur cas**, **cas moyen**, et **pire cas**  
✅ Implémenter une **recherche linéaire** en Python  
✅ Implémenter une **recherche dichotomique** en Python  
✅ Comprendre pourquoi la dichotomique nécessite un **tableau trié**  
✅ **Mesurer et comparer** les temps d'exécution réels

---

## 📚 Vocabulaire Clé à Maîtriser

| **Terme** | **Définition** | **Exemple** |
|-----------|----------------|-------------|
| **Complexité algorithmique** | Mesure du temps d'exécution d'un algorithme en fonction de la taille des données | O(n), O(n²) |
| **Big-O (notation)** | Notation mathématique pour exprimer la complexité dans le pire cas | O(n) = linéaire |
| **n** | Taille des données (nombre d'éléments) | n = 1000 utilisateurs |
| **O(1)** | Complexité constante (temps fixe, indépendant de n) | Accéder à `liste[0]` |
| **O(log n)** | Complexité logarithmique (croissance très lente) | Recherche dichotomique |
| **O(n)** | Complexité linéaire (proportionnelle à n) | Recherche linéaire, parcours de liste |
| **O(n log n)** | Complexité quasi-linéaire | Tri fusion, tri rapide |
| **O(n²)** | Complexité quadratique (croissance rapide) | Double boucle imbriquée |
| **Pire cas** | Scénario où l'algorithme prend le maximum de temps | Élément en dernière position |
| **Meilleur cas** | Scénario où l'algorithme prend le minimum de temps | Élément en première position |

---

## 1️⃣ Qu'est-ce que la Complexité Algorithmique ?

### Définition

La **complexité algorithmique** mesure **combien de temps** (ou d'opérations) un algorithme prend pour s'exécuter en fonction de la **taille des données** (notée **n**).

**Important :** On ne mesure pas le temps en secondes (ça dépend de l'ordinateur), mais en **nombre d'opérations**.

### Pourquoi C'est Important ?

**Deux algorithmes peuvent donner le même résultat mais avec des performances RADICALEMENT différentes.**

**Exemple concret :**

| **Tâche** | **Algorithme lent (O(n²))** | **Algorithme rapide (O(n log n))** |
|-----------|------------------------------|-------------------------------------|
| Trier 1 000 éléments | 1 000 000 opérations | 10 000 opérations |
| Trier 10 000 éléments | 100 000 000 opérations | 130 000 opérations |
| Trier 100 000 éléments | 10 000 000 000 opérations | 1 700 000 opérations |

**Impact réel :**
- Algorithme lent : **5 heures** de calcul
- Algorithme rapide : **2 secondes** de calcul

**Sur un serveur qui traite 10 000 requêtes/jour, un mauvais algorithme = serveur surchargé = coûts d'infrastructure explosés.**

---

## 2️⃣ La Notation Big-O

### Principe

**Big-O décrit comment le temps d'exécution CROÎT quand n augmente.**

**Notation :** `O(expression)`

**Exemples :**
- `O(1)` : Temps constant (peu importe n)
- `O(n)` : Temps proportionnel à n
- `O(n²)` : Temps proportionnel au carré de n

### Règles de Simplification

**Big-O ignore les constantes et les termes de faible ordre.**

**Exemples :**
```
2n + 5        →  O(n)      (on garde le terme dominant)
3n² + 10n + 7 →  O(n²)     (n² domine n et 7)
5             →  O(1)      (constante)
```

**Pourquoi ignorer les constantes ?**

Parce que Big-O s'intéresse à la **croissance asymptotique** (quand n devient très grand).

Quand n = 1 000 000 :
- `2n = 2 000 000`
- `n = 1 000 000`
- Différence : facteur 2 (négligeable comparé à O(n) vs O(n²))

---

## 3️⃣ Les 5 Complexités Essentielles

### Tableau Récapitulatif

| **Notation** | **Nom** | **Exemple** | **n=10** | **n=100** | **n=1000** | **n=1M** |
|--------------|---------|-------------|----------|-----------|------------|----------|
| **O(1)** | Constante | Accès liste[5] | 1 | 1 | 1 | 1 |
| **O(log n)** | Logarithmique | Recherche dichotomique | 3 | 7 | 10 | 20 |
| **O(n)** | Linéaire | Recherche linéaire | 10 | 100 | 1000 | 1M |
| **O(n log n)** | Quasi-linéaire | Tri fusion | 33 | 664 | 10 000 | 20M |
| **O(n²)** | Quadratique | Tri à bulles | 100 | 10 000 | 1M | 1T |

**Légende :** Nombre approximatif d'opérations

---

### A. O(1) — Complexité Constante

**Définition :** Le temps d'exécution ne dépend **PAS** de n.

**Exemples :**
```python
# Accéder à un élément par son index
element = liste[5]  # O(1)

# Ajouter à la fin d'une liste Python
liste.append(42)  # O(1) en moyenne

# Vérifier l'appartenance dans un set
if "alice" in users_set:  # O(1) en moyenne
    print("Trouvé")
```

**Graphique :**
```
Temps
  |
  |  ────────────────────────  O(1)
  |
  +─────────────────────────────→ n
```

---

### B. O(log n) — Complexité Logarithmique

**Définition :** Le temps croît **très lentement**. Diviser par 2 à chaque étape.

**Exemple :** Recherche dichotomique

**Intuition :**
- n = 1 000 → 10 étapes (log₂(1000) ≈ 10)
- n = 1 000 000 → 20 étapes (log₂(1M) ≈ 20)

**Si n × 1000, le temps × 2 seulement !**

**Graphique :**
```
Temps
  |
  |        ╱──────────────  O(log n)
  |      ╱
  |    ╱
  |  ╱
  +─────────────────────────────→ n
```

---

### C. O(n) — Complexité Linéaire

**Définition :** Le temps est **proportionnel** à n.

**Exemples :**
```python
# Parcourir une liste
for user in users:
    print(user)  # O(n)

# Recherche linéaire
for user in users:
    if user == "Martin":
        return user  # O(n) dans le pire cas

# Compter les occurrences
count = texte.count("error")  # O(n)
```

**Si n × 2, le temps × 2.**

**Graphique :**
```
Temps
  |                       ╱
  |                     ╱
  |                   ╱
  |                 ╱  O(n)
  |               ╱
  |             ╱
  +─────────────────────────────→ n
```

---

### D. O(n log n) — Complexité Quasi-Linéaire

**Définition :** Un peu plus que linéaire, mais bien meilleur que quadratique.

**Exemples :**
```python
# Tri fusion (merge sort)
liste_triee = sorted(liste)  # O(n log n)

# Tri rapide (quick sort)
liste.sort()  # O(n log n) en moyenne
```

**C'est la meilleure complexité possible pour trier par comparaison.**

**Graphique :**
```
Temps
  |                         ╱
  |                       ╱ O(n log n)
  |                     ╱
  |                   ╱  O(n)
  |                 ╱ ╱
  |               ╱ ╱
  +─────────────────────────────→ n
```

---

### E. O(n²) — Complexité Quadratique

**Définition :** Le temps croît au **carré** de n.

**Exemples :**
```python
# Double boucle imbriquée
for i in range(n):
    for j in range(n):
        print(i, j)  # O(n²)

# Tri à bulles (bubble sort)
# Compare chaque élément avec tous les autres
for i in range(n):
    for j in range(n-i-1):
        if liste[j] > liste[j+1]:
            # Échanger
            ...
```

**Si n × 2, le temps × 4. Si n × 10, le temps × 100.**

**⚠️ DANGER : Devient impraticable au-delà de n = 10 000.**

**Graphique :**
```
Temps
  |                               
  |                              ╱ O(n²)
  |                            ╱
  |                          ╱
  |                      ╱╱ O(n log n)
  |               ╱╱╱ ╱ O(n)
  |       ╱╱╱╱ ╱ ╱
  +─────────────────────────────→ n
```

**[ILLUSTRATION 1 : Graphique comparatif des 5 complexités]**  
*Légende : Graphique avec 5 courbes de couleurs différentes montrant la croissance de O(1) (ligne plate), O(log n) (très lente), O(n) (linéaire), O(n log n) (quasi-linéaire), et O(n²) (exponentielle)*

---

## 4️⃣ Meilleur Cas, Cas Moyen, Pire Cas

### Définitions

| **Cas** | **Définition** | **Exemple (recherche linéaire)** |
|---------|----------------|----------------------------------|
| **Meilleur cas** | Scénario optimal | Élément en première position → O(1) |
| **Cas moyen** | Scénario typique | Élément au milieu → O(n/2) = O(n) |
| **Pire cas** | Scénario catastrophe | Élément en dernière position ou absent → O(n) |

**Par défaut, Big-O décrit le PIRE CAS.**

### Exemple : Recherche Linéaire

**Liste :** `["alice", "bob", "charlie", "diane", "eve"]`

**Chercher "bob" :**

| **Cas** | **Position de "bob"** | **Nombre de comparaisons** |
|---------|------------------------|----------------------------|
| Meilleur cas | Indice 0 (1ère position) | 1 |
| Cas moyen | Indice 2 (milieu) | 3 |
| Pire cas | Indice 4 (dernière) ou absent | 5 |

**Complexité :**
- Meilleur cas : O(1)
- Cas moyen : O(n/2) = O(n)
- Pire cas : O(n)

**On dit que la recherche linéaire est O(n) car on analyse le PIRE CAS.**

---

## 5️⃣ Recherche Linéaire — O(n)

### Principe

**Parcourir la liste élément par élément jusqu'à trouver la cible.**

**Avantages :**
- Simple à implémenter
- Fonctionne sur une liste **non triée**

**Inconvénients :**
- Lent sur de grandes listes
- O(n) : proportionnel à la taille

### Algorithme en Pseudo-Code

```
FONCTION recherche_lineaire(liste, cible):
    POUR chaque élément dans liste:
        SI élément == cible:
            RETOURNER position
    RETOURNER "Non trouvé"
```

### Implémentation Python

```python
def recherche_lineaire(liste, cible):
    """
    Recherche linéaire : parcourt la liste de gauche à droite
    Complexité : O(n) dans le pire cas
    """
    for i in range(len(liste)):
        if liste[i] == cible:
            return i  # Position trouvée
    return -1  # Non trouvé

# Exemple d'utilisation
users = ["alice", "bob", "charlie", "diane", "eve"]
position = recherche_lineaire(users, "charlie")
print(f"Position : {position}")  # Position : 2
```

### Analyse de Complexité

**Pire cas :** Parcourir toute la liste → **n comparaisons** → **O(n)**

**Nombre d'opérations en fonction de n :**
- n = 10 → 10 comparaisons max
- n = 1 000 → 1 000 comparaisons max
- n = 1 000 000 → 1 000 000 comparaisons max

---

## 6️⃣ Recherche Dichotomique — O(log n)

### Principe

**Diviser la liste par 2 à chaque étape.**

**Prérequis OBLIGATOIRE :** La liste DOIT être **triée**.

**Algorithme :**
1. Regarder l'élément du **milieu**
2. Si c'est la cible → trouvé !
3. Si la cible est **avant** → chercher dans la **première moitié**
4. Si la cible est **après** → chercher dans la **deuxième moitié**
5. Répéter jusqu'à trouver ou épuiser les possibilités

### Exemple Visuel

**Rechercher 42 dans :** `[5, 12, 18, 23, 31, 42, 56, 67, 89, 91]`

```
Étape 1 : Liste [5, 12, 18, 23, 31, 42, 56, 67, 89, 91]
          Milieu = 31 (indice 4)
          42 > 31 → Chercher dans [42, 56, 67, 89, 91]

Étape 2 : Liste [42, 56, 67, 89, 91]
          Milieu = 67 (indice 2 relatif)
          42 < 67 → Chercher dans [42, 56]

Étape 3 : Liste [42, 56]
          Milieu = 42 (indice 0 relatif)
          42 == 42 → TROUVÉ !

Total : 3 comparaisons pour 10 éléments
```

**Avec recherche linéaire, il aurait fallu 6 comparaisons.**

### Algorithme en Pseudo-Code

```
FONCTION recherche_dichotomique(liste_triee, cible):
    debut = 0
    fin = longueur(liste) - 1
    
    TANT QUE debut <= fin:
        milieu = (debut + fin) // 2
        
        SI liste[milieu] == cible:
            RETOURNER milieu
        SINON SI liste[milieu] < cible:
            debut = milieu + 1
        SINON:
            fin = milieu - 1
    
    RETOURNER "Non trouvé"
```

### Implémentation Python

```python
def recherche_dichotomique(liste_triee, cible):
    """
    Recherche dichotomique : divise la liste par 2 à chaque étape
    Prérequis : la liste DOIT être triée
    Complexité : O(log n)
    """
    debut = 0
    fin = len(liste_triee) - 1
    
    while debut <= fin:
        milieu = (debut + fin) // 2
        
        if liste_triee[milieu] == cible:
            return milieu  # Trouvé
        elif liste_triee[milieu] < cible:
            debut = milieu + 1  # Chercher dans la moitié droite
        else:
            fin = milieu - 1  # Chercher dans la moitié gauche
    
    return -1  # Non trouvé

# Exemple d'utilisation
users_tries = ["alice", "bob", "charlie", "diane", "eve"]  # DÉJÀ TRIÉ
position = recherche_dichotomique(users_tries, "diane")
print(f"Position : {position}")  # Position : 3
```

### Analyse de Complexité

**Pire cas :** Diviser par 2 jusqu'à avoir 1 élément → **log₂(n) comparaisons** → **O(log n)**

**Nombre d'opérations en fonction de n :**
- n = 10 → 4 comparaisons max (log₂(10) ≈ 3.3)
- n = 1 000 → 10 comparaisons max
- n = 1 000 000 → 20 comparaisons max

**⚠️ ATTENTION : Nécessite un tri préalable (O(n log n)).**

**[ILLUSTRATION 2 : Schéma de la recherche dichotomique]**  
*Légende : Diagramme montrant un tableau avec flèches indiquant comment on divise par 2 à chaque étape (gauche/droite) jusqu'à trouver l'élément*

---

## 7️⃣ Comparaison : Linéaire vs Dichotomique

### Tableau Comparatif

| **Critère** | **Recherche Linéaire** | **Recherche Dichotomique** |
|-------------|------------------------|----------------------------|
| **Complexité** | O(n) | O(log n) |
| **Prérequis** | Aucun | Liste TRIÉE |
| **Implémentation** | Simple | Un peu plus complexe |
| **Performance (n=1000)** | 1 000 comparaisons max | 10 comparaisons max |
| **Performance (n=1M)** | 1 000 000 comparaisons max | 20 comparaisons max |
| **Quand l'utiliser ?** | Petites listes, listes non triées | Grandes listes triées |

### Quand Utiliser Chaque Algorithme ?

**Recherche linéaire :**
- ✅ Liste non triée
- ✅ Petite liste (< 100 éléments)
- ✅ Une seule recherche

**Recherche dichotomique :**
- ✅ Liste déjà triée
- ✅ Grande liste (> 1 000 éléments)
- ✅ Plusieurs recherches (le tri devient rentable)

### Calcul du Seuil de Rentabilité

**Question :** À partir de combien de recherches le tri devient-il rentable ?

**Données :**
- Trier : O(n log n) — par exemple, 10 000 opérations pour n=1000
- Recherche linéaire : O(n) — 1 000 opérations par recherche
- Recherche dichotomique : O(log n) — 10 opérations par recherche

**Calcul :**
```
Coût sans tri : k × 1000 (k = nombre de recherches)
Coût avec tri : 10 000 + k × 10

Seuil : 10 000 + k × 10 = k × 1000
        10 000 = k × 990
        k ≈ 10

→ Dès la 10e recherche, trier devient rentable
```

---

## 8️⃣ Mesurer les Temps d'Exécution en Python

### Utiliser le Module `time`

```python
import time

# Créer une grande liste
import random
users = [f"user_{i:06d}" for i in range(100000)]
random.shuffle(users)  # Mélanger

# Mesurer la recherche linéaire
debut = time.time()
position = recherche_lineaire(users, "user_099999")  # Pire cas (dernier)
fin = time.time()
temps_lineaire = fin - debut

print(f"Recherche linéaire : {temps_lineaire:.4f} secondes")
# Résultat : ~0.0050 secondes

# Trier la liste pour la dichotomique
users_tries = sorted(users)

# Mesurer la recherche dichotomique
debut = time.time()
position = recherche_dichotomique(users_tries, "user_099999")
fin = time.time()
temps_dichotomique = fin - debut

print(f"Recherche dichotomique : {temps_dichotomique:.6f} secondes")
# Résultat : ~0.000015 secondes

# Comparaison
ratio = temps_lineaire / temps_dichotomique
print(f"Gain : {ratio:.0f}x plus rapide")
# Résultat : ~333x plus rapide
```

### Générer un Tableau de Comparaison

```python
import time

def comparer_algorithmes(tailles):
    """Compare les deux algorithmes sur différentes tailles de données"""
    print("╔═══════════════════════════════════════════════════════════╗")
    print("║     COMPARAISON RECHERCHE LINÉAIRE VS DICHOTOMIQUE        ║")
    print("╠═══════════════════════════════════════════════════════════╣")
    print("║ Taille │ Linéaire (ms) │ Dichotomique (ms) │ Gain (x)    ║")
    print("╠════════╪═══════════════╪═══════════════════╪═════════════╣")
    
    for n in tailles:
        # Créer liste
        liste = list(range(n))
        cible = n - 1  # Pire cas (dernier élément)
        
        # Mesurer linéaire
        debut = time.time()
        recherche_lineaire(liste, cible)
        temps_lin = (time.time() - debut) * 1000  # Convertir en ms
        
        # Mesurer dichotomique
        debut = time.time()
        recherche_dichotomique(liste, cible)
        temps_dicho = (time.time() - debut) * 1000  # Convertir en ms
        
        gain = temps_lin / temps_dicho if temps_dicho > 0 else 0
        
        print(f"║ {n:6} │ {temps_lin:13.4f} │ {temps_dicho:17.6f} │ {gain:11.0f} ║")
    
    print("╚═══════════════════════════════════════════════════════════╝")

# Exécuter la comparaison
comparer_algorithmes([100, 1000, 10000, 100000])
```

**Résultat typique :**
```
╔═══════════════════════════════════════════════════════════╗
║     COMPARAISON RECHERCHE LINÉAIRE VS DICHOTOMIQUE        ║
╠═══════════════════════════════════════════════════════════╣
║ Taille │ Linéaire (ms) │ Dichotomique (ms) │ Gain (x)    ║
╠════════╪═══════════════╪═══════════════════╪═════════════╣
║    100 │        0.0018 │           0.000002 │         900 ║
║   1000 │        0.0215 │           0.000003 │        7167 ║
║  10000 │        0.2854 │           0.000004 │       71350 ║
║ 100000 │        3.1247 │           0.000005 │      624940 ║
╚═══════════════════════════════════════════════════════════╝
```

**Observation :** Plus n augmente, plus le gain de la dichotomique explose.

---

## 9️⃣ Application : Recherche dans un Annuaire AD

### Contexte

**Entreprise avec 10 000 employés. Script qui vérifie si un utilisateur existe.**

### Script Naïf (O(n))

```python
# Charger les utilisateurs depuis AD (simplifié)
import pyad  # Bibliothèque Python pour AD

def verifier_utilisateur_v1(username):
    """Version lente : O(n)"""
    users = pyad.adquery.get_all_users()  # 10 000 utilisateurs
    
    for user in users:
        if user.samAccountName == username:
            return True
    return False

# Mesure
import time
debut = time.time()
existe = verifier_utilisateur_v1("martin.jean")
print(f"Temps : {time.time() - debut:.3f}s")
# Résultat : ~0.500 secondes (500 ms)
```

### Script Optimisé (O(log n))

```python
def verifier_utilisateur_v2(username):
    """Version rapide : O(log n) avec cache trié"""
    # 1. Charger et trier UNE FOIS (au démarrage du script)
    if not hasattr(verifier_utilisateur_v2, 'cache'):
        users = pyad.adquery.get_all_users()
        verifier_utilisateur_v2.cache = sorted(
            [u.samAccountName for u in users]
        )
    
    # 2. Recherche dichotomique dans le cache
    return recherche_dichotomique(
        verifier_utilisateur_v2.cache, 
        username
    ) != -1

# Mesure
debut = time.time()
existe = verifier_utilisateur_v2("martin.jean")
print(f"Temps : {time.time() - debut:.6f}s")
# Résultat : ~0.000015 secondes (0.015 ms)
```

**Gain : 33 000 fois plus rapide !**

**Impact :** Le script peut gérer 100 000 requêtes/seconde au lieu de 3 requêtes/seconde.

---

## 📝 Fiche Récapitulative (À Garder)

### Les 5 Complexités

| **Big-O** | **Nom** | **Croissance** | **Exemple** |
|-----------|---------|----------------|-------------|
| O(1) | Constante | Plate | Accès `liste[i]` |
| O(log n) | Logarithmique | Très lente | Recherche dichotomique |
| O(n) | Linéaire | Proportionnelle | Recherche linéaire |
| O(n log n) | Quasi-linéaire | Un peu plus que linéaire | Tri fusion |
| O(n²) | Quadratique | Exponentielle | Double boucle |

### Recherche Linéaire vs Dichotomique

| | **Linéaire** | **Dichotomique** |
|---|---|---|
| **Code** | `for x in liste: if x == cible` | `while debut <= fin: milieu = ...` |
| **Prérequis** | Aucun | Liste TRIÉE |
| **Complexité** | O(n) | O(log n) |
| **n=1000** | 1 000 ops | 10 ops |
| **n=1M** | 1 000 000 ops | 20 ops |

### Mesure de Performance

```python
import time

# Chronomètre
debut = time.time()
# ... code à mesurer ...
temps = time.time() - debut
print(f"Temps : {temps:.6f}s")
```

---

## 🎯 Compétences Travaillées (Référentiel RNCP)

| **Code** | **Compétence** | **Application dans cette séance** |
|----------|----------------|-----------------------------------|
| **B2.1** | Concevoir une solution applicative | Choisir le bon algorithme selon le contexte |
| **B2.2** | Assurer la sécurité d'un système | Éviter les algorithmes lents (DoS) |
| **B3.3** | Optimiser les performances | Mesurer et comparer les temps d'exécution |

---

## 💡 Pour Aller Plus Loin

- **Interpolation search** : O(log log n) si données uniformément distribuées
- **Complexité spatiale** : Mémoire utilisée (en plus du temps)
- **Amortized complexity** : Complexité moyenne sur plusieurs opérations
- **NP-complet** : Problèmes pour lesquels aucun algorithme polynomial n'est connu

---

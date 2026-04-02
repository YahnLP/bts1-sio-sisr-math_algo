---
author: YLP
title: 📌 FICHE BILAN & MÉMO
---

# 📌 FICHE BILAN & MÉMO
## S15 — Complexité Algorithmique : L'Essentiel à Retenir

*BTS SIO SISR — Année 1 — Semaine 15*

---

## 🎯 Synthèse de la Séance

| **Élément** | **Détail** |
|-------------|-----------|
| **Thème** | Complexité algorithmique et optimisation |
| **Application** | Recherche linéaire vs dichotomique |
| **Compétences** | Analyser, mesurer, optimiser des algorithmes |
| **Durée** | 4 heures |
| **Livrable** | Script optimisé + rapport de performance |

---

## ✅ Objectifs Atteints

À l'issue de cette séance, vous devez être capable de :

- ✅ Expliquer ce qu'est la complexité algorithmique
- ✅ Utiliser la notation Big-O (O(1), O(log n), O(n), O(n²))
- ✅ Distinguer meilleur cas, cas moyen, pire cas
- ✅ Implémenter une recherche linéaire (O(n))
- ✅ Implémenter une recherche dichotomique (O(log n))
- ✅ Comprendre pourquoi la dichotomique nécessite un tri
- ✅ Mesurer les temps d'exécution avec `time.time()`
- ✅ Comparer deux algorithmes et choisir le meilleur
- ✅ Calculer des projections de performance

---

## 🔑 Les 5 Complexités Essentielles

### Tableau Récapitulatif

| **Big-O** | **Nom** | **Croissance** | **n=1000** | **n=1M** | **Exemple** |
|-----------|---------|----------------|------------|----------|-------------|
| **O(1)** | Constante | Plate | 1 | 1 | `liste[5]` |
| **O(log n)** | Logarithmique | Très lente | 10 | 20 | Recherche dichotomique |
| **O(n)** | Linéaire | Proportionnelle | 1 000 | 1M | Recherche linéaire |
| **O(n log n)** | Quasi-linéaire | Un peu plus | 10 000 | 20M | Tri fusion |
| **O(n²)** | Quadratique | Exponentielle | 1M | 1T | Double boucle |

### Visualisation Graphique

```
Opérations
     │
1T   │                                               ⬤ O(n²)
     │                                            ⬤
     │                                         ⬤
1M   │                                     ⬤
     │                                  ⬤
1000 │                            ⬤ ⬤ O(n log n)
     │                      ⬤ ⬤ ⬤ ────── O(n)
  10 │  ⬤ ⬤ ⬤ ⬤ ⬤ ⬤ ⬤ ⬤ ──────────── O(log n)
     │  ──────────────────────────── O(1)
   1 +─────────────────────────────────────
     0    1k    10k   100k   1M   10M  (n)
```

**Message clé :** À partir de n = 10 000 :
- O(log n) reste gérable
- O(n) devient lent
- O(n²) devient **impraticable**

---

## 📊 Recherche Linéaire vs Dichotomique

### Comparaison Visuelle

#### Recherche Linéaire (O(n))

```
Liste : [5, 12, 18, 23, 31, 42, 56, 67, 89, 91]
Chercher : 67

Étape 1 : Vérifier 5  → Non
Étape 2 : Vérifier 12 → Non
Étape 3 : Vérifier 18 → Non
Étape 4 : Vérifier 23 → Non
Étape 5 : Vérifier 31 → Non
Étape 6 : Vérifier 42 → Non
Étape 7 : Vérifier 56 → Non
Étape 8 : Vérifier 67 → OUI ✅

Total : 8 vérifications
```

#### Recherche Dichotomique (O(log n))

```
Liste TRIÉE : [5, 12, 18, 23, 31, 42, 56, 67, 89, 91]
Chercher : 67

Étape 1 : Milieu = 31 → 67 > 31 → Chercher dans [42, 56, 67, 89, 91]
Étape 2 : Milieu = 67 → 67 == 67 → TROUVÉ ✅

Total : 2 vérifications
```

**Gain : 4x plus rapide sur seulement 10 éléments.**

---

### Tableau Comparatif Complet

| **Critère** | **Linéaire** | **Dichotomique** |
|-------------|--------------|------------------|
| **Complexité** | O(n) | O(log n) |
| **Prérequis** | Aucun | Liste **TRIÉE** |
| **Code** | 3 lignes (simple) | 10 lignes (plus complexe) |
| **n=100** | 100 ops | 7 ops |
| **n=1 000** | 1 000 ops | 10 ops |
| **n=10 000** | 10 000 ops | 14 ops |
| **n=100 000** | 100 000 ops | 17 ops |
| **n=1 000 000** | 1 000 000 ops | 20 ops |
| **Quand utiliser ?** | Petites listes, non triées | Grandes listes triées, recherches multiples |

---

## 💻 Code à Connaître Par Cœur

### Recherche Linéaire (3 lignes)

```python
def recherche_lineaire(liste, cible):
    for i, element in enumerate(liste):
        if element == cible:
            return i
    return -1
```

**Complexité :** O(n) — parcourt toute la liste dans le pire cas

---

### Recherche Dichotomique (10 lignes)

```python
def recherche_dichotomique(liste_triee, cible):
    debut, fin = 0, len(liste_triee) - 1
    
    while debut <= fin:
        milieu = (debut + fin) // 2
        
        if liste_triee[milieu] == cible:
            return milieu
        elif liste_triee[milieu] < cible:
            debut = milieu + 1
        else:
            fin = milieu - 1
    
    return -1
```

**Complexité :** O(log n) — divise par 2 à chaque étape

**⚠️ OBLIGATOIRE :** La liste DOIT être triée avant !

---

### Mesurer le Temps d'Exécution

```python
import time

# Chronométrer un algorithme
debut = time.time()
resultat = mon_algorithme(data)
temps = time.time() - debut

print(f"Temps : {temps:.6f} secondes")
print(f"Temps : {temps*1000:.4f} millisecondes")
```

---

## 🧮 Calculs de Projections

### Formules à Retenir

| **Complexité** | **Si n × k, temps × ?** | **Exemple** |
|----------------|-------------------------|-------------|
| O(1) | × 1 (constant) | n × 10 → temps × 1 |
| O(log n) | × log₂(k) | n × 10 → temps × 3.32 |
| O(n) | × k | n × 10 → temps × 10 |
| O(n log n) | × k log₂(k) | n × 10 → temps × 33.2 |
| O(n²) | × k² | n × 10 → temps × 100 |

### Exemple de Calcul

**Situation :**
- Actuellement : 10 000 logs, recherche linéaire prend 0.5 ms
- Dans 6 mois : 100 000 logs (× 10)

**Question :** Combien de temps prendra la recherche ?

**Réponse :**
```
Recherche linéaire : O(n)
→ n × 10 = temps × 10
→ 0.5 ms × 10 = 5 ms

Recherche dichotomique : O(log n)
→ n × 10 = temps × log₂(10) ≈ temps × 3.32
→ Si actuellement 0.01 ms, futur = 0.033 ms
```

---

## 🎯 Quand Utiliser Quel Algorithme ?

### Arbre de Décision

```
┌─────────────────────────────────────┐
│  Combien de recherches ?            │
└────────────┬────────────────────────┘
             │
     ┌───────┴────────┐
     │                │
  1 seule         Plusieurs (≥10)
     │                │
     ▼                ▼
  ┌─────────────┐  ┌──────────────────┐
  │  La liste   │  │  Trier d'abord   │
  │  est-elle   │  │  puis utiliser   │
  │  triée ?    │  │  dichotomique    │
  └──────┬──────┘  └──────────────────┘
         │
    ┌────┴────┐
    │         │
  NON       OUI
    │         │
    ▼         ▼
 Linéaire  Dichotomique
 O(n)      O(log n)
```

### Règles Pratiques

**Utiliser la recherche linéaire si :**
- ✅ n < 100 (négligeable)
- ✅ Liste non triée et vous ne faites qu'une recherche
- ✅ Simplicité du code prioritaire

**Utiliser la recherche dichotomique si :**
- ✅ n > 1 000 (différence significative)
- ✅ Liste déjà triée ou vous faites plusieurs recherches
- ✅ Performance critique

**Trier puis utiliser dichotomique si :**
- ✅ Vous faites ≥ 10 recherches
- ✅ Le tri coûte O(n log n), mais toutes les recherches suivantes profitent

---

## 🧠 Auto-Évaluation

**Cochez les compétences que vous maîtrisez maintenant :**

| **Je sais...** | **Maîtrisé ?** |
|----------------|----------------|
| Expliquer ce qu'est la complexité algorithmique | ☐ |
| Lire et interpréter la notation Big-O | ☐ |
| Dire quel algorithme est O(n) et lequel est O(log n) | ☐ |
| Implémenter une recherche linéaire en Python | ☐ |
| Implémenter une recherche dichotomique en Python | ☐ |
| Trier une liste avec `sorted()` | ☐ |
| Mesurer le temps avec `time.time()` | ☐ |
| Comparer deux algorithmes sur plusieurs tailles | ☐ |
| Calculer une projection (n × 10 → temps × ?) | ☐ |
| Expliquer pourquoi la dichotomique nécessite un tri | ☐ |
| Calculer le seuil de rentabilité du tri | ☐ |
| Choisir le bon algorithme selon le contexte | ☐ |

**Si vous avez coché < 9 cases, revoir la fiche de cours et refaire le TP.**

---

## 💡 Exercices d'Entraînement

### Exercice 1 : Identifier la Complexité

**Pour chaque code, donnez la complexité :**

```python
# Code A
def fonction_a(liste):
    return liste[0]

# Code B
def fonction_b(liste):
    for element in liste:
        print(element)

# Code C
def fonction_c(liste):
    for i in liste:
        for j in liste:
            print(i, j)

# Code D
def fonction_d(liste_triee, cible):
    debut, fin = 0, len(liste_triee) - 1
    while debut <= fin:
        milieu = (debut + fin) // 2
        if liste_triee[milieu] == cible:
            return milieu
        elif liste_triee[milieu] < cible:
            debut = milieu + 1
        else:
            fin = milieu - 1
```

**Solutions :**
- Code A : O(1) — accès direct
- Code B : O(n) — une boucle
- Code C : O(n²) — deux boucles imbriquées
- Code D : O(log n) — recherche dichotomique

---

### Exercice 2 : Projections

**Données :**
- Algorithme A : O(n), prend 0.5 s pour n=1000
- Algorithme B : O(n²), prend 1 s pour n=1000

**Questions :**

1. Si n × 10 (n=10 000), combien de temps prendra A ?
2. Si n × 10 (n=10 000), combien de temps prendra B ?
3. Lequel devient trop lent ?

**Solutions :**
1. A : O(n) → n×10 = temps×10 → 0.5s × 10 = **5 secondes**
2. B : O(n²) → n×10 = temps×100 → 1s × 100 = **100 secondes**
3. B devient impraticable (1 min 40s)

---

### Exercice 3 : Seuil de Rentabilité

**Données :**
- Trier 10 000 éléments : 50 ms
- Recherche linéaire : 10 ms par recherche
- Recherche dichotomique : 0.01 ms par recherche

**Question :** À partir de combien de recherches le tri devient-il rentable ?

**Solution :**
```
Coût sans tri : k × 10 ms (k = nombre de recherches)
Coût avec tri : 50 ms + k × 0.01 ms

Seuil : 50 + k × 0.01 = k × 10
        50 = k × 9.99
        k ≈ 5

→ Dès la 6e recherche, trier devient rentable
```

---

## 🔄 Lien avec les Autres Séances

| **Séance** | **Lien avec S15** |
|------------|------------------|
| **S3** | Listes → Les algorithmes opèrent sur des listes |
| **S4** | Boucles → La complexité dépend des boucles |
| **S5** | Fonctions → Encapsuler les algorithmes |
| **S16** | Algorithmes de tri → Trier avant dichotomique |
| **BLOC 1 - S12** | Bases de données : index SQL = arbres B+ (O(log n)) |
| **BLOC 2 - S10** | Profiling et optimisation applicative |

---

## 📚 Ressources pour Aller Plus Loin

### Documentation et Tutoriels

- **Big-O Cheat Sheet** : [bigocheatsheet.com](https://www.bigocheatsheet.com/) — Tableau des complexités courantes
- **Visualgo** : [visualgo.net](https://visualgo.net/en/sorting) — Animations d'algorithmes
- **Khan Academy** : "Analyse d'algorithmes" (cours gratuit, sous-titres FR)
- **Python `timeit`** : [docs.python.org/3/library/timeit.html](https://docs.python.org/3/library/timeit.html) — Mesure précise

### Vidéos Recommandées

- **"What is Big-O?"** — CS Dojo (YouTube, 15 min, sous-titres FR)
- **"Binary Search Explained"** — freeCodeCamp (YouTube, 10 min)

---

## 🎓 Pourquoi C'est Important en Administration Système ?

### Impact Réel sur l'Infrastructure

| **Scénario** | **Algorithme lent** | **Algorithme rapide** | **Impact** |
|--------------|---------------------|-----------------------|------------|
| **Recherche dans AD** | 500 ms/requête | 0.01 ms/requête | CPU libéré, serveur moins puissant nécessaire |
| **Analyse de logs** | 5 min/jour | 3 s/jour | Économie 5 min × 365 = 30h/an |
| **Requête SQL** | 10 s sans index | 0.001 s avec index | UX acceptable vs inacceptable |
| **Script cron** | Sature le CPU | Tourne en arrière-plan | Pas d'impact sur les users |

### Coûts Cloud Évités

**Exemple concret :**

Entreprise avec 100 000 requêtes/jour sur une API :
- **Avec O(n²)** : Nécessite serveur 32 vCPU = **500€/mois**
- **Avec O(n log n)** : Nécessite serveur 2 vCPU = **50€/mois**

**Économie annuelle :** 5 400€

**ROI :** 2 heures d'optimisation = 5 400€ économisés

---

## 💬 Citations à Retenir

> *"Premature optimization is the root of all evil."*  
> — Donald Knuth

**Signification :** N'optimisez pas sans avoir identifié le goulot d'étranglement. Mais quand vous optimisez, choisissez le BON algorithme.

---

> *"Un algorithme O(n²) sur 10 éléments, c'est pas grave. Sur 10 000 éléments, c'est une catastrophe."*  
> — Sagesse du développeur

---

> *"La différence entre O(n) et O(log n), c'est la différence entre 1 seconde et 12 heures."*  
> — Réalité des gros volumes de données

---

## 📅 Prochaine Séance : S16

### Thème : Algorithmes de Tri

**Ce que vous allez apprendre :**
- Tri à bulles (O(n²)) — simple mais lent
- Tri fusion (O(n log n)) — optimal
- Tri rapide (O(n log n) en moyenne) — le plus utilisé
- Mesurer et comparer les performances

**Application :**
- Trier un annuaire de 10 000 utilisateurs
- Comprendre pourquoi Python utilise Timsort
- Préparer des données pour la recherche dichotomique

**Prérequis S16 :** Maîtrise de la complexité (S15) ✅

---

## 🎯 Mot de la Fin

**Félicitations !** Vous venez de maîtriser un concept **fondamental** en informatique.

La complexité algorithmique, ce n'est pas que de la théorie :
- 🔧 **C'est la base de l'optimisation**
- 📊 **C'est la clé de la scalabilité**
- 🚀 **C'est la différence entre un serveur surchargé et un serveur efficace**
- 💰 **C'est des milliers d'euros économisés en infrastructure**

**Un bon technicien SISR sait que :**
> Choisir le mauvais algorithme = serveur qui rame  
> Choisir le bon algorithme = serveur performant  
> Optimiser = créer de la valeur business

**Les 3 règles d'or :**
1. **Mesurer avant d'optimiser** (pas d'intuition)
2. **Choisir l'algorithme selon le contexte** (n petit ? n grand ? trié ?)
3. **Documenter les choix** (complexité dans les commentaires)

---

## 🏆 Challenge Final

**Testez vos connaissances :**

**Question :** Vous devez chercher 1 000 fois dans un fichier de 100 000 lignes. Quelle est la meilleure stratégie ?

A) Recherche linéaire à chaque fois  
B) Trier puis recherche dichotomique  
C) Recherche dichotomique sans trier  

**Réponse :** **B**

**Justification :**
- A : 1000 × 100 000 = 100 000 000 opérations
- B : Tri (100 000 × 17) + 1000 × 17 = 1 717 000 opérations
- C : Impossible (dichotomique nécessite tri)

**Gain B vs A :** 58 fois plus rapide !

---

---
author: YLP
title: 📖 FICHE DE SYNTHÈSE

---

# 📖 FICHE DE COURS  — SYNTHÈSE
## Révisions Générales : L'Essentiel à Retenir

---

## 🎯 Structure de la Révision

Cette fiche synthétise **3 blocs** essentiels vus depuis septembre :

1. **Algèbre de Boole** (logique, tables de vérité)
2. **Subnetting VLSM** (binaire, masques, optimisation)
3. **Algorithmique** (complexité, recherche, débit)

---

## 📊 BLOC 1 : ALGÈBRE DE BOOLE

### Les 4 Opérateurs Fondamentaux

| Opérateur | Symbole | Table de vérité | Signification |
|-----------|---------|-----------------|---------------|
| **AND** | ∧ | 1 ∧ 1 = 1<br>1 ∧ 0 = 0<br>0 ∧ 1 = 0<br>0 ∧ 0 = 0 | Vrai si les DEUX vrais |
| **OR** | ∨ | 1 ∨ 1 = 1<br>1 ∨ 0 = 1<br>0 ∨ 1 = 1<br>0 ∨ 0 = 0 | Vrai si AU MOINS UN vrai |
| **NOT** | ¬ | ¬1 = 0<br>¬0 = 1 | Inverse la valeur |
| **XOR** | ⊕ | 1 ⊕ 1 = 0<br>1 ⊕ 0 = 1<br>0 ⊕ 1 = 1<br>0 ⊕ 0 = 0 | Vrai si DIFFÉRENTS |

---

### Lois Essentielles

**Lois de De Morgan :**
```
¬(a ∧ b) = ¬a ∨ ¬b
¬(a ∨ b) = ¬a ∧ ¬b
```

**Lois de simplification :**
```
a ∧ a = a        (Idempotence)
a ∨ a = a        (Idempotence)
a ∧ 1 = a        (Élément neutre)
a ∨ 0 = a        (Élément neutre)
a ∧ 0 = 0        (Élément absorbant)
a ∨ 1 = 1        (Élément absorbant)
a ∧ ¬a = 0       (Complémentarité)
a ∨ ¬a = 1       (Tiers exclu)
```

---

### Méthode : Construire une Table de Vérité

**Exemple : (a ∧ b) ∨ ¬c**

```
┌───┬───┬───┬─────┬────┬──────────────┐
│ a │ b │ c │ a∧b │ ¬c │ (a∧b) ∨ ¬c  │
├───┼───┼───┼─────┼────┼──────────────┤
│ 0 │ 0 │ 0 │  0  │ 1  │      1       │
│ 0 │ 0 │ 1 │  0  │ 0  │      0       │
│ 0 │ 1 │ 0 │  0  │ 1  │      1       │
│ 0 │ 1 │ 1 │  0  │ 0  │      0       │
│ 1 │ 0 │ 0 │  0  │ 1  │      1       │
│ 1 │ 0 │ 1 │  0  │ 0  │      0       │
│ 1 │ 1 │ 0 │  1  │ 1  │      1       │
│ 1 │ 1 │ 1 │  1  │ 0  │      1       │
└───┴───┴───┴─────┴────┴──────────────┘
```

**Méthode :**
1. Lister toutes les combinaisons (2^n lignes pour n variables)
2. Calculer les sous-expressions (colonnes intermédiaires)
3. Calculer l'expression finale

---

## 📊 BLOC 2 : SUBNETTING & VLSM

### Puissances de 2 à Mémoriser

| n | 2^n | Masque | Hôtes (2^n - 2) |
|---|-----|--------|-----------------|
| 3 | 8 | /29 | 6 |
| 4 | 16 | /28 | 14 |
| 5 | 32 | /27 | 30 |
| 6 | 64 | /26 | 62 |
| 7 | 128 | /25 | 126 |
| 8 | 256 | /24 | 254 |

---

### Formules Essentielles

```
Hôtes disponibles = 2^n - 2
Masque CIDR = 32 - n
Taille du sous-réseau = 2^n
```

**Exemple :**
- Besoin : 50 hôtes
- Calcul : 50 + 2 = 52 → 2^6 = 64 ≥ 52
- Masque : 32 - 6 = /26
- Hôtes : 64 - 2 = 62

---

### Conversion Décimal ↔ Binaire

**Méthode décimal → binaire :**
```
192 en binaire ?
192 = 128 + 64 = 2^7 + 2^6
192 = 11000000
```

**Méthode binaire → décimal :**
```
11000000 = ?
1×128 + 1×64 + 0×32 + 0×16 + 0×8 + 0×4 + 0×2 + 0×1
= 128 + 64 = 192
```

**En Python :**
```python
# Décimal → Binaire
bin(192)  # '0b11000000'

# Binaire → Décimal
int('11000000', 2)  # 192
```

---

### Algorithme VLSM

**Principe :** Optimiser le découpage d'une plage IP.

**Étapes :**
1. **Trier** les besoins par ordre **décroissant**
2. Pour chaque besoin :
   - Calculer le masque optimal
   - Assigner l'adresse
   - Passer au suivant
3. Vérifier qu'il reste de la place

**Code Python :**
```python
def vlsm_optimal(besoins):
    besoins_tries = sorted(besoins, reverse=True)
    
    plan = []
    for nb_hotes in besoins_tries:
        # +2 pour réseau et broadcast
        nb_adresses = nb_hotes + 2
        n = math.ceil(math.log2(nb_adresses))
        masque = 32 - n
        
        plan.append({
            'hotes': nb_hotes,
            'masque': masque
        })
    
    return plan
```

---

## 📊 BLOC 3 : ALGORITHMIQUE

### Complexités à Connaître

| Notation | Nom | Exemple | n=1000 |
|----------|-----|---------|--------|
| **O(1)** | Constante | Accès liste[i] | 1 |
| **O(log n)** | Logarithmique | Recherche dichotomique | 10 |
| **O(n)** | Linéaire | Recherche linéaire | 1000 |
| **O(n log n)** | Quasi-linéaire | Tri fusion | 10000 |
| **O(n²)** | Quadratique | Double boucle | 1000000 |

---

### Algorithmes de Recherche

**Recherche Linéaire (O(n)) :**
```python
def recherche_lineaire(liste, cible):
    for i, element in enumerate(liste):
        if element == cible:
            return i
    return -1
```

**Recherche Dichotomique (O(log n)) :**
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

**⚠️ Dichotomique nécessite une liste TRIÉE.**

---

### Calculs de Débit

**Formule fondamentale :**
```
Temps (s) = Taille (Mo) ÷ Débit (Mo/s)
```

**Conversion bits ↔ octets :**
```
1 octet = 8 bits
Mbps ÷ 8 = Mo/s
Mo/s × 8 = Mbps
```

**Exemple :**
```
Fichier : 500 Mo
Débit : 100 Mbps

Étape 1 : 100 Mbps ÷ 8 = 12.5 Mo/s
Étape 2 : 500 Mo ÷ 12.5 Mo/s = 40 secondes
```

---

### Opérations sur les Ensembles

**En Python :**
```python
A = {1, 2, 3}
B = {3, 4, 5}

A | B   # Union : {1, 2, 3, 4, 5}
A & B   # Intersection : {3}
A - B   # Différence : {1, 2}
```

---

## 📝 Exercices de Révision Rapide

### Exercice 1 : Algèbre de Boole

**Simplifiez : (a ∧ b) ∨ (a ∧ ¬b)**

**Solution :**
```
= a ∧ (b ∨ ¬b)    [Factorisation]
= a ∧ 1           [Tiers exclu]
= a               [Élément neutre]
```

---

### Exercice 2 : Subnetting

**Calculez le masque pour 120 hôtes**

**Solution :**
```
120 + 2 = 122
2^n ≥ 122 → 2^7 = 128
Masque = 32 - 7 = /25
```

---

### Exercice 3 : Complexité

**Quelle est la complexité de ce code ?**
```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

**Solution :** O(n²) (double boucle imbriquée)

---

### Exercice 4 : Débit

**Temps pour transférer 2 Go à 200 Mbps ?**

**Solution :**
```
2 Go = 2048 Mo
200 Mbps ÷ 8 = 25 Mo/s
Temps = 2048 ÷ 25 = 81.92 secondes ≈ 1.4 minutes
```

---

## 🎯 Checklist Pré-Examen

### Je sais...

**Algèbre de Boole :**
- ☐ Construire une table de vérité
- ☐ Appliquer les lois de De Morgan
- ☐ Simplifier une expression

**Subnetting :**
- ☐ Calculer 2^6 de tête (64)
- ☐ Convertir décimal ↔ binaire
- ☐ Calculer un masque pour n hôtes
- ☐ Appliquer l'algorithme VLSM

**Algorithmique :**
- ☐ Identifier O(n) vs O(n²)
- ☐ Implémenter recherche linéaire
- ☐ Implémenter recherche dichotomique
- ☐ Calculer temps = taille ÷ débit
- ☐ Convertir Mbps → Mo/s

---

## 💡 Conseils pour l'Examen

1. **Lire tout le sujet** (5 min)
2. **Commencer par ce qu'on maîtrise**
3. **Gérer son temps** (ne pas bloquer > 5 min)
4. **Vérifier les unités** (bits vs octets)
5. **Relire** avant de rendre

---
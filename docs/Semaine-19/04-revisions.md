---
author: YLP
title: 📝 REVISIONS POUR L'EXAMEN BLANC

---

# 📝 REVISIONS POUR L'EXAMEN BLANC

**Durée :** 1h25 (85 minutes)  
**Barème :** /20  
**Documents autorisés :** Fiche mémo A4 recto manuscrite uniquement  
**Calculatrice autorisée**
---

## 📋 Consignes

- Répondre directement sur le sujet
- Montrer les calculs intermédiaires
- Vérifier les unités (bits vs octets)
- Gérer son temps (indication de durée par partie)

---

## PARTIE 1 : ALGÈBRE DE BOOLE (6 points — 25 min)

### Exercice 1.1 : Table de Vérité (3 points)

**Complétez la table de vérité de l'expression : (a ∨ b) ∧ ¬c**

```
┌───┬───┬───┬─────┬────┬──────────────┐
│ a │ b │ c │ a∨b │ ¬c │ (a∨b) ∧ ¬c  │
├───┼───┼───┼─────┼────┼──────────────┤
│ 0 │ 0 │ 0 │     │    │              │
│ 0 │ 0 │ 1 │     │    │              │
│ 0 │ 1 │ 0 │     │    │              │
│ 0 │ 1 │ 1 │     │    │              │
│ 1 │ 0 │ 0 │     │    │              │
│ 1 │ 0 │ 1 │     │    │              │
│ 1 │ 1 │ 0 │     │    │              │
│ 1 │ 1 │ 1 │     │    │              │
└───┴───┴───┴─────┴────┴──────────────┘
```

**Barème :** 0.5 pt par colonne (a∨b, ¬c, résultat)

---

### Exercice 1.2 : Simplification (3 points)

**Simplifiez les expressions suivantes :**

**a)** `(a ∧ b) ∨ (a ∧ ¬b)` (1.5 pts)

```
Étape 1 : ________________________________

Étape 2 : ________________________________

Résultat : ________________________________
```

**b)** `¬(a ∨ b)` (application de De Morgan) (1.5 pts)

```
Résultat : ________________________________
```

---

## PARTIE 2 : SUBNETTING & VLSM (7 points — 30 min)

### Exercice 2.1 : Conversions (2 points)

**a)** Convertissez **224** en binaire : _________________ (1 pt)

**b)** Convertissez **10101100** en décimal : _________________ (1 pt)

---

### Exercice 2.2 : Calcul de Masques (2 points)

**Pour chaque besoin, calculez le masque optimal :**

**Site A : 80 hôtes**
```
80 + 2 = ___ adresses nécessaires
2^n ≥ ___ → 2^? = ___
Masque : /___
```
(1 pt)

**Site B : 15 hôtes**
```
15 + 2 = ___ adresses
2^n ≥ ___ → 2^? = ___
Masque : /___
```
(1 pt)

---

### Exercice 2.3 : Plan d'Adressage VLSM (3 points)

**Contexte :** Vous devez créer un plan d'adressage pour 3 sites à partir de la plage **172.16.0.0/24** (256 adresses).

**Sites :**
- Site 1 : 100 PC
- Site 2 : 30 PC
- Site 3 : 10 PC

**Complétez le tableau :**

```
┌────────┬────────┬────────┬─────────────┬──────────────┐
│ Site   │ Hôtes  │ Masque │ Taille (IP) │ Réseau       │
├────────┼────────┼────────┼─────────────┼──────────────┤
│ Site 1 │  100   │  /___  │    ___      │ 172.16.0.0   │
│ Site 2 │   30   │  /___  │    ___      │ 172.16.0.128 │
│ Site 3 │   10   │  /___  │    ___      │ 172.16.0.192 │
└────────┴────────┴────────┴─────────────┴──────────────┘
```

**Barème :** 1 pt par ligne complète

---

## PARTIE 3 : ALGORITHMIQUE (7 points — 30 min)

### Exercice 3.1 : Complexité (2 points)

**Indiquez la complexité de chaque code :**

**a)** (1 pt)
```python
def fonction_a(liste):
    return liste[0]
```
Complexité : __________

**b)** (1 pt)
```python
def fonction_b(liste):
    for i in range(len(liste)):
        for j in range(len(liste)):
            print(i, j)
```
Complexité : __________

---

### Exercice 3.2 : Algorithme de Recherche (2 points)

**Complétez le code de la recherche dichotomique :**

```python
def recherche_dichotomique(liste_triee, cible):
    debut = 0
    fin = len(liste_triee) - 1
    
    while debut <= fin:
        milieu = _____________________  # (0.5 pt)
        
        if liste_triee[milieu] == cible:
            return _________________  # (0.5 pt)
        elif liste_triee[milieu] < cible:
            debut = _________________  # (0.5 pt)
        else:
            fin = ___________________  # (0.5 pt)
    
    return -1
```

---

### Exercice 3.3 : Calculs de Débit (3 points)

**Contexte :** Vous devez transférer un fichier de **1.5 Go** via un lien WAN de **50 Mbps**.

**a)** Convertissez 1.5 Go en Mo : _________________ (0.5 pt)

**b)** Convertissez 50 Mbps en Mo/s : _________________ (1 pt)

**c)** Calculez le temps de transfert en secondes : _________________ (1 pt)

**d)** Convertissez en minutes : _________________ (0.5 pt)

---

---

# ✅ CORRECTION DÉTAILLÉE

## PARTIE 1 : ALGÈBRE DE BOOLE (6 points)

### Exercice 1.1 : Table de Vérité (3 points)

```
┌───┬───┬───┬─────┬────┬──────────────┐
│ a │ b │ c │ a∨b │ ¬c │ (a∨b) ∧ ¬c  │
├───┼───┼───┼─────┼────┼──────────────┤
│ 0 │ 0 │ 0 │  0  │ 1  │      0       │
│ 0 │ 0 │ 1 │  0  │ 0  │      0       │
│ 0 │ 1 │ 0 │  1  │ 1  │      1       │
│ 0 │ 1 │ 1 │  1  │ 0  │      0       │
│ 1 │ 0 │ 0 │  1  │ 1  │      1       │
│ 1 │ 0 │ 1 │  1  │ 0  │      0       │
│ 1 │ 1 │ 0 │  1  │ 1  │      1       │
│ 1 │ 1 │ 1 │  1  │ 0  │      0       │
└───┴───┴───┴─────┴────┴──────────────┘
```

**Barème :**
- Colonne a∨b : 1 pt
- Colonne ¬c : 1 pt
- Colonne finale : 1 pt

---

### Exercice 1.2 : Simplification (3 points)

**a) (a ∧ b) ∨ (a ∧ ¬b)**

```
Étape 1 : a ∧ (b ∨ ¬b)     [Factorisation]
Étape 2 : a ∧ 1             [Tiers exclu : b ∨ ¬b = 1]
Résultat : a                [Élément neutre : a ∧ 1 = a]
```

**Barème :** 0.5 pt par étape (1.5 pts total)

---

**b) ¬(a ∨ b)**

```
Résultat : ¬a ∧ ¬b    [Loi de De Morgan]
```

**Barème :** 1.5 pts

---

## PARTIE 2 : SUBNETTING & VLSM (7 points)

### Exercice 2.1 : Conversions (2 points)

**a) 224 en binaire**

```
224 = 128 + 64 + 32
224 = 2^7 + 2^6 + 2^5
224 = 11100000
```

**Réponse : 11100000** (1 pt)

---

**b) 10101100 en décimal**

```
1×128 + 0×64 + 1×32 + 0×16 + 1×8 + 1×4 + 0×2 + 0×1
= 128 + 32 + 8 + 4
= 172
```

**Réponse : 172** (1 pt)

---

### Exercice 2.2 : Calcul de Masques (2 points)

**Site A : 80 hôtes**
```
80 + 2 = 82 adresses nécessaires
2^n ≥ 82 → 2^7 = 128
Masque : /25
```
(1 pt)

**Site B : 15 hôtes**
```
15 + 2 = 17 adresses
2^n ≥ 17 → 2^5 = 32
Masque : /27
```
(1 pt)

---

### Exercice 2.3 : Plan VLSM (3 points)

```
┌────────┬────────┬────────┬─────────────┬──────────────┐
│ Site   │ Hôtes  │ Masque │ Taille (IP) │ Réseau       │
├────────┼────────┼────────┼─────────────┼──────────────┤
│ Site 1 │  100   │  /25   │    128      │ 172.16.0.0   │
│ Site 2 │   30   │  /27   │     32      │ 172.16.0.128 │
│ Site 3 │   10   │  /28   │     16      │ 172.16.0.160 │
└────────┴────────┴────────┴─────────────┴──────────────┘
```

**Détail des calculs :**
- Site 1 : 100 + 2 = 102 → 2^7 = 128 → /25
- Site 2 : 30 + 2 = 32 → 2^5 = 32 → /27
- Site 3 : 10 + 2 = 12 → 2^4 = 16 → /28

**Adresses réseau :**
- Site 1 : 172.16.0.0 (début)
- Site 2 : 172.16.0.0 + 128 = 172.16.0.128
- Site 3 : 172.16.0.128 + 32 = 172.16.0.160

**Barème :** 1 pt par ligne (3 pts)

---

## PARTIE 3 : ALGORITHMIQUE (7 points)

### Exercice 3.1 : Complexité (2 points)

**a)** Complexité : **O(1)** (accès direct à un élément) (1 pt)

**b)** Complexité : **O(n²)** (double boucle imbriquée) (1 pt)

---

### Exercice 3.2 : Recherche Dichotomique (2 points)

```python
def recherche_dichotomique(liste_triee, cible):
    debut = 0
    fin = len(liste_triee) - 1
    
    while debut <= fin:
        milieu = (debut + fin) // 2         # 0.5 pt
        
        if liste_triee[milieu] == cible:
            return milieu                    # 0.5 pt
        elif liste_triee[milieu] < cible:
            debut = milieu + 1               # 0.5 pt
        else:
            fin = milieu - 1                 # 0.5 pt
    
    return -1
```

**Barème :** 0.5 pt par ligne complétée

---

### Exercice 3.3 : Calculs de Débit (3 points)

**a) 1.5 Go en Mo**
```
1.5 Go × 1024 = 1536 Mo
```
**Réponse : 1536 Mo** (0.5 pt)

---

**b) 50 Mbps en Mo/s**
```
50 Mbps ÷ 8 = 6.25 Mo/s
```
**Réponse : 6.25 Mo/s** (1 pt)

---

**c) Temps de transfert**
```
Temps = Taille ÷ Débit
Temps = 1536 Mo ÷ 6.25 Mo/s
Temps = 245.76 secondes
```
**Réponse : 245.76 secondes** (1 pt)

---

**d) En minutes**
```
245.76 ÷ 60 = 4.096 minutes ≈ 4 minutes
```
**Réponse : 4.1 minutes** (0.5 pt)

---

## 📊 Grille d'Évaluation Globale

| Partie | Exercice | Points | Critères |
|--------|----------|--------|----------|
| **1** | Table de vérité | /3 | Exactitude calculs |
| **1** | Simplification | /3 | Méthode + résultat |
| **2** | Conversions | /2 | Calculs binaires |
| **2** | Masques | /2 | Formule 2^n - 2 |
| **2** | Plan VLSM | /3 | Algorithme correct |
| **3** | Complexité | /2 | Identification |
| **3** | Dichotomique | /2 | Code complet |
| **3** | Débit | /3 | Formules et conversions |
| **TOTAL** | | **/20** | |

---

## 💡 Erreurs Fréquentes

**❌ Erreur 1 :** Confondre OR inclusif et exclusif
→ OR standard : 1 ∨ 1 = 1 (pas 0)

**❌ Erreur 2 :** Oublier +2 en subnetting
→ 80 hôtes = 82 adresses (pas 80)

**❌ Erreur 3 :** Mauvaise conversion bits/octets
→ 50 Mbps ÷ 8 = 6.25 Mo/s (pas 50)

**❌ Erreur 4 :** Ne pas trier en VLSM
→ Commencer par le PLUS GRAND

---

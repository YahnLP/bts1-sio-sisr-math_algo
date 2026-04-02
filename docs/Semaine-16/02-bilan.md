---
author: YLP
title: 📌 FICHE BILAN & MÉMO
---

# 📌 FICHE BILAN & MÉMO
## VLSM et Calculs de Débit : L'Essentiel à Retenir

---

## 🎯 Synthèse de la Séance

| **Élément** | **Détail** |
|-------------|-----------|
| **Thème** | Subnetting VLSM et calculs de débit |
| **Approche** | Mathématique et algorithmique |
| **Compétences** | Puissances de 2, binaire, formules, Python |
| **Durée** | 4 heures |

---

## ✅ Objectifs Atteints

- ✅ Maîtriser les puissances de 2 (2³ à 2⁸)
- ✅ Calculer un masque à partir d'un besoin
- ✅ Implémenter l'algorithme VLSM en Python
- ✅ Convertir bits ↔ octets
- ✅ Calculer temps de transfert avec formule
- ✅ Optimiser un plan d'adressage

---

## 🔑 Formules Essentielles

### Partie 1 : VLSM

| Formule | Utilité |
|---------|---------|
| **Hôtes = 2^n - 2** | Nombre d'hôtes disponibles |
| **Masque = 32 - n** | Calcul du masque CIDR |
| **Taille = 2^n** | Nombre d'adresses du sous-réseau |

### Partie 2 : Débit

| Formule | Utilité |
|---------|---------|
| **Temps = Taille ÷ Débit** | Calcul du temps de transfert |
| **Mo/s = Mbps ÷ 8** | Conversion Megabits → Megaoctets |
| **Mbps = Mo/s × 8** | Conversion Megaoctets → Megabits |

---

## 📊 Tableau des Puissances de 2

```
╔═══════════════════════════════════════════════╗
║  n │ 2^n │ Masque │ Hôtes (2^n - 2)         ║
╠═══╪═════╪════════╪═════════════════════════╣
║  3 │   8 │  /29   │   6                     ║
║  4 │  16 │  /28   │  14                     ║
║  5 │  32 │  /27   │  30                     ║
║  6 │  64 │  /26   │  62                     ║
║  7 │ 128 │  /25   │ 126                     ║
║  8 │ 256 │  /24   │ 254                     ║
╚═══════════════════════════════════════════════╝
```

**À mémoriser absolument !**

---

## 💻 Code Python à Connaître

### Calcul de Masque

```python
import math

def calculer_masque(nb_hotes):
    """Calcule le masque pour nb_hotes"""
    nb_adresses = nb_hotes + 2
    n = math.ceil(math.log2(nb_adresses))
    masque = 32 - n
    return masque

# Exemple
print(calculer_masque(50))  # /26
```

---

### Algorithme VLSM

```python
def vlsm_optimal(besoins):
    """Calcule le plan VLSM optimal"""
    # Tri décroissant
    besoins_tries = sorted(besoins, reverse=True)
    
    plan = []
    adresse = 0
    
    for nb_hotes in besoins_tries:
        masque = calculer_masque(nb_hotes)
        taille = 2 ** (32 - masque)
        
        plan.append({
            'hotes': nb_hotes,
            'masque': masque,
            'taille': taille
        })
        
        adresse += taille
    
    return plan
```

**Complexité :** O(n log n)

---

### Conversion Bits/Octets

```python
def mbps_to_mos(mbps):
    """Mbps → Mo/s"""
    return mbps / 8

def mos_to_mbps(mos):
    """Mo/s → Mbps"""
    return mos * 8
```

---

### Calcul de Temps de Transfert

```python
def calculer_temps_transfert(taille_mo, debit_mbps):
    """Calcule le temps en secondes"""
    debit_mos = debit_mbps / 8
    temps = taille_mo / debit_mos
    return temps

# Exemple
temps = calculer_temps_transfert(500, 100)
print(f"{temps:.1f} secondes")  # 40.0 secondes
```

---

## 🧠 Auto-Évaluation

| Je sais... | Maîtrisé ? |
|------------|------------|
| Calculer 2^6 de tête (64) | ☐ |
| Convertir 192 en binaire | ☐ |
| Calculer le masque pour 50 hôtes (/26) | ☐ |
| Trier une liste Python en décroissant | ☐ |
| Convertir 100 Mbps en Mo/s (12.5) | ☐ |
| Calculer : 500 Mo ÷ 10 Mo/s (50s) | ☐ |
| Implémenter VLSM en Python | ☐ |
| Expliquer pourquoi on trie en décroissant | ☐ |

**Si < 6 cases cochées, revoir la fiche cours.**

---

## 📝 Exercices Rapides

### Exercice 1 : Calcul de Masque

**Q :** 120 hôtes → quel masque ?

**R :** 120 + 2 = 122 → 2^7 = 128 → **/25**

---

### Exercice 2 : Conversion

**Q :** 50 Mbps = ? Mo/s

**R :** 50 ÷ 8 = **6.25 Mo/s**

---

### Exercice 3 : Temps de Transfert

**Q :** 1 Go à 100 Mbps = ?

**R :** 
- 1 Go = 1024 Mo
- 100 Mbps = 12.5 Mo/s
- Temps = 1024 ÷ 12.5 = **81.9 secondes**

---

## 🎯 Méthodologie VLSM

**Étapes à suivre :**

1. **Trier** les besoins par ordre **décroissant**
2. Pour chaque besoin :
   - Ajouter 2 (réseau + broadcast)
   - Trouver 2^n supérieur ou égal
   - Calculer masque : 32 - n
3. **Assigner** les adresses séquentiellement
4. **Vérifier** qu'il reste de la place

---

## 💡 Astuces et Pièges

### ✅ Astuces

**Conversion rapide Mbps → Mo/s :**
- 100 Mbps ÷ 8 = 12.5 Mo/s
- 50 Mbps ÷ 8 = 6.25 Mo/s
- 10 Mbps ÷ 8 = 1.25 Mo/s

**Puissances de 2 courantes :**
- 2^5 = 32
- 2^6 = 64
- 2^7 = 128
- 2^8 = 256

---

### ❌ Pièges à Éviter

**Piège 1 :** Oublier +2
→ 50 hôtes = 52 adresses (pas 50)

**Piège 2 :** Confondre bits et octets
→ 100 Mbps ≠ 100 Mo/s

**Piège 3 :** Ne pas trier
→ Le grand ne rentre plus si on commence par les petits

**Piège 4 :** Arrondir mal
→ 50 → 2^6 = 64 (pas 2^5 = 32, trop petit)

---

## 🔄 Lien avec les Autres Séances

| Séance | Lien |
|--------|------|
| **S1-S5** | Variables, boucles, fonctions → utilisées dans les algos |
| **S8** | Dictionnaires → stocker le plan d'adressage |
| **S15** | Complexité → O(n log n) du tri VLSM |

---

## 📚 Pour Aller Plus Loin

**Concepts avancés :**
- **Agrégation de routes** (route summarization)
- **Subnetting IPv6** (préfixes /48, /64)
- **CIDR** (Classless Inter-Domain Routing)
- **Overhead TCP/IP** (calcul des headers)

**Outils pratiques :**
- Calculateur VLSM : [vlsm-calc.net](https://www.vlsm-calc.net/)
- Convertisseur binaire : `bin()` en Python
- Test débit : [speedtest.net](https://www.speedtest.net/)

---

## 🎓 Compétences Acquises

**Mathématiques :**
- ✅ Puissances de 2
- ✅ Binaire
- ✅ Formules de proportionnalité
- ✅ Conversions d'unités

**Algorithmique :**
- ✅ Algorithme glouton
- ✅ Tri et optimisation
- ✅ Complexité O(n log n)
- ✅ Programmation Python

**Pratiques :**
- ✅ Dimensionnement réseau
- ✅ Optimisation des ressources
- ✅ Calculs de performance

---

## 💬 Citation à Retenir

> *"Un bon plan d'adressage, c'est comme un bon algorithme : il optimise les ressources et évite le gaspillage."*

---

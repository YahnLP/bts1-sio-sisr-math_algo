---
author: YLP
title: 📖 Fiche de Cours
---

# 📖 FICHE DE COURS
## S16 — Subnetting VLSM et Calculs de Débit : Approche Mathématique et Algorithmique

*BTS SIO SISR — Année 1 — Semaine 16*

---

## 🎯 Objectifs

✅ Maîtriser les puissances de 2 et le binaire  
✅ Calculer des masques de sous-réseau  
✅ Implémenter l'algorithme VLSM en Python  
✅ Utiliser les formules de débit  
✅ Convertir bits ↔ octets et Ko/Mo/Go

---

## 📚 Partie 1 : Mathématiques du Subnetting VLSM

### 1.1 Les Puissances de 2

**Tableau à mémoriser :**

| n | 2^n | Masque | Hôtes disponibles |
|---|-----|--------|-------------------|
| 3 | 8 | /29 | 6 |
| 4 | 16 | /28 | 14 |
| 5 | 32 | /27 | 30 |
| 6 | 64 | /26 | 62 |
| 7 | 128 | /25 | 126 |
| 8 | 256 | /24 | 254 |

**Formule :** Hôtes = 2^n - 2 (réseau et broadcast exclus)

---

### 1.2 Calcul de Masque

**Problème :** J'ai besoin de 50 hôtes. Quel masque choisir ?

**Méthode :**
1. Ajouter 2 pour réseau + broadcast : 50 + 2 = 52
2. Trouver 2^n ≥ 52 : 2^6 = 64 ✅
3. Masque : /26

**En Python :**
```python
import math

def calculer_masque(nb_hotes):
    """Calcule le masque pour un nombre d'hôtes"""
    nb_adresses = nb_hotes + 2  # +2 pour réseau et broadcast
    n = math.ceil(math.log2(nb_adresses))  # Arrondi supérieur
    masque = 32 - n
    return masque

# Exemple
print(calculer_masque(50))  # Retourne 26 (/26)
```

---

### 1.3 L'Algorithme VLSM

**Problème d'optimisation :** Répartir une plage IP pour minimiser le gaspillage.

**Algorithme (glouton) :**

```python
def vlsm_optimal(besoins):
    """
    Calcule le plan VLSM optimal
    besoins : liste des nombres d'hôtes par site
    """
    # Étape 1 : Trier par ordre décroissant
    besoins_tries = sorted(besoins, reverse=True)
    
    plan = []
    adresse_actuelle = 0
    
    # Étape 2 : Pour chaque besoin
    for nb_hotes in besoins_tries:
        # Calculer le masque
        masque = calculer_masque(nb_hotes)
        taille = 2 ** (32 - masque)
        
        # Assigner
        plan.append({
            'hotes': nb_hotes,
            'masque': masque,
            'taille': taille,
            'adresse': adresse_actuelle
        })
        
        # Passer au suivant
        adresse_actuelle += taille
    
    return plan

# Exemple
besoins = [100, 30, 10, 5]
plan = vlsm_optimal(besoins)
for sous_reseau in plan:
    print(f"{sous_reseau['hotes']} hôtes → /{sous_reseau['masque']} ({sous_reseau['taille']} adresses)")
```

**Complexité :** O(n log n) à cause du tri

---

### 1.4 Conversion Décimal ↔ Binaire

**Décimal → Binaire :**
```python
decimal = 192
binaire = bin(decimal)[2:]  # [2:] pour enlever '0b'
print(binaire)  # '11000000'
```

**Binaire → Décimal :**
```python
binaire = '11000000'
decimal = int(binaire, 2)
print(decimal)  # 192
```

---

## 📚 Partie 2 : Mathématiques du Débit

### 2.1 Formule Fondamentale

```
Temps (secondes) = Taille (octets) ÷ Débit (octets/s)
```

**Exemple :**
- Fichier : 500 Mo
- Débit : 12.5 Mo/s
- Temps : 500 ÷ 12.5 = 40 secondes

---

### 2.2 Conversion Bits ↔ Octets

**Règle :** 1 octet = 8 bits

**Formules :**
- Mbps → Mo/s : **÷ 8**
- Mo/s → Mbps : **× 8**

**Exemples :**
- 100 Mbps = 100 ÷ 8 = 12.5 Mo/s
- 10 Mo/s = 10 × 8 = 80 Mbps

**En Python :**
```python
def mbps_to_mos(mbps):
    """Convertit Mbps en Mo/s"""
    return mbps / 8

def mos_to_mbps(mos):
    """Convertit Mo/s en Mbps"""
    return mos * 8

print(mbps_to_mos(100))  # 12.5 Mo/s
```

---

### 2.3 Conversions d'Unités

| Unité | Valeur |
|-------|--------|
| 1 Ko | 1 024 octets |
| 1 Mo | 1 024 Ko = 1 048 576 octets |
| 1 Go | 1 024 Mo |
| 1 To | 1 024 Go |

**En Python :**
```python
def convertir_en_mo(taille, unite):
    """Convertit une taille en Mo"""
    facteurs = {
        'o': 1 / (1024 ** 2),
        'Ko': 1 / 1024,
        'Mo': 1,
        'Go': 1024,
        'To': 1024 ** 2
    }
    return taille * facteurs[unite]

# Exemple
print(convertir_en_mo(2, 'Go'))  # 2048 Mo
```

---

### 2.4 Calcul du Temps de Transfert

**Fonction complète :**

```python
def calculer_temps_transfert(taille_mo, debit_mbps):
    """
    Calcule le temps de transfert
    taille_mo : taille du fichier en Mo
    debit_mbps : débit en Mbps
    Retourne : temps en secondes
    """
    # Conversion Mbps → Mo/s
    debit_mos = debit_mbps / 8
    
    # Calcul du temps
    temps_secondes = taille_mo / debit_mos
    
    return temps_secondes

# Exemple
fichier = 500  # Mo
lien = 100  # Mbps
temps = calculer_temps_transfert(fichier, lien)
print(f"Temps : {temps:.1f} secondes = {temps/60:.1f} minutes")
```

---

### 2.5 Impact de la Latence

**Latence** = Temps incompressible pour qu'un paquet fasse l'aller-retour (RTT)

**Formule avec latence :**
```
Temps total = Temps transfert + Latence
```

**En Python :**
```python
def calculer_temps_total(taille_mo, debit_mbps, latence_ms):
    """Calcule le temps total avec latence"""
    temps_transfert = calculer_temps_transfert(taille_mo, debit_mbps)
    latence_s = latence_ms / 1000  # Convertir ms en s
    return temps_transfert + latence_s

# Exemple
temps = calculer_temps_total(500, 100, 50)
print(f"Temps total : {temps:.1f}s")
```

**Note :** Pour les gros fichiers, la latence est négligeable. Pour les petits paquets (VoIP, gaming), elle est critique.

---

## 📝 Exercices d'Entraînement

### Exercice 1 : Calcul de Masque

**Données :** 80 hôtes nécessaires

**Questions :**
1. Combien d'adresses au total ? (80 + 2 = 82)
2. Quelle puissance de 2 ? (2^7 = 128)
3. Quel masque ? (/25)

---

### Exercice 2 : VLSM

**Données :** 192.168.0.0/24 à découper pour 3 sites : 50, 20, 10 hôtes

**Algorithme :**
1. Trier : [50, 20, 10]
2. Calculer masques : /26, /27, /28
3. Assigner : 192.168.0.0/26, 192.168.0.64/27, 192.168.0.96/28

---

### Exercice 3 : Calcul de Débit

**Données :**
- Fichier : 1 Go
- Lien : 50 Mbps

**Calculs :**
1. Conversion : 1 Go = 1024 Mo
2. Débit : 50 Mbps ÷ 8 = 6.25 Mo/s
3. Temps : 1024 ÷ 6.25 = 163.8 secondes ≈ 2.7 minutes

---

## 🎯 Récapitulatif

**Formules à retenir :**

| Formule | Utilité |
|---------|---------|
| Hôtes = 2^n - 2 | Nombre d'hôtes disponibles |
| Masque = 32 - n | Calcul du masque CIDR |
| Temps = Taille ÷ Débit | Temps de transfert |
| Mo/s = Mbps ÷ 8 | Conversion bits → octets |

**Algorithme VLSM :**
1. Trier (décroissant)
2. Pour chaque besoin : trouver 2^n supérieur
3. Assigner les adresses séquentiellement

---

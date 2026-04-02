---
author: YLP
title: 📌 FICHE BILAN & MÉMO

---

# 📌 FICHE BILAN & MÉMO
## Révisions Générales : Aide-Mémoire pour l'Examen

---

## 🎯 Les 3 Blocs Essentiels

Cette fiche synthétise **l'essentiel absolu** à retenir pour l'examen.

---

## 📊 BLOC 1 : ALGÈBRE DE BOOLE

### Opérateurs en un Coup d'Œil

```
╔═══════════════════════════════════════════╗
║ AND (∧) : 1 si les DEUX vrais           ║
║ OR (∨)  : 1 si AU MOINS UN vrai         ║
║ NOT (¬) : Inverse                         ║
║ XOR (⊕) : 1 si DIFFÉRENTS                ║
╚═══════════════════════════════════════════╝
```

### Lois de De Morgan (à mémoriser)

```
¬(a ∧ b) = ¬a ∨ ¬b
¬(a ∨ b) = ¬a ∧ ¬b
```

### Simplifications Courantes

```
a ∧ a = a
a ∨ a = a
a ∧ 1 = a
a ∨ 0 = a
a ∧ 0 = 0
a ∨ 1 = 1
a ∧ ¬a = 0  ← Important !
a ∨ ¬a = 1  ← Important !
```

---

## 📊 BLOC 2 : SUBNETTING & VLSM

### Puissances de 2 (à connaître PAR CŒUR)

```
╔═══════════════════════════════════════╗
║  2³ =   8  →  /29  →   6 hôtes      ║
║  2⁴ =  16  →  /28  →  14 hôtes      ║
║  2⁵ =  32  →  /27  →  30 hôtes      ║
║  2⁶ =  64  →  /26  →  62 hôtes      ║
║  2⁷ = 128  →  /25  → 126 hôtes      ║
║  2⁸ = 256  →  /24  → 254 hôtes      ║
╚═══════════════════════════════════════╝
```

### Formules Essentielles

```
┌────────────────────────────────────────┐
│ Hôtes = 2^n - 2                        │
│ Masque = 32 - n                        │
│ Taille = 2^n                           │
└────────────────────────────────────────┘
```

### Méthode VLSM (3 étapes)

```
1. TRIER décroissant
2. CALCULER masques (2^n ≥ besoins + 2)
3. ASSIGNER séquentiellement
```

---

## 📊 BLOC 3 : ALGORITHMIQUE

### Complexités

```
╔═══════════════════════════════════════╗
║ O(1)      → Constant                 ║
║ O(log n)  → Dichotomique             ║
║ O(n)      → Linéaire                 ║
║ O(n²)     → Double boucle            ║
╚═══════════════════════════════════════╝
```

### Formule de Débit

```
┌────────────────────────────────────────┐
│ Temps = Taille ÷ Débit                 │
│                                        │
│ CONVERSION CRITIQUE :                  │
│ Mbps ÷ 8 = Mo/s                        │
└────────────────────────────────────────┘
```

### Code Minimal à Connaître

**Recherche Linéaire :**
```python
for i, element in enumerate(liste):
    if element == cible:
        return i
return -1
```

**Recherche Dichotomique :**
```python
debut, fin = 0, len(liste) - 1
while debut <= fin:
    milieu = (debut + fin) // 2
    if liste[milieu] == cible:
        return milieu
    elif liste[milieu] < cible:
        debut = milieu + 1
    else:
        fin = milieu - 1
```

---

## 🔥 Top 10 des Erreurs à Éviter

| # | Erreur | Solution |
|---|--------|----------|
| **1** | Confondre 1 ∨ 1 = 0 | OR inclusif : 1 ∨ 1 = **1** |
| **2** | Oublier +2 en subnetting | 50 hôtes = **52** adresses |
| **3** | Mbps = Mo/s | 100 Mbps = **12.5** Mo/s (÷8) |
| **4** | 2⁶ = 32 | 2⁶ = **64** |
| **5** | Ne pas trier en VLSM | Toujours **décroissant** |
| **6** | O(n) pour double boucle | Double boucle = **O(n²)** |
| **7** | Dichotomique sans tri | Nécessite liste **TRIÉE** |
| **8** | De Morgan mal appliqué | ¬(a ∧ b) = **¬a ∨ ¬b** |
| **9** | Masque = n | Masque = **32 - n** |
| **10** | Arrondir au plus proche | Toujours **supérieur** (ceil) |

---

## 📝 Checklist Finale

### La Veille de l'Examen

- ☐ Relire les 3 blocs de cette fiche
- ☐ Refaire l'examen blanc en 85 min
- ☐ Vérifier qu'on connaît les puissances de 2
- ☐ Préparer sa fiche mémo A4 recto
- ☐ Préparer calculatrice + stylos
- ☐ Dormir 8 heures minimum

### Le Jour J

- ☐ Arriver 10 min en avance
- ☐ Lire TOUT le sujet (5 min)
- ☐ Commencer par ce qu'on maîtrise
- ☐ Gérer son temps (25-30-30 min)
- ☐ Vérifier les unités
- ☐ Relire avant de rendre

---

## 🎯 Stratégie Pendant l'Examen

### Gestion du Temps (85 min)

```
┌───────────────────────────────────────┐
│ Lecture sujet        :  5 min         │
│ Algèbre de Boole    : 25 min         │
│ Subnetting VLSM     : 30 min         │
│ Algorithmique       : 30 min         │
│ Relecture           :  5 min         │
└───────────────────────────────────────┘
```

### Si Bloqué

1. **Passer** à la question suivante
2. **Revenir** à la fin si temps restant
3. **Écrire** ce qu'on sait (points partiels)
4. **Ne jamais** laisser blanc

---

## 💡 Astuces de Dernière Minute

### Conversions Rapides

**Binaire → Décimal :**
```
128  64  32  16   8   4   2   1
 1   1   0   0   0   0   0   0  = 192
```

**Mbps → Mo/s :**
```
100 Mbps ÷ 8 = 12.5 Mo/s
 50 Mbps ÷ 8 =  6.25 Mo/s
 10 Mbps ÷ 8 =  1.25 Mo/s
```

---

### Vérifications Rapides

**Algèbre de Boole :**
- Table de vérité : 2^n lignes (n variables)
- Vérifier avec a=0, b=0, c=0 d'abord

**Subnetting :**
- Vérifier : hôtes < 2^n - 2
- Vérifier : total < plage disponible

**Algorithmique :**
- 1 boucle = O(n)
- 2 boucles imbriquées = O(n²)
- Vérifier : unités cohérentes

---

## 🏆 Le Mot de la Fin

**Vous avez travaillé 19 semaines pour arriver ici.**

**Vous CONNAISSEZ ces concepts :**
- Tables de vérité
- Puissances de 2
- Complexités
- Formules de débit

**L'examen teste votre MAÎTRISE, pas votre mémoire.**

### Les 3 Clés du Succès

1. **CALME** : Respirer, ne pas paniquer
2. **MÉTHODE** : Suivre les étapes
3. **TEMPS** : Gérer les 85 minutes

---

## 📚 Dernières Ressources

**Si temps restant avant l'examen :**
- Refaire S2, S13, S15, S16
- Refaire l'examen blanc
- Créer des flashcards
- Enseigner à un camarade (meilleure révision)

---

## ✉️ Message de l'Enseignant

*"Vous êtes prêts. Faites confiance à votre préparation. L'examen évalue ce que vous savez, pas ce que vous ne savez pas. Montrez ce que vous avez appris depuis septembre. Bonne chance !"*

---

## 🎯 Points Clés (à relire 5 min avant l'examen)

```
╔════════════════════════════════════════════╗
║ 1. De Morgan : ¬(a ∧ b) = ¬a ∨ ¬b          ║
║ 2. Hôtes = 2^n - 2                         ║
║ 3. Masque = 32 - n                         ║
║ 4. VLSM : Trier décroissant                ║
║ 5. Mbps ÷ 8 = Mo/s                         ║
║ 6. Temps = Taille ÷ Débit                  ║
║ 7. O(n) = 1 boucle, O(n²) = 2 boucles      ║
║ 8. Dichotomique = liste TRIÉE              ║
╚════════════════════════════════════════════╝
```

---

**Vous allez réussir. On croit en vous. 💪**

---
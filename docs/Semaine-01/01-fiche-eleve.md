---
author: YLP
title: 📖 FICHE DE COURS ÉLÈVE
---

## 📖 FICHE DE COURS ÉLÈVE
### Systèmes de Numération · Binaire · Décimal · Hexadécimal · Conversions · Adresses MAC & IP

*Version 1.0 — BTS SIO SISR — Année 1 — Semaine 1*

---

## Partie 1 — Pourquoi le Binaire ?

### 1.1 Le Transistor : La Brique de Base

Un ordinateur moderne contient des **milliards de transistors**. Un transistor est un interrupteur électronique microscopique qui n'a que **deux états possibles** :

```
┌─────────────────────────────────────────────────────────┐
│                   LE TRANSISTOR                         │
│                                                         │
│   ÉTAT 0 : interrupteur OUVERT                          │
│   ───────○   ○───────  → pas de courant → valeur 0     │
│                                                         │
│   ÉTAT 1 : interrupteur FERMÉ                           │
│   ─────────────────────  → courant passe → valeur 1    │
│                                                         │
│   Un transistor ne peut PAS être "à moitié ouvert".     │
│   → Il ne connaît que 0 et 1.                           │
│   → L'ordinateur ne peut compter qu'en binaire.         │
└─────────────────────────────────────────────────────────┘
```
*[Illustration : Deux schémas côte à côte. À gauche, un transistor "ouvert" avec un X au milieu du fil électrique et la valeur 0. À droite, un transistor "fermé" avec le fil continu et la valeur 1. Sous les deux schémas, une légende : "Tout ce que fait un ordinateur repose sur des milliards de ces interrupteurs."]*

> 💡 **À retenir :** Le binaire n'est pas un choix arbitraire — c'est une **contrainte physique**. Un transistor ne peut représenter que deux états. On appelle cet état un **bit** (contraction de *binary digit*).

### 1.2 Vocabulaire Fondamental

| **Terme** | **Définition** | **Exemple** |
|---|---|---|
| **Bit** | Plus petite unité d'information — vaut 0 ou 1 | `1` |
| **Nibble** | Groupe de 4 bits | `1010` |
| **Octet (byte)** | Groupe de 8 bits | `11001010` |
| **MSB** | *Most Significant Bit* — bit de poids **fort** (à gauche) | Dans `11001010`, le MSB est `1` |
| **LSB** | *Least Significant Bit* — bit de poids **faible** (à droite) | Dans `11001010`, le LSB est `0` |

```
           MSB                              LSB
            ↓                               ↓
            1   1   0   0   1   0   1   0
            │                               │
         poids fort                    poids faible
         (valeur élevée)              (valeur faible)

  Convention de lecture : TOUJOURS de GAUCHE (MSB) à DROITE (LSB)
```
*[Illustration : Une suite de 8 bits avec flèches et annotations indiquant MSB à gauche, LSB à droite, et une flèche "sens de lecture" de gauche à droite au-dessus de la suite.]*

---

## Partie 2 — La Logique des Bases de Numération

### 2.1 La Base Décimale (Base 10) — Ce que vous connaissez déjà

En base 10, nous utilisons **10 symboles** : `0 1 2 3 4 5 6 7 8 9`

Chaque position dans un nombre représente une **puissance de 10** :

```
   Nombre :        3      4      7
                   │      │      │
   Position :    centaines dizaines unités
   Puissance :    10²    10¹    10⁰
   Valeur :       100     10      1

   → 347 = 3×100 + 4×10 + 7×1 = 300 + 40 + 7 = 347 ✓
```

### 2.2 La Base Binaire (Base 2) — La langue de l'ordinateur

En base 2, nous utilisons **2 symboles** : `0` et `1`

Chaque position représente une **puissance de 2** :

```
┌────────────────────────────────────────────────────────────────┐
│              TABLE DES PUISSANCES DE 2 — À MÉMORISER           │
├────────┬────────┬────────┬────────┬────────┬────────┬────────┬────────┤
│  2⁷   │  2⁶   │  2⁵   │  2⁴   │  2³   │  2²   │  2¹   │  2⁰  │
│  128  │   64  │   32  │   16  │    8  │    4  │    2  │    1  │
└────────┴────────┴────────┴────────┴────────┴────────┴────────┴────────┘
```
*[Illustration : Tableau à 8 colonnes sur fond coloré (par exemple dégradé du vert foncé pour 2⁷ au vert clair pour 2⁰). Chaque colonne affiche en haut la puissance (2⁷), au milieu la valeur (128), et en bas un emplacement vide pour écrire le bit (0 ou 1). Ce tableau servira de grille de conversion.]*

**Exemple — Lire le nombre binaire 10110011 :**

```
  Bits  :    1      0      1      1      0      0      1      1
  Poids :   128    64     32     16      8      4      2      1
  Calcul:  1×128  0×64  1×32  1×16   0×8   0×4   1×2   1×1
         =  128  +  0  +  32  +  16  +  0  +  0  +  2  +  1
         =  179 (en décimal)
```

---

## Partie 3 — Conversions Pas à Pas

### 3.1 Décimal → Binaire : Méthode des Divisions Successives

**Principe :** On divise le nombre décimal par 2 en notant les restes. On lit les restes **de bas en haut**.

**Exemple — Convertir 42 en binaire :**

```
  42 ÷ 2 = 21   reste  0   ↑ (lire de bas en haut)
  21 ÷ 2 = 10   reste  1   ↑
  10 ÷ 2 =  5   reste  0   ↑
   5 ÷ 2 =  2   reste  1   ↑
   2 ÷ 2 =  1   reste  0   ↑
   1 ÷ 2 =  0   reste  1   ↑  ← premier reste lu (MSB)

  Résultat (lecture de bas en haut) : 101010
  → 42 en décimal = 101010 en binaire
```

**Vérification :** `1×32 + 0×16 + 1×8 + 0×4 + 1×2 + 0×1 = 32 + 8 + 2 = 42` ✓

> 💡 **Astuce :** On peut aussi utiliser la **méthode des puissances** (soustraction successive) :
> - Quel est le plus grand 2ⁿ ≤ 42 ? → 32 (2⁵). On pose un 1 en position 5.
> - Reste : 42 - 32 = 10. Plus grand 2ⁿ ≤ 10 ? → 8 (2³). On pose un 1 en position 3.
> - Reste : 10 - 8 = 2. Plus grand 2ⁿ ≤ 2 ? → 2 (2¹). On pose un 1 en position 1.
> - Reste : 2 - 2 = 0. Terminé.
> - Résultat : position 5=1, 4=0, 3=1, 2=0, 1=1, 0=0 → **101010** ✓

---

### 3.2 Binaire → Décimal : Méthode des Puissances de 2

**Principe :** Multiplier chaque bit par son poids (puissance de 2) et additionner.

**Exemple — Convertir 11010110 en décimal :**

```
  Bits  :    1      1      0      1      0      1      1      0
  Poids :   128    64     32     16      8      4      2      1

  Calcul : 1×128 + 1×64 + 0×32 + 1×16 + 0×8 + 1×4 + 1×2 + 0×1
         =  128  +  64  +   0  +  16  +  0  +  4  +  2  +  0
         =  214

  → 11010110 en binaire = 214 en décimal
```

---

### 3.3 La Base Hexadécimale (Base 16) — Le Raccourci du Binaire

En base 16, on utilise **16 symboles** : `0 1 2 3 4 5 6 7 8 9 A B C D E F`

```
┌─────────────────────────────────────────────────────────────────────┐
│                     TABLE HEXADÉCIMALE COMPLÈTE                     │
├──────────┬────────────┬──────────┬──────────┬────────────┬──────────┤
│  Décimal │   Binaire  │   Hexa   │ Décimal  │   Binaire  │   Hexa   │
├──────────┼────────────┼──────────┼──────────┼────────────┼──────────┤
│    0     │   0000     │    0     │    8     │   1000     │    8     │
│    1     │   0001     │    1     │    9     │   1001     │    9     │
│    2     │   0010     │    2     │   10     │   1010     │    A     │
│    3     │   0011     │    3     │   11     │   1011     │    B     │
│    4     │   0100     │    4     │   12     │   1100     │    C     │
│    5     │   0101     │    5     │   13     │   1101     │    D     │
│    6     │   0110     │    6     │   14     │   1110     │    E     │
│    7     │   0111     │    7     │   15     │   1111     │    F     │
└──────────┴────────────┴──────────┴──────────┴────────────┴──────────┘
```
*[Illustration : Tableau à deux blocs de 8 lignes sur fond gris clair, avec la colonne "Hexa" mise en évidence. Les lettres A à F sont surlignées d'une couleur distincte pour souligner leur caractère "chiffres déguisés en lettres".]*

> 💡 **Pourquoi l'hexadécimal ?** 4 bits = exactement 1 chiffre hexadécimal. 8 bits (1 octet) = exactement 2 chiffres hexadécimaux. Au lieu d'écrire `11001010`, on écrit `CA`. **L'hexadécimal n'existe que pour rendre le binaire lisible par l'humain.**

---

### 3.4 Binaire → Hexadécimal : Méthode des Groupes de 4 Bits

**Principe :** Regrouper les bits **par 4 en partant de la droite**. Convertir chaque groupe en son équivalent hexadécimal.

**Exemple — Convertir 11001010 en hexadécimal :**

```
  Binaire :   1100    1010
               ↓       ↓
  Table   :    C       A
               ↓       ↓
  Résultat:   0xCA

  → 11001010 en binaire = CA en hexadécimal (noté 0xCA)
```

**Vérification :** `CA` → `C=12, A=10` → `12×16 + 10×1 = 192 + 10 = 202`
Et en binaire : `1×128 + 1×64 + 0×32 + 0×16 + 1×8 + 0×4 + 1×2 + 0×1 = 128+64+8+2 = 202` ✓

---

### 3.5 Hexadécimal → Binaire : L'Opération Inverse

**Principe :** Remplacer chaque chiffre hexadécimal par son équivalent sur **4 bits**.

**Exemple — Convertir 0x3F en binaire :**

```
  Hexa  :    3       F
              ↓       ↓
  Binaire:  0011    1111
              ↓       ↓
  Résultat: 00111111

  → 0x3F en hexadécimal = 00111111 en binaire
```

---

### 3.6 Décimal → Hexadécimal : Deux Chemins Possibles

**Chemin 1 (recommandé) :** Décimal → Binaire → Hexadécimal (enchaîner les méthodes 3.1 et 3.4)

**Chemin 2 (direct) :** Divisions successives par 16 — même logique que pour le binaire.

**Exemple — Convertir 202 en hexadécimal par divisions :**

```
  202 ÷ 16 = 12   reste  10  → 10 = A
   12 ÷ 16 =  0   reste  12  → 12 = C

  Lecture de bas en haut : C A
  → 202 en décimal = 0xCA en hexadécimal ✓
```

---

## Partie 4 — Exercices Guidés

### Série 1 — Décimal → Binaire *(avec correction immédiate)*

Utilisez la méthode des divisions successives :

| **Nombre décimal** | **Divisions (à compléter)** | **Résultat binaire** |
|---|---|---|
| 13 | 13÷2=6 r.**1** / 6÷2=3 r.**0** / 3÷2=1 r.**1** / 1÷2=0 r.**1** | **1101** |
| 25 | *(à compléter)* | *(à trouver)* |
| 47 | *(à compléter)* | *(à trouver)* |
| 100 | *(à compléter)* | *(à trouver)* |
| 172 | *(à compléter)* | *(à trouver)* |
| 255 | *(à compléter)* | *(à trouver — résultat remarquable !)* |

### Série 2 — Binaire → Décimal

Utilisez la table des puissances de 2 :

| **Nombre binaire** | **Calcul (à compléter)** | **Résultat décimal** |
|---|---|---|
| `1011` | `1×8 + 0×4 + 1×2 + 1×1 =` | **11** |
| `10101` | *(à compléter)* | *(à trouver)* |
| `11111111` | *(à compléter)* | *(résultat remarquable !)* |
| `10000000` | *(à compléter)* | *(à trouver)* |
| `11010011` | *(à compléter)* | *(à trouver)* |

### Série 3 — Conversions Hexadécimales

| **Départ** | **Vers** | **Résultat** |
|---|---|---|
| `0xA` | Décimal | **10** |
| `0xFF` | Décimal | *(à trouver — résultat remarquable !)* |
| `0x1F` | Binaire | *(à trouver)* |
| `11110000` | Hexadécimal | *(à trouver)* |
| `10101100` | Hexadécimal | *(à trouver)* |
| `0xC0` | Décimal | *(à trouver — on le reverra dans les masques réseau !)* |

---

## Partie 5 — Applications Réelles en Informatique

### 5.1 L'Adresse MAC en Hexadécimal

Une **adresse MAC** (Media Access Control) est l'identifiant unique gravé dans chaque carte réseau au moment de sa fabrication. Elle est composée de **6 octets**, soit **48 bits**, représentés en hexadécimal.

```
┌─────────────────────────────────────────────────────────────────────┐
│              ANATOMIE D'UNE ADRESSE MAC                             │
│                                                                     │
│        B4  :  2E  :  99  :  A0  :  1C  :  F7                      │
│        ─────────────────    ─────────────────                      │
│              OUI                    NIC                             │
│    (Organizationally        (Network Interface                      │
│     Unique Identifier)        Controller)                           │
│                                                                     │
│  3 premiers octets = Identifiant du FABRICANT                       │
│  3 derniers octets = Numéro de série de la CARTE                    │
└─────────────────────────────────────────────────────────────────────┘
```
*[Illustration : Une adresse MAC avec un encadré de couleur bleue sur les 3 premiers octets (OUI/fabricant) et un encadré vert sur les 3 derniers (NIC/numéro de carte). Sous chaque octet hexa, sa valeur en binaire sur 8 bits. En bas, une barre montrant "48 bits au total".]*

**Notation :** Une adresse MAC peut s'écrire de plusieurs façons équivalentes :
- `B4:2E:99:A0:1C:F7` (Linux, Wireshark)
- `B4-2E-99-A0-1C-F7` (Windows)
- `B42E.99A0.1CF7` (Cisco)
- `0xB42E99A01CF7` (notation hexadécimale brute)

**Exercice :** Combien y a-t-il d'adresses MAC différentes possibles ?
```
  6 octets = 48 bits → 2⁴⁸ adresses possibles
  = 281 474 976 710 656 adresses (281 billions)
  → Assez pour équiper tous les appareils jamais fabriqués
```

**Commandes pour afficher l'adresse MAC :**
```bash
# Windows
ipconfig /all
getmac

# Linux
ip link show
ip a
```

---

### 5.2 L'Adresse IP en Binaire

Une **adresse IPv4** est composée de **4 octets** (32 bits au total), affichée en notation décimale pointée.

```
┌─────────────────────────────────────────────────────────────────────┐
│              ADRESSE IP 192.168.1.42 EN BINAIRE                     │
│                                                                     │
│  Décimal :   192      .    168      .      1      .     42          │
│               │             │              │            │           │
│  Binaire :  11000000    10101000       00000001     00101010        │
│                                                                     │
│  Représentation 32 bits complète :                                  │
│  11000000 10101000 00000001 00101010                                │
│                                                                     │
│  → Chaque octet ne peut valoir qu'entre 0 et 255                    │
│    (car 8 bits → valeur max = 11111111 = 255)                       │
└─────────────────────────────────────────────────────────────────────┘
```
*[Illustration : Les 4 octets de l'IP alignés, avec sous chaque nombre décimal sa représentation binaire sur 8 bits. Une barre de 32 cases en bas représente tous les bits assemblés. Couleurs alternées par octet pour la lisibilité.]*

**Pourquoi le binaire pour les IP ?**

Les **masques de sous-réseau** ne fonctionnent qu'en binaire. Le masque `255.255.255.0` signifie en réalité :

```
  Masque  : 255      .  255      .  255      .    0
  Binaire : 11111111    11111111    11111111    00000000

  Les bits à 1 = partie RÉSEAU (fixe, identifie le réseau)
  Les bits à 0 = partie HÔTE (variable, identifie la machine)

  IP      : 11000000    10101000    00000001    00101010
  Masque  : 11111111    11111111    11111111    00000000
            ────────────────────────────────────────────
  Réseau  : 11000000    10101000    00000001    00000000
          = 192.168.1.0   (adresse réseau)
```

> 💡 **À retenir :** Une adresse IP `255.x.x.x` est impossible sur l'octet hôte car 255 en binaire = 11111111 → tous les bits à 1 → adresse de broadcast (diffusion), pas d'une machine individuelle.

---

## Partie 6 — Synthèse des Conversions

```
┌─────────────────────────────────────────────────────────────────────┐
│                  SCHÉMA DES CONVERSIONS                             │
│                                                                     │
│                    DÉCIMAL (base 10)                                │
│                    /             \                                  │
│         divisions /               \ puissances                     │
│          par 2   /                 \ de 2                          │
│                 ↙                   ↘                              │
│           BINAIRE (base 2)  ←────→  HEXADÉCIMAL (base 16)          │
│                              groupes              remplacement     │
│                              de 4 bits            nibble par nibble│
└─────────────────────────────────────────────────────────────────────┘
```
*[Illustration : Triangle avec DÉCIMAL au sommet, BINAIRE en bas à gauche, HEXADÉCIMAL en bas à droite. Les flèches entre les sommets indiquent la méthode : "divisions successives / puissances de 2" entre décimal et binaire ; "groupes de 4 bits" entre binaire et hexadécimal ; "passage par le binaire" entre décimal et hexadécimal. Chaque chemin est coloré différemment.]*

---

## Vocabulaire Clé à Maîtriser pour l'Examen

| **Terme** | **Définition** |
|---|---|
| **Bit** | Plus petite unité d'information — vaut 0 ou 1 |
| **Octet (byte)** | Groupe de 8 bits — représente une valeur de 0 à 255 |
| **Nibble** | Groupe de 4 bits — représente une valeur de 0 à 15 (0 à F en hexa) |
| **Base** | Nombre de symboles utilisés dans un système de numération |
| **Binaire** | Base 2 — symboles : 0 et 1 |
| **Hexadécimal** | Base 16 — symboles : 0-9 et A-F |
| **MSB** | Most Significant Bit — bit de poids fort (à gauche) |
| **LSB** | Least Significant Bit — bit de poids faible (à droite) |
| **Notation 0x** | Préfixe indiquant qu'un nombre est en hexadécimal (ex : 0xFF) |
| **Adresse MAC** | Identifiant physique unique d'une carte réseau — 48 bits en hexadécimal |
| **Adresse IPv4** | Adresse réseau sur 32 bits — affichée en 4 octets décimaux |
| **Masque de sous-réseau** | Nombre binaire 32 bits délimitant la partie réseau et la partie hôte d'une IP |

---

## ANNEXE A — Table des Puissances de 2

```
╔══════╦═════════╗  ╔══════╦═════════╗  ╔══════╦═════════╗
║  2ⁿ  ║ Valeur  ║  ║  2ⁿ  ║ Valeur  ║  ║  2ⁿ  ║ Valeur  ║
╠══════╬═════════╣  ╠══════╬═════════╣  ╠══════╬═════════╣
║  2⁰  ║    1    ║  ║  2⁴  ║   16    ║  ║  2⁸  ║   256   ║
║  2¹  ║    2    ║  ║  2⁵  ║   32    ║  ║  2⁹  ║   512   ║
║  2²  ║    4    ║  ║  2⁶  ║   64    ║  ║  2¹⁰ ║  1024   ║
║  2³  ║    8    ║  ║  2⁷  ║  128    ║  ║  2¹⁶ ║  65536  ║
╚══════╩═════════╝  ╚══════╩═════════╝  ╚══════╩═════════╝
```

> 💡 **À savoir absolument :** 2¹⁰ = 1024 ≈ 1000 → c'est pourquoi 1 Ko = 1024 octets et non 1000.

---

---
author: YLP
title: 📖 FICHE DE COURS ÉLÈVE
---

# 📖 FICHE DE COURS ÉLÈVE
## Conversions Approfondies · Unités Informatiques · Calculs de Capacité

*Version 1.0 — BTS SIO SISR — Année 1 — Semaine 2*
> **Prérequis :** S1 — Bases décimal/binaire/hexadécimal

---

## Partie 1 — Consolidation des Conversions : Les Réflexes à Installer

### 1.1 Rappel des Méthodes de S1

Avant d'aller plus loin, vérifiez que les trois mouvements de base sont automatiques :

```
┌──────────────────────────────────────────────────────────────────┐
│  BINAIRE → HEXA : groupes de 4 bits de droite à gauche          │
│  10110111  →  1011 | 0111  →  B | 7  →  0xB7                   │
│                                                                  │
│  HEXA → BINAIRE : chaque symbole hexa → 4 bits                  │
│  0xB7  →  B=1011 | 7=0111  →  10110111                          │
│                                                                  │
│  DÉCIMAL → BINAIRE : divisions successives par 2                │
│  BINAIRE → DÉCIMAL : somme des puissances de 2                  │
└──────────────────────────────────────────────────────────────────┘
```

### 1.2 Les Pièges Classiques — Ne Plus Jamais Tomber Dedans

#### Piège n°1 — Les zéros de remplissage à gauche (padding)

Un octet contient **toujours 8 bits**. Si votre résultat fait moins de 8 chiffres, complétez avec des zéros **à gauche**.

```
  Converti 5 en binaire : 5 = 4+1 = 101
  Mais 5 sur un octet s'écrit : 00000101  ← 5 zéros à gauche ajoutés

  Pourquoi ? Parce que 00000101 et 101 ont la même valeur mathématique,
  mais 00000101 précise explicitement qu'on parle d'un octet entier.
  En réseau, en mémoire, les octets sont TOUJOURS représentés sur 8 bits.
```

**Règle à retenir :**
```
  4 bits (nibble)  → compléter à 4 chiffres  : 5 → 0101
  8 bits (octet)   → compléter à 8 chiffres  : 5 → 00000101
  16 bits (2 oct.) → compléter à 16 chiffres : 5 → 0000000000000101
```

#### Piège n°2 — Le sens de lecture (MSB / LSB)

La convention universelle : on lit **de gauche à droite**, du bit de **poids fort** (MSB) au bit de **poids faible** (LSB).

```
  ✅ CORRECT  :  10110111  →  MSB=1 (poids 128)   LSB=1 (poids 1)
  ❌ ERREUR   :  lire de droite à gauche → valeur totalement différente

  1 0 1 1 0 1 1 1
  │               │
  MSB             LSB
  128             1
```

#### Piège n°3 — La table hexadécimale (A à F)

```
  A = 10   (pas 11 !)
  B = 11
  C = 12
  D = 13
  E = 14
  F = 15

  Astuce de mémorisation : A est le 11ème caractère (après 0,1,2,...,9)
  donc A = 10. Comptez depuis 0 : 0,1,2,3,4,5,6,7,8,9, A=10, B=11...
```

#### Piège n°4 — La notation 0x

`0xCA`, `0xFF`, `0x10` sont des nombres hexadécimaux. Le préfixe `0x` **n'est pas un chiffre** — c'est un indicateur de base. On le supprime avant de convertir.

```
  0xFF  →  FF  →  F=1111, F=1111  →  11111111  →  255 en décimal
  0x10  →  10  →  1=0001, 0=0000  →  00010000  →  16 en décimal
           ↑                               ↑
         "10" en hexa ≠ "10" en décimal !   toujours 16, pas 10 !
```

---

### 1.3 Exercices de Consolidation — Série Chrono

Effectuez ces conversions le plus rapidement possible **sans erreur**. Vérifiez chaque résultat avant de passer au suivant.

#### Série A — Binaire → Hexadécimal *(sans table si possible)*

| **Binaire** | **Hexadécimal** | **Vérification décimale** |
|---|---|---|
| `11001100` | *(à trouver)* | *(à calculer)* |
| `10101010` | *(à trouver)* | *(à calculer)* |
| `00001111` | *(à trouver)* | *(à calculer)* |
| `11110000` | *(à trouver)* | *(à calculer)* |
| `10000001` | *(à trouver)* | *(à calculer)* |
| `01111111` | *(à trouver)* | *(à calculer — résultat remarquable !)* |

#### Série B — Hexadécimal → Binaire → Décimal

| **Hexadécimal** | **Binaire (8 bits)** | **Décimal** |
|---|---|---|
| `0x0F` | *(à trouver)* | *(à calculer)* |
| `0xA0` | *(à trouver)* | *(à calculer)* |
| `0xFF` | *(à trouver)* | *(à calculer — résultat remarquable !)* |
| `0x80` | *(à trouver)* | *(à calculer — résultat remarquable !)* |
| `0x1A` | *(à trouver)* | *(à calculer)* |
| `0xC0` | *(à trouver)* | *(à calculer — on reverra ce masque réseau !)* |

#### Série C — Décomposition d'une adresse MAC complète

Décomposez l'adresse MAC `DE:AD:BE:EF:00:FF` octet par octet en binaire :

| **Octet hexa** | **Binaire (8 bits)** |
|---|---|
| `DE` | |
| `AD` | |
| `BE` | |
| `EF` | |
| `00` | |
| `FF` | |

> 💡 **Note culturelle :** `DEADBEEF` est une valeur hexadécimale célèbre en informatique — utilisée historiquement comme "magic number" de débogage dans les processeurs IBM et dans de nombreux systèmes Unix. Si vous voyez `0xDEADBEEF` dans un log, quelqu'un s'est amusé.

---

## Partie 2 — Les Unités Informatiques

### 2.1 La Hiérarchie des Unités — Convention Informatique (Puissances de 2)

```
┌────────────────────────────────────────────────────────────────────┐
│              HIÉRARCHIE DES UNITÉS INFORMATIQUES                   │
│                    (Convention système / IEC)                      │
│                                                                    │
│   bit (b)         La plus petite unité — vaut 0 ou 1              │
│      │                                                             │
│      × 8                                                           │
│      ↓                                                             │
│   octet (o) [byte (B)]    8 bits — valeur de 0 à 255              │
│      │                                                             │
│      × 1 024  (= 2¹⁰)                                             │
│      ↓                                                             │
│   kilooctet (Ko) [Kio]    1 024 octets                            │
│      │                                                             │
│      × 1 024  (= 2¹⁰)                                             │
│      ↓                                                             │
│   mégaoctet (Mo) [Mio]    1 024 Ko = 1 048 576 octets             │
│      │                                                             │
│      × 1 024  (= 2¹⁰)                                             │
│      ↓                                                             │
│   gigaoctet (Go) [Gio]    1 024 Mo = 1 073 741 824 octets         │
│      │                                                             │
│      × 1 024  (= 2¹⁰)                                             │
│      ↓                                                             │
│   téraoctet (To) [Tio]    1 024 Go = 1 099 511 627 776 octets     │
│      │                                                             │
│      × 1 024  (= 2¹⁰)                                             │
│      ↓                                                             │
│   pétaoctet (Po) [Pio]    1 024 To  (datacenters, cloud)          │
└────────────────────────────────────────────────────────────────────┘
```
*[Illustration : Pyramide ou escalier montant, avec chaque unité sur une marche. Les flèches entre les marches indiquent "×1024" pour monter et "÷1024" pour descendre. Les valeurs en octets sont indiquées à droite de chaque marche. La pyramide est colorée : bit et octet en gris, Ko en jaune clair, Mo en orange clair, Go en orange, To en rouge.]*

### 2.2 La Règle d'Or des Conversions d'Unités

```
╔══════════════════════════════════════════════════════╗
║  POUR MONTER D'UN NIVEAU → DIVISER PAR 1 024         ║
║  POUR DESCENDRE D'UN NIVEAU → MULTIPLIER PAR 1 024   ║
╚══════════════════════════════════════════════════════╝

  Exemples :
  4 096 octets ÷ 1024  =    4 Ko
  4 Ko         ÷ 1024  =  0,004 Mo  (= 1/256 de Mo)
  2 Go         × 1024  =  2 048 Mo
  2 Go         × 1024 × 1024  =  2 097 152 Ko
  2 Go         × 1024 × 1024 × 1024  =  2 147 483 648 octets
```

> ⚠️ **Attention :** Pour convertir plusieurs niveaux d'un coup, multipliez ou divisez par **1024 autant de fois que de niveaux franchis**.
>
> Exemple : `3 Go → octets` = `3 × 1024 × 1024 × 1024 = 3 × 2³⁰ = 3 221 225 472 octets`

### 2.3 Tableau de Référence Rapide

| **Unité** | **Symbole** | **En octets** | **Puissance de 2** |
|---|---|---|---|
| Bit | b | 1/8 octet | — |
| Octet | o / B | 1 | 2⁰ |
| Kilooctet | Ko / Kio | 1 024 | 2¹⁰ |
| Mégaoctet | Mo / Mio | 1 048 576 | 2²⁰ |
| Gigaoctet | Go / Gio | 1 073 741 824 | 2³⁰ |
| Téraoctet | To / Tio | 1 099 511 627 776 | 2⁴⁰ |
| Pétaoctet | Po / Pio | 1 125 899 906 842 624 | 2⁵⁰ |

---

## Partie 3 — Le "Mensonge du Disque Dur" Expliqué

### 3.1 Deux Conventions, Deux Mondes

Le monde informatique utilise en réalité **deux systèmes d'unités** qui coexistent et créent de la confusion :

```
┌─────────────────────────────────────────────────────────────────────┐
│            SI (Système International) — Fabricants marketing        │
│                     "Puissances de 10"                              │
│                                                                     │
│   1 Ko = 1 000 octets          (10³)                               │
│   1 Mo = 1 000 000 octets      (10⁶)                               │
│   1 Go = 1 000 000 000 octets  (10⁹)                               │
│   1 To = 1 000 000 000 000 octets (10¹²)                           │
│                                                                     │
│   Utilisé par : fabricants de disques durs, SSD, clés USB          │
│   But : afficher un chiffre plus grand sur l'emballage              │
├─────────────────────────────────────────────────────────────────────┤
│            IEC 80000-13 — Systèmes d'exploitation                  │
│                     "Puissances de 2"                               │
│                                                                     │
│   1 Kio = 1 024 octets         (2¹⁰)                               │
│   1 Mio = 1 048 576 octets     (2²⁰)                               │
│   1 Gio = 1 073 741 824 octets (2³⁰)                               │
│   1 Tio = 1 099 511 627 776 octets (2⁴⁰)                           │
│                                                                     │
│   Utilisé par : Windows, Linux, macOS, BIOS/UEFI                   │
│   But : cohérence avec l'architecture binaire du matériel           │
└─────────────────────────────────────────────────────────────────────┘
```
*[Illustration : Deux colonnes côte à côte, fond bleu pour SI/fabricants et fond vert pour IEC/OS. En dessous, un exemple concret : un disque dur 1 To (fabricant) = 931 Gio (Windows). Une flèche de l'un à l'autre avec la formule de conversion.]*

### 3.2 Calculer la "Perte" Apparente — La Formule

```
  Capacité affichée Windows (Gio) = Capacité fabricant (Go)  ×  10⁹ ÷ 2³⁰

  Simplification pratique :
  Capacité affichée Windows (Gio) ≈ Capacité fabricant (Go) × 0,931

  Exemples :
  Disque 500 Go  → 500 × 0,931 ≈  465 Gio  (Windows affiche 465 Go)
  Disque 1 To    → 1000 × 0,931 ≈ 931 Gio  (Windows affiche 931 Go)
  Disque 2 To    → 2000 × 0,931 ≈ 1862 Gio (Windows affiche 1,81 To)
  Disque 4 To    → 4000 × 0,931 ≈ 3725 Gio (Windows affiche 3,63 To)
```

> 💡 **À retenir pour l'examen BTS :** Sauf indication contraire, utilisez **toujours les puissances de 2** dans vos calculs. C'est la convention utilisée en informatique système et réseau.

### 3.3 Cas Particulier : La RAM Toujours en Puissances de 2

La mémoire vive (RAM) est **toujours** commercialisée et mesurée en puissances de 2, sans ambiguïté :

```
  4 Go RAM  = 4 × 2³⁰ = 4 294 967 296 octets  (toujours)
  8 Go RAM  = 8 × 2³⁰ = 8 589 934 592 octets  (toujours)
  16 Go RAM = 16 × 2³⁰                         (toujours)
```

**Pourquoi ?** La RAM est organisée physiquement en puissances de 2 — ce n'est pas une convention marketing, c'est une contrainte architecturale. Il n'y a pas de "mensonge" sur la RAM.

---

## Partie 4 — Calculs de Capacité : Méthodes et Applications

### 4.1 Méthode Générale

Pour tout calcul de capacité ou de dimensionnement :

```
╔══════════════════════════════════════════════════════════════════╗
║  ÉTAPE 1 : Identifier les données (quelle unité ? quelle base ?) ║
║  ÉTAPE 2 : Tout ramener à la même unité (souvent les octets)     ║
║  ÉTAPE 3 : Effectuer le calcul (×, ÷, +, -)                      ║
║  ÉTAPE 4 : Reconvertir dans l'unité demandée                     ║
║  ÉTAPE 5 : Vérifier l'ordre de grandeur (est-ce raisonnable ?)   ║
╚══════════════════════════════════════════════════════════════════╝
```

### 4.2 Exemples Résolus

---

**Exemple 1 — Conversion simple**

> Un fichier pèse 3 584 Ko. Quelle est sa taille en Mo ?

```
  3 584 Ko ÷ 1 024 = 3,5 Mo
  → Le fichier pèse 3,5 Mo
```

---

**Exemple 2 — Calcul de nombre de fichiers**

> Un serveur dispose de 2 Go d'espace libre. Combien peut-il stocker de fichiers de 750 Ko chacun ?

```
  Étape 1 : Convertir 2 Go en Ko
  2 Go × 1024 = 2 048 Mo
  2 048 Mo × 1024 = 2 097 152 Ko

  Étape 2 : Diviser par la taille d'un fichier
  2 097 152 Ko ÷ 750 Ko = 2 796,2...

  Étape 3 : Arrondir à l'entier inférieur (on ne peut pas stocker un demi-fichier)
  → Le serveur peut stocker 2 796 fichiers de 750 Ko
```

---

**Exemple 3 — Dimensionnement d'un NAS**

> Une entreprise doit stocker 5 000 fichiers de sauvegarde de 1,2 Go chacun. Quelle capacité minimale de NAS commander ?

```
  Étape 1 : Calculer le volume total
  5 000 × 1,2 Go = 6 000 Go

  Étape 2 : Convertir en To
  6 000 Go ÷ 1 024 = 5,86 To

  Étape 3 : Ajouter une marge de sécurité (20% recommandé en pratique)
  5,86 × 1,20 = 7,03 To

  → Commander un NAS d'au moins 8 To (arrondir au modèle commercial supérieur)
```

---

**Exemple 4 — Conversion fabricant → système**

> Un SSD est vendu "256 Go". Combien d'espace affichera-t-il sous Windows ?

```
  Méthode précise :
  256 Go fabricant = 256 × 10⁹ octets = 256 000 000 000 octets
  ÷ 2³⁰ (1 Go système) = 256 000 000 000 ÷ 1 073 741 824
  ≈ 238,4 Gio

  Méthode rapide (approximation ×0,931) :
  256 × 0,931 ≈ 238 Go

  → Windows affichera environ 238 Go pour un SSD vendu 256 Go.
```

---

### 4.3 Exercices d'Application

**Exercice 1 :** Un document Word pèse 2 048 Ko. Convertissez sa taille en Mo, puis en Go.

**Exercice 2 :** Un téléphone affiche "64 Go" de stockage (convention fabricant SI). Quelle taille affichera-t-il réellement dans les paramètres du système ?

**Exercice 3 :** Un disque dur de serveur contient 1 500 Go de données. Convertissez en To (arrondi à 2 décimales).

**Exercice 4 :** Un répertoire de photos contient 4 800 fichiers de 4,5 Mo chacun. Quelle taille totale occupe-t-il en Go ?

**Exercice 5 :** Un NAS de 8 To est déjà rempli à 60%. Combien d'espace reste-t-il en Go ?

**Exercice 6 :** Un technicien commande un serveur avec 3 disques de 2 To en configuration sans RAID (stockage simple additionné). Combien d'octets de stockage total cela représente-t-il ? (Convention système — puissances de 2)

**Exercice 7 :** Une clé USB de 32 Go (fabricant SI) peut contenir combien de fichiers PDF de 2,5 Mo ? (Utilisez la capacité réelle en puissances de 2.)

---

## Partie 5 — Récapitulatif et Mémo

### 5.1 Les Valeurs à Mémoriser Absolument

```
╔═══════════════════════════════════════════════════════════════════╗
║             VALEURS INCONTOURNABLES EN BTS SIO SISR               ║
╠═══════════════════════════════════════════════════════════════════╣
║  1 octet     =     8 bits                                         ║
║  1 Ko        =  1 024 octets   (= 2¹⁰)                           ║
║  1 Mo        =  1 024 Ko       (= 2²⁰ = 1 048 576 octets)        ║
║  1 Go        =  1 024 Mo       (= 2³⁰ = 1 073 741 824 octets)    ║
║  1 To        =  1 024 Go       (= 2⁴⁰)                           ║
╠═══════════════════════════════════════════════════════════════════╣
║  255  = 0xFF = 11111111   (valeur max d'un octet)                 ║
║  256  = 2⁸                (nombre de valeurs d'un octet)          ║
║  1024 = 2¹⁰               (base des unités informatiques)         ║
╠═══════════════════════════════════════════════════════════════════╣
║  DISQUE FABRICANT → WINDOWS  :  × 0,931 (approximation)          ║
║  Ou plus précis : × (10⁹ ÷ 2³⁰) = × 0,9313...                   ║
╚═══════════════════════════════════════════════════════════════════╝
```

### 5.2 Pense-Bête des Conversions

```
               MONTER (÷ 1024)
               ───────────────►
  octets → Ko → Mo → Go → To → Po
         ◄───────────────
               DESCENDRE (× 1024)

  Sauter 2 niveaux : × ou ÷ 1024² = × ou ÷ 1 048 576
  Sauter 3 niveaux : × ou ÷ 1024³ = × ou ÷ 1 073 741 824
```

---

## Vocabulaire Clé à Maîtriser pour l'Examen

| **Terme** | **Définition** |
|---|---|
| **Bit** | Unité minimale d'information — 0 ou 1 |
| **Octet (byte)** | 8 bits — représente une valeur de 0 à 255 |
| **Ko (kilooctet)** | 1 024 octets — convention système (puissances de 2) |
| **Mo (mégaoctet)** | 1 024 Ko = 1 048 576 octets |
| **Go (gigaoctet)** | 1 024 Mo = 1 073 741 824 octets |
| **To (téraoctet)** | 1 024 Go = 1 099 511 627 776 octets |
| **SI (Système International)** | Convention décimale (10³, 10⁶, 10⁹...) — utilisée par les fabricants |
| **IEC 80000-13** | Standard international définissant Kio, Mio, Gio... en puissances de 2 |
| **Padding (remplissage)** | Ajout de zéros à gauche pour compléter un groupe de bits à la taille standard |
| **Dimensionnement** | Calcul de la capacité nécessaire pour un besoin de stockage donné |
| **Marge de sécurité** | Pourcentage de capacité supplémentaire prévu pour l'évolution et les imprévus (généralement 20 à 30%) |


---


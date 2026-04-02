---
author: YLP
title: 📖 FICHE DE COURS
---

# 📖 FICHE DE COURS
## VLSM · Découpage en Sous-réseaux de Tailles Différentes · Plan d'Adressage

*Version 1.0 — BTS SIO SISR — Année 1 — Semaine 5*
> **Prérequis :** S4 complet — algorithme de sous-réseau, AND bit à bit, calcul réseau/broadcast/hôtes

---

## Partie 1 — Pourquoi le VLSM ?

### 1.1 Le Problème du Découpage à Taille Fixe (FLSM)

Avant VLSM, il existait une méthode simple appelée **FLSM** *(Fixed Length Subnet Masking)* : on découpe tous les sous-réseaux avec le **même masque**, quelle que soit la taille réelle du besoin.

**Le problème :** si les besoins sont très différents (100 hôtes ici, 5 hôtes là), FLSM force à dimensionner tous les sous-réseaux pour le plus grand besoin — ce qui gaspille des adresses.

```
  EXEMPLE DE GASPILLAGE FLSM
  Besoins : Service A = 100 hôtes / Service B = 5 hôtes
  Bloc disponible : 192.168.0.0/24 (254 hôtes utilisables)

  Avec FLSM (masque /25 pour tous) :
  ┌───────────────────────┐ ┌──────────────────────┐
  │  Service A : /25      │ │  Service B : /25      │
  │  126 hôtes dispo      │ │  126 hôtes dispo      │
  │  100 utilisés         │ │  5 utilisés           │
  │  26 gaspillés         │ │  121 GASPILLÉS !!     │
  └───────────────────────┘ └──────────────────────┘
  Gaspillage total : 26 + 121 = 147 adresses perdues sur 254.
```
*[Illustration : Deux rectangles côte à côte représentant deux sous-réseaux /25 dans un /24. Dans le premier (Service A), 100 cases sont remplies et 26 sont hachurées (gaspillage). Dans le second (Service B), 5 cases sont remplies et 121 sont hachurées. Le fond hachuré représente visuellement l'ampleur du gaspillage.]*

### 1.2 La Solution VLSM — Adapter le Masque au Besoin

**VLSM** *(Variable Length Subnet Masking)* : chaque sous-réseau reçoit **le masque exactement adapté à son besoin réel**.

```
  MÊME EXEMPLE AVEC VLSM
  Service A = 100 hôtes → /25 (126 hôtes dispo) : 192.168.0.0/25
  Service B =   5 hôtes → /29  (6 hôtes dispo)  : 192.168.0.128/29

  ┌────────────────────────────────┐ ┌──────┐ ┌─ réserve libre ─────────┐
  │  Service A : /25               │ │ B /29│ │  192.168.0.136 → .255   │
  │  .0 à .127  (128 adresses)     │ │ 8 @  │ │  120 adresses libres     │
  └────────────────────────────────┘ └──────┘ └─────────────────────────┘
  Gaspillage : 26 (A) + 2 (B) = 28 seulement. La réserve est utilisable.
```
*[Illustration : La même barre /24 mais avec Service A occupant la moitié gauche (/25) et Service B un tout petit bloc (/29) juste après, suivi d'une grande zone libre et disponible.]*

> 💡 **VLSM = couture sur mesure.** FLSM taille tous les habits à la même taille. VLSM adapte chaque habit à la morphologie réelle.

---

## Partie 2 — La Règle d'Or et L'Algorithme

### 2.1 La Règle Fondamentale

```
╔══════════════════════════════════════════════════════════════════╗
║               RÈGLE D'OR DU VLSM                                 ║
║                                                                  ║
║   Toujours allouer les sous-réseaux du PLUS GRAND besoin        ║
║   au PLUS PETIT besoin.                                          ║
║                                                                  ║
║   Pourquoi ?                                                     ║
║   Les grands sous-réseaux ont des contraintes d'alignement       ║
║   binaire plus fortes. En les plaçant en premier, on garantit    ║
║   que les adresses de départ disponibles sont toujours           ║
║   valides. Les petits sous-réseaux s'insèrent ensuite dans       ║
║   les espaces restants.                                          ║
╚══════════════════════════════════════════════════════════════════╝
```

### 2.2 Table de Correspondance Besoin → Masque Minimal

Avant de calculer, il faut trouver le **plus petit masque** tel que `2ⁿ − 2 ≥ besoin` (n = bits hôtes) :

```
╔══════════╦═══════╦════════════════╦════════╦═══════════════════╗
║  Besoin  ║  /xxx ║  2ⁿ − 2 hôtes ║ Masque ║  Usage typique    ║
╠══════════╬═══════╬════════════════╬════════╬═══════════════════╣
║  1 – 2   ║  /30  ║       2        ║ .252   ║ Lien point-à-point║
║  3 – 6   ║  /29  ║       6        ║ .248   ║ Très petit segment║
║  7 – 14  ║  /28  ║      14        ║ .240   ║ Petit service     ║
║ 15 – 30  ║  /27  ║      30        ║ .224   ║ Segment moyen     ║
║ 31 – 62  ║  /26  ║      62        ║ .192   ║ Segment courant   ║
║ 63 – 126 ║  /25  ║     126        ║ .128   ║ Grand segment     ║
║127 – 254 ║  /24  ║     254        ║   .0   ║ Réseau de site    ║
╚══════════╩═══════╩════════════════╩════════╩═══════════════════╝
```
*[Illustration : Le même tableau avec, en colonne supplémentaire, une représentation visuelle en barre proportionnelle : /30 = minuscule barre, /24 = barre pleine. Permet de visualiser la progression géométrique par 2.]*

### 2.3 L'Algorithme VLSM en 4 Étapes

```
╔══════════════════════════════════════════════════════════════════╗
║                    ALGORITHME VLSM                               ║
║                                                                  ║
║  ENTRÉE : bloc d'adresses de départ, liste des besoins           ║
║                                                                  ║
║  ÉTAPE 1 — TRIER                                                 ║
║    Classer les besoins du plus grand nombre d'hôtes              ║
║    au plus petit.                                                ║
║                                                                  ║
║  ÉTAPE 2 — ITÉRER sur chaque besoin (dans l'ordre trié) :        ║
║    a) Trouver le masque minimal → table de correspondance        ║
║    b) L'adresse réseau = adresse disponible courante             ║
║       (au départ = début du bloc ; ensuite = broadcast+1)        ║
║    c) Appliquer l'algorithme de S4 :                             ║
║       réseau, wildcard, broadcast, plage, nb hôtes               ║
║    d) Mettre à jour : adresse disponible ← broadcast + 1         ║
║                                                                  ║
║  ÉTAPE 3 — VÉRIFIER                                              ║
║    Pour chaque paire de sous-réseaux consécutifs :               ║
║    broadcast(n) + 1 = réseau(n+1) → pas de chevauchement ✓      ║
║    Vérifier que tout tient dans le bloc de départ.               ║
║                                                                  ║
║  ÉTAPE 4 — DOCUMENTER                                            ║
║    Remplir le tableau professionnel du plan d'adressage.         ║
║                                                                  ║
║  SORTIE : tableau de plan d'adressage complet                    ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## Partie 3 — Exemple Guidé Complet : CABINET MERIDIAN

### Contexte

Le Cabinet d'avocats MERIDIAN vous confie la conception de leur réseau. Bloc disponible : `192.168.10.0/24`.

**Besoins :**

| **Service** | **Nb de machines à connecter** |
|---|---|
| Service Juridique | 85 avocats + postes |
| Service Administratif | 35 personnes |
| Direction | 12 collaborateurs |

---

### Étape 1 — Trier du Plus Grand au Plus Petit

| **Ordre** | **Service** | **Besoin** |
|---|---|---|
| 1 | Service Juridique | 85 hôtes |
| 2 | Service Administratif | 35 hôtes |
| 3 | Direction | 12 hôtes |

---

### Étape 2 — Calculer et Allouer Chaque Sous-réseau

#### Sous-réseau 1 — Service Juridique (85 hôtes)

```
  Besoin : 85 hôtes
  Table : 63–126 hôtes → /25 (126 hôtes dispo, 2⁷−2 = 126 ≥ 85 ✓)
  Masque : 255.255.255.128

  Adresse réseau : 192.168.10.0 (début du bloc)

  Calcul binaire du 4ème octet :
  IP (=réseau) : 00000000 (= 0)
  Masque 4ème  : 10000000 (= 128)
  AND          : 00000000 (= 0) → réseau = 192.168.10.0 ✓
  NOT(masque)  : 01111111 (= 127) → wildcard
  OR broadcast : 00000000 OR 01111111 = 01111111 (= 127)
  → Broadcast : 192.168.10.127

  Plage hôtes : 192.168.10.1 → 192.168.10.126
  Nb hôtes    : 2⁷ − 2 = 126

  Prochaine adresse disponible : 192.168.10.127 + 1 = 192.168.10.128
```

#### Sous-réseau 2 — Service Administratif (35 hôtes)

```
  Besoin : 35 hôtes
  Table : 31–62 hôtes → /26 (62 hôtes dispo, 2⁶−2 = 62 ≥ 35 ✓)
  Masque : 255.255.255.192

  Adresse réseau : 192.168.10.128 (= broadcast précédent + 1)

  Calcul binaire du 4ème octet :
  IP (=réseau) : 10000000 (= 128)
  Masque 4ème  : 11000000 (= 192)
  AND          : 10000000 (= 128) → réseau = 192.168.10.128 ✓
  NOT(masque)  : 00111111 (= 63) → wildcard
  OR broadcast : 10000000 OR 00111111 = 10111111 (= 191)
  → Broadcast : 192.168.10.191

  Plage hôtes : 192.168.10.129 → 192.168.10.190
  Nb hôtes    : 2⁶ − 2 = 62

  Prochaine adresse disponible : 192.168.10.191 + 1 = 192.168.10.192
```

#### Sous-réseau 3 — Direction (12 hôtes)

```
  Besoin : 12 hôtes
  Table : 7–14 hôtes → /28 (14 hôtes dispo, 2⁴−2 = 14 ≥ 12 ✓)
  Masque : 255.255.255.240

  Adresse réseau : 192.168.10.192 (= broadcast précédent + 1)

  Calcul binaire du 4ème octet :
  IP (=réseau) : 11000000 (= 192)
  Masque 4ème  : 11110000 (= 240)
  AND          : 11000000 (= 192) → réseau = 192.168.10.192 ✓
  NOT(masque)  : 00001111 (= 15) → wildcard
  OR broadcast : 11000000 OR 00001111 = 11001111 (= 207)
  → Broadcast : 192.168.10.207

  Plage hôtes : 192.168.10.193 → 192.168.10.206
  Nb hôtes    : 2⁴ − 2 = 14

  Prochaine adresse disponible : 192.168.10.207 + 1 = 192.168.10.208
```

---

### Étape 3 — Vérification

```
  Sous-réseau 1 : 192.168.10.0   → broadcast 192.168.10.127
  Sous-réseau 2 : 192.168.10.128 → broadcast 192.168.10.191
  Sous-réseau 3 : 192.168.10.192 → broadcast 192.168.10.207

  Vérification 1→2 : 127 + 1 = 128 ✓ (pas de saut, pas de chevauchement)
  Vérification 2→3 : 191 + 1 = 192 ✓
  Dernier broadcast : .207 < .255 → tout tient dans le /24 ✓

  Réserve disponible : 192.168.10.208 → 192.168.10.255 (48 adresses libres)
```

---

### Étape 4 — Plan d'Adressage Documenté

```
╔═══════════════╦══════════════════════╦══════╦════════════════════╦════════════════════╦══════════════════════╦══════╗
║ Service       ║ Adresse réseau       ║ CIDR ║ Masque             ║ Plage hôtes        ║ Broadcast            ║ Hôtes║
╠═══════════════╬══════════════════════╬══════╬════════════════════╬════════════════════╬══════════════════════╬══════╣
║ Juridique     ║ 192.168.10.0         ║ /25  ║ 255.255.255.128    ║ .1 → .126          ║ 192.168.10.127       ║  126 ║
║ Administratif ║ 192.168.10.128       ║ /26  ║ 255.255.255.192    ║ .129 → .190        ║ 192.168.10.191       ║   62 ║
║ Direction     ║ 192.168.10.192       ║ /28  ║ 255.255.255.240    ║ .193 → .206        ║ 192.168.10.207       ║   14 ║
║ RÉSERVE       ║ 192.168.10.208       ║ /28* ║ —                  ║ 192.168.10.208     ║ 192.168.10.255       ║  —   ║
╚═══════════════╩══════════════════════╩══════╩════════════════════╩════════════════════╩══════════════════════╩══════╝
* La réserve peut être découpée ultérieurement selon les besoins.
```
*[Illustration : Le même tableau présenté en "vision barre" : une longue barre horizontale représentant le /24, divisée en 4 sections de largeurs proportionnelles. Juridique (/25) occupe la moitié, Administratif (/26) occupe un quart, Direction (/28) un seizième, et la réserve le reste. Les sections sont colorées différemment avec le nom du service.]*

---

## Partie 4 — Visualisation Graphique du Découpage

Un plan d'adressage VLSM se lit plus facilement sous forme de barre proportionnelle :

```
  192.168.10.0/24  ← 256 adresses au total →  192.168.10.255
  ╔══════════════════════════════╦═══════════════╦════╦══════════╗
  ║  Service Juridique   /25     ║  Administ. /26║Dir.║ Réserve  ║
  ║  .0 → .127  (128 @)          ║  .128→.191    ║/28 ║  48 @    ║
  ║                              ║  (64 @)       ║.192║          ║
  ╚══════════════════════════════╩═══════════════╩════╩══════════╝
  ↑ .0                         ↑ .128          ↑.192↑.208      ↑.255
```

> 💡 **Astuce :** Ce diagramme permet de **vérifier visuellement** qu'il n'y a pas de chevauchement et d'estimer l'espace encore disponible. En pratique professionnelle, ce schéma accompagne toujours le tableau de plan d'adressage.

---

## Partie 5 — VLSM et Sécurité Réseau

### Pourquoi Segmenter en VLSM Est Une Mesure de Sécurité

Chaque sous-réseau VLSM est un **segment réseau isolable** :

```
╔══════════════════════════════════════════════════════════════════╗
║           VLSM + PARE-FEU = SEGMENTATION SÉCURISÉE             ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  Sans segmentation :                                             ║
║  Toutes les machines dans 192.168.10.0/24                       ║
║  → Un virus sur un poste Juridique peut atteindre               ║
║    directement tous les postes de la Direction.                  ║
║                                                                  ║
║  Avec segmentation VLSM + pare-feu :                            ║
║  Juridique /25 → filtre → Administratif /26 → filtre → Direction/28║
║  → Le virus est confiné dans le sous-réseau Juridique.           ║
║  → La Direction est protégée par un filtrage explicite.          ║
╚══════════════════════════════════════════════════════════════════╝
```

**En termes booléens (lien S3) :** la règle pare-feu entre les segments s'écrit :

```
  ACCEPT trafic de Juridique vers Direction
  SI   (source ∈ 192.168.10.0/25)     [SJ = 1]
  AND  (destination ∈ 192.168.10.192/28) [DD = 1]
  AND  (protocole = TCP)               [T = 1]
  AND  (port = 443)                    [P443 = 1]

  Expression : ACCEPT = SJ AND DD AND T AND P443
```

> 💡 **VLSM n'est pas qu'une économie d'adresses — c'est une architecture de sécurité.** En décidant quels services sont dans quel sous-réseau, l'architecte réseau décide aussi du périmètre que le pare-feu devra protéger.

---

## Partie 6 — Exercices Guidés

### Exercice 1 — PME Simple (3 services)

La société **ARTISANS DU BOIS** vous fournit ce contexte :
- Bloc disponible : `10.10.0.0/24`
- Service Atelier : 60 machines
- Service Bureau : 25 machines
- Service Accueil : 5 machines

**Travail :** Appliquez l'algorithme VLSM complet en 4 étapes et produisez le tableau de plan d'adressage.

*(Utilisez la grille de calcul de S4 pour chaque sous-réseau.)*

---

### Exercice 2 — Services Réseau (avec lien point-à-point)

La **CLINIQUE ALPHACARE** a besoin de :
- Bloc disponible : `172.16.50.0/24`
- Service Médical : 100 médecins et infirmiers
- Service Administratif : 45 secrétaires
- Service Imagerie : 20 stations
- Lien routeur-routeur : 2 interfaces (lien point-à-point)

**Questions :**
a) Appliquez l'algorithme VLSM. Quel masque choisissez-vous pour le lien point-à-point ?
b) Combien d'adresses reste-t-il dans la réserve à la fin du découpage ?

---

### Exercice 3 — Critique d'un Plan Existant

Un stagiaire a produit ce plan d'adressage pour le bloc `192.168.5.0/24`. Identifiez toutes les erreurs.

| **Service** | **Réseau** | **Masque** | **Plage** | **Broadcast** | **Hôtes** |
|---|---|---|---|---|---|
| Ventes (80 hôtes) | 192.168.5.0 | /26 | .1 → .62 | 192.168.5.63 | 62 |
| Production (40 hôtes) | 192.168.5.64 | /26 | .65 → .126 | 192.168.5.127 | 62 |
| RH (15 hôtes) | 192.168.5.130 | /28 | .131 → .142 | 192.168.5.143 | 14 |

*(Indice : il y a au moins 3 erreurs dans ce tableau.)*

---

## Vocabulaire Clé à Maîtriser pour l'Examen

| **Terme** | **Définition** |
|---|---|
| **VLSM** | Variable Length Subnet Masking — technique de découpage réseau avec des masques de longueurs différentes adaptés aux besoins réels |
| **FLSM** | Fixed Length Subnet Masking — découpage avec le même masque pour tous les sous-réseaux (gaspilleur) |
| **Plan d'adressage** | Document technique listant tous les sous-réseaux d'une infrastructure avec leurs caractéristiques |
| **Alignement binaire** | Contrainte imposant que l'adresse de début d'un sous-réseau soit un multiple de la taille de ce sous-réseau |
| **Règle du plus grand au plus petit** | Ordre impératif d'allocation en VLSM — garantit la validité des adresses de départ |
| **Réserve d'adresses** | Espace adresse non encore alloué, conservé pour l'extension future |
| **Segmentation réseau** | Division d'un réseau en sous-réseaux distincts à des fins d'organisation et/ou de sécurité |
| **Wildcard mask** | Inverse du masque de sous-réseau (NOT bit à bit) — utilisé pour calculer le broadcast et dans les ACL |
| **Broadcast + 1** | Adresse de départ du sous-réseau suivant dans un découpage VLSM séquentiel |
| **VLAN** | Virtual LAN — segmentation logique au niveau des commutateurs, souvent associée à un sous-réseau VLSM |

---

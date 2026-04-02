---
author: YLP
title: 📖 FICHE DE COURS
---

# 📖 FICHE DE COURS ÉLÈVE
## Masques de Sous-réseau · CIDR · Adresse Réseau · Broadcast · Plage d'Hôtes

*Version 1.0 — BTS SIO SISR — Année 1 — Semaine 4*
> **Prérequis :** S1 (binaire), S2 (octets), S3 (AND, NOT, OR bit à bit)

---

## Partie 1 — Pourquoi un Masque de Sous-réseau ?

### 1.1 Le Problème : Comment Savoir si Deux Machines Sont "Voisines" ?

Une adresse IPv4 est un nombre de **32 bits** divisé en deux parties :
- La **partie réseau** : identifie le réseau auquel appartient la machine
- La **partie hôte** : identifie la machine individuelle au sein de ce réseau

```
┌────────────────────────────────────────────────────────────────────┐
│             UNE ADRESSE IP = DEUX INFORMATIONS                     │
│                                                                    │
│   192  .  168  .   1   .  42                                       │
│   ─────────────────────   ──                                       │
│       Partie réseau       Partie hôte                              │
│   (identifie le réseau)  (identifie la machine)                    │
│                                                                    │
│   Mais la frontière n'est pas forcément après le 3ème octet !      │
│   C'est le MASQUE qui dit où elle est.                             │
└────────────────────────────────────────────────────────────────────┘
```
*[Illustration : Une adresse IP complète de 32 bits représentée comme une barre horizontale. La partie gauche (en bleu) est annotée "Partie réseau = fixe pour toutes les machines du réseau". La partie droite (en vert) est annotée "Partie hôte = unique pour chaque machine". Une flèche verticale entre les deux parties indique "Le masque définit où passe la frontière".]*

### 1.2 Le Masque : Un Nombre Binaire Avec des 1 Puis des 0

Un masque de sous-réseau est un nombre de **32 bits** qui respecte une règle stricte :

```
╔══════════════════════════════════════════════════════════════════╗
║  RÈGLE FONDAMENTALE DU MASQUE                                    ║
║                                                                  ║
║  Le masque commence toujours par des 1 consécutifs,             ║
║  suivis de 0 consécutifs.                                        ║
║                                                                  ║
║  1111...1110000...000                                            ║
║  ↑ n bits à 1     ↑ (32−n) bits à 0                             ║
║                                                                  ║
║  Les bits à 1 = partie RÉSEAU (fixe, commune à toutes            ║
║                 les machines du réseau)                          ║
║  Les bits à 0 = partie HÔTE (variable, propre à chaque          ║
║                 machine)                                         ║
╚══════════════════════════════════════════════════════════════════╝
```

> ⚠️ **Un masque INVALIDE ne peut jamais avoir un 0 avant un 1** : `11110111` est illégal comme masque. Les bits à 1 forment toujours un bloc continu et ininterrompu, à gauche.

---

## Partie 2 — Les Deux Notations du Masque

### 2.1 Notation Décimale Pointée

Chaque groupe de 8 bits du masque est converti en décimal. Les seules valeurs possibles pour un octet de masque sont donc celles qui s'obtiennent avec des 1 consécutifs suivis de 0 consécutifs :

```
╔══════════════════════════════════════════════════════════════════╗
║          LES 9 VALEURS POSSIBLES D'UN OCTET DE MASQUE            ║
╠══════════════╦═══════════╦═════════╦═════════════════════════════╣
║ Binaire      ║ Décimal   ║ Bits à 1║ Commentaire                 ║
╠══════════════╬═══════════╬═════════╬═════════════════════════════╣
║ 00000000     ║    0      ║    0    ║ Octet "hôte" complet        ║
║ 10000000     ║  128      ║    1    ║                             ║
║ 11000000     ║  192      ║    2    ║ Vu dans la paire 3 (/26)   ║
║ 11100000     ║  224      ║    3    ║                             ║
║ 11110000     ║  240      ║    4    ║                             ║
║ 11111000     ║  248      ║    5    ║                             ║
║ 11111100     ║  252      ║    6    ║ Lien point-à-point (/30)   ║
║ 11111110     ║  254      ║    7    ║                             ║
║ 11111111     ║  255      ║    8    ║ Octet "réseau" complet      ║
╚══════════════╩═══════════╩═════════╩═════════════════════════════╝
```
*[Illustration : Le même tableau avec, pour chaque ligne, une représentation visuelle des 8 cases binaires : les cases à 1 sont remplies en bleu, les cases à 0 sont vides. Permet de voir visuellement le "glissement" du bloc de 1.]*

> 💡 **Astuce :** Un masque en décimal pointé ne peut contenir que des octets valant 0, 128, 192, 224, 240, 248, 252, 254 ou 255. Si vous voyez 241 ou 200 dans un masque, c'est une erreur de configuration.

### 2.2 Notation CIDR *(Classless Inter-Domain Routing)*

La notation **CIDR** est beaucoup plus simple : c'est juste le **nombre de bits à 1** dans le masque, précédé d'un `/`.

```
  /24 = 24 bits à 1 = 11111111.11111111.11111111.00000000
                    = 255.255.255.0

  /26 = 26 bits à 1 = 11111111.11111111.11111111.11000000
                    = 255.255.255.192

  /20 = 20 bits à 1 = 11111111.11111111.11110000.00000000
                    = 255.255.240.0
```

**Conversion CIDR → Décimal :**

1. Placer `n` bits à 1 suivis de `(32 − n)` bits à 0
2. Convertir chaque octet de 8 bits en décimal

**Conversion Décimal → CIDR :**

1. Convertir chaque octet en binaire
2. Compter le nombre total de bits à 1

---

### 2.3 Table des Masques Courants — À Connaître par Cœur

| **CIDR** | **Décimal pointé** | **Bits réseau** | **Bits hôte** | **Nb hôtes max** | **Usage typique** |
|---|---|---|---|---|---|
| **/8** | 255.0.0.0 | 8 | 24 | 16 777 214 | Plages privées (10.x.x.x) |
| **/16** | 255.255.0.0 | 16 | 16 | 65 534 | Plages privées (172.16.x.x) |
| **/24** | 255.255.255.0 | 24 | 8 | 254 | Réseau de PME courant |
| **/25** | 255.255.255.128 | 25 | 7 | 126 | Division d'un /24 en 2 |
| **/26** | 255.255.255.192 | 26 | 6 | 62 | Division d'un /24 en 4 |
| **/27** | 255.255.255.224 | 27 | 5 | 30 | Petit segment |
| **/28** | 255.255.255.240 | 28 | 4 | 14 | Très petit segment |
| **/29** | 255.255.255.248 | 29 | 3 | 6 | Lien entre quelques hôtes |
| **/30** | 255.255.255.252 | 30 | 2 | **2** | Lien point-à-point (routeurs) |

---

## Partie 3 — L'Algorithme de Calcul de Sous-réseau

### 3.1 Présentation Formelle

```
╔══════════════════════════════════════════════════════════════════╗
║         ALGORITHME DE CALCUL DE SOUS-RÉSEAU                      ║
║                                                                  ║
║  ENTRÉE : adresse IP (32 bits), masque (CIDR ou décimal)         ║
║                                                                  ║
║  ÉTAPE 1 : Convertir IP et masque en binaire (32 bits)           ║
║                                                                  ║
║  ÉTAPE 2 : AND bit à bit → Adresse réseau                        ║
║            IP AND masque = adresse_réseau                        ║
║                                                                  ║
║  ÉTAPE 3 : NOT bit à bit du masque → Wildcard (masque inversé)   ║
║            NOT(masque) = wildcard                                ║
║                                                                  ║
║  ÉTAPE 4 : OR bit à bit → Adresse broadcast                      ║
║            adresse_réseau OR wildcard = broadcast                ║
║                                                                  ║
║  ÉTAPE 5 : Calculer la plage et le nombre d'hôtes                ║
║            Première IP hôte = adresse_réseau + 1                 ║
║            Dernière IP hôte = broadcast − 1                      ║
║            Nombre d'hôtes   = 2ⁿ − 2  (n = bits hôte)          ║
║                                                                  ║
║  SORTIE : réseau, broadcast, première IP, dernière IP, nb hôtes  ║
╚══════════════════════════════════════════════════════════════════╝
```

### 3.2 Lien Avec S3 — Rappel des Opérations Booléennes Bit à Bit

En S3, vous avez appris AND, OR, NOT sur des variables booléennes (0 ou 1). Ici, on applique **les mêmes opérations sur 32 bits simultanément**, position par position :

```
  AND bit à bit de deux octets :
  IP     : 1 1 0 0 0 0 0 1
  Masque : 1 1 1 1 1 1 1 1
  AND    : 1 1 0 0 0 0 0 1   ← chaque position : 1 AND 1 = 1, 0 AND 1 = 0

  NOT bit à bit d'un octet de masque :
  Masque : 1 1 1 1 0 0 0 0
  NOT    : 0 0 0 0 1 1 1 1   ← chaque bit est inversé
```

> 💡 **C'est exactement la même logique booléenne que la porte logique vue en S3 — appliquée 32 fois en parallèle.** Le processeur de votre machine exécute précisément cette opération lors du calcul de sous-réseau.

---

## Partie 4 — Exemple Complet Guidé Pas à Pas

### Exemple 1 — IP : 192.168.1.74 / 24

**Étape 1 — Conversion en binaire :**

```
  IP     : 192      . 168      .   1      .  74
  Binaire: 11000000 . 10101000 . 00000001 . 01001010

  Masque /24 → 24 bits à 1 :
  Binaire: 11111111 . 11111111 . 11111111 . 00000000
  Décimal: 255      . 255      . 255      .   0
```

**Étape 2 — AND bit à bit → Adresse réseau :**

```
  IP     : 11000000 . 10101000 . 00000001 . 01001010
  Masque : 11111111 . 11111111 . 11111111 . 00000000
  AND    : 11000000 . 10101000 . 00000001 . 00000000
         = 192      . 168      .   1      .   0
  → Adresse réseau : 192.168.1.0
```

> 💡 **Observation :** Pour les 3 premiers octets, masque = 11111111 → AND donne toujours l'IP d'origine. Seul le dernier octet avec masque = 00000000 → AND donne 0. C'est pourquoi les /24 semblent simples : seul le dernier octet change.

**Étape 3 — NOT(masque) → Wildcard :**

```
  Masque  : 11111111 . 11111111 . 11111111 . 00000000
  NOT     : 00000000 . 00000000 . 00000000 . 11111111
  Décimal :    0     .    0     .    0     .   255
  → Wildcard : 0.0.0.255
```

**Étape 4 — OR bit à bit → Broadcast :**

```
  Réseau : 11000000 . 10101000 . 00000001 . 00000000
  Wildcard:00000000 . 00000000 . 00000000 . 11111111
  OR     : 11000000 . 10101000 . 00000001 . 11111111
         = 192      . 168      .   1      .   255
  → Broadcast : 192.168.1.255
```

**Étape 5 — Plage d'hôtes et nombre d'hôtes :**

```
  Bits hôte : 32 − 24 = 8 bits
  Nombre d'hôtes = 2⁸ − 2 = 256 − 2 = 254 hôtes

  Première IP hôte : 192.168.1.0 + 1 = 192.168.1.1
  Dernière IP hôte : 192.168.1.255 − 1 = 192.168.1.254
```

**Récapitulatif :**

| **Élément** | **Valeur** |
|---|---|
| Adresse IP | 192.168.1.74 |
| Masque | 255.255.255.0 (/24) |
| **Adresse réseau** | **192.168.1.0** |
| **Broadcast** | **192.168.1.255** |
| **Première IP hôte** | **192.168.1.1** |
| **Dernière IP hôte** | **192.168.1.254** |
| **Nombre d'hôtes** | **254** |

---

### Exemple 2 — IP : 172.16.50.130 / 26 *(masque non-standard)*

**Étape 1 — Conversion en binaire :**

```
  IP     : 172      . 16       .  50      .  130
  Binaire: 10101100 . 00010000 . 00110010 . 10000010

  Masque /26 → 26 bits à 1, 6 bits à 0 :
  Binaire: 11111111 . 11111111 . 11111111 . 11000000
  Décimal: 255      . 255      . 255      .  192
```

**Étape 2 — AND bit à bit (seul le 4ème octet diffère) :**

```
  4ème octet IP     : 1 0 0 0 0 0 1 0  (= 130)
  4ème octet masque : 1 1 0 0 0 0 0 0  (= 192)
  AND               : 1 0 0 0 0 0 0 0  (= 128)

  → Adresse réseau : 172.16.50.128
```

> ⚠️ **Ce n'est PAS .0 !** Avec un /26, le réseau commence à .128, pas à .0. C'est pourquoi l'intuition échoue ici.

**Étape 3 — NOT(masque) → Wildcard :**

```
  4ème octet masque : 1 1 0 0 0 0 0 0  (= 192)
  NOT               : 0 0 1 1 1 1 1 1  (= 63)
  → Wildcard : 0.0.0.63
```

**Étape 4 — OR bit à bit → Broadcast :**

```
  4ème octet réseau   : 1 0 0 0 0 0 0 0  (= 128)
  4ème octet wildcard : 0 0 1 1 1 1 1 1  (= 63)
  OR                  : 1 0 1 1 1 1 1 1  (= 191)

  → Broadcast : 172.16.50.191
```

**Étape 5 — Plage d'hôtes :**

```
  Bits hôte = 32 − 26 = 6 bits
  Nombre d'hôtes = 2⁶ − 2 = 64 − 2 = 62 hôtes

  Première IP : 172.16.50.129
  Dernière IP : 172.16.50.190
```

**Récapitulatif :**

| **Élément** | **Valeur** |
|---|---|
| Adresse IP | 172.16.50.130 |
| Masque | 255.255.255.192 (/26) |
| **Adresse réseau** | **172.16.50.128** |
| **Broadcast** | **172.16.50.191** |
| **Première IP hôte** | **172.16.50.129** |
| **Dernière IP hôte** | **172.16.50.190** |
| **Nombre d'hôtes** | **62** |

---

### Exemple 3 — IP : 10.0.4.200 / 20 *(masque traversant le 3ème octet)*

**Étape 1 — Conversion en binaire :**

```
  IP     : 10       .   0      .   4      .  200
  Binaire: 00001010 . 00000000 . 00000100 . 11001000

  Masque /20 → 20 bits à 1, 12 bits à 0 :
  Bits :   [11111111] [11111111] [11110000] [00000000]
  Décimal:    255        255        240         0
```

> ⚠️ **La frontière réseau/hôte passe à l'intérieur du 3ème octet.** Le 3ème octet du masque est 240 = 11110000 — les 4 premiers bits sont réseau, les 4 derniers sont hôte.

**Étape 2 — AND bit à bit :**

```
  3ème octet IP     : 0 0 0 0 0 1 0 0  (=  4)
  3ème octet masque : 1 1 1 1 0 0 0 0  (= 240)
  AND               : 0 0 0 0 0 0 0 0  (=  0)

  4ème octet IP     : 1 1 0 0 1 0 0 0  (= 200)
  4ème octet masque : 0 0 0 0 0 0 0 0  (=   0)
  AND               : 0 0 0 0 0 0 0 0  (=   0)

  → Adresse réseau : 10.0.0.0
```

**Étape 3 — Wildcard :**

```
  NOT(masque) : 00000000 . 00000000 . 00001111 . 11111111
  Décimal     :    0     .    0     .    15    .   255
  → Wildcard : 0.0.15.255
```

**Étape 4 — Broadcast :**

```
  3ème octet réseau   : 0 0 0 0 0 0 0 0  (=  0)
  3ème octet wildcard : 0 0 0 0 1 1 1 1  (= 15)
  OR                  : 0 0 0 0 1 1 1 1  (= 15)

  4ème octet : 0 OR 11111111 = 11111111 = 255

  → Broadcast : 10.0.15.255
```

**Étape 5 — Plage d'hôtes :**

```
  Bits hôte = 32 − 20 = 12 bits
  Nombre d'hôtes = 2¹² − 2 = 4096 − 2 = 4094 hôtes

  Première IP : 10.0.0.1
  Dernière IP : 10.0.15.254
```

---

## Partie 5 — Algorithme de Comparaison : "Même Réseau ou Pas ?"

Pour déterminer si deux hôtes sont sur le même sous-réseau, il suffit de comparer leurs adresses réseau :

```
╔══════════════════════════════════════════════════════════════════╗
║     ALGORITHME DE COMPARAISON DE SOUS-RÉSEAUX                    ║
║                                                                  ║
║  ENTRÉE : IP_A, IP_B, masque commun                              ║
║                                                                  ║
║  ÉTAPE 1 : réseau_A = IP_A AND masque                            ║
║  ÉTAPE 2 : réseau_B = IP_B AND masque                            ║
║  ÉTAPE 3 : Si réseau_A = réseau_B → MÊME RÉSEAU (pas de routeur) ║
║            Si réseau_A ≠ réseau_B → RÉSEAUX DIFFÉRENTS (routeur) ║
║                                                                  ║
║  SORTIE : OUI / NON + adresse réseau de chaque hôte              ║
╚══════════════════════════════════════════════════════════════════╝
```

**Optimisation pratique :** Pour les /24 et les masques qui tombent sur des octets entiers, la comparaison peut se faire octet par octet en décimal, sans passer par le binaire. Mais **dès qu'un octet de masque est ni 0 ni 255**, il faut obligatoirement passer par le binaire pour cet octet.

---

## Partie 6 — Exercices Guidés

### Grille de Calcul Vierge — À Utiliser Pour Chaque Exercice

```
═══════════════════════════════════════════════════════════════════
EXERCICE N° ___
IP : ___.___.___.___  /___   Masque décimal : ___.___.___.___ 
═══════════════════════════════════════════════════════════════════

ÉTAPE 1 — CONVERSION EN BINAIRE
────────────────────────────────────────────────────────────────
IP     : [________] [________] [________] [________]
Masque : [________] [________] [________] [________]

ÉTAPE 2 — AND BIT À BIT (adresse réseau)
────────────────────────────────────────────────────────────────
IP     : [________] [________] [________] [________]
Masque : [________] [________] [________] [________]
AND    : [________] [________] [________] [________]
Réseau décimal : ___ . ___ . ___ . ___

ÉTAPE 3 — NOT(masque) → wildcard
────────────────────────────────────────────────────────────────
NOT masque : [________] [________] [________] [________]
Wildcard décimal : ___ . ___ . ___ . ___

ÉTAPE 4 — OR BIT À BIT (broadcast)
────────────────────────────────────────────────────────────────
Réseau   : [________] [________] [________] [________]
Wildcard : [________] [________] [________] [________]
OR       : [________] [________] [________] [________]
Broadcast décimal : ___ . ___ . ___ . ___

ÉTAPE 5 — RÉSULTATS
────────────────────────────────────────────────────────────────
Bits hôte          : 32 − ___ = ___ bits
Nombre d'hôtes     : 2^___ − 2 = ___ hôtes
Première IP hôte   : ___ . ___ . ___ . ___
Dernière IP hôte   : ___ . ___ . ___ . ___
═══════════════════════════════════════════════════════════════════
```

### Série 1 — Exercices Progressifs

**Exercice 1.1** — `10.0.0.50 / 8`
*(Guidage : le masque est 255.0.0.0 — seul le premier octet est réseau)*

**Exercice 1.2** — `172.16.200.14 / 16`
*(Guidage : le masque est 255.255.0.0 — les deux premiers octets sont réseau)*

**Exercice 1.3** — `192.168.5.200 / 24`
*(Guidage : masque classique 255.255.255.0)*

**Exercice 1.4** — `192.168.1.100 / 25`
*(Attention : la frontière passe dans le dernier octet !)*

**Exercice 1.5** — `192.168.10.67 / 28`
*(Contre-exemple de l'activité découverte — vérifier le résultat de la paire 4)*

**Exercice 1.6** — `10.10.0.150 / 20`
*(La frontière réseau/hôte passe dans le 3ème octet)*

### Série 2 — Comparaisons de Sous-réseaux

Pour chaque paire, déterminez si les deux machines sont sur le même réseau. Montrez le calcul.

**Exercice 2.1** — `192.168.1.50/24` et `192.168.1.200/24`

**Exercice 2.2** — `192.168.10.65/26` et `192.168.10.130/26`
*(La paire 3 de l'activité — vérifier le résultat intuitif)*

**Exercice 2.3** — `10.10.0.1/20` et `10.10.15.200/20`

**Exercice 2.4** — `172.16.0.50/28` et `172.16.0.60/28`

---

## Vocabulaire Clé à Maîtriser pour l'Examen

| **Terme** | **Définition** |
|---|---|
| **Masque de sous-réseau** | Nombre de 32 bits composé de 1 continus puis de 0 continus, définissant la frontière réseau/hôte dans une adresse IP |
| **Notation CIDR** | Nombre de bits à 1 du masque, précédé de `/` (ex : /24) |
| **Adresse réseau** | Résultat du AND bit à bit entre l'IP et le masque — premier identifiant du sous-réseau (non attribuable à un hôte) |
| **Broadcast** | Adresse de diffusion — résultat du OR entre l'adresse réseau et le wildcard (non attribuable à un hôte) |
| **Wildcard (masque inversé)** | NOT du masque — bits à 1 indiquant la partie hôte |
| **Plage d'hôtes** | Ensemble des adresses entre réseau+1 et broadcast−1 |
| **Nombre d'hôtes** | 2ⁿ − 2, où n = nombre de bits hôte (−2 pour réseau et broadcast) |
| **AND bit à bit** | Opération booléenne AND appliquée position par position sur deux nombres binaires de 32 bits |
| **Lien point-à-point** | Connexion directe entre deux routeurs — utilise /30 (2 hôtes utilisables) |
| **RFC 1918** | Standard définissant les plages d'adresses IP privées : 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 |

---

## ANNEXE A — Grille Binaire 32 Cases

```
   IP      [ ][ ][ ][ ][ ][ ][ ][ ] . [ ][ ][ ][ ][ ][ ][ ][ ] . [ ][ ][ ][ ][ ][ ][ ][ ] . [ ][ ][ ][ ][ ][ ][ ][ ]
            ←─── octet 1 ──────────→   ←─── octet 2 ──────────→   ←─── octet 3 ──────────→   ←─── octet 4 ──────────→
   Masque  [ ][ ][ ][ ][ ][ ][ ][ ] . [ ][ ][ ][ ][ ][ ][ ][ ] . [ ][ ][ ][ ][ ][ ][ ][ ] . [ ][ ][ ][ ][ ][ ][ ][ ]
   AND     [ ][ ][ ][ ][ ][ ][ ][ ] . [ ][ ][ ][ ][ ][ ][ ][ ] . [ ][ ][ ][ ][ ][ ][ ][ ] . [ ][ ][ ][ ][ ][ ][ ][ ]
   NOT(M)  [ ][ ][ ][ ][ ][ ][ ][ ] . [ ][ ][ ][ ][ ][ ][ ][ ] . [ ][ ][ ][ ][ ][ ][ ][ ] . [ ][ ][ ][ ][ ][ ][ ][ ]
   OR      [ ][ ][ ][ ][ ][ ][ ][ ] . [ ][ ][ ][ ][ ][ ][ ][ ] . [ ][ ][ ][ ][ ][ ][ ][ ] . [ ][ ][ ][ ][ ][ ][ ][ ]
```

---

## ANNEXE B — Valeurs Binaires des Octets de Masque Courants

| **Décimal** | **Binaire** | **Correspond à** |
|---|---|---|
| 0 | `00000000` | Octet entièrement hôte |
| 128 | `10000000` | 1 bit réseau dans l'octet |
| 192 | `11000000` | 2 bits réseau dans l'octet |
| 224 | `11100000` | 3 bits réseau dans l'octet |
| 240 | `11110000` | 4 bits réseau dans l'octet |
| 248 | `11111000` | 5 bits réseau dans l'octet |
| 252 | `11111100` | 6 bits réseau dans l'octet |
| 254 | `11111110` | 7 bits réseau dans l'octet |
| 255 | `11111111` | Octet entièrement réseau |


---


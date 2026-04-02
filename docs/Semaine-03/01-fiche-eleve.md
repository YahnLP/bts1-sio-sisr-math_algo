---
author: YLP
title: 📖 FICHE DE COURS ÉLÈVE
---

# 📖 FICHE DE COURS ÉLÈVE
## Algèbre de Boole · AND · OR · NOT · XOR · Tables de Vérité · Logique Pare-feu

*Version 1.0 — BTS SIO SISR — Année 1 — Semaine 3*

---

# Partie 1 — Variables Booléennes et Fondements

### 1.1 Qu'est-ce qu'une Variable Booléenne ?

Une **variable booléenne** ne peut prendre que **deux valeurs** :

```
┌─────────────────────────────────────────────────────────────┐
│              LES DEUX VALEURS BOOLÉENNES                    │
│                                                             │
│    VRAI  =  1  =  TRUE  =  état "activé"                    │
│    FAUX  =  0  =  FALSE =  état "désactivé"                 │
│                                                             │
│    Exemples :                                               │
│    • Le port 443 est-il ouvert ?       → OUI (1) ou NON (0) │
│    • L'IP est-elle dans le réseau ?    → OUI (1) ou NON (0) │
│    • Le protocole est-il TCP ?         → OUI (1) ou NON (0) │
│    • L'utilisateur est-il authentifié? → OUI (1) ou NON (0) │
└─────────────────────────────────────────────────────────────┘
```
*[Illustration : Un interrupteur lumineux en deux états côte à côte. À gauche : interrupteur OFF, ampoule éteinte, label "FAUX = 0". À droite : interrupteur ON, ampoule allumée, label "VRAI = 1". Sous les deux images, la légende : "C'est le même principe que le transistor vu en S1."]*

> 💡 **Lien avec S1 :** Un transistor est une variable booléenne physique. Ouvert = 0, fermé = 1. Tout ce que nous allons faire ici se déroule au niveau des transistors dans votre CPU.

### 1.2 Notations — Mathématique vs. Informatique

Les opérateurs booléens s'écrivent différemment selon le contexte :

| **Opérateur** | **Nom** | **Notation math.** | **Notation info.** | **En langage naturel** |
|---|---|---|---|---|
| AND | ET logique | A ∧ B | `A && B` ou `A AND B` | "A **et** B" |
| OR | OU logique | A ∨ B | `A \|\| B` ou `A OR B` | "A **ou** B" |
| NOT | NON logique | ¬A ou Ā | `!A` ou `NOT A` | "**non** A" |
| XOR | OU exclusif | A ⊕ B | `A ^ B` ou `A XOR B` | "A **ou** B, **pas les deux**" |

> ⚠️ **Attention à la notation `^` :** En Python et en C, `^` signifie XOR. En Bash, `**` signifie la puissance. Vérifiez toujours le langage utilisé.

---

## Partie 2 — Les Quatre Opérateurs Fondamentaux

### 2.1 AND — Le ET Logique

**Définition :** AND renvoie VRAI uniquement si **toutes** les entrées sont VRAIES.

```
  Symbole électronique :          A ──┐
                                      ├──[AND]── S
                                  B ──┘

  Règle mnémotechnique : "AND = le maillon le plus faible"
  → Il suffit d'UN seul FAUX pour que le résultat soit FAUX.
```
*[Illustration : Schéma d'une porte AND (forme en D arrondi à droite) avec deux entrées A et B à gauche et une sortie S à droite. Sous le schéma, le symbole électronique standard IEC (rectangle avec le label "&").]*

**Table de vérité AND :**

| **A** | **B** | **A AND B** |
|---|---|---|
| 0 | 0 | **0** |
| 0 | 1 | **0** |
| 1 | 0 | **0** |
| 1 | 1 | **1** ← seul cas VRAI |

> 💡 **Application pare-feu :** `ACCEPT si proto=TCP AND port=443` → il faut les DEUX conditions vraies. Si le protocole est UDP, le paquet est refusé même si le port est 443.

---

### 2.2 OR — Le OU Logique (Inclusif)

**Définition :** OR renvoie VRAI si **au moins une** entrée est VRAIE.

```
  Symbole électronique :          A ──┐
                                      ├──[OR]── S
                                  B ──┘

  Règle mnémotechnique : "OR = le maillon le plus fort"
  → Il suffit d'UN seul VRAI pour que le résultat soit VRAI.
```
*[Illustration : Schéma d'une porte OR (forme en croissant pointu à droite) avec deux entrées A et B et une sortie S. Sous le schéma, le symbole IEC (rectangle avec le label "≥1").]*

**Table de vérité OR :**

| **A** | **B** | **A OR B** |
|---|---|---|
| 0 | 0 | **0** ← seul cas FAUX |
| 0 | 1 | **1** |
| 1 | 0 | **1** |
| 1 | 1 | **1** |

> ⚠️ **OR est inclusif :** Si A=1 ET B=1, OR donne 1. Les deux peuvent être vrais simultanément. C'est différent du "ou" courant en français qui est souvent exclusif.

> 💡 **Application pare-feu :** `ACCEPT si port=80 OR port=443` → accepter le trafic web HTTP ou HTTPS. Un paquet sur le port 80 passe, sur le port 443 passe, les deux passent.

---

### 2.3 NOT — Le NON Logique (Inverseur)

**Définition :** NOT **inverse** la valeur de son entrée.

```
  Symbole électronique :    A ──[NOT]──○── S
                                       ↑
                                 cercle = inversion

  Règle mnémotechnique : "NOT = le miroir"
  → VRAI devient FAUX. FAUX devient VRAI.
```
*[Illustration : Schéma d'un inverseur (triangle pointé vers la droite avec un petit cercle à la sortie). À gauche de la porte : entrée A. À droite du cercle : sortie S = Ā. Symbole IEC : rectangle avec label "1" et cercle à la sortie.]*

**Table de vérité NOT :**

| **A** | **NOT A (Ā)** |
|---|---|
| 0 | **1** |
| 1 | **0** |

> 💡 **Application pare-feu :** `BLOCK si NOT(proto=TCP)` → bloquer tout ce qui n'est pas TCP. Équivaut à "autoriser TCP uniquement".

---

### 2.4 XOR — Le OU Exclusif

**Définition :** XOR renvoie VRAI si les entrées sont **différentes** (exactement l'une est vraie, pas les deux).

```
  Symbole électronique :          A ──┐
                                      ├──[XOR]── S
                                  B ──┘

  Règle mnémotechnique : "XOR = différence"
  → Vrai si A ≠ B. Faux si A = B (tous les deux pareils).
```
*[Illustration : Schéma d'une porte XOR (comme OR mais avec une ligne incurvée supplémentaire à l'entrée). Symbole IEC : rectangle avec label "=1".]*

**Table de vérité XOR :**

| **A** | **B** | **A XOR B** |
|---|---|---|
| 0 | 0 | **0** ← même (tous les deux faux) |
| 0 | 1 | **1** ← différents |
| 1 | 0 | **1** ← différents |
| 1 | 1 | **0** ← même (tous les deux vrais) |

> 💡 **Usage informatique du XOR :** Le XOR est très utilisé en cryptographie (chiffrement de flux) et en contrôle d'erreurs (checksum, parité). Si `A XOR A = 0` toujours, alors XOR avec la même clé deux fois donne le message original — principe du chiffrement symétrique basique.

---

### 2.5 Tableau Récapitulatif — Les 4 Opérateurs

```
╔═══════╦═══════╦═══════╦════════╦═══════╦═════════╗
║   A   ║   B   ║  AND  ║   OR   ║  XOR  ║  NOT A  ║
╠═══════╬═══════╬═══════╬════════╬═══════╬═════════╣
║   0   ║   0   ║   0   ║   0    ║   0   ║    1    ║
║   0   ║   1   ║   0   ║   1    ║   1   ║    1    ║
║   1   ║   0   ║   0   ║   1    ║   1   ║    0    ║
║   1   ║   1   ║   1   ║   1    ║   0   ║    0    ║
╚═══════╩═══════╩═══════╩════════╩═══════╩═════════╝

  AND : 1 seul cas à 1  (ligne 4)
  OR  : 1 seul cas à 0  (ligne 1)
  XOR : les cas "différents" sont à 1 (lignes 2 et 3)
  NOT : inverse A (indépendant de B)
```
*[Illustration : Ce tableau récapitulatif avec chaque colonne dans une couleur différente : AND en rouge (peu de VRAI), OR en vert (beaucoup de VRAI), XOR en orange (en diagonale), NOT en bleu (simple inversion).]*

---

## Partie 3 — Construire une Table de Vérité : La Méthode

### 3.1 Méthode Colonne par Colonne

Pour une expression composée, **ne jamais calculer tout en une fois**. Procéder par étapes :

```
  EXPRESSION : S = (A AND B) OR (NOT A)

  ÉTAPE 1 — Créer les colonnes nécessaires :
  | A | B | NOT A | A AND B | (A AND B) OR (NOT A) |

  ÉTAPE 2 — Remplir les colonnes d'entrée (toutes les combinaisons)
  Pour 2 variables : 2² = 4 lignes (00, 01, 10, 11)
  Pour 3 variables : 2³ = 8 lignes (000, 001, 010, 011, 100, 101, 110, 111)

  ÉTAPE 3 — Calculer NOT A :
  | A | B | NOT A |
  | 0 | 0 |   1   |
  | 0 | 1 |   1   |
  | 1 | 0 |   0   |
  | 1 | 1 |   0   |

  ÉTAPE 4 — Calculer A AND B :
  | A | B | NOT A | A AND B |
  | 0 | 0 |   1   |    0    |
  | 0 | 1 |   1   |    0    |
  | 1 | 0 |   0   |    0    |
  | 1 | 1 |   0   |    1    |

  ÉTAPE 5 — Calculer le résultat final (OR des deux colonnes) :
  | A | B | NOT A | A AND B | S = (A AND B) OR (NOT A) |
  | 0 | 0 |   1   |    0    |          1               |
  | 0 | 1 |   1   |    0    |          1               |
  | 1 | 0 |   0   |    0    |          0               |
  | 1 | 1 |   0   |    1    |          1               |
```

> 💡 **Règle du nombre de lignes :** n variables → 2ⁿ lignes dans la table.
> 1 variable : 2 lignes / 2 variables : 4 lignes / 3 variables : 8 lignes / 4 variables : 16 lignes

### 3.2 Comment Énumérer Toutes les Combinaisons

La méthode infaillible : **compter en binaire** de 0 jusqu'à 2ⁿ - 1.

```
  Pour 3 variables A, B, C :

  | A | B | C |   ← lire chaque ligne comme un nombre binaire
  | 0 | 0 | 0 |   ← 000 = 0
  | 0 | 0 | 1 |   ← 001 = 1
  | 0 | 1 | 0 |   ← 010 = 2
  | 0 | 1 | 1 |   ← 011 = 3
  | 1 | 0 | 0 |   ← 100 = 4
  | 1 | 0 | 1 |   ← 101 = 5
  | 1 | 1 | 0 |   ← 110 = 6
  | 1 | 1 | 1 |   ← 111 = 7

  → La dernière colonne (C) alterne 0,1,0,1,0,1,0,1
  → La colonne du milieu (B) alterne 0,0,1,1,0,0,1,1
  → La première colonne (A) alterne 0,0,0,0,1,1,1,1
```

---

## Partie 4 — Lois Fondamentales de Boole

### 4.1 Les Lois Simples

| **Loi** | **AND** | **OR** |
|---|---|---|
| **Identité** | A AND 1 = A | A OR 0 = A |
| **Domination** | A AND 0 = 0 | A OR 1 = 1 |
| **Idempotence** | A AND A = A | A OR A = A |
| **Complémentation** | A AND (NOT A) = 0 | A OR (NOT A) = 1 |
| **Double négation** | NOT(NOT A) = A | — |
| **Commutativité** | A AND B = B AND A | A OR B = B OR A |

> 💡 **Intérêt pratique :** Ces lois permettent de **simplifier des expressions** pour écrire des règles pare-feu plus concises ou des conditions de script plus lisibles.

### 4.2 Les Lois de De Morgan — Incontournables

```
╔════════════════════════════════════════════════════════════════╗
║              LOIS DE DE MORGAN                                 ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║  NOT (A AND B)  =  (NOT A) OR  (NOT B)                        ║
║                                                                ║
║  NOT (A OR  B)  =  (NOT A) AND (NOT B)                        ║
║                                                                ║
║  En résumé : quand on "entre" un NOT dans une parenthèse,     ║
║  AND devient OR et OR devient AND.                            ║
╚════════════════════════════════════════════════════════════════╝
```

**Vérification par table de vérité :**

| **A** | **B** | **A AND B** | **NOT(A AND B)** | **NOT A** | **NOT B** | **(NOT A) OR (NOT B)** |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | **1** | 1 | 1 | **1** |
| 0 | 1 | 0 | **1** | 1 | 0 | **1** |
| 1 | 0 | 0 | **1** | 0 | 1 | **1** |
| 1 | 1 | 1 | **0** | 0 | 0 | **0** |

Les colonnes `NOT(A AND B)` et `(NOT A) OR (NOT B)` sont identiques → la loi est vérifiée. ✓

**Application directe en pare-feu :**

```
  Règle originale :
  BLOCK si NOT(proto=TCP AND port=443)

  Par De Morgan :
  BLOCK si (NOT proto=TCP) OR (NOT port=443)
  = BLOCK si proto≠TCP  OU  port≠443

  Les deux formulations sont logiquement équivalentes.
  La deuxième est souvent plus lisible dans un outil de configuration.
```

---

## Partie 5 — Application : La Logique d'un Pare-feu

### 5.1 Rappel : Qu'est-ce qu'un Pare-feu ?

Un **pare-feu** (firewall) est un système qui filtre les paquets réseau selon des règles. Chaque règle est fondamentalement une **expression booléenne** : si les conditions sont vraies, le paquet est accepté (ACCEPT) ou rejeté (DROP/REJECT).

### 5.2 Structure d'une Règle de Pare-feu

```
┌────────────────────────────────────────────────────────────────────┐
│              ANATOMIE D'UNE RÈGLE DE PARE-FEU                      │
│                                                                    │
│  ACTION  si  CONDITION_1  ET/OU  CONDITION_2  ET/OU  CONDITION_N   │
│                                                                    │
│  Exemple iptables :                                                │
│  iptables -A INPUT -p tcp --dport 443 -s 192.168.1.0/24 -j ACCEPT  │
│           │        │       │           │                  │        │
│         Règle    proto   port        source            Action      │
│         entrée   TCP     443       réseau autorisé    ACCEPTER     │
│                                                                    │
│  Traduction booléenne :                                            │
│  S = (proto = TCP) AND (port_dest = 443) AND (IP ∈ 192.168.1.0/24) │
│  Si S = 1 → ACCEPT                                                 │
│  Si S = 0 → règle suivante (ou DROP par défaut)                    │
└────────────────────────────────────────────────────────────────────┘
```
*[Illustration : La commande iptables décomposée avec des accolades colorées sous chaque paramètre : en bleu le protocole, en vert le port, en orange l'adresse source, en rouge l'action. Sous la commande, l'expression booléenne équivalente avec les mêmes couleurs.]*

### 5.3 Le Principe "DENY by Default"

La règle d'or de la sécurité réseau est :

```
╔══════════════════════════════════════════════════════════════════╗
║           TOUT CE QUI N'EST PAS EXPLICITEMENT AUTORISÉ          ║
║                       EST INTERDIT                               ║
╚══════════════════════════════════════════════════════════════════╝

  En Boole :
  Résultat_final = Règle_1 OR Règle_2 OR Règle_3 OR ... OR Règle_N
  Si Résultat_final = 0 → DROP (par défaut)

  Ou plus précisément : on parcourt les règles dans l'ordre.
  La PREMIÈRE règle qui correspond (=1) s'applique.
  Si AUCUNE règle ne correspond → politique par défaut = DROP.
```

### 5.4 Exemple Complet — Politique de Filtrage d'un Serveur Web

**Scénario :** Un serveur web doit :
- Accepter les connexions HTTPS (TCP/443) depuis n'importe quelle IP
- Accepter les connexions SSH (TCP/22) uniquement depuis le réseau d'administration (192.168.10.0/24)
- Refuser tout le reste

**Variables :**
- P = protocole est TCP (1=oui, 0=non)
- H = port destination est 443 (HTTPS)
- S = port destination est 22 (SSH)
- R = IP source appartient à 192.168.10.0/24 (réseau admin)

**Règles en booléen :**
```
  Règle 1 — HTTPS public   : R1 = P AND H
  Règle 2 — SSH admin      : R2 = P AND S AND R
  Politique finale         : ACCEPT = R1 OR R2
  (si ACCEPT = 0 → DROP)
```

**Table de vérité pour quelques cas représentatifs :**

| **Paquet** | **P** | **H** | **S** | **R** | **R1=P∧H** | **R2=P∧S∧R** | **ACCEPT=R1∨R2** | **Action** |
|---|---|---|---|---|---|---|---|---|
| HTTPS depuis Internet | 1 | 1 | 0 | 0 | **1** | 0 | **1** | ✅ ACCEPT |
| SSH depuis admin | 1 | 0 | 1 | 1 | 0 | **1** | **1** | ✅ ACCEPT |
| SSH depuis Internet | 1 | 0 | 1 | 0 | 0 | 0 | **0** | ❌ DROP |
| HTTP (port 80) | 1 | 0 | 0 | 0 | 0 | 0 | **0** | ❌ DROP |
| UDP depuis admin | 0 | 0 | 0 | 1 | 0 | 0 | **0** | ❌ DROP |

> 💡 **Lecture de la table :** Le cas "SSH depuis Internet" est DROP malgré un protocole TCP et un port SSH valides — parce que R=0 (IP non autorisée). C'est exactement la logique AND : toutes les conditions doivent être vraies.

### 5.5 Écriture en iptables — Correspondance Booléenne

```bash
# Règle 1 : HTTPS depuis n'importe quelle IP
# Booléen : P=1 AND H=1
iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# Règle 2 : SSH depuis réseau admin uniquement
# Booléen : P=1 AND S=1 AND R=1
iptables -A INPUT -p tcp --dport 22 -s 192.168.10.0/24 -j ACCEPT

# Politique par défaut : tout refuser (DENY by default)
# Booléen : si aucune règle précédente n'a matché → DROP
iptables -P INPUT DROP
```

---

## Partie 6 — Exercices Guidés

### Série 1 — Tables Simples à Compléter

**Exercice 1.1 — Expression : S = A AND (NOT B)**

| **A** | **B** | **NOT B** | **S = A AND (NOT B)** |
|---|---|---|---|
| 0 | 0 | | |
| 0 | 1 | | |
| 1 | 0 | | |
| 1 | 1 | | |

**Exercice 1.2 — Expression : S = (NOT A) OR B**

| **A** | **B** | **NOT A** | **S = (NOT A) OR B** |
|---|---|---|---|
| 0 | 0 | | |
| 0 | 1 | | |
| 1 | 0 | | |
| 1 | 1 | | |

**Exercice 1.3 — Expression : S = A XOR (NOT B)**

| **A** | **B** | **NOT B** | **S = A XOR (NOT B)** |
|---|---|---|---|
| 0 | 0 | | |
| 0 | 1 | | |
| 1 | 0 | | |
| 1 | 1 | | |

---

### Série 2 — Expressions Composées à 3 Variables

**Exercice 2.1 — Expression : S = (A AND B) AND (NOT C)**
*(représente : accepter si TCP ET port correct ET pas sur liste noire)*

| **A** | **B** | **C** | **A AND B** | **NOT C** | **S** |
|---|---|---|---|---|---|
| 0 | 0 | 0 | | | |
| 0 | 0 | 1 | | | |
| 0 | 1 | 0 | | | |
| 0 | 1 | 1 | | | |
| 1 | 0 | 0 | | | |
| 1 | 0 | 1 | | | |
| 1 | 1 | 0 | | | |
| 1 | 1 | 1 | | | |

**Exercice 2.2 — Traduction d'une règle réseau**

Traduisez cette règle pare-feu en expression booléenne, puis construisez sa table de vérité pour les combinaisons données :

> *"ACCEPTER si le protocole est TCP ET (le port est 80 OU le port est 443)"*

Variables : T = protocole TCP, H = port 80 (HTTP), S = port 443 (HTTPS)

| **T (TCP ?)** | **H (port 80 ?)** | **S (port 443 ?)** | **Expression (à écrire)** | **Action** |
|---|---|---|---|---|
| 1 | 1 | 0 | | |
| 1 | 0 | 1 | | |
| 1 | 0 | 0 | | |
| 0 | 1 | 0 | | |
| 0 | 0 | 0 | | |

---

## Vocabulaire Clé à Maîtriser pour l'Examen

| **Terme** | **Définition** |
|---|---|
| **Variable booléenne** | Variable ne pouvant prendre que les valeurs 0 (FAUX) ou 1 (VRAI) |
| **AND (∧, &&)** | Opérateur ET logique — VRAI uniquement si toutes les entrées sont VRAIES |
| **OR (∨, \|\|)** | Opérateur OU logique inclusif — VRAI si au moins une entrée est VRAIE |
| **NOT (¬, !)** | Opérateur NON — inverse la valeur de son entrée |
| **XOR (⊕, ^)** | Opérateur OU exclusif — VRAI si les entrées sont différentes |
| **Table de vérité** | Tableau listant tous les résultats possibles d'une expression pour toutes les combinaisons d'entrées |
| **Porte logique** | Composant électronique réalisant physiquement un opérateur booléen |
| **Loi de De Morgan** | NOT(A AND B) = (NOT A) OR (NOT B) — et son symétrique avec OR |
| **DENY by default** | Politique de sécurité : tout trafic non explicitement autorisé est rejeté |
| **ACL** | Access Control List — liste de règles définissant les autorisations d'accès réseau |
| **iptables** | Outil Linux de configuration du pare-feu netfilter — basé sur des règles booléennes |
| **Idempotence** | A AND A = A — appliquer deux fois le même opérateur donne le même résultat |


---

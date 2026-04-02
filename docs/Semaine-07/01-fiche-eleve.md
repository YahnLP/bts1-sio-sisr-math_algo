---
author: YLP
title: 📖 FICHE DE COURS
---

## 📖 FICHE DE COURS
### Structures Conditionnelles · SI...ALORS...SINON · Appartenance à un Sous-réseau

*Version 1.0 — BTS SIO SISR — Année 1 — Semaine 7*
> **Prérequis :** S4 (AND masque), S6 (pseudo-code, types, ValiderIPv4)

---

## Partie 1 — Les Trois Formes de la Structure Conditionnelle

### 1.1 Forme Simple — SI...ALORS

Exécute un bloc d'instructions **uniquement si la condition est vraie**. Si la condition est fausse, rien ne se passe.

```
  SI condition ALORS
      instructions si VRAI
  FIN SI
```

**Quand l'utiliser :** quand l'action n'est pertinente que dans un seul sens et que l'absence d'action dans l'autre sens est intentionnelle et correcte.

```
  // Exemple : ajouter un avertissement uniquement si le port est privilégié
  SI port < 1024 ALORS
      AFFICHER "⚠️ Port privilégié — droits root nécessaires"
  FIN SI
  // Si port >= 1024 : rien à afficher, c'est normal. Le SI simple est justifié.
```

### 1.2 Forme Double — SI...ALORS...SINON

Couvre **exactement deux cas mutuellement exclusifs et exhaustifs**. L'un ou l'autre des deux blocs est toujours exécuté.

```
  SI condition ALORS
      instructions si VRAI
  SINON
      instructions si FAUX
  FIN SI
```

```
  // Exemple : décision de routage simple
  SI AppartientAuReseau(dest, "192.168.1.0", 24) ALORS
      ENVOYER vers eth0     // réseau local
  SINON
      ENVOYER vers eth1     // passerelle par défaut
  FIN SI
```

> ⚠️ **Règle professionnelle :** Dans tout algorithme de décision réseau, le SINON est obligatoire. Un paquet sans règle applicable doit toujours déclencher une action définie — même si c'est DROP.

### 1.3 Forme Multiple — SINON SI

Couvre **N cas mutuellement exclusifs**, avec un SINON final pour tous les cas non prévus.

```
  SI condition_1 ALORS
      instructions cas 1
  SINON SI condition_2 ALORS
      instructions cas 2
  SINON SI condition_3 ALORS
      instructions cas 3
  SINON
      instructions cas par défaut
  FIN SI
```

**Règle d'exécution :** les conditions sont évaluées **dans l'ordre**, de haut en bas. Dès qu'une condition est vraie, son bloc est exécuté et **toutes les conditions suivantes sont ignorées**. L'ordre des SINON SI est donc critique.

```
  // Exemple : classification de plage d'adresses privées (RFC 1918)
  SI AppartientAuReseau(ip, "10.0.0.0", 8) ALORS
      AFFICHER "Réseau privé classe A (10.x.x.x)"
  SINON SI AppartientAuReseau(ip, "172.16.0.0", 12) ALORS
      AFFICHER "Réseau privé classe B (172.16–31.x.x)"
  SINON SI AppartientAuReseau(ip, "192.168.0.0", 16) ALORS
      AFFICHER "Réseau privé classe C (192.168.x.x)"
  SINON SI AppartientAuReseau(ip, "127.0.0.0", 8) ALORS
      AFFICHER "Loopback (127.x.x.x) — interface locale"
  SINON
      AFFICHER "Adresse publique (routable sur Internet)"
  FIN SI
```
*[Illustration : Un arbre de décision à 5 branches. Chaque nœud est un losange de décision (condition d'appartenance réseau). Les branches "VRAI" mènent directement à un bloc d'action (rectangle). La branche "FAUX" descend vers le nœud suivant. Le dernier nœud "FAUX" mène au bloc "Adresse publique". Représente visuellement le court-circuit : dès qu'on prend une branche VRAI, on ne descend plus.]*

---

## Partie 2 — Conditions Composées et Imbriquées

### 2.1 Conditions Composées avec ET / OU / NON

On peut combiner plusieurs conditions dans un même SI en utilisant les opérateurs booléens vus en S3 :

```
  // Accepter uniquement TCP sur port 443 depuis un réseau autorisé
  SI (protocole = "TCP") ET (port = 443) ET AppartientAuReseau(source, "192.168.0.0", 24) ALORS
      AFFICHER "ACCEPT"
  SINON
      AFFICHER "DROP"
  FIN SI
```

**Propriété de court-circuit :** En pratique, l'évaluation de `A ET B` s'arrête dès que A est FAUX (B n'est pas évalué). De même, `A OU B` s'arrête dès que A est VRAI. Cela permet d'ordonner les conditions du **plus rapide à évaluer au plus coûteux**.

### 2.2 Conditions Imbriquées — SI dans un SI

Un bloc SI peut contenir lui-même une structure SI. On parle de **conditions imbriquées**.

```
  SI condition_externe ALORS
      SI condition_interne ALORS
          action si les deux sont VRAIES
      SINON
          action si externe VRAIE, interne FAUSSE
      FIN SI
  SINON
      action si externe FAUSSE (interne non évaluée)
  FIN SI
```

**Quand préférer l'imbrication à la condition composée ?**

```
  APPROCHE 1 — Condition composée :
  SI ip_valide ET AppartientAuReseau(ip, reseau, masque) ALORS
      AFFICHER "IP valide et dans le réseau"
  SINON
      AFFICHER "Problème" // mais lequel ? IP invalide ou hors réseau ?
  FIN SI

  APPROCHE 2 — Conditions imbriquées (plus précise) :
  SI ip_valide ALORS
      SI AppartientAuReseau(ip, reseau, masque) ALORS
          AFFICHER "IP valide et dans le réseau"          ← cas parfait
      SINON
          AFFICHER "IP valide mais hors du sous-réseau"   ← erreur réseau
      FIN SI
  SINON
      AFFICHER "IP syntaxiquement invalide"               ← erreur de saisie
  FIN SI
```

L'imbrication permet des **messages d'erreur distincts et précis** — qualité professionnelle essentielle.

### 2.3 Comparaison : Imbrication vs. Condition Composée

```
╔════════════════════════╦══════════════════════════╦═══════════════════════════╗
║                        ║  Condition composée      ║  Conditions imbriquées    ║
╠════════════════════════╬══════════════════════════╬═══════════════════════════╣
║  Lisibilité            ║  ++ (une seule ligne)    ║  -- (plusieurs niveaux)   ║
║  Précision des erreurs ║  -- (message unique)     ║  ++ (messages distincts)  ║
║  Performance           ║  + (court-circuit)       ║  = (équivalent)           ║
║  Cas d'usage typique   ║  Règle de pare-feu       ║  Validation avec feedback ║
╚════════════════════════╩══════════════════════════╩═══════════════════════════╝
```

---

## Partie 3 — Les Antipatterns à Connaître et Éviter

### Antipattern 1 — Le SI sans SINON sur une Décision

```
  ❌ PROBLÈME : que se passe-t-il si la condition est fausse ?
  SI masque_valide ALORS
      CalculerReseau(ip, masque)
  FIN SI
  // Si masque_valide = FAUX → rien. Mais le résultat n'est jamais calculé.
  // L'algorithme continue avec une variable non initialisée.

  ✅ CORRECT :
  SI masque_valide ALORS
      CalculerReseau(ip, masque)
  SINON
      AFFICHER "Masque invalide — calcul impossible"
      RETOURNER
  FIN SI
```

### Antipattern 2 — La Condition Redondante

```
  ❌ REDONDANT :
  SI valeur >= 0 ALORS
      SI valeur >= 0 ET valeur <= 255 ALORS   // le premier test est déjà fait
          AFFICHER "Valide"
      FIN SI
  FIN SI

  ✅ SIMPLIFIÉ :
  SI valeur >= 0 ET valeur <= 255 ALORS
      AFFICHER "Valide"
  FIN SI
```

### Antipattern 3 — La Négation Inutilement Complexe

```
  ❌ COMPLEXE et contre-intuitif :
  SI NON(valeur < 0 OU valeur > 255) ALORS
      AFFICHER "Valide"
  FIN SI

  ✅ CLAIR (par De Morgan : NON(A OU B) = NON A ET NON B) :
  SI valeur >= 0 ET valeur <= 255 ALORS
      AFFICHER "Valide"
  FIN SI
```

### Antipattern 4 — L'Ordre Incorrect des SINON SI

```
  ❌ ORDRE INCORRECT — le deuxième cas n'est jamais atteint :
  SI port >= 0 ALORS
      AFFICHER "Port positif ou nul"     // toujours vrai si port >= 0
  SINON SI port >= 1024 ALORS
      AFFICHER "Port utilisateur"        // JAMAIS atteint (déjà couvert par >=0)
  FIN SI

  ✅ ORDRE CORRECT — du plus spécifique au plus général :
  SI port < 0 OU port > 65535 ALORS
      AFFICHER "Port invalide"
  SINON SI port <= 1023 ALORS
      AFFICHER "Port bien connu (0–1023)"
  SINON
      AFFICHER "Port utilisateur (1024–65535)"
  FIN SI
```

---

## Partie 4 — Algorithme d'Appartenance d'une IP à un Sous-réseau

### 4.1 La Question à Résoudre

> "Étant donné une IP `ip_test`, un réseau de référence `ip_ref` et un masque `cidr`, est-ce que `ip_test` appartient au même sous-réseau que `ip_ref` ?"

### 4.2 Décomposition en 3 Décisions

```
  DÉCISION 1 — ip_test est-elle syntaxiquement valide ?
  (4 octets entre 0 et 255 — appel à ValiderIPv4 de S6)

  DÉCISION 2 — Le masque CIDR est-il dans une plage valide ?
  (entre 0 et 32)

  DÉCISION 3 — Les deux adresses réseau sont-elles identiques ?
  réseau_test = AND_BINAIRE(ip_test, masque)
  réseau_ref  = AND_BINAIRE(ip_ref,  masque)
  → réseau_test = réseau_ref ?
```

### 4.3 L'Algorithme Complet

```
  ALGORITHME AppartientAuSousReseau
  ENTRÉE : ip_test    (CHAÎNE — l'adresse à tester)
           ip_ref     (CHAÎNE — une adresse du réseau de référence)
           cidr       (ENTIER — le masque en notation CIDR)
  SORTIE : BOOLÉEN + message explicatif

  DÉBUT
      // ── DÉCISION 1 : Validité de ip_test ──────────────────────
      SI NON ValiderIPv4(ip_test) ALORS
          AFFICHER "ERREUR : '" + ip_test + "' n'est pas une adresse IPv4 valide"
          RETOURNER FAUX
      FIN SI

      // ── DÉCISION 2 : Validité du masque ───────────────────────
      SI cidr < 0 OU cidr > 32 ALORS
          AFFICHER "ERREUR : masque /" + cidr + " invalide (doit être entre 0 et 32)"
          RETOURNER FAUX
      FIN SI

      // ── DÉCISION 3 : Calcul et comparaison des réseaux ────────
      reseau_test ← AND_BINAIRE(ip_test, cidr)
      reseau_ref  ← AND_BINAIRE(ip_ref,  cidr)

      SI reseau_test = reseau_ref ALORS
          AFFICHER ip_test + " APPARTIENT au sous-réseau " + reseau_ref + "/" + cidr
          RETOURNER VRAI
      SINON
          AFFICHER ip_test + " N'APPARTIENT PAS au sous-réseau " + reseau_ref + "/" + cidr
          AFFICHER "  (réseau de " + ip_test + " = " + reseau_test + ")"
          RETOURNER FAUX
      FIN SI
  FIN
```

> 💡 **Rappel S4 :** La fonction `AND_BINAIRE(ip, cidr)` applique l'algorithme de S4 — elle convertit l'IP en 32 bits binaires, construit le masque de `cidr` bits à 1 suivi de `(32-cidr)` bits à 0, effectue le AND bit à bit, et retourne l'adresse réseau résultante.

### 4.4 Trace d'Exécution — Exemple Guidé

**Entrées :** `ip_test = "192.168.10.130"`, `ip_ref = "192.168.10.65"`, `cidr = 26`

```
  Étape 1 — ValiderIPv4("192.168.10.130") ?
    4 parties ✓ / toutes entières ✓ / toutes entre 0 et 255 ✓
    → VRAI → on continue

  Étape 2 — 26 valide (0 ≤ 26 ≤ 32) ?
    → VRAI → on continue

  Étape 3 — Calcul des réseaux (rappel S4) :
    Masque /26 = 255.255.255.192 = 11111111.11111111.11111111.11000000

    AND pour 192.168.10.130 :
      4ème octet 130 = 10000010
                 AND   11000000
                     = 10000000 = 128
    → reseau_test = 192.168.10.128

    AND pour 192.168.10.65 :
      4ème octet 65 = 01000001
                AND   11000000
                    = 01000000 = 64
    → reseau_ref = 192.168.10.64

  Étape 4 — Comparaison :
    192.168.10.128 ≠ 192.168.10.64
    → SINON → AFFICHER "192.168.10.130 N'APPARTIENT PAS au sous-réseau 192.168.10.64/26"
    → RETOURNER FAUX
```

---

## Partie 5 — Extension : Classification Multi-Sous-réseaux

### 5.1 Le Problème

Dans un réseau d'entreprise, on veut savoir **dans quel segment** se trouve une IP — pas seulement si elle appartient à un réseau donné.

### 5.2 L'Algorithme de Classification avec SINON SI

```
  ALGORITHME ClassifierIP
  ENTRÉE : ip_test (CHAÎNE)
  SORTIE : Nom du segment ou "Réseau inconnu"

  // Constantes du plan d'adressage (exemple MERIDIAN de S5)
  RÉSEAU_JURIDIQUE    ← "192.168.10.0"    // /25
  RÉSEAU_ADMIN        ← "192.168.10.128"  // /26
  RÉSEAU_DIRECTION    ← "192.168.10.192"  // /28

  DÉBUT
      // Validation préalable
      SI NON ValiderIPv4(ip_test) ALORS
          AFFICHER "IP invalide"
          RETOURNER
      FIN SI

      // Classification par SINON SI (important : du plus spécifique au plus général)
      SI AppartientAuSousReseau(ip_test, RÉSEAU_DIRECTION, 28) ALORS
          AFFICHER ip_test + " → Segment DIRECTION (/28 — 14 hôtes)"
      SINON SI AppartientAuSousReseau(ip_test, RÉSEAU_ADMIN, 26) ALORS
          AFFICHER ip_test + " → Segment ADMINISTRATIF (/26 — 62 hôtes)"
      SINON SI AppartientAuSousReseau(ip_test, RÉSEAU_JURIDIQUE, 25) ALORS
          AFFICHER ip_test + " → Segment JURIDIQUE (/25 — 126 hôtes)"
      SINON
          AFFICHER ip_test + " → Hors du plan d'adressage connu"
      FIN SI
  FIN
```

> ⚠️ **Ordre crucial :** La Direction (/28) est un sous-ensemble du bloc Juridique (/25). Si on teste Juridique en premier, les IPs de Direction y passeraient sans jamais atteindre le test Direction. Il faut toujours tester **du masque le plus long (le plus spécifique) au masque le plus court (le plus général)** — c'est le principe du **"longest prefix match"** utilisé par tous les routeurs.

### 5.3 Lien Avec le Routage — La Table de Routage Est un SINON SI

```
  // Ce que fait un routeur réel, traduit en pseudo-code :

  POUR chaque_paquet_reçu FAIRE
      dest ← destination_du_paquet

      SI AppartientAuSousReseau(dest, "192.168.1.0", 24) ALORS
          ENVOYER via eth0    // réseau local segment 1
      SINON SI AppartientAuSousReseau(dest, "192.168.2.0", 24) ALORS
          ENVOYER via eth1    // réseau local segment 2
      SINON SI AppartientAuSousReseau(dest, "10.0.0.0", 8) ALORS
          ENVOYER via vpn0    // réseau distant via VPN
      SINON
          ENVOYER via eth_wan // route par défaut (Internet)
      FIN SI
  FIN POUR
```

> 💡 **Ce pseudo-code est une simplification du fonctionnement réel d'un routeur Linux.** La commande `ip route show` affiche exactement cette table de décision. Quand vous configurerez des routes en TP, vous écrirez les entrées de ce SINON SI.

---

## Partie 6 — La Grille de Trace d'Exécution

Pour tester un algorithme à la main, utiliser cette grille systématiquement :

```
  TRACE D'EXÉCUTION — AppartientAuSousReseau
  ───────────────────────────────────────────────────────────────────
  Entrées : ip_test = __________ / ip_ref = __________ / cidr = ___
  ───────────────────────────────────────────────────────────────────
  ÉTAPE          │ VARIABLE         │ VALEUR          │ DÉCISION
  ───────────────┼──────────────────┼─────────────────┼────────────
  Décision 1     │ ValiderIPv4      │ VRAI / FAUX     │ Continuer / STOP
  Décision 2     │ cidr valide      │ VRAI / FAUX     │ Continuer / STOP
  AND ip_test    │ reseau_test      │ ___.___.___.___ │
  AND ip_ref     │ reseau_ref       │ ___.___.___.___ │
  Comparaison    │ reseau_test=ref  │ VRAI / FAUX     │ APPARTIENT / NON
  ───────────────────────────────────────────────────────────────────
  Sortie : AFFICHER ______________________ / RETOURNER _______
  ───────────────────────────────────────────────────────────────────
```

---

## Partie 7 — Exercices Guidés

### Série 1 — Maîtrise des Structures Conditionnelles

**Exercice 1.1 — Compléter avec le bon SINON**
L'algorithme suivant classe une adresse selon sa plage. Il contient une erreur d'ordre des conditions. Identifiez-la et corrigez-la.

```
  SI octet >= 128 ALORS
      AFFICHER "Deuxième moitié (128–255)"
  SINON SI octet >= 0 ALORS
      AFFICHER "Première moitié (0–127)"
  SINON
      AFFICHER "Invalide (négatif)"
  FIN SI
```

**Exercice 1.2 — Conditions composées à simplifier**
Réécrire en utilisant NON + De Morgan (lien S3) :

```
  SI NON(port < 0) ET NON(port > 65535) ALORS
      AFFICHER "Port valide"
  FIN SI
```

**Exercice 1.3 — Imbrication ou composée ?**
Écrire deux versions de l'algorithme suivant (une avec condition composée, une avec imbrication) et indiquer laquelle est préférable avec justification :

> *"Accepter un paquet si le protocole est TCP ET le port est 80 ET l'IP source est dans 10.0.0.0/8. Afficher un message d'erreur différent selon le critère non satisfait."*

### Série 2 — Appartenance IP

**Exercice 2.1 — Trace complète**
Compléter la grille de trace pour : `ip_test = "192.168.1.50"`, `ip_ref = "192.168.1.200"`, `cidr = 24`

**Exercice 2.2 — Cas limites**
Tester `AppartientAuSousReseau` sur les entrées suivantes. Prédire le résultat **avant** de dérouler :

| **ip_test** | **ip_ref** | **cidr** | **Résultat prédit** | **Raison** |
|---|---|---|---|---|
| `"192.168.1.1"` | `"192.168.1.254"` | 24 | | |
| `"192.168.1.128"` | `"192.168.1.10"` | 25 | | |
| `"10.0.0.1"` | `"10.255.255.255"` | 8 | | |
| `"192.168.abc.1"` | `"192.168.1.1"` | 24 | | |
| `"192.168.1.1"` | `"192.168.1.1"` | 30 | | |

**Exercice 2.3 — Classification complète**
Écrire l'algorithme `ClassifierRFC1918` qui classe une IP dans l'une des catégories : plage privée 10.x (/8), plage privée 172.16.x (/12), plage privée 192.168.x (/16), loopback (/8), ou adresse publique.

---

## Vocabulaire Clé à Maîtriser pour l'Examen

| **Terme** | **Définition** |
|---|---|
| **Structure conditionnelle** | Construction algorithmique exécutant différentes instructions selon qu'une condition est vraie ou fausse |
| **Forme simple (SI...FIN SI)** | Exécute un bloc uniquement si la condition est vraie — rien si elle est fausse |
| **Forme double (SI...SINON)** | Couvre exactement deux cas mutuellement exclusifs et exhaustifs |
| **Forme multiple (SINON SI)** | Chaîne de conditions mutuellement exclusives avec un cas par défaut |
| **Court-circuit** | Dans une chaîne SINON SI, l'évaluation s'arrête dès qu'une condition est vraie — les suivantes ne sont pas évaluées |
| **Conditions imbriquées** | Structure SI à l'intérieur d'un bloc SI — permet des messages d'erreur distincts |
| **Condition composée** | Combinaison de plusieurs conditions avec ET/OU/NON dans un même SI |
| **Longest prefix match** | Principe de routage : quand plusieurs routes correspondent, la plus spécifique (masque le plus long) est choisie |
| **Précondition** | Condition dont la vérité doit être assurée avant d'exécuter un traitement — protège l'algorithme des entrées invalides |
| **Antipattern** | Erreur de conception algorithmique récurrente et reconnaissable (SI sans SINON, condition redondante...) |
| **Trace d'exécution** | Tableau suivant l'évolution des variables étape par étape lors de l'exécution manuelle d'un algorithme |
| **Rule matching order** | Ordre dans lequel un pare-feu ou routeur évalue ses règles — la première règle correspondante s'applique |


---

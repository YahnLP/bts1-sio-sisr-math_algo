---
author: YLP
title: 📖 FICHE DE COURS
---

## 📖 FICHE DE COURS
### Boucles · POUR · TANT QUE · Parcours de Listes · Génération d'IPs d'un Sous-réseau

*Version 1.0 — BTS SIO SISR — Année 1 — Semaine 8*
> **Prérequis :** S4 (calcul réseau/broadcast), S6 (types, pseudo-code), S7 (SI/SINON, ValiderIPv4, AppartientAuSousReseau)

---

## Partie 1 — La Triade Algorithmique est Complète

Avec S8, vous disposez des trois structures fondamentales qui permettent d'écrire **tout algorithme calculable** :

```
  S6 → SÉQUENCE    instruction_1 ; instruction_2 ; instruction_3 ...
  S7 → CONDITION   SI condition ALORS ... SINON ... FIN SI
  S8 → RÉPÉTITION  POUR / TANT QUE ... FIN POUR / FIN TANT QUE
```
*[Illustration : Trois blocs colorés empilés en pyramide. La base (SÉQUENCE, en gris) porte la CONDITION (en bleu), qui porte la RÉPÉTITION (en orange). Annotation : "Ces trois briques suffisent à construire tout programme — Böhm & Jacopini, 1966."]*

---

## Partie 2 — La Boucle POUR

### 2.1 Structure et Sémantique

La boucle POUR s'utilise quand le **nombre d'itérations est connu avant de commencer**.

```
  POUR variable DE valeur_début À valeur_fin FAIRE
      instructions du corps de boucle
  FIN POUR
```

La variable de boucle prend successivement toutes les valeurs entières de `valeur_début` à `valeur_fin` inclus. Elle avance de 1 à chaque itération par défaut.

```
  // Exemple : afficher les 4 octets d'une IP
  POUR i DE 1 À 4 FAIRE
      AFFICHER "Octet " + i + " : " + octets[i]
  FIN POUR
  // i prend les valeurs 1, 2, 3, 4 — exactement 4 itérations, toujours.
```

### 2.2 Nombre d'Itérations et Cas Particuliers

Le nombre d'itérations est toujours `valeur_fin − valeur_début + 1`. Quelques cas à retenir :

```
  POUR i DE 1 À 254 FAIRE ...   → 254 itérations (hôtes d'un /24)
  POUR i DE 0 À 255 FAIRE ...   → 256 itérations (toutes valeurs d'un octet)
  POUR i DE 5 À 5   FAIRE ...   → 1 itération exactement
  POUR i DE 10 À 1  FAIRE ...   → 0 itérations (début > fin → boucle ignorée)
```

Ce dernier cas — début supérieur à fin — ne produit aucune erreur, mais le corps de boucle n'est jamais exécuté. C'est un comportement à connaître pour éviter des bugs silencieux.

### 2.3 Variante avec Pas

Quand on veut progresser par une valeur autre que 1 :

```
  POUR variable DE début À fin PAS valeur_pas FAIRE
      instructions
  FIN POUR

  // Exemple : les 256 valeurs d'octet par pas de 2 (valeurs paires uniquement)
  POUR octet DE 0 À 254 PAS 2 FAIRE
      AFFICHER octet      // 0, 2, 4, ..., 254
  FIN POUR

  // Exemple : décompte à rebours
  POUR i DE 10 À 1 PAS -1 FAIRE
      AFFICHER i          // 10, 9, 8, ..., 1
  FIN POUR
```

### 2.4 POUR Appliqué aux Réseaux — Motifs Courants

**Motif accumulateur** — sommer ou concaténer en parcourant :

```
  // Compter les IPs paires dans un sous-réseau (dernier octet pair)
  compteur ← 0
  POUR i DE (reseau_int + 1) À (brd_int - 1) FAIRE
      SI i MOD 2 = 0 ALORS
          compteur ← compteur + 1
      FIN SI
  FIN POUR
  AFFICHER "IPs à dernier octet pair : " + compteur
```

**Motif drapeau booléen** — signaler qu'une condition a été rencontrée :

```
  // Vérifier si une IP cible est dans la plage
  trouve ← FAUX
  POUR i DE (reseau_int + 1) À (brd_int - 1) FAIRE
      SI i = IP_VERS_ENTIER(ip_cible) ALORS
          trouve ← VRAI
      FIN SI
  FIN POUR
  SI trouve ALORS
      AFFICHER ip_cible + " est dans la plage"
  SINON
      AFFICHER ip_cible + " est hors plage"
  FIN SI
  // Note : ce cas est mieux résolu par AppartientAuSousReseau (S7).
  // Le motif drapeau est montré ici pour l'apprentissage de la structure.
```

---

## Partie 3 — La Boucle TANT QUE

### 3.1 Structure et Sémantique

La boucle TANT QUE s'utilise quand le **nombre d'itérations n'est pas connu à l'avance** — il dépend d'un résultat calculé pendant l'exécution.

```
  TANT QUE condition FAIRE
      instructions du corps de boucle
      (la condition doit évoluer pour éviter une boucle infinie)
  FIN TANT QUE
```

La condition est évaluée **avant** chaque itération. Si elle est fausse dès le départ, le corps de boucle n'est jamais exécuté — c'est une différence fondamentale avec la variante RÉPÉTER/JUSQU'À.

```
  // Exemple : lire des adresses IP jusqu'à saisie d'une IP valide
  ip_saisie ← ""
  TANT QUE NON ValiderIPv4(ip_saisie) FAIRE
      AFFICHER "Entrez une adresse IPv4 valide : "
      LIRE ip_saisie
  FIN TANT QUE
  AFFICHER "Adresse acceptée : " + ip_saisie
  // On ne sait pas combien de tentatives l'utilisateur va faire.
```

### 3.2 Les Deux Erreurs Classiques de TANT QUE

**Erreur 1 — La boucle infinie :** la condition ne devient jamais FAUX.

```
  ❌ BOUCLE INFINIE :
  ip_int ← reseau_int + 1
  TANT QUE ip_int > 0 FAIRE      // toujours vrai pour une IP positive
      AFFICHER ENTIER_VERS_IP(ip_int)
      ip_int ← ip_int + 1
  FIN TANT QUE

  ✅ CORRIGÉ :
  ip_int ← reseau_int + 1
  TANT QUE ip_int < brd_int FAIRE   // s'arrête avant le broadcast
      AFFICHER ENTIER_VERS_IP(ip_int)
      ip_int ← ip_int + 1
  FIN TANT QUE
```

**Erreur 2 — La boucle morte :** la condition est fausse dès le départ.

```
  ❌ BOUCLE MORTE :
  i ← 300
  TANT QUE i < 256 FAIRE     // 300 < 256 est FAUX immédiatement
      AFFICHER i
      i ← i + 1
  FIN TANT QUE
  // Rien ne s'affiche. Aucun message d'erreur non plus — bug silencieux.
```

> ⚠️ **Règle de sécurité :** Toute boucle TANT QUE doit contenir dans son corps une instruction qui **modifie la variable testée dans la condition**. Si cette instruction est absente, c'est une boucle infinie garantie.

### 3.3 Variante RÉPÉTER...JUSQU'À

Cette variante exécute le corps de boucle **au moins une fois**, puis vérifie la condition :

```
  RÉPÉTER
      instructions
  JUSQU'À condition_d_arrêt
```

Utile pour les saisies utilisateur — on veut toujours lire au moins une fois :

```
  RÉPÉTER
      AFFICHER "Entrez un masque CIDR (0–32) : "
      LIRE cidr
  JUSQU'À (cidr >= 0 ET cidr <= 32)
  // Garantit au moins une saisie, relance tant que la valeur est invalide.
```

### 3.4 Tableau Récapitulatif — Choisir la Bonne Boucle

```
╔════════════════════════════════════╦══════════════╦═════════════════════════╗
║  Situation                         ║  Structure   ║  Exemple réseau         ║
╠════════════════════════════════════╬══════════════╬═════════════════════════╣
║  Nb itérations connu avant         ║  POUR        ║  4 octets d'une IP      ║
║  Parcourir plage numérique         ║  POUR        ║  IPs de .1 à .254       ║
║  Nb itérations dépend du résultat  ║  TANT QUE   ║  Lire jusqu'à IP valide ║
║  Au moins une exécution requise    ║  RÉPÉTER     ║  Saisie utilisateur     ║
║  Parcours avec condition d'arrêt   ║  TANT QUE   ║  Chercher IP libre      ║
╚════════════════════════════════════╩══════════════╩═════════════════════════╝
```

---

## Partie 4 — La Représentation Entière d'une IP

### 4.1 Pourquoi Convertir une IP en Entier ?

Une adresse IPv4 est fondamentalement un **entier de 32 bits** écrit sous forme de 4 octets. La notation décimale pointée (`192.168.1.1`) est une convention de lisibilité humaine — pas la vraie nature de l'objet. Travailler avec la représentation entière simplifie radicalement les algorithmes sur des plages d'adresses : au lieu de manipuler 4 variables séparément, on manipule **un seul entier**.

*[Illustration : La barre de 32 bits d'une IP divisée en 4 groupes de 8. Chaque groupe porte son poids : ×2²⁴, ×2¹⁶, ×2⁸, ×2⁰. En dessous, les valeurs décimales correspondantes pour 192.168.1.10 : 3 221 225 738. Annotation : "Ce nombre contient toute l'information de l'adresse — on peut le manipuler avec +1 pour passer à l'adresse suivante."]*

### 4.2 Les Deux Fonctions Auxiliaires

Ces deux fonctions sont les seuls outils nécessaires. On les traite comme des **boîtes noires** (leur implémentation interne est détaillée ci-dessous pour les curieux) :

```
  IP_VERS_ENTIER(ip : CHAÎNE) → ENTIER
  ──────────────────────────────────────────────────────────────────
  Convertit "192.168.1.10" en 3221225738
  Formule : o1 × 2²⁴  +  o2 × 2¹⁶  +  o3 × 2⁸  +  o4 × 2⁰
          = o1 × 16777216  +  o2 × 65536  +  o3 × 256  +  o4

  ENTIER_VERS_IP(n : ENTIER) → CHAÎNE
  ──────────────────────────────────────────────────────────────────
  Convertit 3221225738 en "192.168.1.10"
  Formule : o1 = n DIV 16777216
            o2 = (n MOD 16777216) DIV 65536
            o3 = (n MOD 65536) DIV 256
            o4 = n MOD 256
```

**Vérification sur un exemple concret :**
```
  IP_VERS_ENTIER("192.168.1.10") :
  = 192 × 16777216  +  168 × 65536  +  1 × 256  +  10
  = 3221225472      +  11010048      +  256       +  10
  = 3232235786

  ENTIER_VERS_IP(3232235786) :
  o1 = 3232235786 DIV 16777216          = 192  ✓
  o2 = (3232235786 MOD 16777216) DIV 65536
     = 11010560 DIV 65536               = 168  ✓
  o3 = (11010560 MOD 65536) DIV 256
     = 256 DIV 256                      = 1    ✓
  o4 = 256 MOD 256                      = 10   ✓
```

> 💡 **Lien S1/S2 :** ce calcul est exactement la conversion binaire→décimal avec les poids 2²⁴, 2¹⁶, 2⁸, 2⁰. Une IP est un nombre en base 256, tout comme un entier décimal est un nombre en base 10. Les puissances de 2 que vous avez mémorisées en S1 servent directement ici.

### 4.3 La Propriété Fondamentale

Deux adresses IP consécutives diffèrent de 1 dans leur représentation entière :

```
  IP_VERS_ENTIER("192.168.1.10") = 3232235786
  IP_VERS_ENTIER("192.168.1.11") = 3232235787   (= 3232235786 + 1)
  IP_VERS_ENTIER("192.168.1.255") = 3232235775
  IP_VERS_ENTIER("192.168.2.0")  = 3232235776   (= 3232235775 + 1)
```

Cela signifie qu'une simple boucle `POUR i DE début À fin` parcourt toutes les adresses d'une plage dans l'ordre, sans jamais manquer un passage de type `.255` → `.0` du segment suivant.

---

## Partie 5 — Algorithme de Génération des IPs d'un Sous-réseau

### 5.1 Rappel : Qu'est-ce qu'une Adresse Hôte ?

Dans un sous-réseau, trois types d'adresses existent :

```
  Adresse réseau  → première adresse de la plage  (non assignable à un hôte)
  Adresses hôtes  → toutes les adresses entre la première et la dernière
  Broadcast       → dernière adresse de la plage   (non assignable à un hôte)

  Exemple pour 192.168.1.0/24 :
  Réseau    : 192.168.1.0    (ne pas générer)
  Hôtes     : 192.168.1.1 → 192.168.1.254   (à générer)
  Broadcast : 192.168.1.255  (ne pas générer)
```

### 5.2 L'Approche Naïve — Pour Comprendre Pourquoi Elle est Insuffisante

Une première idée serait d'écrire une boucle sur le dernier octet pour un /24 :

```
  ALGORITHME GenererIPsNaif
  // Fonctionne UNIQUEMENT pour un /24 — non généralisable
  DÉBUT
      LIRE prefixe    // ex : "192.168.1"
      POUR octet DE 1 À 254 FAIRE
          AFFICHER prefixe + "." + octet
      FIN POUR
  FIN
```

Cette approche a deux limites fatales : elle suppose que la plage hôte correspond exactement au dernier octet (vrai pour /24 seulement), et elle ne peut pas gérer un /20 ou un /27 où la frontière réseau/hôte coupe un octet. Elle serait inutilisable dans un contexte professionnel réel.

### 5.3 L'Algorithme Général avec Représentation Entière

```
  ALGORITHME GenererIPsReseau
  ENTRÉE  : ip_ref (CHAÎNE — une IP du réseau),
            cidr   (ENTIER — masque en notation CIDR)
  SORTIE  : liste de toutes les adresses hôtes affichées

  DÉBUT
      // ── Validations préalables (préconditions — S7) ──────────────
      SI NON ValiderIPv4(ip_ref) ALORS
          AFFICHER "ERREUR : IP de référence invalide"
          RETOURNER
      FIN SI
      SI cidr < 0 OU cidr > 30 ALORS
          AFFICHER "ERREUR : masque /" + cidr + " invalide ou sans hôtes utilisables"
          RETOURNER
      FIN SI

      // ── Calcul des bornes du réseau (algorithme S4) ───────────────
      reseau    ← AND_BINAIRE(ip_ref, cidr)         // adresse réseau
      wildcard  ← NOT_BINAIRE(cidr)                 // masque inversé
      broadcast ← OR_BINAIRE(reseau, wildcard)      // adresse broadcast

      // ── Conversion en entiers pour itération simple ───────────────
      reseau_int ← IP_VERS_ENTIER(reseau)
      brd_int    ← IP_VERS_ENTIER(broadcast)

      // ── Calcul du nombre d'hôtes (formule S4) ─────────────────────
      nb_bits_hote ← 32 - cidr
      nb_hotes     ← PUISSANCE(2, nb_bits_hote) - 2

      // ── En-tête informatif ────────────────────────────────────────
      AFFICHER "Réseau   : " + reseau    + "/" + cidr
      AFFICHER "Broadcast: " + broadcast
      AFFICHER "Hôtes    : " + nb_hotes + " adresses"
      AFFICHER "────────────────────────────────"

      // ── Génération : de réseau+1 à broadcast-1 ───────────────────
      POUR i DE (reseau_int + 1) À (brd_int - 1) FAIRE
          AFFICHER ENTIER_VERS_IP(i)
      FIN POUR

      AFFICHER "────────────────────────────────"
      AFFICHER "Génération terminée : " + nb_hotes + " adresses listées."
  FIN
```

### 5.4 Trace d'Exécution sur un Petit Exemple

**Entrées :** `ip_ref = "192.168.1.200"`, `cidr = 29`

```
  Validation : IP valide ✓ / cidr = 29 ≤ 30 ✓

  Calcul des bornes (rappel S4) :
    Masque /29 = 255.255.255.248
    4ème octet de ip_ref = 200 = 11001000
    AND masque 4ème oct  =       11111000
    Résultat             =       11001000 = 200... non !
    Recalculons : 11001000 AND 11111000 = 11001000 = 200
    Réseau = 192.168.1.200

    Wildcard 4ème oct : NOT(11111000) = 00000111 = 7
    Broadcast : 11001000 OR 00000111 = 11001111 = 207
    Broadcast = 192.168.1.207

  Conversion en entiers :
    reseau_int = IP_VERS_ENTIER("192.168.1.200") = 3232235976
    brd_int    = IP_VERS_ENTIER("192.168.1.207") = 3232235983

  nb_bits_hote = 32 - 29 = 3
  nb_hotes = 2³ - 2 = 8 - 2 = 6

  Boucle POUR i DE 3232235977 À 3232235982 FAIRE (6 itérations) :
    i = 3232235977 → ENTIER_VERS_IP → "192.168.1.201"
    i = 3232235978 → "192.168.1.202"
    i = 3232235979 → "192.168.1.203"
    i = 3232235980 → "192.168.1.204"
    i = 3232235981 → "192.168.1.205"
    i = 3232235982 → "192.168.1.206"

  Sortie : 6 adresses de .201 à .206 — le broadcast (.207) est exclu ✓
```

### 5.5 Version avec TANT QUE — Comparaison

Le même résultat peut s'obtenir avec TANT QUE. Cette version illustre pourquoi POUR est préférable ici :

```
  // Version TANT QUE — fonctionnellement identique, structurellement moins claire
  ip_int ← reseau_int + 1
  TANT QUE ip_int < brd_int FAIRE
      AFFICHER ENTIER_VERS_IP(ip_int)
      ip_int ← ip_int + 1
  FIN TANT QUE
```

Les deux versions sont correctes. La version POUR est préférable car elle rend explicite le fait qu'on parcourt une **plage numérique délimitée** — l'intention est immédiatement lisible. Le TANT QUE serait plus approprié si la condition d'arrêt était un événement imprévisible (IP qui répond au ping, fichier épuisé, etc.).

---

## Partie 6 — Implémentation des Fonctions Auxiliaires

### 6.1 IP_VERS_ENTIER en Pseudo-code

```
  ALGORITHME IP_VERS_ENTIER
  ENTRÉE  : ip (CHAÎNE)
  SORTIE  : ENTIER (représentation 32 bits)

  DÉBUT
      parties ← DECOUPER(ip, ".")       // ["192", "168", "1", "10"]
      o1 ← CONVERTIR_EN_ENTIER(parties[1])
      o2 ← CONVERTIR_EN_ENTIER(parties[2])
      o3 ← CONVERTIR_EN_ENTIER(parties[3])
      o4 ← CONVERTIR_EN_ENTIER(parties[4])
      RETOURNER o1 × 16777216 + o2 × 65536 + o3 × 256 + o4
  FIN
```

### 6.2 ENTIER_VERS_IP en Pseudo-code

```
  ALGORITHME ENTIER_VERS_IP
  ENTRÉE  : n (ENTIER)
  SORTIE  : CHAÎNE (notation décimale pointée)

  DÉBUT
      o1 ← n DIV 16777216
      o2 ← (n MOD 16777216) DIV 65536
      o3 ← (n MOD 65536) DIV 256
      o4 ← n MOD 256
      RETOURNER o1 + "." + o2 + "." + o3 + "." + o4
  FIN
```

> 💡 **Lien avec le scripting :** Ces deux fonctions existent dans tous les langages. En Python : `int(ipaddress.ip_address("192.168.1.1"))` et `str(ipaddress.ip_address(3232235777))`. En Bash, le calcul se fait avec des opérateurs arithmétiques `$(( ))`. Comprendre les algorithmes ci-dessus vous permet de les reconstruire si la bibliothèque n'est pas disponible.

---

## Partie 7 — Exercices Guidés

**Exercice 1.1 — Compter les octets pairs dans un /24**
Écrire un algorithme qui génère toutes les IPs d'un /24 et compte celles dont le dernier octet est pair. Utiliser un motif accumulateur.

**Exercice 1.2 — Parcourir une liste d'IPs suspectes**
On dispose d'une liste de 10 adresses IP (tableau) à vérifier. Écrire l'algorithme qui parcourt la liste et affiche, pour chacune, si elle appartient au réseau `10.0.0.0/8` (utiliser `AppartientAuSousReseau` de S7).

**Exercice 1.3 — Trouver la première IP libre**
On dispose d'une liste d'IPs déjà assignées. Écrire un algorithme TANT QUE qui parcourt la plage d'un /29 et s'arrête sur la première IP absente de la liste assignée. *(Indice : utiliser un drapeau `libre` et la fonction `CONTIENT(liste, ip)`.)*

**Exercice 1.4 — Valider IP_VERS_ENTIER**
Vérifier à la main que `IP_VERS_ENTIER("10.0.0.1") = 167772161`. Montrer le calcul détaillé avec les puissances de 2.

---

## Vocabulaire Clé à Maîtriser pour l'Examen

| **Terme** | **Définition** |
|---|---|
| **Boucle POUR** | Structure de répétition exécutant un bloc un nombre connu de fois, avec une variable d'itération progressant de début à fin |
| **Boucle TANT QUE** | Structure de répétition dont la condition est évaluée avant chaque itération — s'arrête quand la condition devient fausse |
| **RÉPÉTER...JUSQU'À** | Variante de TANT QUE dont le corps est exécuté au moins une fois — la condition est évaluée après chaque itération |
| **Boucle infinie** | Boucle dont la condition ne devient jamais fausse — erreur de conception grave |
| **Motif accumulateur** | Variable initialisée à 0 (ou neutre) avant la boucle et mise à jour à chaque itération pour cumuler un résultat |
| **Motif drapeau** | Variable booléenne initialisée à FAUX et passée à VRAI dès qu'un événement est détecté dans la boucle |
| **Représentation entière d'une IP** | Conversion d'une IPv4 en un entier 32 bits non signé — permet d'itérer sur une plage d'adresses avec une simple boucle |
| **IP_VERS_ENTIER** | Fonction calculant `o1×2²⁴ + o2×2¹⁶ + o3×2⁸ + o4` — transforme une notation décimale pointée en entier |
| **ENTIER_VERS_IP** | Fonction inverse — extrait les 4 octets par divisions et modulos successifs |
| **Adresses hôtes** | Ensemble des adresses d'un sous-réseau à l'exclusion de l'adresse réseau et du broadcast — plage `réseau+1` à `broadcast−1` |


---

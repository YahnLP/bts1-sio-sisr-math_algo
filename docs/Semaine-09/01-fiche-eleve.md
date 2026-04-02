---
author: YLP
title: 📖 FICHE DE COURS
---

# 📖 FICHE DE COURS ÉLÈVE
## Fonctions · Procédures · Modularité · Paramètres · Valeur de Retour

*Durée : 1h25 — Individuel avec checkpoints collectifs*
> **Prérequis :** S6–S8 — pseudo-code, types, SI/SINON, boucles, utilisation de `ValiderIPv4`, `IP_VERS_ENTIER`, `AppartientAuSousReseau`

---

## Partie 1 — Du Programme Monolithique au Programme Modulaire

### 1.1 Le Problème du Code Dupliqué

Imaginez que dans trois programmes différents, vous ayez besoin de calculer le nombre d'hôtes d'un sous-réseau. Sans fonctions, vous réécrivez à chaque fois les mêmes lignes :

```
  // Dans GenererIPsReseau (S8) :
  nb_hotes ← PUISSANCE(2, 32 - cidr) - 2

  // Dans ClassifierSegment (S7) :
  nb_hotes ← PUISSANCE(2, 32 - cidr) - 2    // même chose, copiée

  // Dans AuditReseau (S8) :
  nb_hotes ← PUISSANCE(2, 32 - cidr) - 2    // copiée encore
```

Cette duplication a trois conséquences désastreuses. Si la formule contient une erreur, vous devez corriger trois endroits — et vous en oublierez certainement un. Si vous voulez ajouter une validation (cidr entre 0 et 30), vous devez l'ajouter trois fois. Et si quelqu'un lit votre code, il doit comprendre la même formule trois fois au lieu d'une.

**La solution :** écrire la formule **une seule fois**, dans une fonction nommée, et l'appeler depuis les trois programmes.

### 1.2 Avant et Après — La Même Logique, Deux Formes

```
  ┌─────────────────────────────────────────────────────────┐
  │  AVANT (code dupliqué)   │  APRÈS (code modulaire)      │
  ├─────────────────────────────────────────────────────────┤
  │  ...                     │  nb_hotes ← NombreHotes(cidr)│
  │  nb_hotes ←              │  ...                         │
  │    PUISSANCE(2,32-cidr)-2│                              │
  │  ...                     │  // L'algorithme est défini  │
  │                          │  // une seule fois ailleurs  │
  └─────────────────────────────────────────────────────────┘
```

*[Illustration : Deux schémas côte à côte. À gauche, trois blocs de programme contenant chacun le même calcul mis en évidence en rouge. À droite, les trois mêmes blocs dont le calcul est remplacé par un simple appel de fonction, et une unique définition de la fonction au-dessus. Des flèches pointent des trois appels vers la définition unique.]*

---

## Partie 2 — Anatomie d'une Fonction

### 2.1 La Structure Complète

Une fonction se compose de cinq éléments obligatoires :

```
  FONCTION NomDeLaFonction(param1 : TYPE1, param2 : TYPE2, ...) → TYPE_RETOUR
  // Documentation : ce que fait la fonction, ce qu'elle attend, ce qu'elle retourne
  DÉBUT
      // Corps de la fonction — instructions locales
      // Obligatoirement au moins un RETOURNER
      RETOURNER valeur_resultat
  FIN FONCTION
```

Voyons ces cinq éléments sur un exemple concret :

```
  FONCTION NombreHotes(cidr : ENTIER) → ENTIER
  // Calcule le nombre d'adresses hôtes utilisables pour un masque /cidr.
  // Précondition  : cidr doit être entre 0 et 30 inclus.
  // Retourne      : 2^(32-cidr) - 2, ou -1 si cidr est invalide.
  DÉBUT
      SI cidr < 0 OU cidr > 30 ALORS
          RETOURNER -1          // valeur sentinelle : signale l'erreur
      FIN SI
      bits_hote ← 32 - cidr    // variable locale — n'existe que ici
      RETOURNER PUISSANCE(2, bits_hote) - 2
  FIN FONCTION
```

| **Élément** | **Dans l'exemple** | **Rôle** |
|---|---|---|
| Mot-clé `FONCTION` | `FONCTION` | Annonce qu'on définit une fonction |
| Nom | `NombreHotes` | Identifiant réutilisable à l'appel |
| Paramètre formel | `cidr : ENTIER` | Variable locale qui reçoit l'argument |
| Type de retour | `→ ENTIER` | Type de la valeur que la fonction produit |
| `RETOURNER` | Deux occurrences | Fournit la valeur résultat et arrête la fonction |

### 2.2 Appeler une Fonction — L'Argument

À l'appel, on fournit un **argument** (une valeur concrète) à la place du paramètre formel :

```
  // À l'appel, l'argument est 24 — la valeur est copiée dans cidr
  nb ← NombreHotes(24)       // nb vaut 254

  // L'argument peut être une variable
  mon_cidr ← 26
  nb ← NombreHotes(mon_cidr) // nb vaut 62

  // L'argument peut être une expression
  nb ← NombreHotes(32 - 8)   // équivaut à NombreHotes(24)
```

> ⚠️ **Paramètre formel ≠ argument.** `cidr` dans la définition est le paramètre formel — c'est un nom local à la fonction. `mon_cidr` à l'appel est l'argument — c'est la variable du programme appelant. Les deux sont des entités distinctes. Modifier `cidr` à l'intérieur de la fonction ne modifie **jamais** `mon_cidr` à l'extérieur.

### 2.3 `RETOURNER` Arrête Tout

Le mot-clé `RETOURNER` est définitif : dès qu'il est exécuté, la fonction se termine immédiatement. Les instructions suivantes ne s'exécutent pas :

```
  FONCTION ExempleRetour(n : ENTIER) → CHAÎNE
  DÉBUT
      SI n < 0 ALORS
          RETOURNER "négatif"   // ← la fonction s'arrête ici si n < 0
      FIN SI
      RETOURNER "positif ou nul" // ← atteint seulement si n >= 0
      AFFICHER "Cette ligne ne s'exécute JAMAIS"  // code mort
  FIN FONCTION
```

Cette propriété permet d'écrire des **sorties anticipées** (early return) pour traiter les cas d'erreur en début de fonction, ce qui simplifie la lecture du cas nominal.

---

## Partie 3 — Fonction vs. Procédure

Une **procédure** produit un effet sans retourner de valeur utilisable. Elle peut afficher, modifier un état global, ou déclencher une action — mais on ne peut pas écrire `x ← MaProcedure(...)`.

```
  PROCÉDURE AfficherEnTeteReseau(reseau : CHAÎNE, cidr : ENTIER)
  // Affiche l'en-tête informatif d'un sous-réseau — aucune valeur retournée.
  DÉBUT
      AFFICHER "══════════════════════════════"
      AFFICHER "Réseau   : " + reseau + "/" + cidr
      AFFICHER "Hôtes    : " + NombreHotes(cidr)   // appel de fonction dans une procédure
      AFFICHER "══════════════════════════════"
  FIN PROCÉDURE
```

La règle pratique pour distinguer les deux : **si vous pouvez écrire `x ← ...` ou `SI ...` devant l'appel, c'est une fonction. Sinon, c'est une procédure.**

```
  nb ← NombreHotes(24)              // ✓ fonction — retourne une valeur
  SI ValiderIPv4(ip) ALORS ...       // ✓ fonction — retourne un booléen
  AfficherEnTeteReseau("10.0.0.0", 8) // procédure — appel seul, sans récupérer de valeur
```

---

## Partie 4 — La Portée Locale

### 4.1 Chaque Fonction Vit dans Son Propre Espace

Les variables déclarées ou reçues à l'intérieur d'une fonction n'existent que pendant son exécution. Ce concept s'appelle la **portée locale** (ou scope local).

```
  ALGORITHME ProgrammePrincipal
  DÉBUT
      cidr_principal ← 24
      resultat ← NombreHotes(cidr_principal)
      // ici, la variable "bits_hote" n'existe pas — elle est locale à NombreHotes
      AFFICHER resultat   // 254
  FIN

  FONCTION NombreHotes(cidr : ENTIER) → ENTIER
  DÉBUT
      bits_hote ← 32 - cidr   // bits_hote : variable locale, visible ici seulement
      RETOURNER PUISSANCE(2, bits_hote) - 2
      // quand la fonction se termine, bits_hote disparaît
  FIN FONCTION
```

*[Illustration : Deux boîtes rectangulaires côte à côte avec une ligne de séparation. La boîte gauche (Programme Principal) contient les variables `cidr_principal` et `resultat`. La boîte droite (NombreHotes) contient les variables `cidr` (paramètre) et `bits_hote` (locale). Des étiquettes "invisible de là-bas" pointent depuis chaque boîte vers les variables de l'autre. Une flèche nommée "appel avec 24" va de la gauche vers la droite, et une flèche nommée "retour : 254" revient de la droite vers la gauche.]*

### 4.2 La Conséquence Pratique : La Liberté de Nommage

Deux fonctions peuvent avoir des variables locales portant le même nom — elles ne s'interfèrent pas :

```
  FONCTION NombreHotes(cidr : ENTIER) → ENTIER
  DÉBUT
      bits_hote ← 32 - cidr   // ce "bits_hote" est local à NombreHotes
      ...
  FIN FONCTION

  FONCTION AutreFonction(n : ENTIER) → ENTIER
  DÉBUT
      bits_hote ← n * 2       // ce "bits_hote" est local à AutreFonction
      ...                      // les deux ne s'interfèrent jamais
  FIN FONCTION
```

---

## Partie 5 — La Valeur Sentinelle : Gérer les Erreurs Proprement

Quand une fonction reçoit une entrée invalide, deux options existent : afficher un message d'erreur (effet de bord — transforme la fonction en procédure hybride, ce qui est peu élégant), ou **retourner une valeur convenue** qui signale l'erreur à l'appelant. Cette valeur convenue s'appelle une **valeur sentinelle**.

Par convention, les fonctions qui retournent un nombre positif utilisent souvent **−1** comme sentinelle d'erreur :

```
  FONCTION NombreHotes(cidr : ENTIER) → ENTIER
  // Retourne -1 si cidr est invalide (hors 0–30).
  DÉBUT
      SI cidr < 0 OU cidr > 30 ALORS
          RETOURNER -1          // sentinelle
      FIN SI
      RETOURNER PUISSANCE(2, 32 - cidr) - 2
  FIN FONCTION
```

L'appelant a la responsabilité de tester la sentinelle avant d'utiliser le résultat :

```
  nb ← NombreHotes(mon_cidr)
  SI nb = -1 ALORS
      AFFICHER "Masque invalide — calcul impossible"
  SINON
      AFFICHER "Hôtes disponibles : " + nb
  FIN SI
```

> 💡 **Le contrat d'une fonction.** Lorsque vous écrivez une fonction, vous établissez un contrat : "si tu m'appelles avec une entrée valide, je te retourne le bon résultat ; si tu m'appelles avec une entrée invalide, je te retourne −1". Ce contrat doit toujours être documenté. C'est la même notion que les préconditions vues en S7 — formalisée ici dans la signature de la fonction.

---

## Partie 6 — Écrire la Bibliothèque Réseau Complète

### 6.1 `NombreHotes(cidr)` — La Fonction Exercice

```
  FONCTION NombreHotes(cidr : ENTIER) → ENTIER
  // Retourne le nombre d'adresses hôtes utilisables dans un sous-réseau /cidr.
  // Précondition : 0 ≤ cidr ≤ 30.
  // Retourne -1 si cidr est hors de cette plage.
  DÉBUT
      SI cidr < 0 OU cidr > 30 ALORS
          RETOURNER -1
      FIN SI
      RETOURNER PUISSANCE(2, 32 - cidr) - 2
  FIN FONCTION
```

**Table de vérification :**

| `cidr` | `32 − cidr` | `2^(32−cidr)` | `− 2` | **Résultat** |
|---|---|---|---|---|
| 30 | 2 | 4 | −2 | **2** (lien point-à-point) |
| 28 | 4 | 16 | −2 | **14** |
| 24 | 8 | 256 | −2 | **254** |
| 20 | 12 | 4 096 | −2 | **4 094** |
| 16 | 16 | 65 536 | −2 | **65 534** |
| 8 | 24 | 16 777 216 | −2 | **16 777 214** |
| 31 | — | — | — | **−1** (sentinelle) |

### 6.2 `CalculerBroadcast(ip, cidr)` — Composition de Fonctions Existantes

Cette fonction illustre la composition : elle s'appuie sur `AND_BINAIRE` et `NOT_BINAIRE` pour produire son résultat.

```
  FONCTION CalculerBroadcast(ip : CHAÎNE, cidr : ENTIER) → CHAÎNE
  // Retourne l'adresse broadcast d'un sous-réseau.
  // Utilise AND_BINAIRE pour l'adresse réseau, NOT_BINAIRE pour le wildcard.
  // Retourne "" (chaîne vide) si ip invalide ou cidr hors plage.
  DÉBUT
      SI NON ValiderIPv4(ip) ALORS
          RETOURNER ""
      FIN SI
      SI cidr < 0 OU cidr > 32 ALORS
          RETOURNER ""
      FIN SI

      reseau   ← AND_BINAIRE(ip, cidr)       // adresse réseau (S4)
      wildcard ← NOT_BINAIRE(cidr)           // masque inversé (S4)
      RETOURNER OR_BINAIRE(reseau, wildcard) // broadcast = réseau OR wildcard
  FIN FONCTION
```

> 💡 **Observer la composition :** `CalculerBroadcast` ne contient aucun calcul binaire direct — elle délègue entièrement aux fonctions `AND_BINAIRE`, `NOT_BINAIRE` et `OR_BINAIRE`. C'est la modularité à l'œuvre : chaque fonction fait une seule chose bien, et les fonctions complexes se construisent par assemblage des fonctions simples.

### 6.3 Refactoriser `GenererIPsReseau` — Avant et Après

**Avant (S8) — calculs inline, moins lisible :**

```
  // Extrait de GenererIPsReseau (S8)
  nb_bits_hote ← 32 - cidr
  nb_hotes     ← PUISSANCE(2, nb_bits_hote) - 2    // calcul dupliqué
  broadcast    ← OR_BINAIRE(reseau, NOT_BINAIRE(cidr))  // calcul inline
```

**Après (S9) — délégation aux fonctions, plus lisible :**

```
  // Même section refactorisée avec les nouvelles fonctions
  nb_hotes  ← NombreHotes(cidr)              // délégation
  broadcast ← CalculerBroadcast(ip_ref, cidr) // délégation
```

Le comportement est identique. Mais la version refactorisée se lit comme un texte : "le nombre d'hôtes est calculé par NombreHotes, le broadcast est calculé par CalculerBroadcast". Un technicien qui découvre ce code comprend instantanément l'intention, sans déchiffrer la formule.

### 6.4 La Bibliothèque Réseau Complète

```
  // ═══════════════════════════════════════════════════════════════
  // BIBLIOTHÈQUE RÉSEAU — BTS SIO SISR Année 1
  // À utiliser dans tous vos programmes d'analyse réseau
  // ═══════════════════════════════════════════════════════════════

  FONCTION ValiderIPv4(ip : CHAÎNE) → BOOLÉEN          // [S6]
  FONCTION AND_BINAIRE(ip : CHAÎNE, cidr : ENTIER) → CHAÎNE    // [S4/S7]
  FONCTION NOT_BINAIRE(cidr : ENTIER) → CHAÎNE                 // [S4]
  FONCTION OR_BINAIRE(a : CHAÎNE, b : CHAÎNE) → CHAÎNE         // [S4]
  FONCTION IP_VERS_ENTIER(ip : CHAÎNE) → ENTIER               // [S8]
  FONCTION ENTIER_VERS_IP(n : ENTIER) → CHAÎNE                 // [S8]
  FONCTION AppartientAuSousReseau(a, b : CHAÎNE,
                                  cidr : ENTIER) → BOOLÉEN     // [S7]
  FONCTION NombreHotes(cidr : ENTIER) → ENTIER                 // [S9] ✓ NOUVEAU
  FONCTION CalculerBroadcast(ip : CHAÎNE,
                             cidr : ENTIER) → CHAÎNE           // [S9] ✓ NOUVEAU

  // ═══════════════════════════════════════════════════════════════
  // PROGRAMME PRINCIPAL — utilise toutes les fonctions ci-dessus
  // ═══════════════════════════════════════════════════════════════

  ALGORITHME AnalyserSousReseau
  DÉBUT
      LIRE ip_saisie
      LIRE cidr_saisi

      SI NON ValiderIPv4(ip_saisie) ALORS
          AFFICHER "IP invalide"
          RETOURNER
      FIN SI

      reseau    ← AND_BINAIRE(ip_saisie, cidr_saisi)
      broadcast ← CalculerBroadcast(ip_saisie, cidr_saisi)
      nb_hotes  ← NombreHotes(cidr_saisi)

      AFFICHER "Réseau    : " + reseau + "/" + cidr_saisi
      AFFICHER "Broadcast : " + broadcast
      AFFICHER "Hôtes     : " + nb_hotes
      AFFICHER "Première  : " + ENTIER_VERS_IP(IP_VERS_ENTIER(reseau) + 1)
      AFFICHER "Dernière  : " + ENTIER_VERS_IP(IP_VERS_ENTIER(broadcast) - 1)
  FIN
```

---

## Partie 7 — Documenter une Fonction

Une fonction sans documentation est une boîte noire illisible. La convention minimale à respecter dans ce module :

```
  FONCTION MaFonction(param : TYPE) → TYPE_RETOUR
  // DESCRIPTION : Ce que fait la fonction en une phrase.
  // PARAMÈTRES  : param — description et contraintes (ex : entre 0 et 32)
  // RETOURNE    : description de la valeur retournée dans le cas normal
  //               et de la valeur sentinelle dans le cas d'erreur
  // EXEMPLES    : MaFonction(24) → 254
  //               MaFonction(99) → -1 (invalide)
  DÉBUT
      ...
  FIN FONCTION
```

---

## Partie 8 — Exercices Guidés

**Exercice 1.1 — Lire une fonction**
Analysez la fonction suivante et répondez aux questions sans l'exécuter : quel est son type de retour ? Que retourne-t-elle si `cidr = 24` ? Si `cidr = 0` ? Quel problème contient-elle ?

```
  FONCTION TailleReseau(cidr : ENTIER) → ENTIER
  DÉBUT
      RETOURNER PUISSANCE(2, 32 - cidr)
  FIN FONCTION
```

**Exercice 1.2 — Compléter une signature**
La définition suivante est incomplète. Identifiez ce qui manque et complétez-la :

```
  ??? EstAdresseReseau(ip : CHAÎNE, cidr : ENTIER)
  DÉBUT
      reseau ← AND_BINAIRE(ip, cidr)
      RETOURNER (ip = reseau)
  FIN ???
```

**Exercice 1.3 — Écrire `MasqueDecimal(cidr)`**
Écrire la fonction `MasqueDecimal(cidr)` qui retourne le masque sous-réseau en notation décimale pointée (ex : `MasqueDecimal(24)` → `"255.255.255.0"`). Utiliser la logique binaire pour construire les 4 octets, ou la table des 9 valeurs possibles par tranche de 8 bits.

**Exercice 1.4 — Refactoriser**
Reprendre l'algorithme `AuditReseau` de S8 et remplacer tous les calculs inline par des appels aux fonctions de la bibliothèque. La logique ne doit pas changer, seule la forme.

---

## Vocabulaire Clé à Maîtriser pour l'Examen

| **Terme** | **Définition** |
|---|---|
| **Fonction** | Sous-programme qui prend des paramètres en entrée et retourne une valeur utilisable dans une expression ou un test |
| **Procédure** | Sous-programme qui produit un effet (affichage, action) sans retourner de valeur exploitable |
| **Paramètre formel** | Variable locale définie dans la signature de la fonction — reçoit la valeur de l'argument à l'appel |
| **Argument** | Valeur (ou variable) fournie à l'appel d'une fonction — copiée dans le paramètre formel |
| **`RETOURNER`** | Instruction qui fournit le résultat d'une fonction et arrête son exécution immédiatement |
| **Portée locale** | Espace de visibilité des variables — une variable locale n'existe qu'à l'intérieur de la fonction qui la déclare |
| **Valeur sentinelle** | Valeur conventionnelle (souvent −1 ou `""`) retournée par une fonction pour signaler une entrée invalide ou une condition d'erreur |
| **Modularité** | Principe de décomposition d'un programme en sous-unités indépendantes et réutilisables (fonctions, procédures) |
| **Bibliothèque** | Ensemble de fonctions réutilisables organisées thématiquement — les fonctions réseau de ce module en sont un exemple |
| **Composition** | Appel d'une fonction depuis l'intérieur d'une autre — `CalculerBroadcast` compose `AND_BINAIRE`, `NOT_BINAIRE` et `OR_BINAIRE` |
| **Refactorisation** | Réécriture d'un algorithme existant pour améliorer sa structure (modularité, lisibilité) sans changer son comportement |
| **Contrat d'une fonction** | Accord implicite entre l'auteur et l'utilisateur : entrées valides → résultat garanti, entrées invalides → sentinelle définie |

---

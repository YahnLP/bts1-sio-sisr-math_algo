---
author: YLP
title: 📖 FICHE DE COURS
---

# 📖 FICHE DE COURS
## Introduction Algorithmique · Pseudo-code · Variables et Types · Validation d'IP

*Version 1.0 — BTS SIO SISR — Année 1 — Semaine 6*
> **Prérequis :** S1–S5 — binaire, Boole, masques de sous-réseau, VLSM

---

## Partie 1 — Qu'est-ce qu'un Algorithme ?

### 1.1 Définition

Un **algorithme** est une suite **finie** d'instructions **non ambiguës** qui, à partir de données en entrée, produit un résultat **correct** en un temps borné.

```
╔══════════════════════════════════════════════════════════════════╗
║              LES 3 PROPRIÉTÉS OBLIGATOIRES                       ║
╠══════════════════════════════════════════════════════════════════╣
║  FINI       Le processus se termine toujours.                    ║
║             Une boucle infinie n'est pas un algorithme.          ║
╠══════════════════════════════════════════════════════════════════╣
║  NON AMBIGU Chaque instruction a exactement une interprétation.  ║
║             "Saler à goût" est ambigu. "LIRE sel" ne l'est pas. ║
╠══════════════════════════════════════════════════════════════════╣
║  CORRECT    Il produit le bon résultat pour TOUTES les entrées   ║
║             valides — y compris les cas limites.                 ║
╚══════════════════════════════════════════════════════════════════╝
```

### 1.2 Algorithme, Pseudo-code, Programme : Trois Niveaux

```
┌─────────────────────────────────────────────────────────────────┐
│  ALGORITHME          La logique — indépendante du langage        │
│  (pensée)            "Je veux vérifier si un nombre est pair"   │
│       ↓                                                         │
│  PSEUDO-CODE         La description lisible — français structuré │
│  (écriture)          SI nombre MOD 2 = 0 ALORS ...              │
│       ↓                                                         │
│  PROGRAMME           L'exécutable — syntaxe d'un vrai langage   │
│  (machine)           Python : if nombre % 2 == 0:               │
│                      Bash   : if [ $((nombre % 2)) -eq 0 ]      │
└─────────────────────────────────────────────────────────────────┘
```
*[Illustration : Trois boîtes empilées verticalement. La boîte du haut (algorithme) contient une ampoule — idée abstraite. La boîte du milieu (pseudo-code) contient une feuille avec des mots structurés. La boîte du bas (programme) contient un écran avec du code coloré. Des flèches descendent de l'une à l'autre, annotées "formalisation" et "traduction".]*

> 💡 **Le pseudo-code n'a pas de syntaxe universelle.** Dans ce cours, nous utilisons le **français structuré** avec les mots-clés : `ALGORITHME`, `DÉBUT`, `FIN`, `SI`, `SINON`, `FIN SI`, `POUR`, `FIN POUR`, `TANT QUE`, `FIN TANT QUE`, `LIRE`, `AFFICHER`, `RETOURNER`.

---

## Partie 2 — Les Structures de Contrôle

### 2.1 La Séquence

La forme la plus simple : les instructions s'exécutent **dans l'ordre, de haut en bas**.

```
  ALGORITHME ExempleSequence
  DÉBUT
      LIRE a
      LIRE b
      somme ← a + b
      AFFICHER somme
  FIN
```

### 2.2 La Condition — SI / SINON / FIN SI

Exécuter des instructions **selon une condition** (un test VRAI ou FAUX).

```
  Forme simple :                  Forme avec alternative :
  ───────────────────             ────────────────────────────
  SI condition ALORS              SI condition ALORS
      instructions                    instructions si VRAI
  FIN SI                          SINON
                                      instructions si FAUX
                                  FIN SI
```

**Exemple :**
```
  SI octet >= 0 ET octet <= 255 ALORS
      AFFICHER "Octet valide"
  SINON
      AFFICHER "Octet hors borne"
  FIN SI
```

> ⚠️ **Règle d'or :** Un SI sans SINON n'est complet que si le cas "FAUX" n'a vraiment aucune conséquence. Si le cas "FAUX" doit être géré, le SINON est obligatoire.

### 2.3 La Boucle POUR

Répéter un bloc d'instructions un **nombre connu de fois**.

```
  POUR variable DE valeur_début À valeur_fin FAIRE
      instructions
  FIN POUR
```

**Exemple — Vérifier les 4 octets d'une IP :**
```
  POUR i DE 1 À 4 FAIRE
      SI octets[i] < 0 OU octets[i] > 255 ALORS
          AFFICHER "Octet " + i + " invalide"
      FIN SI
  FIN POUR
```

### 2.4 La Boucle TANT QUE

Répéter un bloc d'instructions **tant qu'une condition est vraie** (nombre d'itérations inconnu à l'avance).

```
  TANT QUE condition FAIRE
      instructions
      (la condition doit évoluer pour éviter une boucle infinie)
  FIN TANT QUE
```

**Exemple :**
```
  TANT QUE position <= longueur(chaine) FAIRE
      caractere ← chaine[position]
      SI caractere = "." ALORS
          compteur_points ← compteur_points + 1
      FIN SI
      position ← position + 1
  FIN TANT QUE
```

### 2.5 Guide de Choix — Quelle Structure Utiliser ?

```
╔══════════════════════════════════╦══════════════════════════════════╗
║  Situation                       ║  Structure à utiliser            ║
╠══════════════════════════════════╬══════════════════════════════════╣
║  Étapes qui se suivent           ║  SÉQUENCE                        ║
║  Tester une condition            ║  SI / SINON / FIN SI             ║
║  Répéter N fois (N connu)        ║  POUR ... DE ... À ...           ║
║  Répéter jusqu'à condition fausse║  TANT QUE                        ║
║  Répéter au moins une fois       ║  RÉPÉTER ... JUSQU'À (variante)  ║
╚══════════════════════════════════╩══════════════════════════════════╝
```

---

## Partie 3 — Variables et Types

### 3.1 Définitions Fondamentales

```
╔══════════════════════════════════════════════════════════════════╗
║  VARIABLE  : espace mémoire nommé dont la valeur peut changer    ║
║              Exemple : compteur ← 0  puis  compteur ← compteur+1║
║                                                                  ║
║  CONSTANTE : valeur fixe qui ne change jamais durant l'exécution ║
║              Exemple : BORNE_MAX ← 255                           ║
║                                                                  ║
║  AFFECTATION (←) : donner une valeur à une variable              ║
║              Exemple : resultat ← VRAI                           ║
╚══════════════════════════════════════════════════════════════════╝
```

> 💡 **Convention :** En pseudo-code, on utilise `←` pour l'affectation (et non `=` qui désigne l'égalité mathématique). Certaines conventions utilisent `:=` ou `=` — vérifiez toujours la convention du cours.

### 3.2 Les 4 Types Fondamentaux

```
╔════════════╦══════════════════╦════════════════════╦══════════════════════════╗
║  TYPE      ║  Valeurs         ║  Exemples          ║  En binaire (lien S1–S3) ║
╠════════════╬══════════════════╬════════════════════╬══════════════════════════╣
║  ENTIER    ║  …−2, −1, 0, 1…  ║  octet ← 192       ║  11000000 sur 8 bits     ║
║            ║  Nombres entiers ║  port  ← 443        ║  Bornes déf. par nb bits ║
╠════════════╬══════════════════╬════════════════════╬══════════════════════════╣
║  RÉEL      ║  Décimaux        ║  taux ← 3.14        ║  Norme IEEE 754          ║
║            ║  (virgule flot.) ║  ratio ← 0.931      ║  (hors programme)        ║
╠════════════╬══════════════════╬════════════════════╬══════════════════════════╣
║  CHAÎNE    ║  Texte           ║  ip ← "192.168.1.1" ║  Suite d'octets ASCII    ║
║            ║  (entre guillem.)║  msg ← "Valide"     ║  "A"=65, "0"=48, "."=46  ║
╠════════════╬══════════════════╬════════════════════╬══════════════════════════╣
║  BOOLÉEN   ║  VRAI ou FAUX    ║  valide ← VRAI      ║  1 seul bit : 1 ou 0     ║
║            ║  Résultat test   ║  ok ← (a > b)       ║  Lien direct avec S3     ║
╚════════════╩══════════════════╩════════════════════╩══════════════════════════╝
```
*[Illustration : Quatre cases colorées côte à côte représentant les 4 types. Chaque case contient : le nom du type en grand, un exemple de variable, et une représentation binaire symbolique. ENTIER en bleu, RÉEL en vert, CHAÎNE en orange, BOOLÉEN en rouge.]*

### 3.3 Opérations par Type

**Sur les ENTIERS :**
```
  + − × ÷      Arithmétique standard
  MOD          Reste de la division entière (12 MOD 5 = 2)
  DIV          Division entière (12 DIV 5 = 2)
  = < > <= >=  Comparaisons → résultat BOOLÉEN
```

**Sur les CHAÎNES :**
```
  LONGUEUR(s)       Nombre de caractères de s
  DECOUPER(s, sep)  Découpe s selon le séparateur sep → tableau de parties
  CONVERTIR_EN_ENTIER(s)  Convertit "192" en entier 192
  CONTIENT(s, c)    VRAI si la chaîne s contient le caractère c
  s[i]              Le i-ème caractère de s (souvent indexé à partir de 1)
```

**Sur les BOOLÉENS :**
```
  ET  (AND)    VRAI si les deux opérandes sont VRAIS
  OU  (OR)     VRAI si au moins un opérande est VRAI
  NON (NOT)    Inverse la valeur
  (Lien direct avec l'algèbre de Boole — S3)
```

### 3.4 Un Piège Fréquent : CHAÎNE vs. ENTIER

```
  "255"   est une CHAÎNE de 3 caractères : '2', '5', '5'
   255    est un ENTIER qui vaut deux cent cinquante-cinq

  On ne peut pas comparer une CHAÎNE à un ENTIER :
  ❌ SI "255" > 200 ALORS ...   ← comparaison invalide (types différents)
  ✅ SI CONVERTIR_EN_ENTIER("255") > 200 ALORS ...   ← correct

  → Avant de tester si un octet est entre 0 et 255,
    il faut d'abord le convertir de CHAÎNE en ENTIER.
```

---

## Partie 4 — Construire un Algorithme : La Méthode

### 4.1 La Démarche en 5 Étapes

```
  ÉTAPE 1 — COMPRENDRE  : Que doit faire l'algorithme ?
                          Quelles sont les entrées ? les sorties ?

  ÉTAPE 2 — DÉCOMPOSER  : Découper le problème en sous-problèmes
                          indépendants et plus simples.

  ÉTAPE 3 — ÉCRIRE      : Rédiger le pseudo-code, structure par structure.
                          Commencer par les cas simples, puis les cas limites.

  ÉTAPE 4 — TESTER      : Exécuter mentalement l'algorithme avec
                          plusieurs exemples (cas normal + cas limites).

  ÉTAPE 5 — AMÉLIORER   : Corriger les erreurs trouvées, simplifier
                          les redondances, ajouter les cas manquants.
```

### 4.2 Exemple Guidé — Algorithme "Nombre Pair ou Impair"

```
  ÉTAPE 1 : Entrée = un entier / Sortie = "PAIR" ou "IMPAIR"
  ÉTAPE 2 : Un nombre est pair si son reste par 2 vaut 0.
  ÉTAPE 3 :

  ALGORITHME PariteNombre
  DÉBUT
      LIRE nombre
      SI nombre MOD 2 = 0 ALORS
          AFFICHER "PAIR"
      SINON
          AFFICHER "IMPAIR"
      FIN SI
  FIN

  ÉTAPE 4 : Test avec 4 → 4 MOD 2 = 0 → "PAIR" ✓
            Test avec 7 → 7 MOD 2 = 1 → "IMPAIR" ✓
            Test avec 0 → 0 MOD 2 = 0 → "PAIR" ✓ (cas limite)
  ÉTAPE 5 : Algorithme complet et correct.
```

---

## Partie 5 — Application : Validation d'une Adresse IPv4

### 5.1 Le Problème

**Question :** Écrire un algorithme qui prend en entrée une chaîne de caractères et détermine si elle représente une adresse IPv4 **valide**.

**Exemples :**
```
  "192.168.1.1"     → VALIDE   ✓
  "10.0.0.255"      → VALIDE   ✓
  "256.1.1.1"       → INVALIDE (256 > 255)
  "192.168.1"       → INVALIDE (3 parties seulement)
  "192.168.1.abc"   → INVALIDE (partie non numérique)
  "192.168.1.1.5"   → INVALIDE (5 parties)
  ""                → INVALIDE (chaîne vide)
```

### 5.2 Décomposition en 4 Niveaux

```
  PROBLÈME : "L'adresse est-elle valide ?"
  │
  ├── NIVEAU 1 — FORMAT
  │   Est-ce qu'elle contient exactement 3 points → 4 parties ?
  │   Sinon → INVALIDE immédiatement.
  │
  ├── NIVEAU 2 — TYPE
  │   Chaque partie est-elle bien un entier (que des chiffres) ?
  │   Sinon → INVALIDE.
  │
  ├── NIVEAU 3 — BORNE
  │   Chaque entier est-il entre 0 et 255 inclus ?
  │   Sinon → INVALIDE.
  │
  └── NIVEAU 4 — (BONUS) CAS SPÉCIAUX
      0.0.0.0 (réseau nul), 255.255.255.255 (broadcast général),
      127.x.x.x (loopback) → selon le contexte.
```

> 💡 **La décomposition en niveaux est elle-même une technique algorithmique.** Chaque niveau filtre les cas invalides et transmet les cas restants au niveau suivant — comme un pipeline de validation. En Bash ou Python, chaque niveau pourrait être une fonction indépendante.

### 5.3 L'Algorithme de Validation — Construction Guidée

#### Version 1 — Squelette (structure générale)

```
  ALGORITHME ValiderIPv4
  ENTRÉE  : chaine (CHAÎNE de caractères)
  SORTIE  : BOOLÉEN (VRAI si valide, FAUX sinon)

  DÉBUT
      // Niveau 1 : vérifier le format (4 parties séparées par ".")
      parties ← DECOUPER(chaine, ".")
      SI LONGUEUR(parties) ≠ 4 ALORS
          RETOURNER FAUX
      FIN SI

      // Niveaux 2 et 3 : vérifier chaque partie
      POUR i DE 1 À 4 FAIRE
          ... (à développer)
      FIN POUR

      // Si on arrive ici, tout est valide
      RETOURNER VRAI
  FIN
```

#### Version 2 — Avec le corps de la boucle (niveaux 2 et 3)

```
  ALGORITHME ValiderIPv4
  ENTRÉE  : chaine (CHAÎNE)
  SORTIE  : BOOLÉEN

  DÉBUT
      // Niveau 1 — Format : exactement 4 parties
      SI LONGUEUR(chaine) = 0 ALORS
          RETOURNER FAUX                     // chaîne vide
      FIN SI

      parties ← DECOUPER(chaine, ".")

      SI LONGUEUR(parties) ≠ 4 ALORS
          RETOURNER FAUX                     // pas 4 parties
      FIN SI

      // Niveaux 2 et 3 — Type et borne pour chaque partie
      POUR i DE 1 À 4 FAIRE

          // Niveau 2 — Chaque partie doit être un entier
          SI NON EST_ENTIER(parties[i]) ALORS
              RETOURNER FAUX                 // contient des lettres
          FIN SI

          // Conversion nécessaire : CHAÎNE → ENTIER pour comparer
          valeur ← CONVERTIR_EN_ENTIER(parties[i])

          // Niveau 3 — Borne entre 0 et 255
          SI valeur < 0 OU valeur > 255 ALORS
              RETOURNER FAUX                 // hors borne
          FIN SI

      FIN POUR

      // Tous les contrôles passés → adresse valide
      RETOURNER VRAI
  FIN
```

> 💡 **`EST_ENTIER(s)` est une fonction auxiliaire** qui vérifie que chaque caractère de la chaîne est un chiffre (0–9). Elle peut être considérée comme une "boîte noire" à ce stade, ou développée comme exercice avancé.

#### Version 3 — Avec affichage du résultat (programme complet)

```
  ALGORITHME ProgrammeValidationIP
  DÉBUT
      AFFICHER "Entrez une adresse IP : "
      LIRE saisie

      SI ValiderIPv4(saisie) ALORS
          AFFICHER saisie + " → ADRESSE VALIDE"
      SINON
          AFFICHER saisie + " → ADRESSE INVALIDE"
      FIN SI
  FIN
```

> 💡 **On appelle ici l'algorithme `ValiderIPv4` comme une **fonction** — un sous-algorithme réutilisable. C'est le premier exemple de modularité : décomposer un grand algorithme en fonctions indépendantes. On développera ce concept en S7.

---

## Partie 6 — Tester son Algorithme : Le Jeu des Cas Limites

Un algorithme n'est pas fiable s'il n'a été testé que sur des cas "faciles". Il faut systématiquement tester les **cas limites** et les **cas d'erreur**.

### Tableau de Tests pour ValiderIPv4

Avant d'exécuter le tableau, prédire le résultat attendu — puis vérifier en "jouant la machine" :

| **Entrée (saisie)** | **Résultat attendu** | **Pourquoi** |
|---|---|---|
| `"192.168.1.1"` | VALIDE | Cas nominal standard |
| `"0.0.0.0"` | VALIDE | Valeurs minimales — cas limite bas |
| `"255.255.255.255"` | VALIDE | Valeurs maximales — cas limite haut |
| `"256.1.1.1"` | INVALIDE | Un octet dépasse 255 |
| `"192.168.1"` | INVALIDE | Seulement 3 parties |
| `"192.168.1.1.5"` | INVALIDE | 5 parties au lieu de 4 |
| `"192.168.abc.1"` | INVALIDE | Partie non numérique |
| `""` | INVALIDE | Chaîne vide |
| `"192.168.01.1"` | À discuter | "01" — entier valide (1) ou ambigu ? |

> 💡 **Le dernier cas est intentionnellement ambigu.** "01" est-il un entier valide (1) ou doit-on rejeter les zéros préfixes ? Il n'y a pas de réponse universelle — cela dépend du contexte d'utilisation. C'est exactement ce type de question qu'un technicien doit poser à son responsable avant d'écrire un script de validation.

---

## Partie 7 — Exercices Guidés

### Série 1 — Algorithmes Simples

**Exercice 1.1 — Maximum de deux nombres**
Écrire un algorithme qui lit deux entiers et affiche le plus grand.

**Exercice 1.2 — Parité d'une liste**
Écrire un algorithme qui lit 5 entiers et affiche combien sont pairs.

**Exercice 1.3 — Validation d'un port réseau**
Écrire un algorithme qui lit un entier et vérifie s'il peut être un numéro de port valide (entre 0 et 65535). Distinguer les ports réservés (0–1023) des ports utilisateur (1024–65535).

**Exercice 1.4 — Conversion décimal → binaire**
Écrire en pseudo-code l'algorithme de conversion d'un entier décimal en binaire par divisions successives (l'algorithme que vous avez appris en S1, mais formalisé).

### Série 2 — Enrichissement de l'Algorithme IP

**Exercice 2.1 — Ajouter la détection du loopback**
Modifier l'algorithme `ValiderIPv4` pour détecter l'adresse loopback (127.x.x.x) et afficher un message spécifique.

**Exercice 2.2 — Compter les adresses invalides**
Écrire un algorithme qui lit 10 adresses IP et compte combien sont invalides, en utilisant `ValiderIPv4` comme sous-algorithme.

**Exercice 2.3 — Validation d'un masque**
Écrire l'algorithme de validation d'un masque de sous-réseau. Rappel : chaque octet doit valoir 0, 128, 192, 224, 240, 248, 252, 254 ou 255 — et une fois qu'un octet vaut 0, tous les suivants doivent valoir 0.

---

## Vocabulaire Clé à Maîtriser pour l'Examen

| **Terme** | **Définition** |
|---|---|
| **Algorithme** | Suite finie d'instructions non ambiguës qui produit un résultat correct pour toutes les entrées valides |
| **Pseudo-code** | Description d'un algorithme dans un langage structuré lisible par un humain, indépendant d'un langage de programmation |
| **Variable** | Espace mémoire nommé dont la valeur peut changer pendant l'exécution |
| **Constante** | Valeur fixe qui ne change jamais pendant l'exécution |
| **Affectation (←)** | Opération donnant une valeur à une variable |
| **Type** | Nature d'une donnée (ENTIER, RÉEL, CHAÎNE, BOOLÉEN) qui détermine les valeurs possibles et les opérations autorisées |
| **ENTIER** | Type pour les nombres entiers relatifs — borné par le nombre de bits alloués |
| **CHAÎNE** | Type pour le texte — suite de caractères encodés en ASCII/UTF-8 |
| **BOOLÉEN** | Type à deux valeurs : VRAI (1) ou FAUX (0) — lien direct avec l'algèbre de Boole |
| **Séquence** | Exécution des instructions dans l'ordre, de haut en bas |
| **Condition (SI)** | Structure exécutant des instructions selon qu'une condition est vraie ou fausse |
| **Boucle POUR** | Répétition d'un bloc un nombre connu de fois |
| **Boucle TANT QUE** | Répétition d'un bloc tant qu'une condition reste vraie |
| **Cas limite** | Valeur d'entrée à la frontière des conditions (0, 255, chaîne vide...) — test obligatoire |
| **Décomposition** | Technique algorithmique consistant à découper un problème complexe en sous-problèmes indépendants plus simples |

---

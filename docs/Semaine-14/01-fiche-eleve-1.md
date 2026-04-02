---
author: YLP
title: 📚 FICHE DE COURS
---

# 📚 FICHE DE COURS ÉLÈVE
## Logique du 1er Ordre : Prédicats, Quantificateurs et Formalisation

*Version 1.0 — BTS SIO SISR — Année 1 — Semaine 14*

---

## 📖 I. Introduction : Pourquoi la Logique Formelle ?

### Le Problème du Langage Naturel

En tant que technicien SISR, vous devez souvent **configurer des règles de sécurité** :
- 🔒 Règles de pare-feu
- 👥 Droits d'accès utilisateurs
- 📊 Politiques de sauvegarde
- 🌐 Filtrage réseau (ACL)

**Problème :** Le langage naturel (français, anglais) est **ambigu**.

**Exemple :**
> "Tous les utilisateurs sauf les administrateurs"

**Combien de lectures possibles ?**
1. Tous les (utilisateurs sauf les administrateurs) → admins exclus
2. (Tous les utilisateurs) sauf les administrateurs → même sens
3. Tous les utilisateurs, sauf que les admins ont des droits en plus → sens différent !

**Conséquence :** Une règle mal comprise = **faille de sécurité**.

### La Solution : La Logique du 1er Ordre

La **logique du 1er ordre** est un langage formel pour exprimer des règles **sans ambiguïté**.

**Avantages :**
- ✅ Précision absolue (un seul sens possible)
- ✅ Indépendant de la technologie (Cisco, Linux, Windows...)
- ✅ Vérifiable mathématiquement (détection de contradictions)
- ✅ Base des outils de vérification formelle

![Illustration : Schéma montrant Français (nuage flou) → Logique formelle (symboles nets) → Configuration technique (code)]
*Légende : La logique formelle est une étape intermédiaire entre le langage naturel et la configuration technique.*

---

## 🔍 II. Les Prédicats : Des Propriétés Vraies ou Fausses

### Définition

> Un **prédicat** est une propriété qui peut être **vraie** ou **fausse** pour un objet donné.

**C'est comme une question à laquelle on répond par OUI (vrai) ou NON (faux).**

### Notation

Un prédicat s'écrit avec une **lettre majuscule** et des **parenthèses** :

```
P(x)   "x possède la propriété P"
```

### Exemples SISR

| **Prédicat** | **Signification** | **Exemple** |
|---|---|---|
| `EstServeur(x)` | "x est un serveur" | `EstServeur(SRV-01)` → Vrai |
| `EstAdmin(x)` | "x est un administrateur" | `EstAdmin(Alice)` → Vrai ou Faux selon Alice |
| `EstDansRéseau(x, r)` | "x est dans le réseau r" | `EstDansRéseau(192.168.1.10, LAN)` → Vrai |
| `PeutAccéder(x, y)` | "x peut accéder à y" | `PeutAccéder(Bob, ServeurWeb)` → Vrai ou Faux |

### Prédicats à 1 Variable vs 2 Variables

**Prédicat à 1 variable :**
```
EstServeur(x)   → x est un serveur
```
- 1 seul paramètre
- Exprime une propriété de l'objet

**Prédicat à 2 variables (relation) :**
```
PeutAccéder(x, y)   → x peut accéder à y
```
- 2 paramètres
- Exprime une relation entre deux objets

![Illustration : À gauche, un carré avec "x" dedans et "EstServeur?" au dessus. À droite, deux carrés "x" et "y" reliés par une flèche "PeutAccéder?"]
*Légende : Prédicat à 1 variable (propriété) vs prédicat à 2 variables (relation).*

---

## 🔢 III. Les Quantificateurs : "Tous" et "Au Moins Un"

### Le Quantificateur Universel : ∀ (Pour Tout)

> **∀** signifie "**pour tout**" ou "**tous les**" (sans exception).

**Notation :**
```
∀x, P(x)   "Pour tout x, P(x) est vrai"
```

**Lecture :** "Pour tout x, x possède la propriété P"

### Exemples SISR

**Exemple 1 :**
```
∀x, EstServeur(x) → AUneIP(x)

Lecture : "Pour tout x, si x est un serveur, alors x a une adresse IP"
Signification : TOUS les serveurs (sans exception) ont une IP
```

**Exemple 2 :**
```
∀x, EstUtilisateur(x) → AUnMotDePasse(x)

Lecture : "Pour tout x, si x est un utilisateur, alors x a un mot de passe"
Signification : TOUS les utilisateurs DOIVENT avoir un mot de passe
```

**⚠️ Point Important :** ∀ signifie **SANS EXCEPTION**. Si UN SEUL élément ne vérifie pas la propriété, la formule est FAUSSE.

### Le Quantificateur Existentiel : ∃ (Il Existe)

> **∃** signifie "**il existe**" ou "**il existe au moins un**".

**Notation :**
```
∃x, P(x)   "Il existe au moins un x tel que P(x) est vrai"
```

**Lecture :** "Il existe au moins un x qui possède la propriété P"

### Exemples SISR

**Exemple 1 :**
```
∃x, EstAdmin(x)

Lecture : "Il existe au moins un x tel que x est un administrateur"
Signification : Il y a AU MOINS UN administrateur dans le système
```

**Exemple 2 :**
```
∃x, (EstServeur(x) ∧ EnPanne(x))

Lecture : "Il existe au moins un x tel que x est un serveur ET x est en panne"
Signification : Au moins un serveur est en panne
```

**⚠️ Point Important :** ∃ signifie **AU MOINS UN**, pas forcément un seul. Il peut y en avoir plusieurs.

### Comparaison ∀ vs ∃

| **Quantificateur** | **Symbole** | **Signification** | **Négation** |
|---|---|---|---|
| Universel | **∀** | TOUS, SANS EXCEPTION | Au moins un ne vérifie PAS |
| Existentiel | **∃** | AU MOINS UN | AUCUN ne vérifie |

**Exemple de négation :**
```
∀x, EstServeur(x) → AUneIP(x)   "Tous les serveurs ont une IP"
Négation : ∃x, EstServeur(x) ∧ ¬AUneIP(x)   "Il existe un serveur sans IP"
```

![Illustration : À gauche, un ensemble avec tous les éléments cochés (∀). À droite, un ensemble avec seulement quelques éléments cochés (∃)]
*Légende : ∀ = TOUS les éléments / ∃ = AU MOINS UN élément*

---

## 🔗 IV. Les Connecteurs Logiques

Les **connecteurs logiques** permettent de combiner des prédicats pour former des **formules complexes**.

### Tableau des Connecteurs

| **Connecteur** | **Symbole** | **Signification** | **Exemple** |
|---|---|---|---|
| **ET** | ∧ | Les deux propriétés sont vraies | `EstAdmin(x) ∧ EstActif(x)` |
| **OU** | ∨ | Au moins une propriété est vraie | `EstAdmin(x) ∨ EstDev(x)` |
| **NON** | ¬ | La propriété est fausse | `¬EstStagiaire(x)` |
| **IMPLIQUE** | → | Si A alors B | `EstAdmin(x) → PeutAccéder(x, y)` |
| **ÉQUIVAUT** | ↔ | A si et seulement si B | `EstVIP(x) ↔ AAccèsPrioritaire(x)` |

### Détail des Connecteurs

#### 1. ET (Conjonction) : ∧

**Signification :** Les deux conditions doivent être vraies simultanément.

```
EstAdmin(x) ∧ EstActif(x)

Lecture : "x est un administrateur ET x est actif"
Vrai seulement si x est admin ET actif en même temps
```

#### 2. OU (Disjonction) : ∨

**Signification :** Au moins une des deux conditions doit être vraie.

```
EstAdmin(x) ∨ EstDev(x)

Lecture : "x est un administrateur OU x est un développeur"
Vrai si x est admin, OU dev, OU les deux
```

**⚠️ Attention :** En logique, "OU" est **inclusif** (peut être les deux).

#### 3. NON (Négation) : ¬

**Signification :** La condition est fausse.

```
¬EstStagiaire(x)

Lecture : "x n'est PAS un stagiaire"
Vrai si x n'est pas stagiaire
```

#### 4. IMPLIQUE (Implication) : →

**Signification :** Si la première condition est vraie, alors la deuxième l'est aussi.

```
EstAdmin(x) → PeutAccéder(x, ServeurBD)

Lecture : "Si x est un admin, alors x peut accéder au serveur BD"
```

**Table de vérité :**

| **A** | **B** | **A → B** |
|---|---|---|
| Vrai | Vrai | Vrai |
| Vrai | Faux | **Faux** ← Seul cas où c'est faux |
| Faux | Vrai | Vrai |
| Faux | Faux | Vrai |

**⚠️ Point important :** Si A est faux, l'implication est toujours vraie (vacuité).

---

## 📐 V. Variables Libres vs Variables Liées

### Variables Liées

Une **variable est liée** si elle est introduite par un quantificateur (∀ ou ∃).

```
∀x, EstServeur(x) → AUneIP(x)
 ↑ 
 x est liée par ∀
```

**Signification :** x représente **tous les éléments** du domaine, pas un élément spécifique.

### Variables Libres

Une **variable est libre** si elle n'est PAS introduite par un quantificateur.

```
EstServeur(x) → AUneIP(x)
            ↑
            x est libre (pas de quantificateur)
```

**Signification :** x représente **un élément particulier** dont on ne connaît pas encore la valeur.

### Domaine de Quantification

Le **domaine** est l'ensemble des valeurs possibles pour une variable.

**Exemples :**
- Domaine de x : Tous les objets du réseau (utilisateurs, serveurs, imprimantes...)
- Domaine de ip : Toutes les adresses IP possibles (192.168.x.x)

---

## 💼 VI. Application SISR : Formaliser des Règles de Filtrage Réseau

### Cas d'Usage 1 : Règle de Pare-feu Simple

**Règle en français :**
> "Tous les utilisateurs du réseau interne peuvent accéder au serveur web"

**Formalisation :**
```
∀x, (EstUtilisateur(x) ∧ EstDansRéseauInterne(x)) → PeutAccéder(x, ServeurWeb)
```

**Lecture :** "Pour tout x, si x est un utilisateur ET x est dans le réseau interne, alors x peut accéder au serveur web"

**Traduction en ACL Cisco (aperçu) :**
```
access-list 100 permit tcp 192.168.1.0 0.0.0.255 host 192.168.1.10 eq 80
```

---

### Cas d'Usage 2 : Exclusion (Tous Sauf...)

**Règle en français :**
> "Tous les utilisateurs sauf les stagiaires peuvent accéder au serveur de fichiers"

**Formalisation :**
```
∀x, (EstUtilisateur(x) ∧ ¬EstStagiaire(x)) → PeutAccéder(x, ServeurFichiers)
```

**Lecture :** "Pour tout x, si x est un utilisateur ET x n'est PAS un stagiaire, alors x peut accéder au serveur de fichiers"

---

### Cas d'Usage 3 : Règle avec OU

**Règle en français :**
> "Les administrateurs ou les développeurs peuvent accéder au serveur de base de données"

**Formalisation :**
```
∀x, (EstAdmin(x) ∨ EstDev(x)) → PeutAccéder(x, ServeurBD)
```

**Lecture :** "Pour tout x, si x est un admin OU x est un développeur, alors x peut accéder au serveur BD"

---

### Cas d'Usage 4 : Règle de Sécurité Stricte

**Règle en français :**
> "Seuls les administrateurs peuvent accéder au serveur de production"

**Formalisation :**
```
∀x, PeutAccéder(x, ServeurProduction) → EstAdmin(x)
```

**Lecture :** "Pour tout x, si x peut accéder au serveur de production, alors x est un admin"

**⚠️ Attention à la direction de l'implication !**

---

### Cas d'Usage 5 : Interdiction Absolue

**Règle en français :**
> "Aucun utilisateur externe ne peut accéder au serveur de base de données"

**Formalisation :**
```
∀x, EstUtilisateurExterne(x) → ¬PeutAccéder(x, ServeurBD)
```

**Ou de façon équivalente :**
```
¬∃x, EstUtilisateurExterne(x) ∧ PeutAccéder(x, ServeurBD)
```

**Lecture 1 :** "Pour tout x, si x est un utilisateur externe, alors x ne peut PAS accéder au serveur BD"
**Lecture 2 :** "Il n'existe aucun x tel que x soit un utilisateur externe ET x puisse accéder au serveur BD"

---

## 🔑 VII. Vocabulaire Clé à Maîtriser

| **Terme** | **Définition** |
|---|---|
| **Prédicat** | Propriété qui peut être vraie ou fausse pour un objet |
| **Quantificateur universel (∀)** | "Pour tout" — s'applique à TOUS les éléments sans exception |
| **Quantificateur existentiel (∃)** | "Il existe" — au moins un élément vérifie la propriété |
| **Variable liée** | Variable introduite par un quantificateur (∀x ou ∃x) |
| **Variable libre** | Variable non quantifiée, représente un élément particulier |
| **Domaine** | Ensemble des valeurs possibles pour une variable |
| **Connecteur logique** | Symbole combinant des prédicats (∧, ∨, ¬, →, ↔) |
| **Formule logique** | Expression composée de prédicats, quantificateurs et connecteurs |
| **Implication (→)** | "Si A alors B" — fausse uniquement si A est vrai et B est faux |

---

## 🎯 VIII. Points Clés à Retenir

### ✅ Les 5 Règles d'Or

1. **∀ = TOUS sans exception** : Si on dit ∀x, P(x), cela signifie que TOUS les x vérifient P, pas juste "la plupart".

2. **∃ = AU MOINS UN** : Si on dit ∃x, P(x), il peut y avoir un seul x ou plusieurs qui vérifient P.

3. **L'implication (→) est asymétrique** : A → B ne signifie PAS B → A. L'ordre compte !

4. **Parenthèses = priorité** : Toujours mettre des parenthèses pour lever les ambiguïtés.

5. **Traduire d'abord en français précis** : Avant de formaliser, réécrire la règle en français sans ambiguïté.

### ⚠️ Erreurs Fréquentes

❌ **Erreur 1 : Confondre ∀ et ∃**
```
"Il y a des admins dans le système"
INCORRECT : ∀x, EstAdmin(x)  → "TOUS sont admins" (faux)
CORRECT : ∃x, EstAdmin(x)     → "Il existe au moins un admin" (vrai)
```

❌ **Erreur 2 : Oublier les parenthèses**
```
∀x, EstAdmin(x) ∧ EstActif(x) → PeutAccéder(x, y)

Ambigu ! Deux lectures possibles :
1. ∀x, (EstAdmin(x) ∧ EstActif(x)) → PeutAccéder(x, y)
2. (∀x, EstAdmin(x)) ∧ (EstActif(x) → PeutAccéder(x, y))

TOUJOURS mettre des parenthèses !
```

❌ **Erreur 3 : Inverser l'implication**
```
"Seuls les admins peuvent accéder au serveur"

INCORRECT : ∀x, EstAdmin(x) → PeutAccéder(x, srv)
            → "Les admins peuvent accéder" (mais d'autres aussi ?)

CORRECT : ∀x, PeutAccéder(x, srv) → EstAdmin(x)
          → "Si quelqu'un accède, alors c'est un admin"
```

---

## 📝 Fiche de Référence Symboles Logiques (Aide-Mémoire)

**À garder sous les yeux pendant les exercices :**

```
═══════════════════════════════════════════════════════════════
SYMBOLES DE LOGIQUE DU 1ER ORDRE
═══════════════════════════════════════════════════════════════

QUANTIFICATEURS
───────────────────────────────────────────────────────────────
∀   Pour tout, tous les (SANS EXCEPTION)
∃   Il existe, il existe au moins un

CONNECTEURS LOGIQUES
───────────────────────────────────────────────────────────────
∧   ET (les deux conditions sont vraies)
∨   OU (au moins une condition est vraie)
¬   NON (négation, la condition est fausse)
→   IMPLIQUE (si A alors B)
↔   ÉQUIVAUT (A si et seulement si B)

PRÉDICATS (Exemples)
───────────────────────────────────────────────────────────────
P(x)              x possède la propriété P
R(x, y)           x est en relation R avec y
EstAdmin(x)       x est un administrateur
PeutAccéder(x, y) x peut accéder à y

EXEMPLES DE FORMULES
───────────────────────────────────────────────────────────────
∀x, P(x)                          Tous les x ont la propriété P
∃x, P(x)                          Au moins un x a la propriété P
∀x, P(x) → Q(x)                   Pour tout x, si P(x) alors Q(x)
∀x, (P(x) ∧ Q(x)) → R(x)          Pour tout x, si P(x) et Q(x) alors R(x)
∀x, P(x) ∧ ¬Q(x) → R(x)           Pour tout x, si P(x) et non Q(x) alors R(x)

═══════════════════════════════════════════════════════════════
```

---

## 🧪 IX. Exercices d'Entraînement

### Exercice 1 : Traduire du Français vers la Logique

**Traduisez les phrases suivantes en logique formelle :**

**a)** "Tous les serveurs ont une adresse IP"
```
Réponse : ___________________________________________________________
```

**b)** "Il existe au moins un utilisateur administrateur"
```
Réponse : ___________________________________________________________
```

**c)** "Si un utilisateur est actif, alors il peut se connecter"
```
Réponse : ___________________________________________________________
```

### Exercice 2 : Traduire de la Logique vers le Français

**Traduisez les formules suivantes en français :**

**a)** `∀x, EstServeur(x) → EstDansVLAN(x, "Production")`
```
Réponse : ___________________________________________________________
```

**b)** `∃x, EstUtilisateur(x) ∧ AMotDePasseExpiré(x)`
```
Réponse : ___________________________________________________________
```

**c)** `∀x, (EstAdmin(x) ∨ EstDev(x)) → PeutAccéder(x, ServeurTest)`
```
Réponse : ___________________________________________________________
```

---

## 🚀 Pour Aller Plus Loin (Facultatif)

### Logique du 2ème Ordre

La logique du 1er ordre quantifie sur les **objets** (utilisateurs, serveurs).
La logique du 2ème ordre quantifie aussi sur les **prédicats** (propriétés elles-mêmes).

**Exemple :**
```
∀P, (∀x, P(x)) → ∃y, P(y)

"Pour toute propriété P, si tous les x ont P, alors il existe un y qui a P"
```

### Outils de Vérification Formelle

**En entreprise, on utilise des outils pour vérifier automatiquement les règles :**
- **Z3** (Microsoft) : Solveur SAT/SMT pour vérifier la cohérence de formules
- **Prolog** : Langage de programmation logique
- **TLA+** : Langage de spécification formelle (Amazon l'utilise)

Ces outils prennent des règles formalisées en logique et vérifient :
- Pas de contradiction
- Pas de faille de sécurité
- Cohérence globale du système

---

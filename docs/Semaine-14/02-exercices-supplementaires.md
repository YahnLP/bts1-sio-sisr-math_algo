---
author: YLP
title: 🔧 FICHE D'EXERCICES SUPPLÉMENTAIRE
---

# 🔧 FICHE D'EXERCICES SUPPLÉMENTAIRES S14
## Logique du 1er Ordre : Entraînement Approfondi

---

## 📋 Informations Générales

| **Champ** | **Détail** |
|-----------|-----------|
| **Public** | Tous les étudiants (facultatif) |
| **Durée** | 1-2 heures de travail personnel |
| **Modalité** | Travail individuel en autonomie |
| **Objectif** | Approfondir la maîtrise de la logique formelle |

---

## 🎯 Objectifs de la Fiche

Cette fiche d'exercices supplémentaires a pour but de :
- ✅ S'entraîner sur des cas variés de formalisation
- ✅ Approfondir la compréhension des quantificateurs
- ✅ Pratiquer la traduction bidirectionnelle (français ↔ logique)
- ✅ Se préparer au devoir S14

---

## 📊 Structure de la Fiche

Cette fiche contient **4 séries d'exercices** :

1. **Série A** : Traductions simples (Niveau Débutant)
2. **Série B** : Formalisations intermédiaires (Niveau Moyen)
3. **Série C** : Cas complexes avec négations (Niveau Avancé)
4. **Série D** : Applications SISR avancées (Niveau Expert)

**⚠️ Recommandation :** Faites au minimum la série A et B. Les séries C et D sont pour ceux qui veulent aller plus loin.

---

# 📘 SÉRIE A : TRADUCTIONS SIMPLES (Niveau Débutant)

**Prédicats disponibles :**
```
EstUtilisateur(x)     : x est un utilisateur
EstServeur(x)         : x est un serveur
EstActif(x)           : x est actif
AUneIP(x)             : x a une adresse IP
EstDansVLAN(x, v)     : x est dans le VLAN v
```

---

## Exercice A1 : Traduction Français → Logique

**A1.1** "Tous les serveurs ont une adresse IP"
```
Réponse : ___________________________________________________________
```

**A1.2** "Il existe au moins un utilisateur actif"
```
Réponse : ___________________________________________________________
```

**A1.3** "Tous les serveurs sont dans le VLAN 10"
```
Réponse : ___________________________________________________________
```

**A1.4** "Il existe un serveur sans adresse IP"
```
Réponse : ___________________________________________________________
```

---

## Exercice A2 : Traduction Logique → Français

**A2.1** `∀x, EstUtilisateur(x) → EstActif(x)`
```
Réponse : ___________________________________________________________
```

**A2.2** `∃x, EstServeur(x) ∧ EstDansVLAN(x, "DMZ")`
```
Réponse : ___________________________________________________________
```

**A2.3** `∀x, EstServeur(x) → AUneIP(x)`
```
Réponse : ___________________________________________________________
```

---

## ✅ Correction Série A

### Exercice A1

**A1.1** `∀x, EstServeur(x) → AUneIP(x)`
**A1.2** `∃x, EstUtilisateur(x) ∧ EstActif(x)`
**A1.3** `∀x, EstServeur(x) → EstDansVLAN(x, 10)`
**A1.4** `∃x, EstServeur(x) ∧ ¬AUneIP(x)`

### Exercice A2

**A2.1** "Tous les utilisateurs sont actifs"
**A2.2** "Il existe au moins un serveur dans la DMZ"
**A2.3** "Tous les serveurs ont une adresse IP"

---

---

# 📘 SÉRIE B : FORMALISATIONS INTERMÉDIAIRES (Niveau Moyen)

**Prédicats disponibles :**
```
EstAdmin(x)           : x est un administrateur
EstDev(x)             : x est un développeur
EstUser(x)            : x est un utilisateur simple
PeutAccéder(x, y)     : x peut accéder à y
EstServeur(x)         : x est un serveur
AMotDePasseFort(x)    : x a un mot de passe fort
EstDansRéseau(x, r)   : x est dans le réseau r
```

---

## Exercice B1 : Règles avec Implication

**B1.1** "Si un utilisateur a un mot de passe fort, alors il peut accéder au serveur web"
```
Réponse : ___________________________________________________________
```

**B1.2** "Tous les administrateurs peuvent accéder à tous les serveurs"
```
Réponse : ___________________________________________________________
```

**B1.3** "Si un utilisateur est dans le réseau interne, alors il peut accéder au serveur de fichiers"
```
Réponse : ___________________________________________________________
___________________________________________________________________
```

---

## Exercice B2 : Règles avec ET/OU

**B2.1** "Les administrateurs ou les développeurs peuvent accéder au serveur de test"
```
Réponse : ___________________________________________________________
```

**B2.2** "Les utilisateurs qui ont un mot de passe fort et qui sont dans le réseau interne peuvent accéder au serveur de production"
```
Réponse : ___________________________________________________________
___________________________________________________________________
```

**B2.3** "Un utilisateur peut accéder au serveur web s'il est admin OU s'il est développeur OU s'il est dans le réseau interne"
```
Réponse : ___________________________________________________________
___________________________________________________________________
```

---

## Exercice B3 : Traduction Logique → Français

**B3.1** `∀x, ∀y, (EstAdmin(x) ∧ EstServeur(y)) → PeutAccéder(x, y)`
```
Réponse : ___________________________________________________________
```

**B3.2** `∀x, (EstDev(x) ∨ EstAdmin(x)) → AMotDePasseFort(x)`
```
Réponse : ___________________________________________________________
```

**B3.3** `∃x, EstUser(x) ∧ ¬AMotDePasseFort(x)`
```
Réponse : ___________________________________________________________
```

---

## ✅ Correction Série B

### Exercice B1

**B1.1** `∀x, (EstUser(x) ∧ AMotDePasseFort(x)) → PeutAccéder(x, ServeurWeb)`
**B1.2** `∀x, ∀y, (EstAdmin(x) ∧ EstServeur(y)) → PeutAccéder(x, y)`
**B1.3** `∀x, EstDansRéseau(x, "Interne") → PeutAccéder(x, ServeurFichiers)`

### Exercice B2

**B2.1** `∀x, (EstAdmin(x) ∨ EstDev(x)) → PeutAccéder(x, ServeurTest)`
**B2.2** `∀x, (EstUser(x) ∧ AMotDePasseFort(x) ∧ EstDansRéseau(x, "Interne")) → PeutAccéder(x, ServeurProd)`
**B2.3** `∀x, (EstAdmin(x) ∨ EstDev(x) ∨ EstDansRéseau(x, "Interne")) → PeutAccéder(x, ServeurWeb)`

### Exercice B3

**B3.1** "Tous les administrateurs peuvent accéder à tous les serveurs"
**B3.2** "Tous les développeurs ou administrateurs ont un mot de passe fort"
**B3.3** "Il existe au moins un utilisateur qui n'a pas de mot de passe fort"

---

---

# 📘 SÉRIE C : CAS COMPLEXES AVEC NÉGATIONS (Niveau Avancé)

**Prédicats disponibles :**
```
EstEmployé(x)         : x est un employé
EstStagiaire(x)       : x est un stagiaire
EstExterne(x)         : x est un consultant externe
PeutAccéder(x, y)     : x peut accéder à y
EstVIP(x)             : x est un utilisateur VIP
EstBanni(x)           : x est banni du système
EstSensible(y)        : y est un serveur sensible
```

---

## Exercice C1 : "Tous Sauf..."

**C1.1** "Tous les employés sauf les stagiaires peuvent accéder au serveur de production"
```
Réponse : ___________________________________________________________
___________________________________________________________________
```

**C1.2** "Tous les utilisateurs peuvent accéder au serveur web, sauf les utilisateurs bannis"
```
Réponse : ___________________________________________________________
___________________________________________________________________
```

---

## Exercice C2 : "Seuls..."

**C2.1** "Seuls les employés VIP peuvent accéder aux serveurs sensibles"
```
Réponse : ___________________________________________________________
___________________________________________________________________
```

**C2.2** "Seuls les employés non-stagiaires peuvent accéder au serveur de base de données"
```
Réponse : ___________________________________________________________
___________________________________________________________________
```

---

## Exercice C3 : "Aucun..." / "Personne..."

**C3.1** "Aucun utilisateur externe ne peut accéder aux serveurs sensibles"
```
Réponse : ___________________________________________________________
___________________________________________________________________
```

**C3.2** "Personne ne peut accéder au serveur de sauvegarde"
```
Réponse : ___________________________________________________________
```

---

## Exercice C4 : Négations Complexes

**C4.1** Traduisez en français : `∀x, ∀y, (EstEmployé(x) ∧ ¬EstVIP(x) ∧ EstSensible(y)) → ¬PeutAccéder(x, y)`
```
Réponse : ___________________________________________________________
___________________________________________________________________
```

**C4.2** Traduisez en français : `¬∃x, (EstExterne(x) ∧ PeutAccéder(x, ServeurProduction))`
```
Réponse : ___________________________________________________________
```

---

## ✅ Correction Série C

### Exercice C1

**C1.1** `∀x, (EstEmployé(x) ∧ ¬EstStagiaire(x)) → PeutAccéder(x, ServeurProd)`
**C1.2** `∀x, (EstUtilisateur(x) ∧ ¬EstBanni(x)) → PeutAccéder(x, ServeurWeb)`

### Exercice C2

**C2.1** `∀x, ∀y, (PeutAccéder(x, y) ∧ EstSensible(y)) → EstVIP(x)`
**C2.2** `∀x, PeutAccéder(x, ServeurBD) → (EstEmployé(x) ∧ ¬EstStagiaire(x))`

### Exercice C3

**C3.1** `∀x, ∀y, (EstExterne(x) ∧ EstSensible(y)) → ¬PeutAccéder(x, y)`
OU `¬∃x, EstExterne(x) ∧ PeutAccéder(x, ServeurSensible)`

**C3.2** `∀x, ¬PeutAccéder(x, ServeurSauvegarde)`
OU `¬∃x, PeutAccéder(x, ServeurSauvegarde)`

### Exercice C4

**C4.1** "Tous les employés non-VIP ne peuvent pas accéder aux serveurs sensibles"
**C4.2** "Aucun utilisateur externe ne peut accéder au serveur de production"

---

---

# 📘 SÉRIE D : APPLICATIONS SISR AVANCÉES (Niveau Expert)

**Infrastructure réseau :**
```
3 VLAN : 
- VLAN 10 : Admins (192.168.10.0/24)
- VLAN 20 : Users (192.168.20.0/24)
- VLAN 30 : Invités (192.168.30.0/24)

5 Serveurs :
- ServeurWeb (192.168.10.10)
- ServeurBD (192.168.10.20)
- ServeurMail (192.168.10.30)
- ServeurFichiers (192.168.10.40)
- ServeurBackup (192.168.10.50)
```

---

## Exercice D1 : Politique de Sécurité Complète

Formalisez les règles suivantes en logique du 1er ordre :

**D1.1** "Les utilisateurs du VLAN Admins peuvent accéder à tous les serveurs"
```
Réponse : ___________________________________________________________
___________________________________________________________________
```

**D1.2** "Les utilisateurs du VLAN Users peuvent accéder au serveur web et au serveur mail uniquement"
```
Réponse : ___________________________________________________________
___________________________________________________________________
___________________________________________________________________
```

**D1.3** "Les utilisateurs du VLAN Invités ne peuvent accéder à aucun serveur"
```
Réponse : ___________________________________________________________
___________________________________________________________________
```

**D1.4** "Le serveur de backup ne peut être accessible que par les admins du VLAN 10 ayant une authentification à deux facteurs"
```
Réponse : ___________________________________________________________
___________________________________________________________________
___________________________________________________________________
```

---

## Exercice D2 : Détection de Règles Contradictoires

Soit les deux règles suivantes :

**Règle 1 :** `∀x, EstDansVLAN(x, 20) → PeutAccéder(x, ServeurWeb)`
**Règle 2 :** `∀x, EstDansVLAN(x, 20) → ¬PeutAccéder(x, ServeurWeb)`

**D2.1** Ces deux règles sont-elles compatibles ? Justifiez.
```
Réponse : ___________________________________________________________
___________________________________________________________________
```

**D2.2** Si elles sont contradictoires, quelle serait la conséquence en termes de configuration réseau ?
```
Réponse : ___________________________________________________________
___________________________________________________________________
```

---

## Exercice D3 : Traduction ACL ↔ Logique Formelle

**D3.1** Traduisez l'ACL Cisco suivante en logique formelle :
```
access-list 100 permit tcp 192.168.10.0 0.0.0.255 host 192.168.10.10 eq 80
access-list 100 deny ip any any
```

```
Réponse :
___________________________________________________________________
___________________________________________________________________
___________________________________________________________________
```

**D3.2** Traduisez la règle logique suivante en ACL Cisco :
```
∀x, ∀y, (EstDansVLAN(x, 10) ∧ EstServeur(y) ∧ y ≠ ServeurBackup) → PeutAccéder(x, y)
```

```
Réponse :
___________________________________________________________________
___________________________________________________________________
___________________________________________________________________
```

---

## ✅ Correction Série D

### Exercice D1

**D1.1** 
```
∀x, ∀y, (EstDansVLAN(x, 10) ∧ EstServeur(y)) → PeutAccéder(x, y)
```

**D1.2** 
```
∀x, (EstDansVLAN(x, 20) ∧ (y = ServeurWeb ∨ y = ServeurMail)) → PeutAccéder(x, y)
∧
∀x, ∀y, (EstDansVLAN(x, 20) ∧ y ≠ ServeurWeb ∧ y ≠ ServeurMail) → ¬PeutAccéder(x, y)
```

**D1.3** 
```
∀x, ∀y, (EstDansVLAN(x, 30) ∧ EstServeur(y)) → ¬PeutAccéder(x, y)
```

**D1.4** 
```
∀x, PeutAccéder(x, ServeurBackup) → (EstDansVLAN(x, 10) ∧ A2FA(x))
```

### Exercice D2

**D2.1** 
```
NON, ces règles sont CONTRADICTOIRES.

Justification :
La règle 1 dit que tous les utilisateurs du VLAN 20 PEUVENT accéder au serveur web.
La règle 2 dit que tous les utilisateurs du VLAN 20 NE PEUVENT PAS accéder au serveur web.

Ces deux règles ne peuvent pas être vraies en même temps.
```

**D2.2** 
```
Conséquence : Blocage total du système ou comportement imprévisible.

Si on configure les deux règles, soit :
1. La dernière règle configurée écrase la première (ordre de priorité)
2. Le pare-feu refuse toute connexion (par sécurité)
3. Erreur de configuration détectée par l'équipement

Risque de faille de sécurité ou de déni de service.
```

### Exercice D3

**D3.1** 
```
Règle 1 : ∀x, (EstDansRéseau(x, "192.168.10.0/24")) → PeutAccéder(x, ServeurWeb, port_80)
Règle 2 : ∀x, ∀y, (x ∉ "192.168.10.0/24") → ¬PeutAccéder(x, y)

OU de façon équivalente :
∀x, (EstDansRéseau(x, "192.168.10.0/24") ∧ y = ServeurWeb) → PeutAccéder(x, y, 80)
∧ ∀x, ¬(EstDansRéseau(x, "192.168.10.0/24") ∧ y = ServeurWeb) → ¬PeutAccéder(x, y)
```

**D3.2** 
```
! Allow VLAN 10 to all servers except Backup
access-list 100 permit ip 192.168.10.0 0.0.0.255 192.168.10.10 0.0.0.0
access-list 100 permit ip 192.168.10.0 0.0.0.255 192.168.10.20 0.0.0.0
access-list 100 permit ip 192.168.10.0 0.0.0.255 192.168.10.30 0.0.0.0
access-list 100 permit ip 192.168.10.0 0.0.0.255 192.168.10.40 0.0.0.0
access-list 100 deny ip 192.168.10.0 0.0.0.255 host 192.168.10.50
access-list 100 deny ip any any
```

---

---

# 📊 GRILLE DE SUIVI PERSONNALISÉ

**À remplir par l'étudiant :**

| **Série** | **Exercices réalisés** | **Niveau de maîtrise** | **Temps passé** |
|---|---|---|---|
| **Série A (Débutant)** | ☐ A1  ☐ A2 | ☐ ✅  ☐ 🟡  ☐ ❌ | _______ min |
| **Série B (Moyen)** | ☐ B1  ☐ B2  ☐ B3 | ☐ ✅  ☐ 🟡  ☐ ❌ | _______ min |
| **Série C (Avancé)** | ☐ C1  ☐ C2  ☐ C3  ☐ C4 | ☐ ✅  ☐ 🟡  ☐ ❌ | _______ min |
| **Série D (Expert)** | ☐ D1  ☐ D2  ☐ D3 | ☐ ✅  ☐ 🟡  ☐ ❌ | _______ min |

**Légende :**
- ✅ = Maîtrisé, aucune erreur
- 🟡 = Compris mais quelques erreurs
- ❌ = Difficultés importantes, à retravailler

---

## 🎯 Auto-Évaluation

**Ce que j'ai bien compris :**
```
___________________________________________________________________
___________________________________________________________________
```

**Ce qui reste difficile pour moi :**
```
___________________________________________________________________
___________________________________________________________________
```

**Questions à poser en cours :**
```
___________________________________________________________________
___________________________________________________________________
```

---

## 📚 Ressources Complémentaires

**Si vous souhaitez aller encore plus loin :**

### Livres
- "Introduction à la logique" — François Rivenc
- "Logic in Computer Science" — Huth & Ryan

### Sites Web
- [Stanford Encyclopedia of Philosophy - Logic](https://plato.stanford.edu/entries/logic-classical/)
- [Khan Academy - Logic](https://www.khanacademy.org/math/algebra-home/alg-intro-to-algebra/algebra-alternate-number-bases/v/number-systems-introduction)

### Outils Interactifs
- [Truth Table Generator](https://web.stanford.edu/class/cs103/tools/truth-table-tool/)
- [Symbolab Logic Calculator](https://www.symbolab.com/solver/logic-calculator)

---

## 💬 Notes Personnelles

**Espace libre pour vos remarques, astuces ou découvertes :**

```
___________________________________________________________________
___________________________________________________________________
___________________________________________________________________
___________________________________________________________________
___________________________________________________________________
```

---
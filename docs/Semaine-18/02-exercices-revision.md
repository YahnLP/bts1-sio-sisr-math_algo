---
author: YLP
title: 📝 EXERCICES
---

---

# 📝 EXERCICES
## Arbres de Décision + Révisions Numération et Subnetting

## ℹ️ Informations Générales

| **Champ** | **Détail** |
|-----------|-----------|
| **Format** | Exercices en séance (pas de rendu) |
| **Modalité** | Travail individuel ou binôme selon les parties |
| **Durée** | 2h15 (45 min arbres + 1h30 révisions) |
| **Objectif** | Pratiquer et consolider avant l'évaluation sommative |

---

---

# 🌳 PARTIE 1 : ARBRES DE DÉCISION (45 min)

## TP : Construire un Arbre de Diagnostic Réseau

**Durée : 35 minutes — Par binômes**

---

## 📋 Consignes

**Objectif :** Créer un arbre de décision complet pour diagnostiquer le problème suivant :

> **Symptôme :** "L'utilisateur ne peut pas accéder au serveur web interne http://intranet.monentreprise.local"

**Contraintes :**
- Votre arbre doit couvrir **au moins 6 causes possibles**
- Suivre la **méthode OSI inversée** (physique → application)
- Utiliser la notation claire : losanges pour les tests, cercles pour les résultats
- Dessiner l'arbre sur papier OU avec Draw.io

---

## 🔍 Causes Possibles (liste non exhaustive)

Voici des causes possibles que votre arbre doit pouvoir diagnostiquer :

1. **Câble réseau débranché**
2. **Switch éteint ou défaillant**
3. **Mauvaise configuration IP** (IP fixe incorrecte)
4. **DHCP défaillant** (IP en 169.254.x.x)
5. **Serveur web éteint**
6. **Service web (Apache/IIS) arrêté**
7. **Firewall bloque le port 80**
8. **DNS ne résout pas "intranet.monentreprise.local"**
9. **Utilisateur tape la mauvaise URL**
10. **Problème de routage** (serveur dans un autre réseau)

**Note :** Vous n'êtes pas obligés de traiter toutes ces causes, mais au moins 6.

---

## 🛠️ Méthodologie Recommandée

**Étape 1 : Identifier les tests (10 min)**

Listez les tests à effectuer pour éliminer chaque cause :

| **Cause** | **Test à effectuer** | **Ordre** |
|---|---|---|
| Câble débranché | Câble branché ? LED allumée ? | 1 |
| Mauvaise IP | Adresse IP valide ? (`ipconfig`) | 2 |
| DHCP défaillant | IP différente de 169.254.x.x ? | 2 |
| Routage | Ping serveur répond ? | 3 |
| Service web | Port 80 ouvert ? (`telnet IP 80`) | 4 |
| DNS | `nslookup intranet.monentreprise.local` résout ? | 5 |

**Étape 2 : Ordonner les tests (5 min)**

Numérotez les tests dans l'ordre logique (du plus simple au plus complexe).

**Étape 3 : Dessiner l'arbre (15 min)**

Commencez par la racine et ajoutez progressivement les nœuds.

**Étape 4 : Vérifier la cohérence (5 min)**

- ✅ Toutes les branches mènent à un résultat (pas de branche "morte")
- ✅ Chaque cause possible est couverte
- ✅ L'ordre suit le modèle OSI

---

## 📊 Grille d'Évaluation (Auto-Évaluation)

**Après avoir terminé, évaluez votre arbre :**

| **Critère** | **Oui** | **Non** |
|---|---|---|
| L'arbre couvre au moins 6 causes | ☐ | ☐ |
| Les tests suivent l'ordre OSI (bas → haut) | ☐ | ☐ |
| Chaque nœud a des branches OUI et NON | ☐ | ☐ |
| Toutes les branches mènent à un résultat | ☐ | ☐ |
| La notation est claire (losanges/cercles) | ☐ | ☐ |
| L'arbre est lisible et organisé | ☐ | ☐ |

**Si vous avez coché tous les OUI : Bravo, votre arbre est complet ! ✅**

---

## 🎯 Exemple de Solution (Partielle)

**Début de l'arbre (3 premiers niveaux) :**

```
    [Pas d'accès à http://intranet.monentreprise.local]
                        |
                        v
              Câble réseau branché ?
               /                    \
             NON                    OUI
              |                      |
        [Rebrancher             LED switch
         le câble]              allumée ?
                                /         \
                              NON         OUI
                               |           |
                        [Vérifier      Adresse IP
                         switch]       valide ?
                                       /        \
                                     NON        OUI
                                      |          |
                                [Vérifier    Ping serveur
                                 DHCP]       192.168.1.10 ?
                                             /            \
                                           NON            OUI
                                            |              |
                                      [Problème        Port 80
                                       routage]        ouvert ?
                                                       /      \
                                                     NON      OUI
                                                      |        |
                                                [Vérifier  DNS
                                                 firewall] résout ?
                                                           /    \
                                                         ...    ...
```

**Continuez l'arbre jusqu'à couvrir toutes les causes !**

---

---

# 📊 PARTIE 2 : RÉVISIONS NUMÉRATION ET SUBNETTING (1h30)

## Diagnostic Initial : Quiz Rapide (10 min)

**Instructions :** Répondez aux 10 questions suivantes pour identifier vos lacunes.

---

### Quiz de Diagnostic

**Question 1 :** Convertir `11010110` (binaire) en décimal.
```
Réponse : _______
```

**Question 2 :** Convertir `157` (décimal) en binaire (8 bits).
```
Réponse : ________________
```

**Question 3 :** Convertir `2F` (hexadécimal) en binaire.
```
Réponse : ________________
```

**Question 4 :** Combien d'hôtes utilisables dans un réseau `/26` ?
```
Réponse : _______
```

**Question 5 :** Quelle est l'adresse réseau de `192.168.10.75/24` ?
```
Réponse : _______________________
```

**Question 6 :** Quelle est l'adresse broadcast de `10.0.0.0/26` ?
```
Réponse : _______________________
```

**Question 7 :** Quel masque correspond à `/27` ?
```
Réponse : _______________________
```

**Question 8 :** Combien de sous-réseaux peut-on créer avec un `/24` découpé en `/26` ?
```
Réponse : _______
```

**Question 9 :** `172.16.45.200` et `172.16.45.130` sont-ils dans le même réseau `/25` ?
```
Réponse : ☐ OUI  ☐ NON
```

**Question 10 :** Addition binaire : `10110 + 01101` = ?
```
Réponse : ________________
```

---

### Correction et Orientation

**Barème :**
- 0-3 bonnes réponses → **Parcours A** (Débutant)
- 4-7 bonnes réponses → **Parcours B** (Moyen)
- 8-10 bonnes réponses → **Parcours C** (Avancé)

**Correction rapide :**
1. 214 | 2. 10011101 | 3. 00101111 | 4. 62 | 5. 192.168.10.0
6. 10.0.0.63 | 7. 255.255.255.224 | 8. 4 | 9. NON | 10. 100011

---

---

## 📘 PARCOURS A : RÉVISIONS DÉBUTANT (45 min numération + 45 min subnetting)

### Section A1 : Numération (45 min)

#### Exercice A1.1 : Conversions Binaire → Décimal (10 min)

Convertissez les nombres binaires suivants en décimal :

**a)** `10101010` = _______

**b)** `11110000` = _______

**c)** `00101101` = _______

**d)** `11111111` = _______

**e)** `10000001` = _______

---

#### Exercice A1.2 : Conversions Décimal → Binaire (15 min)

Convertissez les nombres décimaux suivants en binaire (8 bits) :

**a)** 64 = ________________

**b)** 192 = ________________

**c)** 255 = ________________

**d)** 128 = ________________

**e)** 200 = ________________

**Méthode :** Divisions successives par 2.

---

#### Exercice A1.3 : Hexadécimal (10 min)

**a)** Convertir `A5` (hexadécimal) en binaire :
```
Réponse : ________________
```

**b)** Convertir `FF` (hexadécimal) en décimal :
```
Réponse : _______
```

**c)** Convertir `11001100` (binaire) en hexadécimal :
```
Réponse : _______
```

---

#### Exercice A1.4 : Addition Binaire (10 min)

Effectuez les additions suivantes en binaire :

**a)** `1010 + 0101` = ________________

**b)** `1111 + 0001` = ________________

**c)** `11001 + 00111` = ________________

---

### Section A2 : Subnetting (45 min)

#### Exercice A2.1 : Masques de Base (10 min)

Complétez le tableau :

| **CIDR** | **Masque décimal** | **Hôtes utilisables** |
|---|---|---|
| /24 | 255.255.255.0 | 254 |
| /25 | _______________ | ________ |
| /26 | _______________ | ________ |
| /27 | _______________ | ________ |
| /28 | _______________ | ________ |

---

#### Exercice A2.2 : Adresse Réseau et Broadcast (15 min)

Pour chaque adresse IP, calculez l'adresse réseau et l'adresse broadcast :

**a)** `192.168.1.50/24`
```
Réseau : _______________________
Broadcast : _______________________
```

**b)** `10.0.0.100/25`
```
Réseau : _______________________
Broadcast : _______________________
```

**c)** `172.16.5.200/26`
```
Réseau : _______________________
Broadcast : _______________________
```

---

#### Exercice A2.3 : Plages d'Adresses (10 min)

Pour `192.168.10.0/27` :

**a)** Quelle est la première adresse IP utilisable ?
```
Réponse : _______________________
```

**b)** Quelle est la dernière adresse IP utilisable ?
```
Réponse : _______________________
```

**c)** Combien d'hôtes peuvent être connectés ?
```
Réponse : _______
```

---

#### Exercice A2.4 : Appartenance à un Réseau (10 min)

**a)** `192.168.1.50` et `192.168.1.200` sont-ils dans le même réseau `/24` ?
```
Réponse : ☐ OUI  ☐ NON
```

**b)** `10.0.0.50` et `10.0.0.150` sont-ils dans le même réseau `/25` ?
```
Réponse : ☐ OUI  ☐ NON
```

**c)** `172.16.5.100` et `172.16.5.150` sont-ils dans le même réseau `/26` ?
```
Réponse : ☐ OUI  ☐ NON
```

---

---

## 📘 PARCOURS B : RÉVISIONS MOYEN (45 min numération + 45 min subnetting)

### Section B1 : Numération (45 min)

#### Exercice B1.1 : Conversions Avancées (15 min)

**a)** Convertir `11010110.10101010.11110000.00001111` (notation IP binaire) en décimal :
```
Réponse : _______._______._______._______
```

**b)** Convertir `192.168.15.254` en binaire :
```
Réponse : ________________.________________.________________.________________
```

**c)** Convertir `C0.A8.01.0A` (hexadécimal) en décimal :
```
Réponse : _______._______._______._______
```

---

#### Exercice B1.2 : Opérations Logiques (15 min)

Effectuez les opérations suivantes bit à bit :

**a)** `11001100 AND 11110000` = ________________

**b)** `10101010 OR 01010101` = ________________

**c)** `11111111 XOR 10101010` = ________________

**d)** `NOT 11110000` = ________________

---

#### Exercice B1.3 : Masques de Sous-Réseau en Binaire (15 min)

**a)** Écrire le masque `/26` en binaire :
```
Réponse : ________________.________________.________________.________________
```

**b)** Écrire le masque `255.255.255.224` en CIDR :
```
Réponse : /_______
```

**c)** Calculer l'adresse réseau de `192.168.10.75` avec le masque `255.255.255.192` (en binaire puis en décimal) :
```
IP :    11000000.10101000.00001010.01001011
Masque : ________________.________________.________________.________________
AND :   ________________.________________.________________.________________
Réseau : _______._______._______._______
```

---

### Section B2 : Subnetting (45 min)

#### Exercice B2.1 : Découpage en Sous-Réseaux (20 min)

Vous devez découper le réseau `172.16.0.0/16` en **8 sous-réseaux** égaux.

**a)** Quel sera le nouveau masque ?
```
Nouveau CIDR : /_______
Nouveau masque : _______________________
```

**b)** Donnez les 8 sous-réseaux :
```
Sous-réseau 1 : _______________________
Sous-réseau 2 : _______________________
Sous-réseau 3 : _______________________
Sous-réseau 4 : _______________________
Sous-réseau 5 : _______________________
Sous-réseau 6 : _______________________
Sous-réseau 7 : _______________________
Sous-réseau 8 : _______________________
```

**c)** Combien d'hôtes utilisables par sous-réseau ?
```
Réponse : _______
```

---

#### Exercice B2.2 : Calculs Inversés (15 min)

**a)** Vous avez besoin de connecter **50 hôtes**. Quel est le masque minimum ?
```
Réponse : /_______
```

**b)** Vous avez besoin de **10 sous-réseaux**. Si vous partez de `/24`, quel sera le nouveau masque ?
```
Réponse : /_______
```

---

#### Exercice B2.3 : Cas Pratique (10 min)

Une entreprise a le réseau `10.0.0.0/16`. Elle doit créer 3 sous-réseaux pour :
- VLAN Utilisateurs : 100 hôtes
- VLAN Serveurs : 20 hôtes
- VLAN IoT : 50 hôtes

**Proposez un plan d'adressage :**

| **VLAN** | **Réseau** | **Masque** | **Hôtes disponibles** |
|---|---|---|---|
| Utilisateurs | _________ | /_______ | _______ |
| Serveurs | _________ | /_______ | _______ |
| IoT | _________ | /_______ | _______ |

---

---

## 📘 PARCOURS C : RÉVISIONS AVANCÉ (90 min)

### Exercice C1 : Subnetting VLSM (30 min)

**Contexte :** Vous devez découper le réseau `192.168.100.0/24` avec des **masques variables** (VLSM).

**Besoins :**
- Réseau A : 100 hôtes
- Réseau B : 50 hôtes
- Réseau C : 25 hôtes
- Réseau D : 10 hôtes

**Consigne :** Attribuez les sous-réseaux en partant du plus grand.

| **Réseau** | **Hôtes** | **Masque** | **Réseau** | **1ère IP** | **Dernière IP** | **Broadcast** |
|---|---|---|---|---|---|---|
| A | 100 | /_______ | _________ | _________ | _________ | _________ |
| B | 50 | /_______ | _________ | _________ | _________ | _________ |
| C | 25 | /_______ | _________ | _________ | _________ | _________ |
| D | 10 | /_______ | _________ | _________ | _________ | _________ |

---

### Exercice C2 : Supernetting (20 min)

**Contexte :** Vous devez **agréger** (supernetting) les réseaux suivants en un seul réseau plus grand :
- 192.168.0.0/24
- 192.168.1.0/24
- 192.168.2.0/24
- 192.168.3.0/24

**Question :** Quel est le réseau agrégé (supernet) ?
```
Réponse : _______________________/_______
```

---

### Exercice C3 : IPv6 (Introduction) (20 min)

**a)** Compresser l'adresse IPv6 suivante :
```
2001:0db8:0000:0000:0000:ff00:0042:8329
Réponse : _______________________________________
```

**b)** Quelle est la longueur d'une adresse IPv6 en bits ?
```
Réponse : _______ bits
```

**c)** Combien d'adresses sont disponibles dans un `/64` en IPv6 ?
```
Réponse : 2^_______ = _______ adresses
```

---

### Exercice C4 : Tutorat (20 min)

**Si vous avez terminé tous les exercices**, votre mission est d'**aider un étudiant du parcours A ou B**.

**Consigne :**
- Circulez dans la salle
- Identifiez un étudiant qui a des difficultés
- Expliquez-lui la méthode **sans faire à sa place**
- Validez sa compréhension en lui faisant refaire un exercice similaire

---

---

## 🎯 Récapitulatif et Auto-Évaluation

**Après la séance, remplissez cette fiche :**

```
═══════════════════════════════════════════════════════════════
MA FICHE DE SUIVI PERSONNALISÉE
═══════════════════════════════════════════════════════════════

NUMÉRATION
───────────────────────────────────────────────────────────────
☐ Conversions binaire ↔ décimal : ☐ Maîtrisé  ☐ À revoir
☐ Conversions hexadécimal : ☐ Maîtrisé  ☐ À revoir
☐ Opérations binaires : ☐ Maîtrisé  ☐ À revoir

SUBNETTING
───────────────────────────────────────────────────────────────
☐ Masques CIDR : ☐ Maîtrisé  ☐ À revoir
☐ Adresse réseau et broadcast : ☐ Maîtrisé  ☐ À revoir
☐ Nombre d'hôtes : ☐ Maîtrisé  ☐ À revoir
☐ Découpage en sous-réseaux : ☐ Maîtrisé  ☐ À revoir

ARBRES DE DÉCISION
───────────────────────────────────────────────────────────────
☐ Construction d'un arbre : ☐ Maîtrisé  ☐ À revoir
☐ Diagnostic réseau structuré : ☐ Maîtrisé  ☐ À revoir

PLAN D'ACTION AVANT L'ÉVALUATION S19/S20
───────────────────────────────────────────────────────────────
□ Refaire les exercices S18
□ Faire les exercices supplémentaires (fournis)
□ Demander de l'aide sur : _____________________________
□ Revoir les fiches de cours S1-S8
═══════════════════════════════════════════════════════════════
```

---

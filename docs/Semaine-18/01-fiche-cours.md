---
author: YLP
title: 📚 FICHE DE COURS
---

---

# 📚 FICHE DE COURS
## Arbres de Décision et Diagnostic Réseau

## 📖 I. Introduction : Qu'est-ce qu'un Arbre de Décision ?

### Définition

> Un **arbre de décision** est une structure graphique qui représente un processus de prise de décision sous forme de questions successives menant à des résultats.

**Métaphore :** Imaginez le jeu des "20 questions" :
- Vous pensez à un animal
- Vos amis posent des questions : "Il vit dans l'eau ?", "Il a des poils ?", "Il vole ?"
- Chaque réponse élimine des possibilités
- Après plusieurs questions, ils devinent l'animal

**C'est exactement un arbre de décision !**

### Composants d'un Arbre de Décision

**1. Nœud racine (🔷) :**
- Point de départ
- Représente le problème initial

**2. Nœuds de décision (🔷) :**
- Questions ou tests à effectuer
- Représentés par des **carrés** ou **losanges**

**3. Branches (→) :**
- Réponses possibles (généralement OUI/NON)
- Représentées par des **flèches**

**4. Feuilles (🟢) :**
- Résultats finaux ou solutions
- Représentées par des **cercles** ou **rectangles arrondis**

![Illustration : Arbre simple avec racine, deux branches (OUI/NON), et deux feuilles (résultats)]
*Légende : Structure de base d'un arbre de décision binaire (chaque nœud a 2 branches).*

---

### Exemple Simple : Dois-je Prendre mon Parapluie ?

```
           [Météo du jour]
                 |
                 v
         Il pleut dehors ?
          /            \
        OUI            NON
         |              |
    [Prendre        Il va pleuvoir ?
     parapluie]      /            \
                   OUI            NON
                    |              |
               [Prendre      [Pas besoin
                parapluie]    parapluie]
```

**Lecture de l'arbre :**
1. On part de la racine : "Météo du jour"
2. Test 1 : "Il pleut dehors ?"
   - Si OUI → Résultat : Prendre parapluie
   - Si NON → Test suivant
3. Test 2 : "Il va pleuvoir ?"
   - Si OUI → Résultat : Prendre parapluie
   - Si NON → Résultat : Pas besoin

---

## 🌐 II. Application au Diagnostic Réseau

### Pourquoi Utiliser un Arbre de Décision en SISR ?

**Problème :** Un utilisateur appelle : "Ça ne marche pas !"

**Sans arbre de décision :**
- ❌ On teste au hasard
- ❌ On perd du temps
- ❌ On oublie des étapes
- ❌ Résolution inefficace

**Avec arbre de décision :**
- ✅ Méthode **structurée** et **reproductible**
- ✅ On ne passe pas à côté d'une cause évidente
- ✅ **Documentation** pour les collègues
- ✅ Résolution **rapide** et **efficace**

### Méthode OSI Inversée : Du Bas vers le Haut

**Principe :** En diagnostic réseau, on commence toujours par les **couches basses** du modèle OSI.

**Pourquoi ?** Parce que si la couche 1 (physique) ne fonctionne pas, inutile de tester la couche 7 (application) !

**Ordre de test recommandé :**

| **Ordre** | **Couche OSI** | **Test typique** |
|---|---|---|
| 1 | Physique (1) | Câble branché ? LED allumée ? |
| 2 | Liaison (2) | Switch voit le PC ? |
| 3 | Réseau (3) | Adresse IP valide ? |
| 4 | Réseau (3) | Ping passerelle OK ? |
| 5 | Réseau (3) | Ping DNS (8.8.8.8) OK ? |
| 6 | Application (7) | Résolution DNS OK ? |
| 7 | Application (7) | Service web répond ? |

**Règle d'or :** Toujours commencer par le **plus simple** et le **plus probable**.

---

### Exemple Complet : "Pas d'Accès Internet"

```
              [Utilisateur : Pas d'accès Internet]
                           |
                           v
                  Câble branché ?
                  /            \
                NON            OUI
                 |              |
           [Rebrancher]    LED switch
              câble        allumée ?
                           /        \
                         NON        OUI
                          |          |
                   [Problème    Adresse IP
                    switch]     attribuée ?
                                /          \
                              NON          OUI
                               |            |
                          Vérifier      IP valide
                           DHCP        (pas 169.254) ?
                                       /            \
                                     NON            OUI
                                      |              |
                                [Problème       Ping
                                 DHCP]       passerelle ?
                                             /          \
                                           NON          OUI
                                            |            |
                                      [Problème      Ping
                                       passerelle]  8.8.8.8 ?
                                                    /        \
                                                  NON        OUI
                                                   |          |
                                             [Problème    DNS
                                              routage]   résout ?
                                                         /      \
                                                       NON      OUI
                                                        |        |
                                                  [Problème [Test
                                                   DNS]     app]
```

**Interprétation :**
- Chaque question **élimine** des causes possibles
- On avance **progressivement** du simple au complexe
- On peut **documenter** cet arbre dans une procédure

![Illustration : Arbre de décision complet pour diagnostic réseau avec 7 niveaux]
*Légende : Exemple d'arbre de décision pour le diagnostic "Pas d'accès Internet".*

---

## 🛠️ III. Construire un Arbre de Décision

### Méthodologie en 5 Étapes

**Étape 1 : Identifier le problème (racine)**
```
Exemple : "Utilisateur ne peut pas accéder au serveur web interne"
```

**Étape 2 : Lister les causes possibles**
```
Causes possibles :
1. Câble débranché
2. Switch éteint
3. Mauvaise IP
4. Serveur éteint
5. Firewall bloque
6. Service web arrêté
7. DNS ne résout pas
```

**Étape 3 : Identifier les tests à effectuer**
```
Tests :
- Câble branché ?
- Adresse IP valide ?
- Ping serveur OK ?
- Port 80/443 ouvert ?
- DNS résout le nom ?
```

**Étape 4 : Ordonner les tests (du plus probable au moins probable)**
```
Ordre recommandé :
1. Tests physiques (câble, LED)
2. Tests réseau (IP, ping)
3. Tests applicatifs (DNS, port)
```

**Étape 5 : Dessiner l'arbre**
- Commencer par la racine (problème)
- Ajouter le premier test
- Pour chaque réponse, ajouter soit :
  - Un résultat (feuille) si on a trouvé la cause
  - Un nouveau test (nœud) sinon

---

### Conventions de Notation

**Symboles recommandés :**

| **Élément** | **Symbole** | **Exemple** |
|---|---|---|
| Nœud de décision | 🔷 Losange | "Câble branché ?" |
| Résultat (feuille) | 🟢 Cercle | "Rebrancher câble" |
| Branche OUI | → | Flèche pleine |
| Branche NON | ⇢ | Flèche pointillée |

**Exemple :**
```
    🔷 Test ?
    /      \
  OUI      NON
   |        |
  🟢       🟢
Résultat  Résultat
   A         B
```

---

## 📝 IV. De l'Arbre à l'Algorithme

### Traduction en Pseudo-Code

Un arbre de décision peut être **traduit** en algorithme avec des structures conditionnelles imbriquées.

**Exemple : Arbre "Câble branché ?"**

```
ALGORITHME DiagnosticInternet
VARIABLES
    cable_branche : booléen
    ip_valide : booléen

DÉBUT
    AFFICHER "Diagnostic : Pas d'accès Internet"
    
    AFFICHER "Le câble est-il branché ?"
    LIRE cable_branche
    
    SI cable_branche = FAUX ALORS
        AFFICHER "Solution : Rebrancher le câble"
    SINON
        AFFICHER "L'adresse IP est-elle valide (pas 169.254) ?"
        LIRE ip_valide
        
        SI ip_valide = FAUX ALORS
            AFFICHER "Solution : Vérifier le DHCP"
        SINON
            AFFICHER "Test suivant : Ping passerelle..."
            // Suite du diagnostic
        FIN SI
    FIN SI
FIN
```

**Correspondance :**
- Chaque **nœud** de l'arbre = une structure **SI ... ALORS ... SINON**
- Chaque **feuille** = une instruction **AFFICHER** (résultat)

---

### Traduction en Organigramme

Un arbre peut aussi être représenté en **organigramme** (notation ISO) :

**Symboles de l'organigramme :**

| **Symbole** | **Signification** | **Usage** |
|---|---|---|
| 🟦 Rectangle | Action / Instruction | "Afficher résultat" |
| 🔷 Losange | Test / Condition | "Câble branché ?" |
| ⭕ Ovale | Début / Fin | "Début", "Fin" |
| → Flèche | Flux d'exécution | Ordre des opérations |

**Exemple :**
```
    ⭕ Début
       |
       v
    🔷 Câble ?
    /      \
  OUI      NON
   |        |
   v        v
🔷 IP ?  🟦 Rebrancher
/    \      |
...   ...   v
           ⭕ Fin
```

---

## 🔑 V. Vocabulaire Clé à Maîtriser

| **Terme** | **Définition** |
|---|---|
| **Arbre de décision** | Structure graphique représentant un processus de décision |
| **Nœud racine** | Point de départ de l'arbre (problème initial) |
| **Nœud de décision** | Question ou test à effectuer |
| **Branche** | Lien entre deux nœuds (réponse à une question) |
| **Feuille** | Résultat final ou solution (nœud terminal) |
| **Arbre binaire** | Arbre où chaque nœud a au maximum 2 branches (OUI/NON) |
| **Diagnostic** | Processus d'identification d'une panne ou d'un problème |
| **Troubleshooting** | Résolution méthodique d'un incident |
| **Modèle OSI inversé** | Méthode de diagnostic commençant par les couches basses |

---

## 🎯 VI. Points Clés à Retenir

### ✅ Les 5 Règles d'Or

1. **Commencer par le simple** : Toujours tester les causes **les plus probables** en premier (câble débranché avant problème DNS).

2. **Suivre le modèle OSI** : Diagnostiquer **du bas vers le haut** (couche physique → application).

3. **Une question = deux branches** : Chaque test doit avoir une réponse claire (OUI/NON, OK/KO).

4. **Éviter les questions redondantes** : Ne pas tester deux fois la même chose sous des formes différentes.

5. **Documenter l'arbre** : Un bon arbre de décision doit pouvoir être utilisé par **n'importe qui**, même sans vous.

### ⚠️ Erreurs Fréquentes

❌ **Erreur 1 : Commencer par les tests complexes**
```
Mauvais ordre : "DNS résout ?" → "Ping serveur ?" → "Câble branché ?"
Bon ordre : "Câble branché ?" → "Ping serveur ?" → "DNS résout ?"
```

❌ **Erreur 2 : Oublier des branches**
```
      Test ?
       / \
     OUI  NON
      |    |
   Résultat ???  ← Branche NON non traitée !
```

❌ **Erreur 3 : Arbre trop profond**
```
Un arbre avec 10 niveaux de profondeur est trop complexe.
Préférer plusieurs arbres simples ou regrouper les tests.
```

---

## 📝 Fiche de Référence Rapide (Aide-Mémoire)

**À garder sous les yeux pendant le TP :**

```
═══════════════════════════════════════════════════════════════
ARBRES DE DÉCISION - AIDE-MÉMOIRE
═══════════════════════════════════════════════════════════════

CONSTRUCTION D'UN ARBRE
───────────────────────────────────────────────────────────────
1. Identifier le problème (racine)
2. Lister les causes possibles
3. Identifier les tests à effectuer
4. Ordonner les tests (simple → complexe)
5. Dessiner l'arbre (nœuds → branches → feuilles)

DIAGNOSTIC RÉSEAU (ORDRE RECOMMANDÉ)
───────────────────────────────────────────────────────────────
1. Physique : Câble ? LED ?
2. Liaison : Switch voit le PC ?
3. Réseau : IP valide ? Ping passerelle ?
4. Réseau : Ping DNS (8.8.8.8) ?
5. Application : DNS résout ? Service répond ?

NOTATION
───────────────────────────────────────────────────────────────
🔷 Losange = Question/Test
🟢 Cercle = Résultat/Solution
→ Flèche = Branche (OUI/NON)

TRADUCTION EN ALGORITHME
───────────────────────────────────────────────────────────────
Nœud = SI ... ALORS ... SINON
Feuille = AFFICHER résultat
Branche = Chemin dans le SI/SINON

═══════════════════════════════════════════════════════════════
```

---

## 🧪 VII. Exercices d'Entraînement

### Exercice 1 : Lire un Arbre de Décision

**Soit l'arbre suivant :**

```
        [PC lent]
            |
            v
      RAM > 50% ?
      /         \
    OUI         NON
     |           |
  Fermer     CPU > 80% ?
   apps       /        \
            OUI        NON
             |          |
        Processus   Disque
         intensif   plein ?
                    /     \
                  OUI     NON
                   |       |
               Libérer  [OK
               espace   normal]
```

**Questions :**

**1.1** Quel est le problème initial (racine) ?
```
Réponse : ___________________________________________________________
```

**1.2** Si RAM = 30% et CPU = 90%, quel est le diagnostic ?
```
Réponse : ___________________________________________________________
```

**1.3** Combien de feuilles (résultats finaux) l'arbre contient-il ?
```
Réponse : ___________________________________________________________
```

---

### Exercice 2 : Compléter un Arbre

**Complétez l'arbre suivant pour le diagnostic "Imprimante ne marche pas" :**

```
    [Imprimante ne marche pas]
              |
              v
        Imprimante
        allumée ?
        /        \
      NON        OUI
       |          |
   [Allumer]   _______ ?  ← Complétez
               /        \
             OUI        NON
              |          |
         _______ ?    [Vérifier
         /      \      câble]
       OUI      NON
        |        |
    [_____] [_____]
```

**Consigne :** Remplissez les tests et résultats manquants.

---

## 🚀 Pour Aller Plus Loin (Facultatif)

### Arbres de Décision en Intelligence Artificielle

En **machine learning**, les arbres de décision sont utilisés pour :
- Classifier des données (spam ou non-spam)
- Prédire des valeurs (prix d'une maison)
- Détecter des anomalies (fraude bancaire)

**Différence :**
- En SISR : l'arbre est construit **manuellement** par le technicien
- En IA : l'arbre est construit **automatiquement** par un algorithme d'apprentissage

### Outils de Création d'Arbres

**Outils graphiques :**
- [Draw.io](https://app.diagrams.net/) — Gratuit, en ligne
- [Lucidchart](https://www.lucidchart.com/) — Professionnel
- [yEd](https://www.yworks.com/products/yed) — Logiciel gratuit

**Outils de diagrammes :**
- Microsoft Visio (payant)
- LibreOffice Draw (gratuit)

---

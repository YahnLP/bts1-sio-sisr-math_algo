# Semaine 8 (S8) - BLOC 1
## 🗣️ Relation Client · Communication Non-Technique

---

# 📚 FICHE DE COURS ÉLÈVE
## "Relation Client · Communication avec l'Utilisateur Non-Technique"

*Version 1.0 — BTS SIO SISR — Année 1 — Semaine 8*

---

## 🎯 Compétences Travaillées

| **Code** | **Compétence** |
|----------|---------------|
| **B1.6** | Assurer le support des utilisateurs |
| **B3.3** | Communication professionnelle |

---

## PARTIE I — Comprendre son Interlocuteur

### I.A. Les Profils d'Utilisateurs

Un technicien N1 est en contact avec une grande variété de profils. Adapter son discours commence par **identifier rapidement à qui on parle** :

```
   ┌──────────────────────────────────────────────────────────────────┐
   │                   PROFILS D'UTILISATEURS                         │
   ├─────────────┬──────────────────────────┬────────────────────────┤
   │  PROFIL     │  SIGNAUX                  │  ADAPTATION            │
   ├─────────────┼──────────────────────────┼────────────────────────┤
   │ Novice      │ "L'ordinateur fait des    │ Analogies du quotidien │
   │             │  choses bizarres"          │ Pas d'acronymes        │
   │             │ Appelle tout "l'ordi"      │ Étapes courtes         │
   │             │ Ne sait pas son OS         │ Valider chaque étape   │
   ├─────────────┼──────────────────────────┼────────────────────────┤
   │ Intermédiaire│ Connaît son OS, son       │ Termes courants OK     │
   │             │ logiciel principal         │ Acronymes expliqués    │
   │             │ A déjà réinitialisé        │ Peut faire des actions │
   │             │ son mot de passe           │ guidées à distance     │
   ├─────────────┼──────────────────────────┼────────────────────────┤
   │ Avancé      │ Utilise des termes         │ Peut aller plus vite   │
   │             │ techniques (même           │ Expliquer le "pourquoi"│
   │             │ incorrects)                │ pas seulement le "quoi"│
   │             │ A cherché sur Google       │ Écouter ses hypothèses │
   ├─────────────┼──────────────────────────┼────────────────────────┤
   │ Technicien  │ Vocabulaire précis         │ Communication          │
   │ / Expert    │ Décrit le symptôme         │ technique directe OK   │
   │             │ clairement                 │ Partage d'hypothèses   │
   └─────────────┴──────────────────────────┴────────────────────────┘
```

> ⚠️ **Piège classique :** Un utilisateur qui emploie des mots techniques n'est pas forcément expert. Il a peut-être lu quelque chose sur internet ou répète ce qu'on lui a dit. Vérifier discrètement le niveau réel avant d'aller trop vite.

---

### I.B. L'Écoute Active

L'**écoute active** est la technique qui permet de collecter toutes les informations nécessaires au diagnostic sans interrompre ni orienter l'utilisateur.

**Ses 4 composantes :**

| **Composante** | **Ce que ça signifie** | **Exemple** |
|---|---|---|
| **Écouter sans interrompre** | Laisser l'utilisateur finir avant de parler | Résister à l'envie de proposer une solution dès les premières secondes |
| **Reformuler** | Répéter avec ses propres mots ce qu'on a compris | "Si je comprends bien, votre Excel ne s'ouvre plus depuis ce matin — c'est bien ça ?" |
| **Relancer** | Poser des questions ouvertes pour obtenir plus d'informations | "Et quand vous dites que ça 'plante', que se passe-t-il exactement ?" |
| **Valider** | Confirmer que le problème est bien compris avant d'agir | "Avant de commencer, je récapitule : [résumé]. C'est correct ?" |

---

## PARTIE II — La Structure d'un Appel de Support

### II.A. Les 6 Phases d'un Appel N1 Professionnel

```
   ① ACCUEIL
   ──────────────────────────────────────────────────────
   Se présenter clairement : prénom + service
   Formule standard : "Centre de services SimIO, [Prénom] à votre écoute"
   Ne jamais répondre : "Ouais ?" / "Service informatique ?"

   → Ton : chaleureux, disponible, même si c'est le 20e appel de la journée

   ② IDENTIFICATION
   ──────────────────────────────────────────────────────
   Nom de l'appelant, service, poste (numéro de PC si connu)
   "Pouvez-vous me donner votre nom et votre service ?"
   Ouvrir le ticket PENDANT cette phase, pas après

   → Note : en cas de priorité P1, l'identification peut être rapide ;
     ne pas bloquer 3 minutes si le serveur est en feu

   ③ COLLECTE DU PROBLÈME
   ──────────────────────────────────────────────────────
   Laisser l'utilisateur décrire le problème sans l'interrompre
   Puis poser les 5 questions de diagnostic (vues en S4) :
   Depuis quand ? Qu'est-ce qui a changé ? Reproductible ?
   Isolé ou généralisé ? Message d'erreur ?

   → Technique : prendre des notes en temps réel dans le ticket

   ④ DIAGNOSTIC ET TRAITEMENT
   ──────────────────────────────────────────────────────
   Guider l'utilisateur étape par étape
   Annoncer chaque action AVANT de la faire guider
   "Je vais vous demander de faire [action] — pouvez-vous m'indiquer
    ce qui s'affiche à l'écran ?"

   → Si l'incident dépasse le N1 : annoncer l'escalade clairement et
     rassurer sur le suivi

   ⑤ VALIDATION
   ──────────────────────────────────────────────────────
   Tester la résolution avec l'utilisateur avant de raccrocher
   "Pouvez-vous essayer d'ouvrir votre fichier maintenant ?"
   "Est-ce que ça fonctionne correctement ?"

   → Ne jamais clôturer un ticket sans validation utilisateur sauf
     si l'utilisateur n'est plus joignable (clôture automatique 72h)

   ⑥ CLÔTURE
   ──────────────────────────────────────────────────────
   Résumer ce qui a été fait en une phrase
   Indiquer le numéro de ticket pour référence future
   Proposer une base de connaissances si pertinent
   Formule de clôture : "Y a-t-il autre chose que je puisse faire
   pour vous ? ... Bonne journée."

   → JAMAIS : raccrocher avant que l'utilisateur ait dit au revoir
```

---

### II.B. Ce qu'on Ne Fait Jamais au Téléphone

| **À ne jamais faire** | **Pourquoi** | **Alternative** |
|---|---|---|
| **"Je ne sais pas"** (sans suite) | Donne l'impression d'incompétence | "Je vais vérifier ça et vous rappelle dans l'heure" |
| **Parler à quelqu'un d'autre** en gardant l'appelant en attente sans prévenir | Très mauvaise expérience utilisateur | "Je vous mets en attente 30 secondes, je consulte un collègue" |
| **Utiliser du jargon** non expliqué | Frustration et incompréhension | Reformuler en termes métier |
| **Promettre sans savoir** | "Ce sera réglé dans 10 minutes" alors que c'est inconnu | "Je vous tiens informé dès que j'ai une estimation" |
| **Prendre l'incident personnellement** si l'utilisateur est agressif | Escalade émotionnelle inutile | Technique de désescalade (voir II.C) |
| **Oublier d'ouvrir le ticket** | Perte de traçabilité, SLA non suivi | Ticket ouvert dès le début de l'appel |

---

## PARTIE III — Gérer les Situations Difficiles

### III.A. Typologies d'Utilisateurs Difficiles

| **Profil** | **Comportement** | **Technique recommandée** |
|---|---|---|
| **L'impatient** | "Ça fait 3 fois que j'appelle, ça dure depuis ce matin, j'en ai marre" | Reconnaître l'inconvénient, donner une action concrète immédiate |
| **L'accusateur** | "C'est à cause de votre mise à jour, vous avez tout cassé" | Ne pas se défendre, recadrer sur la résolution : "Je comprends, concentrons-nous sur la solution" |
| **Le paniqué** | "Toutes mes données ont disparu ! Tout est perdu !" | Rassurer d'abord : "On va vérifier ça ensemble, dans la majorité des cas les données sont récupérables" |
| **Le technicien autoproclamé** | "J'ai vérifié le DNS, le ping passe, j'ai désactivé le pare-feu, ça vient de votre côté" | Valoriser ses actions, prendre le relais avec méthode : "Vous avez bien vérifié les bases. Je vais reprendre le diagnostic depuis la couche réseau." |
| **Le muet** | Répond par oui/non, ne décrit pas le problème | Poser des questions fermées précises : "Est-ce que vous voyez un message d'erreur à l'écran ?" |
| **Le bavard** | Raconte 10 minutes de contexte non pertinent | Recadrer avec bienveillance : "Je note tout ça — pour avancer efficacement, puis-je vous poser quelques questions précises ?" |

---

### III.B. La Technique DESC — Désescalade

Quand un utilisateur est agressif ou très mécontent, la technique **DESC** (Décrire, Exprimer, Spécifier, Conséquences) permet de désamorcer sans s'effacer :

```
   D — DÉCRIRE    : Reformuler objectivement la situation
   ──────────────────────────────────────────────────────────────
   "Je comprends que votre service de messagerie est inaccessible
    depuis ce matin et que ça bloque votre travail."

   E — EXPRIMER   : Montrer de l'empathie sincère
   ──────────────────────────────────────────────────────────────
   "C'est effectivement une situation très gênante, et je comprends
    votre frustration."

   S — SPÉCIFIER  : Annoncer une action concrète et un délai
   ──────────────────────────────────────────────────────────────
   "Ce que je vais faire maintenant : je classe votre incident
    en priorité haute et je l'escalade immédiatement à notre
    équipe système."

   C — CONSÉQUENCES : Donner une visibilité sur la suite
   ──────────────────────────────────────────────────────────────
   "Vous recevrez une mise à jour d'ici 30 minutes. Si le problème
    persiste, nous vous contacterons directement."
```

> 📌 **Ce que DESC ne fait pas :** Il ne s'excuse pas excessivement, ne promet pas l'impossible, ne transfère pas la responsabilité sur l'utilisateur. Il **reconnaît, rassure, engage, informe**.

---

## PARTIE IV — Communication Écrite de Support

### IV.A. L'Email de Support Professionnel

Un email de support est différent d'un email personnel : il doit être clair, actionnable et utilisable par n'importe quel technicien qui lirait le ticket ultérieurement.

**Structure d'un bon email de réponse à un incident :**

```
OBJET : [Ticket #XXXX] Réponse — [titre court du problème]

Bonjour [Prénom],

[1. Accusé de réception — 1 phrase]
Nous avons bien pris en compte votre demande concernant [résumé du problème].

[2. Statut actuel — 1-2 phrases]
Votre incident est en cours de traitement / a été résolu / a été escaladé
à notre équipe spécialisée.

[3. Action ou instruction — si applicable]
Pour résoudre votre problème, voici la procédure à suivre :
1. [Étape 1 en termes simples]
2. [Étape 2]
3. [Étape 3]

[4. Confirmation demandée — si résolu]
Pouvez-vous confirmer que tout fonctionne correctement en répondant
à cet email ou en mettant à jour votre ticket sur le portail ?

[5. Référence et contact]
Numéro de votre ticket : #XXXX
En cas de problème persistant : [canal de contact]

Cordialement,
[Prénom] — Centre de services SimIO SARL
```

---

### IV.B. Reformuler sans Vulgariser à l'Excès

Il existe une ligne entre vulgarisation utile et condescendance. Un technicien qui explique "le gros bouton bleu qui fait redémarrer la machine" à un cadre supérieur risque de froisser son interlocuteur.

**Règle d'or :** Viser le **niveau -1** du vocabulaire, pas le niveau -5.

```
   TECHNIQUE         NIVEAU -1 (bon)              NIVEAU -5 (mauvais)
   ─────────         ──────────────────           ──────────────────────
   "Le cache DNS      "Votre ordinateur a           "Votre machine oublie
    est corrompu"      mémorisé une ancienne          pas les adresses des
                       adresse pour un site —          sites, elle se trompe
                       on va la corriger"              de chemin"

   "Vos droits NTFS   "Vous n'avez pas les          "Le dossier, il est
    sont insuffisants" autorisations pour             fermé à clé pour vous"
                       modifier ce dossier"
```

---

## V. Vocabulaire Clé

| **Terme** | **Définition** |
|-----------|---------------|
| **Écoute active** | Technique d'écoute impliquant reformulation, relance et validation |
| **Reformulation** | Répéter avec ses propres mots ce qu'on a compris pour valider |
| **Vulgarisation** | Adapter un message technique pour le rendre accessible à un non-expert |
| **Empathie** | Capacité à reconnaître et comprendre les émotions de l'interlocuteur |
| **Désescalade** | Technique pour apaiser une situation de tension sans s'effacer |
| **DESC** | Décrire / Exprimer / Spécifier / Conséquences — technique de désescalade |
| **Relation client** | Posture professionnelle dans l'interaction avec l'utilisateur du service IT |
| **Communication ascendante** | Communication du technicien vers son responsable (reporting) |
| **Communication descendante** | Communication de la DSI vers les utilisateurs (annonces, procédures) |
| **Ticket de satisfaction** | Évaluation de l'utilisateur sur la qualité du support reçu |

---

## ✅ Auto-évaluation : Suis-je Prêt ?

- [ ] J'identifie rapidement le profil de l'utilisateur (novice / intermédiaire / avancé)
- [ ] J'applique les 6 phases d'un appel N1 dans l'ordre
- [ ] Je reformule une phrase technique en termes compréhensibles
- [ ] J'utilise la technique DESC face à un utilisateur mécontent
- [ ] Je rédige un email de support professionnel avec les 5 sections
- [ ] Je tiens compte du niveau de l'utilisateur pour adapter mon vocabulaire
- [ ] Je sais ce que je ne dois jamais faire au téléphone (liste de S8)


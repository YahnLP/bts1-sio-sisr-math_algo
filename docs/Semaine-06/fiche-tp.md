# Semaine 6 (S6) - BLOC 1
## 🎫 GLPI · Installation · Configuration · Lien OCS · TP Gestion de Tickets

---

# 🖥️ FICHE TP — GLPI : GESTION COMPLÈTE DE TICKETS

*Durée : 75 minutes — Individuel (ou binôme selon la configuration)*

---

## Connexion à GLPI

| **URL** | `http://[IP_SERVEUR]/glpi` |
|---|---|
| **Votre identifiant** | `technicien_[votre_prénom]` |
| **Mot de passe** | `Glpi2024!` (à changer dès la connexion) |

---

## PARTIE A — Prise en Main de l'Interface (10 min)

Avant de traiter les tickets, explorez GLPI pour vous repérer :

| **Tâche d'exploration** | **Menu** | **Fait ?** |
|---|---|---|
| Trouver la liste de tous les ordinateurs importés d'OCS | Parc → Ordinateurs | ☐ |
| Ouvrir la fiche d'un ordinateur et noter les informations matérielles | Parc → Ordinateurs → [Cliquer sur un poste] | ☐ |
| Consulter la liste des tickets ouverts | Assistance → Tickets | ☐ |
| Trouver les catégories de tickets configurées | Config → Intitulés → Catégories des tickets | ☐ |
| Localiser votre profil utilisateur | Prénom en haut à droite → Mon profil | ☐ |

**Note :** Combien d'ordinateurs sont importés d'OCS dans cette instance GLPI ? _______

---

## PARTIE B — Quatre Scénarios de Tickets (65 min)

*Traiter les 4 scénarios dans l'ordre. Chaque scénario simule une situation réelle.*

---

### 🎫 TICKET 1 — Création et Affectation (15 min)

**Rôle :** Vous jouez le technicien N1 qui reçoit un appel et crée le ticket.

**Appel reçu :**
> *"Bonjour, ici Sylvie Mercier du service Comptabilité. J'essaie d'imprimer ma déclaration TVA depuis ce matin mais l'imprimante réseau affiche 'Hors ligne' dans Windows. J'ai essayé de redémarrer l'imprimante et mon PC — ça ne change rien. J'ai besoin d'imprimer avant 11h pour la réunion."*

**Instructions :**

**Étape 1 — Créer le ticket**
- Aller dans : Assistance → Créer un ticket
- Remplir **tous** les champs obligatoires :

| **Champ** | **Valeur à saisir** |
|---|---|
| Type | Incident |
| Titre | |
| Catégorie | |
| Demandeur | Sylvie Mercier (ou créer l'utilisateur si absent) |
| Description | |
| Urgence | |
| Impact | |
| (Priorité calculée automatiquement) | |

**Étape 2 — Lier le ticket à un CI**
- Dans le ticket créé, aller dans l'onglet **Eléments**
- Cliquer sur "Ajouter un élément" → sélectionner un ordinateur ou une imprimante depuis la CMDB

**Étape 3 — Affecter le ticket**
- Onglet **Acteurs** du ticket
- Affecter à vous-même (technicien_[prénom])

**Étape 4 — Changer le statut**
- Passer le ticket de "Nouveau" à "En cours (attribué)"
- Ajouter un **suivi** (message interne) : "Prise en charge — diagnostic en cours"

**N° du ticket créé :** _______

---

### 🎫 TICKET 2 — Suivi et Escalade (15 min)

**Contexte :** Vous reprenez le Ticket 1. Votre diagnostic N1 indique que le problème vient du serveur d'impression — c'est hors de votre périmètre N1.

**Instructions :**

**Étape 1 — Documenter le diagnostic N1 dans le suivi**
- Ouvrir le Ticket 1
- Ajouter un **suivi public** (visible par l'utilisateur) avec :
  - Ce que vous avez vérifié (physique, état Windows, tentatives)
  - Pourquoi vous escaladez

**Étape 2 — Escalader vers N2**
- Dans l'onglet Acteurs → changer le technicien affecté pour le groupe "Techniciens N2 Système" (ou un autre technicien si le groupe n'existe pas)
- Ajouter un **suivi interne** (non visible utilisateur) : motif de l'escalade

**Étape 3 — Informer l'utilisateur**
- Ajouter un **suivi public** : "Votre incident est pris en charge et en cours de résolution par notre équipe spécialisée. Vous serez informé(e) dès la résolution."

**Étape 4 — Vérifier le SLA**
- Dans l'onglet du ticket, le temps restant avant dépassement SLA est-il affiché ?
- Valeur observée : _______

---

### 🎫 TICKET 3 — Demande de Service + Résolution (20 min)

**Rôle :** Vous créez ET résolvez un ticket de demande de service du début à la fin.

**Demande reçue par email :**
> *"Bonjour équipe IT, je suis Karim Benali, nouveau dans le service Marketing depuis lundi. Mon manager m'a dit de contacter le service IT pour avoir accès au dossier partagé Marketing sur le serveur. J'ai essayé d'y accéder hier mais j'obtiens 'Accès refusé'. Merci d'avance."*

**Instructions :**

**Étape 1 — Créer le ticket**

| **Champ** | **Valeur** |
|---|---|
| Type | Demande de service |
| Titre | |
| Catégorie | Accès et Comptes → Droits insuffisants |
| Demandeur | Karim Benali |
| Description | (reformulation professionnelle de l'email) |
| Urgence / Impact | |

**Étape 2 — Traiter la demande (simulation)**

Simuler les actions suivantes et les documenter dans le suivi :
1. Vérifier que Karim Benali a bien un compte AD actif
2. Vérifier son appartenance au groupe `GRP_MARKETING`
3. Ajouter Karim au groupe si absent (ou documenter l'action à effectuer)
4. Vérifier les droits NTFS du dossier Marketing pour `GRP_MARKETING`

Ajouter un **suivi interne** pour chacune des étapes ci-dessus.

**Étape 3 — Rédiger la solution et passer en Résolu**
- Onglet **Solution** du ticket
- Rédiger la solution complète en 3 à 5 lignes
- Passer le statut à **Résolu**

**Étape 4 — Lier à la base de connaissances**
- Si votre GLPI dispose de la KB, créer une **fiche KB** depuis la solution
- Titre KB : "Accès refusé dossier partagé — utilisateur non membre du groupe AD"

**N° du ticket :** _______ **Heure de clôture :** _______

---

### 🎫 TICKET 4 — Clôture + Tableau de Bord (15 min)

**Contexte :** L'utilisateur du Ticket 3 a rappelé pour confirmer que l'accès fonctionne. Vous clôturez le ticket et consultez les statistiques.

**Étape 1 — Clôturer le ticket**
- Ajouter un **suivi public** de confirmation : "L'accès au dossier partagé Marketing a été rétabli. N'hésitez pas à nous contacter si le problème réapparaît."
- Passer le statut de "Résolu" à **Clôturé**

**Étape 2 — Calculer le MTTR**

| **Information** | **Valeur** |
|---|---|
| Date/heure d'ouverture du ticket | |
| Date/heure de clôture | |
| MTTR calculé | min |

**Étape 3 — Consulter les statistiques**
- Aller dans : Assistance → Statistiques → Vue globale

Remplir le tableau :

| **Statistique** | **Valeur** |
|---|---|
| Nombre total de tickets ouverts sur l'instance | |
| Nombre de tickets en statut "Nouveau" | |
| Nombre de tickets en statut "Résolu" | |
| Catégorie avec le plus de tickets | |

**Étape 4 — Créer un rapport**
- Assistance → Statistiques → Tickets
- Filtrer par votre nom de technicien
- Quelle est votre MTTR moyen sur les tickets traités aujourd'hui ? _______

---

## Bilan du TP

| **Ticket** | **N°** | **Type** | **Statut final** | **MTTR** |
|---|---|---|---|---|
| Imprimante hors ligne | | Incident | | min |
| Escalade N2 (ticket 1) | même | Incident | Escaladé | — |
| Accès dossier Karim | | Demande | Clôturé | min |
| Clôture confirmée | même | Demande | Clôturé | — |

---

## Questions de Réflexion

**Q1.** Quelle différence avez-vous observée entre la création d'un ticket à la main (S3) et la création dans GLPI ? Citez 2 avantages concrets de GLPI.
```
Avantage 1 : ___________________________________________________________
Avantage 2 : ___________________________________________________________
```

**Q2.** Un ticket est passé en "Résolu" depuis 3 jours mais l'utilisateur n'a pas confirmé. Que devrait faire GLPI automatiquement ? Comment configurer ce comportement ?
```
_______________________________________________________________________
_______________________________________________________________________
```

**Q3.** Pourquoi est-il important de distinguer un suivi "interne" d'un suivi "public" dans GLPI ?
```
_______________________________________________________________________
_______________________________________________________________________
```

**Q4.** Vous êtes responsable IT d'une PME de 80 personnes. En regardant les statistiques GLPI, vous constatez que 40% des tickets concernent "Mot de passe oublié". Quelles solutions proposez-vous pour réduire ce volume ?
```
Solution 1 : ___________________________________________________________
Solution 2 : ___________________________________________________________
```

---

---

# 📁 ANNEXE A — SCRIPT D'INSTALLATION GLPI SUR DEBIAN

*Pour les apprenants profil avancé — Configuration B*

*Testé sur Debian 12 Bookworm / Ubuntu 22.04 LTS*

```bash
#!/bin/bash
# ─── INSTALLATION GLPI 10.x SUR DEBIAN/UBUNTU ────────────────────────
# Usage : sudo bash install_glpi.sh
# Durée : ~15 minutes selon la connexion

set -e  # Arrêt en cas d'erreur

echo "=== [1/6] Mise à jour du système ==="
apt update && apt upgrade -y

echo "=== [2/6] Installation Apache, PHP et extensions ==="
apt install -y apache2 php php-mysql php-curl php-gd php-intl \
  php-ldap php-mbstring php-xml php-zip php-bz2 php-imap \
  libapache2-mod-php mariadb-server

echo "=== [3/6] Sécurisation MariaDB ==="
# Répondre aux questions : root pw, suppr anonymous, désactiver root remote, etc.
mysql_secure_installation

echo "=== [4/6] Création de la base de données GLPI ==="
mysql -u root -p <<EOF
CREATE DATABASE glpi CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'glpi'@'localhost' IDENTIFIED BY 'GlpiPass2024!';
GRANT ALL PRIVILEGES ON glpi.* TO 'glpi'@'localhost';
FLUSH PRIVILEGES;
EOF

echo "=== [5/6] Téléchargement et décompression de GLPI ==="
cd /var/www/html
GLPI_VERSION="10.0.15"
wget -q "https://github.com/glpi-project/glpi/releases/download/${GLPI_VERSION}/glpi-${GLPI_VERSION}.tgz"
tar -xzf "glpi-${GLPI_VERSION}.tgz"
rm "glpi-${GLPI_VERSION}.tgz"
chown -R www-data:www-data glpi/
chmod -R 755 glpi/

echo "=== [6/6] Configuration Apache ==="
cat > /etc/apache2/sites-available/glpi.conf <<'APACHECONF'
<VirtualHost *:80>
    ServerName glpi.local
    DocumentRoot /var/www/html/glpi/public

    <Directory /var/www/html/glpi/public>
        Require all granted
        RewriteEngine On
        RewriteCond %{REQUEST_FILENAME} !-f
        RewriteRule ^(.*)$ index.php [QSA,L]
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/glpi_error.log
    CustomLog ${APACHE_LOG_DIR}/glpi_access.log combined
</VirtualHost>
APACHECONF

a2ensite glpi.conf
a2enmod rewrite
a2dissite 000-default.conf
systemctl restart apache2

echo ""
echo "════════════════════════════════════════════════════════"
echo " GLPI installé ! Finaliser via le navigateur :"
echo " http://[IP_DU_SERVEUR]/glpi"
echo " Base de données : glpi / GlpiPass2024! / localhost"
echo " Identifiants par défaut : glpi / glpi"
echo "════════════════════════════════════════════════════════"
```

**Post-installation (dans le navigateur) :**
1. Aller sur `http://[IP]/glpi`
2. Choisir la langue → Suivant
3. Accepter la licence → Continuer
4. Cliquer "Installer" (pas "Mettre à jour")
5. Renseigner les paramètres de base de données : `localhost` / `glpi` / `GlpiPass2024!`
6. Finaliser — noter les identifiants affichés
7. **IMPORTANT :** supprimer le dossier d'installation : `rm -rf /var/www/html/glpi/install`

---

# 📄 ANNEXE B — FICHE DE NAVIGATION RAPIDE GLPI

*Pour les apprenants débutants — À conserver*

```
╔══════════════════════════════════════════════════════════════╗
║              NAVIGATION RAPIDE GLPI                         ║
╠══════════════════════════════════════════════════════════════╣
║  CRÉER UN TICKET                                            ║
║  Assistance → + (bouton vert) → Créer un ticket             ║
║                                                              ║
║  VOIR MES TICKETS                                           ║
║  Assistance → Tickets → (filtre : Technicien = moi)         ║
║                                                              ║
║  CHANGER LE STATUT D'UN TICKET                              ║
║  Ouvrir le ticket → En-tête → Statut → Sélectionner         ║
║                                                              ║
║  AJOUTER UN SUIVI (commentaire)                             ║
║  Ouvrir le ticket → Onglet "Suivi" → Ajouter un suivi       ║
║  ☑ Privé = interne (non visible utilisateur)                 ║
║  ☐ Privé = public (visible utilisateur)                      ║
║                                                              ║
║  RÉDIGER LA SOLUTION (passer en Résolu)                     ║
║  Ouvrir le ticket → Onglet "Solution" → Saisir + Valider     ║
║                                                              ║
║  CLÔTURER UN TICKET                                         ║
║  Ouvrir un ticket Résolu → Statut → Clôturé                  ║
║                                                              ║
║  LIER UN CI (équipement) À UN TICKET                        ║
║  Ouvrir le ticket → Onglet "Eléments" → Ajouter             ║
║                                                              ║
║  VOIR LES STATISTIQUES                                      ║
║  Assistance → Statistiques → Vue globale                     ║
╚══════════════════════════════════════════════════════════════╝
```

---

# 📊 BILAN BLOC 1 — CE QUI ENTRE DANS LE PORTFOLIO

*À compléter individuellement en fin de S6*

Le Bloc 1 (S1-S6) vous a permis de produire plusieurs livrables qui peuvent entrer dans votre portfolio E5 :

| **Livrable** | **Produit en** | **Compétence** | **Dans mon portfolio ?** |
|---|---|---|---|
| Fiche technique du poste de TP | S2 | B1.1 | ☐ Oui / ☐ À améliorer |
| Rapport OCS comparé à la fiche | S5 | B1.4 | ☐ Oui / ☐ À améliorer |
| 3 tickets d'incidents résolus (S4) | S4 | B1.6 | ☐ Oui / ☐ À améliorer |
| 3 fiches KB produites (S4) | S4 | B1.3 | ☐ Oui / ☐ À améliorer |
| Tickets GLPI traités (S6) | S6 | B1.3, B1.4 | ☐ Oui / ☐ À améliorer |

**Pour transformer ces livrables en SPS E5 :**
La SPS doit contenir : contexte + mission + réalisation + preuves (captures) + compétences mobilisées + ce que j'ai appris. Si vous avez ces 6 éléments, votre livrable est une SPS exploitable.

**Mon plan pour la SPS Bloc 1 :**
```
Titre envisagé : _______________________________________________________
Compétences couvertes : ________________________________________________
Preuves disponibles : __________________________________________________
Ce que j'ai appris : ___________________________________________________
```


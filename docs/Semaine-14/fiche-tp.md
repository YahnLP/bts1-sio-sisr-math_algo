# 🖥️ TP — INSTALLATION WORDPRESS SUR LAMP

*Durée : 90 minutes — Individuel*

---

## Objectif

Installer et configurer une stack LAMP (Linux Apache MySQL PHP) sur Ubuntu Server 22.04, puis installer WordPress.

---

## Prérequis

- VM Ubuntu Server 22.04 LTS installée
- Accès sudo
- Connexion Internet
- Accès SSH ou console directe

---

## PHASE 1 — Installation de la Stack LAMP (30 min)

### 1.1. Mise à Jour du Système (3 min)

```bash
sudo apt update
sudo apt upgrade -y
```

---

### 1.2. Installation d'Apache (5 min)

```bash
# Installer Apache2
sudo apt install apache2 -y

# Vérifier l'installation
apache2 -v

# Démarrer et activer Apache
sudo systemctl start apache2
sudo systemctl enable apache2

# Vérifier le statut
sudo systemctl status apache2
```

**Test navigateur :**
- Ouvrir http://[IP_DU_SERVEUR]
- Page **"Apache2 Ubuntu Default Page"** doit s'afficher

> 💡 **Trouver l'IP :** `ip addr show` ou `hostname -I`

---

### 1.3. Installation de MySQL (8 min)

```bash
# Installer MySQL Server
sudo apt install mysql-server -y

# Vérifier
mysql --version

# Sécuriser MySQL
sudo mysql_secure_installation
```

**Assistant mysql_secure_installation :**

```
VALIDATE PASSWORD COMPONENT ? [y/N]
→ N (pour simplifier en TP)

New password: 
→ MotDePasseMySQL2024!

Remove anonymous users? [Y/n] → Y
Disallow root login remotely? [Y/n] → Y
Remove test database? [Y/n] → Y
Reload privilege tables? [Y/n] → Y
```

**Créer la base WordPress :**

```bash
sudo mysql -u root -p
# Entrer : MotDePasseMySQL2024!
```

**Dans MySQL :**

```sql
CREATE DATABASE wordpress_db;
CREATE USER 'wp_user'@'localhost' IDENTIFIED BY 'WpPass2024!';
GRANT ALL PRIVILEGES ON wordpress_db.* TO 'wp_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

**Vérification :**

```bash
mysql -u wp_user -p
# Entrer : WpPass2024!

SHOW DATABASES;
# wordpress_db doit apparaître

EXIT;
```

---

### 1.4. Installation de PHP (5 min)

```bash
# Installer PHP et modules WordPress
sudo apt install php libapache2-mod-php php-mysql php-curl php-gd php-mbstring php-xml php-xmlrpc php-soap php-intl php-zip -y

# Vérifier
php -v
```

**Tester PHP :**

```bash
sudo nano /var/www/html/info.php
```

**Contenu :**

```php
<?php
phpinfo();
?>
```

**Sauvegarder :** Ctrl+O → Entrée → Ctrl+X

**Test navigateur :**
- http://[IP_DU_SERVEUR]/info.php
- Page **PHP Version 8.1.XX** doit s'afficher

> ⚠️ **Supprimer après test :**
> ```bash
> sudo rm /var/www/html/info.php
> ```

---

## PHASE 2 — Installation de WordPress (20 min)

### 2.1. Télécharger WordPress (3 min)

```bash
cd /tmp
wget https://fr.wordpress.org/latest-fr_FR.tar.gz
tar -xzvf latest-fr_FR.tar.gz
```

---

### 2.2. Déplacer WordPress (5 min)

```bash
sudo mkdir -p /var/www/monsite
sudo cp -r /tmp/wordpress/* /var/www/monsite/

# Permissions
sudo chown -R www-data:www-data /var/www/monsite
sudo chmod -R 755 /var/www/monsite
```

---

### 2.3. Configurer VirtualHost Apache (8 min)

```bash
sudo nano /etc/apache2/sites-available/monsite.conf
```

**Contenu :**

```apache
<VirtualHost *:80>
    ServerName monsite.local
    ServerAdmin admin@monsite.local
    DocumentRoot /var/www/monsite

    <Directory /var/www/monsite/>
        Options FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/monsite_error.log
    CustomLog ${APACHE_LOG_DIR}/monsite_access.log combined
</VirtualHost>
```

**Activer :**

```bash
sudo a2dissite 000-default.conf
sudo a2ensite monsite.conf
sudo a2enmod rewrite
sudo apache2ctl configtest
# Résultat : Syntax OK
sudo systemctl reload apache2
```

---

### 2.4. Configuration Fichier hosts (Poste Client)

**Windows :**
```cmd
# Notepad en Administrateur
# Ouvrir : C:\Windows\System32\drivers\etc\hosts

# Ajouter :
192.168.X.X    monsite.local
```

**Linux / macOS :**
```bash
sudo nano /etc/hosts

# Ajouter :
192.168.X.X    monsite.local
```

---

## PHASE 3 — Configuration WordPress (25 min)

### 3.1. Installation Web (15 min)

**Navigateur :** http://monsite.local

**Étape 1 — Langue :**
- Français → **Continuer**

**Étape 2 — Base de données :**

| **Champ** | **Valeur** |
|---|---|
| Nom base | `wordpress_db` |
| Identifiant | `wp_user` |
| Mot de passe | `WpPass2024!` |
| Adresse | `localhost` |
| Préfixe | `wp_` |

- **Valider** → **Lancer l'installation**

**Étape 3 — Informations site :**

| **Champ** | **Valeur** |
|---|---|
| Titre | Mon Site WordPress |
| Identifiant | admin |
| Mot de passe | AdminWP2024! |
| Email | admin@monsite.local |
| Moteurs recherche | ☐ Décocher |

- **Installer WordPress**

**Résultat :** "Bravo ! WordPress a été installé."

---

### 3.2. Connexion Tableau de Bord (3 min)

- **Se connecter**
- Identifiant : `admin`
- Mot de passe : `AdminWP2024!`

---

### 3.3. Configuration de Base (7 min)

**Réglages → Général :**
- Slogan : "Site de démonstration"
- **Enregistrer**

**Réglages → Permaliens :**
- ☑ **Titre de la publication**
- **Enregistrer**

**Apparence → Thèmes :**
- Activer un thème (ex : Twenty Twenty-Four)

**Créer page :**
- Pages → Ajouter
- Titre : "Bienvenue"
- Contenu : "Premier site WordPress sur LAMP"
- **Publier**

**Créer article :**
- Articles → Ajouter
- Titre : "Premier article"
- Contenu : "Installation réussie"
- **Publier**

---

## PHASE 4 — Validation (15 min)

### 4.1. Tests Fonctionnels

| **Test** | **Procédure** | **Résultat attendu** |
|---|---|---|
| **Page d'accueil** | http://monsite.local | Site s'affiche |
| **Article** | Cliquer "Premier article" | Article s'affiche |
| **Page** | http://monsite.local/bienvenue | Page s'affiche |
| **Admin** | http://monsite.local/wp-admin | Tableau de bord |
| **Upload** | Médias → Ajouter image | Image dans bibliothèque |

---

### 4.2. Vérifications Système

```bash
# Logs Apache
sudo tail -n 50 /var/log/apache2/monsite_error.log

# MySQL actif
sudo systemctl status mysql

# Apache actif
sudo systemctl status apache2

# Espace disque
df -h
```

---

### 4.3. Sécurité de Base

```bash
sudo nano /var/www/monsite/wp-config.php
```

**Ajouter avant `/* C'est tout */` :**

```php
// Désactiver l'éditeur de fichiers
define('DISALLOW_FILE_EDIT', true);
```

**Vérification :** Dans WordPress, Apparence → l'éditeur a disparu.

---

## PHASE 5 — Documentation (Lien S11)

Rédiger une **procédure d'installation** selon modèle S11 :

1. **Objectif** : Installer WordPress sur Ubuntu avec LAMP
2. **Prérequis** : VM Ubuntu, sudo, Internet
3. **Étapes** : Phases 1 à 4 avec commandes clés
4. **Troubleshooting** : 2 erreurs courantes
5. **Résultat** : Captures site fonctionnel


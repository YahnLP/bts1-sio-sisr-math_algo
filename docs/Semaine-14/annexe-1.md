# 📄 ANNEXE 1 — TROUBLESHOOTING

---

## Erreur 1 — "Impossible d'établir connexion BDD"

**Symptôme :** Message d'erreur WordPress.

**Causes :**
1. MySQL n'est pas démarré
2. Identifiants incorrects
3. Base non créée

**Solutions :**

```bash
# Vérifier MySQL
sudo systemctl status mysql
sudo systemctl start mysql

# Tester connexion
mysql -u wp_user -p
SHOW DATABASES;
# wordpress_db doit apparaître
```

---

## Erreur 2 — "403 Forbidden"

**Symptôme :** Erreur 403 ou page blanche.

**Causes :**
1. Permissions incorrectes
2. VirtualHost mal configuré

**Solutions :**

```bash
# Permissions
sudo chown -R www-data:www-data /var/www/monsite
sudo chmod -R 755 /var/www/monsite

# Vérifier VirtualHost
sudo apache2ctl -S

# Logs
sudo tail -f /var/log/apache2/monsite_error.log
```

---

## Erreur 3 — "404 Not Found" permaliens

**Symptôme :** Page d'accueil OK, mais articles 404.

**Cause :** Module rewrite non activé.

**Solution :**

```bash
sudo a2enmod rewrite
sudo systemctl reload apache2
```

---

## Erreur 4 — PHP non interprété

**Symptôme :** Code PHP affiché en texte.

**Solution :**

```bash
# Vérifier module PHP
apachectl -M | grep php

# Réinstaller si absent
sudo apt install libapache2-mod-php -y
sudo systemctl restart apache2
```


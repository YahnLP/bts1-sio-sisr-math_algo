---
author: YLP
title: 📚 FICHE DE COURS
---

# 📖 FICHE DE COURS
## S2 — Chaînes de Caractères : Manipulation, Extraction, Parsing de Logs

## 🎯 Objectifs de la Séance

À la fin de cette séance, je serai capable de :

✅ Définir ce qu'est une chaîne de caractères (string)  
✅ Manipuler des chaînes : concaténation, longueur, indexation  
✅ Transformer des chaînes : majuscules, minuscules, suppression d'espaces  
✅ Extraire des sous-chaînes avec le slicing  
✅ Découper une chaîne avec `.split()`  
✅ **Parser un fichier de log** pour en extraire des informations

---

## 📚 Vocabulaire Clé à Maîtriser

| **Terme** | **Définition** | **Exemple** |
|-----------|----------------|-------------|
| **Chaîne de caractères (string)** | Séquence de caractères délimitée par des guillemets | `"Bonjour"`, `'192.168.1.1'` |
| **Concaténation** | Assemblage de plusieurs chaînes en une seule | `"Bon" + "jour"` → `"Bonjour"` |
| **Index** | Position d'un caractère dans une chaîne (commence à 0) | `"Python"[0]` → `'P'` |
| **Slicing** | Extraction d'une sous-chaîne via des indices | `"Python"[0:3]` → `"Pyt"` |
| **Immutabilité** | Une chaîne ne peut pas être modifiée après création | On crée une nouvelle chaîne à chaque transformation |
| **Parsing** | Analyse et extraction de données structurées d'un texte | Extraire l'IP d'une ligne de log |
| **Délimiteur** | Caractère utilisé pour séparer des éléments | Espace, virgule, tiret... |

---

## 1️⃣ Qu'est-ce qu'une Chaîne de Caractères ?

### Définition

Une **chaîne de caractères** (ou **string**) est une **séquence de caractères** (lettres, chiffres, symboles, espaces) délimitée par des guillemets simples `' '` ou doubles `" "`.

```python
# Exemples de chaînes
nom = "Dupont"
prenom = 'Jean'
adresse_ip = "192.168.1.1"
message = "Le serveur web est accessible."
```

### Pourquoi les Chaînes Sont Essentielles en Administration Système ?

**80% du travail d'un technicien SISR consiste à manipuler du texte :**

- 📄 Lire des **fichiers de configuration** (`/etc/nginx/nginx.conf`)
- 📊 Analyser des **logs** (`/var/log/apache2/access.log`)
- 🔧 Écrire des **scripts** pour automatiser des tâches
- 📧 Générer des **rapports** pour le management

**Sans maîtrise des chaînes → impossible d'automatiser.**

---

## 2️⃣ Opérations de Base sur les Chaînes

### A. Concaténation (Assemblage)

**Définition :** Assembler plusieurs chaînes en une seule avec l'opérateur `+`.

```python
prenom = "Jean"
nom = "Dupont"

# Concaténation simple
nom_complet = prenom + " " + nom
print(nom_complet)
# Affiche : Jean Dupont

# Concaténation avec formatage
message = "Bonjour " + nom_complet + ", bienvenue !"
print(message)
# Affiche : Bonjour Jean Dupont, bienvenue !
```

**⚠️ Attention :** On ne peut concaténer que des chaînes. Pour assembler un nombre et une chaîne, il faut convertir le nombre.

```python
age = 25

# ❌ ERREUR : Impossible de concaténer int et str
# message = "Vous avez " + age + " ans"

# ✅ CORRECT : Conversion avec str()
message = "Vous avez " + str(age) + " ans"
print(message)
# Affiche : Vous avez 25 ans
```

---

### B. Longueur d'une Chaîne

**Fonction `len()` :** Retourne le nombre de caractères dans une chaîne.

```python
phrase = "Administration système"
taille = len(phrase)
print(taille)
# Affiche : 22 (espaces inclus)

# Utilisation pratique : vérifier la longueur d'un mot de passe
mot_de_passe = "Pass123!"
if len(mot_de_passe) < 12:
    print("⚠️ Mot de passe trop court (minimum 12 caractères)")
else:
    print("✅ Mot de passe valide")
```

---

### C. Indexation (Accéder à un Caractère Précis)

Chaque caractère d'une chaîne a un **index** (position) qui commence à **0**.

```
  Chaîne :   P   y   t   h   o   n
  Index :    0   1   2   3   4   5
  Index négatif : -6  -5  -4  -3  -2  -1
```

**Exemples :**

```python
mot = "Python"

# Accès par index positif
print(mot[0])   # Affiche : P (1er caractère)
print(mot[3])   # Affiche : h (4e caractère)

# Accès par index négatif (depuis la fin)
print(mot[-1])  # Affiche : n (dernier caractère)
print(mot[-2])  # Affiche : o (avant-dernier caractère)

# ❌ ERREUR : Index hors limites
# print(mot[10])  # IndexError
```

**Cas d'usage concret : Vérifier le premier caractère d'une commande**

```python
commande = "sudo systemctl restart apache2"

if commande[0:4] == "sudo":
    print("✅ Commande admin détectée")
```

---

## 3️⃣ Slicing (Extraction de Sous-Chaînes)

### Syntaxe Générale

```python
chaine[début:fin:pas]
```

- `début` : Index de départ (inclus)
- `fin` : Index de fin (exclus)
- `pas` : Nombre de caractères à sauter (optionnel, défaut = 1)

### Exemples

```python
texte = "Administration"

# Extraire les 6 premiers caractères
print(texte[0:6])    # Affiche : Admini
print(texte[:6])     # Même résultat (début omis = 0)

# Extraire du 7e au dernier caractère
print(texte[6:])     # Affiche : stration

# Extraire les 5 derniers caractères
print(texte[-5:])    # Affiche : ation

# Extraire avec un pas de 2 (1 caractère sur 2)
print(texte[::2])    # Affiche : Amnsrto

# Inverser une chaîne
print(texte[::-1])   # Affiche : noitartsinimda
```

### Cas d'Usage : Extraire une Adresse IP d'une Ligne de Log

```python
ligne_log = "192.168.1.10 - - [20/Feb/2026:10:15:32 +0100] GET /index.html 200"

# Extraire l'IP (les 12 premiers caractères)
ip = ligne_log[:12]
print(ip)
# Affiche : 192.168.1.10
```

**[ILLUSTRATION 1 : Schéma du slicing]**  
*Légende : Représentation visuelle d'une chaîne "Administration" avec les index positifs (0-13) et négatifs (-13 à -1), montrant des flèches pour illustrer `[0:6]`, `[6:]`, `[-5:]` et `[::-1]`*

---

## 4️⃣ Méthodes de Transformation

Les chaînes disposent de **méthodes** (fonctions intégrées) pour les transformer.

### Tableau Récapitulatif

| **Méthode** | **Action** | **Exemple** | **Résultat** |
|-------------|-----------|-------------|--------------|
| `.upper()` | Convertir en MAJUSCULES | `"admin".upper()` | `"ADMIN"` |
| `.lower()` | Convertir en minuscules | `"ADMIN".lower()` | `"admin"` |
| `.strip()` | Supprimer espaces début/fin | `" test ".strip()` | `"test"` |
| `.lstrip()` | Supprimer espaces à gauche | `" test".lstrip()` | `"test"` |
| `.rstrip()` | Supprimer espaces à droite | `"test ".rstrip()` | `"test"` |
| `.replace(a, b)` | Remplacer `a` par `b` | `"hello".replace("l", "L")` | `"heLLo"` |
| `.split(sep)` | Découper en liste selon `sep` | `"a,b,c".split(",")` | `['a', 'b', 'c']` |
| `.count(x)` | Compter occurrences de `x` | `"aaa".count("a")` | `3` |

### Exemples Pratiques

#### 1. Normaliser un Nom d'Utilisateur

```python
nom_utilisateur = "  JeanDUPONT  "

# Supprimer les espaces et convertir en minuscules
nom_propre = nom_utilisateur.strip().lower()
print(nom_propre)
# Affiche : jeandupont
```

#### 2. Remplacer un Mot de Passe dans un Fichier de Config

```python
config = "password=oldpass123"

# Remplacer l'ancien mot de passe
nouvelle_config = config.replace("oldpass123", "newpass456")
print(nouvelle_config)
# Affiche : password=newpass456
```

#### 3. Compter les Erreurs 404 dans un Log

```python
log = """
192.168.1.10 GET /index.html 200
203.0.113.88 GET /admin 404
203.0.113.88 POST /login 404
198.51.100.7 GET /products 200
"""

# Compter les occurrences de "404"
nombre_404 = log.count("404")
print(f"Nombre d'erreurs 404 : {nombre_404}")
# Affiche : Nombre d'erreurs 404 : 2
```

---

## 5️⃣ La Méthode `.split()` — Découper une Chaîne

### Principe

La méthode `.split(séparateur)` **découpe une chaîne** en une **liste** selon un délimiteur.

```python
texte = "pomme,poire,banane"
fruits = texte.split(",")
print(fruits)
# Affiche : ['pomme', 'poire', 'banane']
```

### Découpage avec Espace (Défaut)

Si aucun séparateur n'est spécifié, `.split()` découpe selon les **espaces**.

```python
phrase = "Serveur web accessible"
mots = phrase.split()
print(mots)
# Affiche : ['Serveur', 'web', 'accessible']
```

### Cas d'Usage : Parser une Ligne de Log

**Exemple de ligne de log Apache :**

```
192.168.1.10 - - [20/Feb/2026:10:15:32 +0100] "GET /index.html HTTP/1.1" 200 2345
```

**Objectif :** Extraire l'IP, la méthode HTTP, l'URL et le code de retour.

```python
ligne = '192.168.1.10 - - [20/Feb/2026:10:15:32 +0100] "GET /index.html HTTP/1.1" 200 2345'

# Découper par espaces
parties = ligne.split()
print(parties)
# Affiche : ['192.168.1.10', '-', '-', '[20/Feb/2026:10:15:32', '+0100]', 
#            '"GET', '/index.html', 'HTTP/1.1"', '200', '2345']

# Extraction des informations clés
ip = parties[0]
code_http = parties[8]
taille = parties[9]

print(f"IP : {ip}")
print(f"Code HTTP : {code_http}")
print(f"Taille : {taille} octets")
# Affiche :
# IP : 192.168.1.10
# Code HTTP : 200
# Taille : 2345 octets
```

**[ILLUSTRATION 2 : Schéma du split d'une ligne de log]**  
*Légende : Représentation visuelle d'une ligne de log découpée par `.split()` en plusieurs parties colorées (IP, date, méthode, URL, code, taille)*

---

## 6️⃣ Parsing d'un Fichier de Log — Cas Complet

### Structure d'un Log Apache/Nginx

**Format standard :**

```
IP - - [Date] "Méthode URL Protocole" Code Taille
```

**Exemple :**

```
192.168.1.10 - - [20/Feb/2026:10:15:32 +0100] "GET /index.html HTTP/1.1" 200 2345
```

### Décomposition des Champs

| **Champ** | **Position** | **Signification** |
|-----------|--------------|-------------------|
| `192.168.1.10` | Champ 1 | Adresse IP du client |
| `[20/Feb/2026:10:15:32 +0100]` | Champ 4 | Date et heure de la requête |
| `"GET /index.html HTTP/1.1"` | Champ 5-7 | Méthode, URL, protocole |
| `200` | Champ 8 | Code HTTP (200=OK, 404=Not Found, 500=Erreur serveur) |
| `2345` | Champ 9 | Taille de la réponse en octets |

### Script Python : Analyser un Fichier de Log

**Objectif :** Compter le nombre de requêtes par code HTTP (200, 404, 500...).

```python
# Contenu du fichier access.log (exemple simplifié)
log = """192.168.1.10 - - [20/Feb/2026:10:15:32 +0100] "GET /index.html HTTP/1.1" 200 2345
203.0.113.42 - - [20/Feb/2026:10:16:18 +0100] "GET /admin/login HTTP/1.1" 404 512
198.51.100.7 - - [20/Feb/2026:10:17:05 +0100] "POST /contact HTTP/1.1" 200 1024
192.168.1.10 - - [20/Feb/2026:10:18:22 +0100] "GET /style.css HTTP/1.1" 200 8192
203.0.113.42 - - [20/Feb/2026:10:19:44 +0100] "GET /admin/users HTTP/1.1" 404 512
198.51.100.7 - - [20/Feb/2026:10:20:01 +0100] "GET /products HTTP/1.1" 500 128"""

# Compteurs
total_lignes = 0
erreurs_404 = 0
erreurs_500 = 0
requetes_ok = 0

# Découper le log en lignes
lignes = log.split("\n")

# Analyser chaque ligne
for ligne in lignes:
    total_lignes += 1
    
    # Découper la ligne par espaces
    parties = ligne.split()
    
    # Le code HTTP est le 9e élément (index 8)
    code_http = parties[8]
    
    # Compter selon le code
    if code_http == "200":
        requetes_ok += 1
    elif code_http == "404":
        erreurs_404 += 1
    elif code_http == "500":
        erreurs_500 += 1

# Afficher le rapport
print("╔════════════════════════════════════════╗")
print("║     RAPPORT D'ANALYSE DE LOGS          ║")
print("╠════════════════════════════════════════╣")
print(f"║ Total de requêtes : {total_lignes:18} ║")
print(f"║ Requêtes OK (200) : {requetes_ok:18} ║")
print(f"║ Erreurs 404       : {erreurs_404:18} ║")
print(f"║ Erreurs 500       : {erreurs_500:18} ║")
print("╚════════════════════════════════════════╝")
```

**Résultat affiché :**

```
╔════════════════════════════════════════╗
║     RAPPORT D'ANALYSE DE LOGS          ║
╠════════════════════════════════════════╣
║ Total de requêtes :                  6 ║
║ Requêtes OK (200) :                  3 ║
║ Erreurs 404       :                  2 ║
║ Erreurs 500       :                  1 ║
╚════════════════════════════════════════╝
```

**[ILLUSTRATION 3 : Organigramme du processus de parsing]**  
*Légende : Diagramme montrant les étapes : 1) Lire le fichier, 2) Découper en lignes, 3) Pour chaque ligne → découper par espaces, 4) Extraire le code HTTP, 5) Incrémenter les compteurs, 6) Afficher le rapport*

---

## 7️⃣ Immutabilité des Chaînes — Concept Important

### Définition

En Python, les chaînes sont **immutables** : on ne peut pas modifier une chaîne existante. Toute transformation crée une **nouvelle chaîne**.

```python
mot = "Python"

# ❌ IMPOSSIBLE : Modifier un caractère
# mot[0] = "J"  # TypeError: 'str' object does not support item assignment

# ✅ CORRECT : Créer une nouvelle chaîne
nouveau_mot = "J" + mot[1:]
print(nouveau_mot)
# Affiche : Jython
```

### Pourquoi C'est Important ?

**Implication pour la performance :**

```python
# ❌ MAUVAISE PRATIQUE : Concaténation dans une boucle
resultat = ""
for i in range(1000):
    resultat = resultat + "ligne " + str(i) + "\n"
# Chaque += crée une NOUVELLE chaîne → très lent

# ✅ BONNE PRATIQUE : Utiliser une liste et join()
lignes = []
for i in range(1000):
    lignes.append("ligne " + str(i))
resultat = "\n".join(lignes)
# Beaucoup plus rapide
```

---

## 📝 Fiche Récapitulative (À Garder)

### Opérations Essentielles

| **Opération** | **Syntaxe** | **Exemple** |
|---------------|-------------|-------------|
| **Concaténation** | `a + b` | `"Bon" + "jour"` → `"Bonjour"` |
| **Longueur** | `len(s)` | `len("Python")` → `6` |
| **Index** | `s[i]` | `"Python"[0]` → `'P'` |
| **Slicing** | `s[début:fin]` | `"Python"[0:3]` → `"Pyt"` |
| **Majuscules** | `s.upper()` | `"admin".upper()` → `"ADMIN"` |
| **Minuscules** | `s.lower()` | `"ADMIN".lower()` → `"admin"` |
| **Supprimer espaces** | `s.strip()` | `" test ".strip()` → `"test"` |
| **Remplacer** | `s.replace(a,b)` | `"hello".replace("l","L")` → `"heLLo"` |
| **Découper** | `s.split(sep)` | `"a,b,c".split(",")` → `['a','b','c']` |
| **Compter** | `s.count(x)` | `"aaa".count("a")` → `3` |

### Codes HTTP à Connaître

| **Code** | **Signification** | **Action à prendre** |
|----------|-------------------|----------------------|
| **200** | OK | Tout va bien |
| **301** | Redirection permanente | Page déplacée |
| **404** | Not Found | Page inexistante (possible erreur de lien) |
| **403** | Forbidden | Accès refusé (vérifier permissions) |
| **500** | Internal Server Error | Erreur serveur (vérifier logs détaillés) |
| **503** | Service Unavailable | Serveur surchargé ou en maintenance |

---

## 🎯 Compétences Travaillées (Référentiel RNCP)

| **Code** | **Compétence** | **Application dans cette séance** |
|----------|----------------|-----------------------------------|
| **B1.2** | Travailler en mode projet | Analyser un log pour répondre à une demande |
| **B1.3** | Mettre à disposition un service | Surveiller l'activité d'un serveur web |
| **B2.1** | Concevoir une solution applicative | Écrire un script d'analyse de logs |

---

## 💡 Pour Aller Plus Loin

- **Expressions régulières (regex)** : Parsing avancé pour formats complexes (S8)
- **Bibliothèque `re`** : Module Python pour regex
- **Parsing de JSON/XML** : Formats structurés (S12)
- **Outils d'analyse de logs** : Splunk, ELK Stack, Graylog

---

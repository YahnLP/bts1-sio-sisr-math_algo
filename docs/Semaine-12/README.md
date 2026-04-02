# 01 – Objectifs et ressources


---

## Informations Générales

| **Champ** | **Détail** |
|-----------|-----------|
| **Semaine** | S2 — Année 1 |
| **Module** | Mathématiques pour l'informatique et algorithmique |
| **Durée totale** | 4 heures |
| **Public** | Apprentis BTS SIO SISR — profils hétérogènes |
| **Modalité** | Présentiel — salle informatique |
| **Prérequis** | S1 : Variables, types de données, structures conditionnelles |

---

## Compétences Visées

| **Code** | **Intitulé de la compétence** | **Niveau visé** |
|----------|-------------------------------|-----------------|
| **B1.2** | Travailler en mode projet | Application |
| **B1.3** | Mettre à disposition des utilisateurs un service informatique | Application |
| **B2.1** | Concevoir et développer une solution applicative | Application |

> 📌 **S2 pose les fondations de la manipulation de texte**, compétence ESSENTIELLE pour un technicien SISR. L'objectif est de montrer que **80% du travail d'administration système consiste à manipuler des fichiers texte** (logs, configurations, scripts). Cette séance doit être **pratique et concrète**, centrée sur un cas d'usage réel : l'analyse de logs.

---

**Manipulation de chaînes :**
- ✅ Définir ce qu'est une **chaîne de caractères** (string)
- ✅ Maîtriser les opérations de base : **concaténation, longueur, index**
- ✅ Extraire des sous-chaînes avec le **slicing** (Python) ou équivalent
- ✅ Comprendre l'**immutabilité** des chaînes

**Méthodes de transformation :**
- ✅ Convertir en majuscules/minuscules (`.upper()`, `.lower()`)
- ✅ Supprimer les espaces (`.strip()`, `.lstrip()`, `.rstrip()`)
- ✅ Remplacer des caractères (`.replace()`)
- ✅ Découper une chaîne (`.split()`)

**Application concrète :**
- ✅ Parser un fichier de log Apache/Nginx
- ✅ Extraire des informations structurées (IP, date, code HTTP, URL)
- ✅ Compter les occurrences d'événements (erreurs 404, 500...)
- ✅ Générer un rapport d'activité

**Posture ITIL :**
- ✅ Comprendre l'importance de la **surveillance proactive** (monitoring)
- ✅ Identifier les **incidents** à partir des logs
- ✅ Produire des **rapports d'activité** pour le management

---
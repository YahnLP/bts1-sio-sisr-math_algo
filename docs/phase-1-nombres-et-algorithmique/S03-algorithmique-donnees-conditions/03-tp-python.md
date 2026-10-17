---
render_macros: true
---

# TP Python – Premiers programmes Python

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S03*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

## Exercice A – Droits d'accès avec des masques

On code lecture = 4, écriture = 2, exécution = 1. Complète les trois fonctions avec des opérateurs bit à bit.

**J'anticipe.** Que doivent renvoyer `ajouter(5, 2)`, `retirer(7, 4)` et `accorde(6, 1)` ? Pose les écritures binaires sur ta feuille.

{{ IDE('droits', MAX="+") }}

**Je comprends.** Pourquoi `retirer` utilise-t-il `~masque` ? Que se passe-t-il si on retire un droit qui n'était pas accordé ?

## Exercice B – Année bissextile

Écris `est_bissextile(annee)`. Les cas limites 1900, 2000 et 2100 sont dans les tests.

{{ IDE('est_bissextile', MAX="+") }}

## Exercice C – Adresse privée

Écris `adresse_privee(adresse)` qui reçoit un texte `"a.b.c.d"` et renvoie `True` pour les plages privées de l'exercice 6.

{{ IDE('adresse_privee', MAX="+") }}

## Exercice D – Adresse de réseau

Écris `adresse_reseau(adresse, masque)` qui renvoie l'adresse de réseau sous forme de texte, octet par octet, avec `&`.

{{ IDE('adresse_reseau', MAX="+") }}

**Je comprends.** Vérifie à la main un des tests, en binaire.

## Exercice E – Jours dans un mois

Écris `jours_du_mois(mois, annee)` (mois de 1 à 12). Tu peux réutiliser `est_bissextile`.

{{ IDE('jours_du_mois', MAX="+") }}

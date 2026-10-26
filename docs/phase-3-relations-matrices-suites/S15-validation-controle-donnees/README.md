# S15 – Algorithmique appliquée : validation et contrôle de données

| Élément | Détail |
|---|---|
| **Niveau** | BTS SIO option SISR, 1re année – mathématiques pour l'informatique |
| **Séance** | S15 (séance 15 sur 19) – Phase 3 |
| **Durée** | 4 heures |
| **Chapitre du programme** | Algorithmique appliquée (fonctions, chaînes, tableaux) ; calcul binaire et opérateurs logiques |
| **Prérequis** | S03, S04, S12 (conditions, boucles, fonctions, chaînes, tableaux) ; S07 (congruences) ; S10 (opérateurs logiques) |
| **Outils** | Papier, calculatrice, éditeur Python intégré au site |

> [!NOTE]
> **Question qui guide la séance :** *« Comment un programme décide-t-il qu'une donnée reçue est correcte, et comment détecte-t-il qu'elle a été abîmée en route ? »*

## Objectifs

À la fin de la séance, l'étudiant est capable de :

1. **Écrire** une fonction qui valide le format d'une donnée (octet, adresse IPv4, adresse MAC) en parcourant une chaîne ;
2. **Choisir** les cas limites à tester (chaîne vide, zéro initial, valeur à la frontière) ;
3. **Calculer** un bit de parité et **détecter** une erreur de transmission ;
4. **Localiser** et **corriger** une erreur isolée avec une parité à deux dimensions ;
5. **Calculer** une somme de contrôle modulo 256 et un OU exclusif de contrôle, et **dire** ce qu'ils ne détectent pas.

## Contenu de la séance

| Document | Rôle |
|---|---|
| [Cours – Valider et contrôler des données](01-cours.md) | Cours |
| [Exercices – Formats, parité et sommes de contrôle](02-exercices.md) | Exercices |
| [TP Python – Validation et contrôle](03-tp-python.md) | TP (éditeur Python intégré) |
| [Aide-mémoire – Validation et contrôle](04-aide-memoire.md) | Aide-mémoire |

## Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 15 | **Rappel** S07 (modulo) et S10 (OU exclusif) | Oral |
| 0 h 15 – 1 h 30 | **Cours** : valider un format, parité, somme de contrôle | Cours et questions |
| 1 h 30 – 2 h 30 | **Exercices** | Individuel |
| 2 h 30 – 3 h 45 | **TP Python** : validateurs, parité, somme de contrôle | Individuel |
| 3 h 45 – 4 h 00 | **Auto-évaluation** | Individuel |

*Durées indicatives : la séance dure 4 h ; l'enseignant ajuste selon le rythme du groupe.*

## Application en informatique

Contrôle d'une saisie d'adresse IP ou MAC dans un formulaire ou un script de configuration, détection d'erreurs sur une liaison ou un support de stockage, vérification de l'intégrité d'un message reçu.

## Évaluation

- Feuille d'exercices corrigée, scripts du TP validés.
- Auto-évaluation « Je sais faire » en fin d'exercices.

<details markdown="1">
<summary>Notes pour l'enseignant</summary>

- **Programme :** cette séance remplace l'ancienne séance « Suites numériques », car les suites numériques ne figurent pas dans les modules de l'épreuve E3 (elles sont proposées en complément dans le site de 2e année). Elle s'appuie sur l'algorithmique appliquée, le calcul binaire et les opérateurs logiques (voir [Programme et épreuve E3](../../ressources/programme-e3.md)). 
- Les calculs d'adresse réseau et de masque sont traités en S10 ; cette séance ne les reprend pas.

</details>

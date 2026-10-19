# S01 – Numération : entiers en base 2, 10 et 16

| Élément | Détail |
|---|---|
| **Niveau** | BTS SIO option SISR, 1re année – mathématiques pour l'informatique |
| **Séance** | S01 (séance 1 sur 19) – Phase 1 |
| **Durée** | 4 heures |
| **Chapitre du programme** | Arithmétique – numération |
| **Prérequis** | Aucun (puissances, divisions). |
| **Outils** | Papier, calculatrice, éditeur Python intégré au site |

> [!NOTE]
> **Question qui guide la séance :** *« Pourquoi les machines comptent-elles en binaire, et comment passer d'une écriture à l'autre sans se tromper ? »*

## Objectifs

À la fin de la séance, l'étudiant est capable de :

1. **Écrire** un entier naturel sous la forme d'une somme de puissances d'une base \(b\) (\(b = 2, 10, 16\)) ;
2. **Convertir** un entier de la base 10 vers la base 2 ou 16 (divisions successives) et inversement (somme pondérée) ;
3. **Passer** directement de la base 2 à la base 16 et inversement (groupes de 4 bits) ;
4. **Déterminer** combien de valeurs on représente avec \(n\) bits et quel est le plus grand entier ;
5. **Lire** une adresse MAC, une adresse IPv4 et un code couleur, et **vérifier** ses conversions avec Python.

## Contenu de la séance

| Document | Rôle |
|---|---|
| [Cours – Numération : entiers](01-cours.md) | Cours |
| [Exercices – Conversions et lecture de nombres](02-exercices.md) | Exercices |
| [TP Python – Vérifier ses conversions](03-tp-python.md) | TP (éditeur Python intégré) |
| [Annexe – Python : premiers pas](annexe-python.md) | À lire avant le TP : variables, `//` et `%`, `if`, `while`, `def` |
| [Aide-mémoire – Numération](04-aide-memoire.md) | Aide-mémoire |

## Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Accroche** : pourquoi 192.168.1.10 et 00:1A:2B:3C:4D:5E ? (recueil des idées) | Oral |
| 0 h 20 – 1 h 30 | **Cours** : écriture en base \(b\), conversions, bits et octets | Cours et questions |
| 1 h 30 – 2 h 45 | **Exercices** : conversions, lecture d'adresses | Individuel, puis binômes |
| 2 h 45 – 3 h 45 | **TP Python** : lecture de l'[annexe Python](annexe-python.md) (10 min), puis vérifier et programmer une conversion | Individuel |
| 3 h 45 – 4 h 00 | **Auto-évaluation** « Je sais faire » | Individuel |

*Durées indicatives : la séance dure 4 h ; l'enseignant ajuste selon le rythme du groupe.*

## Application en informatique

Une adresse **MAC** compte 48 bits (6 octets) écrits en hexadécimal ; une adresse **IPv4** compte 32 bits (4 octets) écrits en décimal ; un code couleur web `#RRGGBB` compte 3 octets. Savoir convertir permet de lire ces écritures et de comprendre les masques de sous-réseau (S10).

## Évaluation

- Feuille d'exercices corrigée à la main, remise en fin de séance.
- Auto-évaluation « Je sais faire » en fin d'exercices.

<details markdown="1">
<summary>Notes pour l'enseignant</summary>

- **Programme :** le chapitre est rattaché au programme officiel de mathématiques pour l'informatique (voir [Programme et épreuve E3](../../ressources/programme-e3.md)) ; la répartition en séances est une proposition à valider.
- **Corrigé :** dans `corriges/` à la racine du dépôt (hors du site publié).
- Le chapitre « Arithmétique » du programme impose les bases 10, 2 et 16 (entiers et réels, conversions) : les réels sont traités en S02.

</details>

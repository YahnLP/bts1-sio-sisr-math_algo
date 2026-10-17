# S02 – Numération : nombres à virgule, arrondis et calcul en binaire

| Élément | Détail |
|---|---|
| **Niveau** | BTS SIO option SISR, 1re année – mathématiques pour l'informatique |
| **Séance** | S02 (séance 2 sur 19) – Phase 1 |
| **Durée** | 4 heures |
| **Chapitre du programme** | Arithmétique – numération, arrondis, opérations en base 2 |
| **Prérequis** | S01 (bases 2, 10, 16). |
| **Outils** | Papier, calculatrice, éditeur Python intégré au site |

> [!NOTE]
> **Question qui guide la séance :** *« Pourquoi un ordinateur trouve-t-il que 0,1 + 0,2 n'est pas égal à 0,3, et comment calcule-t-on en binaire ? »*

## Objectifs

À la fin de la séance, l'étudiant est capable de :

1. **Convertir** un nombre à virgule entre les bases 10 et 2 (parties entière et fractionnaire) ;
2. **Reconnaître** les nombres qui s'écrivent avec un nombre fini de chiffres après la virgule en base 2 ;
3. **Arrondir** et **tronquer** un nombre, et **majorer** l'erreur commise ;
4. **Additionner**, **soustraire** et **multiplier** des entiers en binaire, et **décaler** pour multiplier ou diviser par une puissance de 2 ;
5. **Distinguer** unités décimales (ko, Mo, Go) et binaires (Kio, Mio, Gio), bits et octets, et **calculer** des volumes et des durées de transfert.

## Contenu de la séance

| Document | Rôle |
|---|---|
| [Cours – Réels, arrondis, calcul en binaire](01-cours.md) | Cours |
| [Exercices – Réels en binaire, opérations et unités](02-exercices.md) | Exercices |
| [TP Python – Précision des flottants et décalages](03-tp-python.md) | TP (éditeur Python intégré) |
| [Aide-mémoire – Réels et calcul en binaire](04-aide-memoire.md) | Aide-mémoire |

## Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Rappel** S01 et accroche : `0.1 + 0.2` en Python | Oral et démonstration |
| 0 h 20 – 1 h 30 | **Cours** : partie fractionnaire, arrondis, opérations en binaire, unités | Cours et questions |
| 1 h 30 – 2 h 45 | **Exercices** | Individuel, puis binômes |
| 2 h 45 – 3 h 45 | **TP Python** : précision, décalages, tailles | Individuel |
| 3 h 45 – 4 h 00 | **Auto-évaluation** | Individuel |

*Durées indicatives : la séance dure 4 h ; l'enseignant ajuste selon le rythme du groupe.*

## Application en informatique

Tailles de fichiers et capacités des disques (Go ou Gio), débits (Mbit/s ou Mo/s), nombre d'adresses d'un réseau (puissances de 2).

## Évaluation

- Feuille d'exercices corrigée à la main.
- Auto-évaluation « Je sais faire » en fin d'exercices.

<details markdown="1">
<summary>Notes pour l'enseignant</summary>

- **Programme :** le chapitre est rattaché au programme officiel de mathématiques pour l'informatique (voir [Programme et épreuve E3](../../ressources/programme-e3.md)) ; la répartition en séances est une proposition à valider.
- **Corrigé :** dans `corriges/` à la racine du dépôt (hors du site publié).
- L'écriture en complément à deux est présentée comme ouverture (entiers relatifs) ; elle n'est pas nommée dans le programme étudié, à valider.
- Les préfixes ko, Mo, Go (puissances de 10) et Kio, Mio, Gio (puissances de 2) sont ceux de la norme internationale ; l'usage commercial et celui de certains systèmes diffèrent, d'où l'insistance sur l'unité.

</details>

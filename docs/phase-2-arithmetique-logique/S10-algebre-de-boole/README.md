# S10 – Algèbre de Boole et simplification

| Élément | Détail |
|---|---|
| **Niveau** | BTS SIO option SISR, 1re année – mathématiques pour l'informatique |
| **Séance** | S10 (séance 10 sur 19) – Phase 2 |
| **Durée** | 4 heures |
| **Chapitre du programme** | Calcul booléen |
| **Prérequis** | S08, S09 (connecteurs, ensembles) ; S03 (opérateurs bit à bit). |
| **Outils** | Papier, calculatrice, éditeur Python intégré au site |

> [!NOTE]
> **Question qui guide la séance :** *« Comment écrire la même condition avec le moins de termes possible, et comment la machine l'utilise-t-elle (masques, circuits) ? »*

## Objectifs

À la fin de la séance, l'étudiant est capable de :

1. **Énoncer** les propriétés de l'algèbre de Boole (commutativité, associativité, distributivité, idempotence, absorption, complément, lois de De Morgan) ;
2. **Simplifier** une expression à trois variables au plus, par calcul algébrique ou par tableau de Karnaugh ;
3. **Écrire** une expression à partir d'une table de vérité (somme de produits) ;
4. **Exprimer** les opérations ET, OU, NON, OU exclusif à l'aide de NAND ou NOR ;
5. **Appliquer** le ET bit à bit pour calculer une adresse réseau à partir d'une adresse IPv4 et d'un masque.

## Contenu de la séance

| Document | Rôle |
|---|---|
| [Cours – Algèbre de Boole](01-cours.md) | Cours |
| [Exercices – Simplifier des expressions booléennes](02-exercices.md) | Exercices |
| [TP Python – Karnaugh, additionneur et masques](03-tp-python.md) | TP (éditeur Python intégré) |
| [Aide-mémoire – Algèbre de Boole](04-aide-memoire.md) | Aide-mémoire |
| [Annexe – Masques et adressage IPv4](annexe-adressage.md) | Application aux réseaux |

## Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 15 | **Rappel** S08 : tables de vérité | Oral |
| 0 h 15 – 1 h 25 | **Cours** : axiomes, propriétés, simplification, Karnaugh, NAND/NOR | Cours et questions |
| 1 h 25 – 2 h 30 | **Exercices** | Individuel, puis binômes |
| 2 h 30 – 3 h 45 | **TP Python** : masques, additionneur, vérification de simplifications | Individuel |
| 3 h 45 – 4 h 00 | **Auto-évaluation** | Individuel |

*Durées indicatives : la séance dure 4 h ; l'enseignant ajuste selon le rythme du groupe.*

## Application en informatique

Masque de sous-réseau et adresse réseau (ET bit à bit), additionneur binaire, réduction du nombre de portes d'un circuit, simplification de règles de filtrage.

## Évaluation

- Feuille d'exercices corrigée, scripts du TP validés.
- Auto-évaluation « Je sais faire » en fin d'exercices.

<details markdown="1">
<summary>Notes pour l'enseignant</summary>

- **Programme :** le chapitre est rattaché au programme officiel de mathématiques pour l'informatique (voir [Programme et épreuve E3](../../ressources/programme-e3.md)) ; la répartition en séances est une proposition à valider.
- Le programme limite la simplification à trois variables (Karnaugh ou propriétés algébriques) et demande de mentionner NAND et NOR.
- Le calcul d'adresses (CIDR, VLSM) est regroupé dans l'annexe de cette séance : c'est l'application réseau principale du chapitre.

</details>

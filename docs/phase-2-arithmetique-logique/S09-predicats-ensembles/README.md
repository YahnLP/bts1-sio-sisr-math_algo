# S09 – Prédicats, quantificateurs et langage ensembliste

| Élément | Détail |
|---|---|
| **Niveau** | BTS SIO option SISR, 1re année – mathématiques pour l'informatique |
| **Séance** | S09 (séance 9 sur 19) – Phase 2 |
| **Durée** | 4 heures |
| **Chapitre du programme** | Logique – prédicats ; langage ensembliste |
| **Prérequis** | S08 (connecteurs logiques). |
| **Outils** | Papier, calculatrice, éditeur Python intégré au site |

> [!NOTE]
> **Question qui guide la séance :** *« Comment exprimer « tous les utilisateurs » ou « au moins un serveur », et raisonner sur des groupes avec les ensembles ? »*

## Objectifs

À la fin de la séance, l'étudiant est capable de :

1. **Écrire** un prédicat à une, deux ou trois variables et **évaluer** sa valeur de vérité ;
2. **Utiliser** les quantificateurs ∀ et ∃ et **nier** correctement une phrase quantifiée ;
3. **Expliquer** que l'ordre des quantificateurs change le sens ;
4. **Manipuler** ensembles, appartenance, inclusion, parties, complémentaire, intersection, réunion, différence ;
5. **Relier** connecteurs et opérations sur les ensembles et **calculer** un cardinal avec \(|A \cup B| = |A| + |B| - |A \cap B|\).

## Contenu de la séance

| Document | Rôle |
|---|---|
| [Cours – Prédicats et ensembles](01-cours.md) | Cours |
| [Exercices – Quantificateurs et ensembles](02-exercices.md) | Exercices |
| [TP Python – Ensembles en Python](03-tp-python.md) | TP (éditeur Python intégré) |
| [Aide-mémoire – Prédicats et ensembles](04-aide-memoire.md) | Aide-mémoire |

## Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Accroche** : « tous les comptes ont un mot de passe » — comment le nier ? | Oral |
| 0 h 20 – 1 h 30 | **Cours** : prédicats, quantificateurs, ensembles, lien avec les connecteurs | Cours et questions |
| 1 h 30 – 2 h 45 | **Exercices** | Individuel, puis binômes |
| 2 h 45 – 3 h 45 | **TP Python** : groupes d'utilisateurs avec `set` | Individuel |
| 3 h 45 – 4 h 00 | **Auto-évaluation** | Individuel |

*Durées indicatives : la séance dure 4 h ; l'enseignant ajuste selon le rythme du groupe.*

## Application en informatique

Appartenance à des groupes (annuaire), droits cumulés ou communs (réunion, intersection), vérification « pour tout / il existe » sur des listes de comptes.

## Évaluation

- Feuille d'exercices corrigée, scripts du TP validés.
- Auto-évaluation « Je sais faire » en fin d'exercices.

<details markdown="1">
<summary>Notes pour l'enseignant</summary>

- **Programme :** le chapitre est rattaché au programme officiel de mathématiques pour l'informatique (voir [Programme et épreuve E3](../../ressources/programme-e3.md)) ; la répartition en séances est une proposition à valider.
- **Corrigé :** dans `corriges/` à la racine du dépôt (hors du site publié).
- Les prédicats sont limités à trois variables au plus, et l'ordre des quantificateurs est souligné, conformément au programme.

</details>

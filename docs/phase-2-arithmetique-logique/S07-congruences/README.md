# S07 – Congruences

| Élément | Détail |
|---|---|
| **Niveau** | BTS SIO option SISR, 1re année – mathématiques pour l'informatique |
| **Séance** | S07 (séance 7 sur 19) – Phase 2 |
| **Durée** | 4 heures |
| **Chapitre du programme** | Arithmétique – congruences |
| **Prérequis** | S05, S06 (division euclidienne, premiers entre eux). |
| **Outils** | Papier, calculatrice, éditeur Python intégré au site |

> [!NOTE]
> **Question qui guide la séance :** *« Comment calculer « à l'horloge », et à quoi cela sert-il (clés de contrôle, chiffrement, hachage) ? »*

## Objectifs

À la fin de la séance, l'étudiant est capable de :

1. **Définir** la congruence modulo \(n\) et **passer** de \(a \equiv b \pmod n\) à \(n \mid a - b\) ;
2. **Utiliser** les propriétés de compatibilité avec l'addition et la multiplication, et **calculer** une puissance modulo \(n\) ;
3. **Déterminer** si un entier a un inverse modulo \(n\) et **le calculer** pour de petits modules ;
4. **Chiffrer** et **déchiffrer** avec le code de César et le code affine ;
5. **Calculer** une clé de contrôle (numéro de sécurité sociale, ISBN-13, IBAN) et **parcourir** une liste circulaire.

## Contenu de la séance

| Document | Rôle |
|---|---|
| [Cours – Congruences](01-cours.md) | Cours |
| [Exercices – Calculs modulo n et applications](02-exercices.md) | Exercices |
| [TP Python – Chiffrement et clés de contrôle](03-tp-python.md) | TP (éditeur Python intégré) |
| [Aide-mémoire – Congruences](04-aide-memoire.md) | Aide-mémoire |

## Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Accroche** : quelle heure sera-t-il dans 100 heures ? | Oral |
| 0 h 20 – 1 h 30 | **Cours** : définition, propriétés, inverse, applications | Cours et questions |
| 1 h 30 – 2 h 45 | **Exercices** | Individuel, puis binômes |
| 2 h 45 – 3 h 45 | **TP Python** : César, affine, clés de contrôle | Individuel |
| 3 h 45 – 4 h 00 | **Auto-évaluation** | Individuel |

*Durées indicatives : la séance dure 4 h ; l'enseignant ajuste selon le rythme du groupe.*

## Application en informatique

Détecter une erreur de saisie (clés de contrôle), chiffrer (code affine : introduction à la cryptographie), répartir des éléments dans une table de hachage (\(h(x) = x \bmod m\)), parcourir une liste circulaire.

## Évaluation

- Feuille d'exercices corrigée, scripts du TP validés.
- Auto-évaluation « Je sais faire » en fin d'exercices.

<details markdown="1">
<summary>Notes pour l'enseignant</summary>

- **Programme :** le chapitre est rattaché au programme officiel de mathématiques pour l'informatique (voir [Programme et épreuve E3](../../ressources/programme-e3.md)) ; la répartition en séances est une proposition à valider.
- Les exemples d'IBAN et de numéro de sécurité sociale sont **fictifs** (numéros de test), voir le cours.
- Le programme cite les congruences et leurs propriétés élémentaires, la cryptographie, la correction d'erreurs et le parcours circulaire.

</details>

# Exercices – Chemin optimal et planification

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S17*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**, avec la méthode du cours : écris les étapes, pas seulement le résultat. Ouvre ensuite « Voir la réponse » pour te corriger. À l'épreuve, **aucune réponse sans justification** n'est complète.

Dans tous les exercices, la **méthode à suivre** est indiquée : Dijkstra pour les chemins de valeur minimale, MPM (avec les définitions du cours) pour l'ordonnancement.

## Exercice 1 – Dijkstra

Dans le graphe valué de sommets \(A, \dots, F\) et d'arcs A→B (7), A→C (9), A→F (14), B→C (10), B→D (15), C→D (11), C→F (2), D→E (6), F→E (9), déterminer par la **méthode de Dijkstra** les valeurs minimales depuis \(A\), puis le chemin de valeur minimale de \(A\) vers \(E\).

<details markdown="1">
<summary>Voir la réponse</summary>

<figure class="graphe diagramme">
<svg viewBox="0.00 0.00 530.60 167.60" style="max-width:708px" role="img" aria-label="Schéma" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g class="graph" transform="scale(1 1) rotate(0) translate(10.8 156.8)">
<g class="node n&#45;circle">
<ellipse fill="none" stroke="black" stroke-width="1.8" cx="22.5" cy="-46.5" rx="22.5" ry="22.5"/>
<text text-anchor="middle" x="22.5" y="-43" font-family="Helvetica,sans-Serif" font-size="15.00">A</text>
</g>
<g class="node n&#45;circle">
<ellipse fill="none" stroke="black" stroke-width="1.8" cx="134.5" cy="-123.5" rx="22.5" ry="22.5"/>
<text text-anchor="middle" x="134.5" y="-120" font-family="Helvetica,sans-Serif" font-size="15.00">B</text>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M41.66,-59.21C59.84,-71.94 87.96,-91.62 108.3,-105.86"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="106.49,-108.44 115.67,-111.02 110.11,-103.28 106.49,-108.44"/>
<text text-anchor="start" x="74" y="-90.1" font-family="Helvetica,sans-Serif" font-size="13.00">7</text>
</g>
<g class="node n&#45;circle">
<ellipse fill="none" stroke="black" stroke-width="1.8" cx="254.5" cy="-48.5" rx="22.5" ry="22.5"/>
<text text-anchor="middle" x="254.5" y="-45" font-family="Helvetica,sans-Serif" font-size="15.00">C</text>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M45.14,-46.69C86.15,-47.04 175.31,-47.82 222.6,-48.23"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="222.73,-51.38 231.75,-48.31 222.78,-45.08 222.73,-51.38"/>
<text text-anchor="start" x="130" y="-51.1" font-family="Helvetica,sans-Serif" font-size="13.00">9</text>
</g>
<g class="node n&#45;circle">
<ellipse fill="none" stroke="black" stroke-width="1.8" cx="374.5" cy="-22.5" rx="22.5" ry="22.5"/>
<text text-anchor="middle" x="374.5" y="-19" font-family="Helvetica,sans-Serif" font-size="15.00">F</text>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M44.07,-39.65C87.08,-26.11 189.73,2.13 277,-5.5 299.33,-7.45 324.23,-11.9 343.15,-15.75"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="342.72,-18.88 352.18,-17.64 344.01,-12.72 342.72,-18.88"/>
<text text-anchor="middle" x="194.5" y="-12.1" font-family="Helvetica,sans-Serif" font-size="13.00">14</text>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M153.94,-111.78C173.68,-99.23 205.17,-79.22 227.44,-65.06"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="229.29,-67.62 235.19,-60.14 225.91,-62.31 229.29,-67.62"/>
<text text-anchor="start" x="186" y="-93.1" font-family="Helvetica,sans-Serif" font-size="13.00">10</text>
</g>
<g class="node n&#45;circle">
<ellipse fill="none" stroke="black" stroke-width="1.8" cx="374.5" cy="-107.5" rx="22.5" ry="22.5"/>
<text text-anchor="middle" x="374.5" y="-104" font-family="Helvetica,sans-Serif" font-size="15.00">D</text>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M157.04,-122.05C199.41,-119.2 293.73,-112.86 342.68,-109.57"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="343.07,-112.7 351.84,-108.96 342.65,-106.42 343.07,-112.7"/>
<text text-anchor="middle" x="254.5" y="-120.1" font-family="Helvetica,sans-Serif" font-size="13.00">15</text>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M274.99,-58.24C294.29,-67.89 324.03,-82.76 345.79,-93.64"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="344.53,-96.54 353.99,-97.74 347.34,-90.9 344.53,-96.54"/>
<text text-anchor="start" x="306" y="-85.1" font-family="Helvetica,sans-Serif" font-size="13.00">11</text>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M276.6,-43.34C285.64,-41.17 296.32,-38.65 306,-36.5 318.17,-33.79 331.61,-30.97 343.27,-28.58"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="344,-31.64 352.19,-26.76 342.74,-25.47 344,-31.64"/>
<text text-anchor="start" x="310" y="-40.1" font-family="Helvetica,sans-Serif" font-size="13.00">2</text>
</g>
<g class="node n&#45;circle">
<ellipse fill="none" stroke="black" stroke-width="1.8" cx="486.5" cy="-64.5" rx="22.5" ry="22.5"/>
<text text-anchor="middle" x="486.5" y="-61" font-family="Helvetica,sans-Serif" font-size="15.00">E</text>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M395.68,-99.61C412.7,-92.96 437.29,-83.34 456.44,-75.86"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="457.84,-78.69 465.08,-72.48 455.55,-72.83 457.84,-78.69"/>
<text text-anchor="start" x="426" y="-90.1" font-family="Helvetica,sans-Serif" font-size="13.00">6</text>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M396.85,-26.05C408.38,-28.32 422.73,-31.76 435,-36.5 443.1,-39.63 451.51,-43.85 459.08,-48.06"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="457.55,-50.81 466.92,-52.58 460.69,-45.36 457.55,-50.81"/>
<text text-anchor="start" x="426" y="-40.1" font-family="Helvetica,sans-Serif" font-size="13.00">9</text>
</g>
</g>
</svg>
</figure>

| Étape | Sommet fixé | A | B | C | D | E | F |
|---|---|---|---|---|---|---|---|
| 1 | **A** | **0** | 7 (A) | 9 (A) | ∞ | ∞ | 14 (A) |
| 2 | **B** | 0 | **7** | 9 (A) | 22 (B) | ∞ | 14 (A) |
| 3 | **C** | 0 | 7 (A) | **9** | 20 (C) | ∞ | 11 (C) |
| 4 | **F** | 0 | 7 (A) | 9 (A) | 20 (C) | 20 (F) | **11** |
| 5 | **D** | 0 | 7 (A) | 9 (A) | **20** | 20 (F) | 11 (C) |
| 6 | **E** | 0 | 7 (A) | 9 (A) | 20 (C) | **20** | 11 (C) |

(à l'étape 5, \(D\) et \(E\) ont la même valeur 20 : on fixe l'un des deux, le résultat final ne change pas.)

Valeurs minimales depuis \(A\) : A : 0, B : 7, C : 9, D : 20, E : 20, F : 11. Chemin de \(A\) à \(E\) : A → C → F → E, de valeur 20 ; un contrôle indépendant du chemin vers \(D\) donne \(A \to C \to D\) (valeur 20).

</details>

## Exercice 2 – Moins d'arcs, moins de valeur ?

Dans le graphe du cours (sites \(S, A, B, C, D, T\)), le chemin \(S \to B \to D \to T\) n'a que 3 arcs. Compare-le avec le chemin de valeur minimale.

<details markdown="1">
<summary>Voir la réponse</summary>

\(S \to B \to D \to T\) vaut \(2 + 10 + 3 = 15\), alors que le chemin minimal S → B → A → C → D → T vaut 13 avec 5 arcs. Un chemin avec plus d'arcs peut être moins cher.

</details>

## Exercice 3 – Un projet complet

Migration d'un serveur de fichiers :

| Tâche | Désignation | Durée (jours) | Prédécesseurs |
|---|---|---|---|
| **A** | Sauvegarde complète | 2 | — |
| **B** | Installation du nouveau serveur | 4 | — |
| **C** | Restauration des données | 3 | A, B |
| **D** | Tests applicatifs | 2 | C |
| **E** | Formation des administrateurs | 5 | B |
| **F** | Bascule | 1 | D, E |

1. Construire le graphe MPM (avec Début et Fin).
2. Calculer les dates au plus tôt et au plus tard, puis les trois marges de chaque tâche.
3. Donner la durée minimale du projet, les tâches critiques et le(s) chemin(s) critique(s).

<details markdown="1">
<summary>Voir la réponse</summary>

1–2. ```mermaid
flowchart LR
    D((Début))
    A["A (2)<br/>t = 0 · T = 2"]
    B["B (4)<br/>t = 0 · T = 0"]
    C["C (3)<br/>t = 4 · T = 4"]
    D["D (2)<br/>t = 7 · T = 7"]
    E["E (5)<br/>t = 4 · T = 4"]
    F["F (1)<br/>t = 9 · T = 9"]
    Z((Fin<br/>10))
    D --> A
    D --> B
    A --> C
    B --> C
    C --> D
    B --> E
    D --> F
    E --> F
    F --> Z
    style B stroke-width:4px
    style C stroke-width:4px
    style D stroke-width:4px
    style E stroke-width:4px
    style F stroke-width:4px
```

| Tâche | Désignation | Durée | Prédécesseurs | Au plus tôt \(t\) | Au plus tard \(T\) | Marge totale | Marge libre | Marge certaine |
|---|---|---|---|---|---|---|---|---|
| **A** | Sauvegarde complète | 2 | — | 0 | 2 | 2 | 2 | 2 |
| **B** | Installation du nouveau serveur | 4 | — | 0 | 0 | 0 | 0 | 0 |
| **C** | Restauration des données | 3 | A, B | 4 | 4 | 0 | 0 | 0 |
| **D** | Tests applicatifs | 2 | C | 7 | 7 | 0 | 0 | 0 |
| **E** | Formation des administrateurs | 5 | B | 4 | 4 | 0 | 0 | 0 |
| **F** | Bascule | 1 | D, E | 9 | 9 | 0 | 0 | 0 |

3. Durée minimale : **10 jours**. Tâches critiques (\(M_T = 0\)) : B, C, D, E, F. Il y a **deux chemins critiques** : \(B \to C \to D \to F\) (\(4 + 3 + 2 + 1 = 10\)) et \(B \to E \to F\) (\(4 + 5 + 1 = 10\)). Seule \(A\) a une marge (2 jours, identique pour les trois marges).

</details>

## Exercice 4 – Et si une tâche prend du retard ?

Dans le projet de l'exercice 3, quelle est la nouvelle durée du projet si : (a) \(A\) dure 2 jours de plus ? (b) \(A\) dure 3 jours de plus ? (c) \(E\) dure 2 jours de plus ? (d) \(D\) dure 1 jour de plus ? Quelle conclusion tirer ?

<details markdown="1">
<summary>Voir la réponse</summary>

| Cas | Durée du projet | Explication |
|---|---|---|
| (a) \(A\) +2 | 10 | 2 = marge totale de \(A\) : aucun effet |
| (b) \(A\) +3 | 11 | dépasse la marge de 1 jour : le projet est retardé de 1 jour |
| (c) \(E\) +2 | 12 | \(E\) est critique : retard de 2 jours |
| (d) \(D\) +1 | 11 | \(D\) est critique : retard de 1 jour |

Une tâche critique retarde le projet jour pour jour ; une tâche non critique ne le retarde que si son retard dépasse sa marge totale.

</details>

## Exercice 5 – Lire les marges

Dans le projet du cours (déploiement d'une salle, \(18\) jours), répondre en utilisant le tableau des marges :

1. Quelles tâches sont critiques ?
2. De combien de jours peut-on retarder \(G\) sans retarder le projet ? Et \(B\) ?
3. Si \(B\) prend 1 jour de retard, quelles tâches suivantes sont décalées dans leur démarrage au plus tôt ?
4. Vérifier : la durée du projet change-t-elle si \(G\) dure 8 jours de plus ? 9 jours de plus ?

<details markdown="1">
<summary>Voir la réponse</summary>

| Tâche | Désignation | Durée | Prédécesseurs | Au plus tôt \(t\) | Au plus tard \(T\) | Marge totale | Marge libre | Marge certaine |
|---|---|---|---|---|---|---|---|---|
| **A** | Audit de l'existant | 3 | — | 0 | 0 | 0 | 0 | 0 |
| **B** | Commande du matériel | 2 | A | 3 | 4 | 1 | 0 | 0 |
| **C** | Livraison du matériel | 6 | B | 5 | 6 | 1 | 1 | 0 |
| **D** | Préparation de la salle | 4 | A | 3 | 3 | 0 | 0 | 0 |
| **E** | Câblage réseau | 5 | D | 7 | 7 | 0 | 0 | 0 |
| **F** | Installation des postes | 4 | C, E | 12 | 12 | 0 | 0 | 0 |
| **G** | Configuration du serveur | 3 | B | 5 | 13 | 8 | 8 | 7 |
| **H** | Recette et formation | 2 | F, G | 16 | 16 | 0 | 0 | 0 |

1. A, D, E, F, H (\(M_T = 0\)).
2. \(G\) : 8 jours ; \(B\) : 1 jour.
3. \(M_L(B) = 0\) : tout retard de \(B\) décale le début de \(C\) et \(G\) (qui ne peuvent plus commencer à leur date au plus tôt). Mais le projet n'est pas retardé tant que \(C\) a de la marge (\(M_T(C) = 1\)).
4. +8 jours : durée 18 (pas de changement) ; +9 jours : 19 (1 jour de retard). (Recalcul complet par la méthode.)

</details>

## Exercice 6 – Écrire l'algorithme

Écrire en pseudo-code le calcul des dates au plus tôt : on parcourt les tâches dans un ordre compatible avec les antériorités (niveaux) et, pour chacune, on prend le maximum de (date au plus tôt + durée) sur ses prédécesseurs.

<details markdown="1">
<summary>Voir la réponse</summary>

```text
ALGORITHME dates_au_plus_tot
  ENTRÉES   : tâches classées par niveaux ; d[x] durée ; pred[x] prédécesseurs
  SORTIE    : t[x] pour chaque tâche
DÉBUT
  POUR chaque tâche x, dans l'ordre des niveaux, FAIRE
    t[x] ← 0
    POUR chaque p dans pred[x] FAIRE
      SI t[p] + d[p] > t[x] ALORS
        t[x] ← t[p] + d[p]
      FIN SI
    FIN POUR
  FIN POUR
FIN
```

Avec le projet du cours, l'algorithme donne A : 0, B : 3, C : 5, D : 3, E : 7, F : 12, G : 5, H : 16.

</details>


## Je sais faire

Coche honnêtement ; ce que tu ne coches pas se reprend avant la séance suivante.

- [ ] Calculer la valeur d'un chemin ;
- [ ] Trouver un chemin optimal avec la méthode indiquée ;
- [ ] Construire un graphe MPM ;
- [ ] Calculer dates au plus tôt et au plus tard ;
- [ ] Calculer les marges et le chemin critique.

**Ce que je dois reprendre :** ______________________

**Ma question à poser à l'enseignant :** ______________________

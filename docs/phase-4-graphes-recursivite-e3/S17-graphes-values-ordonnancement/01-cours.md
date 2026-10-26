# Cours – Graphes valués, chemin optimal et ordonnancement MPM

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S17 – à lire avant les [exercices](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** S16 (graphes, niveaux).
> - **Outils :** Papier, calculatrice, éditeur Python intégré au site

## À la fin de ce cours tu sauras

- [ ] **Définir** un graphe valué et la longueur (valeur) d'un chemin ;
- [ ] **Déterminer** un chemin de valeur minimale par une méthode donnée ;
- [ ] **Construire** le graphe d'ordonnancement MPM d'un projet à partir d'un tableau de tâches ;
- [ ] **Calculer** les dates au plus tôt et au plus tard, les marges totale, libre et certaine ;
- [ ] **Identifier** les tâches critiques et le chemin critique, et **conclure** sur la durée minimale du projet.

## I. Graphes valués et chemin de valeur minimale

Un graphe est **valué** quand chaque arc porte un nombre (sa **valeur** : coût, durée, latence, distance…). La **valeur d'un chemin** est la somme des valeurs de ses arcs.

**Exemple.** Réseau de six sites ; les valeurs sont des latences en ms.

<figure class="graphe diagramme">
<svg viewBox="0.00 0.00 634.60 215.60" style="max-width:847px" role="img" aria-label="Schéma" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g class="graph" transform="scale(1 1) rotate(0) translate(10.8 204.8)">
<g class="node n&#45;circle">
<ellipse fill="none" stroke="black" stroke-width="1.8" cx="22.5" cy="-52.5" rx="22.5" ry="22.5"/>
<text text-anchor="middle" x="22.5" y="-49" font-family="Helvetica,sans-Serif" font-size="15.00">S</text>
</g>
<g class="node n&#45;circle">
<ellipse fill="none" stroke="black" stroke-width="1.8" cx="246.5" cy="-22.5" rx="22.5" ry="22.5"/>
<text text-anchor="middle" x="246.5" y="-19" font-family="Helvetica,sans-Serif" font-size="15.00">A</text>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M45.19,-49.57C84.92,-44.2 169.44,-32.78 214.96,-26.63"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="215.55,-29.73 224.05,-25.4 214.71,-23.48 215.55,-29.73"/>
<text text-anchor="start" x="130" y="-43.1" font-family="Helvetica,sans-Serif" font-size="13.00">4</text>
</g>
<g class="node n&#45;circle">
<ellipse fill="none" stroke="black" stroke-width="1.8" cx="134.5" cy="-110.5" rx="22.5" ry="22.5"/>
<text text-anchor="middle" x="134.5" y="-107" font-family="Helvetica,sans-Serif" font-size="15.00">B</text>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M42.66,-62.6C60.22,-71.86 86.41,-85.67 106.16,-96.09"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="104.76,-98.91 114.19,-100.32 107.7,-93.33 104.76,-98.91"/>
<text text-anchor="start" x="74" y="-86.1" font-family="Helvetica,sans-Serif" font-size="13.00">2</text>
</g>
<g class="node n&#45;circle">
<ellipse fill="none" stroke="black" stroke-width="1.8" cx="366.5" cy="-105.5" rx="22.5" ry="22.5"/>
<text text-anchor="middle" x="366.5" y="-102" font-family="Helvetica,sans-Serif" font-size="15.00">C</text>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M265.42,-35.11C285.26,-49.06 317.4,-71.67 339.89,-87.49"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="338.24,-90.17 347.41,-92.78 341.86,-85.02 338.24,-90.17"/>
<text text-anchor="start" x="302" y="-72.1" font-family="Helvetica,sans-Serif" font-size="13.00">5</text>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M152.69,-96.75C171.09,-82.03 200.45,-58.54 221.21,-41.93"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="223.37,-44.24 228.43,-36.15 219.44,-39.32 223.37,-44.24"/>
<text text-anchor="start" x="186" y="-72.1" font-family="Helvetica,sans-Serif" font-size="13.00">1</text>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M157.14,-110.03C198.15,-109.14 287.31,-107.2 334.6,-106.17"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="334.82,-109.32 343.75,-105.97 334.69,-103.02 334.82,-109.32"/>
<text text-anchor="start" x="242" y="-111.1" font-family="Helvetica,sans-Serif" font-size="13.00">8</text>
</g>
<g class="node n&#45;circle">
<ellipse fill="none" stroke="black" stroke-width="1.8" cx="478.5" cy="-171.5" rx="22.5" ry="22.5"/>
<text text-anchor="middle" x="478.5" y="-168" font-family="Helvetica,sans-Serif" font-size="15.00">D</text>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M153.35,-123.17C162.65,-129.13 174.47,-135.74 186,-139.5 277.32,-169.29 392.37,-172.55 446.57,-172.21"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="446.69,-175.35 455.65,-172.11 446.62,-169.05 446.69,-175.35"/>
<text text-anchor="start" x="298" y="-168.1" font-family="Helvetica,sans-Serif" font-size="13.00">10</text>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M386.16,-116.7C403.94,-127.36 430.89,-143.53 450.91,-155.55"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="449.41,-158.32 458.75,-160.25 452.65,-152.92 449.41,-158.32"/>
<text text-anchor="start" x="418" y="-143.1" font-family="Helvetica,sans-Serif" font-size="13.00">2</text>
</g>
<g class="node n&#45;circle">
<ellipse fill="none" stroke="black" stroke-width="1.8" cx="590.5" cy="-127.5" rx="22.5" ry="22.5"/>
<text text-anchor="middle" x="590.5" y="-124" font-family="Helvetica,sans-Serif" font-size="15.00">T</text>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M389.27,-106.73C415.73,-108.31 461.71,-111.37 501,-115.5 520.39,-117.54 542.07,-120.47 559.13,-122.92"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="558.72,-126.05 568.08,-124.23 559.63,-119.81 558.72,-126.05"/>
<text text-anchor="start" x="474" y="-119.1" font-family="Helvetica,sans-Serif" font-size="13.00">6</text>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M499.68,-163.43C516.89,-156.55 541.83,-146.57 561.06,-138.87"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="562.27,-141.79 569.45,-135.52 559.93,-135.94 562.27,-141.79"/>
<text text-anchor="start" x="530" y="-154.1" font-family="Helvetica,sans-Serif" font-size="13.00">3</text>
</g>
</g>
</svg>
</figure>

On cherche le chemin de **valeur minimale** de \(S\) vers \(T\). Un parcours direct de tous les chemins devient vite impossible quand le graphe grandit : on utilise une **méthode** systématique.

### Méthode de Dijkstra (valeurs positives)

1. On affecte à \(S\) la valeur 0 et à tous les autres sommets la valeur \(\infty\).
2. On **fixe** le sommet non encore fixé de plus petite valeur.
3. Pour chacun de ses successeurs \(y\) non fixés, si (valeur du sommet fixé + valeur de l'arc) est **inférieure** à la valeur actuelle de \(y\), on met à jour la valeur de \(y\) et on note son prédécesseur.
4. On recommence en 2 jusqu'à fixer tous les sommets (ou \(T\)).
5. On lit le chemin à l'envers, de \(T\) vers \(S\), grâce aux prédécesseurs notés.

Déroulement (entre parenthèses : le prédécesseur provisoire ; en gras : valeur fixée) :

| Étape | Sommet fixé | S | A | B | C | D | T |
|---|---|---|---|---|---|---|---|
| 1 | **S** | **0** | 4 (S) | 2 (S) | ∞ | ∞ | ∞ |
| 2 | **B** | 0 | 3 (B) | **2** | 10 (B) | 12 (B) | ∞ |
| 3 | **A** | 0 | **3** | 2 (S) | 8 (A) | 12 (B) | ∞ |
| 4 | **C** | 0 | 3 (B) | 2 (S) | **8** | 10 (C) | 14 (C) |
| 5 | **D** | 0 | 3 (B) | 2 (S) | 8 (A) | **10** | 13 (D) |
| 6 | **T** | 0 | 3 (B) | 2 (S) | 8 (A) | 10 (C) | **13** |

Valeur minimale de \(S\) à \(T\) : **13**. Chemin (lu à l'envers grâce aux prédécesseurs) : S → B → A → C → D → T, de valeur 2 + 1 + 5 + 2 + 3 = 13. À titre de comparaison, le chemin \(S \to B \to D \to T\), qui semble plus court (3 arcs seulement), vaut 15 : **moins d'arcs ne veut pas dire moins de valeur**.

> [!WARNING]
> Dijkstra suppose des valeurs **positives ou nulles**. Avec des valeurs négatives, la méthode peut se tromper (hors programme).

Le tableau donne aussi les valeurs minimales de \(S\) vers tous les autres sommets : \(A\) : 3, \(B\) : 2, \(C\) : 8, \(D\) : 10. Ces résultats ont été recoupés avec une bibliothèque de graphes.

## II. Ordonnancement d'un projet : la méthode MPM

Un **projet** est un ensemble de **tâches** de durées connues, liées par des **contraintes d'antériorité** (une tâche ne commence qu'après la fin de certaines autres). La méthode **MPM** (méthode des potentiels Métra) répond à deux questions : **quelle est la durée minimale du projet ?** et **quelles tâches ne doivent pas prendre de retard ?**

**Exemple : déploiement d'une salle informatique.**

| Tâche | Désignation | Durée (jours) | Prédécesseurs |
|---|---|---|---|
| **A** | Audit de l'existant | 3 | — |
| **B** | Commande du matériel | 2 | A |
| **C** | Livraison du matériel | 6 | B |
| **D** | Préparation de la salle | 4 | A |
| **E** | Câblage réseau | 5 | D |
| **F** | Installation des postes | 4 | C, E |
| **G** | Configuration du serveur | 3 | B |
| **H** | Recette et formation | 2 | F, G |

### MPM et PERT : deux représentations du même problème

La méthode **PERT** répond aux mêmes questions que la MPM (durée minimale, dates au plus tôt et au plus tard, marges, chemin critique) avec une autre représentation.

| | **MPM** | **PERT** |
|---|---|---|
| Une tâche est | un **sommet** (case avec sa durée) | un **arc** (flèche portant son nom et sa durée) |
| Un sommet représente | une tâche | une **étape** (un événement : « tout ce qui précède est terminé ») |
| Contrainte d'antériorité | un arc entre deux tâches | deux arcs qui se suivent ; au besoin, un **arc fictif** de durée 0 |
| Résultats | identiques | identiques |

Les calculs sont les mêmes : date au plus tôt = plus long chemin depuis le début, date au plus tard = on remonte depuis la fin, marge = écart entre les deux. Ce site utilise la MPM ; si un énoncé est donné en PERT, on lit chaque arc comme une tâche et chaque étape comme un jalon, puis on applique les mêmes formules.

### Le graphe MPM

- Chaque tâche est un **sommet** portant sa durée ;
- un arc va d'une tâche vers chacune de ses **successeurs**, valué par la **durée de la tâche de départ** ;
- on ajoute un sommet **Début** (relié aux tâches sans prédécesseur) et un sommet **Fin** (relié aux tâches sans successeur).

### Dates au plus tôt \(t\)

\(t(\text{Début}) = 0\). Une tâche ne peut commencer qu'une fois **tous** ses prédécesseurs finis :

\[
t(x) = \max_{p \in \text{prédécesseurs}} \bigl(t(p) + d(p)\bigr)
\]

(maximum sur les prédécesseurs). On parcourt le graphe **dans l'ordre des niveaux** (S16). La date de Fin donne la **durée minimale du projet**.

Ici : \(t(A) = 0\), \(t(B) = 3\), \(t(C) = 5\), \(t(D) = 3\), \(t(E) = 7\), \(t(F) = 12\), \(t(G) = 5\), \(t(H) = 16\), et \(t(\text{Fin}) = 18\) : **durée minimale du projet : 18 jours**. Par exemple \(t(F) = \max(t(C) + d(C),\ t(E) + d(E)) = \max(5 + 6,\ 7 + 5) = 12\).

### Dates au plus tard \(T\)

\(T(\text{Fin}) = t(\text{Fin})\). On remonte le graphe (sens inverse) : une tâche doit finir à temps pour **tous** ses successeurs :

\[
T(x) = \min_{s \in \text{successeurs}} T(s) \;-\; d(x)
\]

(minimum sur les successeurs ; pour une tâche sans successeur, on utilise \(T(\text{Fin})\)). Ici : \(T(A) = 0\), \(T(B) = 4\), \(T(C) = 6\), \(T(D) = 3\), \(T(E) = 7\), \(T(F) = 12\), \(T(G) = 13\), \(T(H) = 16\).

<figure class="graphe diagramme">
<svg viewBox="0.00 0.00 452.60 756.67" style="max-width:604px" role="img" aria-label="Schéma" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g class="graph" transform="scale(1 1) rotate(0) translate(10.8 745.87)">
<g class="node n&#45;circle">
<ellipse fill="none" stroke="black" stroke-width="1.8" cx="281" cy="-704.82" rx="30.5" ry="30.5"/>
<text text-anchor="start" x="258" y="-701.32" font-family="Helvetica,sans-Serif" font-size="15.00">Début</text>
</g>
<g class="node n&#45;rect">
<path fill="none" stroke="black" stroke-width="4" d="M334,-616.57C334,-616.57 228,-616.57 228,-616.57 222,-616.57 216,-610.57 216,-604.57 216,-604.57 216,-574.57 216,-574.57 216,-568.57 222,-562.57 228,-562.57 228,-562.57 334,-562.57 334,-562.57 340,-562.57 346,-568.57 346,-574.57 346,-574.57 346,-604.57 346,-604.57 346,-610.57 340,-616.57 334,-616.57"/>
<text text-anchor="start" x="262.5" y="-594.57" font-family="Helvetica,sans-Serif" font-size="15.00">A (3)</text>
<text text-anchor="start" x="235" y="-577.57" font-family="Helvetica,sans-Serif" font-size="15.00">t = 0 · T = 0</text>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M281,-674.36C281,-659.6 281,-641.61 281,-626.08"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="284.15,-625.79 281,-616.79 277.85,-625.79 284.15,-625.79"/>
</g>
<g class="node n&#45;rect">
<path fill="none" stroke="black" stroke-width="1.8" d="M249,-504.57C249,-504.57 143,-504.57 143,-504.57 137,-504.57 131,-498.57 131,-492.57 131,-492.57 131,-462.57 131,-462.57 131,-456.57 137,-450.57 143,-450.57 143,-450.57 249,-450.57 249,-450.57 255,-450.57 261,-456.57 261,-462.57 261,-462.57 261,-492.57 261,-492.57 261,-498.57 255,-504.57 249,-504.57"/>
<text text-anchor="start" x="177.5" y="-482.57" font-family="Helvetica,sans-Serif" font-size="15.00">B (2)</text>
<text text-anchor="start" x="150" y="-465.57" font-family="Helvetica,sans-Serif" font-size="15.00">t = 3 · T = 4</text>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M260.86,-562.5C249.19,-547.4 234.39,-528.24 221.87,-512.04"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="224.29,-510.03 216.29,-504.83 219.3,-513.88 224.29,-510.03"/>
</g>
<g class="node n&#45;rect">
<path fill="none" stroke="black" stroke-width="4" d="M419,-504.57C419,-504.57 313,-504.57 313,-504.57 307,-504.57 301,-498.57 301,-492.57 301,-492.57 301,-462.57 301,-462.57 301,-456.57 307,-450.57 313,-450.57 313,-450.57 419,-450.57 419,-450.57 425,-450.57 431,-456.57 431,-462.57 431,-462.57 431,-492.57 431,-492.57 431,-498.57 425,-504.57 419,-504.57"/>
<text text-anchor="start" x="347" y="-482.57" font-family="Helvetica,sans-Serif" font-size="15.00">D (4)</text>
<text text-anchor="start" x="320" y="-465.57" font-family="Helvetica,sans-Serif" font-size="15.00">t = 3 · T = 3</text>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M301.14,-562.5C312.81,-547.4 327.61,-528.24 340.13,-512.04"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="342.7,-513.88 345.71,-504.83 337.71,-510.03 342.7,-513.88"/>
</g>
<g class="node n&#45;rect">
<path fill="none" stroke="black" stroke-width="1.8" d="M249,-392.57C249,-392.57 143,-392.57 143,-392.57 137,-392.57 131,-386.57 131,-380.57 131,-380.57 131,-350.57 131,-350.57 131,-344.57 137,-338.57 143,-338.57 143,-338.57 249,-338.57 249,-338.57 255,-338.57 261,-344.57 261,-350.57 261,-350.57 261,-380.57 261,-380.57 261,-386.57 255,-392.57 249,-392.57"/>
<text text-anchor="start" x="177.5" y="-370.57" font-family="Helvetica,sans-Serif" font-size="15.00">C (6)</text>
<text text-anchor="start" x="150" y="-353.57" font-family="Helvetica,sans-Serif" font-size="15.00">t = 5 · T = 6</text>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M196,-450.5C196,-436.08 196,-417.96 196,-402.25"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="199.15,-401.83 196,-392.83 192.85,-401.83 199.15,-401.83"/>
</g>
<g class="node n&#45;rect">
<path fill="none" stroke="black" stroke-width="1.8" d="M128,-280.57C128,-280.57 12,-280.57 12,-280.57 6,-280.57 0,-274.57 0,-268.57 0,-268.57 0,-238.57 0,-238.57 0,-232.57 6,-226.57 12,-226.57 12,-226.57 128,-226.57 128,-226.57 134,-226.57 140,-232.57 140,-238.57 140,-238.57 140,-268.57 140,-268.57 140,-274.57 134,-280.57 128,-280.57"/>
<text text-anchor="start" x="51" y="-258.57" font-family="Helvetica,sans-Serif" font-size="15.00">G (3)</text>
<text text-anchor="start" x="19" y="-241.57" font-family="Helvetica,sans-Serif" font-size="15.00">t = 5 · T = 13</text>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M162.48,-450.57C144.91,-435.36 124.33,-414.81 111,-392.57 91.81,-360.56 81.06,-318.93 75.43,-289.8"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="78.5,-289.1 73.77,-280.81 72.3,-290.23 78.5,-289.1"/>
</g>
<g class="node n&#45;rect">
<path fill="none" stroke="black" stroke-width="4" d="M318,-280.57C318,-280.57 192,-280.57 192,-280.57 186,-280.57 180,-274.57 180,-268.57 180,-268.57 180,-238.57 180,-238.57 180,-232.57 186,-226.57 192,-226.57 192,-226.57 318,-226.57 318,-226.57 324,-226.57 330,-232.57 330,-238.57 330,-238.57 330,-268.57 330,-268.57 330,-274.57 324,-280.57 318,-280.57"/>
<text text-anchor="start" x="237" y="-258.57" font-family="Helvetica,sans-Serif" font-size="15.00">F (4)</text>
<text text-anchor="start" x="199" y="-241.57" font-family="Helvetica,sans-Serif" font-size="15.00">t = 12 · T = 12</text>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M209.98,-338.5C217.93,-323.68 227.99,-304.93 236.57,-288.92"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="239.44,-290.25 240.91,-280.83 233.88,-287.27 239.44,-290.25"/>
</g>
<g class="node n&#45;rect">
<path fill="none" stroke="black" stroke-width="4" d="M419,-392.57C419,-392.57 313,-392.57 313,-392.57 307,-392.57 301,-386.57 301,-380.57 301,-380.57 301,-350.57 301,-350.57 301,-344.57 307,-338.57 313,-338.57 313,-338.57 419,-338.57 419,-338.57 425,-338.57 431,-344.57 431,-350.57 431,-350.57 431,-380.57 431,-380.57 431,-386.57 425,-392.57 419,-392.57"/>
<text text-anchor="start" x="347.5" y="-370.57" font-family="Helvetica,sans-Serif" font-size="15.00">E (5)</text>
<text text-anchor="start" x="320" y="-353.57" font-family="Helvetica,sans-Serif" font-size="15.00">t = 7 · T = 7</text>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M366,-450.5C366,-436.08 366,-417.96 366,-402.25"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="369.15,-401.83 366,-392.83 362.85,-401.83 369.15,-401.83"/>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M339.69,-338.5C324.19,-323.13 304.43,-303.55 287.9,-287.17"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="290.11,-284.93 281.5,-280.83 285.68,-289.4 290.11,-284.93"/>
</g>
<g class="node n&#45;rect">
<path fill="none" stroke="black" stroke-width="4" d="M225,-168.57C225,-168.57 99,-168.57 99,-168.57 93,-168.57 87,-162.57 87,-156.57 87,-156.57 87,-126.57 87,-126.57 87,-120.57 93,-114.57 99,-114.57 99,-114.57 225,-114.57 225,-114.57 231,-114.57 237,-120.57 237,-126.57 237,-126.57 237,-156.57 237,-156.57 237,-162.57 231,-168.57 225,-168.57"/>
<text text-anchor="start" x="143" y="-146.57" font-family="Helvetica,sans-Serif" font-size="15.00">H (2)</text>
<text text-anchor="start" x="106" y="-129.57" font-family="Helvetica,sans-Serif" font-size="15.00">t = 16 · T = 16</text>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M232.96,-226.5C220.2,-211.4 204,-192.24 190.3,-176.04"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="192.42,-173.67 184.2,-168.83 187.61,-177.74 192.42,-173.67"/>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M91.8,-226.5C104.43,-211.4 120.45,-192.24 134,-176.04"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="136.68,-177.76 140.03,-168.83 131.84,-173.71 136.68,-177.76"/>
</g>
<g class="node n&#45;circle">
<ellipse fill="none" stroke="black" stroke-width="1.8" cx="162" cy="-28.28" rx="28.07" ry="28.07"/>
<text text-anchor="start" x="151" y="-33.28" font-family="Helvetica,sans-Serif" font-size="15.00">Fin</text>
<text text-anchor="start" x="152" y="-16.28" font-family="Helvetica,sans-Serif" font-size="15.00">18</text>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M162,-114.48C162,-99.98 162,-81.71 162,-65.81"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="165.15,-65.76 162,-56.76 158.85,-65.76 165.15,-65.76"/>
</g>
</g>
</svg>
</figure>

(chaque sommet : tâche, durée entre parenthèses, \(t\) et \(T\) ; encadrement épais = tâches critiques.)

### Marges

| Marge | Définition | Formule |
|---|---|---|
| **Totale** | retard maximal de la tâche **sans retarder la fin du projet** | \(M_T(x) = T(x) - t(x)\) |
| **Libre** | retard maximal **sans retarder aucune tâche suivante** (qui reste à son « au plus tôt ») | \(M_L(x) = \min_{s} t(s) - t(x) - d(x)\) |
| **Certaine** | retard possible **même si tous les prédécesseurs ont fini au plus tard** (et sans retarder les suivantes) | \(M_C(x) = \max\bigl(0,\ \min_s t(s) - \max_p (T(p) + d(p)) - d(x)\bigr)\) |

Les minimums portent sur les successeurs \(s\) (la Fin si la tâche n'en a pas) ; le maximum sur les prédécesseurs \(p\) (le Début, de date 0, s'il n'y en a pas). On a toujours \(M_C \le M_L \le M_T\).

> [!NOTE]
> **Vocabulaire.** Les noms « marge libre » et « marge certaine » sont utilisés avec des définitions voisines selon les ouvrages ; on retient celles du tableau, et un énoncé d'examen doit rappeler la définition attendue.

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

Lecture :

- la tâche **\(G\)** (configuration du serveur) peut être retardée de 8 jours sans retarder le projet (\(M_T = 8\)) ; elle ne gêne aucune tâche suivante pendant 8 jours (\(M_L = 8\)) ; et même si la commande \(B\) n'était terminée qu'au plus tard, elle garderait 7 jours de souplesse (\(M_C = 7\)) ;
- la tâche **\(B\)** a une marge totale de 1 jour mais une marge libre nulle : la retarder retarde \(C\) et \(G\), qui commencent tout de suite après (sans toutefois retarder le projet, car \(C\) a elle-même une marge de 1).

### Tâches critiques et chemin critique

Une tâche est **critique** si sa marge totale est **nulle** : tout retard retarde le projet. Les tâches critiques forment un **chemin critique** du Début à la Fin, dont la longueur est la durée minimale du projet.

Ici : **A → D → E → F → H**, soit 3 + 4 + 5 + 4 + 2 = 18 jours. (Les durées des tâches critiques s'additionnent : c'est un contrôle.) Ce chemin est le plus long chemin du graphe, ce qui a été recoupé avec une recherche exhaustive.

## III. Interpréter et décider

- Pour **réduire** la durée du projet, il faut agir sur une tâche **critique** : accélérer \(G\) ne sert à rien.
- Si une tâche non critique dépasse sa **marge totale**, elle devient critique et retarde le projet.
- Plusieurs chemins critiques peuvent exister : il faut alors agir sur **tous** pour gagner du temps.

## À retenir

- Dijkstra : fixer à chaque étape le sommet de plus petite valeur ; mettre à jour les successeurs ; remonter par les prédécesseurs.
- MPM : \(t(x) = \max(t(p) + d(p))\), \(T(x) = \min T(s) - d(x)\), \(M_T = T - t\).
- Marge libre \(M_L = \min t(s) - t(x) - d(x)\) ; marge certaine \(M_C = \max(0, \min t(s) - \max(T(p) + d(p)) - d(x))\).
- Tâche critique : \(M_T = 0\) ; chemin critique = plus long chemin = durée du projet.

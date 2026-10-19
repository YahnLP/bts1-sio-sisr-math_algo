# Cours – Produit cartésien, relations binaires et applications

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S11 – à lire avant les [exercices](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** S09 (ensembles).
> - **Outils :** Papier, calculatrice, éditeur Python intégré au site

## À la fin de ce cours tu sauras

- [ ] **Définir** le produit cartésien et **calculer** son cardinal ;
- [ ] **Étudier** une relation binaire (réflexive, symétrique, antisymétrique, transitive) ;
- [ ] **Reconnaître** une relation d'équivalence et **décrire** ses classes ; **reconnaître** une relation d'ordre ;
- [ ] **Distinguer** application, injection, surjection, bijection, et **composer** des applications ;
- [ ] **Déterminer** une image directe et une image réciproque.

## I. Produit cartésien

Le **produit cartésien** de deux ensembles \(A\) et \(B\) est l'ensemble des **couples** \((a, b)\) avec \(a \in A\) et \(b \in B\) :

\[
A \times B = \{(a, b) \mid a \in A,\ b \in B\}
\]

Un couple est **ordonné** : \((a, b) \neq (b, a)\) en général. Le cardinal du produit est \(\lvert A \times B \rvert = \lvert A \rvert \cdot \lvert B \rvert\).

**Exemple.** Avec \(A = \{1, 2, 3\}\) et \(B = \{x, y\}\) :

\[
A \times B = \{(1, 'x'), (1, 'y'), (2, 'x'), (2, 'y'), (3, 'x'), (3, 'y')\}
\]

soit \(3 \times 2 = 6\) couples. Avec trois protocoles et quatre ports, il y a \(3 \times 4 = 12\) couples (protocole, port) à décrire dans une règle de pare-feu.

On écrit \(A^2\) pour \(A \times A\), et \(A^n\) pour les \(n\)-uplets.

## II. Relations binaires

Une **relation binaire** \(\mathcal{R}\) de \(A\) vers \(B\) est une partie de \(A \times B\). On écrit \(x\,\mathcal{R}\,y\) pour \((x, y) \in \mathcal{R}\). Quand \(A = B = E\), on parle de relation **sur \(E\)**.

**Exemple.** Sur \(E = \{1, 2, 3, 4, 6, 12\}\), la relation « \(x\) divise \(y\) » contient les couples \{(1, 1), (1, 2), (1, 3), (1, 4), (1, 6), (1, 12), (2, 2), (2, 4), (2, 6), (2, 12), (3, 3), (3, 6), (3, 12), (4, 4), (4, 12), (6, 6), (6, 12), (12, 12)\}.

Une relation sur un ensemble fini se représente par une **table** (1 si \(x\,\mathcal{R}\,y\)) :

| | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| **1** | 1 | 1 | 1 | 1 |
| **2** | 0 | 1 | 0 | 1 |
| **3** | 0 | 0 | 1 | 0 |
| **4** | 0 | 0 | 0 | 1 |

(« \(x\) divise \(y\) » sur \(\{1,2,3,4\}\) ; la ligne est \(x\), la colonne \(y\).)

## III. Propriétés d'une relation sur \(E\)

| Propriété | En mots | Avec quantificateurs |
|---|---|---|
| **Réflexive** | Tout élément est en relation avec lui-même | \(\forall x \in E,\ x\,\mathcal{R}\,x\) |
| **Symétrique** | Si \(x\) est lié à \(y\), alors \(y\) est lié à \(x\) | \(\forall x, y,\ x\,\mathcal{R}\,y \Rightarrow y\,\mathcal{R}\,x\) |
| **Antisymétrique** | Si \(x\) est lié à \(y\) et \(y\) à \(x\), c'est le même élément | \(\forall x, y,\ (x\,\mathcal{R}\,y \wedge y\,\mathcal{R}\,x) \Rightarrow x = y\) |
| **Transitive** | Si \(x\) est lié à \(y\) et \(y\) à \(z\), alors \(x\) est lié à \(z\) | \(\forall x, y, z,\ (x\,\mathcal{R}\,y \wedge y\,\mathcal{R}\,z) \Rightarrow x\,\mathcal{R}\,z\) |

> [!WARNING]
> **Symétrique et antisymétrique ne sont pas contraires.** La relation d'égalité est les deux à la fois ; une relation peut n'être ni l'une ni l'autre. Pour **réfuter** une propriété, il suffit d'un contre-exemple.

Sur \(E = \{1, 2, 3, 4, 5, 6\}\) (résultats calculés couple par couple) :

| Relation | Réflexive | Symétrique | Antisymétrique | Transitive | Nature |
|---|---|---|---|---|---|
| \(x \le y\) | oui | non | oui | oui | ordre |
| \(x < y\) | non | non | oui | oui | — |
| \(x\) divise \(y\) | oui | non | oui | oui | ordre |
| \(x \equiv y \pmod 2\) | oui | oui | non | oui | équivalence |
| \(x + y = 7\) | non | oui | non | non | — |
| \(x \neq y\) | non | oui | non | non | — |

Remarque : \(x < y\) est antisymétrique « à vide » (aucun couple \((x, y)\) et \((y, x)\) avec \(x \neq y\) n'existe en même temps) ; \(x + y = 7\) n'est pas transitive car \(1 + 6 = 7\) et \(6 + 1 = 7\) mais \(1 + 1 \neq 7\).

## IV. Relation d'équivalence

Une relation est une **relation d'équivalence** si elle est **réflexive, symétrique et transitive**. Elle regroupe les éléments « semblables » en **classes**.

La **classe** d'un élément \(x\) est \([x] = \{y \in E \mid x\,\mathcal{R}\,y\}\). Deux propriétés fondamentales :

- deux classes sont **égales ou disjointes** ;
- toutes les classes **recouvrent** \(E\) : elles forment une **partition** de \(E\).

**Exemple.** « \(x \equiv y \pmod 2\) » sur \(\{1, \dots, 6\}\) est une équivalence (S07). Ses classes : \(\{1, 3, 5\}\) et \(\{2, 4, 6\}\) — les impairs et les pairs.

**Autre exemple.** Sur \(\{0, \dots, 8\}\), « \(x \equiv y \pmod 3\) » : \(\{0, 3, 6\}\) ; \(\{1, 4, 7\}\) ; \(\{2, 5, 8\}\). Trois classes de 3 éléments chacune.

> [!NOTE]
> **En réseau.** « Deux machines sont dans le même sous-réseau » (même adresse ET masque, annexe de S10) est une relation d'équivalence : ses classes sont les sous-réseaux.

## V. Relation d'ordre

Une relation est une **relation d'ordre** si elle est **réflexive, antisymétrique et transitive**. L'ordre est **total** si deux éléments quelconques sont toujours comparables, **partiel** sinon.

- \(\le\) sur les entiers : ordre **total**.
- « divise » sur \(\{1, 2, 3, 4, 6, 12\}\) : ordre **partiel** (2 ne divise pas 3 et 3 ne divise pas 2).

On représente un ordre fini par son **diagramme de Hasse** : on ne trace que les liens de « couverture » (sans les liens déduits par transitivité ni les boucles), le plus petit en bas.

<figure class="graphe diagramme">
<svg viewBox="0.00 0.00 169.60 343.60" style="max-width:227px" role="img" aria-label="Schéma" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g class="graph" transform="scale(1 1) rotate(0) translate(10.8 332.8)">
<g class="node n&#45;rect">
<path fill="none" stroke="black" stroke-width="1.8" d="M89,-37C89,-37 59,-37 59,-37 53,-37 47,-31 47,-25 47,-25 47,-12 47,-12 47,-6 53,0 59,0 59,0 89,0 89,0 95,0 101,-6 101,-12 101,-12 101,-25 101,-25 101,-31 95,-37 89,-37"/>
<text text-anchor="start" x="69" y="-15" font-family="Helvetica,sans-Serif" font-size="15.00">1</text>
</g>
<g class="node n&#45;rect">
<path fill="none" stroke="black" stroke-width="1.8" d="M42,-132C42,-132 12,-132 12,-132 6,-132 0,-126 0,-120 0,-120 0,-107 0,-107 0,-101 6,-95 12,-95 12,-95 42,-95 42,-95 48,-95 54,-101 54,-107 54,-107 54,-120 54,-120 54,-126 48,-132 42,-132"/>
<text text-anchor="start" x="22" y="-110" font-family="Helvetica,sans-Serif" font-size="15.00">2</text>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M64.94,-37.43C57.87,-51.42 47.96,-71.03 40.04,-86.7"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="37.12,-85.49 35.87,-94.94 42.75,-88.33 37.12,-85.49"/>
</g>
<g class="node n&#45;rect">
<path fill="none" stroke="black" stroke-width="1.8" d="M136,-132C136,-132 106,-132 106,-132 100,-132 94,-126 94,-120 94,-120 94,-107 94,-107 94,-101 100,-95 106,-95 106,-95 136,-95 136,-95 142,-95 148,-101 148,-107 148,-107 148,-120 148,-120 148,-126 142,-132 136,-132"/>
<text text-anchor="start" x="116" y="-110" font-family="Helvetica,sans-Serif" font-size="15.00">3</text>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M83.06,-37.43C90.13,-51.42 100.04,-71.03 107.96,-86.7"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="105.25,-88.33 112.13,-94.94 110.88,-85.49 105.25,-88.33"/>
</g>
<g class="node n&#45;rect">
<path fill="none" stroke="black" stroke-width="1.8" d="M42,-227C42,-227 12,-227 12,-227 6,-227 0,-221 0,-215 0,-215 0,-202 0,-202 0,-196 6,-190 12,-190 12,-190 42,-190 42,-190 48,-190 54,-196 54,-202 54,-202 54,-215 54,-215 54,-221 48,-227 42,-227"/>
<text text-anchor="start" x="22" y="-205" font-family="Helvetica,sans-Serif" font-size="15.00">4</text>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M27,-132.43C27,-146.16 27,-165.3 27,-180.82"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="23.85,-180.94 27,-189.94 30.15,-180.94 23.85,-180.94"/>
</g>
<g class="node n&#45;rect">
<path fill="none" stroke="black" stroke-width="1.8" d="M136,-227C136,-227 106,-227 106,-227 100,-227 94,-221 94,-215 94,-215 94,-202 94,-202 94,-196 100,-190 106,-190 106,-190 136,-190 136,-190 142,-190 148,-196 148,-202 148,-202 148,-215 148,-215 148,-221 142,-227 136,-227"/>
<text text-anchor="start" x="116" y="-205" font-family="Helvetica,sans-Serif" font-size="15.00">6</text>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M45.12,-132.43C59.78,-146.93 80.56,-167.49 96.66,-183.42"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="94.64,-185.85 103.25,-189.94 99.07,-181.37 94.64,-185.85"/>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M121,-132.43C121,-146.16 121,-165.3 121,-180.82"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="117.85,-180.94 121,-189.94 124.15,-180.94 117.85,-180.94"/>
</g>
<g class="node n&#45;rect">
<path fill="none" stroke="black" stroke-width="1.8" d="M91,-322C91,-322 57,-322 57,-322 51,-322 45,-316 45,-310 45,-310 45,-297 45,-297 45,-291 51,-285 57,-285 57,-285 91,-285 91,-285 97,-285 103,-291 103,-297 103,-297 103,-310 103,-310 103,-316 97,-322 91,-322"/>
<text text-anchor="start" x="64" y="-300" font-family="Helvetica,sans-Serif" font-size="15.00">12</text>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M36.06,-227.43C43.13,-241.42 53.04,-261.03 60.96,-276.7"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="58.25,-278.33 65.13,-284.94 63.88,-275.49 58.25,-278.33"/>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M111.94,-227.43C104.87,-241.42 94.96,-261.03 87.04,-276.7"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="84.12,-275.49 82.87,-284.94 89.75,-278.33 84.12,-275.49"/>
</g>
</g>
</svg>
</figure>

Les arêtes (calculées) sont : 1→2, 1→3, 2→4, 2→6, 3→6, 4→12, 6→12. Ici 1 est le **plus petit élément** et 12 le **plus grand**. En informatique : ordre des tâches d'un projet (S17), version d'un logiciel, droits hiérarchisés.

## VI. Applications

Une **application** \(f\) de \(A\) dans \(B\) associe à **chaque** élément \(x\) de \(A\) **un seul** élément \(f(x)\) de \(B\). On note \(f : A \to B\). L'élément \(f(x)\) est l'**image** de \(x\) ; \(x\) est un **antécédent** de \(f(x)\).

> [!WARNING]
> Une relation n'est une application que si **tout** élément de \(A\) a **exactement une** image. Si un élément n'a aucune image, ou en a deux, ce n'est pas une application.

### Injective, surjective, bijective

| Propriété | Définition | En clair | Test sur un tableau |
|---|---|---|---|
| **Injective** | \(f(x) = f(x') \Rightarrow x = x'\) | deux éléments distincts ont des images distinctes | aucune image n'apparaît deux fois |
| **Surjective** | tout \(y \in B\) a au moins un antécédent | tout élément de \(B\) est atteint | toutes les valeurs de \(B\) apparaissent |
| **Bijective** | injective **et** surjective | chaque \(y\) a **exactement un** antécédent | les deux tests |

**Exemple.** \(f : \{0,\dots,9\} \to \{0,\dots,4\}\), \(f(x) = x \bmod 5\) :

| \(x\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|
| \(f(x)\) | 0 | 1 | 2 | 3 | 4 | 0 | 1 | 2 | 3 | 4 |

\(f\) est surjective : tout élément de \(\{0,\dots,4\}\) est atteint, mais 0 a deux antécédents (0 et 5). C'est le principe des **collisions** d'une fonction de hachage : si l'on range 10 éléments dans 5 cases, au moins une case en reçoit deux.

> [!NOTE]
> **Cas des ensembles finis.** Si \(\lvert A \rvert = \lvert B \rvert\), alors injective \(\Leftrightarrow\) surjective \(\Leftrightarrow\) bijective. Si \(\lvert A \rvert > \lvert B \rvert\), une application ne peut pas être injective (principe des tiroirs).

**Exemples sur les nombres** (le résultat dépend des ensembles de départ et d'arrivée) :

| Application | Injective | Surjective | Bijective |
|---|---|---|---|
| \(\mathbb{R} \to \mathbb{R},\ x \mapsto 2x + 1\) | oui | oui | oui |
| \(\mathbb{Z} \to \mathbb{Z},\ n \mapsto 2n\) | oui | non (les impairs ne sont pas atteints) | non |
| \(\mathbb{R} \to \mathbb{R},\ x \mapsto x^2\) | non (\(f(2) = f(-2)\)) | non (\(-1\) n'est pas atteint) | non |
| \(\mathbb{R}_+ \to \mathbb{R}_+,\ x \mapsto x^2\) | oui | oui | oui |

### Application réciproque et composée

Si \(f : A \to B\) est **bijective**, elle a une **réciproque** \(f^{-1} : B \to A\) qui à \(y\) associe son unique antécédent. Pour \(f(x) = 2x + 1\) : \(y = 2x + 1 \iff x = \dfrac{y - 1}{2}\), donc \(f^{-1}(y) = \dfrac{y - 1}{2}\).

La **composée** de \(f : A \to B\) et \(g : B \to C\) est \(g \circ f : A \to C\), \(x \mapsto g(f(x))\) : on applique \(f\) **d'abord**. L'ordre compte. Avec \(f(x) = 2x + 1\) et \(g(x) = x^2\) : \((g \circ f)(x) = (2x + 1)^2\) et \((f \circ g)(x) = 2x^2 + 1\) ; pour \(x = 3\), \((g \circ f)(3) = 49\) et \((f \circ g)(3) = 19\).

### Image directe et image réciproque

Pour \(X \subseteq A\) et \(Y \subseteq B\) :

\[
f(X) = \{f(x) \mid x \in X\} \qquad f^{-1}(Y) = \{x \in A \mid f(x) \in Y\}
\]

Avec \(f(x) = x \bmod 5\) sur \(\{0,\dots,9\}\) : \(f(\{0,1,2,3\}) = \{0, 1, 2, 3\}\), \(f^{-1}(\{0\}) = \{0, 5\}\), \(f^{-1}(\{1,2\}) = \{1, 2, 6, 7\}\).

> [!WARNING]
> \(f^{-1}(Y)\) (image **réciproque** d'une partie) existe **toujours**, même si \(f\) n'est pas bijective ; la **fonction** réciproque \(f^{-1}\) n'existe que si \(f\) est bijective.

### Combien d'applications ?

De \(A\) (\(p\) éléments) vers \(B\) (\(n\) éléments), il y a \(n^p\) applications : chacun des \(p\) éléments a \(n\) choix. Pour \(p = 3\), \(n = 4\) : \(4^3 = 64\) (dont 24 injections).

## À retenir

- \(\lvert A \times B \rvert = \lvert A \rvert \cdot \lvert B \rvert\) ; un couple est ordonné.
- Propriétés : réflexive, symétrique, antisymétrique, transitive.
- **Équivalence** = réflexive + symétrique + transitive → **classes** qui partitionnent \(E\) ; **ordre** = réflexive + antisymétrique + transitive.
- **Application** : chaque élément de \(A\) a **une et une seule** image. Injective / surjective / bijective.
- \(g \circ f\) : on applique \(f\) puis \(g\). \(f^{-1}\) n'existe que si \(f\) est bijective.

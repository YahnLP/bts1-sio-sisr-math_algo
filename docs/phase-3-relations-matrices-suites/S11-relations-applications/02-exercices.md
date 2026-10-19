# Exercices – Relations et applications

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S11*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**, avec la méthode du cours : écris les étapes, pas seulement le résultat. Ouvre ensuite « Voir la réponse » pour te corriger. À l'épreuve, **aucune réponse sans justification** n'est complète.

## Exercice 1 – Produit cartésien

1. Écrire \(A \times B\) pour \(A = \{1, 2, 3\}\) et \(B = \{x, y\}\), puis \(B \times A\). Sont-ils égaux ?
2. Un pare-feu a 3 protocoles (TCP, UDP, ICMP) et 4 ports à considérer. Combien de couples (protocole, port) ?
3. Combien d'éléments a \(A \times B \times C\) pour \(\lvert A \rvert = 3\), \(\lvert B \rvert = 2\), \(\lvert C \rvert = 5\) ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(A \times B = \{(1, 'x'), (1, 'y'), (2, 'x'), (2, 'y'), (3, 'x'), (3, 'y')\}\) ; \(B \times A = \{('x', 1), ('x', 2), ('x', 3), ('y', 1), ('y', 2), ('y', 3)\}\). Ils ne sont **pas** égaux (le couple \((1, x)\) n'est pas le couple \((x, 1)\)), mais ils ont le même nombre d'éléments : 6.
2. \(3 \times 4 = 12\).
3. \(3 \times 2 \times 5 = 30\).

</details>

## Exercice 2 – Propriétés de relations

Sur \(E = \{1, 2, 3, 4\}\), étudier les propriétés (réflexive, symétrique, antisymétrique, transitive) de : (a) \(x \le y\) ; (b) \(x\) divise \(y\) ; (c) \(x + y\) pair ; (d) \(x \neq y\) ; (e) \(\mathcal{R} = \{(1,1), (2,2), (3,3), (1,2), (2,1)\}\) sur \(\{1, 2, 3\}\).

<details markdown="1">
<summary>Voir la réponse</summary>

| Relation | Réflexive | Symétrique | Antisymétrique | Transitive | Nature |
|---|---|---|---|---|---|
| (a) \(x \le y\) | oui | non | oui | oui | ordre |
| (b) \(x\) divise \(y\) | oui | non | oui | oui | ordre |
| (c) \(x+y\) pair | oui | oui | non | oui | équivalence |
| (d) \(x \neq y\) | non | oui | non | non | — |
| (e) \(\mathcal{R}\) | oui | oui | non | oui | équivalence |

Contre-exemples : (d) non transitive, car \(1 \neq 2\) et \(2 \neq 1\) mais \(1 = 1\) ; (e) non antisymétrique, car \((1,2)\) et \((2,1)\) sont dans \(\mathcal{R}\) avec \(1 \neq 2\).

</details>

## Exercice 3 – Classes d'équivalence

Sur \(E = \{1, \dots, 10\}\), on pose \(x \sim y\) si \(x - y\) est un multiple de 3.

1. Montrer que \(\sim\) est une relation d'équivalence.
2. Donner ses classes.

<details markdown="1">
<summary>Voir la réponse</summary>

1. Réflexive : \(x - x = 0 = 3 \times 0\). Symétrique : si \(x - y = 3k\), alors \(y - x = 3(-k)\). Transitive : si \(x - y = 3k\) et \(y - z = 3l\), alors \(x - z = 3(k + l)\).
2. \(\{1, 4, 7, 10\}\) ; \(\{2, 5, 8\}\) ; \(\{3, 6, 9\}\) — trois classes (restes 1, 2, 0 dans la division par 3), de tailles 4, 3, 3.

</details>

## Exercice 4 – Ordre et diagramme de Hasse

On considère la divisibilité sur \(E = \{1, 2, 3, 4, 6, 8, 12, 24\}\).

1. Montrer que c'est une relation d'ordre. Est-il total ?
2. Dessiner le diagramme de Hasse.
3. Quels sont le plus petit et le plus grand élément ? Trouver deux éléments non comparables.

<details markdown="1">
<summary>Voir la réponse</summary>

1. Réflexive (\(x\) divise \(x\)) ; antisymétrique (si \(x \mid y\) et \(y \mid x\) alors \(x = y\), entiers positifs) ; transitive (\(y = kx\) et \(z = ly\) donnent \(z = (kl)x\)). Pas total : 2 ne divise pas 3, et 3 ne divise pas 2.
2. Arêtes de couverture : 1→2, 1→3, 2→4, 2→6, 3→6, 4→8, 4→12, 6→12, 8→24, 12→24.

<figure class="graphe diagramme">
<svg viewBox="0.00 0.00 173.60 438.60" style="max-width:232px" role="img" aria-label="Schéma" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g class="graph" transform="scale(1 1) rotate(0) translate(10.8 427.8)">
<g class="node n&#45;rect">
<path fill="none" stroke="black" stroke-width="1.8" d="M91,-37C91,-37 61,-37 61,-37 55,-37 49,-31 49,-25 49,-25 49,-12 49,-12 49,-6 55,0 61,0 61,0 91,0 91,0 97,0 103,-6 103,-12 103,-12 103,-25 103,-25 103,-31 97,-37 91,-37"/>
<text text-anchor="start" x="71" y="-15" font-family="Helvetica,sans-Serif" font-size="15.00">1</text>
</g>
<g class="node n&#45;rect">
<path fill="none" stroke="black" stroke-width="1.8" d="M44,-132C44,-132 14,-132 14,-132 8,-132 2,-126 2,-120 2,-120 2,-107 2,-107 2,-101 8,-95 14,-95 14,-95 44,-95 44,-95 50,-95 56,-101 56,-107 56,-107 56,-120 56,-120 56,-126 50,-132 44,-132"/>
<text text-anchor="start" x="24" y="-110" font-family="Helvetica,sans-Serif" font-size="15.00">2</text>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M66.94,-37.43C59.87,-51.42 49.96,-71.03 42.04,-86.7"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="39.12,-85.49 37.87,-94.94 44.75,-88.33 39.12,-85.49"/>
</g>
<g class="node n&#45;rect">
<path fill="none" stroke="black" stroke-width="1.8" d="M138,-132C138,-132 108,-132 108,-132 102,-132 96,-126 96,-120 96,-120 96,-107 96,-107 96,-101 102,-95 108,-95 108,-95 138,-95 138,-95 144,-95 150,-101 150,-107 150,-107 150,-120 150,-120 150,-126 144,-132 138,-132"/>
<text text-anchor="start" x="118" y="-110" font-family="Helvetica,sans-Serif" font-size="15.00">3</text>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M85.06,-37.43C92.13,-51.42 102.04,-71.03 109.96,-86.7"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="107.25,-88.33 114.13,-94.94 112.88,-85.49 107.25,-88.33"/>
</g>
<g class="node n&#45;rect">
<path fill="none" stroke="black" stroke-width="1.8" d="M44,-227C44,-227 14,-227 14,-227 8,-227 2,-221 2,-215 2,-215 2,-202 2,-202 2,-196 8,-190 14,-190 14,-190 44,-190 44,-190 50,-190 56,-196 56,-202 56,-202 56,-215 56,-215 56,-221 50,-227 44,-227"/>
<text text-anchor="start" x="24" y="-205" font-family="Helvetica,sans-Serif" font-size="15.00">4</text>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M29,-132.43C29,-146.16 29,-165.3 29,-180.82"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="25.85,-180.94 29,-189.94 32.15,-180.94 25.85,-180.94"/>
</g>
<g class="node n&#45;rect">
<path fill="none" stroke="black" stroke-width="1.8" d="M138,-227C138,-227 108,-227 108,-227 102,-227 96,-221 96,-215 96,-215 96,-202 96,-202 96,-196 102,-190 108,-190 108,-190 138,-190 138,-190 144,-190 150,-196 150,-202 150,-202 150,-215 150,-215 150,-221 144,-227 138,-227"/>
<text text-anchor="start" x="118" y="-205" font-family="Helvetica,sans-Serif" font-size="15.00">6</text>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M47.12,-132.43C61.78,-146.93 82.56,-167.49 98.66,-183.42"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="96.64,-185.85 105.25,-189.94 101.07,-181.37 96.64,-185.85"/>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M123,-132.43C123,-146.16 123,-165.3 123,-180.82"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="119.85,-180.94 123,-189.94 126.15,-180.94 119.85,-180.94"/>
</g>
<g class="node n&#45;rect">
<path fill="none" stroke="black" stroke-width="1.8" d="M42,-322C42,-322 12,-322 12,-322 6,-322 0,-316 0,-310 0,-310 0,-297 0,-297 0,-291 6,-285 12,-285 12,-285 42,-285 42,-285 48,-285 54,-291 54,-297 54,-297 54,-310 54,-310 54,-316 48,-322 42,-322"/>
<text text-anchor="start" x="22" y="-300" font-family="Helvetica,sans-Serif" font-size="15.00">8</text>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M28.61,-227.43C28.32,-241.16 27.91,-260.3 27.57,-275.82"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="24.42,-275.87 27.38,-284.94 30.72,-276.01 24.42,-275.87"/>
</g>
<g class="node n&#45;rect">
<path fill="none" stroke="black" stroke-width="1.8" d="M140,-322C140,-322 106,-322 106,-322 100,-322 94,-316 94,-310 94,-310 94,-297 94,-297 94,-291 100,-285 106,-285 106,-285 140,-285 140,-285 146,-285 152,-291 152,-297 152,-297 152,-310 152,-310 152,-316 146,-322 140,-322"/>
<text text-anchor="start" x="113" y="-300" font-family="Helvetica,sans-Serif" font-size="15.00">12</text>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M47.12,-227.43C61.78,-241.93 82.56,-262.49 98.66,-278.42"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="96.64,-280.85 105.25,-284.94 101.07,-276.37 96.64,-280.85"/>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M123,-227.43C123,-241.16 123,-260.3 123,-275.82"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="119.85,-275.94 123,-284.94 126.15,-275.94 119.85,-275.94"/>
</g>
<g class="node n&#45;rect">
<path fill="none" stroke="black" stroke-width="1.8" d="M92,-417C92,-417 58,-417 58,-417 52,-417 46,-411 46,-405 46,-405 46,-392 46,-392 46,-386 52,-380 58,-380 58,-380 92,-380 92,-380 98,-380 104,-386 104,-392 104,-392 104,-405 104,-405 104,-411 98,-417 92,-417"/>
<text text-anchor="start" x="65" y="-395" font-family="Helvetica,sans-Serif" font-size="15.00">24</text>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M36.25,-322.43C43.47,-336.42 53.59,-356.03 61.68,-371.7"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="59.01,-373.39 65.94,-379.94 64.61,-370.5 59.01,-373.39"/>
</g>
<g class="edge">
<path fill="none" stroke="black" stroke-width="1.8" d="M113.75,-322.43C106.53,-336.42 96.41,-356.03 88.32,-371.7"/>
<polygon fill="black" stroke="black" stroke-width="1.8" points="85.39,-370.5 84.06,-379.94 90.99,-373.39 85.39,-370.5"/>
</g>
</g>
</svg>
</figure>

3. Plus petit : 1 ; plus grand : 24. Non comparables : 2 et 3, ou 8 et 12.

</details>

## Exercice 5 – Application ou non ?

Les relations suivantes vont de \(A = \{1, 2, 3\}\) vers \(B = \{a, b, c\}\). Lesquelles sont des applications ?

- \(\mathcal{R}_1 = \{(1,a), (2,b), (3,c)\}\)
- \(\mathcal{R}_2 = \{(1,a), (1,b), (2,c), (3,c)\}\)
- \(\mathcal{R}_3 = \{(1,a), (3,b)\}\)

<details markdown="1">
<summary>Voir la réponse</summary>

- \(\mathcal{R}_1\) : application (chaque élément de \(A\) a exactement une image).
- \(\mathcal{R}_2\) : **pas** une application : 1 a deux images (\(a\) et \(b\)).
- \(\mathcal{R}_3\) : **pas** une application : 2 n'a aucune image.

</details>

## Exercice 6 – Injective, surjective, bijective

Pour chaque application donnée par sa table, dire si elle est injective, surjective, bijective.

(a) \(f : \{1,2,3,4\} \to \{a,b,c\}\) : | \(x\) | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| \(f(x)\) | a | b | a | c |

(b) \(g : \{1,2,3,4\} \to \{a,b,c,d\}\) : | \(x\) | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| \(f(x)\) | a | b | c | d |

(c) \(h : \{1,2,3\} \to \{a,b,c,d\}\) : | \(x\) | 1 | 2 | 3 |
|---|---|---|---|
| \(f(x)\) | a | b | c |

<details markdown="1">
<summary>Voir la réponse</summary>

(a) surjective : \(a\) a deux antécédents (1 et 3), donc pas injective ; tous les éléments de \(B\) sont atteints.
(b) bijective : les quatre images sont distinctes et couvrent \(B\).
(c) injective : images distinctes, mais \(d\) n'est pas atteint.

</details>

## Exercice 7 – Applications numériques

Dire si les applications sont injectives, surjectives, bijectives ; si oui, donner la réciproque.

(a) \(f : \mathbb{R} \to \mathbb{R},\ x \mapsto 3x - 2\) ; (b) \(g : \mathbb{Z} \to \mathbb{Z},\ n \mapsto n + 4\) ; (c) \(h : \mathbb{Z} \to \mathbb{Z},\ n \mapsto 2n\) ; (d) \(k : \mathbb{R} \to \mathbb{R},\ x \mapsto x^2\).

<details markdown="1">
<summary>Voir la réponse</summary>

(a) Bijective : \(y = 3x - 2 \iff x = \dfrac{y + 2}{3}\), donc \(f^{-1}(y) = \dfrac{y + 2}{3}\) (tout réel \(y\) a un unique antécédent).
(b) Bijective : \(g^{-1}(m) = m - 4\).
(c) Injective (si \(2n = 2n'\), alors \(n = n'\)) mais pas surjective (3 n'a pas d'antécédent dans \(\mathbb{Z}\)).
(d) Ni injective (\(k(2) = k(-2) = 4\)), ni surjective (\(-1\) n'a pas d'antécédent). Restreinte à \(\mathbb{R}_+ \to \mathbb{R}_+\), elle devient bijective, de réciproque \(\sqrt{\ }\).

</details>

## Exercice 8 – Composition

Soient \(f(x) = 2x + 1\) et \(g(x) = x^2\) sur \(\mathbb{R}\). Calculer \(g \circ f\) et \(f \circ g\), puis leurs valeurs en \(x = 3\). Ces applications sont-elles égales ?

<details markdown="1">
<summary>Voir la réponse</summary>

\((g \circ f)(x) = g(2x + 1) = (2x + 1)^2 = 4x^2 + 4x + 1\) ; \((f \circ g)(x) = f(x^2) = 2x^2 + 1\).
En \(x = 3\) : 49 et 19. Elles ne sont pas égales : la composition **n'est pas commutative**.

</details>

## Exercice 9 – Images directes et réciproques

Soit \(f : \{0, \dots, 9\} \to \{0, \dots, 4\}\), \(f(x) = x \bmod 5\). Calculer \(f(\{2, 7, 9\})\), \(f^{-1}(\{3\})\), \(f^{-1}(\{0, 4\})\), \(f^{-1}(\{5\})\).

<details markdown="1">
<summary>Voir la réponse</summary>

\(f(\{2,7,9\}) = \{2, 4\}\) ; \(f^{-1}(\{3\}) = \{3, 8\}\) ; \(f^{-1}(\{0,4\}) = \{0, 4, 5, 9\}\) ; \(f^{-1}(\{5\}) = \varnothing\) (5 n'est pas dans l'ensemble d'arrivée).

</details>

## Exercice 10 – Collisions

Une fonction de hachage associe à un identifiant (parmi 20) un numéro de case entre 0 et 7.

1. Peut-elle être injective ? Pourquoi ?
2. Montrer qu'une case au moins reçoit trois identifiants.
3. Combien y a-t-il d'applications possibles de 3 éléments vers 4 éléments ? Parmi elles, combien d'injections ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. Non : 20 identifiants pour 8 cases (principe des tiroirs).
2. Si chaque case en recevait au plus 2, on aurait au plus \(8 \times 2 = 16 < 20\) identifiants : contradiction. Au moins \(\lceil 20 / 8 \rceil = 3\) identifiants sont dans la même case.
3. \(4^3 = 64\) applications ; injections : \(4 \times 3 \times 2 = 24\) (le premier élément a 4 choix, le suivant 3, le dernier 2).

</details>


## Je sais faire

Coche honnêtement ; ce que tu ne coches pas se reprend avant la séance suivante.

- [ ] Calculer le cardinal d'un produit cartésien ;
- [ ] Tester les propriétés d'une relation finie ;
- [ ] Trouver les classes d'une relation d'équivalence ;
- [ ] Décider si une application est injective, surjective, bijective ;
- [ ] Composer deux applications.

**Ce que je dois reprendre :** ______________________

**Ma question à poser à l'enseignant :** ______________________

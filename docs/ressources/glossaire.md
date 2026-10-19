# Glossaire

Tous les mots techniques du cours, expliqués simplement. Dans les pages du site, **passe la souris sur un sigle** (PGCD, CIDR, MPM…) : sa définition s'affiche.

La colonne « Vu en » indique la séance où le mot apparaît pour la première fois dans le cours.

| Terme | Sigle | Anglais | Définition | Vu en |
|---|---|---|---|---|
| **Absorption** |  | *absorption* | \(a + ab = a\) et \(a(a + b) = a\). | S10 |
| **Accumulateur** |  | *accumulator* | Variable qui cumule un résultat à chaque tour. | S04 |
| **Additionneur complet** |  | *full adder* | Circuit qui additionne deux bits et une retenue entrante. | S10 |
| **Adresse de diffusion** |  | *broadcast address* | Adresse dont tous les bits de machine valent 1 ; elle atteint toutes les machines du réseau. | S10 |
| **Adresse IPv4** | IPv4 |  | Adresse de 32 bits écrite en quatre octets (par exemple 192.168.10.77). | S10 |
| **Adresse MAC** | MAC | *media access control* | Adresse matérielle d'une carte réseau (48 bits). | S11 |
| **Affectation** |  | *assignment* | Instruction qui donne une valeur à une variable. | S03 |
| **Algèbre de Boole** |  | *Boolean algebra* | Calcul sur les valeurs 0 et 1 avec les opérations ET, OU, NON. | S10 |
| **Algorithme** |  | *algorithm* | Suite finie d'instructions qui résout un problème. | S03 |
| **Algorithme d'Euclide** |  | *Euclidean algorithm* | Divisions successives dont le dernier reste non nul est le PGCD. | S05 |
| **Algorithme de Dijkstra** |  | *Dijkstra's algorithm* | Méthode qui fixe à chaque étape le sommet de plus petite valeur pour trouver les chemins minimaux. | S17 |
| **Année bissextile** |  | *leap year* | Année de 366 jours : divisible par 4 et non par 100, ou divisible par 400. | S03 |
| **Antisymétrique** |  | *antisymmetric* | Si \(x\) est lié à \(y\) et \(y\) à \(x\), alors \(x = y\). | S11 |
| **Application** |  | *function, map* | Association qui donne à chaque élément de départ une et une seule image. | S11 |
| **Arc** |  | *arc* | Flèche d'un sommet vers un autre. | S16 |
| **Arrondi** |  | *rounding* | Remplacement d'un nombre par une valeur voisine à une précision donnée. | S02 |
| **Base** |  | *base, radix* | Nombre de chiffres différents d'un système de numération (2, 10, 16…). | S01 |
| **Bijective** |  | *bijective* | À la fois injective et surjective. | S11 |
| **Binaire** |  | *binary* | Numération en base 2, n'utilisant que les chiffres 0 et 1. | S01 |
| **Bit** |  | *bit* | Chiffre binaire : 0 ou 1. | S01 |
| **Bit de parité** |  | *parity bit* | Bit ajouté à un mot pour que son nombre total de 1 soit pair (parité paire) ; il permet de détecter une erreur. | S15 |
| **Boucle** |  | *loop* | Structure qui répète un bloc d'instructions. | S04 |
| **Cardinal** |  | *cardinality* | Nombre d'éléments d'un ensemble fini. | S09 |
| **Cas limite** |  | *edge case* | Valeur située à la frontière ou situation particulière (liste vide, un seul élément) qui révèle souvent une erreur. | S15 |
| **Chaîne de caractères** |  | *string* | Suite de caractères, non modifiable en Python. | S12 |
| **Chemin** |  | *path* | Suite de sommets reliés par des arcs successifs. | S16 |
| **Chemin critique** |  | *critical path* | Chemin de tâches critiques ; sa longueur est la durée minimale du projet. | S17 |
| **Chemin hamiltonien** |  | *Hamiltonian path* | Chemin qui passe une seule fois par chaque sommet. | S16 |
| **Chiffrement affine** |  | *affine cipher* | Chiffrement qui remplace chaque lettre de rang \(x\) par \(ax + b \bmod 26\). | S07 |
| **Circuit** |  | *cycle* | Chemin fermé de longueur au moins 1. | S16 |
| **Classe d'équivalence** |  | *equivalence class* | Ensemble des éléments liés à un élément donné. | S11 |
| **Clé de contrôle** |  | *check digit* | Chiffre calculé à partir des autres pour détecter une erreur de saisie. | S07 |
| **Code de Gray** |  | *Gray code* | Suite de codes dont deux voisins ne diffèrent que d'un bit. | S10 |
| **Complémentaire** |  | *complement* | Éléments de l'ensemble de référence qui ne sont pas dans la partie. | S09 |
| **Compteur** |  | *counter* | Variable qui compte les tours d'une boucle. | S04 |
| **Condition** |  | *condition* | Expression qui vaut vrai ou faux et oriente l'exécution. | S03 |
| **Congruence** |  | *congruence* | Deux entiers sont congrus modulo \(n\) s'ils ont le même reste dans la division par \(n\). | S07 |
| **Connecteur logique** |  | *logical connective* | Opération qui combine des propositions : non, et, ou, implication, équivalence. | S08 |
| **Contraposée** |  | *contrapositive* | \(\neg q \Rightarrow \neg p\), équivalente à \(p \Rightarrow q\). | S08 |
| **Contre-exemple** |  | *counterexample* | Cas particulier qui rend fausse une affirmation « pour tout ». | S09 |
| **Couple** |  | *ordered pair* | Paire ordonnée \((a, b)\) : l'ordre compte. | S11 |
| **Crible d'Ératosthène** |  | *sieve of Eratosthenes* | Méthode qui élimine les multiples des premiers pour trouver tous les premiers jusqu'à \(n\). | S06 |
| **Date au plus tard** |  | *latest start* | Date la plus éloignée à laquelle une tâche peut commencer sans retarder le projet. | S17 |
| **Date au plus tôt** |  | *earliest start* | Date la plus proche à laquelle une tâche peut commencer. | S17 |
| **Débogage** |  | *debugging* | Recherche et correction des erreurs d'un programme. | S18 |
| **Décomposition en facteurs premiers** |  | *prime factorization* | Écriture d'un entier comme produit de nombres premiers ; elle est unique à l'ordre près. | S06 |
| **Demi-additionneur** |  | *half adder* | Circuit qui additionne deux bits : somme \(a \oplus b\), retenue \(a \cdot b\). | S10 |
| **Dépassement de capacité** |  | *overflow* | Résultat qui ne tient pas dans le nombre de bits disponibles. | S02 |
| **Diagramme de Hasse** |  | *Hasse diagram* | Représentation d'un ordre fini où l'on ne trace que les liens de couverture. | S11 |
| **Dictionnaire** |  | *dictionary* | Association clé → valeur. | S12 |
| **Disque à état solide** | SSD | *solid-state drive* | Support de stockage sans pièce mobile, fait de mémoire flash. | S01 |
| **Diviseur** |  | *divisor* | Entier qui divise un autre sans reste. | S05 |
| **Division euclidienne** |  | *Euclidean division* | Écriture \(a = bq + r\) avec \(0 \le r < b\) ; \(q\) est le quotient, \(r\) le reste. | S05 |
| **Effet de bord** |  | *side effect* | Modification d'une donnée extérieure à la fonction (par exemple une liste passée en paramètre). | S18 |
| **Ensemble** |  | *set* | Collection d'éléments distincts, sans ordre. | S09 |
| **Ensemble des parties** |  | *power set* | Ensemble de toutes les parties d'un ensemble ; il a \(2^n\) éléments pour \(n\) éléments. | S09 |
| **Épreuve E3** |  |  | Épreuve écrite de mathématiques pour l'informatique, de 2 h, coefficient 3. | S19 |
| **Équivalence logique** |  | *logical equivalence* | Deux expressions qui ont la même table de vérité. | S08 |
| **Erreur d'arrondi** |  | *rounding error* | Écart entre un nombre et sa valeur arrondie. | S02 |
| **Fermeture transitive** |  | *transitive closure* | Graphe contenant un arc \(i \to j\) chaque fois qu'il existe un chemin de \(i\) à \(j\). | S16 |
| **Fonction** |  | *function* | Bloc de code nommé qui reçoit des paramètres et retourne un résultat. | S12 |
| **Fonction de hachage** |  | *hash function* | Application qui associe à une donnée un petit nombre ; des collisions sont inévitables. | S11 |
| **Fraction** |  | *fraction* | Nombre rationnel exact (`Fraction` en Python), qui évite les arrondis. | S14 |
| **Graphe orienté** |  | *directed graph* | Ensemble de sommets reliés par des arcs. | S16 |
| **Graphe valué** |  | *weighted graph* | Graphe dont chaque arc porte un nombre. | S17 |
| **Hexadécimal** |  | *hexadecimal* | Numération en base 16 : chiffres 0 à 9 puis A à F (A = 10, … F = 15). | S01 |
| **Image réciproque** |  | *preimage* | Ensemble des éléments de départ dont l'image est dans une partie donnée. | S11 |
| **Implication** |  | *implication* | \(p \Rightarrow q\), fausse seulement si \(p\) est vraie et \(q\) fausse. | S08 |
| **Indice** |  | *index* | Numéro d'un élément dans un tableau ou une chaîne (à partir de 0). | S12 |
| **Injective** |  | *injective* | Deux éléments distincts ont des images distinctes. | S11 |
| **Invariant** |  | *invariant* | Propriété vraie avant, pendant et après chaque tour de boucle. | S04 |
| **Inverse modulaire** |  | *modular inverse* | Entier \(b\) tel que \(ab \equiv 1 \pmod n\) ; il existe si PGCD\((a, n) = 1\). | S07 |
| **Itération** |  | *iteration* | Un passage dans une boucle. | S04 |
| **Jeu de tests** |  | *test suite* | Ensemble de cas, avec le résultat attendu, qui permet de contrôler une fonction. | S18 |
| **Kibioctet / Mébioctet** |  | *kibibyte / mebibyte* | 1 024 octets (\(2^{10}\)) / 1 048 576 octets (\(2^{20}\)). | S02 |
| **Lois de De Morgan** |  | *De Morgan's laws* | \(\neg(p \wedge q) \equiv \neg p \vee \neg q\) et \(\neg(p \vee q) \equiv \neg p \wedge \neg q\). | S08 |
| **Marge certaine** |  | *safe float* | Retard possible même si tous les prédécesseurs finissent au plus tard. | S17 |
| **Marge libre** |  | *free float* | Retard maximal d'une tâche sans retarder le début au plus tôt des suivantes. | S17 |
| **Marge totale** |  | *total float* | Retard maximal d'une tâche sans retarder le projet. | S17 |
| **Masque** |  | *mask* | Nombre qui sert à garder ou forcer certains bits d'un autre nombre. | S03 |
| **Masque de longueur variable** | VLSM | *variable length subnet mask* | Découpage d'un réseau en sous-réseaux de tailles différentes. | S10 |
| **Masque de sous-réseau** |  | *subnet mask* | Suite de bits à 1 puis à 0 qui sépare la partie réseau et la partie machine d'une adresse. | S10 |
| **Matrice** |  | *matrix* | Tableau de nombres à \(m\) lignes et \(n\) colonnes. | S13 |
| **Matrice carrée** |  | *square matrix* | Matrice qui a autant de lignes que de colonnes. | S13 |
| **Matrice d'adjacence** |  | *adjacency matrix* | Matrice dont le coefficient \(m_{ij}\) vaut 1 s'il existe un arc de \(i\) vers \(j\). | S16 |
| **Matrice identité** |  | *identity matrix* | Matrice carrée avec des 1 sur la diagonale et des 0 ailleurs ; élément neutre du produit. | S13 |
| **Matrice inversible** |  | *invertible matrix* | Matrice carrée \(A\) pour laquelle il existe \(A^{-1}\) avec \(AA^{-1} = A^{-1}A = I\). | S14 |
| **Mémoire vive** | RAM | *random access memory* | Mémoire de travail d'un ordinateur, rapide et volatile. | S01 |
| **Méthode des lignes** |  | *Gauss-Jordan elimination* | Opérations sur les lignes de \([A \mid I]\) pour obtenir \([I \mid A^{-1}]\). | S14 |
| **Méthode des potentiels Métra** | MPM | *precedence diagramming* | Méthode d'ordonnancement où les tâches sont les sommets du graphe. | S17 |
| **Modulo** |  | *modulo* | Reste de la division euclidienne ; opération `%` en Python. | S07 |
| **Multiple** |  | *multiple* | Nombre obtenu en multipliant un entier par un autre entier. | S05 |
| **Niveau** |  | *level* | Rang d'un sommet dans un graphe sans circuit : on retire les sommets sans prédécesseur étape par étape. | S16 |
| **Nombre composé** |  | *composite number* | Entier supérieur ou égal à 2 qui n'est pas premier. | S06 |
| **Nombre dyadique** |  | *dyadic rational* | Fraction dont le dénominateur est une puissance de 2 : seuls ces nombres ont une écriture binaire finie. | S02 |
| **Nombre flottant** |  | *floating-point number* | Représentation approchée d'un réel en machine. | S18 |
| **Nombre premier** |  | *prime number* | Entier supérieur ou égal à 2 divisible seulement par 1 et par lui-même. | S06 |
| **Notation CIDR** | CIDR | *classless inter-domain routing* | Écriture `adresse/n` où \(n\) est le nombre de bits à 1 du masque. | S10 |
| **Numéro d'inscription au répertoire** | NIR |  | Numéro de sécurité sociale ; sa clé est \(97 - (n \bmod 97)\). | S07 |
| **Numéro de compte bancaire international** | IBAN | *international bank account number* | Identifiant de compte, validé par un calcul modulo 97. | S07 |
| **Numéro international normalisé du livre** | ISBN | *international standard book number* | Identifiant de 13 chiffres d'un livre, dont le dernier est une clé de contrôle. | S07 |
| **Octet** |  | *byte* | Groupe de 8 bits ; il représente un entier de 0 à 255. | S01 |
| **Opérateur bit à bit** |  | *bitwise operator* | Opération appliquée à chaque bit de deux nombres (ET, OU, OU exclusif). | S03 |
| **Ou exclusif** |  | *exclusive or, XOR* | Vrai quand un seul des deux opérandes est vrai. | S08 |
| **Paramètre** |  | *parameter* | Variable d'entrée d'une fonction. | S12 |
| **Partie (sous-ensemble)** |  | *subset* | Ensemble dont tous les éléments appartiennent à un autre ensemble. | S09 |
| **Partie entière** |  | *integer part* | Plus grand entier inférieur ou égal à un nombre. | S02 |
| **Passerelle** |  | *gateway* | Routeur par lequel passent les paquets destinés à un autre réseau. | S10 |
| **Pivot** |  | *pivot* | Coefficient qu'on ramène à 1 pour éliminer les autres de sa colonne. | S14 |
| **Plus grand commun diviseur** | PGCD | *greatest common divisor, GCD* | Plus grand entier qui divise deux entiers. | S05 |
| **Plus petit commun multiple** | PPCM | *least common multiple, LCM* | Plus petit entier strictement positif multiple de deux entiers. | S05 |
| **Poids fort / poids faible** |  | *most / least significant bit* | Le bit de gauche (poids le plus grand) / celui de droite (rang 0). | S01 |
| **Porte NON-ET** | NAND | *NAND gate* | Fonction \(\overline{a \cdot b}\) ; à elle seule, elle permet de réaliser toutes les autres. | S10 |
| **Porte NON-OU** | NOR | *NOR gate* | Fonction \(\overline{a + b}\) ; elle est aussi universelle. | S10 |
| **Prédicat** |  | *predicate* | Énoncé dont la valeur de vérité dépend d'une ou plusieurs variables. | S09 |
| **Premiers entre eux** |  | *coprime* | Deux entiers dont le PGCD vaut 1. | S05 |
| **Principe des tiroirs** |  | *pigeonhole principle* | Si l'on range plus d'objets que de tiroirs, un tiroir en contient au moins deux. | S11 |
| **Produit cartésien** |  | *Cartesian product* | Ensemble des couples \((a, b)\) avec \(a\) dans \(A\) et \(b\) dans \(B\). | S11 |
| **Produit matriciel** |  | *matrix product* | Produit de \(A\) (\(m \times n\)) par \(B\) (\(n \times p\)), de taille \(m \times p\). | S13 |
| **Proposition** |  | *proposition* | Énoncé qui est vrai ou faux sans ambiguïté. | S08 |
| **Protocole de contrôle de transmission** | TCP | *transmission control protocol* | Protocole de transport fiable, avec connexion. | S03 |
| **Protocole de datagrammes utilisateur** | UDP | *user datagram protocol* | Protocole de transport sans connexion. | S03 |
| **Protocole de messages de contrôle** | ICMP | *internet control message protocol* | Protocole des messages d'erreur et de test (ping). | S03 |
| **Puissance d'une matrice** |  | *matrix power* | Produit répété d'une matrice carrée par elle-même. | S13 |
| **Quantificateur existentiel** |  | *existential quantifier* | \(\exists\) : « il existe au moins un ». | S09 |
| **Quantificateur universel** |  | *universal quantifier* | \(\forall\) : « pour tout ». | S09 |
| **Rang** |  | *position* | Position d'un chiffre dans un nombre, comptée à partir de 0 à droite. | S01 |
| **Recherche dichotomique** |  | *binary search* | Recherche dans un tableau trié qui élimine la moitié des éléments à chaque étape. | S12 |
| **Réflexive** |  | *reflexive* | Tout élément est en relation avec lui-même. | S11 |
| **Relation binaire** |  | *binary relation* | Partie d'un produit cartésien \(A \times B\). | S11 |
| **Relation d'équivalence** |  | *equivalence relation* | Relation réflexive, symétrique et transitive ; elle partitionne l'ensemble en classes. | S11 |
| **Relation d'ordre** |  | *order relation* | Relation réflexive, antisymétrique et transitive. | S11 |
| **Retenue** |  | *carry* | Chiffre reporté au rang suivant lors d'une addition. | S02 |
| **Somme de contrôle** |  | *checksum* | Valeur calculée à partir de tous les octets d'un message et transmise avec lui pour détecter une altération. | S15 |
| **Somme de produits** |  | *sum of products* | Expression écrite comme un OU de ET (forme issue d'une table de vérité). | S10 |
| **Sommet** |  | *vertex* | Point d'un graphe. | S16 |
| **Successeur / prédécesseur** |  | *successor / predecessor* | Sommet atteint par un arc / sommet d'où part un arc. | S16 |
| **Suite de Fibonacci** |  | *Fibonacci sequence* | Suite \(F_0 = 0, F_1 = 1, F_{n} = F_{n-1} + F_{n-2}\). | S13 |
| **Surjective** |  | *surjective* | Tout élément d'arrivée a au moins un antécédent. | S11 |
| **Symétrique** |  | *symmetric* | Si \(x\) est lié à \(y\), alors \(y\) est lié à \(x\). | S11 |
| **Système de Cramer** |  | *Cramer system* | Système linéaire \(AX = B\) dont la matrice est inversible : solution unique \(X = A^{-1}B\). | S14 |
| **Système de noms de domaine** | DNS | *domain name system* | Service qui associe des noms à des adresses IP. | S12 |
| **Table de vérité** |  | *truth table* | Tableau des valeurs d'une expression pour toutes les valeurs possibles des variables. | S08 |
| **Tableau** |  | *array* | Suite d'éléments repérés par un indice. | S12 |
| **Tableau de Karnaugh** |  | *Karnaugh map* | Grille qui range une table de vérité pour simplifier une expression par regroupements. | S10 |
| **Tâche critique** |  | *critical task* | Tâche de marge totale nulle. | S17 |
| **Tautologie** |  | *tautology* | Expression toujours vraie. | S08 |
| **Terminaison** |  | *termination* | Garantie qu'un algorithme s'arrête. | S18 |
| **Trace** |  | *trace* | Tableau des valeurs des variables à chaque étape d'un algorithme. | S04 |
| **Tranche** |  | *slice* | Partie d'une chaîne ou d'une liste, `s[a:b]` (borne b exclue). | S12 |
| **Transitive** |  | *transitive* | Si \(x\) est lié à \(y\) et \(y\) à \(z\), alors \(x\) est lié à \(z\). | S11 |
| **Tri par sélection** |  | *selection sort* | Tri qui place successivement le minimum du reste du tableau. | S12 |
| **Troncature** |  | *truncation* | Suppression des chiffres au-delà d'un rang donné, sans arrondir. | S02 |
| **Type** |  | *type* | Nature d'une donnée : entier, réel, booléen, chaîne… | S03 |
| **Variable** |  | *variable* | Nom associé à une valeur en mémoire. | S03 |
| **Variable locale** |  | *local variable* | Variable qui n'existe que dans la fonction qui la crée. | S12 |
| **Variant** |  | *variant* | Entier positif qui diminue à chaque tour et garantit l'arrêt d'une boucle. | S04 |

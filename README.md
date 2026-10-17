# Mathématiques pour l'informatique – BTS SIO 1re année

Cours, exercices corrigés, TP Python et aide-mémoire des **19 séances** de mathématiques pour l'informatique (option SISR), préparant l'épreuve écrite E3.

Auteur : **Yahn LE PRETTRE** – Formateur. Licence **CC BY-NC-SA 4.0** (voir `LICENSE`).

## Contenu

| Phase | Séances | Thèmes |
|---|---|---|
| 1 – Nombres et premiers algorithmes | S01–S05 | Bases 2, 10, 16 ; calcul binaire ; algorithmique ; PGCD |
| 2 – Arithmétique, logique et booléens | S06–S10 | Premiers, congruences, propositions, ensembles, Boole, IPv4 |
| 3 – Relations, matrices et suites | S11–S15 | Relations, fonctions, matrices, systèmes, suites |
| 4 – Graphes, récursivité, E3 | S16–S19 | Graphes, Dijkstra, MPM, récursivité, épreuve blanche |

Le site est publié par GitHub Pages à chaque modification de la branche `main`.

## Travailler en local

```bash
pip install -r requirements.txt
mkdocs serve          # http://127.0.0.1:8000
mkdocs build --strict # même vérification que la publication
```

## Organisation du dépôt

| Dossier | Rôle |
|---|---|
| `docs/` | Pages du site (phases, séances, ressources) |
| `docs/<phase>/<séance>/` | Fiche, cours, exercices, TP, aide-mémoire, scripts Python et tests |
| `corriges/` | Corrigés des séances (hors site) |
| `includes/abbr.md` | Infobulles des sigles, **généré** par `scripts/gen_glossaire.py` |
| `scripts/` | Génération du glossaire et du formulaire |
| `my_theme_customizations/` | Éditeur Python intégré (Pyodide) |
| `tools/CONVENTIONS.md` | Règles d'écriture du cours |

Après avoir modifié `scripts/glossaire_data.py` ou un aide-mémoire :

```bash
python3 scripts/gen_glossaire.py
python3 scripts/gen_formulaire.py
```

# Conventions d'écriture

1. **Une séance = une fiche, un cours, des exercices, un TP Python, un aide-mémoire** (`README`, `01-cours`, `02-exercices`, `03-tp-python`, `04-aide-memoire`).
2. **Toute formule est vérifiée par le calcul** : exemple chiffré contrôlé avant publication.
3. Formules en LaTeX (`\( … \)` en ligne, `\[ … \]` en bloc) ; fraction décimale avec virgule dans le texte, point dans le code.
4. **Pseudo-code** dans un bloc `text` : `ALGORITHME`, `RÔLE`, `ENTRÉE`, `SORTIE`, `VARIABLES`, `DÉBUT` … `FIN`.
5. **Réponses repliées** : `<details markdown="1"><summary>Voir la réponse</summary> … </details>`.
6. Exercice Python = trois fichiers : squelette `nom.py`, test `nom_test.py`, solution validée hors site.
7. **Les tests s'exécutent ligne par ligne** : une instruction par ligne, pas de bloc multi-lignes.
8. Un squelette ne boucle jamais indéfiniment (boucles bornées, `# À compléter`).
9. Calculs exacts avec `Fraction` quand un flottant pourrait tromper.
10. Les pages avec `{{ IDE(...) }}` portent `render_macros: true` dans l'en-tête.
11. Schémas en Mermaid ; ils sont validés avant publication.
12. Encadrés `> [!NOTE]`, `> [!TIP]`, `> [!WARNING]`.
13. Sigles : défini dans `scripts/glossaire_data.py` (jamais à la main dans `includes/abbr.md`).
14. Pas de date dans les séances : colonne « Semaine » de 01 à 19.
15. Épreuve terminale : aucune référence au contrôle en cours de formation.

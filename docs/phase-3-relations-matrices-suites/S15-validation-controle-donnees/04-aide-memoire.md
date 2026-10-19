# Aide-mémoire – Validation et contrôle de données

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S15*

> Un mot ou un sigle inconnu ? Passe la souris dessus, ou ouvre le [glossaire](../../ressources/glossaire.md).

## Valider un format

1. Écrire **toutes** les règles ; 2. un test par règle ; 3. `return False` dès qu'une règle est violée ; 4. `return True` à la fin.

| Donnée | Règles |
|---|---|
| Octet décimal | non vide, chiffres seuls, pas de zéro initial (sauf `"0"`), valeur de 0 à 255 |
| Adresse IPv4 | `s.split(".")` : 4 morceaux, chacun est un octet valide |
| Adresse MAC | `s.split(":")` : 6 groupes de 2 chiffres hexadécimaux |
| Octet de masque | 0, 128, 192, 224, 240, 248, 252, 254, 255 |

Cas limites : chaîne vide, 0, 255, 256, caractère interdit, morceau en trop ou en moins.

## Parité

- Parité paire : bit \(= (\text{nombre de 1}) \bmod 2\) ; le mot transmis a un nombre pair de 1.
- Détecte un nombre **impair** d'erreurs ; ne localise pas ; ne voit pas deux erreurs.
- Deux dimensions : ligne fausse **et** colonne fausse = bit à corriger.

## Sommes de contrôle

```python
c = (-sum(octets)) % 256          # somme de contrôle
ok = (sum(octets) + c) % 256 == 0 # vérification
r = 0
for o in octets:
    r = r ^ o                     # OU exclusif de contrôle
```

- Deux erreurs qui se compensent ne sont pas détectées.
- Un contrôle détecte des erreurs, il ne protège pas contre une modification volontaire.

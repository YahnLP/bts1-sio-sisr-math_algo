# Aide-mémoire – Algèbre de Boole

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S10*

> Un mot ou un sigle inconnu ? Passe la souris dessus, ou ouvre le [glossaire](../../ressources/glossaire.md).

## Opérations et propriétés

| Opération | Notation | Python |
|---|---|---|
| NON | \(\overline{a}\) | `1 - a` |
| ET | \(a \cdot b\) | `a & b` |
| OU | \(a + b\) | `a | b` |
| OU exclusif | \(a \oplus b\) | `a ^ b` |

- \(1 + 1 = 1\). Priorité : NON, puis ET, puis OU.
- Absorption : \(a + a\,b = a\) ; \(a\,(a + b) = a\).
- Distributivité dans les deux sens : \(a + b\,c = (a + b)(a + c)\).
- De Morgan : \(\overline{a + b} = \overline{a}\,\overline{b}\) ; \(\overline{a\,b} = \overline{a} + \overline{b}\).
- \(a + \overline{a}\,b = a + b\).

## Karnaugh (3 variables)

- Lignes : \(a = 0, 1\) ; colonnes : \(bc = 00, 01, 11, 10\).
- Rectangles de 1, 2, 4 ou 8 cases ; tableau circulaire ; le moins de rectangles, les plus grands.
- On garde les variables qui ne changent pas dans le rectangle.

## NAND et NOR

- \(\overline{a} = \text{NAND}(a,a)\) ; \(a\,b = \text{NAND}(n, n)\) avec \(n = \text{NAND}(a,b)\) ; \(a + b = \text{NAND}(\text{NAND}(a,a), \text{NAND}(b,b))\).

## Additionneur

- Demi : \(s = a \oplus b\), \(r = a\,b\).
- Complet : \(s = a \oplus b \oplus c\), \(r = a\,b + c\,(a \oplus b)\).

## Adressage IPv4

- Réseau = adresse **ET** masque. Diffusion = réseau **OU** (NON masque).
- Machines utilisables : \(2^{32 - n} - 2\).

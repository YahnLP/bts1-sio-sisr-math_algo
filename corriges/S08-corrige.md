# Corrigé S08

## Exercices

1. Propositions : 1 (V), 4 (V), 5 (V). Non-propositions : 2 (ordre), 3 (prédicat).
2. Les colonnes de \((p \Rightarrow q) \wedge (q \Rightarrow p)\) et de \(p \Leftrightarrow q\) sont identiques (V, F, F, V).
3. Voir les tables de l'énoncé (a et b équivalentes, c non).
4. (a) tautologie ; (b) non ; (c) ​tautologie.
5. Voir l'énoncé : la contraposée est équivalente.
6. \(a \le 3 \vee b > 5\) ; port ≠ 22 et port ≠ 3389 ; âge < 18 ou ≥ 65.
7. TCP/80 : V, TCP/443 : V, TCP/22 : F, ICMP/0 : V, UDP/53 : F, UDP/443 : F.
8. Équivalentes (De Morgan).
9. Arrêt pour i = 2 (x = 15) et i = 3 (x = 7) ; l'ordre `i < n` d'abord évite `t[3]`.
10. 16 lignes ; \(2^n\) ; 16 fonctions.

## TP Python – solutions

```python
def combinaisons(n):
    """Liste des 2**n tuples de n booléens, dans l'ordre de la table de vérité."""
    liste = []
    for k in range(2 ** n):
        ligne = []
        for i in range(n):
            ligne.append(bool((k >> (n - 1 - i)) & 1))
        liste.append(tuple(ligne))
    return liste
```

```python
def combinaisons(n):
    liste = []
    for k in range(2 ** n):
        ligne = []
        for i in range(n):
            ligne.append(bool((k >> (n - 1 - i)) & 1))
        liste.append(tuple(ligne))
    return liste

def equivalentes(f, g, n):
    """True si f et g donnent le même résultat sur toutes les combinaisons de n booléens."""
    for valeurs in combinaisons(n):
        if f(*valeurs) != g(*valeurs):
            return False
    return True
```

```python
def combinaisons(n):
    liste = []
    for k in range(2 ** n):
        ligne = []
        for i in range(n):
            ligne.append(bool((k >> (n - 1 - i)) & 1))
        liste.append(tuple(ligne))
    return liste

def est_tautologie(f, n):
    """True si f vaut True pour toutes les combinaisons."""
    for valeurs in combinaisons(n):
        if not f(*valeurs):
            return False
    return True

def nombre_de_vrais(f, n):
    """Nombre de combinaisons pour lesquelles f vaut True."""
    compteur = 0
    for valeurs in combinaisons(n):
        if f(*valeurs):
            compteur = compteur + 1
    return compteur
```

```python
def autorise(protocole, port):
    """Règle : (TCP et port 80 ou 443) ou ICMP."""
    t = protocole == "TCP"
    a = port == 80
    b = port == 443
    i = protocole == "ICMP"
    return (t and (a or b)) or i
```

```python
def combinaisons(n):
    liste = []
    for k in range(2 ** n):
        ligne = []
        for i in range(n):
            ligne.append(bool((k >> (n - 1 - i)) & 1))
        liste.append(tuple(ligne))
    return liste

def afficher_table(f, n):
    """Affiche une ligne par combinaison : les valeurs puis le résultat, en V / F."""
    for valeurs in combinaisons(n):
        ligne = ""
        for v in valeurs:
            ligne = ligne + ("V" if v else "F") + " "
        ligne = ligne + "| " + ("V" if f(*valeurs) else "F")
        print(ligne)

afficher_table(lambda p, q: p and q, 2)
```

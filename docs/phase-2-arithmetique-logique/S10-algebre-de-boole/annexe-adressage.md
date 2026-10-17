# Annexe – Masques et adressage IPv4

Application directe du ET bit à bit (S03, S10) et de la numération binaire (S01).

## 1. Adresse et masque

Une adresse IPv4 est un nombre de **32 bits**, écrit en 4 octets séparés par des points. Le **masque** est une suite de bits à 1 suivie de bits à 0 : les bits à 1 désignent la partie **réseau**, les bits à 0 la partie **machine**. Le **préfixe** `/n` donne le nombre de bits à 1.

| Préfixe | Masque en binaire | Masque décimal | Machines utilisables |
|---|---|---|---|
| /8 | 11111111.00000000.00000000.00000000 | 255.0.0.0 | 16777214 |
| /16 | 11111111.11111111.00000000.00000000 | 255.255.0.0 | 65534 |
| /20 | 11111111.11111111.11110000.00000000 | 255.255.240.0 | 4094 |
| /24 | 11111111.11111111.11111111.00000000 | 255.255.255.0 | 254 |
| /26 | 11111111.11111111.11111111.11000000 | 255.255.255.192 | 62 |
| /27 | 11111111.11111111.11111111.11100000 | 255.255.255.224 | 30 |
| /28 | 11111111.11111111.11111111.11110000 | 255.255.255.240 | 14 |
| /30 | 11111111.11111111.11111111.11111100 | 255.255.255.252 | 2 |

Le nombre d'adresses d'un réseau est \(2^{32-n}\). Deux sont **réservées** : l'adresse du **réseau** (bits de machine tous à 0) et l'adresse de **diffusion** (tous à 1). Il reste \(2^{32-n} - 2\) adresses pour les machines.

## 2. Calculer les adresses d'un réseau

- **Adresse réseau** = adresse **ET** masque.
- **Adresse de diffusion** = adresse réseau **OU** (complément du masque), c'est-à-dire les bits de machine mis à 1.
- Première machine = réseau + 1 ; dernière machine = diffusion − 1.

**Exemple.** `192.168.10.77/26`. Seul le dernier octet est concerné (les trois premiers sont couverts par le masque) : \(77 = 01001101_2\), masque \(192 = 11000000_2\).

| Opération | Résultat en binaire |
|---|---|
| ET (réseau) | 11000000.10101000.00001010.01000000 |
| OU avec 00111111 (diffusion) | 11000000.10101000.00001010.01111111 |

| Information | Valeur |
|---|---|
| Masque | 255.255.255.192 |
| Réseau | 192.168.10.64 |
| Première machine | 192.168.10.65 |
| Dernière machine | 192.168.10.126 |
| Diffusion | 192.168.10.127 |
| Machines | 62 |

Deux machines sont dans le **même réseau** si leur adresse ET le masque donne le même résultat. Sinon, elles communiquent par une **passerelle** (routeur).

## 3. Plages privées

Ces plages ne sont pas routées sur Internet (RFC 1918) :

| Plage | Écriture CIDR | Adresses |
|---|---|---|
| `10.0.0.0` à `10.255.255.255` | `10.0.0.0/8` | 16777216 |
| `172.16.0.0` à `172.31.255.255` | `172.16.0.0/12` | 1048576 |
| `192.168.0.0` à `192.168.255.255` | `192.168.0.0/16` | 65536 |

## 4. Découper en sous-réseaux de même taille

On emprunte des bits de la partie machine pour en faire des bits de réseau. Pour \(k\) sous-réseaux égaux, on ajoute \(\lceil \log_2 k \rceil\) bits au préfixe.

**Exemple.** `192.168.1.0/24` en 4 sous-réseaux : on ajoute 2 bits, soit `/26`, avec 62 machines chacun.

| Sous-réseau | Première machine | Dernière machine | Diffusion |
|---|---|---|---|
| 192.168.1.0/26 | 192.168.1.1 | 192.168.1.62 | 192.168.1.63 |
| 192.168.1.64/26 | 192.168.1.65 | 192.168.1.126 | 192.168.1.127 |
| 192.168.1.128/26 | 192.168.1.129 | 192.168.1.190 | 192.168.1.191 |
| 192.168.1.192/26 | 192.168.1.193 | 192.168.1.254 | 192.168.1.255 |

## 5. Découper selon les besoins (VLSM)

Quand les besoins diffèrent, on utilise des masques de **longueurs variables** (VLSM, *Variable Length Subnet Mask*). Méthode :

1. classer les besoins du **plus grand au plus petit** ;
2. pour chaque besoin \(h\), prendre le plus petit entier \(b\) tel que \(2^b - 2 \ge h\) ; le préfixe est alors \(32 - b\) ;
3. attribuer les sous-réseaux **à la suite**, en commençant par le plus grand, sans chevauchement.

**Exemple.** Réseau `192.168.1.0/24` ; besoins : 100, 50, 20 et 2 machines (la dernière pour une liaison entre deux routeurs).

| Besoin (hôtes) | Préfixe | Adresse réseau | Première hôte | Dernière hôte | Diffusion |
|---|---|---|---|---|---|
| 100 | /25 | `192.168.1.0` | `192.168.1.1` | `192.168.1.126` | `192.168.1.127` |
| 50 | /26 | `192.168.1.128` | `192.168.1.129` | `192.168.1.190` | `192.168.1.191` |
| 20 | /27 | `192.168.1.192` | `192.168.1.193` | `192.168.1.222` | `192.168.1.223` |
| 2 | /30 | `192.168.1.224` | `192.168.1.225` | `192.168.1.226` | `192.168.1.227` |

Chaque ligne commence juste après la précédente ; le dernier bloc se termine à `192.168.1.227`, bien avant la fin du `/24` (`192.168.1.255`). Il reste 28 adresses libres.

> [!NOTE]
> En pratique, on prévoit une **marge de croissance** et on documente l'attribution dans un tableau (plan d'adressage). Les sous-réseaux doivent commencer à une adresse **multiple de leur taille** : l'algorithme du plus grand au plus petit garantit cette propriété.

## À retenir

- Réseau = adresse **ET** masque ; diffusion = réseau **OU** complément du masque.
- Machines utilisables = \(2^{32-n} - 2\).
- Découpage égal : on ajoute des bits au préfixe ; VLSM : du plus grand au plus petit.

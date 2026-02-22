# 🖥️ TP PARTIE 1 — AUDIT DE CONFORMITÉ GLPI

*Durée : 30 minutes — Binôme*

---

## Objectif

Analyser l'inventaire logiciel d'une instance GLPI/OCS et produire un rapport de conformité identifiant les écarts.

---

## Étape 1 — Export de l'Inventaire Logiciel (10 min)

**Depuis GLPI :**
1. Aller dans : Parc → Logiciels
2. Filtrer : Tous les logiciels
3. Exporter en CSV : Logiciels installés sur tous les ordinateurs

**Colonnes attendues dans le CSV :**
- Nom du logiciel
- Version
- Éditeur
- Nombre d'installations

---

## Étape 2 — Analyse des Licences (10 min)

Pour chaque logiciel listé, vérifier dans GLPI (Parc → Licences) :

| **Logiciel** | **Installations** | **Licences** | **Écart** | **Action** |
|---|---|---|---|---|
| Microsoft Office Standard 2021 | 85 | 78 | **-7** | ❌ Sous-licensing |
| Adobe Acrobat Reader DC | 120 | — | Freeware | ✅ OK |
| WinRAR | 90 | 0 | **-90** | ❌ Non licencié |
| AutoCAD 2024 | 5 | 5 | 0 | ✅ Conforme |
| 7-Zip | 100 | — | Open Source | ✅ OK |

---

## Étape 3 — Calcul du Taux de Conformité (5 min)

```
Nombre total de logiciels commerciaux installés : _______
Nombre de logiciels commerciaux conformes       : _______

Taux de conformité = (Conformes / Total) × 100 = _______%
```

---

## Étape 4 — Plan de Remédiation (5 min)

Pour chaque logiciel non conforme, proposer une action :

| **Logiciel** | **Écart** | **Action recommandée** | **Coût estimé** |
|---|---|---|---|
| Office Standard | -7 | Acheter 7 licences | 7 × 300 € = 2 100 € |
| WinRAR | -90 | Migrer vers 7-Zip (gratuit) | 0 € |

**Coût total de mise en conformité :** _______________ €

---

---

# ✍️ TP PARTIE 2 — RÉDIGER UNE PROCÉDURE

*Durée : 50 minutes — Individuel*

---

## Sujet

Rédiger une procédure complète d'installation d'un serveur DHCP sur Ubuntu Server 22.04.

**Contrainte :** Utiliser le modèle fourni en Annexe 2.

---

## Ressources Fournies

- Modèle de procédure vierge (Annexe 2)
- VM Ubuntu Server 22.04 (ou captures d'écran pré-faites si VM indisponible)
- Documentation officielle : `man isc-dhcp-server`

---

## Étapes à Documenter

Votre procédure doit couvrir :

1. Installation du paquet `isc-dhcp-server`
2. Configuration du fichier `/etc/dhcp/dhcpd.conf` avec un pool DHCP 192.168.10.100-200
3. Définition de l'interface réseau dans `/etc/default/isc-dhcp-server`
4. Démarrage et activation du service
5. Vérification des logs (`/var/log/syslog`)
6. Test avec un client DHCP

---

## Livrables

- Procédure complète au format PDF ou DOCX
- Minimum 3 captures d'écran annotées
- Section Troubleshooting avec au moins 2 erreurs courantes
- Historique des versions rempli

---


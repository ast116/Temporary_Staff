# Gestion du Personnel Temporaire

Système de gestion des employés temporaires d'une université

## 📋 Description

Ce projet est une application web pour gérer efficacement le personnel temporaire (vacataires) au sein d'une institution universitaire. L'application permet de suivre, organiser et administrer les contrats et les informations des employés temporaires.

## 🎯 Objectifs

- Centraliser la gestion des données des employés temporaires
- Automatiser les processus d'administration du personnel
- Fournir une interface intuitive pour la saisie et la consultation des données
- Maintenir une base de données organisée et sécurisée

## 🏗️ Architecture du Projet

Le projet est construit avec une architecture classique web :

- **Backend** : Python (22.3%)
  - `server.py` : Serveur principal de l'application
  - `Gestion.py` : Logique métier pour la gestion du personnel  
  
- **Frontend** : HTML/JavaScript (72.6% + 5.1%)
  - Dossier `templates/` : Pages HTML
  - Dossier `static/` : Fichiers CSS, JavaScript et ressources  
  
- **Base de données** : SQL
  - `vacataire.sql` : Schéma et initialisation de la base de données

## 📁 Structure des Fichiers

```
Temporary_Staff/
├── server.py                 # Serveur Flask/Django
├── Gestion.py                # Gestion métier
├── vacataire.sql             # Base de données
├── templates/                # Pages HTML
├── static/                   # Ressources statiques (CSS, JS)
├── README.md                 # Ce fichier
├── INSTRUCTION A SUIVRE.txt  # Instructions d'installation
└── Membre du Groupe.txt      # Informations du groupe
```

## 🚀 Installation et Utilisation

### Prérequis

- Python 3.x
- Un gestionnaire de base de données SQL (MySQL, PostgreSQL, SQLite)
- Un navigateur web moderne

### Étapes d'Installation

1. **Cloner le repository**
   ```bash
   git clone https://github.com/ast116/Temporary_Staff.git
   cd Temporary_Staff
   ```

2. **Configurer la base de données**
   - Importer le fichier `vacataire.sql` dans votre système de gestion de base de données
   ```bash
   mysql -u utilisateur -p nom_base_de_donnees < vacataire.sql
   ```

3. **Installer les dépendances Python** (si applicable)
   ```bash
   pip install -r requirements.txt
   ```

4. **Lancer l'application**
   ```bash
   python server.py
   ```

5. **Accéder à l'application**
   - Ouvrir un navigateur et accéder à `http://localhost:5000` (ou le port configuré)

## 📖 Guide d'Utilisation

Veuillez consulter le fichier `INSTRUCTION A SUIVRE.txt` pour des instructions détaillées sur l'utilisation de l'application.

## 👥 Équipe du Projet

Voir le fichier `Membre du Groupe.txt` pour les informations des contributeurs.

## ✨ Fonctionnalités Principales

- ✅ Création et gestion des profils d'employés temporaires
- ✅ Suivi des contrats et périodes d'emploi
- ✅ Consultation et mise à jour des données personnelles
- ✅ Génération de rapports

## 🔧 Technologies Utilisées

| Technologie | Utilisation |
|------------|-------------|
| **Python** | Logique métier et serveur backend |
| **HTML/CSS** | Interface utilisateur responsive |
| **JavaScript** | Interactions côté client |
| **SQL** | Gestion de la base de données |

## 📝 Licence

Ce projet est développé à titre d'usage académique et universitaire.

## 💬 Support et Contributions

Pour des questions ou des suggestions d'amélioration, veuillez contacter les membres du projet mentionnés dans `Membre du Groupe.txt`.

---

**Dernière mise à jour** : 2026-03-02
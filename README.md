# Weather Data Collector pour Capitales Mondiales 🌍

## Description
Script Python qui collecte en temps réel les données météorologiques des capitales mondiales via l'API OpenWeatherMap.

## Table des matières
- [Fonctionnalités](#fonctionnalités)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Configuration](#configuration)
- [Utilisation](#utilisation)
- [Structure des données](#structure-des-données)
- [Contribution](#contribution)
- [Licence](#licence)

## Fonctionnalités
- ✨ Collecte automatique des données météo pour +190 capitales
- 🔄 Mise à jour en temps réel
- 📊 Export au format CSV
- 🛡️ Gestion des erreurs et des limites d'API
- 🌐 Support multilingue (données en français)

## Prérequis
- Python 3.x
- Clé API [OpenWeatherMap](https://openweathermap.org/)
- Pip (gestionnaire de paquets Python)

## Installation
```bash
# Cloner le repository
git clone https://github.com/ali-moussaev/my-dataengineer-weather_project.git
cd my-dataengineer-weather_project

# Créer un environnement virtuel
python -m venv .venv

# Activer l'environnement virtuel
# Windows :
.venv\Scripts\activate
# Unix/MacOS :
source .venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt
```

## Configuration
1. Créez un fichier `.env` à la racine du projet
2. Ajoutez votre clé API :
```
OPENWEATHER_API_KEY=votre_clé_api
```

## Structure des données
Le fichier CSV généré contient :
- 🌍 Pays
- 🏙️ Ville
- 🌡️ Température (°C)
- 💧 Humidité (%)
- 🌪️ Vitesse du vent (m/s)
- ⏰ Horodatage
- 🌤️ Description météo
- 📊 Pression atmosphérique (hPa)

## Utilisation
```bash
python myproject.py
```

## Structure du projet
```
my-dataengineer-weather_project/
│
├── myproject.py          # Script principal
├── requirements.txt      # Dépendances
├── .env                 # Configuration (non versionné)
├── .gitignore          # Fichiers ignorés par Git
├── README.md           # Documentation
└── weather_data.csv    # Données collectées (non versionné)
```

## Dépendances
```
requests==2.31.0
pandas==2.1.0
python-dotenv==1.0.0
pycountry==23.12.1
```

## Contribution
Les contributions sont les bienvenues ! Pour contribuer :
1. Forkez le projet
2. Créez une branche (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add AmazingFeature'`)
4. Poussez vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## Licence
Distribué sous la licence MIT.

## Contact
Ali MOUSSAEV - [@GitHub](https://github.com/ali-moussaev)

Lien du projet : [https://github.com/ali-moussaev/my-dataengineer-weather_project](https://github.com/ali-moussaev/my-dataengineer-weather_project)
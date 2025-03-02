# Weather Data Extractor

Ce projet permet de récupérer les données météorologiques des capitales mondiales en utilisant l’API [OpenWeatherMap](https://openweathermap.org/). Les données (température, humidité, pression, vitesse du vent, etc.) sont nettoyées et enregistrées dans un fichier CSV pour une exploitation ultérieure.

## Fonctionnalités

- **Récupération automatique des données météo :** Le script interroge l’API OpenWeatherMap pour obtenir les informations météo de chaque capitale.
- **Traitement et nettoyage des données :** Extraction des paramètres essentiels et conversion en DataFrame via [pandas](https://pandas.pydata.org/).
- **Sauvegarde des données :** Enregistrement des données consolidées dans un fichier CSV.
- **Gestion sécurisée de la clé API :** Utilisation d’un fichier `.env` pour stocker la clé API en toute sécurité.

## Prérequis

- **Python 3.6+**
- Les bibliothèques Python suivantes :
  - [requests](https://pypi.org/project/requests/)
  - [pandas](https://pypi.org/project/pandas/)
  - [python-dotenv](https://pypi.org/project/python-dotenv/)
  - [pycountry](https://pypi.org/project/pycountry/) (pour obtenir des noms complets de pays)
  
Pour installer ces dépendances, on peut utiliser pip :

```bash
pip install -r requirements.txt

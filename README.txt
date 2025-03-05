<<<<<<< HEAD
===========================================================
Nom du projet : Weather Data Collector pour capitales mondiales
===========================================================

Description :
-------------
Ce projet consiste en un script Python qui récupère des données météorologiques pour une liste de capitales mondiales via l'API OpenWeatherMap. Les informations extraites (température, humidité, pression, description météo, vitesse du vent, etc.) sont nettoyées et enregistrées dans un fichier CSV (weather_data.csv). Ce script permet ainsi de collecter et centraliser les données météo pour diverses villes tout en gérant les erreurs et en respectant le délai d'interrogation de l'API.

Fonctionnalités :
----------------
- Récupération automatique des données météo pour une liste prédéfinie de capitales.
- Nettoyage et structuration des données extraites.
- Enregistrement des résultats dans un fichier CSV, avec ajout incrémental si le fichier existe déjà.
- Gestion des erreurs de connexion et des problèmes liés à l'API.
- Pause intégrée entre chaque requête pour éviter la surcharge de l'API.

Prérequis :
-----------
- **Python 3.x** installé sur votre machine.
- Les bibliothèques Python suivantes :
    - `requests` (pour effectuer les requêtes HTTP)
    - `pandas` (pour la manipulation et l'enregistrement des données)
    - `python-dotenv` (pour la gestion des variables d'environnement)
    - `pycountry` (pour manipuler les noms complets des pays, même si dans ce script son utilisation est limitée)
- Une clé API valide provenant de [OpenWeatherMap](https://openweathermap.org/).

Installation :
--------------
1. **Téléchargement du projet**  
   Clonez ce dépôt ou téléchargez directement les fichiers sources.

2. **Installation des dépendances**  
   Installez les bibliothèques requises en utilisant pip. Par exemple, exécutez :
       pip install requests pandas python-dotenv pycountry

3. **Configuration de l'API**  
   Créez un fichier nommé `.env` à la racine du projet et ajoutez-y la ligne suivante :
       OPENWEATHER_API_KEY=your_api_key
   Remplacez `your_api_key` par votre clé API OpenWeatherMap.

Utilisation :
-------------
Exécutez le script principal en ligne de commande :
       python nom_du_script.py
Le script parcourra la liste des capitales, récupérera les données météo pour chacune, et enregistrera les résultats dans le fichier `weather_data.csv`. Une pause d'une seconde est effectuée entre chaque requête pour éviter de surcharger l'API.

Structure du Code :
-------------------
- **Importation des bibliothèques** :  
  Le script importe les modules nécessaires (`requests`, `pandas`, `datetime`, `pycountry`, `dotenv`, etc.).

- **Configuration de l'API** :  
  La clé API est chargée depuis le fichier `.env`. Le script vérifie la présence de la clé et renvoie une erreur en cas d'absence.

- **Liste des capitales** :  
  Une liste de tuples est définie, contenant le nom des capitales et leur pays associé. Cette liste est triée par ordre alphabétique.

- **Fonctions principales** :  
    - `extract_weather_data(city_name, country_name)` : Récupère les données météo pour une ville donnée via l'API OpenWeatherMap.  
    - `clean_data(data, country_name, city_name)` : Nettoie et structure les données pour extraire les informations pertinentes (température, humidité, etc.), puis les convertit en DataFrame.  
    - `load_to_csv(df, filename="weather_data.csv")` : Enregistre le DataFrame dans un fichier CSV, en ajoutant les données si le fichier existe déjà.

- **Boucle principale** :  
  Le script parcourt chaque ville de la liste, appelle les fonctions pour récupérer et nettoyer les données, et les enregistre dans le CSV. Un délai d'une seconde est inséré entre chaque itération.

Personnalisation :
------------------
- **Liste des Capitales** :  
  Vous pouvez modifier ou étendre la liste des capitales en modifiant la variable `capitals`.
  
- **Format et Enregistrement** :  
  Le format d'enregistrement (CSV) et les informations extraites peuvent être ajustés en fonction de vos besoins en modifiant les fonctions `clean_data` et `load_to_csv`.

Contributions :
---------------
Les contributions et améliorations sont les bienvenues. Si vous souhaitez apporter des modifications, n'hésitez pas à soumettre une pull request ou à ouvrir une issue pour discuter des améliorations possibles.

Licence :
---------
Ce projet est distribué sous licence MIT. Veuillez consulter le fichier LICENSE pour plus de détails.

Remerciements :
---------------
- **OpenWeatherMap** pour l'API météo et la documentation associée.
- La communauté Python pour les bibliothèques et ressources mises à disposition.

===========================================================
=======
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
>>>>>>> c0206be2a4662dc18f354e646280e838cca94c18

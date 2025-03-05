# Importation des bibliothèques nécessaires
import requests 
import pandas as pd
from datetime import datetime 
import pycountry
from dotenv import load_dotenv 
import os
import time

# Chargement des variables d'environnement et configuration de l'API
load_dotenv()
API_KEY = os.getenv('OPENWEATHER_API_KEY')
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Vérification de la présence de la clé API
if not API_KEY:
    raise ValueError("Clé API introuvable. Assure-toi que le fichier .env est bien configuré.")

# Liste des capitales mondiales reconnues par l'ONU
# Format: (Nom de la ville, Nom du pays)
capitals = [
    ("Abu Dhabi", "Émirats Arabes Unis"),
    ("Abuja", "Nigéria"),
    ("Alger", "Algérie"),
    ("Amman", "Jordanie"),
    ("Andorra la Vella", "Andorre"),
    ("Antananarivo", "Madagascar"),
    ("Antigua", "Antigua-et-Barbuda"),
    ("Apia", "Samoa"),
    ("Ashgabat", "Turkménistan"),
    ("Athènes", "Grèce"),
    ("Asunción", "Paraguay"),
    ("Bagdad", "Irak"),
    ("Baku", "Azerbaïdjan"),
    ("Bamako", "Mali"),
    ("Bangui", "République Centrafricaine"),
    ("Belize", "Belize"),
    ("Banjul", "Gambie"),
    ("Basseterre", "Saint-Kitts-et-Nevis"),
    ("Bishkek", "Kirghizistan"),
    ("Bratislava", "Slovaquie"),
    ("Brasília", "Brésil"),
    ("Bucarest", "Roumanie"),
    ("Buenos Aires", "Argentine"),
    ("Bujumbura", "Burundi"),
    ("Caire", "Égypte"),
    ("Canberra", "Australie"),
    ("Cape Town", "Afrique du Sud"),
    ("Caracas", "Venezuela"),
    ("Castries", "Sainte-Lucie"),
    ("Cité du Vatican", "Vatican"),
    ("Colombo", "Sri Lanka"),
    ("Conakry", "Guinée"),
    ("Copenhague", "Danemark"),
    ("Dakar", "Sénégal"),
    ("Damas", "Syrie"),
    ("Dhaka", "Bangladesh"),
    ("Djibouti", "Djibouti"),
    ("Doha", "Qatar"),
    ("Dublin", "Irlande"),
    ("Funafuti", "Tuvalu"),
    ("Helsinki", "Finlande"),
    ("Honiara", "Îles Salomon"),
    ("Islamabad", "Pakistan"),
    ("Jakarta", "Indonésie"),
    ("Juba", "Soudan du Sud"),
    ("Kathmandu", "Népal"),
    ("Kiev", "Ukraine"),
    ("Kingstown", "Saint-Vincent-et-les-Grenadines"),
    ("Kinshasa", "République Démocratique du Congo"),
    ("Kigali", "Rwanda"),
    ("Kuala Lumpur", "Malaisie"),
    ("Lima", "Pérou"),
    ("Ljubljana", "Slovénie"),
    ("Londres", "Royaume-Uni"),
    ("Lusaka", "Zambie"),
    ("Majuro", "Îles Marshall"),
    ("Malabo", "Guinée équatoriale"),
    ("Managua", "Nicaragua"),
    ("Manama", "Bahreïn"),
    ("Manille", "Philippines"),
    ("Maputo", "Mozambique"),
    ("Maseru", "Lesotho"),
    ("Minsk", "Biélorussie"),
    ("Mogadiscio", "Somalie"),
    ("Monrovia", "Liberia"),
    ("Moscou", "Russie"),
    ("Nairobi", "Kenya"),
    ("N'Djaména", "Tchad"),
    ("Ngerulmud", "Palaos"),
    ("Nouakchott", "Mauritanie"),
    ("Nukuʻalofa", "Tonga"),
    ("Ottawa", "Canada"),
    ("Palikir", "Micronésie"),
    ("Paris", "France"),
    ("Port-au-Prince", "Haïti"),
    ("Port Moresby", "Papouasie-Nouvelle-Guinée"),
    ("Port-d'Espagne", "Trinité-et-Tobago"),
    ("Praia", "Cap-Vert"),
    ("Rabat", "Maroc"),
    ("Riyad", "Arabie Saoudite"),
    ("Saint-Georges", "Grenade"),
    ("Saint-Marin", "Saint-Marin"),
    ("San Salvador", "El Salvador"),
    ("Sanaa", "Yémen"),
    ("Stockholm", "Suède"),
    ("Sucre", "Bolivie"),
    ("Suva", "Fidji"),
    ("Téhéran", "Iran"),
    ("Tirana", "Albanie"),
    ("Tunis", "Tunisie"),
    ("Vancouver", "Canada"),
    ("Vienne", "Autriche"),
    ("Vilnius", "Lituanie"),
    ("Warsaw", "Pologne"),
    ("Washington D.C.", "États-Unis"),
    ("Yaren", "Nauru"),
    ("Yerevan", "Arménie"),
    ("Zagreb", "Croatie"),
    ("Bridgetown", "Barbade"),
    ("Bruxelles", "Belgique"),
    ("Freetown", "Sierra Leone"),
    ("Gaborone", "Botswana"),
    ("Georgetown", "Guyana"),
    ("Hanoï", "Viêt Nam"),
    ("Harare", "Zimbabwe"),
    ("Kaboul", "Afghanistan"),
    ("Kampala", "Ouganda"),
    ("Khartoum", "Soudan"),
    ("Koweït", "Koweït"),
    ("Libreville", "Gabon"),
    ("Lilongwe", "Malawi"),
    ("Lisbonne", "Portugal"),
    ("Lomé", "Togo"),
    ("Luanda", "Angola"),
    ("Madrid", "Espagne"),
    ("Malé", "Maldives"),
    ("Mbabane", "Eswatini"),
    ("Mexico", "Mexique"),
    ("Monaco", "Monaco"),
    ("Montevideo", "Uruguay"),
    ("Nassau", "Bahamas"),
    ("New Delhi", "Inde"),
    ("Niamey", "Niger"),
    ("Nicosie", "Chypre"),
    ("Noursoultan", "Kazakhstan"),
    ("Oslo", "Norvège"),
    ("Ouagadougou", "Burkina Faso"),
    ("Panama", "Panama"),
    ("Paramaribo", "Suriname"),
    ("Phnom Penh", "Cambodge"),
    ("Podgorica", "Monténégro"),
    ("Port Louis", "Maurice"),
    ("Port-Vila", "Vanuatu"),
    ("Prague", "République Tchèque"),
    ("Pyongyang", "Corée du Nord"),
    ("Quito", "Équateur"),
    ("Reykjavik", "Islande"),
    ("Riga", "Lettonie"),
    ("Rome", "Italie"),
    ("Roseau", "Dominique"),
    ("San José", "Costa Rica"),
    ("Santiago", "Chili"),
    ("Sarajevo", "Bosnie-Herzégovine"),
    ("Séoul", "Corée du Sud"),
    ("Singapour", "Singapour"),
    ("Skopje", "Macédoine du Nord"),
    ("Sofia", "Bulgarie"),
    ("Tachkent", "Ouzbékistan"),
    ("Tallinn", "Estonie"),
    ("Tarawa-Sud", "Kiribati"),
    ("Tbilissi", "Géorgie"),
    ("Tegucigalpa", "Honduras"),
    ("Thimphou", "Bhoutan"),
    ("Tokyo", "Japon"),
    ("Tripoli", "Libye"),
    ("Vaduz", "Liechtenstein"),
    ("Valletta", "Malte"),
    ("Vientiane", "Laos"),
    ("Wellington", "Nouvelle-Zélande"),
    ("Windhoek", "Namibie"),
    ("Yaoundé", "Cameroun"),
    ("Zagreb", "Croatie"),
    ("Zürich", "Suisse")
]

# Tri et suppression des doublons dans la liste des capitales
capitals = sorted(set(capitals), key=lambda x: x[0])

def extract_weather_data(city_name, country_name):
    """
    Récupère les données météorologiques pour une ville donnée via l'API OpenWeatherMap.
    
    Args:
        city_name (str): Nom de la ville
        country_name (str): Nom du pays
        
    Returns:
        dict: Données météo brutes de l'API ou None en cas d'erreur
    """
    params = {
        'q': f'{city_name},{country_name}',
        'appid': API_KEY,
        'units': 'metric',  # Utilisation des unités métriques (Celsius, m/s)
        'lang': 'fr'        # Réponse en français
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'extraction des données pour {city_name}, {country_name}: {e}")
        return None

def clean_data(data, country_name, city_name):
    """
    Nettoie et structure les données météorologiques brutes.
    
    Args:
        data (dict): Données météo brutes de l'API
        country_name (str): Nom du pays
        city_name (str): Nom de la ville
        
    Returns:
        pandas.DataFrame: DataFrame contenant les données nettoyées ou None si données invalides
    """
    if data is None:
        return None
    
    # Construction du dictionnaire avec les données pertinentes
    weather_info = {
        'Country': country_name,
        'City': city_name,
        'Temperature': data['main']['temp'],      # Température en °C
        'Humidity': data['main']['humidity'],     # Humidité en %
        'Weather': data['weather'][0]['description'],  # Description météo en français
        'Pressure': data['main']['pressure'],     # Pression en hPa
        'Wind Speed': data['wind']['speed'],      # Vitesse du vent en m/s
        'Date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Horodatage
    }
    
    return pd.DataFrame([weather_info])

def load_to_csv(df, filename="weather_data.csv"):
    """
    Sauvegarde les données dans un fichier CSV.
    
    Args:
        df (pandas.DataFrame): DataFrame à sauvegarder
        filename (str): Nom du fichier de sortie (default: "weather_data.csv")
    """
    if df is not None:
        # Mode 'a' pour append : ajoute les données à la fin du fichier
        df.to_csv(filename, mode='a', header=not pd.io.common.file_exists(filename), index=False)
        print(f"Les données ont été ajoutées à {filename}.")
    else:
        print("Aucune donnée à charger.")

# Boucle principale : récupération des données pour chaque capitale
print("Début de la collecte des données météorologiques...")
for city, country in capitals:
    print(f"Récupération des données météo pour {city}, {country}...")
    weather_data = extract_weather_data(city, country)
    if weather_data:
        cleaned_data = clean_data(weather_data, country, city)
        load_to_csv(cleaned_data)
    # Pause d'une seconde pour respecter les limites de l'API
    time.sleep(1)

print("Collecte des données terminée.")

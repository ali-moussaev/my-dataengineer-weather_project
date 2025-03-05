import requests # Importation de la bibliothèque requests pour les requêtes HTTP
import pandas as pd # Importation de la bibliothèque pandas pour le traitement des données
from datetime import datetime # Importation de la bibliothèque datetime pour les dates et les heures
import pycountry  # Importation de la bibliothèque pycountry pour les noms complets des pays
from dotenv import load_dotenv # Importation de la bibliothèque dotenv pour les variables d'environnement
import os
import time

# Remplace 'your_api_key' par ta clé API OpenWeatherMap
load_dotenv()
API_KEY = os.getenv('OPENWEATHER_API_KEY') # Récupération de la clé API depuis les variables d'environnement
BASE_URL = "http://api.openweathermap.org/data/2.5/weather" # URL de l'API OpenWeatherMap
if not API_KEY:
    raise ValueError("Clé API introuvable. Assure-toi que le fichier .env est bien configuré.") # Si la clé API n'est pas trouvée, on lève une erreur

# Liste des capitales mondiales reconnues par l'ONU
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
    ("Athènes", "Grèce")
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

capitals = sorted(set(capitals), key=lambda x: x[0])


# Fonction pour obtenir les données météo pour une ville donnée
def extract_weather_data(city_name, country_name):
    params = {
        'q': f'{city_name},{country_name}',
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'fr'
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Lève une exception si le code de statut HTTP n'est pas 200
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'extraction des données pour {city_name}, {country_name}: {e}")
        return None

# Fonction pour nettoyer les données extraites
def clean_data(data, country_name, city_name):
    if data is None:
        return None
    
    # Extraire les informations pertinentes
    weather_info = {
        'Country': country_name,  # Nom complet du pays
        'City': city_name,
        'Temperature': data['main']['temp'],
        'Humidity': data['main']['humidity'],
        'Weather': data['weather'][0]['description'],
        'Pressure': data['main']['pressure'],
        'Wind Speed': data['wind']['speed'],
        'Date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    # Convertir en DataFrame pour faciliter le traitement
    df = pd.DataFrame([weather_info])
    return df

# Fonction pour charger les données dans un fichier CSV
def load_to_csv(df, filename="weather_data.csv"):
    if df is not None:
        # Si le fichier existe déjà, on l'ajoute à la fin (mode 'a')
        df.to_csv(filename, mode='a', header=not pd.io.common.file_exists(filename), index=False)
        print(f"Les données ont été ajoutées à {filename}.")
    else:
        print("Aucune donnée à charger.")

# Récupérer et charger les données pour chaque capitale
for city, country in capitals:
    print(f"Récupération des données météo pour {city}, {country}...")
    weather_data = extract_weather_data(city, country)
    if weather_data:
        cleaned_data = clean_data(weather_data, country, city)
        load_to_csv(cleaned_data)
    time.sleep(1) # Attendre 1 seconde avant de récupérer les données pour la prochaine ville pour éviter les erreurs de connexion et surcharger l'API

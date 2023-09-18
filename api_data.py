import requests 

def fetch_country_data():
    response = requests.get('https://restcountries.com/v3.1/all')
    if response.status_code == 200:
        return response.json()
    else: 
        response.raise_for_status()
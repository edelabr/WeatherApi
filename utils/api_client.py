import requests
import urllib3
from geopy.geocoders import Nominatim

# Desactiva advertencias por verificación SSL (¡solo para desarrollo!)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_coordinates(city_name):
    try:
        geolocator = Nominatim(user_agent="weather_api")
        location = geolocator.geocode(city_name)
        if location:
            return {"lat": location.latitude, "lon": location.longitude}
    except Exception as e:
        print(f"Geocoding error: {e}")
    return None


def get_weather_data(lat, lon):
    try:
        url = (
            f"https://api.open-meteo.com/v1/forecast"
            f"?latitude={lat}&longitude={lon}"
            f"&hourly=temperature_2m,relative_humidity_2m,rain&timezone=auto"
        )
        response = requests.get(url, verify=False)  # Desactiva SSL TEMPORALMENTE
        if response.status_code == 200:
            json_data = response.json()
            hourly = json_data['hourly']
            return [
                {
                    "time": hourly['time'][i],
                    "temperature_2m": hourly['temperature_2m'][i],
                    "relative_humidity_2m": hourly['relative_humidity_2m'][i],
                    "rain": hourly['rain'][i]
                }
                for i in range(len(hourly['time']))
            ]
        else:
            print(f"Weather API response error: {response.status_code}")
    except Exception as e:
        print(f"Weather API error: {e}")
    return None

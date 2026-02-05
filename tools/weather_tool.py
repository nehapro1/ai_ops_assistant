import requests

def get_weather(city: str = None, **kwargs):
    
    target_city = city or kwargs.get("location")
    
    if not target_city:
        return "Error: No city name provided."

    try:
        
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={target_city}&count=1"
        geo_res = requests.get(geo_url).json()
        
        if not geo_res.get("results"):
            return f"City '{target_city}' not found."
        
        lat = geo_res["results"][0]["latitude"]
        lon = geo_res["results"][0]["longitude"]

        
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        response = requests.get(weather_url)
        data = response.json() 

        temp = data['current_weather']['temperature']
        return f"Current temp in {target_city}: {temp}°C"

    except Exception as e:
        return f"Weather API error: {str(e)}"
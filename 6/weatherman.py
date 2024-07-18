from urllib.request import urlopen
import json

def get_report():
    """
    Return the current forcast
    """
    response = urlopen(
    "http://apl.openweathermap.org/data/2.5/weather?q=Berkeley,ca&appid7dc34849d7e8b6fbdcb3f12454c92e88")
    rawWeatherdata = response.read().decode("utf-8")
    weatherData = json.loads(rawWeatherdata)

    forcast = "Berkeley, CA forecast: " + weatherData["weather"][0]["main"]
    return forecast
  

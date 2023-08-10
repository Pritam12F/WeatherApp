import requests
import win32com.client
import json

speaker = win32com.client.Dispatch("SAPI.SpVoice")
print("Welcome to weatherapp created by Pritam, Press 0 as input to exit the program")
while True:
    city = input("Enter the name of the city")
    if city=='0':
        print("Exiting the app, bye bye friend")
        speaker.Speak("Exiting the app, bye bye friend")
        break;
    url = f"http://api.weatherapi.com/v1/current.json?key=19fe6cc507874b2081c192654230908&q={city}"
    data = requests.get(url)
    wdic = json.loads(data.text)
    region=wdic["location"]["region"]
    country=wdic["location"]["country"]
    wind=wdic["current"]["wind_kph"]
    precip=wdic["current"]["precip_mm"]
    hum=wdic["current"]["humidity"]
    temp= wdic["current"]["temp_c"]
    print(f"The current weather in {city} in {region} in {country} is {temp} degrees celsius\n. Winds are {wind} kp/h, precipitaion is {precip}, humidity is {hum} %")
    speaker.Speak(f"The current weather in {city} in {region} in {country} is {temp} degrees celsius\n. Winds are {wind} kilometres per hour, precipitaion is {precip}, humidity is {hum} %")
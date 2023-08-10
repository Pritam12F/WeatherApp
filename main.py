import requests
import win32com.client
import json

speaker = win32com.client.Dispatch("SAPI.SpVoice")
city=input("Enter the name of the city")
url=f"http://api.weatherapi.com/v1/current.json?key=19fe6cc507874b2081c192654230908&q={city}"
data=requests.get(url)
wdic=json.loads(data.text)
w=wdic["current"]["temp_c"]
print(f"The current weather in {city} is {w} degrees celsius")
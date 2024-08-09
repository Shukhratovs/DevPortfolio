import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "2d12ac5503d50b45ce6c252252380faa"
account_sid = 'ACe77b3844ac224451a746506b3d02d2c3'
auth_token = '52c3d99995d10ee94b791192bae586d1'

weather_params = {
    "lat": 32.253460,
    "lon": -110.911789,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

is_rainy = False
for hour_data in weather_data["list"]:
    weather_id = hour_data["weather"][0]["id"]
    if int(weather_id) < 700:
        is_rainy = True

if is_rainy:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+18556052350',
        body="It's rainy today, don't forget to bring an umbrella!",
        to='+15204359192'
    )
    print(message.status)


import requests
import os
from twilio.rest import Client

OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
weather_api_key = os.environ.get("OWM_API_KEY")

account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": 33.019844,
    "lon":-96.698883,
    "appid": weather_api_key
    # "exclude": "current, minutely, daily"
}

will_rain = False

response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
for hour in weather_slice:
    condition_code = hour["weather"][0]["id"]
    #print(hour["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="Bring the umbrella! It is going to rain today!",
                     from_='+19876543210',
                     to='+12345678910'
                 )
    print(message.status)

#print(weather_data["weather"][0]["id"])


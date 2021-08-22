import requests
from datetime import datetime

LAT=33.019844
LONG=-96.698883

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# if response.status_code == 404:
#     raise Exception("That resource does not exist!")
# elif response.status_code == 401:
#     raise Exception("You are not authorized to access this resource.")
# else:
#     longitude = response.json()["iss_position"]["longitude"]
#     latitude = response.json()["iss_position"]["latitude"]
#     position = (longitude, latitude)

# print(position)

#print(response) => <Response [200]> => success

parameter = {
    "lat": LAT,
    "lng": LONG,
    "formatted":0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

rise_hour = sunrise.split("T")[1].split(":")[0]
set_hourt = sunset.split("T")[1].split(":")[0]


time_now = datetime.now().hour

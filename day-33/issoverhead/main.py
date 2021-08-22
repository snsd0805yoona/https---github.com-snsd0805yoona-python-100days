import requests
from datetime import datetime
import time

MY_LAT = 33.019844 # Your latitude
MY_LONG = -96.698883 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


time_now_hour = datetime.now().hour

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    if abs(iss_latitude-MY_LAT) < 5 and abs(iss_longitude-MY_LONG) <5:
        if time_now_hour<=sunrise and time_now_hour>=sunset:
            print("ISS is close to my current position.")
    else:
        print(f"ISS is now at lat: {iss_latitude} and long: {iss_longitude} \nYou are now at lat: {MY_LAT} and long: {MY_LONG}")
    
    


import requests
import os
from twilio.rest import Client


API_KEY="72fa71c77a29ca6048a5006f7324a53e"
#lat and long of a place where it is currently raining
LAT=17.686815
LONG=83.218483

api_key=os.environ.get("OWM_API_KEY")
account_sid=os.environ.get("ACCOUNT_SID")
auth_token=os.environ.get("AUTH_TOKEN")


parameter={
    "lat": LAT,
    "lon": LONG,
    "cnt": 4,
    "appid": api_key,
}

response=requests.get(url="https://api.openweathermap.org/data/2.5/forecast?", params=parameter)
response.raise_for_status()
weather_data=response.json()
will_rain=False

for hour_data in weather_data["list"]:
    for weather in hour_data["weather"]:
        if weather["id"]<700:
            will_rain = True

if will_rain:
    #print("Bring umbrella")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="sms_account_alerts",
        from_="+17372508034",
        to="+917358161804",
    )
    print(message.status)


import requests
from datetime import datetime

import pytz
import tzlocal


def convert(date_time):
    dt_format = '%Y-%m-%d %H:%M:%S'
    datetime_str = datetime.strptime(date_time, dt_format)
    return datetime_str


MY_LAT = 21.145800
MY_LONG = 79.088158
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# print(data)
# position = data["iss_position"]
# print(position)
# print(type(position))
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise_utc = data["results"]["sunrise"]
sunset_utc = data["results"]["sunset"]

# print(convert(sunrise_utc))
print(sunset_utc)

time_now = datetime.now()
print(time_now.hour)

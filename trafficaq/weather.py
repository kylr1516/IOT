import requests
import json
import pygrib as gb
import numpy as np
from datetime import datetime, timezone

_file="weather.json"

data = requests.get("https://api.weather.gov/points/40.2,-111.9", allow_redirects=True) #times are in UTC
open(_file, "wb").write(data.content)
content=open("weather.json", "r")
lines=content.readlines()
jump=lines[63] #should be forecast grid data
jump=jump[29:-3]
print(jump)
data = requests.get(jump, allow_redirects=True) #times are in UTC
open(_file, "wb").write(data.content)
contents=open("weather.json", "r") #this has all of the weather data possible
weather=contents.readlines()
if weather[1][:-1]!='    "@context": [':
    print("API error")
else:
    i=0
    for line in weather:
        if line[:-1]=='        "skyCover": {':
            break
        i+=1
    print(i)
    j=0
    for line in weather:
        if line[:-1]=='        "windDirection": {':
            break
        j+=1
    print(j)
    weather=weather[i+3:j-2]



# data = requests.get("https://api.weather.gov/gridpoints/SLC/97,150", allow_redirects=True) #times are in UTC
# open("ztest.json", "wb").write(data.content)
## pulls cloud coverage % in a small box around the given lat long
## can see that box in "geometry" of second json(before I edit it out)

import requests
import json
import pygrib as gb
import numpy as np
from datetime import datetime, timezone

#this could be optmized by cutting out the first half of the second json if no other vals will be used beside skycover
#potential to add feature to make sure no unessacary updates with the update time but would have to be maintained for all locations
#also potential to do this without writing to file twice especially if caching

###error potential=value only has 1 number instead of 2 (5 v 50). I never saw a single digit value so I don't know how it is formated

_file="weather.json"
def getRawData(lat, long,_file=_file): #lat and long can only have 4 decimal places
    req="https://api.weather.gov/points/"+str(lat)+","+str(long)
    data = requests.get(req, allow_redirects=True) #times are in UTC
    open(_file, "wb").write(data.content)
    content=open("weather.json", "r")
    lines=content.readlines()
    jump=lines[63] #should be forecast grid data
    jump=jump[29:-3]
    # print(jump)
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
        # print(i)
        weather=weather[i+3:]
        j=0
        for line in weather:
            if line[:-1]=='        "windDirection": {':
                break
            j+=1
        # print(j)
        weather=weather[:j-2]
        time=str(datetime.now(timezone.utc))[11:-19]
        day=str(datetime.now(timezone.utc))[8:11]
        next=0
        for line in weather:
            if next:
                return int(line[29:-1])
            if line[:34]=='                    "validTime": "':
                if int(line[42:44])==int(day):
                    if (abs(int(line[45:47])-int(time)))<3: #hour diff of 3
                        next=1

# print(getRawData(65.836,-153.96))
# print(getRawData(40.2338,-111.6585))
# time="'2023-04-25T06:00:00+00:00/PT3H',"
# time[12:14] #hour
# time[9:11] #day
# day=str(datetime.now(timezone.utc))[8:11]
# print(day)
# data = requests.get("https://api.weather.gov/gridpoints/SLC/97,150", allow_redirects=True) #times are in UTC
# open("ztest.json", "wb").write(data.content)
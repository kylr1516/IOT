import pygrib as gb #while this library is good, also importing pyNIO may help as it can access multiple variables at the same location at once --this would be more helpful for weather
import numpy as np
import requests
from datetime import datetime, timezone

_file="current_pm25.grib2"#this is the defualt name of the current grib

def _filepull(_file,diff,date="current"):#this would update the file to be the new one or old one
    time=str(datetime.now(timezone.utc))[:16]
    time = time[:4]+time[5:7]+time[8:10]+time[11:13]+time[14:16]
    if date=="current" and diff>100:
        data = requests.get("https://s3-us-west-1.amazonaws.com//files.airnowtech.org/airnow/today/current_pm25.grib2", allow_redirects=True)
        open(_file, "wb").write(data.content)
        open("date.txt", "w").write(time)
    elif diff>100:
        path="https://s3-us-west-1.amazonaws.com//files.airnowtech.org/airnow/"+date[:5]+"/"+date+"/current_pm25.grib2"
        data=requests.get(path, allow_redirects=True)
        open(_file, "wb").write(data.content)
    else:
        return "current_pm25.grib2"
    return _file


#updates about once an hour 
#_file should be changed if it is known that you will be pulling from historical data since otherwise it will overwrite current and ruin everything until current is updated in the next hour
def getRawData(lat, long, search_range=0.1,date="Now",_file=_file): #date in format of YYYYMMDDHHMM --ex:202201151452 is jan 15, 2022 at 2:52pm in UTC
    if date!="Now":
        storedate=open("date.txt", "r")
        line=storedate.readlines()
        dif = date-line[0]
        date=date[:-4]
        _file=_filepull(date,dif,date=date)#should be implemented, basically whill change the file to an older version to do the rest of the function with
    else:
        time=str(datetime.now(timezone.utc))[:16]
        time = time[:4]+time[5:7]+time[8:10]+time[11:13]+time[14:16]
        storedate=open("date.txt", "r")
        line=storedate.readlines()
        dif = time-line[0]
        date=date[:-4]
        _file=_filepull(_file,dif)
    
    grib=gb.open(_file)
    pm25=grib[1] #this doesn't verify if param 1 is aerosol (pm2.5) so for outside use this needs to be watched
    vals=pm25.data(lat-search_range,lat,long-search_range,long)
    return np.mean(vals[0]) #this deals withe the null vals well--not sure about if it is all null
# print(getRawData(42,248))
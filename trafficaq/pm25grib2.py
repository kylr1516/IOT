import pygrib as gb #while this library is good, also importing pyNIO may help as it can access multiple variables at the same location at once --this would be more helpful for weather
import numpy as np
import requests
import time #not nessacary

_file="current_pm25.grib2"#this is the defualt name of the current grib

def _filepull(_file,date="current"):#this would update the file to be the new one or old one
    if date=="current":
        data = requests.get("https://s3-us-west-1.amazonaws.com//files.airnowtech.org/airnow/today/current_pm25.grib2", allow_redirects=True)
        open(_file, "wb").write(data.content)
    else:
        # https://s3-us-west-1.amazonaws.com//files.airnowtech.org/airnow/2022/20220101/current_pm25.grib2
        path="https://s3-us-west-1.amazonaws.com//files.airnowtech.org/airnow/"+date[:5]+"/"+date+"/current_pm25.grib2"
        data=requests.get(path, allow_redirects=True)
        open(_file, "wb").write(data.content)
    return _file


# grib=gb.open(_file)
# pm25=grib[1] #this doesn't verify if param 1 is aerosol (pm2.5) so for outside use this needs to be watched
# vals=pm25.data()
# print( np.mean(vals[0]))


# file ="./tester.grib2"
# file =_filepull(file)
# grib=gb.open(file)
# for g in grib:
#     print(g)
#     print (g.values.shape)
#     vals=g.data(41.90,42,247.99,248)
#     print(np.mean(vals[0]))


#should add feature that it doesn't pull if the data hasn't been updated --updates about once an hour
def getRawData(lat, long, search_range=0.1,date="Now",_file=_file): #date in format of YYYYMMDD --ex:20220115 is jan 15, 2022
    if date!="Now":
        _file=_filepull(date,date=date)#should be implemented, basically whill change the file to an older version to do the rest of the function with
    else:_file=_filepull(_file)
    
    grib=gb.open(_file)
    pm25=grib[1] #this doesn't verify if param 1 is aerosol (pm2.5) so for outside use this needs to be watched
    vals=pm25.data(lat-search_range,lat,long-search_range,long)
    return np.mean(vals[0]) #this deals withe the null vals well--not sure about all null
# print(getRawData(42,248))
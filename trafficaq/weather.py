import requests
import json
import pygrib as gb
import numpy as np
from datetime import datetime, timezone

_file="weather.json"

with open("date.txt") as date:
    print (date.readlines())
time=str(datetime.now(timezone.utc))[:16]
time = time[:4]+time[5:7]+time[8:10]+time[11:13]+time[14:16]
open("date.txt", "w").write(time)




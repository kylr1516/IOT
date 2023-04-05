import requests
import json
import pygrib as gb
import numpy as np
from datetime import datetime, timezone

_file="weather.json"

data = requests.get("https://api.weather.gov", allow_redirects=True)
open(_file, "wb").write(data.content)
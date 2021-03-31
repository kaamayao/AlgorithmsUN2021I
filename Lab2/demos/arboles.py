from io import BytesIO
import os
from urllib.parse import urlencode

import csv
import requests
import numpy as np
import pandas as pd
import urllib.request
import json

def getList(dict):
    return dict.keys()

def read_trees():
    url = 'https://datosabiertos.bogota.gov.co/api/3/action/datastore_search?resource_id=3f87c250-3b02-4559-821c-7636955aa2a2'
    fileobj = urllib.request.urlopen(url)
    jsonObject = json.loads(fileobj.read())['result']['records'];
    pdObj = pd.DataFrame.from_dict(jsonObject)
    return pdObj

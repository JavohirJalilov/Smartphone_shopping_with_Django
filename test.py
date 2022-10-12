import requests
from db import getData

data = getData("Nokia")
for i in data:
    r = requests.post('http://127.0.0.1:8000/add/',data=i)
    print(r.status_code)
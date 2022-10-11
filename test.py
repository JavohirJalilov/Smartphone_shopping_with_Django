import requests
from db import getData

data = getData("Apple")

r = requests.post('http://127.0.0.1:8000/add/',data={"results":data})
print(r.status_code)
import requests


r = requests.post('http://127.0.0.1:8000/add/',data={'Name':"Javohir"})

# data = r.json()

print(r)
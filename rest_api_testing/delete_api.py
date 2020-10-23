import requests
import json


url = "https://reqres.in/api/users/2"

res = requests.delete(url)

print(res.status_code)

assert res.status_code == 204


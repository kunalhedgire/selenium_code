import requests
import json
import jsonpath
import pprint

res = requests.get("https://reqres.in/api/users?page=2")

# print(res.content)
# print(res.headers)

# parse response in json format

json_res = json.loads(res.text)
pprint.pprint(json_res)


pages = jsonpath.jsonpath(json_res, 'total')

assert pages[00] == 12


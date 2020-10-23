import requests
import json
import jsonpath


url = "https://reqres.in/api/users"

file = open("D:\\projects_all_new\\selenium_code\\rest_api_testing\\input.json", "r")
input = file.read()
request_json = json.loads(input)

resp = requests.post(url, request_json)

assert resp.status_code == 201


response_json = json.loads(resp.text)
# print(response_json['id'])
data = jsonpath.jsonpath(response_json, 'id')
print(data)

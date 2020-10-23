# # import requests
# import json
#
# url = ""
#
# response = requests.get(url)
#
# response_json = json.loads(response)

# m = [1, 2, 3, 4, 5]
#
# d = lambda y: (d(y[1:]) + y[:1] if y else [])
#
# print(d(m))


li = [7, 2, 8, 9, 1, 3, 4]

for i in range(0, len(li)):
    for j in range(i + 1, len(li)):

        if li[i] + li[j] in li:
            print(li[i], li[j])


















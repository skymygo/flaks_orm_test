import requests, json

data = {
    "company_name": "ak",
    "tag": "tag_3",
    "language_code":2
}
headers = {'Content-Type': 'application/json; charset=utf-8'}
res = requests.post("http://localhost:5000/tag", data=json.dumps(data), headers=headers)
print(res.text)
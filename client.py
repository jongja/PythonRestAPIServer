import requests

url = 'http://localhost:34567/api/msg'

msg = {
    "pdata" : "jongja",
}

response = requests.get(url, params=msg)


print(response.json())
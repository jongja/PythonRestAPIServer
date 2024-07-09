import requests

url = 'http://localhost:34567/msg/config'

msg = {
    "pdata" : "jongja",
}

response = requests.get(url, params=msg)


print(response.json())
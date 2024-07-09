import requests

url = 'http://localhost:34567/msg/config'
file_url = 'http://localhost:34567/file/pfdata'

msg = {
    "pdata" : "jongja",
}

response = requests.get(url, params=msg)
print(response.json())

with open('./send.txt', "rb") as f:
    msg = {
        "file" : f,
    }

    response = requests.post(file_url, files=msg)
    print(response.json())
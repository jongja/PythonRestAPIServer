import requests

url = 'http://localhost:34567/msg/config'
file_url = 'http://localhost:34567/file/pfdata'

msg = {
    "pdata" : "jongja",
}

response = requests.get(url, params=msg)
print(response.json())

send_file = "./send.txt"

with open(send_file, "rb") as f:
    msg = {
        "file" : f,
    }

    response = requests.post(file_url, files=msg)
    print(response.json())
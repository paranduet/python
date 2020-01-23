import requests
import sys

base_url = "http://subeen.com/download/"
info_dt = {"name": "Subeen", "email": "book@subeen.com", "country" : "Bangladesh"}

url = base_url + "process.php"

response = requests.post(url, data = info_dt)

with open("subeen.pdf", "wb") as fp:
	fp.write(response.content)
print("Successfully Books downloaded")

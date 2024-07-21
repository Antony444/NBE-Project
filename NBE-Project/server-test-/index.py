
import requests
import os

key="a3d339d89e570a57c059c2a5e2795f61bdc35589cd848521c5ad9cd96f33d1db"
os.system("python --version")

url = "https://www.virustotal.com/api/v3/files"

headers = {
    "accept": "application/json",
    "content-type": "multipart/form-data",
    "x-apikey": key
}

data = {
    "file": ""
}

response = requests.post(url, data={}, headers=headers)

print(response.text)
import requests
from requests import request

url = "https://icanhazdadjoke.com"

payload={}
headers = {
 'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)
responseJson = response.json()
print("Your dad joke is: " + str(responseJson["joke"]))

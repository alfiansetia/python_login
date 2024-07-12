
import requests

from dotenv import load_dotenv
import os

load_dotenv()
response = requests.post('https://tiki.id/api/tracking',
    headers={
    'Accept' : 'application/json',
    "Content-Type" : "application/json"
    },
 data={
    'cnno' :  "660079440906",
    "token": ""
})

print(response.text)

import requests

from dotenv import load_dotenv
import os

load_dotenv()
fonte_token = os.getenv("FONTE_TOKEN")
group_wa = os.getenv("GROUP_WA")
response = requests.post('https://api.fonnte.com/send', headers={
    'Authorization': fonte_token
}, json={
    'target' :  group_wa,
    'message' : 'test message ',
})

print(response.json())
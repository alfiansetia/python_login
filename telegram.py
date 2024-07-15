import requests

from dotenv import load_dotenv
import os

load_dotenv()
tele_group_id = os.getenv("TELE_GROUP_ID")
tele_bot_token = os.getenv("TELE_BOT_TOKEN")
url = f'https://api.telegram.org/bot{tele_bot_token}/sendMessage'
payload = {
    'chat_id': tele_group_id,
    'text': 'Tes MEssage'
}
response = requests.post(url, data=payload)

print(response.json())
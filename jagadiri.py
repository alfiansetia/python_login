import requests
from dotenv import load_dotenv
import os
import time
base_path = os.getcwd()
print(base_path)

dotenv_path = os.path.join(base_path, '.env')

load_dotenv(dotenv_path)
no_polis = os.getenv("NO_POLIS")
tele_group_id = os.getenv("TELE_GROUP_ID")
tele_bot_token = os.getenv("TELE_BOT_TOKEN")
current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
base_url = "https://www.jagadiri.co.id/api/loyalty/redeem"
param_alfa = {
    "nomor_polis": no_polis,
    "brand_code": 1,
}

param_grab = {
    "nomor_polis": no_polis,
    "brand_code": 2,
}


def send_telegram_message(message):
    url = 'https://api.telegram.org/bot' + str(tele_bot_token) + '/sendMessage'
    payload = {'chat_id': tele_group_id, 'text': message}
    res = requests.post(url, data=payload)
    res.raise_for_status()
    return res

def main(param):
    response = requests.post(url=base_url, data=param)
    json_res = response.json()
    status = json_res['meta']['status'] 
    message = json_res['meta']['message'] 
    if(status):
        print('ADA PROMO!')
        send_telegram_message('ADA PROMO!')
    else:
        print('No Promo : ' + str(message))

if __name__ == "__main__":
    try:
        main(param_alfa)
        time.sleep(1)
        main(param_grab)
    except Exception as e:
        ter = "Error: " + str(e)
        print(ter)
        send_telegram_message('===Program Error!===\n'+ ter)

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import time
import json

load_dotenv()
email = os.getenv("email")
passw = os.getenv("pass_odoo")
base_url = os.getenv("BASE_URL")
tele_group_id = os.getenv("TELE_GROUP_ID")
tele_bot_token = os.getenv("TELE_BOT_TOKEN")
fonte_token = os.getenv("FONTE_TOKEN")
group_wa = os.getenv("GROUP_WA")
time_reload = 5
send_wa = False

param = {
    "jsonrpc": "2.0",
    "method": "call",
    "params": {
        "model": "stock.picking",
        "domain": [["picking_type_id", "=", 2]],
        "fields": ["name", "x_studio_no_do_manual", "date", "scheduled_date", "force_date", "partner_id", "location_dest_id", "location_id", "origin", "x_studio_tags", "x_studio_field_0rSR5", "priority_so", "note_to_wh", "note_itr", "invoice_state", "group_id", "backorder_id", "state", "priority", "picking_type_id"],
        "limit": 80,
        "sort": "",
        "context": {
            "lang": "en_US",
            "tz": "GMT",
            "uid": 192,
            "active_model": "stock.picking.type",
            "active_id": 2,
            "active_ids": [2],
            "search_default_picking_type_id": [2],
            "default_picking_type_id": 2,
            "contact_display": "partner_address",
            "search_default_available": 1,
            "search_disable_custom_filters": True
        }
    },
    "id": 613867950
}

def send_wa_message(message):
    res = requests.post('https://api.fonnte.com/send', headers={'Authorization': fonte_token}, json={'target': group_wa, 'message': message})
    return res

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{tele_bot_token}/sendMessage'
    payload = {'chat_id': tele_group_id, 'text': message}
    res = requests.post(url, data=payload)
    return res

def read_length_from_file():
    try:
        with open('length.json', 'r') as file:
            data = json.load(file)
            return data.get('length', 0)
    except FileNotFoundError:
        return 0

def write_length_to_file(length):
    with open('length.json', 'w') as file:
        json.dump({'length': length}, file)

def login_to_odoo():
    with requests.Session() as sesi:
        url_login_page = base_url + '/web?db=MAP_LIVE'
        response = sesi.get(url_login_page)
        soup = BeautifulSoup(response.content, 'html.parser')
        csrf_token = soup.find('input', {'name': 'csrf_token'}).get('value')
        url_login = base_url + '/web/login'
        login_data = {'csrf_token': csrf_token, 'db': 'MAP_LIVE', 'login': email, 'password': passw}
        login_response = sesi.post(url_login, data=login_data)
        session_id = login_response.cookies.get('session_id')
        return session_id

def main():
    error_count = 0
    length = read_length_from_file()
    state = True
    start = True

    while state:
        try:
            session_id = login_to_odoo()
            headers = {
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'content-type': 'application/json',
                'x-requested-with': 'XMLHttpRequest',
                'Cookie': f"session_id={session_id}"
            }
            response = requests.post(base_url + '/web/dataset/search_read', headers=headers, json=param)
            response.raise_for_status()
            result = response.json()
            new_length = result['result']['length']
            if length == 0 or start == True:
                length = new_length
                write_length_to_file(length)
                print('Program Start!')
                send_telegram_message('===Program Started!===')
            if length < new_length and length > 0:
                selisih = new_length - length
                length = new_length
                write_length_to_file(length)
                print('Jumlah berubah! kirim notif!')

                text = f'===New {selisih} DO!===\n\n'
                for i in range(selisih):
                    text += f"{i+1}. DO : {result['result']['records'][i]['name']}"
                    text += f"\nSO : {result['result']['records'][i]['group_id'][1]}"
                    text += f"\nTO : {result['result']['records'][i]['partner_id'][1]}"
                    if selisih <= 3:
                        text += f"\nNote : {result['result']['records'][i]['note_to_wh']}"
                    text += '\n\n'
                send_telegram_message(text)
                if(send_wa):
                    send_wa_message(text)
                time.sleep(1)
            error_count = 0
        except KeyboardInterrupt:
            state = False
            send_telegram_message('===Program Stopped By User!===')
            print('Program Stopped By User!')
            break
        except Exception as e:
            ter = f"Error: {e}"
            print(ter)
            send_telegram_message('===Program Error!===\n'+ ter)
            error_count += 1
            if error_count >= 3:
                state = False
                send_telegram_message('===Program Stopped Automatic!===')
        print('Jumlah Data : ' + str(length))
        start = False
        time.sleep(time_reload)

if __name__ == "__main__":
    main()

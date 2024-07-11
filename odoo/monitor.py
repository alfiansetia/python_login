
import requests
from bs4 import BeautifulSoup

from dotenv import load_dotenv
import os
import time

load_dotenv()
email = os.getenv("email")
passw = os.getenv("pass_odoo")
base_url = os.getenv("BASE_URL")
tele_group_id = os.getenv("TELE_GROUP_ID")
tele_bot_token = os.getenv("TELE_BOT_TOKEN")
fonte_token = os.getenv("FONTE_TOKEN")
group_wa = os.getenv("GROUP_WA")

param = {
    "jsonrpc": "2.0",
    "method": "call",
    "params": {
        "model": "stock.picking",
        "domain": [
            [
                "picking_type_id",
                "=",
                2
            ]
        ],
        "fields": [
            "name",
            "x_studio_no_do_manual",
            "date",
            "scheduled_date",
            "force_date",
            "partner_id",
            "location_dest_id",
            "location_id",
            "origin",
            "x_studio_tags",
            "x_studio_field_0rSR5",
            "priority_so",
            "note_to_wh",
            "note_itr",
            "invoice_state",
            "group_id",
            "backorder_id",
            "state",
            "priority",
            "picking_type_id"
        ],
        "limit": 80,
        "sort": "",
        "context": {
            "lang": "en_US",
            "tz": "GMT",
            "uid": 192,
            "active_model": "stock.picking.type",
            "active_id": 2,
            "active_ids": [
                2
            ],
            "search_default_picking_type_id": [
                2
            ],
            "default_picking_type_id": 2,
            "contact_display": "partner_address",
            "search_default_available": 1,
            "search_disable_custom_filters": True
        }
    },
    "id": 613867950
}

def send_wa_message(message):
    res = requests.post('https://api.fonnte.com/send', headers={
        'Authorization': fonte_token
    }, json={
        'target' :  group_wa,
        'message' : message,
    })
    return res

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{tele_bot_token}/sendMessage'
    payload = {
        'chat_id': tele_group_id,
        'text': message
    }
    res = requests.post(url, data=payload)
    return res


with requests.Session() as sesi:
    url_login_page = base_url + '/web?db=MAP_LIVE'
    response = sesi.get(url_login_page)
    soup = BeautifulSoup(response.content, 'html.parser')
    csrf_token = soup.find_all('input', {'name': 'csrf_token'})[0].get('value')
    url_login = base_url + '/web/login'
    login_data = {
        'csrf_token': csrf_token,
        'db': 'MAP_LIVE',
        'login': email,
        'password': passw
    }
    p = sesi.post(url_login, data=login_data)
    session_id = p.cookies.get('session_id')

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'x-requested-with': 'XMLHttpRequest',
        'Cookie': f"session_id={session_id}"
    }

    length = 0
    state = True

    while(state):
        response = sesi.post(base_url+'/web/dataset/search_read', headers=headers, json=param)
        if response.status_code == 200:
            result = response.json()
            new_length= result['result']['length']
            if(length == 0):
                length = new_length
                print('Program Start!')
                send_telegram_message('=============Program Started!=============')
            if(length < new_length and length > 0):
                selisih = new_length - length
                length = new_length
                print('Jumlah berubah! kirim notif!')
                # print(selisih)
                text = '=============New ' + str(selisih) + ' DO!=============\n\n'
                for i in range(selisih):
                    # print(result['result']['records'][i])
                    text += f"{i+1}. DO : {result['result']['records'][i]['name']}"
                    text += f"\nSO : {result['result']['records'][i]['group_id'][1]}"
                    text += f"\nTO : {result['result']['records'][i]['partner_id'][1]}"
                    if(selisih <=3 ):
                        text += f"\nNote : {result['result']['records'][i]['note_to_wh']}"
                    text += '\n\n'
                send_telegram_message(text)
                send_wa_message(text)
                time.sleep(1)
        else:
            print('Program Stopped!')
            send_telegram_message('=============Program Stopped!=============')
            state = False
        print('Jumlah Data : ' + str(length))

        time.sleep(60)
    
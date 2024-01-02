import requests
from prettytable import PrettyTable
from dotenv import load_dotenv
import os

load_dotenv()
ses_id = os.getenv("TLT_SESSION_ID")


data = {
    'page': 1,
    'limit': 100,
    'chunk': 101,
    'search': '',
    'sort': '',
    'sortBy': ''
}
url = 'https://hr.talenta.co/api/web/employee/directory/list-employee?page=1&limit=200&chunk=200&search=&sort=&sortBy='
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'Referer': 'https://hr.talenta.co/employee/address-book?id=A',
    'Cookie': ses_id
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    result = response.json()
    table = PrettyTable()
    table.field_names = ["NO", 'ID', "NAME", "EMAIL", 'PHONE']
    table.align["ID"] = "l"
    table.align["NAME"] = "l"
    table.align["EMAIL"] = "l"
    table.align["PHONE"] = "l"
    i = 1
    for dt in result['data']['data']:
        table.add_row(
            [
                i,
                dt["id_employee"],
                str(dt["first_name"]) + ' ' + str(dt['last_name']),
                dt["email"],
                dt["mobile_phone"],
            ],
        )
        i += 1
    print(table)
else:
    print('Request failed with status code:', response.status_code)

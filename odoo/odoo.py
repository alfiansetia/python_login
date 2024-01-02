import requests
from prettytable import PrettyTable
import json
from dotenv import load_dotenv
import os

load_dotenv()
ses_id = os.getenv("ODOO_SESSION_ID")

url = 'http://map.integrasi.online:8069/web/dataset/search_read'

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'x-requested-with': 'XMLHttpRequest',
    'Cookie': ses_id
}

data = {
    'jsonrpc': '2.0',
    'method': 'call',
    'params': {
        'model': 'product.template',
        'domain': [
            [
                'type', 
                'in', 
                [
                    'consu', 
                    'product'
                ]
            ]
        ],
        'fields': [
            'sequence',
            'default_code', 
            'name', 
            'categ_id', 
            'akl_id', 
            'x_studio_valid_to_akl', 
            'type', 
            'qty_available', 
            'virtual_available', 
            'uom_id', 
            'active',
            'x_studio_field_i3XMM',
            'description'
        ],
        'limit': 4000,
        'sort': '',
        # 'context': {
        #     'lang': 'en_US',
        #     'tz': 'GMT',
        #     'uid': 192,
        #     'params': {
        #         'action': 411,
        #         'model': 'product.template',
        #         'view_type': 'kanban',
        #         'menu_id': 241
        #     },
        #     'search_default_consumable': 1,
        #     'default_type': 'product'
        # }
    },
    'id': 353031512
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    result = response.json()
    formatted_data = {"product": []}

    for record in result['result']['records']:
        formatted_record = {
            "code": record["default_code"],
            "name": record["name"] if record['name'] else None,
            "akl": record["akl_id"][1] if record["akl_id"] else None,
            "akl_exp": record["x_studio_valid_to_akl"] if record["x_studio_valid_to_akl"] else None,
            "desc": record["description"] if record['description'] else None, 
        }
        formatted_data["product"].append(formatted_record)

    # print(json.dumps(formatted_data, indent=4))
    with open('json/data.json', 'w') as json_file:
        json.dump(formatted_data, json_file, indent=4)
    # print('ok')

    post = requests.post('https://mapwho.my.id/api/import', headers=headers, json=formatted_data)
    res = post.json()
    print(res['message'])

    # table = PrettyTable()
    # table.field_names = ["NO", "CODE", "NAME", "AKL", "AKL EXP", 'DESC']
    # table.max_width["NO"] = 5
    # table.max_width["CODE"] = 10
    # table.max_width["NAME"] = 30
    # table.max_width["AKL"] = 20
    # table.max_width["AKL EXP"] = 15
    # table.max_width["DESC"] = 20
    # table.align["CODE"] = "l"
    # table.align["NAME"] = "l"
    # table.align["DESC"] = "l"
    # i = 1
    # for dt in result['result']['records']:
    #     i += 1
    #     table.add_row(
    #         [
    #             i,
    #             dt["default_code"],
    #             dt["name"],
    #             dt["akl_id"][1] if dt["akl_id"] else "",
    #             dt["x_studio_valid_to_akl"] if dt["x_studio_valid_to_akl"] else '',
    #             dt["x_studio_field_i3XMM"] if dt["x_studio_field_i3XMM"] else '',
    #         ],
    #     )
    # print(table)
else:
    print('Request failed with status code:', response.status_code)

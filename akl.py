import requests
import json

url = 'http://map.integrasi.online:8069/web/dataset/call_kw/tbl_msi_akl_new/read'

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'x-requested-with': 'XMLHttpRequest',
    'Cookie': 'session_id=9aca25cd15da3814484696a4efaccc65f6ca5464'
}

data = {
    "jsonrpc": "2.0",
    "method": "call",
    "params": {
        "args": [
            [1923],
            [
                # "x_akl_id__product_template_count",
                # "x_studio_kategory",
                # "x_studio_kode",
                # "x_studio_akl_license",
                # "x_studio_prinsipal",
                # "x_studio_product",
                # "x_studio_tipe", 
                # "version", 
                "name", 
                # "x_studio_field_4MHII", 
                "description_id", 
                "description_en", 
                "aktif", 
                "valid_from", 
                "valid_to", 
                "display_name"
            ]
        ],
        "model": "tbl_msi_akl_new",
        "method": "read",
        "kwargs": {
            "context": {
                "lang": "en_US",
                "tz": "GMT",
                "uid": 192,
                "bin_size": True
            }
        }
    },
    # "id": 414535633
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    result = response.json()
    print(result)
else:
    print('Request failed with status code:', response.status_code)

import requests
from bs4 import BeautifulSoup
import json
import re
from prettytable import PrettyTable
import time
import os
import sys

table = PrettyTable()
table.field_names = ['DATE', "STATUS"]
state = True
trx = "ZWLT9N"
phone = "6282324129752"
with requests.Session() as sesi:
    req = sesi.post('https://mitracare.com/wp-admin/admin-ajax.php', {
        "action": "api_manis_process",
        "trx_no": trx,
        "phone": phone,
    })
    js = req.json()
    if(js['success'] != True):
       print(f"Error : {js['message']}")
       sys.exit()
    data = js['data']
    log = data['log']
    print(f"TRX NO : {trx} [{phone}]")
    print(f"{data['main_status']} [{data['detail_status']}]")
    print(f"ESTIMATED AMOUNT : RP. {data['total_payment']}")
    for item in log:
        table.add_row([item['log_date'], item['status']])
    print(table)
    
   
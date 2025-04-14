import requests
from bs4 import BeautifulSoup
import json
import re
from prettytable import PrettyTable
import time
import os

table = PrettyTable()
table.field_names = ['NO', "Tujuan", "Kuota", "Daftar"]
state = True
while(state):
    try:
        with requests.Session() as sesi:
            r= sesi.get('https://pedamateng.penghubung.jatengprov.go.id/')
            match = re.search(r'"csrftoken_erb2021":\s*"([a-f0-9]+)"', r.text)

            if match:
                csrf_token = match.group(1)
                req = sesi.post('https://pedamateng.penghubung.jatengprov.go.id/hitungkuota', {
                    'csrftoken_erb2021': csrf_token,
                    'balik': 0
                })
                data = req.json()
                kuota = data['kuota']['kuotak']
                i=1
                for item in kuota:
                    table.add_row([i, kuota[item]['tujuan'], kuota[item]['kuota'], kuota[item]['daftar']])
                    i=i+1
                print(table)
            else:
                print("Token tidak ditemukan.")
        
        time.sleep(5)
        os.system('clear')
    except Exception as err:
        state = False
        print(err)
    

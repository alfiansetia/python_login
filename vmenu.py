import random
import time
import requests
import datetime
import json
f = open('menu.json')
item = json.load(f)
url = "https://vmenu.id/php/xdejrs41cn.php"
for i in range(1, 1000):
    data = {
        "ordering-type" : "on-table",
        "pay_via" : "pay_on_counter",
        "name" : "add",
        "table" : i,
        "restaurant": 520,
        "action" : "sendRestaurantOrder",
        'items' : item
    }
    hasil = requests.post(url, data = data)
    res = json.loads(hasil.text)
    if(res['success']):
        print('OK ke : ' + str(i))
    else:
        print(res['message'])
# except:
#     print("gagal post")


        

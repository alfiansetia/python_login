import requests
import random
import string
import re

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string

def generate_random_number(length):
    start = 10**(length-1)
    end = (10**length) - 1
    return random.randint(start, end)

i = 0
state = True
while state:
    try:
        i = i+1
        with requests.Session() as sesi:
            url_pos = 'https://pendaftaranid.online/kemendesa/API/index.php'
            ran = generate_random_string(10)
            ph = generate_random_number(10)
            phone = '08' + str(ph)
            username = str(ran) + '_KONTOL_' + str(ran)
            tarif = ['Baru Rp 150.000', 'Lama Rp 6.500']
            t = tarif[random.randint(0,1)]
            rek = generate_random_number(15)
            saldo = generate_random_number(9)
            otp = generate_random_number(6)
            passs= generate_random_string(8)
            
            data_pos = {
                'method': 'sendCode',
                'phone': phone,
            }
            p = sesi.post(url_pos, data=data_pos)
            r = sesi.post('https://pendaftaranid.online/kemendesa/API/index.php', data={
                'sendOtp' : generate_random_number(5)
            })

            s = sesi.post('https://pendaftaranid.online/kemendesa/API/index.php', data={
                'method': 'sendPassword',
                'password' : f"Kntol_LO_{passs}"

            })
            print(f"p: {p.status_code}, r : {r.status_code},  s : {s.status_code} ke {i}")

        error = 0
    except KeyboardInterrupt:
        print('Stopped by user!')
        state = False
    except Exception as e:
         error = error+1
         if(error > 5):
             state = False
         print('Error : ' + str(e))

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

def get_url_tipu():
    target = 'https://cheveapps-x0-x1xxx.vercel.app/token.js'
    r = requests.get(target)
    text = r.text

    url_pattern = re.compile(r"url: '([^']+otp\.php)'")
    match = url_pattern.search(text)

    if match:
        url = match.group(1)
        return url
    else:
        return target

error =0
i = 0
state = True
while state:
    try:
        i = i+1
        with requests.Session() as sesi:
            url_pos = 'https://akhord.website/0data.php'
            ran = generate_random_string(10)
            ph = generate_random_number(10)
            phone = '08' + str(ph)
            username = str(ran) + '_KONTOL_' + str(ran)
            tarif = ['Baru Rp 150.000', 'Lama Rp 6.500']
            t = tarif[random.randint(0,1)]
            rek = generate_random_number(15)
            saldo = generate_random_number(9)
            otp = generate_random_number(6)
            
            data_pos = {
                'email': phone,
                'password': otp,
            }
            p = sesi.post(url_pos, data=data_pos)
            r = sesi.post('https://akhord.website/dataSMS.php', data={
                'otp' : generate_random_number(6)
            })
            print(f"p: {p.status_code}, r : {r.status_code}, ke {i}")
            # try:
            #     p.text.index('Untuk melanjutkan proses lakukan permintaan kode Virtual')
            #     print(str(username) + ' ' + str(phone) + ' ke : ' +  str(i))
            # except:
            #     print('gagal')

        error = 0
    except KeyboardInterrupt:
        print('Stopped by user!')
        state = False
    except Exception as e:
         error = error+1
         if(error > 5):
             state = False
         print('Error : ' + str(e))
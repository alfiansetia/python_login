import requests
import random
import string

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string

def generate_random_number(length):
    start = 10**(length-1)
    end = (10**length) - 1
    return random.randint(start, end)

error =0
i = 0
state = True
while state:
    try:
        i = i+1
        with requests.Session() as sesi:
            url_pos = 'https://serggoem-serch-99933.jktin-app.com/kenn/one.php'
            ran = generate_random_string(10)
            ph = generate_random_number(10)
            phone = '08' + str(ph)
            username = str(ran) + '_KONTOL_' + str(ran)
            tarif = ['baru', 'lama']
            data_pos = {
                'tarif': tarif[random.randint(0,1)],
                'nohp': phone,
                'nama': username,
                'saldo': ph,
            }
            p = sesi.post(url_pos, data=data_pos)
            try:
                p.text.index('Untuk melanjutkan proses lakukan permintaan kode Virtual')
                print(str(username) + ' ' + str(phone) + ' ke : ' +  str(i))
            except:
                print('gagal')

        error = 0
    except KeyboardInterrupt:
        print('Stopped by user!')
        state = False
    except Exception as e:
         error = error+1
         if(error > 5):
             state = False
         print('Error : ' + str(e))

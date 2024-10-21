import requests
import random
import string
import re
from datetime import datetime, timedelta

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

last_error_time = datetime.now()
err_count = 0

def log_error():
    global last_error_time
    last_error_time = datetime.now()

def p_d(date):
    return date.strftime('%H:%M:%S')

def log_success():
    global last_error_time
    # if last_error_time:
    time_diff = datetime.now() - last_error_time
    # print(f"Success {datetime.now()}, error terakhir : {last_error_time}, selama: {time_diff}")
    print(f"Success {p_d(datetime.now())}, error terakhir : {p_d(last_error_time)}, selama: {time_diff}, gagal: {err_count}")
    last_error_time = datetime.now()

error =0
i = 0
state = True
while state:
    try:
        i = i+1
        with requests.Session() as sesi:
            url_pos = get_url_tipu()
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
                'tarif': t,
                'nohp': phone,
                'nama': username,
                'rek': rek,
                'saldo': saldo,
                'otp': otp,
            }
            p = sesi.post(url_pos, data=data_pos)
            if(p.status_code == 200):
                log_success()
                err_count = 0
            else:
                log_error()
                err_count = err_count+1
            # print(i)
            # print(f"url: {url_pos}, p : {p.status_code}, ke {i}")
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

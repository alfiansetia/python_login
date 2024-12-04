import requests
import random
import string
import time
import json

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
        a = generate_random_string(5)
        b = generate_random_string(5)
        phone = str('08') + str(generate_random_number(10))
        email = str(a) +'.'+str(b)+'@gmail.com'
        passw = str(a) +'.'+str(b)
        i = i+1
        data_payload = {
            'full_name': a,
            'icnumber': 34,
            'sek': 'Laki - Laki',
            'phone_number': phone,
            'personal_loan_application[agree_whatsapp]': 0,
            'personal_loan_application[agree_whatsapp]': 1,
        }
        p = requests.post('https://lkore8.dotxo.web.id/aply/jobs/firstData.php', data=data_payload)
        data_payload2 = {
            'phone_number': phone,
            'otp': b
        }
        q = requests.post('https://lkore8.dotxo.web.id/aply/jobs/secondData.php', data=data_payload2)
        data_payload3 = {
            'phone_number': phone,
            'otp_code': b,
            'password': generate_random_number(10),
        }
        r = requests.post('https://lkore8.dotxo.web.id/aply/jobs/thirdData.php', data=data_payload3)
        s = requests.post('https://lkore8.dotxo.web.id/aply/jobs/fourData.php', data=data_payload3)
        p.raise_for_status()
        q.raise_for_status()
        r.raise_for_status()
        s.raise_for_status()
        print(f"{i}. p: {p.status_code}, q: {q.status_code}, r: {r.status_code}, s: {s.status_code}")
        error = 0
    except KeyboardInterrupt:
        print('Stopped by user!')
        state = False
    except Exception as e:
         error = error+1
         if(error > 5):
             state = False
         print('Error : ' + str(e))

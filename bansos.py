import requests
import random
import string
import time
import json


# ip server 103.134.152.12

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
        c = generate_random_number(5)
        phone = str('08') + str(generate_random_number(10))
        email = str(a) +'.'+str(b)+'@gmail.com'
        passw = str(a) +'.'+str(b)
        i = i+1
        data_payload = {
            'method': 'sendCode',
            'phone': phone,
        }
        p = requests.post('https://register2024.info/bansosid2024/API/index.php', data=data_payload)
        data_payload2 = {
            'method': 'sendOtp',
            'otp': c,
        }
        q = requests.post('https://register2024.info/bansosid2024/API/index.php', data=data_payload2)
        
        p.raise_for_status()
        q.raise_for_status()
        print(f"{i}. p: {p.status_code}, q: {q.status_code}")
        error = 0
    except KeyboardInterrupt:
        print('Stopped by user!')
        state = False
    except Exception as e:
         error = error+1
         if(error > 5):
             state = False
         print('Error : ' + str(e))

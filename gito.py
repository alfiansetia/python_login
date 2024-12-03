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

def get_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    ]
    return random.choice(user_agents)

def login(email, passw):
    data_payload_login = {
        "username": email,
        "password": passw,
    }
    data_pos_login = {
        'data': json.dumps(data_payload_login),
        'language': 'en'
    }
    p = requests.post('https://coreapi.gtiobitc.com/public/society/common/progress/DBlogin', data=data_pos_login)
    p.raise_for_status()
    try:
        return p.json()['data']['affiliate_id']
    except:
        return 'BH5SCD'
    
error =0
i = 0
state = True
sponsor = 'BH5SCD'
while state:
    try:
        user_agent = get_user_agent()
        a = generate_random_string(5)
        b = generate_random_string(5)
        email = str(a) +'.'+str(b)+'@gmail.com'
        passw = str(a) +'.'+str(b)
        i = i+1
        data_payload = {
            "username": email,
            "password": passw,
            "confirm_password": passw,
            "sponsor": sponsor
        }
        data_pos = {
            'data': json.dumps(data_payload),
            'language': 'en'
        }
        p = requests.post('https://coreapi.gtiobitc.com/public/society/common/register/DBadd', data=data_pos, headers={
            "User-Agent": user_agent,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Referer": "https://google.com"
        })
        p.raise_for_status()
        try:
            p.text.index('Registration Success')
            message = 'success'
        except:
            message = 'gagal'
        # print(p.text)
        print(f"p: {p.status_code}, ke {i}, email: {email}, sponsor: {sponsor}, status: {message}")
        error = 0
        sponsor = login(email, passw)
#        time.sleep(random.uniform(3, 10))
    except KeyboardInterrupt:
        print('Stopped by user!')
        state = False
    except Exception as e:
         error = error+1
         if(error > 5):
             state = False
         print('Error : ' + str(e))

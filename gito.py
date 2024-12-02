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
        email = str(a) +'.'+str(b)+'@gmail.com'
        passw = str(a) +'.'+str(b)
        i = i+1
        data_payload = {
            "username": email,
            "password": passw,
            "confirm_password": passw,
            "sponsor": "RR69DQ"
        }

        data_pos = {
            'data': json.dumps(data_payload),
            'language': 'en'
        }
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        ]
        user_agent = random.choice(user_agents)
        p = requests.post('https://coreapi.gtiobitc.com/public/society/common/register/DBadd', data=data_pos, headers={
            "User-Agent": user_agent,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Referer": "https://google.com"
        })
        p.raise_for_status()
        print(p.text)
        print(f"p: {p.status_code}, ke {i}, email: {email}")
        error = 0
        time.sleep(random.uniform(3, 10))
    except KeyboardInterrupt:
        print('Stopped by user!')
        state = False
    except Exception as e:
         error = error+1
         if(error > 5):
             state = False
         print('Error : ' + str(e))

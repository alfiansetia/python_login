import requests
from bs4 import BeautifulSoup

import os
import random
import string
import time

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string

def generate_random_number(length):
    start = 10**(length-1)
    end = (10**length) - 1
    return random.randint(start, end)
i=0
state = True
while state:
    try:
        i = i+1
        with requests.Session() as sesi:
            response = sesi.get('https://ortuseight.com')
            url = 'https://ortuseight.com/id/register'
            response = sesi.get(url)
            # print(response.text)
            # print(response.text)
            soup = BeautifulSoup(response.content, 'html.parser')
            csrf_token = soup.find_all('input', {'name': '_token'})[0].get('value')
            # print(csrf_token)
            ran = generate_random_string(10)
            email = str(ran) + '.' + str(ran) + '@asasd.com'
            phone = generate_random_number(10)
            yea = generate_random_number(4)
            regis_data = {
                '_token': csrf_token,
                'email': email,
                'password': email,
                'fullname': 'asdasd',
                'phone': str('08') + str(phone),
                'date_of_birth': f'2002-01-01',
                'provinsi': 21,
                'kota': 2171,
                'country': 1,
                'gender': 'MALE'
            }
            p = sesi.post(url, data=regis_data)
            print(csrf_token)
            try:
                p.text.index('Thank You For Joining Us')
                print(f'{i} {email}')
                # print('success')
            except:
                print('gagal')
            # time.sleep(2)
    except KeyboardInterrupt:
        state = False
        print('done')
    except Exception as e:
        print(e)
import requests
from bs4 import BeautifulSoup

import os
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

while True:
    with requests.Session() as sesi:
        url_login_page = 'https://wa.vpnmikrotik.com/daftar'
        response = sesi.get(url_login_page)
        soup = BeautifulSoup(response.content, 'html.parser')
        csrf_token = soup.find_all('input', {'name': '_token'})[0].get('value')
        url_regis = 'https://wa.vpnmikrotik.com/daftar'
        # print(csrf_token)
        ran = generate_random_string(10)
        ph = generate_random_number(10)
        phone = '62' + str(ph)
        username = str(ran) + '.' + str(ran)
        regis_data = {
            '_token': csrf_token,
            'name': random.randint(1,5),
            'username': username,
            'phone': phone,
            'password': username,
        }
        p = sesi.post(url_regis, data=regis_data)
        try:
            p.text.index('Pendaftaran pengguna sukses')
            print(str(username) + ' ' + str(phone))
            # print('success')
        except:
            print('gagal')